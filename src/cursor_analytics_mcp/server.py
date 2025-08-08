#!/usr/bin/env python3
"""
Cursor Analytics MCP Server using FastMCP

A standalone MCP server providing tools for:
- Snowflake operations (query execution, table management)
- Query search functionality  
- Curie experiment exports
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
    from utils.query_search import search_queries_by_keywords, save_results_to_context
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

@mcp.tool
def get_search_system_status() -> str:
    """
    Get the current status of the search system including table configuration
    
    Returns:
        Status information about the search system
    """
    try:
        status = []
        status.append("🔍 Search System Status")
        status.append("=" * 50)
        
        # Check if hybrid search is available
        if HYBRID_SEARCH_AVAILABLE:
            status.append("✅ Hybrid search module: Available")
        else:
            status.append("❌ Hybrid search module: Not available")
            return "\n".join(status)
        
        # Check searcher configuration
        status.append("\n📊 Table Configuration:")
        status.append(f"  Database: proddb")
        status.append(f"  Schema: fionafan") 
        status.append(f"  Table: document_index")
        status.append(f"  Full path: proddb.fionafan.document_index")
        
        # Test connection
        searcher = get_configured_hybrid_searcher()
        if searcher:
            status.append("\n✅ Snowflake connection: Success")
            
            # Try to get table stats
            try:
                hook = searcher.get_snowflake_hook()
                cursor = hook.conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM proddb.fionafan.document_index")
                total_count = cursor.fetchone()[0]
                
                cursor.execute("SELECT category, COUNT(*) FROM proddb.fionafan.document_index GROUP BY category ORDER BY COUNT(*) DESC")
                categories = cursor.fetchall()
                
                status.append(f"\n📈 Table Statistics:")
                status.append(f"  Total documents: {total_count}")
                status.append(f"  Categories:")
                for cat, count in categories:
                    status.append(f"    - {cat}: {count} chunks")
                
                cursor.close()
            except Exception as e:
                status.append(f"\n⚠️  Table statistics: Error - {str(e)}")
        else:
            status.append("\n❌ Snowflake connection: Failed")
        
        return "\n".join(status)
        
    except Exception as e:
        logger.error(f"Get search system status error: {str(e)}")
        return f"Error getting search system status: {str(e)}"

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


@mcp.tool
def snowflake_create_table(
    table_name: str,
    data: str,
    database: Optional[str] = None,
    schema: Optional[str] = None,
    warehouse: Optional[str] = None,
    overwrite: bool = True
) -> str:
    """
    Create and populate a table in Snowflake from DataFrame data.
    
    Args:
        table_name: Name of the table to create
        data: JSON string of the data to insert (list of dicts)
        database: Database name (optional)
        schema: Schema name (optional)
        warehouse: Warehouse name (optional)
        overwrite: Whether to overwrite existing table
    
    Returns:
        Success/error message
    """
    try:
        # Parse JSON data
        import pandas as pd
        data_parsed = json.loads(data)
        df = pd.DataFrame(data_parsed)
        
        # Create SnowflakeHook with optional parameters
        hook_kwargs = {}
        if database:
            hook_kwargs["database"] = database
        if schema:
            hook_kwargs["schema"] = schema  
        if warehouse:
            hook_kwargs["warehouse"] = warehouse
            
        with SnowflakeHook(**hook_kwargs) as sf:
            if overwrite:
                # Drop table if it exists
                try:
                    sf.drop_table(table_name)
                except:
                    pass  # Table might not exist
                    
            sf.create_and_populate_table(df, table_name)
            
        return f"Table '{table_name}' created successfully with {len(df)} rows."
        
    except Exception as e:
        logger.error(f"Create table error: {str(e)}")
        return f"Error creating table: {str(e)}"


@mcp.tool
def snowflake_drop_table(
    table_name: str,
    database: Optional[str] = None,
    schema: Optional[str] = None,
    warehouse: Optional[str] = None
) -> str:
    """
    Drop a table from Snowflake.
    
    Args:
        table_name: Name of the table to drop
        database: Database name (optional)
        schema: Schema name (optional)
        warehouse: Warehouse name (optional)
    
    Returns:
        Success/error message
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
            sf.drop_table(table_name)
            
        return f"Table '{table_name}' dropped successfully."
        
    except Exception as e:
        logger.error(f"Drop table error: {str(e)}")
        return f"Error dropping table: {str(e)}"


# ============================================================================
# QUERY SEARCH
# ============================================================================

@mcp.tool
def query_search(
    keywords: List[str],
    limit: int = 10,
    save_to_context: bool = True
) -> str:
    """
    Search for historical queries by keywords.
    
    Args:
        keywords: Keywords to search for in query history
        limit: Maximum number of results to return
        save_to_context: Whether to save results to context directory
    
    Returns:
        Formatted search results
    """
    try:
        # Search for queries
        results = search_queries_by_keywords(keywords)
        
        if not results:
            return f"No queries found matching keywords: {', '.join(keywords)}"
        
        # Save to context if requested
        saved_path = None
        if save_to_context:
            saved_path = save_results_to_context(results, keywords, limit)
        
        # Format results for display
        limited_results = results[:limit]
        response = f"Found {len(results)} queries matching keywords: {', '.join(keywords)}\n"
        if saved_path:
            response += f"Results saved to: {saved_path}\n"
        response += f"\nTop {len(limited_results)} results:\n\n"
        
        for i, result in enumerate(limited_results, 1):
            response += f"--- Query {i} ---\n"
            response += f"Query ID: {result.get('QUERY_ID')}\n"
            response += f"User: {result.get('USER_NAME')}\n"
            response += f"Time: {result.get('START_TIME')}\n"
            response += f"Type: {result.get('QUERY_TYPE')}\n"
            query_text = result.get('QUERY_TEXT', '')[:500]  # Truncate for display
            if len(result.get('QUERY_TEXT', '')) > 500:
                query_text += "... (truncated)"
            response += f"Query: {query_text}\n"
            response += "-" * 50 + "\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Query search error: {str(e)}")
        return f"Error searching queries: {str(e)}"


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