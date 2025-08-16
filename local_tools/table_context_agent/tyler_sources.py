from typing import Any, Dict, List, Optional, Tuple


def format_row_count(row_count: Optional[int]) -> str:
    """Format row count in human-readable format (xxB, xxM, xxK)."""
    if row_count is None or row_count == 0:
        return "0 rows"
    
    if row_count >= 1_000_000_000:
        return f"{row_count / 1_000_000_000:.1f}B rows"
    elif row_count >= 1_000_000:
        return f"{row_count / 1_000_000:.1f}M rows"
    elif row_count >= 1_000:
        return f"{row_count / 1_000:.1f}K rows"
    else:
        return f"{row_count} rows"


def resolve_table_name(sf, table_input: str, verbose: bool = False) -> str:
    """
    Resolve table name to full qualified name.
    If input is partial (e.g., dimension_deliveries), find most commonly used full name.
    If input is already full (e.g., proddb.public.dimension_deliveries), return as-is.
    """
    # Check if it's already a full table name (contains dots)
    if '.' in table_input and table_input.count('.') >= 2:
        # Verify it exists in usage table
        verify_query = f"""
        SELECT fully_qualified_table_name, COUNT(*) as usage_count
        FROM tyleranderson.sf_table_usage
        WHERE fully_qualified_table_name = '{table_input}'
        GROUP BY fully_qualified_table_name
        """
        if verbose:
            print(f"      🔍 SQL: {verify_query}")
        try:
            df = sf.query_snowflake(verify_query, method="pandas")
            if not df.empty:
                if verbose:
                    print(f"      ✅ Found exact match: {table_input}")
                return table_input
        except Exception:
            pass
    
    # Extract table name from input (handle cases like schema.table or just table)
    table_parts = table_input.split('.')
    table_name = table_parts[-1]  # Last part is always the table name
    
    # Find most commonly used version from sf_table_usage
    usage_query = f"""
    SELECT fully_qualified_table_name, COUNT(*) as usage_count
    FROM tyleranderson.sf_table_usage
    WHERE table_name = '{table_name}'
    GROUP BY fully_qualified_table_name
    ORDER BY usage_count DESC
    LIMIT 1
    """
    
    if verbose:
        print(f"      🔍 SQL: {usage_query}")
    
    try:
        df = sf.query_snowflake(usage_query, method="pandas")
        if not df.empty:
            result = str(df.iloc[0]["fully_qualified_table_name"])
            if verbose:
                print(f"      ✅ Found most used version: {result}")
            return result
    except Exception:
        pass
    
    # Fallback: try to find in sf_tables_full
    fallback_query = f"""
    SELECT LOWER(table_catalog) || '.' || LOWER(table_schema) || '.' || LOWER(table_name) as fqn
    FROM tyleranderson.sf_tables_full
    WHERE lower(table_name) = lower('{table_name}')
    ORDER BY row_count DESC NULLS LAST
    LIMIT 1
    """
    
    try:
        df = sf.query_snowflake(fallback_query, method="pandas")
        if not df.empty:
            return str(df.iloc[0]["fqn"])
    except Exception:
        pass
    
    # If all else fails, return the input
    return table_input


def fetch_table_overview(sf, database: str, schema: str, table: str, verbose: bool = False) -> Dict[str, Any]:
    """Return core table-level metadata from Tyler tables with formatted row counts."""
    query = f"""
    SELECT 
        TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, TABLE_OWNER, TABLE_TYPE, IS_TRANSIENT,
        ROW_COUNT, BYTES, RETENTION_TIME, CREATED, LAST_ALTERED, COMMENT
    FROM tyleranderson.sf_tables_full
    WHERE lower(TABLE_CATALOG)=lower('{database}')
      AND lower(TABLE_SCHEMA)=lower('{schema}')
      AND lower(TABLE_NAME)=lower('{table}')
    LIMIT 1
    """
    if verbose:
        print(f"      🔍 SQL: {query}")
    df = sf.query_snowflake(query, method="pandas")
    if df.empty:
        return {}
    
    result = df.iloc[0].to_dict()
    # Add formatted row count
    if 'ROW_COUNT' in result:
        result['FORMATTED_ROW_COUNT'] = format_row_count(result['ROW_COUNT'])
    
    return result


def fetch_columns_metadata_with_usage(sf, full_table_name: str, verbose: bool = False) -> List[Dict[str, Any]]:
    """
    Return column-level metadata with usage ranking and all required fields.
    This implements the enhanced column query from requirements.
    """
    query = f"""
    WITH usage AS (
        -- Aggregate usage data from sf_column_usage
        SELECT
            fully_qualified_table_name,
            column_name,
            SUM(query_count) AS queries,
            COUNT(DISTINCT dd_user) AS unique_users,
            COUNT(DISTINCT department) AS unique_departments,
            COUNT(DISTINCT query_category) AS unique_query_categories
        FROM tyleranderson.sf_column_usage
        WHERE fully_qualified_table_name = '{full_table_name}'
        GROUP BY fully_qualified_table_name, column_name
    ),
    setup AS (
        -- Get all column metadata from sf_columns
        SELECT
            table_catalog,
            table_schema,
            table_name,
            column_name,
            data_type,
            ordinal_position,
            character_maximum_length,
            common_values,
            is_cluster_key,
            comment,
            LOWER(table_catalog) || '.' || LOWER(table_schema) || '.' || LOWER(table_name) AS fully_qualified_table_name
        FROM tyleranderson.sf_columns
        WHERE LOWER(table_catalog) || '.' || LOWER(table_schema) || '.' || LOWER(table_name) = '{full_table_name}'
    )
    SELECT
        ROW_NUMBER() OVER (ORDER BY COALESCE(u.queries, 0) DESC, s.ordinal_position ASC) AS usage_rank,
        s.column_name,
        COALESCE(u.queries, 0) AS queries,
        s.ordinal_position,
        s.common_values,
        s.data_type,
        s.is_cluster_key,
        s.character_maximum_length,
        s.comment
    FROM setup s
    LEFT JOIN usage u 
        ON s.fully_qualified_table_name = u.fully_qualified_table_name
        AND s.column_name = u.column_name
    ORDER BY 
        queries DESC,
        ordinal_position ASC
    """
    if verbose:
        print(f"      🔍 SQL: {query}")
    df = sf.query_snowflake(query, method="pandas")
    return df.to_dict("records")


def fetch_columns_metadata(sf, database: str, schema: str, table: str) -> List[Dict[str, Any]]:
    """Return column-level metadata with data types and comments (legacy version)."""
    query = f"""
    SELECT 
        TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, ORDINAL_POSITION,
        CHARACTER_MAXIMUM_LENGTH, COMMENT
    FROM tyleranderson.sf_columns
    WHERE lower(TABLE_CATALOG)=lower('{database}')
      AND lower(TABLE_SCHEMA)=lower('{schema}')
      AND lower(TABLE_NAME)=lower('{table}')
    ORDER BY ORDINAL_POSITION
    """
    df = sf.query_snowflake(query, method="pandas")
    return df.to_dict("records")


def fetch_most_common_joins(sf, full_table_name: str, limit: int = 10, verbose: bool = False) -> List[Dict[str, Any]]:
    """
    Find most commonly joined tables using the enhanced join query from requirements.
    """
    query = f"""
    SELECT
        a.fully_qualified_table_name AS base_table,
        b.fully_qualified_table_name AS joined_table,
        COUNT(DISTINCT a.query_id) AS query_count
    FROM tyleranderson.sf_table_usage a
    CROSS JOIN tyleranderson.sf_table_usage b
    WHERE a.query_id = b.query_id
        AND a.fully_qualified_table_name = '{full_table_name}'
        AND a.fully_qualified_table_name <> b.fully_qualified_table_name
        AND a.start_time >= CURRENT_DATE - 365
        AND b.start_time >= CURRENT_DATE - 365
    GROUP BY a.fully_qualified_table_name, b.fully_qualified_table_name
    ORDER BY query_count DESC
    LIMIT {limit}
    """
    
    if verbose:
        print(f"      🔍 SQL: {query}")
    
    try:
        df = sf.query_snowflake(query, method="pandas")
        return df.to_dict("records") if not df.empty else []
    except Exception:
        return []


def fetch_sample_queries_from_most_used_user(sf, full_table_name: str, limit: int = 2, verbose: bool = False) -> List[Dict[str, Any]]:
    """
    Get sample queries from the most used user for the table.
    Implements the sample query requirements.
    """
    query = f"""
    WITH most_used_user AS (
        -- Find the user with the most queries for the given table
        SELECT dd_user
        FROM tyleranderson.sf_table_usage
        WHERE fully_qualified_table_name = '{full_table_name}'
        GROUP BY dd_user
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ),
    recent_distinct_queries AS (
        -- Get distinct queries by the most used user, ordered by most recent
        SELECT DISTINCT
            query_text,
            MAX(start_time) AS latest_execution_time
        FROM tyleranderson.sf_table_usage
        WHERE fully_qualified_table_name = '{full_table_name}'
          AND dd_user = (SELECT dd_user FROM most_used_user)
        GROUP BY query_text
        ORDER BY latest_execution_time DESC
        LIMIT {limit}
    )
    SELECT
        query_text,
        latest_execution_time
    FROM recent_distinct_queries
    ORDER BY latest_execution_time DESC
    """
    
    if verbose:
        print(f"      🔍 SQL: {query}")
    
    try:
        df = sf.query_snowflake(query, method="pandas")
        return df.to_dict("records") if not df.empty else []
    except Exception:
        return []


def fetch_top_sample_queries(sf, database: str, schema: str, table: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Use sf_table_usage / sf_column_usage (or a derived view) to retrieve top queries referencing the table."""
    # We'll try progressively broader queries to handle schema differences
    patterns = [
        f"{database}.{schema}.{table}",
        f"{database}.{schema}.\"{table}\"",
        f"{database}.{schema}.{table.lower()}",
    ]

    # Attempt 1: richer columns (may fail if columns differ)
    query1 = f"""
    SELECT QID AS query_id, START_TIME AS start_time, PURPOSE AS query_type, QUERY_TEXT AS query_text
    FROM tyleranderson.sf_table_usage
    WHERE {" OR ".join([f"CONTAINS(UPPER(QUERY_TEXT), UPPER('{p}'))" for p in patterns])}
    ORDER BY start_time DESC NULLS LAST
    LIMIT {limit}
    """

    # Attempt 2: minimal subset if Attempt 1 fails
    query2 = f"""
    SELECT QUERY_TEXT AS query_text
    FROM tyleranderson.sf_table_usage
    WHERE {" OR ".join([f"CONTAINS(UPPER(QUERY_TEXT), UPPER('{p}'))" for p in patterns])}
    LIMIT {limit}
    """

    for q in (query1, query2):
        try:
            df = sf.query_snowflake(q, method="pandas")
            if not df.empty:
                return df.to_dict("records")
        except Exception:
            continue
    return []


def find_tables_by_name(sf, table_name: str, database: Optional[str] = None, schema: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return potential matches for a bare table name across catalogs/schemas with simple ranking fields.
    Optionally filter by database and/or schema if provided.
    """
    filters = [f"lower(TABLE_NAME) = lower('{table_name}')"]
    if database:
        filters.append(f"lower(TABLE_CATALOG) = lower('{database}')")
    if schema:
        filters.append(f"lower(TABLE_SCHEMA) = lower('{schema}')")
    where_clause = " AND ".join(filters)
    query = f"""
    SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, ROW_COUNT, CREATED
    FROM tyleranderson.sf_tables_full
    WHERE {where_clause}
    ORDER BY ROW_COUNT DESC NULLS LAST, CREATED DESC NULLS LAST
    LIMIT 50
    """
    df = sf.query_snowflake(query, method="pandas")
    return df.to_dict("records") if not df.empty else []


def find_best_fqn_via_usage(sf, table_name: str) -> Optional[Tuple[str, str]]:
    """Fallback: pick the most-referenced database/schema for a table name using sf_table_usage.
    Returns (database, schema) or None if not found.
    """
    query = f"""
    SELECT table_name, table_database, table_schema, COUNT(1) AS cnt
    FROM tyleranderson.sf_table_usage
    WHERE lower(table_name) = lower('{table_name}')
    GROUP BY ALL
    ORDER BY cnt DESC
    LIMIT 1
    """
    try:
        df = sf.query_snowflake(query, method="pandas")
        if df.empty:
            return None
        row = df.iloc[0]
        return str(row["table_database"]), str(row["table_schema"])
    except Exception:
        return None

