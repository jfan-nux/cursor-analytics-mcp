"""
DEFAULT QUERY SEARCH TOOL - Use this faster version for most query searches.
This tool queries a test table that is optimized for performance.
Only use query_search_slow.py when you can't find what you need with this tool.
"""

from typing import List, Dict, Any
from utils.snowflake_connection import SnowflakeHook
import sys
import logging
import os
import json
from datetime import datetime
from pathlib import Path

# Create a logger for this module
from utils.logger import get_logger
logger = get_logger(__name__)

def search_queries_by_keywords(keywords: List[str]) -> List[Dict[str, Any]]:
    """
    Search for historical queries containing keywords in Snowflake query history.

    Args:
        keywords (List[str]): List of keywords to search for

    Returns:
        List[Dict[str, Any]]: List of query records sorted by latest date
    """
    # Build keyword filter condition for the SQL query
    keyword_conditions = []
    for keyword in keywords:
        # Case-insensitive search in query text
        keyword_conditions.append(f"UPPER(QUERY_TEXT) LIKE UPPER('%{keyword}%')")

    keyword_filter = " AND ".join(keyword_conditions)

    # SQL query to search for queries using the new table structure
    # Note: The new table has different columns, adapted accordingly
    query = f"""
    -- CURSOR_ANALYTICS_QUERY_SEARCH: {', '.join(keywords)}
    SELECT
        QID AS QUERY_ID,
        QUERY_TEXT,
        CURRENT_TIMESTAMP() AS START_TIME,  -- Using current timestamp as placeholder
        CURRENT_TIMESTAMP() AS END_TIME,
        'SUCCESS' AS EXECUTION_STATUS,
        PURPOSE AS QUERY_TYPE,
        DD_USER AS USER_NAME
    FROM ethanzhu.cursor_query_search_test_0420
    WHERE
        {keyword_filter}
    ORDER BY
        QID DESC  -- Assuming QID is some form of identifier that can be sorted
    LIMIT 100
    """

    # Use SnowflakeHook to connect to Snowflake and execute the query
    try:
        with SnowflakeHook(use_persistent_spark=False) as sf:
            # Use pandas method instead of Spark to avoid Java dependency
            results = sf.fetch_pandas_all(query)
            # Convert to list of dictionaries for consistency with the original function
            return results.to_dict('records')
    except Exception as e:
        logger.error(f"Error searching for queries: {str(e)}")
        raise

def save_results_to_context(results: List[Dict[str, Any]], keywords: List[str], limit: int = 10) -> str:
    """
    Save the query results to a file in the context folder.

    Args:
        results: List of query results to save
        keywords: The keywords used for the search
        limit: Maximum number of results to save (default: 10)

    Returns:
        Path to the saved file
    """
    # Create context directory if it doesn't exist
    # Use absolute path to ensure files are saved in the right location
    context_dir = Path(__file__).parent.parent / "context" / "query_search"
    context_dir.mkdir(parents=True, exist_ok=True)

    # Format current timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"query_search_{'_'.join(keywords)}_{timestamp}.sql"
    filepath = context_dir / filename

    # Take only the specified limit of results
    results_to_save = results[:limit]

    # Write the results to the file
    with open(filepath, "w") as f:
        f.write(f"-- Query search results for: {', '.join(keywords)}\n")
        f.write(f"-- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"-- Number of results: {min(len(results), limit)} of {len(results)} total found\n\n")

        for i, result in enumerate(results_to_save, 1):
            f.write(f"-- Query {i} --\n")
            f.write(f"-- Query ID: {result.get('QUERY_ID')}\n")
            f.write(f"-- Database: {result.get('DATABASE_NAME', 'N/A')}.{result.get('SCHEMA_NAME', 'N/A')}\n")
            f.write(f"-- Time: {result.get('START_TIME')}\n")
            f.write(f"-- User: {result.get('USER_NAME')}\n")
            f.write(f"-- Type: {result.get('QUERY_TYPE')}\n\n")

            # Write the query text
            query_text = result.get('QUERY_TEXT', '')
            f.write(f"{query_text}\n\n")
            f.write("-- " + "-" * 70 + "\n\n")

    logger.info(f"Saved {min(len(results), limit)} query results to {filepath}")
    return str(filepath)

if __name__ == "__main__":
    # Default limit for number of results to save
    limit = 10

    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python query_search_alt.py [--limit N] <keyword1> [keyword2 ...]")
        sys.exit(1)

    # Check for limit parameter
    if sys.argv[1] == '--limit' and len(sys.argv) >= 4:
        try:
            limit = int(sys.argv[2])
            # Remove the limit arguments
            keywords = sys.argv[3:]
        except ValueError:
            print("Error: --limit must be followed by a number")
            sys.exit(1)
    else:
        # No limit parameter, all arguments are keywords
        keywords = sys.argv[1:]

    logger.info(f"Searching for queries with keywords: {keywords}")

    try:
        # Call the search function
        results = search_queries_by_keywords(keywords)

        # Save results to context file
        if results:
            filepath = save_results_to_context(results, keywords, limit)
            print(f"Found {len(results)} matching queries. Top {min(len(results), limit)} saved to {filepath}")

            # Print the results
            if results:
                print(f"\nQuery preview (showing top {min(len(results), 5)} of {len(results)}):")
                for i, result in enumerate(results[:5], 1):
                    print(f"\n--- Query {i} ---")
                    print(f"Query ID: {result.get('QUERY_ID')}")
                    print(f"Database: {result.get('DATABASE_NAME', 'N/A')}.{result.get('SCHEMA_NAME', 'N/A')}")
                    print(f"Time: {result.get('START_TIME')}")
                    print(f"User: {result.get('USER_NAME')}")
                    print("-" * 80)
        else:
            print("No matching queries found.")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)