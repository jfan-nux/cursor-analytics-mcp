#!/bin/bash

# Exit on error
set -e

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Get the project root (parent of utils)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." &> /dev/null && pwd )"

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Error: Python not found. Make sure Python is installed."
    exit 1
fi

# Check if virtual environment exists
if [ -d "$PROJECT_ROOT/venv" ]; then
    echo "Using virtual environment from: $PROJECT_ROOT/venv"
    source "$PROJECT_ROOT/venv/bin/activate"
else
    echo "Warning: Virtual environment not found at $PROJECT_ROOT/venv"
    echo "You may encounter dependency issues. See SETUP.md for instructions."
fi

# Check if the query_search.py script exists
if [ ! -f "$SCRIPT_DIR/query_search.py" ]; then
    echo "Error: query_search.py not found at $SCRIPT_DIR/query_search.py"
    exit 1
fi

# Print usage information if no arguments provided
if [ $# -eq 0 ]; then
    echo "Query Search Tool"
    echo "----------------"
    echo "Usage: ./query_search.sh [--limit N] <keyword1> [keyword2 ...]"
    echo "Examples:"
    echo "  ./query_search.sh preptime"
    echo "  ./query_search.sh --limit 5 eta delivery"
    exit 1
fi

echo "Running query search with arguments: $@"
# Run the query search script
python "$SCRIPT_DIR/query_search.py" "$@" 