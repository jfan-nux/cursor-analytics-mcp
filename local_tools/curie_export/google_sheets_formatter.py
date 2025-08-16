#!/usr/bin/env python3
"""
Google Sheets Formatter for Experiment Results

This module provides utilities to export experiment results to Google Sheets
with professional formatting, charts, and automated layout.
"""

import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any, Union
import logging
import time
from collections import deque
import random

# Google Sheets API imports
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from gspread.utils import ValueInputOption
    from gspread_formatting import *
    SHEETS_AVAILABLE = True
except ImportError:
    SHEETS_AVAILABLE = False
    logging.warning("Google Sheets libraries not available. Install with: pip install gspread oauth2client gspread-formatting")

from utils.logger import get_logger
from .config import get_default_share_email

logger = get_logger(__name__)


class ExponentialBackoffHandler:
    """
    Implements exponential backoff as recommended by Google Sheets API documentation.
    https://developers.google.com/workspace/sheets/api/limits
    """

    def __init__(self, max_retries: int = 10, max_backoff: int = 64):
        self.max_retries = max_retries
        self.max_backoff = max_backoff  # Maximum backoff in seconds

    def execute_with_backoff(self, func, *args, **kwargs):
        """
        Execute a function with exponential backoff on rate limit errors.

        Args:
            func: The function to execute
            *args, **kwargs: Arguments to pass to the function

        Returns:
            The result of the function call

        Raises:
            Exception: If max retries exceeded or non-rate-limit error
        """
        n = 0  # Retry counter

        while n < self.max_retries:
            try:
                return func(*args, **kwargs)
            except gspread.exceptions.APIError as e:
                # Check if it's a rate limit error (429)
                if hasattr(e, 'response') and e.response.status_code == 429:
                    # Calculate wait time: min(((2^n)+random_number_milliseconds), maximum_backoff)
                    random_milliseconds = random.randint(0, 1000) / 1000.0
                    wait_time = min((2 ** n) + random_milliseconds, self.max_backoff)

                    logger.warning(f"Rate limit hit (429). Retry {n+1}/{self.max_retries}. Waiting {wait_time:.2f}s...")
                    time.sleep(wait_time)
                    n += 1
                else:
                    # Not a rate limit error, re-raise
                    raise
            except Exception as e:
                # Not an API error, re-raise
                raise

        raise Exception(f"Max retries ({self.max_retries}) exceeded. Unable to complete request due to rate limiting.")


class AdaptiveRateLimiter:
    """
    Adaptive rate limiter that tracks API calls and implements proactive rate limiting.
    Google Sheets Write API: 60 requests per 60 seconds per user per project.

    This implementation:
    1. Uses the correct rate limit (60/60)
    2. Implements a sliding window for accurate tracking
    3. Provides buffer to avoid hitting limits
    4. Works in conjunction with ExponentialBackoffHandler for reliability
    """

    def __init__(self, max_requests: int = 60, window_seconds: int = 60, safety_buffer: float = 0.9):
        """
        Initialize the rate limiter.

        Args:
            max_requests: Maximum requests allowed (default: 60)
            window_seconds: Time window in seconds (default: 60)
            safety_buffer: Use only this fraction of the limit to avoid edge cases (default: 0.9 = 90%)
        """
        self.max_requests = int(max_requests * safety_buffer)  # Apply safety buffer
        self.window_seconds = window_seconds
        self.calls = deque()  # Store timestamps of API calls
        self.total_calls = 0
        self.backoff_handler = ExponentialBackoffHandler()

        logger.info(f"Rate limiter initialized: {self.max_requests} requests per {self.window_seconds}s (with {safety_buffer*100:.0f}% safety buffer)")

    def can_make_request(self) -> bool:
        """Check if we can make another API request."""
        now = time.time()

        # Remove calls outside the sliding window
        while self.calls and now - self.calls[0] > self.window_seconds:
            self.calls.popleft()

        return len(self.calls) < self.max_requests

    def record_request(self):
        """Record an API request."""
        now = time.time()
        self.calls.append(now)
        self.total_calls += 1

    def wait_if_needed(self) -> float:
        """Wait if needed to avoid hitting rate limit."""
        if self.can_make_request():
            return 0.0

        # Calculate when we can make the next request
        now = time.time()
        if self.calls:
            oldest_call = self.calls[0]
            # Add small buffer to ensure we're past the window
            wait_time = (oldest_call + self.window_seconds) - now + 0.5

            if wait_time > 0:
                logger.info(f"⏰ Proactive rate limit: {len(self.calls)}/{self.max_requests} requests used. Waiting {wait_time:.1f}s...")
                time.sleep(wait_time)
                return wait_time
        return 0.0

    def get_available_requests(self) -> int:
        """Get number of requests available in current window."""
        now = time.time()
        while self.calls and now - self.calls[0] > self.window_seconds:
            self.calls.popleft()
        return max(0, self.max_requests - len(self.calls))

    def reset_to_next_window(self):
        """Reset and wait until we have more capacity."""
        if not self.calls:
            return

        now = time.time()
        # Wait until we have at least 10% capacity
        target_capacity = int(self.max_requests * 0.1)

        while self.get_available_requests() < target_capacity:
            oldest_call = self.calls[0] if self.calls else now
            wait_time = (oldest_call + self.window_seconds) - now + 1

            if wait_time > 0:
                logger.info(f"🔄 Waiting for capacity. Current: {self.get_available_requests()}/{self.max_requests}. Wait: {wait_time:.1f}s")
                time.sleep(min(wait_time, 5))  # Sleep in 5s increments max
                now = time.time()

                # Clean old calls
                while self.calls and now - self.calls[0] > self.window_seconds:
                    self.calls.popleft()
            else:
                break

    def execute_with_rate_limit(self, func, *args, **kwargs):
        """
        Execute a function with both proactive rate limiting and reactive backoff.

        This combines:
        1. Proactive waiting to avoid hitting limits
        2. Exponential backoff if we still hit a 429 error
        """
        # First, wait if we're near the rate limit
        self.wait_if_needed()

        # Then execute with exponential backoff for safety
        result = self.backoff_handler.execute_with_backoff(func, *args, **kwargs)

        # Record the successful request
        self.record_request()

        return result


class ExperimentSheetsFormatter:
    """
    A comprehensive utility for exporting experiment results to Google Sheets
    with professional formatting and automated layout.
    """

    def __init__(self, credentials_path: Optional[str] = None, auto_share_email: Optional[str] = None):
        """
        Initialize the Google Sheets formatter.

        Args:
            credentials_path: Path to Google Sheets service account credentials JSON file
            auto_share_email: Email address to automatically share created sheets with
        """
        if not SHEETS_AVAILABLE:
            raise ImportError("Google Sheets libraries not available. Install with: pip install gspread oauth2client gspread-formatting")

        # Only find credentials if not explicitly set to None (OAuth case)
        if credentials_path is None:
            self.credentials_path = None
        else:
            self.credentials_path = credentials_path or self._find_credentials()

        self.auto_share_email = auto_share_email or get_default_share_email()
        self.client = None
        self.workbook = None
        self.rate_limiter = AdaptiveRateLimiter()
        self._authenticate()

    def _find_credentials(self) -> str:
        """Find Google Sheets credentials file."""
        possible_paths = [
            "../credentials/google_sheets_credentials.json",  # Moved to parent directory
            "credentials/google_sheets_credentials.json",     # Fallback for current directory
            "utils/google_sheets_credentials.json",
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config/google_oauth_credentials.json"))
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        raise FileNotFoundError(
            "Google Sheets credentials file not found. Please place it at one of: " +
            ", ".join(possible_paths)
        )

    def _authenticate(self):
        """Authenticate with Google Sheets API."""
        # Skip authentication if no credentials path (OAuth will be set externally)
        if not self.credentials_path:
            logger.info("Skipping service account authentication (OAuth client will be provided)")
            return

        try:
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]

            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.credentials_path, scope
            )
            self.client = gspread.authorize(credentials)
            logger.info("Successfully authenticated with Google Sheets API")

        except Exception as e:
            logger.error(f"Failed to authenticate with Google Sheets: {e}")
            raise

    def create_or_open_sheet(self, sheet_name: str, folder_id: Optional[str] = None) -> gspread.Spreadsheet:
        """
        Create a new Google Sheet or open existing one.

        Args:
            sheet_name: Name of the spreadsheet
            folder_id: Optional Google Drive folder ID to create the sheet in

        Returns:
            Google Spreadsheet object
        """
        # Get folder ID from environment if not provided
        if not folder_id:
            folder_id = os.environ.get('GOOGLE_DRIVE_FOLDER_ID')
            if folder_id:
                logger.info(f"📁 Using folder ID from environment: {folder_id}")

        try:
            # Try to open existing sheet
            self.workbook = self.client.open(sheet_name)
            logger.info(f"Opened existing sheet: {sheet_name}")
        except gspread.SpreadsheetNotFound:
            # Create new sheet - specify folder_id during creation
            if folder_id:
                self.workbook = self.client.create(sheet_name, folder_id=folder_id)
                logger.info(f"Created new sheet in folder: {sheet_name}")
            else:
                self.workbook = self.client.create(sheet_name)
                logger.info(f"Created new sheet: {sheet_name}")

            # Automatically share with specified email
            self._auto_share_sheet(self.workbook)

        return self.workbook

    def _auto_share_sheet(self, workbook: gspread.Spreadsheet):
        """Automatically share the sheet with the specified email."""
        # Skip sharing if using OAuth (user already owns the sheet)
        if hasattr(self.client, 'auth') and hasattr(self.client.auth, 'token'):
            logger.info("Using OAuth - sheet owned by authenticated user, no sharing needed")
            return

        if self.auto_share_email:
            try:
                workbook.share(self.auto_share_email, perm_type='user', role='writer')
                logger.info(f"Automatically shared sheet with {self.auto_share_email}")
            except Exception as e:
                logger.warning(f"Could not auto-share sheet with {self.auto_share_email}: {e}")

    def _clean_dataframe_for_export(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean DataFrame to ensure all values are JSON-safe for Google Sheets API.
        Handles infinity, NaN, and other problematic values.
        """
        logger.info("🧹 Cleaning DataFrame for JSON safety...")
        df_clean = df.copy()

        # Track cleaning statistics
        cleaning_stats = {
            'inf_replaced': 0,
            'nan_replaced': 0,
            'large_values_capped': 0,
            'json_unsafe_values': 0,
            'zero_division_fixed': 0
        }

        # First pass: Handle special cases in relative_impact and similar columns
        special_columns = ['relative_impact', 'relative_impact_ci_lower', 'relative_impact_ci_upper',
                          'absolute_impact', 'absolute_impact_ci_lower', 'absolute_impact_ci_upper',
                          'metric_impact_relative', 'metric_impact_absolute']

        for col in special_columns:
            if col in df_clean.columns:
                # Check for cases where both control and treatment are 0
                if 'control_value' in df_clean.columns and 'treatment_value' in df_clean.columns:
                    zero_mask = (df_clean['control_value'] == 0) & (df_clean['treatment_value'] == 0)
                    if zero_mask.any() and col in ['relative_impact', 'relative_impact_ci_lower', 'relative_impact_ci_upper']:
                        # For relative effects, 0/0 should be 0 (no relative change)
                        cleaning_stats['zero_division_fixed'] += zero_mask.sum()
                        df_clean.loc[zero_mask, col] = 0.0
                        logger.info(f"Fixed {zero_mask.sum()} zero division cases in {col}")

        # First, convert object columns that contain Decimal values to float64
        # This ensures they're properly treated as numeric columns throughout
        from decimal import Decimal
        for col in df_clean.select_dtypes(include=['object']).columns:
            # Check if column contains Decimal values
            sample_values = df_clean[col].dropna().head(10)
            if sample_values.empty:
                continue

            # Check if all non-null values are Decimal
            if all(isinstance(val, Decimal) for val in sample_values):
                logger.info(f"Converting Decimal column '{col}' to float64")
                try:
                    # Convert to float64 and ensure dtype is updated
                    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce').astype('float64')
                    logger.debug(f"Successfully converted '{col}' from object to {df_clean[col].dtype}")
                except Exception as e:
                    logger.warning(f"Could not convert {col} to float64: {e}")

        # Handle numeric columns
        for col in df_clean.select_dtypes(include=[np.number]).columns:
            # Convert column to float64 to ensure consistent handling
            try:
                df_clean[col] = df_clean[col].astype('float64')
            except:
                pass  # If conversion fails, keep original dtype

            # Count problematic values
            inf_mask = np.isinf(df_clean[col])
            nan_mask = df_clean[col].isna()

            cleaning_stats['inf_replaced'] += inf_mask.sum()
            cleaning_stats['nan_replaced'] += nan_mask.sum()

            # Replace infinity with None (JSON null)
            if inf_mask.any():
                df_clean.loc[inf_mask, col] = None
                logger.debug(f"Replaced {inf_mask.sum()} infinity values in {col}")

            # Replace NaN with None (JSON null) - more explicit than pandas default
            if nan_mask.any():
                df_clean.loc[nan_mask, col] = None
                logger.debug(f"Replaced {nan_mask.sum()} NaN values in {col}")

            # Check for extremely large values that might cause issues
            if df_clean[col].dtype in ['float64', 'float32']:
                non_null_mask = df_clean[col].notnull()
                if non_null_mask.any():
                    # Use a more conservative max value for JSON safety
                    max_safe_value = 1e15  # Conservative limit

                    # Check both positive and negative large values
                    large_positive_mask = (df_clean[col] > max_safe_value) & non_null_mask
                    large_negative_mask = (df_clean[col] < -max_safe_value) & non_null_mask
                    large_mask = large_positive_mask | large_negative_mask

                    if large_mask.any():
                        cleaning_stats['large_values_capped'] += large_mask.sum()
                        logger.warning(f"Capping {large_mask.sum()} extremely large values in {col}")
                        # Cap values instead of converting to string
                        df_clean.loc[large_positive_mask, col] = max_safe_value
                        df_clean.loc[large_negative_mask, col] = -max_safe_value

        # Handle object/string columns - replace NaN with empty string
        for col in df_clean.select_dtypes(include=['object']).columns:
            nan_count = df_clean[col].isna().sum()
            if nan_count > 0:
                cleaning_stats['nan_replaced'] += nan_count
                df_clean[col] = df_clean[col].fillna('')

        # NEW: Special handling for multi-treatment format
        # Control rows shouldn't have relative_impact or p_value values
        if 'variant_name' in df_clean.columns and 'relative_impact' in df_clean.columns:
            # Identify control variant by checking which variant has NaN/None values for relative_impact
            # Group by variant and check null percentage
            control_mask = df_clean['relative_impact'].isna() | (df_clean['relative_impact'] == '')

            # Find which variant(s) are control
            control_variants = df_clean[control_mask]['variant_name'].unique() if control_mask.any() else []
            if len(control_variants) > 0:
                logger.info(f"Detected control variant(s) based on empty relative_impact: {', '.join(control_variants)}")

                # For control rows, ensure these columns are None/NaN (not 0)
                control_mask = df_clean['variant_name'].isin(control_variants)
                if 'relative_impact' in df_clean.columns:
                    df_clean.loc[control_mask, 'relative_impact'] = None
                if 'p_value' in df_clean.columns:
                    df_clean.loc[control_mask, 'p_value'] = None
                if 'absolute_impact' in df_clean.columns:
                    df_clean.loc[control_mask, 'absolute_impact'] = None

                logger.info(f"Set {control_mask.sum()} control rows' relative_impact, absolute_impact and p_value to None (preserving numeric dtype)")

        # Final validation pass - ensure all values are JSON serializable
        problematic_cells = []
        for col in df_clean.columns:
            for idx in df_clean.index:
                value = df_clean.at[idx, col]
                if value is not None and pd.notna(value):
                    try:
                        # Test JSON serialization
                        json.dumps(value)
                    except (TypeError, ValueError) as e:
                        cleaning_stats['json_unsafe_values'] += 1
                        problematic_cells.append((idx, col, type(value).__name__, str(value)[:50]))
                        # For other non-serializable types, convert to string
                        # (Decimals should already be converted to float64 by now)
                        df_clean.at[idx, col] = str(value)
                        logger.warning(f"Converted non-JSON-serializable value at [{idx}, {col}] from {type(value)} to {type(df_clean.at[idx, col])}")

        # If we found problematic cells, log a summary
        if problematic_cells:
            logger.warning(f"Found {len(problematic_cells)} non-JSON-serializable cells:")
            for idx, col, dtype, val in problematic_cells[:5]:  # Show first 5
                logger.warning(f"  [{idx}, {col}]: {dtype} = {val}")
            if len(problematic_cells) > 5:
                logger.warning(f"  ... and {len(problematic_cells) - 5} more")

        # Final check: Ensure the entire DataFrame can be serialized
        try:
            # Convert to list of lists for a final serialization test
            test_data = df_clean.values.tolist()
            json.dumps(test_data)
            logger.info("✅ Final JSON serialization test passed")
        except Exception as e:
            logger.error(f"❌ DataFrame still has JSON serialization issues after cleaning: {e}")
            # Instead of converting entire DataFrame to strings, handle specific problematic columns
            logger.warning("Handling problematic columns individually...")

            # First try converting datetime columns to strings
            datetime_cols = df_clean.select_dtypes(include=['datetime64']).columns
            for col in datetime_cols:
                logger.info(f"Converting datetime column '{col}' to string")
                df_clean[col] = df_clean[col].astype(str).replace('NaT', '')

            # Then handle any remaining problematic object columns
            object_cols = df_clean.select_dtypes(include=['object']).columns
            for col in object_cols:
                try:
                    # Test if this column can be serialized
                    test_vals = df_clean[col].dropna().head(5).tolist()
                    json.dumps(test_vals)
                except:
                    logger.warning(f"Converting problematic column '{col}' to string")
                    df_clean[col] = df_clean[col].astype(str).replace('nan', '').replace('None', '')

            # Final test
            try:
                test_data = df_clean.values.tolist()
                json.dumps(test_data)
                logger.info("✅ JSON serialization fixed by handling specific columns")
            except Exception as e2:
                # Only as absolute last resort, convert entire DataFrame
                logger.error(f"Still failing after targeted fixes: {e2}")
                logger.warning("Converting entire DataFrame to strings as last resort")
                for col in df_clean.columns:
                    df_clean[col] = df_clean[col].astype(str).replace('nan', '').replace('None', '')

        # Log cleaning summary
        if any(cleaning_stats.values()):
            logger.info(f"DataFrame cleaning: "
                       f"{cleaning_stats['inf_replaced']} infinity values, "
                       f"{cleaning_stats['nan_replaced']} NaN values, "
                       f"{cleaning_stats['large_values_capped']} large values capped, "
                       f"{cleaning_stats['zero_division_fixed']} zero divisions fixed, "
                       f"{cleaning_stats['json_unsafe_values']} JSON-unsafe values converted")

        return df_clean

    def _apply_enhanced_formatting_with_tracking(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int, formatting_state: Dict):
        """
        Apply enhanced formatting with state tracking to handle rate limit interruptions.
        This method ensures all formatting operations complete even if interrupted.
        """
        logger.info(f"🚀 Applying enhanced formatting with tracking for '{ws.title}'...")

        try:
            # Apply header formatting first (before any other formatting)
            logger.info("📋 Applying header formatting...")
            header_range = f'A{header_row}:{self._column_index_to_letter(len(df_clean.columns))}{header_row}'
            self.rate_limiter.execute_with_rate_limit(
                format_cell_range, ws, header_range, CellFormat(
                    textFormat=TextFormat(bold=True, fontFamily='Proxima Nova', fontSize=11, foregroundColor=Color(1, 1, 1)),
                    backgroundColor=Color(0.4, 0.4, 0.4),  # #666666
                    horizontalAlignment='CENTER',
                    verticalAlignment='MIDDLE',
                    wrapStrategy='WRAP',
                    borders=Borders(
                        top=Border('SOLID_THICK', Color(0, 0, 0)),
                        bottom=Border('SOLID_THICK', Color(0, 0, 0)),
                        left=Border('SOLID_THICK', Color(0, 0, 0)),
                        right=Border('SOLID_THICK', Color(0, 0, 0))
                    )
                )
            )
            logger.info(f"✅ Applied header formatting to {header_range}")

            # Apply thick border around entire table
            data_end_row = header_row + len(df_clean)
            table_range = f'A{header_row}:{self._column_index_to_letter(len(df_clean.columns))}{data_end_row}'
            logger.info("🔲 Applying thick border around entire table...")

            # Apply thick border to top row
            top_border_range = f'A{header_row}:{self._column_index_to_letter(len(df_clean.columns))}{header_row}'
            self.rate_limiter.execute_with_rate_limit(
                format_cell_range, ws, top_border_range,
                CellFormat(borders=Borders(top=Border('SOLID_THICK', Color(0, 0, 0))))
            )

            # Apply thick border to bottom row
            bottom_border_range = f'A{data_end_row}:{self._column_index_to_letter(len(df_clean.columns))}{data_end_row}'
            self.rate_limiter.execute_with_rate_limit(
                format_cell_range, ws, bottom_border_range,
                CellFormat(borders=Borders(bottom=Border('SOLID_THICK', Color(0, 0, 0))))
            )

            # Apply thick border to left column
            left_border_range = f'A{header_row}:A{data_end_row}'
            self.rate_limiter.execute_with_rate_limit(
                format_cell_range, ws, left_border_range,
                CellFormat(borders=Borders(left=Border('SOLID_THICK', Color(0, 0, 0))))
            )

            # Apply thick border to right column
            right_col = self._column_index_to_letter(len(df_clean.columns))
            right_border_range = f'{right_col}{header_row}:{right_col}{data_end_row}'
            self.rate_limiter.execute_with_rate_limit(
                format_cell_range, ws, right_border_range,
                CellFormat(borders=Borders(right=Border('SOLID_THICK', Color(0, 0, 0))))
            )

            logger.info(f"✅ Applied thick border around table: {table_range}")

            # Step 1: Basic formatting (font, alignment, number formatting, etc.)
            if not formatting_state['basic_formatting']:
                logger.info("📝 Step 1/4: Applying basic formatting...")
                self._apply_aggressive_basic_formatting(ws, df_clean, header_row)
                formatting_state['basic_formatting'] = True
                logger.info("✅ Basic formatting completed")

            # Step 2: Metric group identification and merging
            if 'metric_name' in df_clean.columns and not formatting_state['metric_merging']:
                logger.info("🔗 Step 2/4: Applying metric merging...")

                # CRITICAL: Refresh worksheet to ensure we have the latest data
                try:
                    logger.info("🔄 Refreshing worksheet before identifying metric groups...")
                    ws_fresh = ws.spreadsheet.worksheet(ws.title)
                    ws = ws_fresh
                    logger.info("✅ Worksheet refreshed for metric group identification")
                except Exception as e:
                    logger.warning(f"⚠️ Could not refresh worksheet: {e}")

                # Identify all metric groups
                metric_groups = self._identify_metric_groups(df_clean, header_row)
                merge_groups = [g for g in metric_groups if g['end_row'] > g['start_row']]

                # Track all merge operations needed
                merge_ops = []

                # Always add metric_name (column A) merges
                for g in merge_groups:
                    merge_ops.append({
                        'range': f'A{g["start_row"]}:A{g["end_row"]}',
                        'metric': g['metric'],
                        'column': 'metric_name'
                    })

                # Check if metric_definition column exists and add its merges
                if 'metric_definition' in df_clean.columns:
                    col_idx = df_clean.columns.get_loc('metric_definition')
                    metric_definition_col = self._column_index_to_letter(col_idx + 1)  # Convert to letter (1-based)
                    logger.info(f"Found metric_definition in column {metric_definition_col}, adding merge operations")

                    for g in merge_groups:
                        merge_ops.append({
                            'range': f'{metric_definition_col}{g["start_row"]}:{metric_definition_col}{g["end_row"]}',
                            'metric': g['metric'],
                            'column': 'metric_definition'
                        })

                # NEW: Check if this is multi-treatment format and add dimension_cut merges
                is_multi_treatment = 'variant_name' in df_clean.columns and 'variant_value' in df_clean.columns
                if is_multi_treatment and 'dimension_cut_name' in df_clean.columns:
                    logger.info("📊 Multi-treatment format detected - adding dimension cut merges")

                    # Get dimension groups within each metric
                    dimension_groups = self._identify_dimension_groups_within_metrics(df_clean, metric_groups, header_row)

                    # Get dimension_cut column letter
                    dim_col_idx = df_clean.columns.get_loc('dimension_cut_name')
                    dim_col_letter = self._column_index_to_letter(dim_col_idx + 1)

                    # Add dimension cut merges
                    for dg in dimension_groups:
                        if dg['end_row'] > dg['start_row']:  # Only merge if multiple rows
                            merge_ops.append({
                                'range': f'{dim_col_letter}{dg["start_row"]}:{dim_col_letter}{dg["end_row"]}',
                                'metric': dg['metric'],
                                'dimension_cut': dg['dimension_cut'],
                                'column': 'dimension_cut_name'
                            })

                    logger.info(f"Added {len([m for m in merge_ops if m['column'] == 'dimension_cut_name'])} dimension cut merge operations")

                formatting_state['merge_operations'] = merge_ops

                logger.info(f"📊 Found {len(formatting_state['merge_operations'])} merge operations to perform")

                # Apply merging with progress tracking
                self._apply_merging_with_progress(ws, formatting_state)
                formatting_state['metric_merging'] = True
                logger.info("✅ Metric merging completed")

            # Step 3: Borders between metric groups
            if 'metric_name' in df_clean.columns and not formatting_state['borders']:
                logger.info("🔲 Step 3/4: Applying borders...")

                # Identify border positions
                metric_groups = self._identify_metric_groups(df_clean, header_row)
                border_groups = metric_groups[:-1]  # All except last

                # Store metric groups in formatting state for border application
                formatting_state['metric_groups'] = metric_groups

                # Track all border operations needed
                formatting_state['border_operations'] = [
                    {
                        'range': f'A{g["end_row"]}:{self._column_index_to_letter(len(df_clean.columns))}{g["end_row"]}',
                        'metric': g['metric']
                    }
                    for g in border_groups
                ]

                logger.info(f"📊 Found {len(formatting_state['border_operations'])} border operations to perform")

                # Apply borders with progress tracking
                self._apply_borders_with_progress(ws, formatting_state)
                formatting_state['borders'] = True
                logger.info("✅ Borders completed")

            # Step 4: Apply conditional formatting AFTER merging to prevent formatting loss
            logger.info("🎨 Step 4/4: Applying conditional formatting after merging...")

            # Apply stat_sig conditional formatting
            self._apply_stat_sig_conditional_formatting(ws, df_clean, header_row)

            # Apply bold formatting for significant results
            self._apply_significant_bold_formatting(ws, df_clean, header_row)

            logger.info("✅ Conditional formatting completed")

            # Final validation
            logger.info("🔍 Running final formatting validation...")

            # CRITICAL: Refresh worksheet data to ensure merges are reflected
            logger.info("🔄 Refreshing worksheet data to ensure formatting is reflected...")
            time.sleep(2)  # Give Google Sheets time to process all formatting

            # Force a refresh by re-fetching worksheet
            try:
                ws_refreshed = ws.spreadsheet.worksheet(ws.title)
                success = self._validate_formatting_and_declare_success(ws_refreshed, df_clean, header_row)
            except:
                # Fallback to original worksheet if refresh fails
                success = self._validate_formatting_and_declare_success(ws, df_clean, header_row)

            if success:
                logger.info(f"🎉 All formatting completed successfully for '{ws.title}'!")
            else:
                logger.warning(f"⚠️ Formatting completed but validation shows issues in '{ws.title}'")

        except Exception as e:
            logger.error(f"❌ Formatting interrupted: {e}")
            logger.info(f"📊 Progress: Basic={formatting_state['basic_formatting']}, "
                       f"Merges={len(formatting_state['completed_merges'])}/{len(formatting_state['merge_operations'])}, "
                       f"Borders={len(formatting_state['completed_borders'])}/{len(formatting_state['border_operations'])}")
            raise

    def _apply_merging_with_progress(self, ws: gspread.Worksheet, formatting_state: Dict):
        """Apply merge operations with progress tracking and resumption capability."""
        total_merges = len(formatting_state['merge_operations'])
        completed = len(formatting_state['completed_merges'])

        if completed >= total_merges:
            logger.info("✅ All merge operations already completed")
            return

        logger.info(f"🔀 Resuming merge operations from {completed}/{total_merges}...")

        # CRITICAL: Refresh worksheet to ensure we have the latest state
        try:
            logger.info("🔄 Refreshing worksheet reference before merging...")
            ws_fresh = ws.spreadsheet.worksheet(ws.title)
            ws = ws_fresh
            logger.info("✅ Worksheet refreshed successfully")
        except Exception as e:
            logger.warning(f"⚠️ Could not refresh worksheet, continuing with existing reference: {e}")

        # Debug: Log first few merge operations
        if total_merges > 0:
            logger.debug(f"First merge operation: {formatting_state['merge_operations'][0]}")
            if total_merges > 1:
                logger.debug(f"Second merge operation: {formatting_state['merge_operations'][1]}")

        # Process remaining merges
        for i, merge_op in enumerate(formatting_state['merge_operations']):
            # Skip if already completed
            if merge_op['range'] in formatting_state['completed_merges']:
                continue

            try:
                # Debug log for each merge
                column_info = f" ({merge_op.get('column', 'unknown')})" if 'column' in merge_op else ""
                logger.debug(f"Applying merge {i+1}/{total_merges}: {merge_op['range']} for metric '{merge_op['metric']}'{column_info}")

                # Apply the merge with rate limiting
                self.rate_limiter.execute_with_rate_limit(
                    ws.merge_cells, merge_op['range']
                )

                # Mark as completed
                formatting_state['completed_merges'].append(merge_op['range'])

                # Log progress every 10 operations or for important milestones
                current_completed = len(formatting_state['completed_merges'])
                if current_completed % 10 == 0 or current_completed == total_merges:
                    logger.info(f"📈 Merge progress: {current_completed}/{total_merges} ({current_completed/total_merges*100:.1f}%)")

            except Exception as e:
                logger.error(f"❌ Failed to merge {merge_op['range']} for {merge_op['metric']}: {e}")
                # Log current progress and re-raise to trigger retry
                logger.info(f"📊 Completed {len(formatting_state['completed_merges'])}/{total_merges} merges before interruption")
                raise

        logger.info(f"✅ Completed all {total_merges} merge operations")

    def _apply_borders_with_progress(self, ws: gspread.Worksheet, formatting_state: Dict):
        """Apply borders with progress tracking for resumable formatting."""
        if 'border_operations' not in formatting_state or not formatting_state['border_operations']:
            return

        total_borders = len(formatting_state['border_operations'])
        completed = len(formatting_state.get('completed_borders', []))

        logger.info(f"🔲 Resuming border operations from {completed}/{total_borders}...")

        # Process remaining borders
        for i, border_op in enumerate(formatting_state['border_operations']):
            # Skip if already completed
            if i < completed:
                continue

            try:
                # Apply the border operation - now simplified to entire row
                self.rate_limiter.execute_with_rate_limit(
                    format_cell_range, ws, border_op['range'],
                    CellFormat(borders=Borders(bottom=Border('SOLID', Color(0.5, 0.5, 0.5))))
                )

                # Mark as completed
                formatting_state['completed_borders'].append(i)
                logger.debug(f"✅ Applied border {i+1}/{total_borders}: {border_op['range']}")

            except Exception as e:
                if "Rate Limit" in str(e) or "Quota" in str(e):
                    # Save progress and re-raise for retry
                    logger.info(f"📊 Completed {len(formatting_state['completed_borders'])}/{total_borders} borders before interruption")
                    raise
                else:
                    logger.error(f"❌ Failed to apply border {border_op['range']}: {e}")
                    # Continue with next border
                    formatting_state['completed_borders'].append(i)

        logger.info(f"📈 Border progress: {len(formatting_state['completed_borders'])}/{total_borders} (100.0%)")
        logger.info(f"✅ Completed all {total_borders} border operations")

    def _apply_aggressive_basic_formatting(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int):
        """Apply basic formatting aggressively with minimal API calls."""
        logger.info("🎨 Applying basic formatting aggressively...")

        # Get dimensions
        data_start_row = header_row + 1  # Start from row after header
        data_end_row = header_row + len(df_clean)
        data_end_col = self._column_index_to_letter(len(df_clean.columns))

        # Prepare batch formatting requests
        batch_requests = []

        # 1. Font formatting for DATA ONLY (not header) + alignment and text wrapping
        data_only_range = f'A{data_start_row}:{data_end_col}{data_end_row}'

        self.rate_limiter.execute_with_rate_limit(
            format_cell_range, ws, data_only_range, CellFormat(
                textFormat=TextFormat(fontFamily='Proxima Nova', fontSize=10),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',
                wrapStrategy='WRAP'
            )
        )
        logger.info(f"✅ Applied font formatting, alignment, and text wrapping to {data_only_range}")

        # 2. Number formatting - batch by column type
        self._apply_aggressive_number_formatting(ws, df_clean, header_row)

        # 3. Apply metric_name column formatting (wrapped text, middle alignment)
        self._apply_metric_name_formatting(ws, df_clean, header_row)

        # NOTE: Moved stat_sig conditional formatting and bold formatting to after merging
        # to prevent formatting loss during merge operations

        logger.info("✅ Basic formatting completed")

    def _column_index_to_letter(self, col_index: int) -> str:
        """Convert a column index (1-based) to column letter(s).

        Examples:
            1 -> 'A'
            26 -> 'Z'
            27 -> 'AA'
            28 -> 'AB'
        """
        result = ""
        while col_index > 0:
            col_index -= 1
            result = chr(65 + (col_index % 26)) + result
            col_index //= 26
        return result

    def _apply_aggressive_number_formatting(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int):
        """Apply number formatting with maximum efficiency and reduced API calls."""
        logger.info("📊 Applying number formatting aggressively...")

        # Define column-specific number formats
        specific_formats = {
            'control_value': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'treatment_value': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'variant_value': NumberFormat(type='NUMBER', pattern='#,##0.00'),  # Multi-treatment format
            'metric_value': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'relative_impact': NumberFormat(type='PERCENT', pattern='0.00%'),  # Unified format
            'relative_impact_ci_lower': NumberFormat(type='PERCENT', pattern='0.00%'),
            'relative_impact_ci_upper': NumberFormat(type='PERCENT', pattern='0.00%'),
            'absolute_impact': NumberFormat(type='NUMBER', pattern='#,##0.00'),  # Unified absolute format
            'absolute_impact_ci_lower': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'absolute_impact_ci_upper': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'p_value': NumberFormat(type='NUMBER', pattern='0.0000'),
            'metric_impact_relative': NumberFormat(type='PERCENT', pattern='0.00%'),  # Raw column name
            'metric_impact_absolute': NumberFormat(type='NUMBER', pattern='#,##0.00'),  # Raw column name
            # Global lift columns
            'metric_impact_relative_global_lift': NumberFormat(type='PERCENT', pattern='0.00%'),  # Raw column name
            'metric_impact_absolute_global_lift': NumberFormat(type='NUMBER', pattern='#,##0.00'),  # Raw column name
            'relative_impact_global_lift': NumberFormat(type='PERCENT', pattern='0.00%'),  # Renamed column
            'absolute_impact_global_lift': NumberFormat(type='NUMBER', pattern='#,##0.00'),  # Renamed column
            # Multi-treatment columns
            'rel_effect': NumberFormat(type='PERCENT', pattern='0.00%'),  # Multi-treatment relative effect
            'relative_effect': NumberFormat(type='PERCENT', pattern='0.00%'),  # Alternative name
            'rel_treatment_effect': NumberFormat(type='PERCENT', pattern='0.00%'),  # Single treatment format
        }

        # Define broader pattern matching for column types
        default_formats = {
            'number': NumberFormat(type='NUMBER', pattern='#,##0.00'),
            'percent': NumberFormat(type='PERCENT', pattern='0.00%'),
            'scientific': NumberFormat(type='SCIENTIFIC', pattern='0.00E+00')
        }

        # Process all numeric columns
        numeric_columns = df_clean.select_dtypes(include=[np.number]).columns.tolist()

        # Also check for columns in specific_formats that might not be detected as numeric
        # (e.g., due to dtype metadata not updating after Decimal conversion)
        for col_name in specific_formats.keys():
            if col_name in df_clean.columns and col_name not in numeric_columns:
                # Check if column contains numeric data despite dtype
                sample_values = df_clean[col_name].dropna().head(10)
                if sample_values.empty:
                    continue

                # Check if values are numeric
                try:
                    # Try to convert to float - if successful, it's numeric
                    sample_values.astype(float)
                    numeric_columns.append(col_name)
                    logger.info(f"Added '{col_name}' to numeric columns (contains numeric data despite dtype: {df_clean[col_name].dtype})")
                except:
                    pass

        for col_name in numeric_columns:
            col_index = df_clean.columns.tolist().index(col_name) + 1
            col_letter = self._column_index_to_letter(col_index)
            data_rows = len(df_clean)
            range_name = f'{col_letter}{header_row+1}:{col_letter}{header_row+data_rows}'

            # Determine format based on column name patterns
            col_name = df_clean.columns[col_index - 1]

            # Check specific formats first
            if col_name in specific_formats:
                number_format = specific_formats[col_name]
                logger.debug(f"Column '{col_name}' using specific format: {number_format.pattern}")
            else:
                # Default to number format for all other numeric columns
                number_format = default_formats['number']
                logger.debug(f"Column '{col_name}' using default number format: {number_format.pattern}")

            try:
                self.rate_limiter.execute_with_rate_limit(
                    format_cell_range, ws, range_name, CellFormat(numberFormat=number_format)
                )
                logger.info(f"✅ Applied {number_format.pattern} to {col_name}")
            except Exception as e:
                logger.error(f"Failed to format {col_name}: {e}")
                # The exponential backoff handler will have already retried

        # Log summary
        logger.info(f"✅ Number formatting completed for {len(numeric_columns)} numeric columns")

    def _apply_stat_sig_conditional_formatting(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int):
        """Apply conditional formatting to stat_sig column based on positive/negative direction."""
        logger.info("🎨 Applying stat_sig conditional formatting...")

        if 'stat_sig' not in df_clean.columns:
            logger.warning("No stat_sig column found, skipping conditional formatting")
            return

        # CRITICAL: Verify worksheet data matches DataFrame before applying formatting
        try:
            ws_data = self.rate_limiter.execute_with_rate_limit(ws.get_all_values)
            actual_rows = len(ws_data)
            expected_rows = header_row + len(df_clean)
            if actual_rows < expected_rows:
                logger.warning(f"⚠️ Worksheet has fewer rows ({actual_rows}) than expected ({expected_rows}). Waiting for data to settle...")
                time.sleep(2)
        except Exception as e:
            logger.warning(f"Could not verify worksheet data: {e}")

        # Get stat_sig column index and letter
        col_index = df_clean.columns.tolist().index('stat_sig') + 1
        col_letter = self._column_index_to_letter(col_index)

        # Light green for positive, light red for negative
        light_green = Color(0.843, 0.925, 0.847)  # #d7ecd8
        light_red = Color(0.933, 0.698, 0.698)    # #eeb2b2

        # Process each row individually to apply conditional formatting
        data_start_row = header_row + 1

        # Batch the formatting operations for efficiency
        positive_cells = []
        negative_cells = []

        # CRITICAL: Use enumerate to get sequential indices (fixes filtered DataFrame issue)
        for row_idx, (idx, row) in enumerate(df_clean.iterrows()):
            stat_sig_value = row['stat_sig']
            cell_row = data_start_row + row_idx  # Use enumerated index, not DataFrame index

            if pd.notna(stat_sig_value):
                stat_sig_lower = str(stat_sig_value).lower()
                if 'positive' in stat_sig_lower:
                    positive_cells.append(f'{col_letter}{cell_row}')
                elif 'negative' in stat_sig_lower:
                    negative_cells.append(f'{col_letter}{cell_row}')

        # Apply formatting in batches
        try:
            # Format positive cells with light green
            if positive_cells:
                # Join individual cells into ranges where possible
                positive_ranges = self._merge_consecutive_cells(positive_cells)
                logger.debug(f"Positive cell ranges: {positive_ranges}")
                for cell_range in positive_ranges:  # Remove limit - format all cells
                    self.rate_limiter.execute_with_rate_limit(
                        format_cell_range, ws, cell_range,
                        CellFormat(backgroundColor=light_green)
                    )
                logger.info(f"✅ Applied light green to {len(positive_cells)} positive stat_sig cells")

            # Format negative cells with light red
            if negative_cells:
                # Join individual cells into ranges where possible
                negative_ranges = self._merge_consecutive_cells(negative_cells)
                logger.debug(f"Negative cell ranges: {negative_ranges}")
                for cell_range in negative_ranges:  # Remove limit - format all cells
                    self.rate_limiter.execute_with_rate_limit(
                        format_cell_range, ws, cell_range,
                        CellFormat(backgroundColor=light_red)
                    )
                logger.info(f"✅ Applied light red to {len(negative_cells)} negative stat_sig cells")

        except Exception as e:
            logger.error(f"Failed to apply stat_sig conditional formatting: {e}")

        logger.info("✅ Stat_sig conditional formatting completed")

    def _apply_metric_name_formatting(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int):
        """Apply wrapped text and middle vertical alignment to metric_name column."""
        logger.info("📝 Applying metric_name column formatting...")

        if 'metric_name' not in df_clean.columns:
            logger.warning("No metric_name column found, skipping metric name formatting")
            return

        # Get metric_name column index and letter
        col_index = df_clean.columns.tolist().index('metric_name') + 1
        col_letter = self._column_index_to_letter(col_index)

        # Apply to entire column including header
        data_end_row = header_row + len(df_clean)
        range_name = f'{col_letter}{header_row}:{col_letter}{data_end_row}'

        # Note: Text wrapping and vertical alignment are now applied globally,
        # but we keep this method for potential future metric_name specific formatting
        logger.info(f"✅ Metric_name column already has text wrapping and alignment from global formatting")

        logger.info("✅ Metric_name formatting completed")

    def _apply_significant_bold_formatting(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int):
        """Apply bold formatting to rows containing 'significant' in stat_sig column."""
        logger.info("🔤 Applying bold formatting for significant results...")

        if 'stat_sig' not in df_clean.columns:
            logger.warning("No stat_sig column found, skipping significant bold formatting")
            return

        # Process each row to find significant results
        data_start_row = header_row + 1
        significant_rows = []

        # CRITICAL: Use enumerate to get sequential indices (fixes filtered DataFrame issue)
        for row_idx, (idx, row) in enumerate(df_clean.iterrows()):
            stat_sig_value = row['stat_sig']
            if pd.notna(stat_sig_value) and 'significant' in str(stat_sig_value).lower():
                row_num = data_start_row + row_idx  # Use enumerated index, not DataFrame index
                significant_rows.append(row_num)

        if not significant_rows:
            logger.info("No significant results found to bold")
            return

        # Apply bold formatting to entire rows with significant results
        data_end_col = self._column_index_to_letter(len(df_clean.columns))

        try:
            # Batch the operations for efficiency
            for row_num in significant_rows:  # Remove limit - format all significant rows
                range_name = f'A{row_num}:{data_end_col}{row_num}'

                # Apply bold while preserving other formatting (font family, size)
                self.rate_limiter.execute_with_rate_limit(
                    format_cell_range, ws, range_name,
                    CellFormat(textFormat=TextFormat(bold=True, fontFamily='Proxima Nova', fontSize=10))
                )

            logger.info(f"✅ Applied bold formatting to {len(significant_rows)} significant result rows")

        except Exception as e:
            logger.error(f"Failed to apply bold formatting for significant results: {e}")

        logger.info("✅ Significant bold formatting completed")

    def _merge_consecutive_cells(self, cells: List[str]) -> List[str]:
        """Merge consecutive cells into ranges for more efficient formatting."""
        if not cells:
            return []

        # Sort cells by row number
        sorted_cells = sorted(cells, key=lambda x: int(x[1:]))

        ranges = []
        current_start = sorted_cells[0]
        current_end = sorted_cells[0]

        for i in range(1, len(sorted_cells)):
            cell = sorted_cells[i]
            prev_row = int(current_end[1:])
            curr_row = int(cell[1:])

            if curr_row == prev_row + 1:
                # Consecutive, extend range
                current_end = cell
            else:
                # Not consecutive, save current range and start new one
                if current_start == current_end:
                    ranges.append(current_start)
                else:
                    ranges.append(f"{current_start}:{current_end}")
                current_start = cell
                current_end = cell

        # Add the last range
        if current_start == current_end:
            ranges.append(current_start)
        else:
            ranges.append(f"{current_start}:{current_end}")

        return ranges

    def _validate_formatting_and_declare_success(self, ws: gspread.Worksheet, df_clean: pd.DataFrame, header_row: int, ignore_failures: bool = False) -> bool:
        """
        Validate formatting and only declare success if everything is perfect.
        """
        logger.info("🔍 Running comprehensive formatting validation...")

        try:
            # Import validation here to avoid circular imports
            from .test_formatting import FormattingValidator

            # Get sheet URL for validation
            sheet_url = ws.spreadsheet.url

            validator = FormattingValidator(self)
            validation_results = validator.validate_sheet_formatting(sheet_url, ws.title)

            # Check if validation passed
            overall_status = validation_results.get('overall_status', 'FAILED')
            passed_checks = validation_results.get('passed_checks', 0)
            total_checks = validation_results.get('total_checks', 0)

            logger.info(f"📊 Validation Results: {overall_status}")
            logger.info(f"✅ {passed_checks}/{total_checks} checks passed")

            # Log any failures
            for check_name, result in validation_results.get('validations', {}).items():
                status_emoji = "🎉" if result['status'] == 'PASSED' else "❌" if result['status'] == 'FAILED' else "⚠️"
                if result['status'] != 'PASSED' and not ignore_failures:
                    logger.warning(f"{status_emoji} {check_name}: {result['message']}")
                else:
                    logger.info(f"{status_emoji} {check_name}: {result['message']}")

            return overall_status == 'PASSED'

        except Exception as e:
            logger.error(f"❌ Validation failed: {e}")
            return False if not ignore_failures else True

    def _identify_metric_groups(self, df_clean: pd.DataFrame, header_row: int):
        """Identify groups of rows that belong to the same metric."""
        logger.info("🔍 Identifying metric groups...")

        if 'metric_name' not in df_clean.columns:
            logger.warning("No metric_name column found")
            return []

        metric_groups = []
        current_metric = None
        start_row = None

        # Calculate the actual data start row (row after header)
        data_start_row = header_row + 1

        # CRITICAL: Use enumerate instead of iterrows to get sequential indices
        # This fixes the issue where filtered DataFrames have non-sequential indices
        for row_idx, (idx, row) in enumerate(df_clean.iterrows()):
            metric = row['metric_name']
            # Calculate actual row number in the sheet using enumerated index
            row_num = data_start_row + row_idx  # row_idx is 0-based sequential

            if metric != current_metric:
                # Save previous group if exists
                if current_metric is not None:
                    metric_groups.append({
                        'metric': current_metric,
                        'start_row': start_row,
                        'end_row': row_num - 1
                    })

                # Start new group
                current_metric = metric
                start_row = row_num

        # Don't forget the last group
        if current_metric is not None:
            # The last row of data is at data_start_row + (number of rows - 1)
            last_data_row = data_start_row + len(df_clean) - 1
            metric_groups.append({
                'metric': current_metric,
                'start_row': start_row,
                'end_row': last_data_row
            })

        logger.info(f"📊 Found {len(metric_groups)} metric groups")
        return metric_groups

    def _identify_dimension_groups_within_metrics(self, df_clean: pd.DataFrame, metric_groups: List[Dict], header_row: int) -> List[Dict]:
        """
        Identify groups of rows that belong to the same dimension cut within each metric.
        Used for multi-treatment format where each dimension cut has multiple variant rows.
        """
        logger.info("🔍 Identifying dimension groups for multi-treatment format...")

        if 'dimension_cut_name' not in df_clean.columns:
            logger.warning("No dimension_cut_name column found")
            return []

        dimension_groups = []

        # Process each metric group
        for metric_group in metric_groups:
            metric_start = metric_group['start_row'] - header_row - 1  # Convert back to dataframe index
            metric_end = metric_group['end_row'] - header_row - 1

            # Get subset of dataframe for this metric
            metric_subset = df_clean.iloc[metric_start:metric_end+1]

            # Group by dimension_cut_name within this metric
            current_dimension = None
            dimension_start_row = None

            for relative_idx, (idx, row) in enumerate(metric_subset.iterrows()):
                dimension = row['dimension_cut_name']
                absolute_row = metric_group['start_row'] + relative_idx

                if dimension != current_dimension:
                    # Save previous dimension group if exists
                    if current_dimension is not None:
                        dimension_groups.append({
                            'metric': metric_group['metric'],
                            'dimension_cut': current_dimension,
                            'start_row': dimension_start_row,
                            'end_row': absolute_row - 1
                        })

                    # Start new dimension group
                    current_dimension = dimension
                    dimension_start_row = absolute_row

            # Don't forget the last dimension group in this metric
            if current_dimension is not None:
                dimension_groups.append({
                    'metric': metric_group['metric'],
                    'dimension_cut': current_dimension,
                    'start_row': dimension_start_row,
                    'end_row': metric_group['end_row']
                })

        logger.info(f"📊 Found {len(dimension_groups)} dimension groups across {len(metric_groups)} metrics")
        return dimension_groups

    def _export_dataframe_to_worksheet(
        self,
        df: pd.DataFrame,
        worksheet: gspread.Worksheet,
        title: str = None,
        description: str = None,
        run_validation: bool = False
    ) -> Dict[str, Any]:
        """
        Export a DataFrame to a specific worksheet with formatting.
        CRITICAL: Ensures formatting completes even if rate limits are hit.

        Args:
            df: DataFrame to export
            worksheet: Target worksheet
            title: Optional title for the data
            description: Optional description
            run_validation: Whether to run validation

        Returns:
            Dictionary with export results
        """
        # Clear the worksheet
        self.rate_limiter.execute_with_rate_limit(worksheet.clear)

        # Clean DataFrame for Google Sheets export
        df_clean = self._clean_dataframe_for_export(df)

        # Prepare data with headers
        data_to_write = []

        if title:
            data_to_write.append([title])
            data_to_write.append([""])  # Empty row after title

        if description:
            data_to_write.append([description])
            data_to_write.append([""])  # Empty row after description

        # Add DataFrame headers
        data_to_write.append(df_clean.columns.tolist())

        # Add DataFrame data
        for _, row in df_clean.iterrows():
            # Convert row to list, replacing NaN with None for JSON compatibility
            row_data = []
            for val in row:
                if pd.isna(val):
                    row_data.append(None)
                elif isinstance(val, np.floating) and np.isnan(val):
                    # Extra check for numpy NaN
                    row_data.append(None)
                else:
                    row_data.append(val)
            data_to_write.append(row_data)

        # Write to sheet
        if data_to_write:
            try:
                # For large datasets, write in chunks
                if len(data_to_write) > 200:
                    logger.info(f"Large dataset detected ({len(data_to_write)} rows). Writing in chunks...")

                    # Calculate header rows
                    header_rows = 0
                    if title:
                        header_rows += 2  # Title + empty row
                    if description:
                        header_rows += 2  # Description + empty row
                    header_rows += 1  # Column headers

                    # Write header data first
                    if header_rows > 0:
                        header_data = data_to_write[:header_rows]
                        self.rate_limiter.execute_with_rate_limit(
                            worksheet.update, 'A1', header_data, value_input_option=ValueInputOption.user_entered
                        )

                    # Write data in chunks
                    chunk_size = 100
                    data_rows = data_to_write[header_rows:]
                    for i in range(0, len(data_rows), chunk_size):
                        chunk = data_rows[i:i+chunk_size]
                        start_row = header_rows + i + 1
                        end_row = start_row + len(chunk) - 1
                        range_name = f'A{start_row}:Z{end_row}'

                        logger.debug(f"Writing chunk: rows {start_row}-{end_row}")
                        self.rate_limiter.execute_with_rate_limit(
                            worksheet.update, range_name, chunk, value_input_option=ValueInputOption.user_entered
                        )
                else:
                    # Small dataset, write all at once
                    logger.info(f"Writing {len(data_to_write)} rows to '{worksheet.title}'...")
                    self.rate_limiter.execute_with_rate_limit(
                        worksheet.update, 'A1', data_to_write, value_input_option=ValueInputOption.user_entered
                    )

                # CRITICAL: Wait for Google Sheets to process the data
                logger.info(f"⏳ Waiting 3 seconds for Google Sheets to process data in '{worksheet.title}'...")
                time.sleep(3)

                # Verify data was written
                try:
                    verify_data = self.rate_limiter.execute_with_rate_limit(
                        worksheet.get_all_values
                    )
                    logger.info(f"✅ Verified {len(verify_data)} rows written to '{worksheet.title}'")
                except Exception as e:
                    logger.warning(f"⚠️ Could not verify data write: {e}")

            except Exception as e:
                logger.error(f"Error writing data to worksheet: {e}")
                raise

        # Calculate header row for formatting
        header_row = 1
        if title:
            header_row += 2
        if description:
            header_row += 2

        # CRITICAL: Apply formatting with proper completion tracking
        formatting_success = False
        max_formatting_retries = 3

        # Persistent formatting state across retries
        formatting_state = {
            'basic_formatting': False,
            'metric_merging': False,
            'borders': False,
            'merge_operations': [],
            'border_operations': [],
            'completed_merges': [],
            'completed_borders': []
        }

        # Check if metric_definition is present in column B
        if 'metric_definition' in df_clean.columns and df_clean.columns.get_loc('metric_definition') == 1:
            formatting_state['has_metric_definition'] = True
        else:
            formatting_state['has_metric_definition'] = False

        for retry in range(max_formatting_retries):
            try:
                logger.info(f"🎨 Applying formatting to '{worksheet.title}' (attempt {retry + 1}/{max_formatting_retries})")

                # Show progress if this is a retry
                if retry > 0:
                    logger.info(f"📊 Resuming from: Basic={formatting_state['basic_formatting']}, "
                               f"Merges={len(formatting_state['completed_merges'])}/{len(formatting_state['merge_operations'])}, "
                               f"Borders={len(formatting_state['completed_borders'])}/{len(formatting_state['border_operations'])}")

                # Apply enhanced formatting with state tracking
                self._apply_enhanced_formatting_with_tracking(worksheet, df_clean, header_row, formatting_state)

                # Auto-resize columns with rate limiting
                for i in range(len(df_clean.columns)):
                    self.rate_limiter.execute_with_rate_limit(
                        worksheet.columns_auto_resize, i, i
                    )

                formatting_success = True
                logger.info(f"✅ Formatting completed successfully for '{worksheet.title}'")
                break

            except Exception as e:
                logger.error(f"❌ Formatting attempt {retry + 1} failed for '{worksheet.title}': {e}")

                if retry < max_formatting_retries - 1:
                    # Wait before retrying
                    wait_time = 30 * (retry + 1)  # Exponential backoff
                    logger.info(f"⏳ Waiting {wait_time}s before retrying formatting...")
                    time.sleep(wait_time)

                    # Reset rate limiter to ensure we have capacity
                    self.rate_limiter.reset_to_next_window()
                else:
                    # Final attempt failed
                    logger.error(f"❌ CRITICAL: All formatting attempts failed for '{worksheet.title}'")
                    raise Exception(f"Formatting failed after {max_formatting_retries} attempts: {e}") from e

        return {
            'rows_exported': len(df_clean),
            'header_row': header_row,
            'worksheet_name': worksheet.title,
            'formatting_success': formatting_success
        }

    @staticmethod
    def combine_confidence_intervals_into_relative_impact(df: pd.DataFrame,
                                                         lower_col: str = 'relative_impact_ci_lower',
                                                         upper_col: str = 'relative_impact_ci_upper',
                                                         remove_ci_columns: bool = True) -> pd.DataFrame:
        """
        Combine confidence interval columns into the relative_impact column.

        This transforms the relative_impact column to show: value (lower, upper)
        For example: 0.123 (0.045, 0.201)

        Args:
            df: DataFrame containing the CI columns
            lower_col: Name of lower bound column (default: 'relative_impact_ci_lower')
            upper_col: Name of upper bound column (default: 'relative_impact_ci_upper')
            remove_ci_columns: Whether to remove the CI columns after combining

        Returns:
            DataFrame with combined CI values in relative_impact column
        """
        df_copy = df.copy()

        # Check if required columns exist
        if 'relative_impact' not in df_copy.columns:
            logger.warning("No relative_impact column found - cannot combine CIs")
            return df_copy

        if lower_col not in df_copy.columns or upper_col not in df_copy.columns:
            logger.info(f"CI columns {lower_col} and/or {upper_col} not found - skipping CI combination")
            return df_copy

        logger.info(f"Combining confidence intervals from {lower_col} and {upper_col} into relative_impact")

        # Create formatted string with effect and CI
        def format_with_ci(row):
            effect = row['relative_impact']
            lower = row[lower_col]
            upper = row[upper_col]

            # Skip if effect is NaN/None (e.g., control rows)
            if pd.isna(effect):
                return effect

            # Format as percentage if numeric
            if pd.notna(lower) and pd.notna(upper):
                # Format all values as percentages
                effect_str = f"{effect * 100:.2f}%"
                lower_str = f"{lower * 100:.2f}%"
                upper_str = f"{upper * 100:.2f}%"
                return f"{effect_str} ({lower_str}, {upper_str})"
            else:
                # No CI available, just show the effect
                return f"{effect * 100:.2f}%"

        df_copy['relative_impact'] = df_copy.apply(format_with_ci, axis=1)

        # Remove CI columns if requested
        if remove_ci_columns:
            columns_to_drop = [col for col in [lower_col, upper_col] if col in df_copy.columns]
            if columns_to_drop:
                df_copy = df_copy.drop(columns=columns_to_drop)
                logger.info(f"Removed CI columns: {', '.join(columns_to_drop)}")

        return df_copy

    @staticmethod
    def get_analyzed_at_range(df: pd.DataFrame) -> Optional[str]:
        """
        Get the timestamp range from analyzed_at column if it exists.

        Args:
            df: DataFrame with experiment results

        Returns:
            String describing the analysis timestamp range, or None if column doesn't exist
        """
        if 'analyzed_at' not in df.columns:
            return None

        # Filter out null values
        analyzed_dates = df['analyzed_at'].dropna()

        if analyzed_dates.empty:
            return None

        try:
            # Convert to datetime if not already
            analyzed_dates = pd.to_datetime(analyzed_dates)

            # Get min and max timestamps
            min_timestamp = analyzed_dates.min()
            max_timestamp = analyzed_dates.max()

            # Format the timestamps
            if min_timestamp == max_timestamp:
                # Same exact timestamp
                return f"Metrics analyzed at {min_timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            elif (max_timestamp - min_timestamp).total_seconds() < 60:
                # Within same minute
                return f"Metrics analyzed at {min_timestamp.strftime('%Y-%m-%d %H:%M')}"
            elif min_timestamp.date() == max_timestamp.date():
                # Same day, show time range
                return f"Metrics analyzed on {min_timestamp.strftime('%Y-%m-%d')} between {min_timestamp.strftime('%H:%M:%S')} and {max_timestamp.strftime('%H:%M:%S')}"
            else:
                # Different days, show full timestamp range
                return f"Metrics analyzed between {min_timestamp.strftime('%Y-%m-%d %H:%M:%S')} and {max_timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        except Exception as e:
            logger.warning(f"Could not parse analyzed_at timestamps: {e}")
            return None


# REMOVED: quick_export functions - Not used anywhere


def export_curie_experiment_results_with_categories(
    df: pd.DataFrame,
    experiment_name: str,
    sheet_name: Optional[str] = None,
    credentials_path: Optional[str] = None,
    auto_share_email: Optional[str] = None,
    metric_categories: Optional[Dict[str, List[str]]] = None,
    run_validation: bool = True,
    analyzed_at_info: Optional[str] = None,
    folder_id: Optional[str] = None,
    oauth_client: Optional[gspread.Client] = None
) -> Dict[str, Any]:
    """
    Export Curie experiment results to Google Sheets with separate tabs for metric categories.

    Args:
        df: DataFrame with experiment results
        experiment_name: Name of the experiment
        sheet_name: Name of the Google Sheet (auto-generated if None)
        credentials_path: Path to credentials file (for service account)
        auto_share_email: Email to automatically share with (for service account)
        metric_categories: Dict mapping category names to lists of metrics
            e.g., {'primary': ['metric1', 'metric2'], 'secondary': ['metric3'], 'guardrail': ['metric4']}
        run_validation: Whether to run comprehensive validation
        analyzed_at_info: Pre-extracted analyzed_at info (optional, will extract from df if not provided)
        folder_id: Optional Google Drive folder ID to create sheets in (avoids service account storage limits)
        oauth_client: Optional OAuth client (if provided, uses OAuth instead of service account)

    Returns:
        Dictionary with sheet URL and validation results
    """
    from datetime import datetime

    if sheet_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        sheet_name = f"{experiment_name}_results_{timestamp}"

    logger.info(f"🚀 Exporting Curie experiment with metric categories: {experiment_name}")
    logger.info(f"📊 Data: {len(df)} rows, {df['metric_name'].nunique() if 'metric_name' in df.columns else 'unknown'} metrics")

    if metric_categories:
        logger.info(f"📋 Metric categories: {', '.join(metric_categories.keys())}")

    # Initialize formatter
    if oauth_client:
        # Use OAuth client - create formatter without credentials
        formatter = ExperimentSheetsFormatter(None, None)
        formatter.client = oauth_client  # Use the provided OAuth client
        logger.info("Using OAuth authentication (sheet will be owned by authenticated user)")
    else:
        # Use service account authentication
        formatter = ExperimentSheetsFormatter(credentials_path, auto_share_email)

    logger.info(f"⚡ API Rate Limiter: {formatter.rate_limiter.max_requests} requests per {formatter.rate_limiter.window_seconds}s")

    # Get analyzed_at date range for descriptions (use provided or extract from df)
    if analyzed_at_info is None:
        analyzed_at_info = formatter.get_analyzed_at_range(df)

    # Create or open the sheet
    workbook = formatter.create_or_open_sheet(sheet_name, folder_id=folder_id)

    # Get existing worksheets
    existing_sheets = [ws.title for ws in workbook.worksheets()]

    # Define worksheet names
    worksheet_names = ["All Metrics"]  # Always have an "All Metrics" tab
    if metric_categories:
        # Add category-specific tabs
        category_order = ['primary', 'secondary', 'guardrail']  # Define order
        for category in category_order:
            if category in metric_categories and metric_categories[category]:
                worksheet_names.append(f"{category.capitalize()} Metrics")

    # Create worksheets if they don't exist
    for ws_name in worksheet_names:
        if ws_name not in existing_sheets:
            workbook.add_worksheet(title=ws_name, rows=1000, cols=26)
            logger.info(f"Created worksheet: {ws_name}")

    # Delete default "Sheet1" if it exists and we have other sheets
    if "Sheet1" in existing_sheets and len(workbook.worksheets()) > 1:
        try:
            workbook.del_worksheet(workbook.worksheet("Sheet1"))
        except:
            pass

    results = {
        'sheet_url': workbook.url,
        'experiment_name': experiment_name,
        'sheet_name': sheet_name,
        'data_rows': len(df),
        'export_timestamp': datetime.now().isoformat(),
        'api_calls_used': 0,
        'worksheets': {}
    }

    # Export to "All Metrics" tab first
    logger.info("📊 Exporting to 'All Metrics' tab...")
    all_metrics_ws = workbook.worksheet("All Metrics")

    # Build description for All Metrics tab
    all_metrics_desc_parts = [f"Complete experiment results exported on {datetime.now().strftime('%Y-%m-%d %H:%M')}"]
    if analyzed_at_info:
        all_metrics_desc_parts.append(f" - {analyzed_at_info}")
    all_metrics_description = "".join(all_metrics_desc_parts)

    all_metrics_result = formatter._export_dataframe_to_worksheet(
        df=df,
        worksheet=all_metrics_ws,
        title=f"{experiment_name.replace('_', ' ').title()} - All Metrics",
        description=all_metrics_description,
        run_validation=False  # We'll validate all tabs at the end
    )
    results['worksheets']['all_metrics'] = all_metrics_result

    # Ensure formatting completed successfully before proceeding
    if not all_metrics_result.get('formatting_success', False):
        logger.error(f"❌ Failed to properly format 'All Metrics' tab. Stopping export.")
        logger.error(f"❌ All Metrics result details: {all_metrics_result}")
        results['success'] = False
        results['error'] = "Failed to format 'All Metrics' tab"
        results['all_metrics_result'] = all_metrics_result
        return results

    # Export category-specific tabs if metrics are categorized
    if metric_categories:
        for category in ['primary', 'secondary', 'guardrail']:
            if category in metric_categories and metric_categories[category]:
                ws_name = f"{category.capitalize()} Metrics"
                logger.info(f"📊 Exporting to '{ws_name}' tab...")

                # Filter DataFrame for this category's metrics
                category_metrics = metric_categories[category]
                category_df = df[df['metric_name'].isin(category_metrics)]

                if not category_df.empty:
                    category_ws = workbook.worksheet(ws_name)

                    # Build description for category tab
                    category_desc_parts = [f"{len(category_metrics)} {category} metrics - Exported on {datetime.now().strftime('%Y-%m-%d %H:%M')}"]
                    if analyzed_at_info:
                        # For category tabs, check if we have different date ranges
                        category_analyzed_info = formatter.get_analyzed_at_range(category_df)
                        if category_analyzed_info and category_analyzed_info != analyzed_at_info:
                            # Use category-specific date range if different
                            category_desc_parts.append(f" - {category_analyzed_info}")
                        else:
                            # Use overall date range
                            category_desc_parts.append(f" - {analyzed_at_info}")
                    category_description = "".join(category_desc_parts)

                    category_result = formatter._export_dataframe_to_worksheet(
                        df=category_df,
                        worksheet=category_ws,
                        title=f"{experiment_name.replace('_', ' ').title()} - {category.capitalize()} Metrics",
                        description=category_description,
                        run_validation=False
                    )
                    results['worksheets'][f'{category}_metrics'] = category_result

                    # Ensure formatting completed successfully before proceeding
                    if not category_result.get('formatting_success', False):
                        logger.error(f"❌ Failed to properly format '{ws_name}' tab. Stopping export.")
                        logger.error(f"❌ Category result details: {category_result}")
                        results['success'] = False
                        results['error'] = f"Failed to format '{ws_name}' tab"
                        results[f'{category}_result'] = category_result
                        return results

                    logger.info(f"✅ Exported {len(category_df)} rows to {ws_name}")
                else:
                    logger.warning(f"⚠️ No data found for {category} metrics: {', '.join(category_metrics)}")

    # Update API calls used
    results['api_calls_used'] = formatter.rate_limiter.total_calls

    # Run comprehensive validation on all tabs if requested
    if run_validation:
        logger.info("🔍 Running comprehensive validation on all tabs...")
        try:
            from .test_formatting import FormattingValidator
            validator = FormattingValidator(formatter)

            all_validations = {}
            all_passed = True

            # Validate each worksheet
            for ws_name in worksheet_names:
                logger.info(f"🔍 Validating '{ws_name}' tab...")
                ws_validation = validator.validate_sheet_formatting(workbook.url, ws_name)
                all_validations[ws_name] = ws_validation

                if ws_validation.get('overall_status') != 'PASSED':
                    all_passed = False
                    logger.error(f"❌ Validation failed for '{ws_name}' tab")
                    logger.error(f"   Validation details: {ws_validation}")
                    # Log specific validation failures
                    if 'checks' in ws_validation:
                        for check_name, check_result in ws_validation['checks'].items():
                            if not check_result.get('passed', True):
                                logger.error(f"   - {check_name}: {check_result}")
                else:
                    logger.info(f"✅ Validation passed for '{ws_name}' tab")

            results['validation'] = {
                'overall_status': 'PASSED' if all_passed else 'FAILED',
                'tab_validations': all_validations
            }
            results['success'] = all_passed

            # Log comprehensive summary
            logger.info("🎯 CURIE EXPORT WITH CATEGORIES COMPLETE")
            logger.info("=" * 60)
            logger.info(f"📋 Experiment: {experiment_name}")
            logger.info(f"📊 Data: {len(df)} total rows exported")
            logger.info(f"📑 Tabs: {len(worksheet_names)} worksheets created")
            logger.info(f"🔗 URL: {workbook.url}")
            logger.info(f"⚡ API Calls Used: {formatter.rate_limiter.total_calls}")
            logger.info(f"✅ Validation: {'PASSED' if all_passed else 'FAILED'}")

            if metric_categories:
                logger.info("📋 Metric Categories:")
                for category, metrics in metric_categories.items():
                    if metrics:
                        logger.info(f"   - {category.capitalize()}: {len(metrics)} metrics")

            logger.info("=" * 60)

        except Exception as e:
            import traceback
            tb_str = traceback.format_exc()
            logger.error(f"❌ Validation failed with error: {e}")
            logger.error(f"❌ Full traceback: {tb_str}")
            results['validation_error'] = str(e)
            results['validation_traceback'] = tb_str
            results['success'] = False
    else:
        results['success'] = True

    return results