#!/bin/bash
# 
# Shell wrapper for sql_to_sheets_mcp.py
# Makes it easier to run SQL queries and export to Google Sheets
#
# Usage:
#   ./sql_to_sheets.sh -f query.sql -s spreadsheet_id -n sheet_name
#   ./sql_to_sheets.sh -q "SELECT * FROM table" -s spreadsheet_id -n sheet_name

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate virtual environment if it exists
if [ -f "${SCRIPT_DIR}/../venv/bin/activate" ]; then
    source "${SCRIPT_DIR}/../venv/bin/activate"
fi

# Run the Python script with all passed arguments
python3 "${SCRIPT_DIR}/sql_to_sheets_mcp.py" "$@"