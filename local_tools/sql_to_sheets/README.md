# SQL to Google Sheets Utility

A general-purpose utility to execute SQL queries against Snowflake and export results to Google Sheets.

## Files

- `sql_to_sheets_mcp.py` - Main Python script with full functionality
- `sql_to_sheets.sh` - Shell wrapper for easier execution
- `sql_to_sheets.py` - Standalone version (deprecated)

## Usage

### Basic Usage

```bash
# Using shell wrapper (recommended)
./local_tools/sql_to_sheets.sh -f path/to/query.sql -s "spreadsheet_id" -n "sheet_name"

# Using Python directly
python local_tools/sql_to_sheets/sql_to_sheets_mcp.py -f path/to/query.sql -s "spreadsheet_id" -n "sheet_name"
```

### Parameters

**Required:**
- `-f, --sql-file`: Path to SQL file to execute
- `-q, --query`: SQL query string (alternative to -f)
- `-s, --spreadsheet-id`: Google Sheets spreadsheet ID
- `-n, --sheet-name`: Name for the sheet/tab

**Optional:**
- `-m, --method`: Query execution method (`pandas` or `spark`, default: `pandas`)
- `-p, --preview`: Show preview of results before exporting
- `--log-level`: Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`)
- `--no-backup`: Skip creating local CSV backup
- `--create-new-sheet`: Force creation of new sheet with timestamp

### Examples

#### Run Funnel Analysis
```bash
cd utils
./sql_to_sheets.sh \
  -f "../sample-analysis/table_exploration/onboarding_complete_funnel_analysis_consumer.sql" \
  -s "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA" \
  -n "FunnelAnalysis" \
  --preview
```

#### Run Inline Query
```bash
./sql_to_sheets.sh \
  -q "SELECT COUNT(*) as total_deliveries FROM edw.finance.dimension_deliveries WHERE delivery_date >= '2025-01-01'" \
  -s "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA" \
  -n "DeliveryCount"
```

#### Run with All Options
```bash
./sql_to_sheets.sh \
  -f "my_analysis.sql" \
  -s "1D45l4noHvjxw2nDfdqjRN3NEoS-8pvpfnshy00X5hcA" \
  -n "MyAnalysis" \
  --method pandas \
  --preview \
  --create-new-sheet \
  --log-level DEBUG
```

## Workflow

1. **Execute SQL**: Connects to Snowflake and runs the query
2. **Process Results**: Converts results to DataFrame and validates
3. **Preview** (optional): Shows data preview and asks for confirmation
4. **Backup**: Saves results to local CSV file (unless `--no-backup`)
5. **Prepare Export**: Formats data for Google Sheets
6. **Export Instructions**: Provides MCP function calls needed

## Integration with MCP Google Sheets

The utility prepares data and provides the exact MCP function calls needed:

1. **Create Sheet** (if new sheet needed):
   ```
   mcp_google-sheets_create_sheet(spreadsheet_id, sheet_name)
   ```

2. **Update Cells**:
   ```
   mcp_google-sheets_update_cells(spreadsheet_id, sheet_name, range, data)
   ```

## Features

- **Flexible Input**: Accept SQL from file or command line
- **Data Validation**: Checks for empty results and data types
- **Local Backup**: Automatically saves CSV backup
- **Preview Mode**: Review results before export
- **Error Handling**: Comprehensive logging and error messages
- **Range Calculation**: Automatically calculates Google Sheets ranges
- **Type Preservation**: Maintains numeric types for Google Sheets

## Output

The utility provides:
- Execution summary (time, row count, columns)
- Local backup file location
- Google Sheets export parameters
- Exact MCP function calls needed
- Data preview (if requested)

## Error Handling

- Validates SQL file existence
- Checks Snowflake connection
- Handles empty query results
- Provides detailed error messages
- Creates backups before export attempts

## Dependencies

- `pandas` - Data manipulation
- `snowflake_connection.py` - Snowflake connectivity
- `logger.py` - Logging utilities
- MCP Google Sheets functions (called separately)

## Notes

- Always creates a local CSV backup unless `--no-backup` is specified
- Handles null values and data type conversions for Google Sheets
- Supports both small and large datasets
- Uses efficient pandas operations for data processing