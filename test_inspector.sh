#!/bin/bash
# Test MCP server with inspector

echo "Starting MCP Inspector..."
echo ""
echo "Make sure you have activated the venv:"
echo "  source venv/bin/activate"
echo ""

# Run the inspector
npx @modelcontextprotocol/inspector python -m cursor_analytics_mcp.server
