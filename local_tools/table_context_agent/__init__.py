"""
Local development tool for building rich Snowflake table context markdown files.

This package is NOT part of the MCP server. It can be invoked directly as a CLI
to generate or update files under `context/analysis-context/snowflake-table-context/`.

Modules:
- agent.py: Orchestrates data collection, LLM synthesis (via Portkey), and rendering
- tyler_sources.py: Queries Tyler Anderson's metadata/usage tables
- snowflake_explorer.py: Heuristics to infer table granularity using SnowflakeHook
- confluence_client.py: Optional Confluence search using REST API
- renderer.py: Produces the final markdown content
"""

__all__ = [
    "agent",
    "tyler_sources",
    "snowflake_explorer",
    "confluence_client",
    "renderer",
]

