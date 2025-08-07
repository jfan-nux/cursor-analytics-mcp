#!/usr/bin/env python3
"""
General utility to run SQL queries and export results to Google Sheets using MCP.

This version integrates with the MCP Google Sheets functions available in the environment.

Usage:
    python sql_to_sheets_mcp.py --query "SELECT * FROM table" --spreadsheet-id "1234" --sheet-name "Results"
    python sql_to_sheets_mcp.py --sql-file "path/to/query.sql" --spreadsheet-id "1234" --sheet-name "Results"
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

class SQLToSheetsExporter:
    """Class to handle SQL query execution and Google Sheets export."""
    
    def __init__(self, logger):
        self.logger = logger
        self.snowhook = SnowflakeHook()
    
    def execute_sql(self, query, method='pandas'):
        """Execute SQL query and return DataFrame."""
        self.logger.info("Executing SQL query...")
        start_time = datetime.now()
        
        df = self.snowhook.query_snowflake(query, method=method)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        self.logger.info(f"Query completed in {execution_time:.2f} seconds")
        self.logger.info(f"Retrieved {len(df)} rows and {len(df.columns)} columns")
        
        return df, execution_time
    
    def prepare_sheet_data(self, df):
        """Prepare DataFrame for Google Sheets export."""
        # Header row
        sheet_data = [list(df.columns)]
        
        # Data rows - convert all values to strings and handle nulls
        for _, row in df.iterrows():
            formatted_row = []
            for val in row:
                if pd.isna(val) or val is None:
                    formatted_row.append("")
                elif isinstance(val, (int, float)):
                    # Keep numbers as numbers for Google Sheets
                    formatted_row.append(val)
                else:
                    formatted_row.append(str(val))
            sheet_data.append(formatted_row)
        
        return sheet_data
    
    def get_sheet_range(self, num_rows, num_cols):
        """Calculate the range string for Google Sheets."""
        def col_num_to_letter(n):
            result = ""
            while n > 0:
                n -= 1
                result = chr(65 + n % 26) + result
                n //= 26
            return result
        
        return f"A1:{col_num_to_letter(num_cols)}{num_rows}"
    
    def save_backup(self, df, sheet_name):
        """Save results to local CSV as backup."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{sheet_name}_{timestamp}.csv"
        df.to_csv(filename, index=False)
        self.logger.info(f"Backup saved to: {filename}")
        return filename

def main():
    parser = argparse.ArgumentParser(
        description='Run SQL query and export results to Google Sheets',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run inline query
  python sql_to_sheets_mcp.py -q "SELECT * FROM table LIMIT 100" -s "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA" -n "MyResults"
  
  # Run query from file
  python sql_to_sheets_mcp.py -f "../sample-analysis/table_exploration/onboarding_complete_funnel_analysis_consumer.sql" -s "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA" -n "FunnelAnalysis"
        """
    )
    
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
    parser.add_argument('--no-backup', action='store_true',
                       help='Skip creating local CSV backup')
    parser.add_argument('--create-new-sheet', action='store_true',
                       help='Force creation of new sheet (will add timestamp if sheet exists)')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger("sql_to_sheets_mcp", level=getattr(logging, args.log_level))
    
    try:
        # Initialize exporter
        exporter = SQLToSheetsExporter(logger)
        
        # Get the SQL query
        if args.sql_file:
            logger.info(f"Reading SQL from file: {args.sql_file}")
            sql_path = Path(args.sql_file)
            if not sql_path.exists():
                raise FileNotFoundError(f"SQL file not found: {args.sql_file}")
            with open(sql_path, 'r') as f:
                query = f.read()
            logger.info(f"Loaded SQL query from {args.sql_file}")
        else:
            logger.info("Using provided SQL query string")
            query = args.query
        
        # Show query preview
        query_preview = query.replace('\n', ' ').strip()[:200]
        logger.info(f"SQL Query Preview: {query_preview}...")
        
        # Execute query
        df, execution_time = exporter.execute_sql(query, args.method)
        
        if len(df) == 0:
            logger.warning("Query returned no results")
            print("No data to export - query returned 0 rows")
            return
        
        # Show preview if requested
        if args.preview:
            print("\n=== QUERY RESULTS PREVIEW ===")
            print(f"Shape: {df.shape}")
            print(f"Columns: {list(df.columns)}")
            print(f"Data types:")
            for col, dtype in df.dtypes.items():
                print(f"  {col}: {dtype}")
            print("\nFirst 10 rows:")
            print(df.head(10).to_string(index=False))
            print(f"\nLast 5 rows:")
            print(df.tail(5).to_string(index=False))
            
            response = input("\nProceed with export to Google Sheets? (y/n): ").strip().lower()
            if response not in ['y', 'yes']:
                logger.info("Export cancelled by user")
                return
        
        # Create backup if requested
        backup_file = None
        if not args.no_backup:
            backup_file = exporter.save_backup(df, args.sheet_name)
        
        # Prepare data for Google Sheets
        logger.info("Preparing data for Google Sheets export...")
        sheet_data = exporter.prepare_sheet_data(df)
        range_str = exporter.get_sheet_range(len(sheet_data), len(sheet_data[0]))
        
        # Handle sheet name for new sheet creation
        final_sheet_name = args.sheet_name
        if args.create_new_sheet:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M')
            final_sheet_name = f"{args.sheet_name}_{timestamp}"
        
        # Print export information for MCP integration
        print(f"\n=== EXPORT READY ===")
        print(f"Query execution time: {execution_time:.2f} seconds")
        print(f"Rows to export: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        if backup_file:
            print(f"Local backup: {backup_file}")
        print(f"\nGoogle Sheets Export Parameters:")
        print(f"  Spreadsheet ID: {args.spreadsheet_id}")
        print(f"  Sheet Name: {final_sheet_name}")
        print(f"  Range: {range_str}")
        print(f"  Data dimensions: {len(sheet_data)} rows x {len(sheet_data[0])} columns")
        
        # Return structured data for MCP functions
        export_data = {
            'spreadsheet_id': args.spreadsheet_id,
            'sheet_name': final_sheet_name,
            'range': range_str,
            'data': sheet_data,
            'backup_file': backup_file,
            'query_time': execution_time,
            'row_count': len(df),
            'col_count': len(df.columns)
        }
        
        # Print MCP function calls that need to be made
        print(f"\n=== MCP FUNCTION CALLS NEEDED ===")
        if args.create_new_sheet or final_sheet_name != args.sheet_name:
            print(f"1. Create sheet:")
            print(f"   mcp_google-sheets_create_sheet('{args.spreadsheet_id}', '{final_sheet_name}')")
        print(f"2. Update cells:")
        print(f"   mcp_google-sheets_update_cells('{args.spreadsheet_id}', '{final_sheet_name}', '{range_str}', <data>)")
        
        return df, export_data
        
    except Exception as e:
        logger.error(f"Error in SQL to Sheets export: {str(e)}")
        raise

if __name__ == "__main__":
    main()