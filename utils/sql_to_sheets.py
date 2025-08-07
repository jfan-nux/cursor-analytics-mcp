#!/usr/bin/env python3
"""
General utility to run SQL queries and export results to Google Sheets.

Usage:
    python sql_to_sheets.py --query "SELECT * FROM table" --spreadsheet-id "1234" --sheet-name "Results"
    python sql_to_sheets.py --sql-file "path/to/query.sql" --spreadsheet-id "1234" --sheet-name "Results"
"""

import argparse
import pandas as pd
import logging
import sys
import os
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from snowflake_connection import SnowflakeHook
from logger import setup_logger

def export_to_google_sheets(df, spreadsheet_id, sheet_name, logger):
    """Export DataFrame to Google Sheets."""
    try:
        # Import Google Sheets MCP functions - they should be available as global functions
        # Try to create a new sheet first
        try:
            logger.info(f"Attempting to create new sheet: {sheet_name}")
            # Note: We'll use the MCP functions that should be available
            # For now, let's create the data structure and show the user how to proceed
            
            # Prepare data for Google Sheets
            sheet_data = [list(df.columns)]  # Header row
            
            # Add data rows, converting all values to strings
            for _, row in df.iterrows():
                sheet_data.append([str(val) if val is not None else "" for val in row])
            
            # Calculate range for the data
            num_rows = len(sheet_data)
            num_cols = len(sheet_data[0])
            
            # Convert column number to letter (A, B, C, ... Z, AA, AB, etc.)
            def col_num_to_letter(n):
                result = ""
                while n > 0:
                    n -= 1
                    result = chr(65 + n % 26) + result
                    n //= 26
                return result
            
            range_str = f"A1:{col_num_to_letter(num_cols)}{num_rows}"
            
            logger.info(f"Prepared data for export:")
            logger.info(f"  Rows: {num_rows} (including header)")
            logger.info(f"  Columns: {num_cols}")
            logger.info(f"  Range: {range_str}")
            
            # Save the data to a local file as backup
            output_file = f"sql_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df.to_csv(output_file, index=False)
            logger.info(f"Results also saved locally to: {output_file}")
            
            # Return the prepared data for manual export
            return {
                'spreadsheet_id': spreadsheet_id,
                'sheet_name': sheet_name,
                'range': range_str,
                'data': sheet_data,
                'local_file': output_file
            }
            
        except Exception as e:
            logger.error(f"Error preparing data for Google Sheets: {e}")
            raise
            
    except Exception as e:
        logger.error(f"Error in Google Sheets export: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Run SQL query and export results to Google Sheets')
    
    # SQL input options (mutually exclusive)
    sql_group = parser.add_mutually_exclusive_group(required=True)
    sql_group.add_argument('--query', '-q', type=str, help='SQL query string to execute')
    sql_group.add_argument('--sql-file', '-f', type=str, help='Path to SQL file to execute')
    
    # Google Sheets options
    parser.add_argument('--spreadsheet-id', '-s', required=True, 
                       help='Google Sheets spreadsheet ID')
    parser.add_argument('--sheet-name', '-n', required=True, 
                       help='Name of the sheet/tab to create or update')
    
    # Optional parameters
    parser.add_argument('--method', '-m', default='pandas', choices=['pandas', 'spark'],
                       help='Method to use for query execution (default: pandas)')
    parser.add_argument('--log-level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    parser.add_argument('--preview', '-p', action='store_true',
                       help='Show preview of results before exporting')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger("sql_to_sheets", level=getattr(logging, args.log_level))
    
    try:
        # Get the SQL query
        if args.sql_file:
            logger.info(f"Reading SQL from file: {args.sql_file}")
            sql_path = Path(args.sql_file)
            if not sql_path.exists():
                raise FileNotFoundError(f"SQL file not found: {args.sql_file}")
            with open(sql_path, 'r') as f:
                query = f.read()
        else:
            logger.info("Using provided SQL query string")
            query = args.query
        
        logger.info(f"SQL Query Preview (first 200 chars): {query[:200]}...")
        
        # Initialize Snowflake connection
        logger.info("Connecting to Snowflake...")
        snowhook = SnowflakeHook()
        
        # Execute query
        logger.info("Executing SQL query...")
        start_time = datetime.now()
        df = snowhook.query_snowflake(query, method=args.method)
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        logger.info(f"Query completed in {execution_time:.2f} seconds")
        logger.info(f"Retrieved {len(df)} rows and {len(df.columns)} columns")
        
        if len(df) == 0:
            logger.warning("Query returned no results")
            return
        
        # Show preview if requested
        if args.preview:
            print("\n=== QUERY RESULTS PREVIEW ===")
            print(f"Shape: {df.shape}")
            print(f"Columns: {list(df.columns)}")
            print("\nFirst 10 rows:")
            print(df.head(10).to_string(index=False))
            
            response = input("\nProceed with export to Google Sheets? (y/n): ")
            if response.lower() not in ['y', 'yes']:
                logger.info("Export cancelled by user")
                return
        
        # Export to Google Sheets
        logger.info(f"Exporting to Google Sheets...")
        logger.info(f"  Spreadsheet ID: {args.spreadsheet_id}")
        logger.info(f"  Sheet Name: {args.sheet_name}")
        
        export_info = export_to_google_sheets(df, args.spreadsheet_id, args.sheet_name, logger)
        
        print(f"\n=== EXPORT SUMMARY ===")
        print(f"Query execution time: {execution_time:.2f} seconds")
        print(f"Rows retrieved: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print(f"Local backup file: {export_info['local_file']}")
        print(f"\nGoogle Sheets Export Info:")
        print(f"  Spreadsheet ID: {export_info['spreadsheet_id']}")
        print(f"  Sheet Name: {export_info['sheet_name']}")
        print(f"  Range: {export_info['range']}")
        print(f"\nTo complete the export, use the MCP Google Sheets functions:")
        print(f"  1. Create sheet (if needed): mcp_google-sheets_create_sheet")
        print(f"  2. Update cells: mcp_google-sheets_update_cells")
        
        return df, export_info
        
    except Exception as e:
        logger.error(f"Error in SQL to Sheets export: {str(e)}")
        raise

if __name__ == "__main__":
    main()