#!/usr/bin/env python3
"""
Cursor Analytics MCP Web Server
Runs the MCP server as a web service with SSE transport (like experimentation-mcp)
"""

import os
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import your existing server
from src.cursor_analytics_mcp.server import mcp

def main():
    """Run the MCP server as a web service with SSE transport"""
    print("🚀 Starting Cursor Analytics MCP Web Server on http://localhost:8080/sse")
    print("📡 Using SSE (Server-Sent Events) transport")
    
    # Run with SSE transport (like experimentation-mcp)
    mcp.run(transport="sse", port=8080, host="0.0.0.0")

if __name__ == "__main__":
    main()
