#!/usr/bin/env python3
"""
Export Curie experiment results to Google Sheets.

This module provides functionality to:
1. Load Curie experiment results from Snowflake
2. Filter results based on metrics, dimensions, and columns
3. Export to Google Sheets with comprehensive formatting

All user interactions should happen through Cursor chat, not CLI prompts.
"""

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union
import json
from pathlib import Path
from dotenv import load_dotenv
import gspread
from google.oauth2 import service_account

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.snowflake_connection import SnowflakeHook
from utils.logger import get_logger
from .config import (
    DEFAULT_EXPORT_COLUMNS,
    DEFAULT_MULTI_TREATMENT_COLUMNS,
    ALL_AVAILABLE_COLUMNS,
    DEFAULT_SHARE_EMAIL,
    SQL_TEMPLATES_DIR,
    EXPERIMENT_DEFAULTS,
    get_default_share_email,
    SERVICE_ACCOUNT_FILE,
    SCOPES
)

logger = get_logger(__name__)

# Check if Google Sheets is available
try:
    import gspread
    GOOGLE_SHEETS_AVAILABLE = True
except ImportError:
    GOOGLE_SHEETS_AVAILABLE = False



def detect_control_variant_from_data(df: pd.DataFrame) -> str:
    """
    Detect which variant is the control based on empty relative_impact/p_value fields.

    Args:
        df: Raw results dataframe with variant_name column

    Returns:
        Control variant name or None if unclear
    """
    if 'variant_name' not in df.columns:
        logger.warning("No variant_name column found - cannot detect control")
        return None

    # Count null percentages for relative impact
    # Raw data has 'metric_impact_relative', renamed data has 'relative_impact'
    rel_impact_col = None
    if 'relative_impact' in df.columns:
        rel_impact_col = 'relative_impact'
    elif 'metric_impact_relative' in df.columns:
        rel_impact_col = 'metric_impact_relative'

    # Aggregate by variant to check which has most null values
    if rel_impact_col:
        # For each variant, count the percentage of null values
        variant_null_percentages = []
        for variant in df['variant_name'].unique():
            variant_df = df[df['variant_name'] == variant]
            # Control variant should have 100% null values for relative_impact
            # Treatment variants should have a mix (null for control comparisons)
            total_rows = len(variant_df)
            if total_rows == 0:
                continue

            null_rows = variant_df[rel_impact_col].isna().sum()
            null_percentage = null_rows / total_rows * 100
            variant_null_percentages.append((variant, null_percentage))

            if null_percentage > 80:  # More than 80% null - likely control
                logger.info(f"Variant '{variant}' has {null_percentage:.1f}% null {rel_impact_col} values - likely control")
            else:
                logger.debug(f"Variant '{variant}' has {null_percentage:.1f}% null {rel_impact_col} values - likely treatment")

        # Sort by null percentage descending
        control_candidates = sorted(variant_null_percentages, key=lambda x: x[1], reverse=True)

        # If top candidate has significantly more nulls than others, it's control
        if control_candidates and control_candidates[0][1] > 80 and (len(control_candidates) == 1 or control_candidates[0][1] - control_candidates[1][1] > 20):
            control_variant = control_candidates[0][0]
            logger.info(f"Detected control variant '{control_variant}' based on {control_candidates[0][1]:.1f}% null {rel_impact_col} values")
            return control_variant

    # Fallback: Check if there's a variant literally named 'control'
    variants = df['variant_name'].unique()
    for v in variants:
        if v.lower() == 'control':
            logger.info(f"Found variant named '{v}' - using as control")
            return v

    logger.warning("Could not reliably detect control variant from data")
    return None







def filter_results(df: pd.DataFrame,
                  selected_metrics: Optional[List[str]] = None,
                  dimension_names: Optional[List[str]] = None,
                  dimension_cuts: Optional[List[str]] = None,
                  dimension_selection: Optional[Union[str, Dict[str, Dict[str, List[str]]]]] = None,
                  selected_columns: Optional[List[str]] = None,
                  treatment_variants: Optional[List[str]] = None,
                  control_variant: Optional[str] = None) -> pd.DataFrame:
    """
    Filter the results DataFrame based on user selections.

    Args:
        df: Original results DataFrame (must have dimension_name and dimension_cut_name columns)
        selected_metrics: List of metric names or None for all
        dimension_names: Simple global filtering - gets ALL cuts for these dimension names
            (e.g., ['ent_pizza_biz'] returns all pizza business cuts)
        dimension_cuts: Simple global filtering - gets ONLY these specific dimension cuts
            (e.g., ['ent_pizza_biz_pji', 'ent_pizza_biz_pji x pizza_transformed_transformed'])
        dimension_selection: Advanced per-metric dimension filtering. Can be:
            - 'all' or None: Include all dimensions
            - 'overall_only': Only overall results
            - Dict[str, Dict[str, List[str]]]: Different dimensions for different metrics:
                {metric_name: {'names': [...], 'cuts': [...]}}
        selected_columns: List of columns to include in output (defaults to DEFAULT_EXPORT_COLUMNS if None)
        treatment_variants: List of treatment variants to include (e.g., ['treatment_1', 'treatment_3'])
            Control is always included. None = include all variants.
        control_variant: Name of the variant to treat as control (for non-standard naming)

    Returns:
        Filtered DataFrame
    """
    # Make a copy to avoid modifying original
    filtered_df = df.copy()

    # Handle 'default' string by converting to None (will trigger default column selection later)
    if selected_columns == 'default':
        selected_columns = None
        logger.info("Converting 'default' to None for automatic column selection")

    # Determine the control variant name
    if 'variant_name' in filtered_df.columns:
        if control_variant:
            # User specified custom control
            actual_control = control_variant
            logger.info(f"Using custom control variant: {actual_control}")
        else:
            # Look for standard control variant (case-insensitive)
            variants = filtered_df['variant_name'].unique()
            control_matches = [v for v in variants if v.lower() == 'control']
            if control_matches:
                actual_control = control_matches[0]  # Use the first match
            else:
                # No control found - this should have been caught earlier
                logger.warning("No 'control' variant found and no custom control specified")
                actual_control = 'control'  # Default fallback
    else:
        actual_control = 'control'

    # Filter treatment variants if specified
    if treatment_variants is not None and 'variant_name' in filtered_df.columns:
        # Always include the control variant
        variants_to_include = [actual_control] + treatment_variants
        logger.info(f"Filtering to {len(variants_to_include)} variants: {', '.join(variants_to_include)}")
        filtered_df = filtered_df[filtered_df['variant_name'].isin(variants_to_include)]

        # Check if all requested variants were found
        found_variants = set(filtered_df['variant_name'].unique())
        missing_variants = set(treatment_variants) - found_variants
        if missing_variants:
            logger.warning(f"Warning: {len(missing_variants)} variants not found: {', '.join(missing_variants)}")

        # Check if control was found
        if actual_control not in found_variants and control_variant:
            logger.warning(f"Warning: Specified control variant '{actual_control}' not found")

    # Filter metrics if specified
    if selected_metrics:
        logger.info(f"Filtering to {len(selected_metrics)} selected metrics")
        filtered_df = filtered_df[filtered_df['metric_name'].isin(selected_metrics)]

        # Check if all requested metrics were found
        found_metrics = set(filtered_df['metric_name'].unique())
        missing_metrics = set(selected_metrics) - found_metrics
        if missing_metrics:
            logger.warning(f"Warning: {len(missing_metrics)} metrics not found: {', '.join(missing_metrics)}")

    # Handle dimension filtering
    # First check dimension_selection parameter for advanced per-metric filtering
    if dimension_selection is not None:
        if dimension_selection == 'overall_only':
            logger.info("Filtering to overall results only")
            filtered_df = filtered_df[filtered_df['dimension_cut_name'] == 'overall']
        elif dimension_selection == 'all':
            # No filtering needed
            pass
        elif isinstance(dimension_selection, dict):
            # Per-metric dimension filtering
            logger.info("Applying per-metric dimension filtering")

            filtered_parts = []
            # Always include overall results for all metrics
            overall_df = filtered_df[filtered_df['dimension_cut_name'] == 'overall']
            filtered_parts.append(overall_df)

            # Process each metric's requirements
            for metric, dim_config in dimension_selection.items():
                if isinstance(dim_config, dict):
                    # New structure: {'names': [...], 'cuts': [...]}
                    metric_dim_names = dim_config.get('names', [])
                    metric_dim_cuts = dim_config.get('cuts', [])

                    if metric_dim_names:
                        metric_df = filtered_df[
                            (filtered_df['metric_name'] == metric) &
                            (filtered_df['dimension_name'].isin(metric_dim_names)) &
                            (filtered_df['dimension_cut_name'] != 'overall')
                        ]
                        if not metric_df.empty:
                            filtered_parts.append(metric_df)

                    if metric_dim_cuts:
                        metric_df = filtered_df[
                            (filtered_df['metric_name'] == metric) &
                            (filtered_df['dimension_cut_name'].isin(metric_dim_cuts)) &
                            (filtered_df['dimension_cut_name'] != 'overall')
                        ]
                        if not metric_df.empty:
                            filtered_parts.append(metric_df)

            # Combine all parts
            if filtered_parts:
                filtered_df = pd.concat(filtered_parts, ignore_index=True).drop_duplicates()
            else:
                filtered_df = pd.DataFrame()

    else:
        # Use simple global filtering parameters
        filtered_parts = []

        # Always include overall
        overall_df = filtered_df[filtered_df['dimension_cut_name'] == 'overall']
        filtered_parts.append(overall_df)

        # Filter by dimension names (gets all cuts for these dimensions)
        if dimension_names:
            logger.info(f"Filtering by {len(dimension_names)} dimension names (all cuts per dimension)")
            dim_name_df = filtered_df[
                (filtered_df['dimension_name'].isin(dimension_names)) &
                (filtered_df['dimension_cut_name'] != 'overall')
            ]
            if not dim_name_df.empty:
                filtered_parts.append(dim_name_df)
                logger.info(f"  Found {len(dim_name_df)} rows for specified dimensions")

            # Check if all requested dimensions were found
            found_dimensions = set(dim_name_df['dimension_name'].unique())
            missing_dimensions = set(dimension_names) - found_dimensions
            if missing_dimensions:
                logger.warning(f"  Warning: {len(missing_dimensions)} dimensions not found: {', '.join(missing_dimensions)}")

        # Filter by specific dimension cuts
        if dimension_cuts:
            logger.info(f"Filtering by {len(dimension_cuts)} specific dimension cuts")
            dim_cut_df = filtered_df[
                (filtered_df['dimension_cut_name'].isin(dimension_cuts)) &
                (filtered_df['dimension_cut_name'] != 'overall')
            ]
            if not dim_cut_df.empty:
                filtered_parts.append(dim_cut_df)
                logger.info(f"  Found {len(dim_cut_df)} rows for specified cuts")

            # Check if all requested cuts were found
            found_cuts = set(dim_cut_df['dimension_cut_name'].unique())
            missing_cuts = set(dimension_cuts) - found_cuts - {'overall'}  # Don't warn about 'overall'
            if missing_cuts:
                logger.warning(f"  Warning: {len(missing_cuts)} dimension cuts not found: {', '.join(list(missing_cuts)[:5])}")

        # Combine all parts
        if filtered_parts:
            filtered_df = pd.concat(filtered_parts, ignore_index=True).drop_duplicates()
        else:
            # If no dimension filtering, include everything
            pass

    # Sort results for better readability
    if not filtered_df.empty:
        # Detect if we have variant_name column for multi-treatment experiments
        if 'variant_name' in filtered_df.columns:
            # For multi-treatment, sort by metric, dimension, and variant (control first)
            # Identify control variant by checking for empty rel_effect values
            control_variant_name = None
            # Check for both possible column names (raw or formatted)
            rel_impact_col = 'relative_impact' if 'relative_impact' in filtered_df.columns else 'metric_impact_relative'
            if rel_impact_col in filtered_df.columns:
                # Find variant(s) with NaN/empty relative_impact (these are control)
                control_mask = filtered_df[rel_impact_col].isna() | (filtered_df[rel_impact_col] == '')
                if control_mask.any():
                    control_variants = filtered_df[control_mask]['variant_name'].unique()
                    if len(control_variants) > 0:
                        control_variant_name = control_variants[0]
                        logger.info(f"Detected control variant '{control_variant_name}' based on empty {rel_impact_col} values")

            # Create sort order with control first
            def variant_sort_key(x):
                if x.name == 'variant_name':
                    # Put control variant first (index 0), all others after
                    return x.map({control_variant_name: '0'}).fillna('1_' + x.astype(str))
                elif x.name == 'dimension_cut_name':
                    return x.map({'overall': '0'}).fillna(x)
                else:
                    return x

            filtered_df = filtered_df.sort_values(
                by=['metric_name', 'dimension_cut_name', 'variant_name'],
                key=variant_sort_key
            ).reset_index(drop=True)
        else:
            # Single treatment or old format - sort without variant_name
            filtered_df = filtered_df.sort_values(
                by=['metric_name', 'dimension_cut_name'],
                key=lambda x: x if x.name != 'dimension_cut_name' else x.map({'overall': '0'}).fillna(x)
            ).reset_index(drop=True)

    # CRITICAL: Always include analyzed_at column if it exists (for metadata display)
    if 'analyzed_at' in filtered_df.columns:
        if selected_columns is not None and 'analyzed_at' not in selected_columns:
            selected_columns = selected_columns + ['analyzed_at']
            logger.info("Added analyzed_at column for metadata display")

    # Column filtering - only apply if columns are specified
    if selected_columns is not None:
        # Ensure all requested columns exist
        available_cols = [col for col in selected_columns if col in filtered_df.columns]
        missing_cols = set(selected_columns) - set(available_cols)
        if missing_cols:
            logger.warning(f"Warning: {len(missing_cols)} columns not found: {', '.join(missing_cols)}")

        # Apply column filter
        filtered_df = filtered_df[available_cols]
        logger.info(f"Filtered to {len(available_cols)} columns")
    else:
        logger.info("No column filtering applied (selected_columns=None)")

    logger.info(f"Filtered results: {len(filtered_df)} rows")
    return filtered_df





def load_curie_results(
    experiment_name: str,
    override_treatment_count: Optional[int] = None,
    skip_pivoting: bool = False,
    control_variant: Optional[str] = None
) -> pd.DataFrame:
    """
    Load experiment results from Snowflake.

    This now returns raw unpivoted data. All formatting is handled by ExperimentDataFormatter.

    Args:
        experiment_name: Name of the experiment
        override_treatment_count: Override auto-detected treatment count
        skip_pivoting: DEPRECATED - kept for backward compatibility
        control_variant: Name of control variant (defaults to 'control')

    Returns:
        Raw unpivoted DataFrame from Snowflake
    """
    from utils.snowflake_connection import SnowflakeHook

    # Read SQL query from file
    from pathlib import Path
    sql_file = Path(__file__).parent / 'sql' / 'combined_curie_results_unified.sql'
    with open(sql_file, 'r') as f:
        unified_query = f.read()

    # Get SQL query
    final_query = unified_query.replace("{analysis_name}", experiment_name)

    # Execute query
    snowhook = SnowflakeHook()
    results_df = snowhook.query_snowflake(final_query, method='pandas')

    # Basic error checking
    if results_df.empty:
        logger.error(f"No data returned for experiment {experiment_name}")
        return results_df

    # Log data summary
    n_rows = len(results_df)
    n_metrics = results_df['metric_name'].nunique() if 'metric_name' in results_df else 0
    n_dimensions = results_df['dimension_name'].nunique() if 'dimension_name' in results_df else 0
    n_variants = results_df['variant_name'].nunique() if 'variant_name' in results_df else 0

    logger.info(f"Loaded {n_rows} rows: {n_metrics} metrics, {n_dimensions} dimensions, {n_variants} variants")

    # No formatting here - just return raw data
    return results_df




def get_google_sheets_client(use_oauth=False):
    """
    Get Google Sheets client using either service account or OAuth authentication.

    Args:
        use_oauth (bool): If True, use OAuth authentication. If False, use service account.

    Returns:
        gspread.Client: Authenticated Google Sheets client
    """
    try:
        if use_oauth:
            # OAuth authentication - sheets will be owned by the authenticated user
            logger.info("Using OAuth authentication for Google Sheets")

            # Get paths relative to project root
            project_root = Path(__file__).parent.parent.parent
            oauth_creds_path = project_root / "credentials" / "google_oauth_credentials.json"
            oauth_token_path = project_root / "credentials" / "google_oauth_token.json"

            # Also check the config directory (alternative location)
            config_creds_path = project_root / "config" / "google_oauth_credentials.json"
            config_token_path = project_root / "config" / "google_oauth_token.json"

            # Also check the default gspread location as fallback
            default_creds_path = os.path.expanduser("~/.config/gspread/credentials.json")
            default_token_path = os.path.expanduser("~/.config/gspread/authorized_user.json")

            # Use project credentials if they exist, check multiple locations
            if oauth_creds_path.exists():
                logger.info(f"Using OAuth credentials from project: {oauth_creds_path}")
                creds_file = str(oauth_creds_path)
                token_file = str(oauth_token_path)
            elif config_creds_path.exists():
                logger.info(f"Using OAuth credentials from config: {config_creds_path}")
                creds_file = str(config_creds_path)
                token_file = str(config_token_path)
            elif os.path.exists(default_creds_path):
                logger.info(f"Using OAuth credentials from default location: {default_creds_path}")
                creds_file = default_creds_path
                token_file = default_token_path
            else:
                logger.error(f"OAuth credentials file not found at {oauth_creds_path}, {config_creds_path}, or {default_creds_path}")
                logger.info("Please place your OAuth credentials at: credentials/google_oauth_credentials.json or config/google_oauth_credentials.json")
                raise FileNotFoundError(f"OAuth credentials file not found")

            # Use gspread's OAuth flow with specified paths
            client = gspread.oauth(
                credentials_filename=creds_file,
                authorized_user_filename=token_file
            )
            logger.info("Successfully authenticated with OAuth")

        else:
            # Service account authentication (existing code)
            logger.info("Using service account authentication for Google Sheets")

            # Get service account file from config
            from .config import SERVICE_ACCOUNT_FILE, SCOPES

            if not os.path.exists(SERVICE_ACCOUNT_FILE):
                logger.error(f"Service account file not found at {SERVICE_ACCOUNT_FILE}")
                raise FileNotFoundError(f"Service account file not found at {SERVICE_ACCOUNT_FILE}")

            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES
            )
            client = gspread.authorize(creds)
            logger.info("Successfully authenticated with service account")

        return client

    except Exception as e:
        logger.error(f"Error authenticating with Google Sheets: {str(e)}")
        raise








def export_to_csv(df: pd.DataFrame, analysis_name: str) -> str:
    """
    Export results to CSV file in user-analysis/curie_export/{experiment_name}/ directory.

    Args:
        df: Results DataFrame
        analysis_name: Name of the analysis/experiment

    Returns:
        Path to the created CSV file
    """
    # Get the project root directory (3 levels up from this file)
    project_root = Path(__file__).parent.parent.parent

    # Create directory structure: user-analysis/curie_export/{experiment_name}
    user_analysis_dir = project_root / "user-analysis"
    curie_export_dir = user_analysis_dir / "curie_export"
    experiment_dir = curie_export_dir / analysis_name

    # Create directories if they don't exist
    # The exist_ok=True parameter ensures no error if directory already exists
    experiment_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Using directory: {experiment_dir}")

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    csv_filename = f"curie_{analysis_name}_{timestamp}.csv"
    csv_file = experiment_dir / csv_filename

    # Save DataFrame to CSV
    df.to_csv(csv_file, index=False)
    logger.info(f"Results saved as CSV: {csv_file}")

    # Return as string for compatibility
    return str(csv_file)


