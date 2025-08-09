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
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Add local utils to path (utils is in the cursor-analytics-mcp root)
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import local modules
try:
    from utils.snowflake_connection import SnowflakeHook
    from utils.curie_export.export_helper import (
        export_curie_with_explicit_params,
        get_experiment_metadata
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

# Try to import hybrid search functionality
try:
    from utils.document_indexer.hybrid_search import HybridSearcher
    HYBRID_SEARCH_AVAILABLE = True
except ImportError:
    print("Warning: Hybrid search not available. Document indexing may not be set up.")
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

def get_configured_hybrid_searcher():
    """
    Get a properly configured HybridSearcher with error handling
    
    Returns:
        HybridSearcher instance or None if initialization fails
    """
    if not HYBRID_SEARCH_AVAILABLE:
        return None
    
    try:
        # Explicit table configuration for clarity
        searcher = HybridSearcher(database="proddb", schema="fionafan", table="document_index")
        
        # Validate Snowflake connection
        hook = searcher.get_snowflake_hook()
        if not hook:
            logger.error("Failed to establish Snowflake connection")
            return None
            
        return searcher
    except Exception as e:
        logger.error(f"Failed to initialize HybridSearcher: {str(e)}")
        return None



# ============================================================================
# SNOWFLAKE OPERATIONS
# ============================================================================

@mcp.tool
def snowflake_query(
    query: str,
    method: str = "pandas",
    database: Optional[str] = None,
    schema: Optional[str] = None,
    warehouse: Optional[str] = None
) -> str:
    """
    Execute SQL queries on Snowflake using SnowflakeHook.
    
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
            if method == "pandas":
                result = sf.query_snowflake(query, method="pandas")
                # Convert DataFrame to JSON for transport
                result_json = result.to_json(orient="records", date_format="iso")
                return f"Query executed successfully. Returned {len(result)} rows.\n\nData (JSON):\n{result_json}"
            elif method == "spark":
                result = sf.query_snowflake(query, method="spark")
                # For Spark DataFrame, show schema and sample data
                schema_info = str(result.schema)
                sample_data = result.limit(10).toPandas().to_json(orient="records", date_format="iso")
                return f"Query executed successfully.\n\nSchema:\n{schema_info}\n\nSample data (first 10 rows):\n{sample_data}"
            else:
                return f"Method '{method}' not yet implemented"
                
    except Exception as e:
        logger.error(f"Snowflake query error: {str(e)}")
        return f"Error executing query: {str(e)}"





# ============================================================================
# QUERY SEARCH
# ============================================================================

@mcp.tool
def query_search(
    table_name: str,
    limit: int = 5
) -> str:
    """
    Find the top most used queries for a specific table in the last 30 days.
    Uses Tyler's sf_table_usage table to find patterns.
    
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
            
            # Step 2: Try to find the top 5 most used queries in the last 30 days
            most_used_queries_sql = f"""
            WITH recent_queries AS (
                SELECT 
                    query_text,
                    dd_user,
                    start_time,
                    COUNT(*) as execution_count,
                    MAX(start_time) as latest_execution
                FROM tyleranderson.sf_table_usage
                WHERE fully_qualified_table_name = '{full_table_name}'
                  AND start_time >= CURRENT_DATE - 30
                  AND query_text IS NOT NULL
                  AND LENGTH(TRIM(query_text)) > 10  -- Filter out very short queries
                GROUP BY query_text, dd_user, start_time
                HAVING execution_count >= 1
                ORDER BY execution_count DESC, latest_execution DESC
                LIMIT {limit * 3}  -- Get more results to filter from
            ),
            distinct_queries AS (
                SELECT DISTINCT
                    query_text,
                    SUM(execution_count) as total_executions,
                    MAX(latest_execution) as most_recent_execution,
                    LISTAGG(DISTINCT dd_user, ', ') as users
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
            
            result_df = sf.query_snowflake(most_used_queries_sql, method="pandas")
            
            # Step 3: If no frequently used queries found, find most active user and their recent queries
            if result_df.empty:
                fallback_sql = f"""
                WITH most_active_user AS (
                    SELECT dd_user
                    FROM tyleranderson.sf_table_usage
                    WHERE fully_qualified_table_name = '{full_table_name}'
                      AND start_time >= CURRENT_DATE - 30
                    GROUP BY dd_user
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                ),
                user_queries AS (
                    SELECT DISTINCT
                        query_text,
                        MAX(start_time) as latest_execution_time,
                        dd_user
                    FROM tyleranderson.sf_table_usage
                    WHERE fully_qualified_table_name = '{full_table_name}'
                      AND start_time >= CURRENT_DATE - 30
                      AND dd_user = (SELECT dd_user FROM most_active_user)
                      AND query_text IS NOT NULL
                      AND LENGTH(TRIM(query_text)) > 10
                    GROUP BY query_text, dd_user
                    ORDER BY latest_execution_time DESC
                    LIMIT {limit}
                )
                SELECT 
                    query_text,
                    1 as total_executions,
                    latest_execution_time as most_recent_execution,
                    dd_user as users
                FROM user_queries
                ORDER BY latest_execution_time DESC
                """
                
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
                if len(query_text) > 800:
                    truncated_query = query_text[:800] + "\n... (truncated)"
                else:
                    truncated_query = query_text
                    
                response += f"💻 Query:\n{truncated_query}\n"
                response += "-" * 70 + "\n\n"
            
            return response
            
    except Exception as e:
        logger.error(f"Table query search error: {str(e)}")
        return f"Error searching queries for table '{table_name}': {str(e)}"


# ============================================================================
# CURIE EXPERIMENT EXPORT
# ============================================================================

@mcp.tool
def curie_export(
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
    try:
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
        
        if success:
            response = f"✅ Curie export completed successfully!\n\n"
            response += f"📊 Google Sheets URL: {url}\n"
            if detected_control:
                response += f"🎯 Control variant: {detected_control}\n"
            response += f"\nThe sheet has been created and formatted with experiment results."
        else:
            response = f"❌ Curie export failed.\n\nError details may be available in the logs."
            
        return response
        
    except Exception as e:
        logger.error(f"Curie export error: {str(e)}")
        return f"Error exporting Curie results: {str(e)}"


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

@mcp.tool
def fetch_table_context(query: str, top_k: int = 5) -> str:
    """
    Search for Snowflake table context using hybrid search (BM25 + embeddings).
    Use natural language queries like 'user dimensions table', 'delivery facts', etc.
    
    Args:
        query: Natural language search query for table context
        top_k: Number of top results to return (default: 5)
    
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
        results = searcher.search_table_context(query, top_k=top_k)
        
        if not results:
            return f"No table context found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        return searcher.format_search_results(results, query)
            
    except Exception as e:
        logger.error(f"Fetch table context error: {str(e)}")
        return f"Error fetching table context: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_pod_queries(query: str, top_k: int = 3) -> str:
    """
    Search for validated master queries using hybrid search (BM25 + embeddings).
    Use natural language queries like 'pricing analysis', 'affordability metrics', etc.
    
    Args:
        query: Natural language search query for SQL queries (use 'list' to see all available queries)
        top_k: Number of top results to return (default: 3)
    
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
        results = searcher.search_pod_queries(query, top_k=top_k)
        
        if not results:
            return f"No pod-level queries found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        return searcher.format_search_results(results, query)
                
    except Exception as e:
        logger.error(f"Fetch pod queries error: {str(e)}")
        return f"Error fetching pod queries: {str(e)}. Please ensure the document index table exists and is populated."


@mcp.tool
def fetch_user_context(query: str, top_k: int = 5) -> str:
    """
    Search for user-specific context using hybrid search (BM25 + embeddings).
    Use natural language queries to find relevant user context documents.
    
    Args:
        query: Natural language search query for user context (use 'list' to see all available files)
        top_k: Number of top results to return (default: 5)
    
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
        results = searcher.search_user_context(query, top_k=top_k)
        
        if not results:
            return f"No user context found for query: '{query}'. The document index may be empty or the query didn't match any content."
        
        return searcher.format_search_results(results, query)
                
    except Exception as e:
        logger.error(f"Fetch user context error: {str(e)}")
        return f"Error fetching user context: {str(e)}. Please ensure the document index table exists and is populated."


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
def generate_snowflake_table_context(
    table_name: str,
    print_only: bool = True,
    output_format: str = "markdown",
    sample_row_limit: int = 10,
    verbose: bool = False
) -> str:
    """
    Generate comprehensive context documentation for a Snowflake table.
    
    This tool creates detailed documentation including business context, 
    metadata analysis, granularity detection, and sample queries.
    
    Args:
        table_name: Table name (can be partial or fully qualified)
        print_only: If True, only returns content. If False, also saves to file.
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
        
        if print_only:
            # Generate the table context using the agent (return content only)
            result = generate_table_context(
                table=table_name,
                print_only=True,
                sample_row_limit=sample_row_limit,
                verbose=verbose
            )
            file_path = None
        else:
            # Import table resolution to get full qualified name for directory structure
            from local_tools.table_context_agent.tyler_sources import resolve_table_name
            
            # Resolve table name first to construct proper output directory
            with SnowflakeHook() as sf:
                try:
                    full_table_name = resolve_table_name(sf, table_name, verbose=False)
                except Exception:
                    # Fallback: use input as-is if resolution fails
                    full_table_name = table_name
            
            # Construct output directory based on full table name
            # Default context directory structure: context/analysis-context/snowflake-table-context/
            context_base = PROJECT_ROOT / "context" / "analysis-context" / "snowflake-table-context"
            
            # Generate and save the table context using the agent
            result_path = generate_table_context(
                table=table_name,
                output_root=str(context_base),
                sample_row_limit=sample_row_limit,
                verbose=verbose
            )
            
            # Also get the content to return
            result = generate_table_context(
                table=table_name,
                print_only=True,
                sample_row_limit=sample_row_limit,
                verbose=verbose
            )
            
            file_path = str(result_path)
            logger.info(f"Table context saved to: {file_path}")
        
        if output_format.lower() == "json":
            # Convert markdown result to JSON structure
            response = {
                "table_name": table_name,
                "format": "markdown",
                "content": result,
                "generated_at": "auto",
                "status": "success"
            }
            if file_path:
                response["file_path"] = file_path
                response["message"] = f"Content generated and saved to {file_path}"
            return json.dumps(response, indent=2)
        else:
            # Return raw markdown with optional file path info
            if file_path:
                return f"📁 File saved to: {file_path}\n\n{result}"
            else:
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
def get_table_context_status() -> str:
    """
    Check the status and availability of the table context generation system.
    
    Returns:
        JSON status information about table context capabilities
    """
    status = {
        "table_context_agent_available": TABLE_CONTEXT_AVAILABLE,
        "dependencies": {},
        "features": [],
        "version": "1.0.0"
    }
    
    if TABLE_CONTEXT_AVAILABLE:
        try:
            # Check individual dependencies
            status["dependencies"]["snowflake_connection"] = True
            status["dependencies"]["confluence_client"] = True
            status["dependencies"]["portkey_llm"] = True
            
            # List available features
            status["features"] = [
                "Table name resolution and validation",
                "Business context generation with LLM",
                "Metadata analysis and formatting", 
                "Granularity detection and analysis",
                "Large table performance optimization (>10B rows)",
                "Sample query extraction",
                "Confluence documentation integration",
                "Case-insensitive field access",
                "Markdown and JSON output formats"
            ]
            
            status["status"] = "ready"
            status["message"] = "Table context agent is fully operational"
            
        except Exception as e:
            status["status"] = "degraded"
            status["error"] = str(e)
            status["message"] = "Table context agent has dependency issues"
    else:
        status["status"] = "unavailable"
        status["message"] = "Table context agent not available - check installation"
        
    return json.dumps(status, indent=2)


@mcp.tool
def list_context_sources(source_type: str = "all") -> str:
    """
    List all available context sources and their contents.
    
    Args:
        source_type: Type of context source to list (all, table_context, pod_queries, user_context, cursor_rules)
    
    Returns:
        Formatted overview of context sources
    """
    try:
        response = "📚 CURSOR ANALYTICS CONTEXT SOURCES\n"
        response += "=" * 50 + "\n\n"
        
        if source_type in ["all", "table_context"]:
            response += "🗂️  SNOWFLAKE TABLE CONTEXT\n"
            response += "Location: context/analysis-context/snowflake-table-context/\n"
            table_context_path = PROJECT_ROOT / "context" / "analysis-context" / "snowflake-table-context"
            if table_context_path.exists():
                count = 0
                for db_dir in table_context_path.iterdir():
                    if db_dir.is_dir():
                        for schema_dir in db_dir.iterdir():
                            if schema_dir.is_dir():
                                tables = list(schema_dir.glob("*.md"))
                                count += len(tables)
                                if tables:
                                    response += f"  📊 {db_dir.name}.{schema_dir.name}: {len(tables)} tables\n"
                response += f"Total table context files: {count}\n\n"
            else:
                response += "  ⚠️  Table context directory not found\n\n"
        
        if source_type in ["all", "pod_queries"]:
            response += "🎯 POD-LEVEL VALIDATED QUERIES\n"
            response += "Location: context/pod-level-validated-master-queries/\n"
            pod_path = PROJECT_ROOT / "context" / "pod-level-validated-master-queries"
            if pod_path.exists():
                sql_files = list(pod_path.glob("*.sql"))
                response += f"Available queries: {len(sql_files)}\n"
                for sql_file in sql_files[:5]:  # Show first 5
                    response += f"  📄 {sql_file.stem}\n"
                if len(sql_files) > 5:
                    response += f"  ... and {len(sql_files) - 5} more\n"
                response += "\n"
            else:
                response += "  ⚠️  Pod queries directory not found\n\n"
        
        if source_type in ["all", "user_context"]:
            response += "👤 USER CONTEXT\n"
            response += "Location: context/user-context/\n"
            user_path = PROJECT_ROOT / "context" / "user-context"
            if user_path.exists():
                files = list(user_path.rglob("*"))
                file_count = len([f for f in files if f.is_file()])
                dir_count = len([f for f in files if f.is_dir()]) - 1  # Exclude root
                response += f"Total files: {file_count}, directories: {dir_count}\n\n"
            else:
                response += "  ⚠️  User context directory not found\n\n"
        
        if source_type in ["all", "cursor_rules"]:
            response += "⚙️  CURSOR RULES\n"
            response += "Location: .cursor/rules/\n"
            rules_path = PROJECT_ROOT / ".cursor" / "rules"
            if rules_path.exists():
                mdc_files = list(rules_path.glob("*.mdc"))
                response += f"Available rules: {len(mdc_files)}\n"
                for rule_file in mdc_files:
                    response += f"  📋 {rule_file.stem}\n"
                response += "\n"
            else:
                response += "  ⚠️  Cursor rules directory not found\n\n"
        
        response += "💡 Use specific fetch tools to retrieve content from any of these sources."
        
        return response
        
    except Exception as e:
        logger.error(f"List context sources error: {str(e)}")
        return f"Error listing context sources: {str(e)}"


# ============================================================================
# SERVER ENTRY POINT
# ============================================================================

def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()