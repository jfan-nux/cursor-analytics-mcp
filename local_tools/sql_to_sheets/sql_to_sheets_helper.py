#!/usr/bin/env python3
"""
SQL to Google Sheets Export Helper

This module provides functionality to execute SQL queries and export results
directly to Google Sheets using the MCP Google Sheets functions.

Integrates with the existing curie_export Google Sheets configuration and setup.
"""

import json
import pandas as pd
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any

# Import curie_export configuration for Google Sheets setup
from local_tools.curie_export.config import (
    get_default_share_email,
    get_google_credentials,
    SCOPES,
    OUTPUT_DIR
)
from utils.snowflake_connection import SnowflakeHook
from utils.logger import get_logger


class SQLToSheetsExporter:
    """
    SQL to Google Sheets exporter that integrates with existing MCP infrastructure.
    
    Uses the same Google Sheets configuration as curie_export for consistency.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the SQL to Sheets exporter.
        
        Args:
            logger: Optional logger instance. If None, creates a new one.
        """
        self.logger = logger or get_logger(__name__)
        self.snowhook = None
        
        # Validate Google Sheets credentials configuration
        try:
            self.credentials_file = get_google_credentials()
            self.logger.info(f"Google Sheets credentials configured: {self.credentials_file}")
        except FileNotFoundError as e:
            self.logger.error(f"Google Sheets credentials error: {e}")
            raise
    
    def _get_snowflake_connection(self) -> SnowflakeHook:
        """Get or create Snowflake connection."""
        if self.snowhook is None:
            self.snowhook = SnowflakeHook()
        return self.snowhook
    
    def execute_sql(self, query: str, method: str = 'pandas') -> Tuple[pd.DataFrame, float]:
        """
        Execute SQL query and return DataFrame with execution time.
        
        Args:
            query: SQL query string to execute
            method: Execution method ('pandas', 'spark', 'polars')
            
        Returns:
            Tuple of (DataFrame, execution_time_seconds)
        """
        self.logger.info("Executing SQL query...")
        start_time = datetime.now()
        
        sf = self._get_snowflake_connection()
        df = sf.query_snowflake(query, method=method)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        self.logger.info(f"Query completed in {execution_time:.2f} seconds")
        self.logger.info(f"Retrieved {len(df)} rows and {len(df.columns)} columns")
        
        return df, execution_time
    
    def prepare_sheet_data(self, df: pd.DataFrame) -> List[List[Any]]:
        """
        Prepare DataFrame for Google Sheets export.
        
        Args:
            df: DataFrame to prepare
            
        Returns:
            List of lists suitable for Google Sheets
        """
        # Header row
        sheet_data = [list(df.columns)]
        
        # Data rows - handle different data types appropriately
        for _, row in df.iterrows():
            formatted_row = []
            for val in row:
                if pd.isna(val) or val is None:
                    formatted_row.append("")
                elif isinstance(val, (int, float)):
                    # Keep numbers as numbers for Google Sheets
                    if pd.isna(val):
                        formatted_row.append("")
                    else:
                        formatted_row.append(val)
                elif isinstance(val, datetime):
                    # Format datetime objects
                    formatted_row.append(val.strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    # Convert everything else to string
                    formatted_row.append(str(val))
            sheet_data.append(formatted_row)
        
        return sheet_data
    
    def calculate_sheet_range(self, num_rows: int, num_cols: int) -> str:
        """
        Calculate the A1 notation range for Google Sheets.
        
        Args:
            num_rows: Number of rows
            num_cols: Number of columns
            
        Returns:
            Range string in A1 notation (e.g., "A1:Z100")
        """
        def col_num_to_letter(n):
            """Convert column number to letter(s)."""
            result = ""
            while n > 0:
                n -= 1
                result = chr(65 + n % 26) + result
                n //= 26
            return result
        
        return f"A1:{col_num_to_letter(num_cols)}{num_rows}"
    
    def save_backup_csv(self, df: pd.DataFrame, sheet_name: str, 
                       output_dir: Optional[str] = None) -> str:
        """
        Save DataFrame as CSV backup.
        
        Args:
            df: DataFrame to save
            sheet_name: Name for the file
            output_dir: Directory to save to (defaults to OUTPUT_DIR)
            
        Returns:
            Path to the saved file
        """
        if output_dir is None:
            output_dir = OUTPUT_DIR
        
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"sql_export_{sheet_name}_{timestamp}.csv"
        filepath = Path(output_dir) / filename
        
        # Save CSV
        df.to_csv(filepath, index=False)
        self.logger.info(f"Backup CSV saved to: {filepath}")
        
        return str(filepath)
    
    def export_sql_to_sheets(
        self,
        query: Optional[str] = None,
        sql_file: Optional[str] = None,
        spreadsheet_id: str = None,
        sheet_name: str = None,
        create_spreadsheet: bool = False,
        spreadsheet_title: Optional[str] = None,
        method: str = 'pandas',
        save_backup: bool = True,
        share_email: Optional[str] = None,
        output_dir: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Complete SQL to Google Sheets export workflow.
        
        Args:
            query: SQL query string (mutually exclusive with sql_file)
            sql_file: Path to SQL file (mutually exclusive with query)
            spreadsheet_id: Google Sheets spreadsheet ID (required if not creating new)
            sheet_name: Name of sheet/tab to create or update (required)
            create_spreadsheet: Whether to create a new spreadsheet
            spreadsheet_title: Title for new spreadsheet (if creating)
            method: SQL execution method ('pandas', 'spark', 'polars')
            save_backup: Whether to save a local CSV backup
            share_email: Email to share the spreadsheet with
            output_dir: Directory for backup files
            
        Returns:
            Dictionary with export results and metadata
        """
        # Validate inputs
        if not query and not sql_file:
            raise ValueError("Either query or sql_file must be provided")
        if query and sql_file:
            raise ValueError("Cannot specify both query and sql_file")
        if not create_spreadsheet and not spreadsheet_id:
            raise ValueError("spreadsheet_id required when not creating new spreadsheet")
        if not sheet_name:
            raise ValueError("sheet_name is required")
        
        try:
            # Get SQL query
            if sql_file:
                self.logger.info(f"Reading SQL from file: {sql_file}")
                sql_path = Path(sql_file)
                if not sql_path.exists():
                    raise FileNotFoundError(f"SQL file not found: {sql_file}")
                with open(sql_path, 'r') as f:
                    final_query = f.read()
            else:
                final_query = query
            
            # Log query preview
            query_preview = final_query.replace('\n', ' ').strip()[:200]
            self.logger.info(f"SQL Query Preview: {query_preview}...")
            
            # Execute SQL query
            df, execution_time = self.execute_sql(final_query, method)
            
            if len(df) == 0:
                self.logger.warning("Query returned no results")
                return {
                    'status': 'warning',
                    'message': 'Query returned no results',
                    'execution_time': execution_time,
                    'row_count': 0,
                    'col_count': 0
                }
            
            # Prepare data for Google Sheets
            self.logger.info("Preparing data for Google Sheets export...")
            sheet_data = self.prepare_sheet_data(df)
            range_str = self.calculate_sheet_range(len(sheet_data), len(sheet_data[0]))
            
            # Save backup if requested
            backup_file = None
            if save_backup:
                backup_file = self.save_backup_csv(df, sheet_name, output_dir)
            
            # Get default share email if not provided
            if share_email is None:
                share_email = get_default_share_email()
            
            # Actually export to Google Sheets using gspread
            sheets_result = None
            try:
                self.logger.info(f"Exporting to Google Sheets...")
                
                # Import and setup gspread
                try:
                    import gspread
                    from google.oauth2.service_account import Credentials
                    
                    # Get credentials
                    creds = Credentials.from_service_account_file(
                        self.credentials_file, 
                        scopes=SCOPES
                    )
                    gc = gspread.authorize(creds)
                    
                except ImportError:
                    self.logger.error("gspread not installed. Please install: pip install gspread")
                    raise Exception("gspread library not available")
                
                if create_spreadsheet and spreadsheet_title:
                    # Create new spreadsheet
                    self.logger.info(f"Creating new spreadsheet: {spreadsheet_title}")
                    spreadsheet = gc.create(spreadsheet_title)
                    spreadsheet_id = spreadsheet.id
                    self.logger.info(f"Created spreadsheet with ID: {spreadsheet_id}")
                    
                    # Share if email provided
                    if share_email:
                        try:
                            spreadsheet.share(share_email, perm_type='user', role='writer')
                            self.logger.info(f"Shared spreadsheet with {share_email}")
                        except Exception as e:
                            self.logger.warning(f"Could not share spreadsheet: {str(e)}")
                else:
                    # Open existing spreadsheet
                    spreadsheet = gc.open_by_key(spreadsheet_id)
                
                if spreadsheet_id:
                    # Create new sheet/tab if needed
                    try:
                        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=len(sheet_data)+10, cols=len(df.columns)+2)
                        self.logger.info(f"Created new sheet: {sheet_name}")
                    except Exception as e:
                        # Sheet might already exist, try to get it
                        try:
                            worksheet = spreadsheet.worksheet(sheet_name)
                            self.logger.info(f"Using existing sheet: {sheet_name}")
                        except:
                            # Use the first sheet if all else fails
                            worksheet = spreadsheet.sheet1
                            worksheet.update_title(sheet_name)
                            self.logger.info(f"Updated first sheet title to: {sheet_name}")
                    
                    # Write data to sheet
                    worksheet.clear()  # Clear existing data
                    worksheet.update(range_str, sheet_data)
                    
                    sheets_result = {
                        'spreadsheet_id': spreadsheet_id,
                        'sheet_name': sheet_name,
                        'range': range_str,
                        'updated_cells': len(sheet_data) * len(df.columns),
                        'updated_rows': len(sheet_data),
                        'updated_columns': len(df.columns)
                    }
                    
                    self.logger.info(f"Successfully wrote {len(sheet_data)} rows to Google Sheets")
                
            except Exception as e:
                self.logger.error(f"Error writing to Google Sheets: {str(e)}")
                sheets_result = {'error': str(e)}
            
            # Prepare return data
            export_result = {
                'status': 'success',
                'execution_time': execution_time,
                'row_count': len(df),
                'col_count': len(df.columns),
                'query_preview': query_preview,
                'backup_file': backup_file,
                'spreadsheet_id': spreadsheet_id,
                'sheet_name': sheet_name,
                'sheets_result': sheets_result,
                'google_sheets_url': f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}" if spreadsheet_id else None,
                'google_sheets_data': {
                    'spreadsheet_id': spreadsheet_id,
                    'sheet_name': sheet_name,
                    'range': range_str,
                    'data': sheet_data,
                    'create_spreadsheet': create_spreadsheet,
                    'spreadsheet_title': spreadsheet_title,
                    'share_email': share_email
                },
                'dataframe_info': {
                    'columns': list(df.columns),
                    'dtypes': df.dtypes.to_dict(),
                    'shape': df.shape,
                    'preview': df.head(5).to_dict('records') if len(df) > 0 else []
                }
            }
            
            self.logger.info(f"Export completed successfully")
            self.logger.info(f"  Rows: {len(df):,}")
            self.logger.info(f"  Columns: {len(df.columns)}")
            self.logger.info(f"  Range: {range_str}")
            if backup_file:
                self.logger.info(f"  Backup: {backup_file}")
            if spreadsheet_id:
                self.logger.info(f"  Google Sheets: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
            
            return export_result
            
        except Exception as e:
            self.logger.error(f"Error in SQL to Sheets export: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'message': f'Export failed: {str(e)}'
            }


def export_sql_to_sheets(
    query: str,
    sheet_name: str,
    spreadsheet_id: str = "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA",  # Default to your sheet
    max_rows: int = 20000,
    save_backup: bool = True
) -> Dict[str, Any]:
    """
    Simple SQL to Google Sheets export function.
    
    Args:
        query: SQL query string to execute
        sheet_name: Name of the sheet/tab to create
        spreadsheet_id: Google Sheets spreadsheet ID (defaults to your sheet)
        max_rows: Maximum number of rows allowed (default 20,000)
        save_backup: Whether to save a local CSV backup
        
    Returns:
        Export result dictionary with status, URL, and row count
    """
    exporter = SQLToSheetsExporter()
    
    # First execute the query to check row count
    try:
        # Get snowflake connection and execute query to check row count
        from utils.snowflake_connection import SnowflakeHook
        snowhook = SnowflakeHook()
        df = snowhook.query_snowflake(query, method='pandas')
        row_count = len(df)
        
        # Check if row count exceeds limit
        if row_count > max_rows:
            return {
                'status': 'error',
                'error': 'too_many_rows',
                'message': f'Query returned {row_count:,} rows, which exceeds the limit of {max_rows:,} rows. Please add LIMIT clause to your query.',
                'row_count': row_count,
                'max_rows': max_rows
            }
        
        # If row count is reasonable, proceed with export
        return exporter.export_sql_to_sheets(
            query=query,
            spreadsheet_id=spreadsheet_id,
            sheet_name=sheet_name,
            save_backup=save_backup
        )
        
    except Exception as e:
        return {
            'status': 'error',
            'error': 'query_execution_failed',
            'message': f'SQL query execution failed: {str(e)}'
        }
