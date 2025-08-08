from pathlib import Path
from typing import Any, Dict, List, Optional


def _round_up_most_significant(n: Optional[int]) -> Optional[str]:
    if n is None:
        return None
    try:
        n_int = int(n)
    except Exception:
        return None
    if n_int <= 0:
        return "0"
    s = str(n_int)
    # Keep first digit, zero the rest
    return s[0] + ("0" * (len(s) - 1))


def build_markdown_content(
    table_fqn: str,
    overview: Dict[str, Any],
    columns_meta: List[Dict[str, Any]],
    granularity: Dict[str, Any],
    top_queries: List[Dict[str, Any]],
    confluence_hits: Optional[List[Dict[str, Any]]],
    narrative: Dict[str, str],
) -> str:
    row_count = overview.get("ROW_COUNT") or overview.get("row_count")
    approx_rows = _round_up_most_significant(row_count)

    general_desc = "TBD"
    business_ctx = "TBD"
    who_maintains = overview.get("TABLE_OWNER") or overview.get("table_owner") or "TBD"
    if narrative and narrative.get("narrative"):
        # Simple parse: sections are inline; don't overfit structure
        text = narrative["narrative"].strip()
        general_desc = text
        business_ctx = "See above"

    confluence_link = None
    if confluence_hits:
        # Pick the first result as the canonical link
        confluence_link = confluence_hits[0].get("url")

    # Columns table
    col_lines = ["| Column | Type | Description |", "|---|---|---|"]
    for col in columns_meta:
        name = col.get("COLUMN_NAME") or col.get("column_name")
        dtype = col.get("DATA_TYPE") or col.get("data_type")
        comment = col.get("COMMENT") or col.get("comment") or ""
        col_lines.append(f"| `{name}` | {dtype} | {comment} |")

    # Top queries (compact)
    query_lines: List[str] = []
    for q in top_queries[:5]:
        qid = q.get("QUERY_ID") or q.get("query_id")
        who = q.get("USER_NAME") or q.get("user_name")
        ts = q.get("START_TIME") or q.get("start_time")
        query_lines.append(f"- {qid} by {who} at {ts}")

    # Enhanced Granularity rendering v2 - Entity vs Granularity separation
    gran_lines = []
    granularity_type = granularity.get("granularity_type")
    
    if granularity_type == "unique_entity":
        # Simple case: entity column is unique
        entity_col = granularity.get("entity_column")
        gran_lines.append(f"- **Entity Level**: `{entity_col}` (each row represents a unique {entity_col.lower().replace('_', ' ')})")
        gran_lines.append(f"- **Granularity**: One-to-one mapping - table is granular at the {entity_col.lower().replace('_', ' ')} level")
        
    elif granularity_type == "entity_with_history":
        # Complex case: entity has multiple rows
        entity_col = granularity.get("entity_column")
        tech_granularity = granularity.get("technical_granularity_column")
        business_explanation = granularity.get("business_explanation", "Multiple rows per entity")
        example_value = granularity.get("example_entity_value")
        dup_count = granularity.get("duplicate_count")
        changing_cols = granularity.get("changing_columns", [])
        timeline_info = granularity.get("timeline_info", {})
        
        # Entity level
        gran_lines.append(f"- **Entity Level**: `{entity_col}` (table tracks individual {entity_col.lower().replace('_', ' ')})")
        
        # Technical granularity
        if tech_granularity and tech_granularity != entity_col:
            gran_lines.append(f"- **Technical Granularity**: `{tech_granularity}` (each row is unique, but column may be meaningless)")
        else:
            gran_lines.append(f"- **Technical Granularity**: No single meaningful unique column found")
        
        # Business explanation
        gran_lines.append(f"- **Business Logic**: {business_explanation}")
        
        # Example with timeline if available
        if example_value:
            gran_lines.append(f"- **Example**: {entity_col} = `{example_value}`")
            
            # Add timeline information
            if timeline_info:
                for date_col, info in timeline_info.items():
                    if info.get("earliest") and info.get("latest"):
                        gran_lines.append(f"  - {date_col}: {info['earliest']} → {info['latest']} ({info.get('count', 'unknown')} distinct values)")
            
            # Show what columns change
            if changing_cols:
                business_cols = [col for col in changing_cols if not any(
                    tech_word in col.lower() for tech_word in ['scd', 'hash', 'dw_', 'created', 'updated']
                )]
                technical_cols = [col for col in changing_cols if col not in business_cols]
                
                if business_cols:
                    gran_lines.append(f"  - Business changes: {', '.join(f'`{col}`' for col in business_cols[:4])}")
                if technical_cols:
                    gran_lines.append(f"  - Technical tracking: {', '.join(f'`{col}`' for col in technical_cols[:4])}")
        
        # Scale information
        if dup_count:
            gran_lines.append(f"- **Scale**: {dup_count:,} {entity_col.lower().replace('_', ' ')}s have multiple rows")
            
    elif granularity_type in ["unique", "pattern"]:
        # Legacy format support
        gran_lines.append(f"- **Primary Key**: `{granularity.get('granularity_column', 'TBD')}`")
        gran_lines.append(f"- **Pattern**: {granularity.get('summary', 'TBD')}")
        
        example_val = granularity.get("example_value")
        example_desc = granularity.get("example_description")
        dup_count = granularity.get("duplicate_count")
        
        if example_val and example_desc:
            gran_lines.append(f"- **Example**: {granularity.get('granularity_column')} = `{example_val}`")
            gran_lines.append(f"  - {example_desc}")
            if dup_count:
                gran_lines.append(f"  - {dup_count:,} total entities have multiple rows")
        
    else:
        # Fallback for unknown/error cases
        gran_lines.append(f"- **Summary**: {granularity.get('summary', 'Unable to determine granularity pattern')}")
        
        # Show any technical granularity found
        tech_granularity = granularity.get("actual_granularity_column")
        if tech_granularity:
            gran_lines.append(f"- **Technical Granularity**: `{tech_granularity}` (unique column found)")
        
        # Show LLM predictions if available
        if granularity.get("llm_predicted_columns"):
            predicted = granularity.get("llm_predicted_columns", [])
            gran_lines.append(f"- **Predicted Entity Columns**: {', '.join(f'`{col}`' for col in predicted[:3])}")
        
        # Show legacy details if available
        for det in granularity.get("details", [])[:3]:
            key = det.get("candidate_key")
            dups = det.get("duplicates")
            if key and dups is not None:
                gran_lines.append(f"  - `{key}` duplicates: {dups:,}")
    
    if not gran_lines:
        gran_lines = ["- Summary: TBD"]

    content = f"""# {table_fqn}

## Table Overview
{general_desc}

## Business Context
{business_ctx}

## Who Maintains It
{who_maintains}

## Data Characteristics
- **Row Count (approx)**: {approx_rows or 'TBD'}
- **Update Frequency**: TBD
- **Data Freshness**: TBD

## Granularity
{chr(10).join(gran_lines)}

## Columns
{chr(10).join(col_lines)}

## Sample Instance Deep Dive
TBD (see granularity details for example keys and samples)

## Top Sample Queries
{chr(10).join(query_lines) if query_lines else 'TBD'}

## Links
{f'- Confluence: {confluence_link}' if confluence_link else 'TBD'}

---
*Last updated: auto-generated*
"""
    return content


def render_markdown(
    output_dir: Path,
    database: str,
    schema: str,
    table: str,
    overview: Dict[str, Any],
    columns_meta: List[Dict[str, Any]],
    granularity: Dict[str, Any],
    top_queries: List[Dict[str, Any]],
    confluence_hits: Optional[List[Dict[str, Any]]],
    narrative: Dict[str, str],
) -> Path:
    output_dir = Path(output_dir) / database / schema
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{table}.md"

    content = build_markdown_content(
        table_fqn=f"{database}.{schema}.{table}",
        overview=overview,
        columns_meta=columns_meta,
        granularity=granularity,
        top_queries=top_queries,
        confluence_hits=confluence_hits,
        narrative=narrative,
    )

    out_path.write_text(content)
    return out_path

