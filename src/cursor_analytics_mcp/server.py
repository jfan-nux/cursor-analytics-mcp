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
- Google Docs to Markdown conversion (gd2md)
- Markdown to Google Docs export (md2gd)
"""

# CRITICAL: Configure environment before any imports to prevent stdout pollution
import os
import sys
import warnings

# Suppress all warnings to prevent them from going to stdout
warnings.filterwarnings('ignore')

# Configure warnings to go to stderr
warnings.simplefilter('default')
import logging
logging.captureWarnings(True)

# Set environment variables to suppress verbose library output
os.environ['PYTHONWARNINGS'] = 'ignore'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'  # Suppress PyArrow warnings

import json
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
    from local_tools.gdocs_sync.crawlers import (
        process_google_docs_batch,
        GoogleDocCrawler,
        convert_google_doc_to_markdown_string
    )
    from local_tools.gdocs_sync.cli import MarkdownGDocsSync
    from local_tools.gdocs_sync.core import MappingManager
    from utils.logger import get_logger
    # Setup logging
    logger = get_logger(__name__)
except ImportError as e:
    # Fallback to basic logging (use stderr to not break MCP JSON protocol)
    import logging
    import sys
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stderr,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    logger.warning(f"Could not import utils modules: {e}")
    logger.warning("Make sure the utils directory is properly copied to the project root")

# Try to import dual-table hybrid search functionality
try:
    from local_tools.document_indexer.dual_table_search import DualTableHybridSearcher
    HYBRID_SEARCH_AVAILABLE = True
except ImportError:
    logger.warning("Dual-table hybrid search not available. Document indexing may not be set up.")
    HYBRID_SEARCH_AVAILABLE = False

# Try to import table context agent functionality
try:
    from local_tools.table_context_agent.agent import main as generate_table_context
    TABLE_CONTEXT_AVAILABLE = True
except ImportError:
    logger.warning("Table context agent not available.")
    TABLE_CONTEXT_AVAILABLE = False

# Try to import Databricks job submission functionality
try:
    from local_tools.databricks_job_submit import (
        run_job as databricks_run_job,
        get_job_manager,
        get_run_url as databricks_get_run_url,
        sql_file_to_notebook,
    )
    from local_tools.databricks_job_submit.databricks_job_manager import DatabricksJobManager
    DATABRICKS_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Databricks job submission not available: {e}")
    DATABRICKS_AVAILABLE = False

# Initialize FastMCP server
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

# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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


# ============================================================================
# MARKDOWN TO GOOGLE DOCS EXPORT (MD2GD)
# ============================================================================

@mcp.tool
def export_markdown_to_google_doc(
    markdown_path: str,
    open_browser: bool = False
) -> str:
    """
    Export a markdown file to Google Docs.

    Creates a new Google Doc or updates an existing one if the markdown file
    is already linked. Preserves formatting, images, and document structure.

    Args:
        markdown_path: Path to the markdown file to export
        open_browser: Whether to open the document in browser after export

    Returns:
        Export results with Google Doc URL and document ID
    """
    try:
        import os
        import webbrowser
        from local_tools.gdocs_sync.core import GoogleDocsClient, ImageHandler
        from local_tools.gdocs_sync.core.markdown_converter import MarkdownConverter
        from googleapiclient.discovery import build

        # Convert to absolute path
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Exporting markdown to Google Docs: {abs_path}")

        # Check if file exists
        if not os.path.exists(abs_path):
            return f"❌ Error: File not found: {abs_path}\n\nPlease provide the full absolute path to the markdown file."

        # Read markdown content
        with open(abs_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Initialize sync tool and mapping manager
        sync = MarkdownGDocsSync()
        mapping_manager = MappingManager()

        # Get services using unified authenticator
        from local_tools.gdocs_sync.auth import UnifiedAuthenticator
        authenticator = UnifiedAuthenticator()
        credentials = authenticator.get_credentials()
        docs_service = authenticator.get_docs_service()
        drive_service = authenticator.get_drive_service()

        # Initialize components
        config = sync.config
        template_id = getattr(config, 'template_doc_id', None)
        gdocs_client = GoogleDocsClient(docs_service, drive_service, template_id)

        # Check if document already exists
        existing_mapping = mapping_manager.get_mapping(abs_path)

        # Process images
        markdown_dir = os.path.dirname(abs_path)
        image_handler = ImageHandler(
            drive_service,
            markdown_dir,
            getattr(config, 'image_download_dir', 'images')
        )
        _, images = image_handler.process_markdown_images(markdown_content)
        image_paths = {}
        for img_path, img_info in images.items():
            upload_result = image_handler.upload_image(img_path)
            if upload_result:
                image_paths[img_path] = upload_result

        # Convert markdown to Google Docs format
        converter = MarkdownConverter()
        tab_id = existing_mapping.get('tab_id') if existing_mapping else None
        requests = converter.markdown_to_gdocs(markdown_content, image_paths, tab_id)

        if existing_mapping:
            # Update existing document
            doc_id = existing_mapping['doc_id']
            doc_url = existing_mapping['doc_url']
            logger.info(f"Updating existing document (ID: {doc_id})...")

            success = gdocs_client.update_doc(doc_id, requests, tab_id)

            if success:
                # Update mapping
                mapping_manager.add_mapping(
                    abs_path,
                    doc_id,
                    doc_url,
                    'export',
                    tab_id
                )

                # Process with Apps Script if configured
                apps_script_id = (getattr(config, 'apps_script_id', '') or '').strip()
                if apps_script_id:
                    try:
                        script_service = authenticator.get_script_service()
                        from local_tools.gdocs_sync.core import AppsScriptClient
                        script_client = AppsScriptClient(script_service, apps_script_id)
                        result = script_client.process_document(doc_id, template_id, tab_id)
                        logger.info(f"Apps Script processing: {result}")
                    except Exception as e:
                        logger.warning(f"Apps Script processing failed: {e}")

                if open_browser:
                    webbrowser.open(doc_url)

                response = f"✅ Markdown exported to Google Docs successfully!\n\n"
                response += f"📄 **Title:** Updated existing document\n"
                response += f"📝 **Document ID:** {doc_id}\n"
                response += f"🔗 **URL:** {doc_url}\n"
                response += f"🔄 **Action:** Updated existing document\n"
                return response
            else:
                return "❌ Failed to update document"
        else:
            # Create new document
            title = sync._format_title(os.path.basename(abs_path))
            result = gdocs_client.create_doc(title, requests)

            doc_id = result['doc_id']
            doc_url = result['doc_url']

            # Save mapping
            mapping_manager.add_mapping(
                abs_path,
                doc_id,
                doc_url,
                'export'
            )

            # Process with Apps Script if configured
            apps_script_id = (getattr(config, 'apps_script_id', '') or '').strip()
            if apps_script_id:
                try:
                    script_service = authenticator.get_script_service()
                    from local_tools.gdocs_sync.core import AppsScriptClient
                    script_client = AppsScriptClient(script_service, apps_script_id)
                    result_script = script_client.process_document(doc_id, template_id, None)
                    logger.info(f"Apps Script processing: {result_script}")
                except Exception as e:
                    logger.warning(f"Apps Script processing failed: {e}")

            if open_browser:
                webbrowser.open(doc_url)

            response = f"✅ Markdown exported to Google Docs successfully!\n\n"
            response += f"📄 **Title:** {title}\n"
            response += f"📝 **Document ID:** {doc_id}\n"
            response += f"🔗 **URL:** {doc_url}\n"
            response += f"🔄 **Action:** Created new document\n"
            response += f"💾 **Mapping:** Automatically created for future exports\n"
            return response

    except Exception as e:
        logger.error(f"Markdown to Google Docs export error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return f"❌ Error exporting markdown to Google Docs: {str(e)}"


@mcp.tool
def import_google_doc_to_markdown(
    doc_url: str,
    markdown_path: str
) -> str:
    """
    Import a Google Doc to markdown format.

    Converts a Google Doc to markdown and saves it to the specified path.
    Preserves formatting including bold, italic, tables, lists, images, and footnotes.

    Args:
        doc_url: Google Doc URL or ID
        markdown_path: Path to save the markdown file

    Returns:
        Import results with conversion details
    """
    try:
        # Convert to absolute path to handle different working directories
        import os
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Importing Google Doc to markdown: {doc_url} -> {abs_path}")

        # Use the gd2md converter to get markdown content
        result = convert_google_doc_to_markdown_string(doc_url, write_file=False, output_path="")

        if result['status'] != 'success':
            return f"❌ Conversion failed: {result.get('error', 'Unknown error')}"

        # Write markdown content to specified path
        output_dir = os.path.dirname(abs_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(result['markdown_content'])

        # Create mapping automatically so user can export/sync later
        mapping_manager = MappingManager()
        mapping_manager.add_mapping(
            markdown_path=abs_path,
            doc_id=result['doc_id'],
            doc_url=result['doc_url'],
            direction='import'
        )

        response = f"✅ Google Doc imported to markdown successfully!\n\n"
        response += f"📄 **Document:** {result['title']}\n"
        response += f"📁 **Saved to:** {abs_path}\n"
        response += f"👥 **Team:** {result['team_path']}\n"
        response += f"🖼️ **Images:** {result['images_downloaded']} processed\n"
        response += f"📝 **Footnotes:** {result['footnotes_processed']} processed\n"
        response += f"🔗 **Source:** {result['doc_url']}\n"
        response += f"🔗 **Mapping created:** You can now use 'status' or 'export' commands\n"

        return response

    except Exception as e:
        logger.error(f"Google Doc to markdown import error: {str(e)}")
        return f"❌ Error importing Google Doc to markdown: {str(e)}"


@mcp.tool
def link_markdown_to_google_doc(
    markdown_path: str,
    doc_url: str
) -> str:
    """
    Link a markdown file to an existing Google Doc (or specific tab).

    This establishes a connection between a local markdown file and a Google Doc,
    allowing future exports to update the same document. The link can also target
    a specific tab within a multi-tab document.

    Args:
        markdown_path: Path to the markdown file
        doc_url: Google Doc URL or ID (can include #tab=t.TAB_ID parameter for specific tab)

    Returns:
        Link confirmation message
    """
    try:
        import os
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Linking markdown to Google Doc: {abs_path} -> {doc_url}")

        # Initialize sync tool
        sync = MarkdownGDocsSync()

        # Capture output
        import io
        from contextlib import redirect_stdout

        stdout_capture = io.StringIO()

        with redirect_stdout(stdout_capture):
            sync.link(abs_path, doc_url)

        output = stdout_capture.getvalue()

        if "✓ Linked" in output or "✅" in output:
            return f"✅ Markdown file linked to Google Doc successfully!\n\n{output}"
        else:
            return f"⚠️ Link operation completed with messages:\n\n{output}"

    except Exception as e:
        logger.error(f"Link error: {str(e)}")
        return f"❌ Error linking markdown to Google Doc: {str(e)}"


# @mcp.tool  # Hidden from MCP - use as local tool only
def unlink_markdown_from_google_doc(
    markdown_path: str
) -> str:
    """
    Remove the link between a markdown file and its Google Doc.

    This only removes the mapping - it does not delete the Google Doc or markdown file.

    Args:
        markdown_path: Path to the markdown file to unlink

    Returns:
        Unlink confirmation message
    """
    try:
        import os
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Unlinking markdown from Google Doc: {abs_path}")

        # Initialize sync tool
        sync = MarkdownGDocsSync()

        # Capture output
        import io
        from contextlib import redirect_stdout

        stdout_capture = io.StringIO()

        with redirect_stdout(stdout_capture):
            sync.unlink(abs_path)

        output = stdout_capture.getvalue()

        if "✓ Unlinked" in output or "✅" in output:
            return f"✅ Markdown file unlinked successfully!\n\n{output}"
        else:
            return f"⚠️ Unlink operation completed with messages:\n\n{output}"

    except Exception as e:
        logger.error(f"Unlink error: {str(e)}")
        return f"❌ Error unlinking markdown from Google Doc: {str(e)}"


# @mcp.tool  # Hidden from MCP - use as local tool only
def list_markdown_google_doc_mappings() -> str:
    """
    List all markdown files linked to Google Docs.

    Shows the current mappings between local markdown files and their corresponding
    Google Docs, including last sync time and direction.

    Returns:
        List of all mappings
    """
    try:
        logger.info("Listing markdown to Google Doc mappings")

        # Initialize sync tool
        sync = MarkdownGDocsSync()

        # Capture output
        import io
        from contextlib import redirect_stdout

        stdout_capture = io.StringIO()

        with redirect_stdout(stdout_capture):
            sync.list_mappings()

        output = stdout_capture.getvalue()

        return output if output else "No mappings found"

    except Exception as e:
        logger.error(f"List mappings error: {str(e)}")
        return f"❌ Error listing mappings: {str(e)}"


# @mcp.tool  # Hidden from MCP - use as local tool only
def show_markdown_google_doc_status(
    markdown_path: str
) -> str:
    """
    Show sync status for a markdown file.

    Displays information about the linked Google Doc, including the Doc ID,
    URL, last sync time, and last sync direction.

    Args:
        markdown_path: Path to the markdown file

    Returns:
        Sync status information
    """
    try:
        import os
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Showing sync status for: {abs_path}")

        # Initialize sync tool
        sync = MarkdownGDocsSync()

        # Capture output
        import io
        from contextlib import redirect_stdout

        stdout_capture = io.StringIO()

        with redirect_stdout(stdout_capture):
            sync.status(abs_path)

        output = stdout_capture.getvalue()

        return output if output else "No mapping found for this file"

    except Exception as e:
        logger.error(f"Status error: {str(e)}")
        return f"❌ Error showing status: {str(e)}"


@mcp.tool
def import_from_linked_google_doc(
    markdown_path: str,
    backup: bool = True
) -> str:
    """
    Import changes from a linked Google Doc back to the markdown file.

    This is useful for pulling changes made in Google Docs (by collaborators or reviewers)
    back into your local markdown file. This is different from the one-way conversion
    import_google_doc_to_markdown - this function requires an existing link and preserves
    the mapping.

    Args:
        markdown_path: Path to the markdown file
        backup: Whether to backup the existing markdown file before importing

    Returns:
        Import results
    """
    try:
        import os
        abs_path = os.path.abspath(os.path.expanduser(markdown_path))

        logger.info(f"Importing from linked Google Doc to: {abs_path}")

        # Initialize sync tool
        sync = MarkdownGDocsSync()

        # Capture output
        import io
        from contextlib import redirect_stdout

        stdout_capture = io.StringIO()

        with redirect_stdout(stdout_capture):
            sync.import_doc(abs_path, backup=backup)

        output = stdout_capture.getvalue()

        if "✓ Successfully imported" in output or "✅" in output:
            return f"✅ Changes imported from Google Doc successfully!\n\n{output}"
        else:
            return f"⚠️ Import completed with messages:\n\n{output}"

    except Exception as e:
        logger.error(f"Import from linked doc error: {str(e)}")
        return f"❌ Error importing from linked Google Doc: {str(e)}"


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

# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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


# @mcp.tool  # Hidden from MCP - use as local tool only
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






# ============================================================================
# DATABRICKS JOB OPERATIONS
# ============================================================================

@mcp.tool
def run_databricks_job(
    job_name: str,
    local_script_path: str,
    job_parameters: Optional[Dict[str, str]] = None,
    existing_cluster_id: Optional[str] = None,
    timeout_seconds: int = 3600,
    wait_for_completion: bool = True,
    save_logs: bool = True,
    cleanup_script: bool = True
) -> str:
    """
    Run a Python script on Databricks using an existing cluster.

    This tool handles the complete workflow:
    1. Uploads the script to DBFS
    2. Submits the job to an existing cluster
    3. Optionally waits for completion and retrieves results
    4. Saves logs locally and cleans up uploaded script

    Args:
        job_name: Name of the job (used for identification and log files)
        local_script_path: Path to the local Python script to run
        job_parameters: Parameters to pass to the script as command-line args (e.g., {"data_path": "s3://bucket/data"})
        existing_cluster_id: ID of existing Databricks cluster to use (falls back to DATABRICKS_CLUSTER_ID env var)
        timeout_seconds: Job timeout in seconds (default: 1 hour)
        wait_for_completion: Whether to wait for job to complete (default: True)
        save_logs: Whether to save logs locally after completion (default: True)
        cleanup_script: Whether to delete uploaded script from DBFS after completion (default: True)

    Returns:
        Job results including status, run ID, job URL, and logs path
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        import os
        logger.info(f"Starting Databricks job: {job_name}")

        # Convert to absolute path
        abs_script_path = os.path.abspath(os.path.expanduser(local_script_path))

        if not os.path.exists(abs_script_path):
            return f"Error: Script file not found: {abs_script_path}"

        # Run the job
        result = databricks_run_job(
            job_name=job_name,
            local_script_path=abs_script_path,
            existing_cluster_id=existing_cluster_id,
            job_parameters=job_parameters,
            timeout_seconds=timeout_seconds,
            wait_for_completion=wait_for_completion,
            save_logs=save_logs,
            cleanup_script=cleanup_script
        )

        # Format response
        status = result.get('status', 'UNKNOWN')
        run_id = result.get('databricks_run_id')
        job_url = result.get('job_url', '')
        log_file = result.get('log_file')
        error = result.get('error')

        if status == "SUCCESS":
            response = f"Job '{job_name}' completed successfully!\n\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"

            # Include job results if available
            job_results = result.get('job_results')
            if job_results:
                response += f"\n**Job Results:**\n```json\n{json.dumps(job_results, indent=2)}\n```"

            return response

        elif status == "SUBMITTED":
            response = f"Job '{job_name}' submitted successfully (not waiting for completion).\n\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            response += f"\nUse `get_databricks_job_status({run_id})` to check progress."
            return response

        else:
            response = f"Job '{job_name}' failed.\n\n"
            if run_id:
                response += f"**Run ID:** {run_id}\n"
            if job_url:
                response += f"**Job URL:** {job_url}\n"
            if error:
                response += f"**Error:** {error}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"
            return response

    except Exception as e:
        logger.error(f"Databricks job error: {str(e)}")
        return f"Error running Databricks job: {str(e)}"


@mcp.tool
def get_databricks_job_status(run_id: int) -> str:
    """
    Get the status of a Databricks job run.

    Args:
        run_id: The Databricks job run ID

    Returns:
        Job status information including state, result, and timing
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        logger.info(f"Getting status for Databricks job run: {run_id}")

        # Get job manager
        job_manager = get_job_manager()

        # Get job status
        status = job_manager.get_job_status(run_id)

        if not status:
            return f"Could not retrieve status for run ID: {run_id}"

        # Extract relevant information
        state = status.get('state', {})
        life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')
        result_state = state.get('result_state', 'N/A')
        state_message = state.get('state_message', '')

        # Timing information
        start_time = status.get('start_time')
        end_time = status.get('end_time')

        # Format response
        response = f"**Databricks Job Run Status**\n\n"
        response += f"**Run ID:** {run_id}\n"
        response += f"**Lifecycle State:** {life_cycle_state}\n"
        response += f"**Result State:** {result_state}\n"

        if state_message:
            response += f"**State Message:** {state_message}\n"

        if start_time:
            from datetime import datetime
            start_dt = datetime.fromtimestamp(start_time / 1000)
            response += f"**Start Time:** {start_dt.strftime('%Y-%m-%d %H:%M:%S')}\n"

        if end_time:
            end_dt = datetime.fromtimestamp(end_time / 1000)
            response += f"**End Time:** {end_dt.strftime('%Y-%m-%d %H:%M:%S')}\n"

        # Job URL
        job_url = databricks_get_run_url(run_id)
        response += f"**Job URL:** {job_url}\n"

        return response

    except Exception as e:
        logger.error(f"Error getting job status: {str(e)}")
        return f"Error getting job status: {str(e)}"


@mcp.tool
def cancel_databricks_job(run_id: int) -> str:
    """
    Cancel a running Databricks job.

    Args:
        run_id: The Databricks job run ID to cancel

    Returns:
        Cancellation result message
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        logger.info(f"Cancelling Databricks job run: {run_id}")

        # Get job manager
        job_manager = get_job_manager()

        # Cancel the job
        success = job_manager.cancel_job(run_id)

        if success:
            return f"Job run {run_id} has been cancelled successfully."
        else:
            return f"Failed to cancel job run {run_id}. It may have already completed or been cancelled."

    except Exception as e:
        logger.error(f"Error cancelling job: {str(e)}")
        return f"Error cancelling job: {str(e)}"


@mcp.tool
def get_databricks_job_logs(run_id: int, job_name: str = "job") -> str:
    """
    Get and save logs for a completed Databricks job run.

    Args:
        run_id: The Databricks job run ID
        job_name: Name to use for the log file (default: "job")

    Returns:
        Log content summary and path to saved log file
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        logger.info(f"Getting logs for Databricks job run: {run_id}")

        # Get job manager
        job_manager = get_job_manager()

        # Get cluster logs
        logs = job_manager.get_cluster_logs(run_id)

        stdout = logs.get('stdout', '')
        stderr = logs.get('stderr', '')

        # Format response
        response = f"**Logs for Run ID: {run_id}**\n\n"

        if stdout:
            # Truncate if too long
            if len(stdout) > 2000:
                response += f"**STDOUT (truncated):**\n```\n{stdout[:2000]}\n... (truncated, {len(stdout)} total chars)\n```\n\n"
            else:
                response += f"**STDOUT:**\n```\n{stdout}\n```\n\n"
        else:
            response += "**STDOUT:** (empty)\n\n"

        if stderr:
            if len(stderr) > 1000:
                response += f"**STDERR (truncated):**\n```\n{stderr[:1000]}\n... (truncated)\n```\n"
            else:
                response += f"**STDERR:**\n```\n{stderr}\n```\n"

        # Save logs to file
        from local_tools.databricks_job_submit import save_logs as databricks_save_logs
        log_path = databricks_save_logs(run_id, job_name)
        response += f"\n**Logs saved to:** {log_path}"

        return response

    except Exception as e:
        logger.error(f"Error getting job logs: {str(e)}")
        return f"Error getting job logs: {str(e)}"


@mcp.tool
def run_sql_tables_on_databricks(
    sql_file_path: str,
    job_name: Optional[str] = None,
    existing_cluster_id: Optional[str] = None,
    timeout_seconds: int = 7200,
    wait_for_completion: bool = True,
    save_logs: bool = True,
    cleanup_script: bool = True,
    snowflake_scope: str = "fionafan-scope",
    snowflake_warehouse: str = "TEAM_DATA_ANALYTICS_ETL",
    snowflake_role: str = "FIONAFAN",
    snowflake_schema: str = "FIONAFAN"
) -> str:
    """
    Run CREATE TABLE statements from a SQL file on Databricks via Snowflake.

    This tool:
    1. Parses the SQL file and extracts only CREATE TABLE / CREATE OR REPLACE TABLE statements
    2. Generates a Databricks notebook that executes these statements via Snowflake
    3. Submits the notebook to Databricks and optionally waits for completion

    All non-CREATE TABLE statements (SELECT, INSERT, UPDATE, etc.) are skipped.

    Args:
        sql_file_path: Path to the .sql file containing CREATE TABLE statements
        job_name: Name for the Databricks job (defaults to SQL filename)
        existing_cluster_id: Databricks cluster ID (falls back to DATABRICKS_CLUSTER_ID env var)
        timeout_seconds: Job timeout in seconds (default: 2 hours)
        wait_for_completion: Whether to wait for job to complete (default: True)
        save_logs: Whether to save logs locally after completion (default: True)
        cleanup_script: Whether to delete uploaded script from DBFS after completion (default: True)
        snowflake_scope: Databricks secrets scope for Snowflake credentials
        snowflake_warehouse: Snowflake warehouse to use
        snowflake_role: Snowflake role to use
        snowflake_schema: Snowflake schema to use

    Returns:
        Job results including tables created, status, run ID, and job URL
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        import os
        import tempfile

        # Convert to absolute path
        abs_sql_path = os.path.abspath(os.path.expanduser(sql_file_path))

        if not os.path.exists(abs_sql_path):
            return f"Error: SQL file not found: {abs_sql_path}"

        if not abs_sql_path.lower().endswith('.sql'):
            return f"Error: Expected .sql file, got: {abs_sql_path}"

        # Generate job name from filename if not provided
        if job_name is None:
            job_name = os.path.splitext(os.path.basename(abs_sql_path))[0]

        logger.info(f"Converting SQL file to Databricks notebook: {abs_sql_path}")

        # Convert SQL to notebook in a temp directory
        temp_dir = tempfile.mkdtemp(prefix="sql_to_databricks_")
        notebook_path = os.path.join(temp_dir, f"{job_name}.py")

        # Generate the notebook
        output_path, table_names, statement_count = sql_file_to_notebook(
            sql_file_path=abs_sql_path,
            output_path=notebook_path,
            snowflake_scope=snowflake_scope,
            snowflake_warehouse=snowflake_warehouse,
            snowflake_role=snowflake_role,
            snowflake_schema=snowflake_schema
        )

        if statement_count == 0:
            return f"No CREATE TABLE statements found in {abs_sql_path}. Only CREATE TABLE and CREATE OR REPLACE TABLE statements are supported."

        logger.info(f"Generated notebook with {statement_count} CREATE TABLE statements")
        logger.info(f"Tables to create: {', '.join(table_names)}")

        # Run the notebook on Databricks
        result = databricks_run_job(
            job_name=f"sql_tables_{job_name}",
            local_script_path=output_path,
            existing_cluster_id=existing_cluster_id,
            timeout_seconds=timeout_seconds,
            wait_for_completion=wait_for_completion,
            save_logs=save_logs,
            cleanup_script=cleanup_script
        )

        # Clean up temp notebook file
        try:
            os.remove(output_path)
            os.rmdir(temp_dir)
        except Exception:
            pass  # Ignore cleanup errors

        # Format response
        status = result.get('status', 'UNKNOWN')
        run_id = result.get('databricks_run_id')
        job_url = result.get('job_url', '')
        log_file = result.get('log_file')
        error = result.get('error')

        response = f"**SQL Tables Job: {job_name}**\n\n"
        response += f"**Source SQL:** {abs_sql_path}\n"
        response += f"**CREATE TABLE statements found:** {statement_count}\n"
        response += f"**Tables:** {', '.join(table_names)}\n\n"

        if status == "SUCCESS":
            response += f"**Status:** SUCCESS\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"

            # Include job results if available
            job_results = result.get('job_results')
            if job_results:
                response += f"\n**Execution Results:**\n```json\n{json.dumps(job_results, indent=2)}\n```"

            return response

        elif status == "SUBMITTED":
            response += f"**Status:** SUBMITTED (not waiting for completion)\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            response += f"\nUse `get_databricks_job_status({run_id})` to check progress."
            return response

        else:
            response += f"**Status:** FAILED\n"
            if run_id:
                response += f"**Run ID:** {run_id}\n"
            if job_url:
                response += f"**Job URL:** {job_url}\n"
            if error:
                response += f"**Error:** {error}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"
            return response

    except Exception as e:
        logger.error(f"SQL tables job error: {str(e)}")
        return f"Error running SQL tables job: {str(e)}"


@mcp.tool
def run_sql_text_on_databricks(
    sql_text: str,
    job_name: Optional[str] = None,
    existing_cluster_id: Optional[str] = None,
    timeout_seconds: int = 7200,
    wait_for_completion: bool = True,
    save_logs: bool = True,
    cleanup_script: bool = True,
    snowflake_scope: str = "fionafan-scope",
    snowflake_warehouse: str = "TEAM_DATA_ANALYTICS_ETL",
    snowflake_role: str = "FIONAFAN",
    snowflake_schema: str = "FIONAFAN"
) -> str:
    """
    Run CREATE TABLE statements from raw SQL text on Databricks via Snowflake.

    Mirrors run_sql_tables_on_databricks, but takes SQL content directly
    instead of a file path.
    """
    if not DATABRICKS_AVAILABLE:
        return "Databricks job submission not available. Please ensure DATABRICKS_WORKSPACE_URL and DATABRICKS_ACCESS_TOKEN environment variables are set."

    try:
        import tempfile

        # Persist SQL text to a temp file for reuse with existing flow
        temp_dir = tempfile.mkdtemp(prefix="sql_text_to_dbx_")
        sql_path = os.path.join(temp_dir, "input.sql")
        with open(sql_path, "w", encoding="utf-8") as f:
            f.write(sql_text)

        if job_name is None:
            job_name = "sql_text_job"

        # Convert SQL to a Databricks notebook
        notebook_path = os.path.join(temp_dir, f"{job_name}.py")
        output_path, table_names, statement_count = sql_file_to_notebook(
            sql_file_path=sql_path,
            output_path=notebook_path,
            snowflake_scope=snowflake_scope,
            snowflake_warehouse=snowflake_warehouse,
            snowflake_role=snowflake_role,
            snowflake_schema=snowflake_schema
        )

        if statement_count == 0:
            return "No CREATE TABLE statements found in provided SQL text. Only CREATE TABLE and CREATE OR REPLACE TABLE statements are supported."

        logger.info(f"Generated notebook with {statement_count} CREATE TABLE statements")
        logger.info(f"Tables to create: {', '.join(table_names)}")

        # Run the notebook on Databricks
        result = databricks_run_job(
            job_name=f"sql_tables_{job_name}",
            local_script_path=output_path,
            existing_cluster_id=existing_cluster_id,
            timeout_seconds=timeout_seconds,
            wait_for_completion=wait_for_completion,
            save_logs=save_logs,
            cleanup_script=cleanup_script
        )

        # Clean up temp files
        try:
            os.remove(output_path)
            os.remove(sql_path)
            os.rmdir(temp_dir)
        except Exception:
            pass

        # Format response
        status = result.get('status', 'UNKNOWN')
        run_id = result.get('databricks_run_id')
        job_url = result.get('job_url', '')
        log_file = result.get('log_file')
        error = result.get('error')

        response = f"**SQL Tables Job (text): {job_name}**\n\n"
        response += f"**CREATE TABLE statements found:** {statement_count}\n"
        response += f"**Tables:** {', '.join(table_names)}\n\n"

        if status == "SUCCESS":
            response += f"**Status:** SUCCESS\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"

            job_results = result.get('job_results')
            if job_results:
                response += f"\n**Execution Results:**\n```json\n{json.dumps(job_results, indent=2)}\n```"

            return response

        elif status == "SUBMITTED":
            response += f"**Status:** SUBMITTED (not waiting for completion)\n"
            response += f"**Run ID:** {run_id}\n"
            response += f"**Job URL:** {job_url}\n"
            response += f"\nUse `get_databricks_job_status({run_id})` to check progress."
            return response

        else:
            response += f"**Status:** FAILED\n"
            if run_id:
                response += f"**Run ID:** {run_id}\n"
            if job_url:
                response += f"**Job URL:** {job_url}\n"
            if error:
                response += f"**Error:** {error}\n"
            if log_file:
                response += f"**Logs saved to:** {log_file}\n"
            return response

    except Exception as e:
        logger.error(f"SQL text job error: {str(e)}")
        return f"Error running SQL text job: {str(e)}"


# ============================================================================
# SERVER ENTRY POINT
# ============================================================================

def main():
    """Main entry point for the MCP server."""
    # Disable banner to prevent it from breaking JSON-RPC protocol on stdout
    mcp.run(show_banner=False)


if __name__ == "__main__":
    main()