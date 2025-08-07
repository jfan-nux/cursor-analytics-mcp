#!/usr/bin/env python3
"""
Run script for Cursor Analytics MCP Server
This script sets up the environment and runs the MCP server.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

# Import and run the server
from cursor_analytics_mcp.server import main

if __name__ == "__main__":
    main()