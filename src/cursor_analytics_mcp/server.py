#!/usr/bin/env python3
"""
Cursor Analytics MCP Server using FastMCP

A standalone MCP server providing tools for:
- Snowflake operations (query execution, table management)
- Query search functionality  
- Curie experiment exports
- Table context generation and documentation
- Context fetching from various sources
- Cursor rules awareness
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Add local utils to path (utils is in the cursor-analytics-mcp root)
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import local modules
try:
    from utils.snowflake_connection import SnowflakeHook
    from local_tools.curie_export.export_helper import (
        export_curie_with_explicit_params,
        get_experiment_metadata
    )
    from local_tools.sql_to_sheets.sql_to_sheets_helper import export_sql_to_sheets
    from local_tools.google_doc_crawler.doc_crawler import (
        process_google_docs_batch,
        convert_single_google_doc,
        GoogleDocCrawler,
        convert_google_doc_to_markdown_string,
        convert_google_docs_to_markdown_strings
    )
    from utils.logger import get_logger
    # Setup logging
    logger = get_logger(__name__)
except ImportError as e:
    print(f"Warning: Could not import utils modules: {e}")
    print("Make sure the utils directory is properly copied to the project root")
    # Fallback to basic logging
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

# Try to import dual-table hybrid search functionality
try:
    from local_tools.document_indexer.dual_table_search import DualTableHybridSearcher
    HYBRID_SEARCH_AVAILABLE = True
except ImportError:
    print("Warning: Dual-table hybrid search not available. Document indexing may not be set up.")
    HYBRID_SEARCH_AVAILABLE = False

# Try to import table context agent functionality
try:
    from local_tools.table_context_agent.agent import main as generate_table_context
    TABLE_CONTEXT_AVAILABLE = True
except ImportError:
    print("Warning: Table context agent not available.")
    TABLE_CONTEXT_AVAILABLE = False

# Initialize FastMCP server
# Disable banner to prevent JSON parsing errors in MCP Inspector
mcp = FastMCP("Cursor Analytics MCP Server 🚀")

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

# SQL builder helpers to avoid duplicating long query templates in multiple
# query-search utilities.

def _build_most_used_queries_sql(filter_condition: str, limit: int) -> str:
    """Return SQL that fetches the most frequently executed queries limited by a
    caller-supplied filter_condition (e.g. fully qualified table name or keyword
    conditions)."""
    return f"""
    WITH recent_queries AS (
        SELECT 
            query_text,
            dd_user,
            start_time,
            COUNT(*) AS execution_count,
            MAX(start_time) AS latest_execution
        FROM tyleranderson.sf_table_usage
        WHERE {filter_condition}
          AND start_time >= CURRENT_DATE - 30
          AND query_text IS NOT NULL
          AND LENGTH(TRIM(query_text)) > 10
          AND LENGTH(TRIM(query_text)) <= 3000
        GROUP BY query_text, dd_user, start_time
        HAVING execution_count >= 1
        ORDER BY execution_count DESC, latest_execution DESC
        LIMIT {limit * 10}
    ),
    distinct_queries AS (
        SELECT DISTINCT
            query_text,
            SUM(execution_count) AS total_executions,
            MAX(latest_execution) AS most_recent_execution,
            LISTAGG(DISTINCT dd_user, ', ') AS users
        FROM recent_queries
        GROUP BY query_text
        ORDER BY total_executions DESC, most_recent_execution DESC
        LIMIT {limit}
    )
    SELECT 
        query_text,
        total_executions,
        most_recent_execution,
        users
    FROM distinct_queries
    ORDER BY total_executions DESC, most_recent_execution DESC
    """

def _build_fallback_sql(filter_condition: str, limit: int) -> str:
    """Return SQL to fetch representative queries from the most active user when
    the primary query returns no rows. The same filter_condition is applied to
    maintain consistency with the primary search."""
    return f"""
    WITH most_active_user AS (
        SELECT dd_user
        FROM tyleranderson.sf_table_usage
        WHERE {filter_condition}
          AND start_time >= CURRENT_DATE - 30
        GROUP BY dd_user
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ),
    user_queries AS (
        SELECT DISTINCT
            query_text,
            MAX(start_time) AS latest_execution_time,
            dd_user
        FROM tyleranderson.sf_table_usage
        WHERE {filter_condition}
          AND start_time >= CURRENT_DATE - 30
          AND dd_user = (SELECT dd_user FROM most_active_user)
          AND query_text IS NOT NULL
          AND LENGTH(TRIM(query_text)) > 10
          AND LENGTH(TRIM(query_text)) <= 3000
        GROUP BY query_text, dd_user
        ORDER BY latest_execution_time DESC
        LIMIT {limit}
    )
    SELECT 
        query_text,
        1 AS total_executions,
        latest_execution_time AS most_recent_execution,
        dd_user AS users
    FROM user_queries
    ORDER BY latest_execution_time DESC
    """

def get_configured_hybrid_searcher():
    """
    Get a properly configured DualTableHybridSearcher with error handling
    
    Returns:
        DualTableHybridSearcher instance or None if initialization fails
    """
    if not HYBRID_SEARCH_AVAILABLE:
        return None
    
    try:
        # Explicit configuration for dual-table structure
        searcher = DualTableHybridSearcher(database="proddb", schema="fionafan")
        
        # Validate Snowflake connection
        hook = searcher.get_snowflake_hook()
        if not hook:
            logger.error("Failed to establish Snowflake connection")
            return None
            
        return searcher
    except Exception as e:
        logger.error(f"Failed to initialize DualTableHybridSearcher: {str(e)}")
        return None



# ============================================================================
# SNOWFLAKE OPERATIONS
# ============================================================================

@mcp.tool
def execute_snowflake_query(
    query: str,
    method: str = "pandas",
    database: Optional[str] = None,
    schema: Optional[str] = None,
    warehouse: Optional[str] = None
) -> str:
    """
    Execute SQL queries on Snowflake. Operations can be for fethching data or executing non-select statements.
    
    Args:
        query: SQL query to execute
        method: Data processing method (pandas, spark, polars)
        database: Database name (optional)
        schema: Schema name (optional)
        warehouse: Warehouse name (optional)
    
    Returns:
        Query results as formatted string
    """
    try:
        # Create SnowflakeHook with optional parameters
        hook_kwargs = {}
        if database:
            hook_kwargs["database"] = database
        if schema:
            hook_kwargs["schema"] = schema
        if warehouse:
            hook_kwargs["warehouse"] = warehouse
            
        with SnowflakeHook(**hook_kwargs) as sf:
            # Shortcut: Spark path (bypasses pandas logic entirely)
            if method == "spark":
                result = sf.query_snowflake(query, method="spark")
                schema_info = str(result.schema)
                sample_data = result.limit(10).toPandas().to_json(orient="records", date_format="iso")
                return (
                    "Query executed successfully.\n\n"  # noqa: E501
                    f"Schema:\n{schema_info}\n\nSample data (first 10 rows):\n{sample_data}"
                )

            # Default path (pandas fetch with fallback)
            lowered = query.strip().lower()
            is_select = lowered.startswith("select") or lowered.startswith("with")

            try:
                if method == "pandas" and is_select:
                    result = sf.query_snowflake(query, method="pandas")
                    result_json = result.to_json(orient="records", date_format="iso")
                    return (
                        f"Query executed successfully. Returned {len(result)} rows.\n\nData (JSON):\n{result_json}"
                    )
                else:
                    sf.query_without_result(query)
                    return "Statement executed successfully. No result set returned."
            except Exception as fetch_err:
                logger.warning(
                    f"Fetch attempt failed ({fetch_err}); retrying as non-result statement."
                )
                try:
                    sf.query_without_result(query)
                    return "Statement executed successfully (fallback). No result set returned."
                except Exception as e2:
                    logger.error(f"Snowflake query fallback error: {str(e2)}")
                    return f"Error executing query: {str(e2)}"
            # If method is something else not supported
            return f"Method '{method}' not yet implemented"
                
    except Exception as e:
        logger.error(f"Snowflake query error: {str(e)}")
        return f"Error executing query: {str(e)}"





# ============================================================================
# QUERY SEARCH
# ============================================================================

@mcp.tool
def search_queries_by_table_name(
    table_name: str,
    limit: int = 5
) -> str:
    """
    Find the top most used queries for a specific table in the last 30 days.
    
    Args:
        table_name: Full or partial table name (e.g., 'dimension_deliveries' or 'edw.finance.dimension_deliveries')
        limit: Maximum number of queries to return (default: 5)
    
    Returns:
        Formatted list of top queries for the table
    """
    try:
        # Import the table resolution function from tyler_sources
        from local_tools.table_context_agent.tyler_sources import resolve_table_name
        
        with SnowflakeHook() as sf:
            # Step 1: Resolve the table name to fully qualified name
            try:
                full_table_name = resolve_table_name(sf, table_name, verbose=False)
            except Exception:
                # Fallback: use the input as-is if resolution fails
                full_table_name = table_name
            
            # Step 2: Try to find the top most used queries in the last 30 days
            most_used_queries_sql = _build_most_used_queries_sql(
                filter_condition=f"fully_qualified_table_name = '{full_table_name}'",
                limit=limit
            )
            
            result_df = sf.query_snowflake(most_used_queries_sql, method="pandas")
            
            # Step 3: If no frequently used queries found, find most active user and their recent queries
            if result_df.empty:
                fallback_sql = _build_fallback_sql(
                    filter_condition=f"fully_qualified_table_name = '{full_table_name}'",
                    limit=limit
                )
                
                result_df = sf.query_snowflake(fallback_sql, method="pandas")
            
            # Step 4: Format the results
            if result_df.empty:
                return f"No queries found for table '{full_table_name}' in the last 30 days."
            
            response = f"🔍 Top {len(result_df)} queries for table: {full_table_name}\n"
            response += f"📅 Search period: Last 30 days\n"
            response += "=" * 70 + "\n\n"
            
            for i, row in result_df.iterrows():
                execution_count = row.get('total_executions', 1)
                recent_time = row.get('most_recent_execution', 'Unknown')
                users = row.get('users', 'Unknown')
                query_text = row.get('query_text', '')
                
                response += f"--- Query {i + 1} ---\n"
                response += f"📊 Executions: {execution_count}\n"
                response += f"⏰ Most Recent: {recent_time}\n"
                response += f"👤 Users: {users}\n\n"
                
                # Truncate long queries for readability
                if len(query_text) > 1500:
                    truncated_query = query_text[:1500] + "\n... (truncated)"
                else:
                    truncated_query = query_text
                    
                response += f"💻 Query:\n{truncated_query}\n"
                response += "-" * 70 + "\n\n"
            
            return response
            
    except Exception as e:
        logger.error(f"Table query search error: {str(e)}")
        return f"Error searching queries for table '{table_name}': {str(e)}"


@mcp.tool
def search_queries_by_keyword(
    keywords: List[str],
    limit: int = 5
) -> str:
    """
    Find the most frequently executed queries that contain **all** provided
    keywords (case-insensitive) in the query text over the last 30 days.

    Args:
        keywords: List of keywords. Every keyword in this list must appear in
            the query text for a query to be counted.
        limit: Maximum number of queries to return (default 5).

    Returns:
        A formatted string that lists the top queries, their execution counts,
        most-recent execution timestamp, and the users who ran them. If no
        queries match, a human-readable message is returned.
    """
    try:
        if not keywords:
            return "Keyword list is empty – please provide at least one keyword."

        # Build case-insensitive LIKE filters for each keyword
        keyword_conditions = [
            f"UPPER(query_text) LIKE UPPER('%{kw}%')" for kw in keywords
        ]
        filter_condition = " AND ".join(keyword_conditions)

        with SnowflakeHook() as sf:
            most_used_queries_sql = _build_most_used_queries_sql(filter_condition, limit)
            result_df = sf.query_snowflake(most_used_queries_sql, method="pandas")

            # Fallback: pick queries from the most active user if no frequent queries found
            if result_df.empty:
                fallback_sql = _build_fallback_sql(filter_condition, limit)
                result_df = sf.query_snowflake(fallback_sql, method="pandas")

            if result_df.empty:
                return (
                    f"No queries found that contain ALL keywords (" + ", ".join(keywords) + ") in the last 30 days."
                )

            response = (
                f"🔍 Top {len(result_df)} queries containing keywords: "
                f"{', '.join(keywords)}\n"
                f"📅 Search period: Last 30 days\n"
                + "=" * 70 + "\n\n"
            )

            for i, row in result_df.iterrows():
                execution_count = row.get("total_executions", 1)
                recent_time = row.get("most_recent_execution", "Unknown")
                users = row.get("users", "Unknown")
                query_text = row.get("query_text", "")

                response += f"--- Query {i + 1} ---\n"
                response += f"📊 Executions: {execution_count}\n"
                response += f"⏰ Most Recent: {recent_time}\n"
                response += f"👤 Users: {users}\n\n"

                # Truncate long queries for readability
                if len(query_text) > 800:
                    truncated_query = query_text[:800] + "\n... (truncated)"
                else:
                    truncated_query = query_text

                response += f"💻 Query:\n{truncated_query}\n"
                response += "-" * 70 + "\n\n"

            return response

    except Exception as e:
        logger.error(f"Keyword query search error: {str(e)}")
        return f"Error searching queries by keyword: {str(e)}"


# ============================================================================
# SQL TO GOOGLE SHEETS EXPORT
# ============================================================================

@mcp.tool
def execute_sql_and_upload_to_google_sheet(
    query: str,
    tab_name: str,
    spreadsheet_id: Optional[str] = None,
    max_rows: int = 20000,
    spreadsheet_title: Optional[str] = None
) -> str:
    """
    Execute a SQL query (select only) and upload the results to Google Sheets.
    
    Args:
        query: SQL query to execute
        tab_name: Name of the sheet tab to create (e.g., "results", "data", "analysis")
        spreadsheet_id: Google Sheets spreadsheet ID. If None, creates a new spreadsheet.
        max_rows: Maximum rows allowed (default 20,000)
        spreadsheet_title: Title for new spreadsheet (only used if spreadsheet_id is None)
    
    Returns:
        Google Sheets URL
    """
    try:
        import io
        import sys
        from contextlib import redirect_stdout, redirect_stderr
        
        # Capture all output
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        debug_info = []
        debug_info.append("🔧 MCP TOOL: Starting SQL → Google Sheets workflow")
        debug_info.append(f"🔧 MCP TOOL: Received parameters:")
        debug_info.append(f"  - query: {query[:50]}...")
        debug_info.append(f"  - tab_name: {tab_name}")
        debug_info.append(f"  - spreadsheet_id: {spreadsheet_id}")
        debug_info.append(f"  - max_rows: {max_rows}")
        debug_info.append(f"  - spreadsheet_title: {spreadsheet_title}")

        logger.info("Starting SQL → Google Sheets workflow (execute_sql_and_upload_to_google_sheet)…")
        logger.info(f"🔧 MCP TOOL: Received spreadsheet_id={spreadsheet_id}")

        # Capture stdout/stderr during the export
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            result = export_sql_to_sheets(
                query=query,
                sheet_name=tab_name,
                spreadsheet_id=spreadsheet_id,
                max_rows=max_rows,
                spreadsheet_title=spreadsheet_title,
            )
        
        # Get captured output
        captured_stdout = stdout_capture.getvalue()
        captured_stderr = stderr_capture.getvalue()
        
        debug_info.append(f"🔧 MCP TOOL: Result spreadsheet_id={result.get('spreadsheet_id')}")
        debug_info.append(f"🔧 MCP TOOL: Result status={result.get('status')}")
        
        if captured_stdout:
            debug_info.append(f"🔧 CAPTURED STDOUT:\n{captured_stdout}")
        if captured_stderr:
            debug_info.append(f"🔧 CAPTURED STDERR:\n{captured_stderr}")

        logger.info(f"🔧 MCP TOOL: Result spreadsheet_id={result.get('spreadsheet_id')}")

        status = result.get("status", "error")
        if status != "success":
            error_msg = result.get("message", "Unknown error")
            if result.get("error") and result.get("error") not in error_msg:
                error_msg += f" ({result['error']})"
            
            # Include debug info in error response
            debug_log = "\n".join(debug_info)
            return f"❌ Export failed: {error_msg}\n\n=== DEBUG LOG ===\n{debug_log}"

        # Extract URL robustly
        sheet_id_val = result.get("spreadsheet_id") or (result.get("sheets_result") or {}).get("spreadsheet_id")
        sheets_url = result.get("google_sheets_url") or (
            f"https://docs.google.com/spreadsheets/d/{sheet_id_val}" if sheet_id_val else ""
        )

        if not sheets_url:
            debug_log = "\n".join(debug_info)
            return f"❌ Export succeeded but URL could not be determined.\n\n=== DEBUG LOG ===\n{debug_log}"

        # Include debug info in success response
        debug_log = "\n".join(debug_info)
        return f"✅ {sheets_url}\n\n=== DEBUG LOG ===\n{debug_log}"
    except Exception as e:
        logger.error(f"SQL → Google Sheets export error: {str(e)}")
        return f"❌ Error in SQL → Google Sheets export: {str(e)}"


# ============================================================================
# GOOGLE DOCS CRAWLER AND CONVERTER
# ============================================================================

@mcp.tool
def crawl_and_convert_google_docs(
    master_doc_url: str,
    output_path: str = "context/experiment-readouts"
) -> str:
    """
    Crawl all Google Docs links from a master document and convert them to markdown.
    
    This tool performs the complete workflow:
    1. Crawls all Google Docs links from the master document
    2. Converts each document to markdown with proper formatting
    3. Organizes files by team structure (e.g., growth/nux)
    4. Preserves formatting (bold, italic, highlights, tables, lists)
    5. Downloads images to team-specific folders
    
    Args:
        master_doc_url: URL of the Google Doc containing links to other docs
        output_path: Base directory to save converted markdown files
        
    Returns:
        Summary of batch conversion results
    """
    try:
        logger.info(f"Starting Google Docs batch conversion from: {master_doc_url}")
        
        result_json = process_google_docs_batch(master_doc_url, output_path)
        result = json.loads(result_json)
        
        if result['status'] == 'warning':
            return f"⚠️ {result['message']}"
        
        # Format successful response
        response = f"✅ Google Docs batch conversion completed!\n\n"
        response += f"📊 **Results:**\n"
        response += f"- Total links found: {result['total_links']}\n"
        response += f"- Successfully processed: {result['processed_successfully']}\n"
        response += f"- Failed: {result['failed']}\n"
        response += f"- Output path: {result['output_path']}\n\n"
        
        if result['results']:
            response += f"📝 **Converted Documents:**\n"
            for doc_result in result['results'][:10]:  # Show first 10
                if doc_result['status'] == 'success':
                    response += f"- {doc_result['title']} → {doc_result['team_path']}\n"
                else:
                    response += f"- ❌ Failed: {doc_result.get('doc_url', 'Unknown')}\n"
            
            if len(result['results']) > 10:
                response += f"- ... and {len(result['results']) - 10} more\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Google Docs batch conversion error: {str(e)}")
        return f"❌ Error in Google Docs batch conversion: {str(e)}"


@mcp.tool
def convert_single_google_doc_to_markdown(
    doc_url: str,
    output_path: str = "context/experiment-readouts"
) -> str:
    """
    Convert a single Google Doc to markdown format.
    
    This tool converts a Google Doc to markdown while preserving:
    - Text formatting (bold, italic, highlights)
    - Document structure (headings, paragraphs)
    - Tables with proper markdown syntax
    - Bullet points and numbered lists
    - Links and footnotes
    - Team-based file organization
    
    Args:
        doc_url: URL of the Google Doc to convert
        output_path: Base directory to save the markdown file
        
    Returns:
        Conversion results and file location
    """
    try:
        logger.info(f"Converting single Google Doc: {doc_url}")
        
        result_json = convert_single_google_doc(doc_url, output_path)
        result = json.loads(result_json)
        
        if result['status'] == 'success':
            response = f"✅ Google Doc converted successfully!\n\n"
            response += f"📄 **Document:** {result['title']}\n"
            response += f"👥 **Team:** {result['team_path']}\n"
            response += f"📁 **File:** {result['markdown_file']}\n"
            response += f"🖼️ **Images:** {result['images_downloaded']} downloaded\n"
            response += f"🔗 **Source:** {result['doc_url']}\n"
        else:
            response = f"❌ Conversion failed: {result.get('error', 'Unknown error')}"
        
        return response
        
    except Exception as e:
        logger.error(f"Single Google Doc conversion error: {str(e)}")
        return f"❌ Error converting Google Doc: {str(e)}"


@mcp.tool
def get_google_doc_links(doc_url: str) -> str:
    """
    Extract all Google Docs links from a document without converting them.
    
    Useful for previewing what documents would be processed in a batch operation.
    
    Args:
        doc_url: URL of the Google Doc to scan for links
        
    Returns:
        List of Google Docs links found in the document
    """
    try:
        logger.info(f"Extracting links from Google Doc: {doc_url}")
        
        crawler = GoogleDocCrawler()
        links = crawler.crawl_links_from_doc(doc_url)
        
        if not links:
            return "ℹ️ No Google Docs links found in the document."
        
        response = f"📋 Found {len(links)} Google Docs links:\n\n"
        for i, link in enumerate(links, 1):
            response += f"{i}. {link}\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error extracting Google Doc links: {str(e)}")
        return f"❌ Error extracting links: {str(e)}"


@mcp.tool
def convert_google_doc_to_markdown(
    doc_url: str,
    write_file: bool = False,
    output_path: str = "context/experiment-readouts"
) -> str:
    """
    Convert a single Google Doc to markdown with optional file writing.
    
    Returns the markdown content as a string, with option to save to local context folder.
    Preserves all formatting including tables, lists, images, footnotes, and team organization.
    
    Args:
        doc_url: URL of the Google Doc to convert
        write_file: Whether to save markdown to local context folder (default: False)
        output_path: Base directory for saving files (only used if write_file=True)
        
    Returns:
        Markdown content as string, plus metadata about the conversion
    """
    try:
        logger.info(f"Converting Google Doc to markdown: {doc_url}, write_file={write_file}")
        
        result = convert_google_doc_to_markdown_string(doc_url, write_file, output_path)
        
        if result['status'] == 'success':
            response = f"✅ Google Doc converted to markdown successfully!\n\n"
            response += f"📄 **Document:** {result['title']}\n"
            response += f"👥 **Team:** {result['team_path']}\n"
            response += f"🎯 **Quarter:** {result['detected_quarter']}\n"
            response += f"🖼️ **Images:** {result['images_downloaded']} processed\n"
            response += f"📝 **Footnotes:** {result['footnotes_processed']} processed\n"
            
            if write_file:
                response += f"📁 **File saved:** {result['markdown_file']}\n"
            else:
                response += f"📁 **File saved:** No (returned as string only)\n"
            
            response += f"🔗 **Source:** {result['doc_url']}\n\n"
            response += "---\n\n"
            response += "**Markdown Content:**\n\n"
            response += result['markdown_content']
        else:
            response = f"❌ Conversion failed: {result.get('error', 'Unknown error')}"
        
        return response
        
    except Exception as e:
        logger.error(f"Google Doc markdown conversion error: {str(e)}")
        return f"❌ Error converting Google Doc to markdown: {str(e)}"


@mcp.tool
def convert_google_docs_to_markdown_bulk(
    doc_urls: List[str],
    write_files: bool = False,
    output_path: str = "context/experiment-readouts"
) -> str:
    """
    Convert multiple Google Docs to markdown with optional file writing.
    
    Returns a list of markdown contents as strings, with option to save to local context folder.
    Processes documents in parallel for efficiency.
    
    Args:
        doc_urls: List of Google Doc URLs to convert
        write_files: Whether to save markdown files to local context folder (default: False)
        output_path: Base directory for saving files (only used if write_files=True)
        
    Returns:
        Summary of bulk conversion with markdown content for each document
    """
    try:
        logger.info(f"Starting bulk Google Docs to markdown conversion: {len(doc_urls)} documents, write_files={write_files}")
        
        result = convert_google_docs_to_markdown_strings(doc_urls, write_files, output_path)
        
        response = f"✅ Bulk Google Docs conversion completed!\n\n"
        response += f"📊 **Summary:**\n"
        response += f"- Total documents: {result['total_documents']}\n"
        response += f"- Successfully converted: {result['successful_conversions']}\n"
        response += f"- Failed: {result['failed_conversions']}\n"
        response += f"- Files saved: {'Yes' if write_files else 'No (returned as strings only)'}\n\n"
        
        if result['results']:
            response += f"📝 **Converted Documents:**\n\n"
            for i, doc_result in enumerate(result['results'], 1):
                if doc_result['status'] == 'success':
                    response += f"**{i}. {doc_result['title']}**\n"
                    response += f"   - Team: {doc_result['team_path']}\n"
                    response += f"   - Quarter: {doc_result['detected_quarter']}\n"
                    response += f"   - Images: {doc_result['images_downloaded']}\n"
                    response += f"   - Footnotes: {doc_result['footnotes_processed']}\n"
                    if write_files and 'markdown_file' in doc_result:
                        response += f"   - File: {doc_result['markdown_file']}\n"
                    response += f"   - Source: {doc_result['doc_url']}\n\n"
                    response += "   **Markdown Content:**\n\n"
                    response += f"   {doc_result['markdown_content'][:500]}...\n\n"  # Show first 500 chars
                    response += "   ---\n\n"
                else:
                    response += f"**{i}. ❌ Failed Document**\n"
                    response += f"   - URL: {doc_result['doc_url']}\n"
                    response += f"   - Error: {doc_result['error']}\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Bulk Google Docs markdown conversion error: {str(e)}")
        return f"❌ Error in bulk Google Docs markdown conversion: {str(e)}"


# ============================================================================
# CURIE EXPERIMENT EXPORT
# ============================================================================

@mcp.tool
def export_curie_experiment_to_sheet(
    experiment_name: str,
    primary_metrics: Optional[List[str]] = None,
    secondary_metrics: Optional[List[str]] = None,
    guardrail_metrics: Optional[List[str]] = None,
    dimension_names: Optional[List[str]] = None,
    dimension_cuts: Optional[List[str]] = None,
    selected_columns: Optional[List[str]] = None,
    share_email: Optional[str] = None,
    use_oauth: bool = True
) -> str:
    """
    Export Curie experiment results to Google Sheets.
    
    Args:
        experiment_name: Name of the experiment to export
        primary_metrics: List of primary metrics
        secondary_metrics: List of secondary metrics
        guardrail_metrics: List of guardrail metrics
        dimension_names: Dimension names to include (gets all cuts)
        dimension_cuts: Specific dimension cuts to include
        selected_columns: Columns to include in export
        share_email: Email to share the sheet with
        use_oauth: Use OAuth authentication
    
    Returns:
        Export results with URL or error message
    """
    import io
    import sys
    import traceback
    import logging
    from contextlib import redirect_stdout, redirect_stderr
    
    # Capture all output and logs
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    log_capture = io.StringIO()
    
    # Create a custom log handler to capture all log messages
    log_handler = logging.StreamHandler(log_capture)
    log_handler.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_formatter)
    
    # Add handler to all relevant loggers
    loggers_to_capture = [
        'local_tools.curie_export.export_helper',
        'local_tools.curie_export.curie_to_sheets',
        'local_tools.curie_export.google_sheets_formatter',
        'local_tools.curie_export.experiment_formatter',
        'utils.snowflake_connection',
        'utils.logger'
    ]
    
    # Also add to root logger to catch everything
    root_logger = logging.getLogger()
    root_logger.addHandler(log_handler)
    original_root_level = root_logger.level
    root_logger.setLevel(logging.DEBUG)
    
    original_handlers = {}
    for logger_name in loggers_to_capture:
        log = logging.getLogger(logger_name)
        original_handlers[logger_name] = log.handlers.copy()  # Save original handlers
        log.addHandler(log_handler)
        log.setLevel(logging.DEBUG)
    
    debug_info = []
    debug_info.append("🔧 MCP CURIE EXPORT: Starting export workflow")
    debug_info.append(f"🔧 Parameters:")
    debug_info.append(f"  - experiment_name: {experiment_name}")
    debug_info.append(f"  - primary_metrics: {primary_metrics}")
    debug_info.append(f"  - secondary_metrics: {secondary_metrics}")
    debug_info.append(f"  - guardrail_metrics: {guardrail_metrics}")
    debug_info.append(f"  - dimension_names: {dimension_names}")
    debug_info.append(f"  - dimension_cuts: {dimension_cuts}")
    debug_info.append(f"  - selected_columns: {selected_columns}")
    debug_info.append(f"  - share_email: {share_email}")
    debug_info.append(f"  - use_oauth: {use_oauth}")
    
    try:
        logger.info("Starting Curie export from MCP server...")
        
        # Capture stdout/stderr during the export
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            url, success, detected_control = export_curie_with_explicit_params(
                experiment_name=experiment_name,
                primary_metrics=primary_metrics,
                secondary_metrics=secondary_metrics,
                guardrail_metrics=guardrail_metrics,
                dimension_names=dimension_names,
                dimension_cuts=dimension_cuts,
                selected_columns=selected_columns,
                share_email=share_email,
                use_oauth=use_oauth
            )
        
        # Get captured output
        captured_stdout = stdout_capture.getvalue()
        captured_stderr = stderr_capture.getvalue()
        captured_logs = log_capture.getvalue()
        
        debug_info.append(f"🔧 Export result:")
        debug_info.append(f"  - url: {url}")
        debug_info.append(f"  - success: {success}")
        debug_info.append(f"  - detected_control: {detected_control}")
        
        if captured_stdout:
            debug_info.append(f"🔧 CAPTURED STDOUT:\n{captured_stdout}")
        if captured_stderr:
            debug_info.append(f"🔧 CAPTURED STDERR:\n{captured_stderr}")
        if captured_logs:
            debug_info.append(f"🔧 CAPTURED LOGS:\n{captured_logs}")
            
        # Restore original log handlers
        root_logger.removeHandler(log_handler)
        root_logger.setLevel(original_root_level)
        for logger_name in loggers_to_capture:
            log = logging.getLogger(logger_name)
            log.removeHandler(log_handler)
            # Note: we don't restore original handlers to avoid interference
        
        if success:
            response = f"✅ Curie export completed successfully!\n\n"
            response += f"📊 Google Sheets URL: {url}\n"
            if detected_control:
                response += f"🎯 Control variant: {detected_control}\n"
            response += f"\nThe sheet has been created and formatted with experiment results."
        else:
            debug_log = "\n".join(debug_info)
            response = f"❌ Curie export failed.\n\n"
            response += f"🔍 **DETAILED ERROR INFORMATION:**\n"
            response += f"- URL returned: {url}\n"
            response += f"- Success flag: {success}\n"
            response += f"- Detected control: {detected_control}\n\n"
            response += f"=== FULL DEBUG LOG ===\n{debug_log}\n"
            
        return response
        
    except Exception as e:
        # Get captured output
        captured_stdout = stdout_capture.getvalue()
        captured_stderr = stderr_capture.getvalue()
        captured_logs = log_capture.getvalue()
        
        # Get full traceback
        tb_str = traceback.format_exc()
        
        debug_info.append(f"🔧 EXCEPTION CAUGHT:")
        debug_info.append(f"  - Exception type: {type(e).__name__}")
        debug_info.append(f"  - Exception message: {str(e)}")
        debug_info.append(f"  - Traceback:\n{tb_str}")
        
        if captured_stdout:
            debug_info.append(f"🔧 CAPTURED STDOUT:\n{captured_stdout}")
        if captured_stderr:
            debug_info.append(f"🔧 CAPTURED STDERR:\n{captured_stderr}")
        if captured_logs:
            debug_info.append(f"🔧 CAPTURED LOGS:\n{captured_logs}")
            
        # Restore original log handlers
        try:
            root_logger.removeHandler(log_handler)
            root_logger.setLevel(original_root_level)
            for logger_name in loggers_to_capture:
                log = logging.getLogger(logger_name)
                log.removeHandler(log_handler)
        except:
            pass  # Don't let cleanup errors mask the real error
        
        debug_log = "\n".join(debug_info)
        
        logger.error(f"Curie export error: {str(e)}")
        
        response = f"❌ Error exporting Curie results: {str(e)}\n\n"
        response += f"🔍 **FULL ERROR DETAILS:**\n"
        response += f"Exception: {type(e).__name__}: {str(e)}\n\n"
        response += f"=== COMPLETE DEBUG LOG ===\n{debug_log}"
        
        return response


@mcp.tool
def curie_get_metadata(experiment_name: str) -> str:
    """
    Get metadata for a Curie experiment.
    
    Args:
        experiment_name: Name of the experiment
    
    Returns:
        Formatted experiment metadata
    """
    try:
        metadata = get_experiment_metadata(experiment_name)
        
        if 'error' in metadata:
            return f"Error getting metadata: {metadata['error']}"
        
        # Format metadata for display
        response = f"📊 EXPERIMENT METADATA: {experiment_name}\n"
        response += "=" * 60 + "\n"
        response += f"Total rows: {metadata['total_rows']:,}\n"
        response += f"Unique metrics: {metadata['unique_metrics']}\n"
        response += f"Unique dimensions: {metadata['unique_dimensions']}\n\n"
        
        # Variant information
        if metadata['is_multi_treatment']:
            response += f"🔀 MULTI-TREATMENT EXPERIMENT\n"
            response += f"Variants ({len(metadata['variants'])}): {', '.join(metadata['variants'])}\n"
            response += f"Control: {metadata['control_variant'] or 'NOT DETECTED'}\n"
            response += f"Treatments ({metadata['treatment_count']}): {', '.join(metadata['treatment_variants'])}\n"
        else:
            response += f"🔀 SINGLE TREATMENT EXPERIMENT\n"
            response += f"Variants: {', '.join(metadata['variants'])}\n"
        
        # Metrics analyzed at
        if metadata.get('analyzed_at_info'):
            response += f"\n📅 METRICS ANALYZED AT:\n{metadata['analyzed_at_info']}\n"
        
        # Available metrics (truncated list)
        if 'metrics' in metadata:
            metrics_list = list(metadata['metrics'])[:10]
            response += f"\n📋 AVAILABLE METRICS (showing first 10 of {len(metadata['metrics'])}):\n"
            for metric in metrics_list:
                response += f"• {metric}\n"
            if len(metadata['metrics']) > 10:
                response += f"... and {len(metadata['metrics']) - 10} more\n"
        
        # Available dimensions  
        if 'dimensions' in metadata:
            response += f"\n📍 AVAILABLE DIMENSIONS:\n"
            for dim in metadata['dimensions']:
                response += f"• {dim}\n"
                
        return response
        
    except Exception as e:
        logger.error(f"Get metadata error: {str(e)}")
        return f"Error getting metadata: {str(e)}"


# ============================================================================
# CONTEXT MANAGEMENT
# ============================================================================

def write_documents_to_session_context(results: List[Dict], query: str, context_type: str) -> str:
    """
    Write retrieved documents to a local session_context folder.
    
    Args:
        results: List of search result dictionaries
        query: The search query that was used
        context_type: Type of context (table, user, experiment_readouts, deep_dives)
    
    Returns:
        Summary message about files written
    """
    if not results:
        return "No documents to write."
    
    # Create timestamp-based session folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = PROJECT_ROOT / "session_context" / f"{timestamp}_{context_type}"
    session_dir.mkdir(parents=True, exist_ok=True)
    
    # Write query info
    query_file = session_dir / "query_info.txt"
    query_info = f"Query: {query}\nContext Type: {context_type}\nTimestamp: {timestamp}\nResults: {len(results)} documents\n\n"
    query_file.write_text(query_info, encoding='utf-8')
    
    written_files = []
    for i, result in enumerate(results, 1):
        # Determine file extension based on content or file path
        file_path = result.get('relative_path', '')
        if file_path.endswith('.sql'):
            ext = '.sql'
        elif file_path.endswith('.md'):
            ext = '.md'
        else:
            # Default to .md for most context documents
            ext = '.md'
        
        # Create filename
        doc_title = result.get('document_title', result.get('file_name', f'document_{i}'))
        # Sanitize filename
        safe_title = "".join(c for c in doc_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_title = safe_title.replace(' ', '_')
        filename = f"{i:02d}_{safe_title}{ext}"
        
        # Get content - prefer context_content over regular content
        content = result.get('context_content', result.get('content', ''))
        
        # Create document header with metadata
        header = f"# {doc_title}\n\n"
        header += f"**Source:** `{result.get('relative_path', 'N/A')}`\n"
        header += f"**Category:** {result.get('category', 'N/A')}\n"
        if result.get('subcategory'):
            header += f"**Team:** {result.get('subcategory')}\n"
        header += f"**Relevance Score:** {result.get('combined_score', 0):.3f}\n"
        header += f"**GitHub URL:** {result.get('github_file_url', 'N/A')}\n\n"
        header += "---\n\n"
        
        # Write file
        doc_file = session_dir / filename
        doc_file.write_text(header + content, encoding='utf-8')
        written_files.append(filename)
    
    # Create index file
    index_file = session_dir / "index.md"
    index_content = f"# Session Context Index\n\n"
    index_content += f"**Query:** {query}\n"
    index_content += f"**Context Type:** {context_type}\n"
    index_content += f"**Timestamp:** {timestamp}\n"
    index_content += f"**Total Documents:** {len(results)}\n\n"
    index_content += "## Documents\n\n"
    for filename in written_files:
        index_content += f"- [{filename}](./{filename})\n"
    index_file.write_text(index_content, encoding='utf-8')
    
    return f"📁 Wrote {len(results)} documents to: {session_dir}\n📄 Files: {', '.join(written_files)}\n📋 Index: index.md"

@mcp.tool
def fetch_table_context(query: str, top_k: int = 5, team: Optional[str] = None, write_to_local: bool = False) -> str:
    """
    Search for Snowflake table context using hybrid search (BM25 + embeddings).
    Use natural language queries like 'user dimensions table', 'delivery facts', etc.
    
    Args:
        query: Natural language search query for table context
        top_k: Number of top results to return (default: 5)
        team: Optional team/subcategory filter (e.g., 'growth/nux', 'edw/consumer')
        write_to_local: If True, write retrieved documents to session_context folder (default: False)
    
    Returns:
        Table context search results with relevance scores
    """
    try:
        if not HYBRID_SEARCH_AVAILABLE:
            return "Hybrid search not available. Please run document indexing first."
        
        # Get configured searcher with validation
        searcher = get_configured_hybrid_searcher()
        if not searcher:
            return "Error: Unable to initialize search system. Please check Snowflake connectivity and ensure the document index table exists."
        
        # Perform search
        results = searcher.search_table_context(query, top_k=top_k, team=team)
        
        if not results:
            return f"No table context found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        # Format the main search results
        formatted_results = searcher.format_search_results(results, query)
        
        # Write to local files if requested
        if write_to_local:
            write_summary = write_documents_to_session_context(results, query, "table_context")
            return f"{formatted_results}\n\n📁 **LOCAL FILES WRITTEN:**\n{write_summary}"
        
        return formatted_results
            
    except Exception as e:
        logger.error(f"Fetch table context error: {str(e)}")
        return f"Error fetching table context: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_pod_queries(query: str, top_k: int = 3, team: Optional[str] = None) -> str:
    """
    Search for validated master queries using hybrid search (BM25 + embeddings).
    Use natural language queries like 'pricing analysis', 'affordability metrics', etc.
    
    Args:
        query: Natural language search query for SQL queries (use 'list' to see all available queries)
        top_k: Number of top results to return (default: 3)
        team: Optional team/subcategory filter (e.g., 'growth/nux', 'growth/pricing-and-affordability')
    
    Returns:
        Query search results with relevance scores
    """
    try:
        if query.lower() == "list":
            # Fallback to file system listing for 'list' command
            pod_queries_path = PROJECT_ROOT / "context" / "pod-level-validated-master-queries"
            if pod_queries_path.exists():
                sql_files = list(pod_queries_path.glob("*.sql"))
                if sql_files:
                    file_list = "\n".join([f"• {f.stem}" for f in sql_files])
                    return f"Available pod-level validated queries:\n\n{file_list}"
                else:
                    return "No SQL files found in pod-level-validated-master-queries directory"
            else:
                return "Pod-level-validated-master-queries directory not found"
        
        if not HYBRID_SEARCH_AVAILABLE:
            return "Hybrid search not available. Please run document indexing first."
        
        # Get configured searcher with validation
        searcher = get_configured_hybrid_searcher()
        if not searcher:
            return "Error: Unable to initialize search system. Please check Snowflake connectivity and ensure the document index table exists."
        
        # Perform search
        results = searcher.search_pod_queries(query, top_k=top_k, team=team)
        
        if not results:
            return f"No pod-level queries found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        return searcher.format_search_results(results, query)
                
    except Exception as e:
        logger.error(f"Fetch pod queries error: {str(e)}")
        return f"Error fetching pod queries: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_user_context(query: str, top_k: int = 5, team: Optional[str] = None, write_to_local: bool = False) -> str:
    """
    Search for user-specific context using hybrid search (BM25 + embeddings).
    Use natural language queries to find relevant user context documents.
    
    Args:
        query: Natural language search query for user context (use 'list' to see all available files)
        top_k: Number of top results to return (default: 5)
        team: Optional team/subcategory filter (e.g., 'fiona.fan', 'team.lead')
        write_to_local: If True, write retrieved documents to session_context folder (default: False)
    
    Returns:
        User context search results with relevance scores
    """
    try:
        if query.lower() == "list":
            # Fallback to file system listing for 'list' command
            user_context_path = PROJECT_ROOT / "context" / "user-context"
            if user_context_path.exists():
                items = []
                for item in user_context_path.rglob("*"):
                    if item.is_file():
                        rel_path = item.relative_to(user_context_path)
                        items.append(f"📄 {rel_path}")
                    elif item.is_dir() and item != user_context_path:
                        rel_path = item.relative_to(user_context_path)
                        items.append(f"📁 {rel_path}/")
                
                if items:
                    items_list = "\n".join(sorted(items))
                    return f"Available user context:\n\n{items_list}"
                else:
                    return "No user context files found"
            else:
                return "User context directory not found"
        
        if not HYBRID_SEARCH_AVAILABLE:
            return "Hybrid search not available. Please run document indexing first."
        
        # Get configured searcher with validation
        searcher = get_configured_hybrid_searcher()
        if not searcher:
            return "Error: Unable to initialize search system. Please check Snowflake connectivity and ensure the document index table exists."
        
        # Perform search
        results = searcher.search_user_context(query, top_k=top_k, team=team)
        
        if not results:
            return f"No user context found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        # Format the main search results
        formatted_results = searcher.format_search_results(results, query)
        
        # Write to local files if requested
        if write_to_local:
            write_summary = write_documents_to_session_context(results, query, "user_context")
            return f"{formatted_results}\n\n📁 **LOCAL FILES WRITTEN:**\n{write_summary}"
        
        return formatted_results
                
    except Exception as e:
        logger.error(f"Fetch user context error: {str(e)}")
        return f"Error fetching user context: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_experiment_readouts(query: str, top_k: int = 5, team: Optional[str] = None, write_to_local: bool = False) -> str:
    """
    Search for experiment readout documents using hybrid search (BM25 + embeddings).
    Use natural language queries like 'conversion experiments', 'iOS testing', etc.
    
    Args:
        query: Natural language search query for experiment readouts
        top_k: Number of top results to return (default: 5)
        team: Optional team/subcategory filter (e.g., 'growth/nux')
        write_to_local: If True, write retrieved documents to session_context folder (default: False)
    
    Returns:
        Experiment readout search results with relevance scores
    """
    try:
        if not HYBRID_SEARCH_AVAILABLE:
            return "Hybrid search not available. Please run document indexing first."
        
        # Get configured searcher with validation
        searcher = get_configured_hybrid_searcher()
        if not searcher:
            return "Error: Unable to initialize search system. Please check Snowflake connectivity and ensure the document index table exists."
        
        # Perform search
        results = searcher.search_experiment_readouts(query, top_k=top_k, team=team)
        
        if not results:
            return f"No experiment readouts found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        # Format the main search results
        formatted_results = searcher.format_search_results(results, query)
        
        # Write to local files if requested
        if write_to_local:
            write_summary = write_documents_to_session_context(results, query, "experiment_readouts")
            return f"{formatted_results}\n\n📁 **LOCAL FILES WRITTEN:**\n{write_summary}"
        
        return formatted_results
                
    except Exception as e:
        logger.error(f"Fetch experiment readouts error: {str(e)}")
        return f"Error fetching experiment readouts: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_deep_dives(query: str, top_k: int = 5, team: Optional[str] = None, write_to_local: bool = False) -> str:
    """
    Search for deep dive analysis documents using hybrid search (BM25 + embeddings).
    Use natural language queries like 'MAU analysis', 'experiment insights', etc.
    
    Args:
        query: Natural language search query for deep dive analyses
        top_k: Number of top results to return (default: 5)
        team: Optional team/subcategory filter (e.g., 'growth/nux')
        write_to_local: If True, write retrieved documents to session_context folder (default: False)
    
    Returns:
        Deep dive analysis search results with relevance scores
    """
    try:
        if not HYBRID_SEARCH_AVAILABLE:
            return "Hybrid search not available. Please run document indexing first."
        
        # Get configured searcher with validation
        searcher = get_configured_hybrid_searcher()
        if not searcher:
            return "Error: Unable to initialize search system. Please check Snowflake connectivity and ensure the document index table exists."
        
        # Perform search
        results = searcher.search_deep_dives(query, top_k=top_k, team=team)
        
        if not results:
            return f"No deep dive analyses found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        # Format the main search results
        formatted_results = searcher.format_search_results(results, query)
        
        # Write to local files if requested
        if write_to_local:
            write_summary = write_documents_to_session_context(results, query, "deep_dives")
            return f"{formatted_results}\n\n📁 **LOCAL FILES WRITTEN:**\n{write_summary}"
        
        return formatted_results
                
    except Exception as e:
        logger.error(f"Fetch deep dives error: {str(e)}")
        return f"Error fetching deep dives: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_cursor_rules(rule_name: str) -> str:
    """
    Fetch Cursor rules from .cursor/rules/ directory.
    
    Args:
        rule_name: Name of the rule file (without .mdc extension), or 'list' to see available rules
    
    Returns:
        Rule content or list of available rules
    """
    try:
        rules_path = PROJECT_ROOT / ".cursor" / "rules"
        
        if rule_name == "list":
            # List available rules
            if rules_path.exists():
                mdc_files = list(rules_path.glob("*.mdc"))
                if mdc_files:
                    file_list = "\n".join([f"• {f.stem}" for f in mdc_files])
                    return f"Available Cursor rules:\n\n{file_list}"
                else:
                    return "No rule files found in .cursor/rules directory"
            else:
                return "Cursor rules directory not found"
        else:
            # Fetch specific rule
            rule_file = rules_path / f"{rule_name}.mdc"
            if rule_file.exists():
                content = rule_file.read_text()
                return f"Cursor rule '{rule_name}':\n\n{content}"
            else:
                return f"Rule file '{rule_name}.mdc' not found in .cursor/rules"
                
    except Exception as e:
        logger.error(f"Fetch cursor rules error: {str(e)}")
        return f"Error fetching cursor rules: {str(e)}"


@mcp.tool
def describe_table(
    table_name: str,
    output_format: str = "markdown",
    sample_row_limit: int = 10,
    verbose: bool = False
) -> str:
    """
    Generate comprehensive context documentation for a Snowflake table.
    
    This tool creates detailed documentation including business context, 
    metadata analysis, granularity detection, and sample queries.
    Returns content only - does not write to filesystem.
    
    Args:
        table_name: Table name (can be partial or fully qualified)
        output_format: Output format - "markdown" or "json" 
        sample_row_limit: Number of sample rows for granularity analysis (1-20)
        verbose: Enable verbose logging for debugging
        
    Returns:
        Generated table context as markdown text or JSON string
    """
    if not TABLE_CONTEXT_AVAILABLE:
        return json.dumps({
            "error": "Table context agent not available. Please ensure local_tools.table_context_agent is properly installed."
        })
    
    try:
        logger.info(f"Generating table context for: {table_name}")
        
        # Validate sample_row_limit
        if not 1 <= sample_row_limit <= 20:
            sample_row_limit = 10
            logger.warning(f"Invalid sample_row_limit, using default: {sample_row_limit}")
        
        # Generate the table context using the agent (content only)
        result = generate_table_context(
            table=table_name,
            print_only=True,
            sample_row_limit=sample_row_limit,
            verbose=verbose
        )
        
        if output_format.lower() == "json":
            # Convert markdown result to JSON structure
            response = {
                "table_name": table_name,
                "format": "markdown",
                "content": result,
                "generated_at": "auto",
                "status": "success"
            }
            return json.dumps(response, indent=2)
        else:
            # Return raw markdown
            return result
            
    except Exception as e:
        logger.error(f"Error generating table context for {table_name}: {e}")
        error_response = {
            "error": f"Failed to generate table context: {str(e)}",
            "table_name": table_name,
            "status": "failed"
        }
        return json.dumps(error_response, indent=2)






@mcp.tool
def upload_md_to_google_doc(
    md_file_path: str,
    google_doc_id: Optional[str] = None,
    doc_title: Optional[str] = None
) -> str:
    """
    Upload a local markdown file to Google Docs.
    
    Converts markdown formatting to Google Docs native formatting including:
    - Headings (# ## ###, etc.)
    - Bullet points and numbered lists
    - Basic text formatting (bold, italic removed for simplicity)
    - Tables and other markdown elements
    
    Args:
        md_file_path: Path to the local markdown file
        google_doc_id: Optional Google Doc ID. If not provided, creates new doc
        doc_title: Optional title for the document. If not provided, uses filename
        
    Returns:
        Google Doc URL
    """
    try:
        logger.info(f"Uploading markdown file to Google Doc: {md_file_path}")
        
        # Import here to avoid naming conflicts
        from local_tools.md_to_google_doc import upload_md_to_google_doc as upload_func
        
        # Call the upload function from the local_tools module
        doc_url = upload_func(md_file_path, google_doc_id, doc_title)
        
        response = f"✅ Markdown file uploaded to Google Doc successfully!\n\n"
        response += f"📄 **Source file:** {md_file_path}\n"
        if doc_title:
            response += f"📝 **Document title:** {doc_title}\n"
        if google_doc_id:
            response += f"🔄 **Updated existing document:** {google_doc_id}\n"
        else:
            response += f"📄 **Created new document**\n"
        response += f"🔗 **Google Doc URL:** {doc_url}\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error uploading markdown to Google Doc: {str(e)}")
        return f"❌ Error uploading markdown file to Google Doc: {str(e)}"


# ============================================================================
# SERVER ENTRY POINT
# ============================================================================

def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()