from typing import Any, Dict, List, Optional
import json


def _count_duplicates(sf, fqn: str, key: str, time_column: str = None, lookback_days: int = 7) -> int:
    time_filter = ""
    if time_column:
        time_filter = f"AND {time_column} >= CURRENT_DATE - {lookback_days}"
    
    query = f"""
    SELECT COUNT(1) AS dup_cnt
    FROM (
      SELECT {key}, COUNT(1) AS cnt
      FROM {fqn}
      WHERE {key} IS NOT NULL {time_filter}
      GROUP BY {key}
      HAVING COUNT(1) > 1
    )
    """
    print('Counting duplicates....')
    print(query)
    df = sf.query_snowflake(query, method="pandas")
    return int(df.iloc[0]["dup_cnt"]) if not df.empty else 0


def _fetch_example_values(sf, fqn: str, key: str, limit: int = 3, time_column: str = None, lookback_days: int = 7) -> List[str]:
    time_filter = ""
    if time_column:
        time_filter = f"AND {time_column} >= CURRENT_DATE - {lookback_days}"
    
    query = f"""
    SELECT DISTINCT {key}
    FROM {fqn}
    WHERE {key} IS NOT NULL {time_filter}
    LIMIT {limit}
    """
    df = sf.query_snowflake(query, method="pandas")
    if df.empty:
        return []
    # Column names are lowercased by SnowflakeHook; be resilient
    try:
        series = df.iloc[:, 0]
    except Exception:
        series = None
    if series is None:
        return []
    return [str(v) for v in series.tolist()]


def _deep_dive_duplicates(sf, fqn: str, key: str, example_value: str, sample_row_limit: int = 10, time_column: str = None, lookback_days: int = 7) -> Dict[str, Any]:
    time_filter = ""
    if time_column:
        time_filter = f"AND {time_column} >= CURRENT_DATE - {lookback_days}"
    
    query = f"""
    SELECT *
    FROM {fqn}
    WHERE {key} = '{example_value}' {time_filter}
    LIMIT {sample_row_limit}
    """
    df = sf.query_snowflake(query, method="pandas")
    return {
        "key": key,
        "value": example_value,
        "row_count": len(df),
        "sample": df.head(min(3, len(df))).to_dict("records") if not df.empty else [],
    }


def _predict_granularity_columns(llm, table_name: str, schema_name: str, columns_meta: List[Dict[str, Any]], business_context: str = "", confluence_context: str = "", table_row_count: int = None) -> tuple[str, str, int]:
    """Use LLM to predict entity and time columns, with logic-based lookback window.
    
    Args:
        llm: Language model for column prediction
        table_name: Name of the table
        schema_name: Schema name
        columns_meta: List of column metadata
        business_context: Business context for better predictions
        confluence_context: Additional context from Confluence
        table_row_count: Number of rows in table (used for lookback logic)
    
    Returns:
        tuple: (entity_column, time_column, lookback_days)
        
    Lookback logic:
        - >100M rows: 1 day (massive tables)
        - 10M-100M rows: 3 days (large tables)  
        - 1M-10M rows: 7 days (medium tables)
        - <1M rows: 30 days (smaller tables)
        - None/unknown: 7 days (default)
    """
    
    # Determine lookback days based on table size using logic
    def get_lookback_days(row_count: int = None) -> int:
        """Determine lookback days based on table row count."""
        if row_count is None:
            return 7  # Default fallback
        
        if row_count > 100_000_000:  # >100M rows: massive tables
            return 1
        elif row_count > 10_000_000:  # 10M-100M rows: large tables
            return 3
        elif row_count > 1_000_000:   # 1M-10M rows: medium tables
            return 7
        else:                         # <1M rows: smaller tables
            return 30
    
    # Calculate lookback days using logic
    lookback_days = get_lookback_days(table_row_count)
    
    # Prepare context for LLM (only for entity and time column prediction)
    table_context = {
        "table_name": table_name,
        "schema_name": schema_name,
        "business_context": business_context,
        "confluence_context": confluence_context,
        "table_row_count": table_row_count,
        "columns": [
            {
                "name": col.get("column_name", ""),
                "type": col.get("data_type", ""),
                "comment": col.get("comment", "")
            }
            for col in columns_meta
        ]
    }
    
    system_prompt = """You are a data scientist expert. Given table metadata, business context, and Confluence documentation, identify the SINGLE most relevant entity column and time column.

Rules:
1. Return a JSON object with two keys: "entity_column", "time_column"
2. entity_column: The ONE most important ID column that represents what each row is about (e.g., user_id, order_id, delivery_id). Prefer the IDs that might be the primary key, where it is granular on that ID.
3. time_column: A single column name for filtering recent data (timestamps, dates, created_at, etc.)
4. Use ALL available context: table name, business context, Confluence docs, column comments
5. Choose the entity column that makes the most business sense given the table's purpose
6. Prefer columns that represent the primary business entity this table tracks
7. If table tracks events/transactions, choose the entity being acted upon (not the transaction ID)

Example response: {"entity_column": "user_id", "time_column": "created_at"}"""
    
    user_prompt = f"Analyze this table and predict granularity columns:\n\n{json.dumps(table_context, indent=2)}"

    try:
        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ])
        
        # Parse JSON response
        result = json.loads(response.strip())
        
        # Extract entity column and time column
        entity_column = result.get("entity_column", None)
        time_column = result.get("time_column", None)
        
        # Filter to only columns that actually exist
        existing_columns = {col.get("column_name", "").upper() for col in columns_meta}
        
        valid_entity_column = None
        if entity_column and isinstance(entity_column, str) and entity_column.upper() in existing_columns:
            valid_entity_column = entity_column
        
        valid_time_column = None
        if time_column and isinstance(time_column, str) and time_column.upper() in existing_columns:
            valid_time_column = time_column
        
        return valid_entity_column, valid_time_column, lookback_days
        
    except Exception:
        pass
    
    # Fallback to heuristic approach
    granularity_cols, time_col = _heuristic_granularity_guess(columns_meta)
    
    # Use the same logic-based lookback days for fallback
    return granularity_cols, time_col, lookback_days


def _heuristic_granularity_guess(columns_meta: List[Dict[str, Any]]) -> tuple[str, str]:
    """Fallback heuristic granularity guessing - returns single best entity column."""
    best_candidate = None
    time_candidate = None
    
    # Priority order for entity columns
    priority_patterns = [
        "user_id", "consumer_id", "customer_id",  # User-centric
        "order_id", "delivery_id", "merchant_id",  # Business entities
        "id"  # Generic fallback
    ]
    
    for col in columns_meta:
        name = str(col.get("column_name", "")).lower()
        col_name = col.get("column_name", "")
        
        # Look for entity column with priority
        if not best_candidate:
            for pattern in priority_patterns:
                if name == pattern or name.endswith("_" + pattern):
                    best_candidate = col_name
                    break
            # Fallback to any ID column
            if not best_candidate and (name.endswith("_id") or name == "id"):
                best_candidate = col_name
        
        # Look for time columns
        if not time_candidate and any(time_word in name for time_word in 
                                    ["created", "updated", "timestamp", "time", "date"]):
            time_candidate = col_name
    
    return best_candidate, time_candidate


def _get_sample_duplicate(sf, fqn: str, key: str, time_column: str = None, lookback_days: int = 7) -> Optional[str]:
    """Get one example value that has duplicates."""
    time_filter = ""
    if time_column:
        time_filter = f"AND {time_column} >= CURRENT_DATE - {lookback_days}"
    
    query = f"""
    SELECT {key}
    FROM {fqn}
    WHERE {key} IS NOT NULL {time_filter}
    GROUP BY {key}
    HAVING COUNT(1) > 1
    LIMIT 1
    """
    df = sf.query_snowflake(query, method="pandas")
    if not df.empty:
        return str(df.iloc[0, 0])
    return None


def _analyze_sample_data_with_llm(llm, fqn: str, key: str, sample_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Send sample data to LLM for pattern analysis."""
    
    # Limit sample data size to avoid LLM token limits
    limited_sample = sample_data[:5] if len(sample_data) > 5 else sample_data
    
    # Simplify data for LLM - only include key columns
    simplified_sample = []
    for row in limited_sample:
        # Keep only important columns (limit to 10 most relevant)
        important_cols = {}
        col_count = 0
        for col_name, value in row.items():
            if col_count >= 10:
                break
            # Prioritize certain column types
            col_lower = str(col_name).lower()
            if any(pattern in col_lower for pattern in ['id', 'date', 'time', 'status', 'flag', 'current', 'start', 'end']):
                important_cols[col_name] = str(value)[:100] if value else None  # Truncate long values
                col_count += 1
        
        # Add remaining columns up to limit
        for col_name, value in row.items():
            if col_count >= 10:
                break
            if col_name not in important_cols:
                important_cols[col_name] = str(value)[:100] if value else None
                col_count += 1
                
        simplified_sample.append(important_cols)
    
    context = {
        "table": fqn,
        "granularity_column": key,
        "sample_rows": simplified_sample,
        "row_count": len(sample_data),
        "note": "Sample data truncated for analysis"
    }
    
    system_prompt = """You are a data analyst. Analyze sample rows for a specific value to understand why this table has multiple rows per entity.

Your task:
1. Determine if there's a finer granularity (additional columns that make each row unique)
2. OR explain the pattern (e.g., SCD table, event log, state changes, data issues, etc)

Look for patterns like:
- SCD (Slowly Changing Dimension) tables with start/end dates
- Event logs with timestamps
- Status change tracking
- Versioning or audit trails
- Data issues where there are duplicate rowseven when it should be granular
- Or other scenarios

Respond with JSON:
{
  "has_finer_granularity": true/false,
  "new_granularity_candidates": ["col1", "col2"] or [],
  "pattern_explanation": "explanation of why multiple rows exist",
  "example_description": "brief description of what these specific rows show"
}"""
    
    user_prompt = f"Analyze these sample rows:\n\n{json.dumps(context, indent=2, default=str)}"
    
    try:
        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ])
        
        return json.loads(response.strip())
    except Exception as e:
        # Provide intelligent fallback based on column patterns
        changing_cols = []
        if len(sample_data) >= 2:
            row1, row2 = sample_data[0], sample_data[1]
            for col_name in row1.keys():
                if row1.get(col_name) != row2.get(col_name):
                    changing_cols.append(col_name)
        
        # Detect various patterns based on changing columns
        pattern_analysis = _detect_pattern_from_columns(changing_cols, sample_data, key)
        
        return {
            "has_finer_granularity": False,
            "new_granularity_candidates": [],
            "pattern_explanation": pattern_analysis["explanation"],
            "example_description": pattern_analysis["description"]
        }


def _detect_pattern_from_columns(changing_cols: List[str], sample_data: List[Dict[str, Any]], key: str) -> Dict[str, str]:
    """Analyze changing columns to detect common data patterns."""
    
    if not changing_cols:
        return {
            "explanation": f"Multiple identical rows found for {key} - possible data quality issue or true duplicates",
            "description": f"All {len(sample_data)} rows appear identical, suggesting potential data duplication"
        }
    
    changing_lower = [str(col).lower() for col in changing_cols]
    
    # Pattern 1: SCD (Slowly Changing Dimension) patterns
    scd_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['scd', 'start', 'end', 'current', 'effective', 'valid', 'active']
    )]
    
    if scd_indicators:
        return {
            "explanation": f"SCD (Slowly Changing Dimension) table tracking historical changes over time. Key changing fields: {', '.join(changing_cols[:5])}",
            "description": f"Shows {len(sample_data)} historical states for {key}, tracking changes in dimension attributes"
        }
    
    # Pattern 2: Event/Log patterns
    event_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['timestamp', 'created', 'updated', 'event', 'log', 'time', 'date']
    )]
    
    if event_indicators:
        return {
            "explanation": f"Event log or time-series data capturing multiple events/transactions per {key}. Time-based fields: {', '.join([col for col in changing_cols if str(col).lower() in event_indicators][:3])}",
            "description": f"Shows {len(sample_data)} events/records for {key}, likely representing different actions or state changes over time"
        }
    
    # Pattern 3: Status/State tracking
    status_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['status', 'state', 'phase', 'stage', 'flag', 'enabled', 'active']
    )]
    
    if status_indicators:
        return {
            "explanation": f"Status or state tracking table recording different states/conditions for {key}. Status fields: {', '.join([col for col in changing_cols if str(col).lower() in status_indicators][:3])}",
            "description": f"Shows {len(sample_data)} different status states for {key}, tracking changes in conditions or flags"
        }
    
    # Pattern 4: Versioning patterns
    version_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['version', 'revision', 'sequence', 'iteration', 'generation']
    )]
    
    if version_indicators:
        return {
            "explanation": f"Versioned data tracking multiple versions/revisions per {key}. Version fields: {', '.join([col for col in changing_cols if str(col).lower() in version_indicators][:3])}",
            "description": f"Shows {len(sample_data)} versions for {key}, likely representing different iterations or updates"
        }
    
    # Pattern 5: Relationship/Association patterns
    relationship_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['_id', 'reference', 'link', 'association', 'mapping', 'related']
    )]
    
    if len([col for col in changing_lower if col.endswith('_id')]) >= 2:
        return {
            "explanation": f"Relationship or mapping table connecting {key} to multiple other entities. Relationship fields: {', '.join([col for col in changing_cols if str(col).lower().endswith('_id')][:3])}",
            "description": f"Shows {len(sample_data)} relationships for {key}, representing associations with different entities"
        }
    
    # Pattern 6: Partitioned/Segmented data
    partition_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['partition', 'segment', 'bucket', 'shard', 'region', 'location', 'type']
    )]
    
    if partition_indicators:
        return {
            "explanation": f"Partitioned or segmented data with multiple records per {key} across different partitions/segments. Partitioning fields: {', '.join([col for col in changing_cols if str(col).lower() in partition_indicators][:3])}",
            "description": f"Shows {len(sample_data)} segments for {key}, likely partitioned by geography, type, or other business dimensions"
        }
    
    # Pattern 7: Aggregation/Metrics at different levels
    metric_indicators = [col for col in changing_lower if any(
        pattern in col for pattern in ['count', 'sum', 'avg', 'total', 'amount', 'value', 'metric', 'measure']
    )]
    
    if metric_indicators:
        return {
            "explanation": f"Aggregated metrics or measurements table with multiple metric records per {key}. Metric fields: {', '.join([col for col in changing_cols if str(col).lower() in metric_indicators][:3])}",
            "description": f"Shows {len(sample_data)} metric records for {key}, representing different measurements or calculated values"
        }
    
    # Default: Generic pattern
    return {
        "explanation": f"Multiple records per {key} with varying attributes. Key changing fields: {', '.join(changing_cols[:5])}. Pattern unclear - could be legitimate business logic, data quality issue, or complex relationship",
        "description": f"Shows {len(sample_data)} distinct records for {key}. Manual investigation recommended to understand the business logic behind multiple rows"
    }


def _find_actual_granularity_column(sf, fqn: str, columns_meta: List[Dict[str, Any]], time_column: str = None, lookback_days: int = 7) -> Optional[str]:
    """Find the actual unique granularity column (even if it's meaningless)."""
    # Test all columns for uniqueness
    for col in columns_meta:
        col_name = col.get("column_name") or col.get("COLUMN_NAME")
        if not col_name:
            continue
            
        try:
            dup_count = _count_duplicates(sf, fqn, col_name, time_column, lookback_days)
            if dup_count == 0:
                return col_name
        except Exception:
            continue
    return None


def _generate_business_explanation(llm, table_name: str, entity_column: str, sample_value: str, 
                                 sample_data: List[Dict[str, Any]], changing_cols: List[str]) -> str:
    """Generate business-friendly explanation for why entity has multiple rows."""
    
    # Analyze timeline if date columns exist
    timeline_info = _extract_timeline_info(sample_data, changing_cols)
    
    context = {
        "table_name": table_name,
        "entity_column": entity_column,
        "entity_value": sample_value,
        "num_rows": len(sample_data),
        "changing_columns": changing_cols[:5],  # Limit for LLM
        "timeline": timeline_info,
        "sample_rows_simplified": [
            {k: str(v)[:50] if v else None for k, v in row.items() if k in changing_cols[:8]}
            for row in sample_data[:3]
        ]
    }
    
    system_prompt = """You are a business analyst explaining data patterns to non-technical stakeholders.

Your task: Explain in plain English why this entity has multiple rows in the table.

Guidelines:
1. Use business language, not technical jargon
2. Focus on the "why" from a business perspective  
3. If it's settings/preferences, say they "changed their settings X times"
4. If it's events/transactions, say they "had X transactions/events"
5. If it's status changes, say they "went through X status changes"
6. Be specific about what changed when possible
7. Keep it concise and clear

Respond with just the explanation sentence, no JSON or extra text."""
    
    user_prompt = f"Explain why this entity has multiple rows:\n\n{json.dumps(context, indent=2, default=str)}"
    
    try:
        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ])
        return response.strip().replace('"', '').replace("'", "")
    except Exception:
        # Fallback to pattern-based explanation
        if any('setting' in str(col).lower() or 'status' in str(col).lower() for col in changing_cols):
            return f"{entity_column.title().replace('_', ' ')} {sample_value} has {len(sample_data)} rows because they changed their settings/preferences {len(sample_data)} times"
        elif any('date' in str(col).lower() or 'time' in str(col).lower() for col in changing_cols):
            return f"{entity_column.title().replace('_', ' ')} {sample_value} has {len(sample_data)} rows representing different time periods or events"
        else:
            return f"{entity_column.title().replace('_', ' ')} {sample_value} has {len(sample_data)} rows due to changes in: {', '.join(changing_cols[:3])}"


def _extract_timeline_info(sample_data: List[Dict[str, Any]], changing_cols: List[str]) -> Dict[str, Any]:
    """Extract timeline information from sample data."""
    date_cols = [col for col in changing_cols if any(
        pattern in str(col).lower() for pattern in ['date', 'time', 'created', 'updated', 'start', 'end']
    )]
    
    if not date_cols or len(sample_data) < 2:
        return {}
    
    timeline = {}
    for date_col in date_cols[:2]:  # Limit to avoid complexity
        try:
            values = [row.get(date_col) for row in sample_data if row.get(date_col)]
            if values:
                timeline[date_col] = {
                    "earliest": min(values),
                    "latest": max(values),
                    "count": len(set(values))
                }
        except Exception:
            continue
    
    return timeline


def enhanced_granularity_analysis(sf, fqn: str, table_name: str, schema_name: str, 
                                columns_meta: List[Dict[str, Any]], llm,
                                sample_row_limit: int = 10, business_context: str = "", 
                                max_iterations: int = 3, verbose: bool = False, table_row_count: int = None) -> Dict[str, Any]:
    """
    Enhanced granularity detection with entity vs granularity separation.
    
    Performance optimization: Skips deep dive analysis for very large tables (>10B rows) 
    to avoid long-running queries and potential timeouts. For large tables, returns 
    lightweight analysis with LLM predictions only.
    
    Args:
        sf: Snowflake connection
        fqn: Fully qualified table name
        table_name: Table name
        schema_name: Schema name  
        columns_meta: List of column metadata
        llm: Language model instance
        sample_row_limit: Number of sample rows for analysis
        business_context: Business context for better predictions
        max_iterations: Maximum iterations for analysis
        verbose: Enable verbose logging
        table_row_count: Number of rows in table (used for skip logic)
    
    Returns:
        Dict containing granularity analysis results. For tables >10B rows,
        returns 'large_table_skipped' type with LLM predictions only.
    """
    if verbose:
        print(f"🔍 Starting enhanced granularity analysis for {fqn}")
        print(f"   📊 Table has {len(columns_meta)} columns")
        if business_context:
            print(f"   📝 Using business context: {business_context[:100]}...")
        if table_row_count:
            print(f"   📈 Table row count: {table_row_count:,}")
    
    # Check if table is too large for deep dive analysis
    skip_deep_dive = False
    if table_row_count and table_row_count > 10_000_000_000:  # >10B rows
        skip_deep_dive = True
        if verbose:
            print(f"   ⚠️  Table too large ({table_row_count:,} rows > 10B), skipping deep dive analysis")
    
    # Step 1: LLM predicts the single most relevant entity column and time column for filtering
    if verbose:
        print("   🤖 Step 1: Using LLM to predict the most relevant entity column and time column...")
    
    # Build confluence context for LLM
    confluence_context = ""
    if business_context and "Confluence" in business_context:
        confluence_context = business_context
    
    entity_column, time_column, lookback_days = _predict_granularity_columns(llm, table_name, schema_name, columns_meta, business_context, confluence_context, table_row_count)
    
    if verbose:
        if entity_column:
            print(f"   ✅ LLM selected entity column: {entity_column}")
        else:
            print("   ⚠️ No entity column identified by LLM")
        if time_column:
            print(f"   ⏰ Time column for filtering: {time_column}")
            print(f"   📅 Adaptive lookback window: {lookback_days} days")
        else:
            print("   ⚠️ No time column identified - using full table")
    
    # Return early for very large tables to avoid performance issues
    if skip_deep_dive:
        if verbose:
            print("   🚀 Returning lightweight analysis due to table size")
        return {
            "granularity_type": "large_table_skipped",
            "entity_column": entity_column,
            "time_column": time_column,
            "lookback_days": lookback_days,
            "summary": f"Large table ({table_row_count:,} rows) - analysis optimized for performance. Predicted entity level: {entity_column or 'unknown'}, time filtering: {time_column or 'none'}",
            "explanation": f"**Performance-Optimized Analysis**\n\nThis is a very large table with {table_row_count:,} rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **{entity_column or 'unknown'}** level.\n\n**Key Insights:**\n- **Entity Level**: Each row likely represents a {entity_column.lower().replace('_', ' ') if entity_column else 'unknown entity'}\n- **Time Filtering**: {'Uses ' + time_column + ' for time-based analysis' if time_column else 'No time column identified for filtering'}\n- **Recommended Lookback**: {lookback_days} days for analysis (automatically determined based on table size)\n\nFor detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.",
            "analysis_log": [f"Table too large ({table_row_count:,} rows) - skipped deep dive analysis"]
        }
    
    # Step 2: Find actual technical granularity (what makes rows unique)
    if verbose:
        print("   🔎 Step 2: Finding actual technical granularity...")
    
    actual_granularity_column = _find_actual_granularity_column(sf, fqn, columns_meta, time_column, lookback_days)
    
    if verbose:
        print(f"   ✅ Technical granularity column: {actual_granularity_column}")
    
    analysis_log = []
    
    # Step 3: Analyze the predicted entity column
    if not entity_column:
        if verbose:
            print("   ❌ No entity columns predicted by LLM")
        return {
            "granularity_type": "unknown",
            "summary": "Unable to determine entity level or granularity",
            "analysis_log": ["No entity columns predicted by LLM"],
            "actual_granularity_column": actual_granularity_column
        }
    
    try:
        # Test entity column for duplicates (with time filtering if available)
        if verbose:
            print(f"   🔍 Step 3: Testing entity column '{entity_column}' for duplicates...")
            if time_column:
                print(f"   ⏰ Applying time filter: {time_column} >= CURRENT_DATE - {lookback_days}")
        
        dup_count = _count_duplicates(sf, fqn, entity_column, time_column, lookback_days)
        analysis_log.append(f"Testing entity column: {entity_column}")
        if time_column:
            analysis_log.append(f"Time filtering: {time_column} >= CURRENT_DATE - {lookback_days}")
        
        if verbose:
            print(f"   📊 Found {dup_count} duplicate values for {entity_column}")
        
        if dup_count == 0:
            # Entity column is unique - this is the granularity
            if verbose:
                print(f"   ✅ {entity_column} is unique - found granularity!")
            return {
                "granularity_type": "unique_entity",
                "entity_column": entity_column,
                "technical_granularity_column": entity_column,
                "summary": f"Table is granular at {entity_column} level - each row represents a unique {entity_column.lower().replace('_', ' ')}",
                "analysis_log": analysis_log
            }
        
        # Entity has duplicates - analyze pattern
        if verbose:
            print(f"   🔍 Step 4: {entity_column} has duplicates, analyzing pattern...")
        
        sample_value = _get_sample_duplicate(sf, fqn, entity_column, time_column, lookback_days)
        if not sample_value:
            if verbose:
                print("   ❌ No sample duplicate found")
            analysis_log.append("No sample duplicate found")
            return {
                "granularity_type": "unknown",
                "summary": "Unable to analyze pattern - no sample data",
                "analysis_log": analysis_log
            }
        
        # Get sample rows for this entity (with time filtering if available)
        time_filter = ""
        if time_column:
            time_filter = f"AND {time_column} >= CURRENT_DATE - {lookback_days}"
        
        sample_query = f"""
        SELECT *
        FROM {fqn}
        WHERE {entity_column} = '{sample_value}' {time_filter}
        LIMIT {sample_row_limit}
        """
        if verbose:
            print(f"   📝 Sampling rows for {entity_column} = '{sample_value}'...")
        
        sample_df = sf.query_snowflake(sample_query, method="pandas")
        
        if sample_df.empty:
            if verbose:
                print("   ❌ Sample query returned no data")
            analysis_log.append("Sample query returned no data")
            return {
                "granularity_type": "unknown",
                "summary": "Unable to analyze pattern - no sample data",
                "analysis_log": analysis_log
            }
        
        sample_data = sample_df.to_dict('records')
        
        # Identify changing columns
        if verbose:
            print(f"   📊 Found {len(sample_data)} sample rows, analyzing changing columns...")
        
        changing_cols = []
        if len(sample_data) >= 2:
            row1, row2 = sample_data[0], sample_data[1]
            for col_name in row1.keys():
                if row1.get(col_name) != row2.get(col_name):
                    changing_cols.append(col_name)
        
        if verbose:
            print(f"   🔄 Changing columns: {changing_cols}")
        
        # Generate business explanation
        if verbose:
            print("   🤖 Generating business explanation via LLM...")
        business_explanation = _generate_business_explanation(
            llm, table_name, entity_column, sample_value, sample_data, changing_cols
        )
        
        # Detect pattern for technical context
        if verbose:
            print("   🔍 Detecting technical patterns...")
        pattern_analysis = _detect_pattern_from_columns(changing_cols, sample_data, entity_column)
        
        if verbose:
            print("   ✅ Enhanced granularity analysis completed successfully")
        
        return {
            "granularity_type": "entity_with_history",
            "entity_column": entity_column,
            "technical_granularity_column": actual_granularity_column,
            "business_explanation": business_explanation,
            "technical_pattern": pattern_analysis["explanation"],
            "example_entity_value": sample_value,
            "sample_data": sample_data,
            "changing_columns": changing_cols,
            "duplicate_count": dup_count,
            "timeline_info": _extract_timeline_info(sample_data, changing_cols),
            "analysis_log": analysis_log
        }
        
    except Exception as e:
        error_msg = f"Error analyzing {entity_column}: {str(e)}"
        if verbose:
            print(f"   ❌ Enhanced analysis failed: {str(e)}")
        analysis_log.append(error_msg)
        return {
            "granularity_type": "error",
            "summary": f"Error during analysis: {str(e)}",
            "analysis_log": analysis_log,
            "actual_granularity_column": actual_granularity_column
        }


def infer_granularity(sf, fqn: str, candidate_keys: List[str], sample_row_limit: int = 10, verbose: bool = False, time_column: str = None, lookback_days: int = 7) -> Dict[str, Any]:
    """
    Legacy function for backward compatibility. 
    Try candidate keys to determine granularity. If duplicates exist for a key, deep dive one value
    to understand why (e.g., multiple rows per id due to status history or partitioning). Returns
    a structured dict summarizing findings.
    """
    if verbose:
        print("   ⚠️ Enhanced granularity analysis failed, falling back to legacy infer_granularity")
        print(f"   🔍 Testing {len(candidate_keys)} candidate keys: {candidate_keys}")
        if time_column:
            print(f"   ⏰ Using time filtering: {time_column} >= CURRENT_DATE - {lookback_days}")
    
    findings: List[Dict[str, Any]] = []
    determined_key: Optional[str] = None
    for key in candidate_keys:
        try:
            if verbose:
                print(f"   🔍 Testing candidate key: {key}")
            dup_cnt = _count_duplicates(sf, fqn, key, time_column, lookback_days)
            if verbose:
                print(f"   📊 Found {dup_cnt} duplicates for {key}")
        except Exception as e:
            if verbose:
                print(f"   ❌ Error testing {key}: {str(e)}")
            continue

        if dup_cnt == 0:
            determined_key = key
            if verbose:
                print(f"   ✅ Found unique key: {key}")
            findings.append({
                "candidate_key": key,
                "duplicates": 0,
                "granularity": f"Appears unique on {key}",
            })
            break
        else:
            # Deep dive one example duplicated value
            if verbose:
                print(f"   🔍 Key {key} has duplicates, analyzing sample...")
            examples = _fetch_example_values(sf, fqn, key, limit=1, time_column=time_column, lookback_days=lookback_days)
            dive: Optional[Dict[str, Any]] = None
            if examples:
                dive = _deep_dive_duplicates(sf, fqn, key, examples[0], sample_row_limit, time_column, lookback_days)
                if verbose:
                    print(f"   📝 Analyzed sample value '{examples[0]}' for {key}")
            findings.append({
                "candidate_key": key,
                "duplicates": dup_cnt,
                "example": dive,
            })

    summary: str
    if determined_key:
        summary = f"Granularity likely at {determined_key}."
        if verbose:
            print(f"   ✅ Legacy analysis completed: {summary}")
    elif findings:
        summary = (
            "No strictly unique key found among candidates; table may be higher-granularity or store multiple "
            "rows per entity (e.g., state changes, partitions). See examples."
        )
        if verbose:
            print(f"   ⚠️ Legacy analysis completed: {summary}")
    else:
        summary = "Unable to infer granularity (no viable keys tested)."
        if verbose:
            print(f"   ❌ Legacy analysis failed: {summary}")

    return {
        "tested_keys": candidate_keys,
        "determined_key": determined_key,
        "summary": summary,
        "details": findings,
    }

