import os
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from portkey_ai import Portkey
except ImportError:
    Portkey = None  # Graceful fallback when Portkey SDK isn't installed
from dotenv import load_dotenv

from utils.snowflake_connection import SnowflakeHook
from local_tools.table_context_agent.tyler_sources import (
    resolve_table_name,
    fetch_table_overview,
    fetch_columns_metadata,
    fetch_columns_metadata_with_usage,
    fetch_top_sample_queries,
    fetch_most_common_joins,
    fetch_sample_queries_from_most_used_user,
    find_tables_by_name,
    find_best_fqn_via_usage,
)
from local_tools.table_context_agent.snowflake_explorer import infer_granularity, enhanced_granularity_analysis
from local_tools.table_context_agent.confluence_client import ConfluenceSearcher
from local_tools.table_context_agent.renderer import render_markdown, build_markdown_content


@dataclass
class TableIdentifier:
    database: str
    schema: str
    table: str

    @property
    def fqn(self) -> str:
        return f"{self.database}.{self.schema}.{self.table}"


class PortkeyLLM:
    """Thin wrapper around Portkey Python SDK for deterministic usage in this tool."""

    def __init__(self) -> None:
        # Load project .env to ensure keys are available
        try:
            project_root = Path(__file__).resolve().parents[2]
            env_path = project_root / "config" / ".env"
            if env_path.exists():
                load_dotenv(dotenv_path=env_path, override=True)
        except Exception:
            pass

        if Portkey is None:
            raise RuntimeError("Portkey SDK not installed. Please `pip install portkey-ai` or set print-only fallback.")
        
        api_key = os.getenv("PORTKEY_API_KEY")
        virtual_key = os.getenv("PORTKEY_OPENAI_VIRTUAL_KEY")
        base_url = os.getenv("PORTKEY_BASE_URL", "https://cybertron-service-gateway.doordash.team/v1")
        
        if not api_key or not virtual_key:
            raise RuntimeError("PORTKEY_API_KEY and PORTKEY_OPENAI_VIRTUAL_KEY must be set in env")

        # Create a Portkey client configured for DoorDash GenAI Gateway
        self.client = Portkey(
            base_url=base_url,
            api_key=api_key,
            virtual_key=virtual_key
        )
        self.model = os.getenv("PORTKEY_MODEL", "gpt-4o-mini")

    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.2) -> str:
        completion = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=temperature,
        )
        # Portkey returns OpenAI-compatible structure
        return completion.choices[0].message["content"]


def case_insensitive_get(d: Dict[str, Any], key: str, default=None):
    """Get value from dictionary with case-insensitive key lookup."""
    # Try exact key first
    if key in d:
        return d[key]
    
    # Try case-insensitive lookup
    for k, v in d.items():
        if k.upper() == key.upper():
            return v
    
    return default


def guess_key_columns(columns: List[Dict[str, Any]]) -> List[str]:
    """Heuristic guess of candidate key columns based on common id suffixes/names."""
    candidates: List[str] = []
    for col in columns:
        name = str(col.get("column_name", ""))
        if not name:
            continue
        lname = name.lower()
        if lname in {"delivery_id", "user_id", "device_id", "order_id"}:
            candidates.append(name)
        elif lname.endswith("_id"):
            candidates.append(name)
    # Deduplicate preserving order
    seen = set()
    uniq = []
    for c in candidates:
        if c not in seen:
            uniq.append(c)
            seen.add(c)
    return uniq[:5]


def build_llm_context_payload(
    table: TableIdentifier,
    overview: Dict[str, Any],
    columns_meta: List[Dict[str, Any]],
    confluence_hits: Optional[List[Dict[str, Any]]],
) -> str:
    payload = {
        "table": table.fqn,
        "overview": overview,
        "columns_meta": columns_meta[:200],  # prevent overly large prompts
        "confluence": confluence_hits or [],
    }
    return json.dumps(payload, default=str)


def synthesize_descriptions(llm: PortkeyLLM, payload_json: str, confluence_hits: Optional[List[Dict[str, Any]]] = None) -> Dict[str, str]:
    system = (
        "You are an analytics documentation assistant. Given Snowflake metadata and optional "
        "Confluence context, produce concise, accurate business-facing descriptions. "
        "Focus on practical business understanding. Use table and column comments as primary source. "
        "Avoid speculation; if unknown, say 'TBD'."
    )
    
    # Enhanced prompt based on whether we have Confluence docs
    if confluence_hits and len(confluence_hits) > 0:
        user = (
            "Using the following JSON context AND Confluence documentation, write:\n"
            "- General table description (focus on business purpose)\n"
            "- Business Context (what business process/domain this supports)\n"
            "- Who maintains it (from metadata or Confluence, otherwise 'TBD')\n"
            "- Primary use cases (based on column usage and comments)\n"
            "\nPrioritize Confluence content for business context, but use table/column comments "
            "from metadata for technical details. Keep each section concise (2-4 sentences).\n\n"
            f"Context JSON:\n{payload_json}"
        )
    else:
        user = (
            "Using the following JSON context (no Confluence docs available), write:\n"
            "- General table description (infer from table name, comments, and column structure)\n"
            "- Business Context (infer business domain from schema/database and column types)\n"
            "- Who maintains it (from TABLE_OWNER field, otherwise 'TBD')\n"
            "- Primary use cases (based on column usage patterns and comments)\n"
            "\nPay special attention to the 'comment' fields in both table and column metadata. "
            "Use column names and types to infer business purpose. Keep each section concise (2-4 sentences).\n\n"
            f"Context JSON:\n{payload_json}"
        )
    
    msg = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    text = llm.chat(msg)
    return {"narrative": text}


def safe_generate_narrative(payload_json: str, confluence_hits: Optional[List[Dict[str, Any]]] = None, verbose: bool = False) -> Dict[str, str]:
    """Generate narrative via Portkey; fallback to placeholders if Portkey or keys are missing."""
    try:
        llm = PortkeyLLM()
        if verbose:
            print(f"      🤖 LLM Request: Generating business context narrative")
            print(f"      📋 Payload length: {len(payload_json)} characters")
        return synthesize_descriptions(llm, payload_json, confluence_hits)
    except Exception as e:
        placeholder = (
            "General table description: TBD.\n\n"
            "Business Context: TBD.\n\n"
            "Who maintains it: TBD.\n\n"
            "Primary use cases: TBD."
        )
        return {"narrative": placeholder}


def build_enhanced_markdown_content(enhanced_data: Dict[str, Any]) -> str:
    """
    Build markdown content following the new report structure:
    - Table Overview
    - Business Context
    - Metadata (Table Metadata, Most Common Joins, Column Metadata)
    - Granularity Analysis
    - Sample Queries
    """
    
    table_overview = enhanced_data['table_overview']
    business_context = enhanced_data['business_context']
    metadata = enhanced_data['metadata']
    granularity = enhanced_data['granularity_analysis']
    sample_queries = enhanced_data['sample_queries']
    confluence_hits = enhanced_data['confluence_hits']
    
    content = []
    
    # Table Overview
    content.append(f"# {table_overview['full_table_name']}")
    content.append("")
    content.append("## Table Overview")
    content.append("")
    content.append(f"**Database:** {table_overview['database']}")
    content.append(f"**Schema:** {table_overview['schema']}")
    content.append(f"**Table:** {table_overview['table']}")
    content.append(f"**Owner:** {table_overview['owner']}")
    content.append(f"**Row Count:** {table_overview['row_count']}")
    if table_overview['created']:
        content.append(f"**Created:** {table_overview['created']}")
    if table_overview['last_altered']:
        content.append(f"**Last Modified:** {table_overview['last_altered']}")
    content.append("")
    content.append(f"**Description:** {table_overview['comment']}")
    content.append("")
    
    # Business Context
    content.append("## Business Context")
    content.append("")
    content.append(business_context)
    content.append("")
    
    # Confluence References (if available)
    if confluence_hits:
        content.append("### Related Documentation")
        for hit in confluence_hits[:3]:  # Show top 3
            content.append(f"- [{hit.get('title', 'Confluence Page')}]({hit.get('url', '#')})")
        content.append("")
    
    # Metadata Section
    content.append("## Metadata")
    content.append("")
    
    # Table Metadata
    content.append("### Table Metadata")
    content.append("")
    table_meta = metadata['table_metadata']
    if table_meta.get('TABLE_TYPE'):
        content.append(f"**Type:** {table_meta['TABLE_TYPE']}")
    if table_meta.get('BYTES'):
        bytes_mb = int(table_meta['BYTES']) / (1024 * 1024) if table_meta['BYTES'] else 0
        content.append(f"**Size:** {bytes_mb:.1f} MB")
    if table_meta.get('IS_TRANSIENT'):
        content.append(f"**Transient:** {table_meta['IS_TRANSIENT']}")
    content.append("")
    
    # Most Common Joins
    content.append("### Most Common Joins")
    content.append("")
    common_joins = metadata['most_common_joins']
    if common_joins:
        content.append("| Joined Table | Query Count |")
        content.append("|--------------|-------------|")
        for join in common_joins[:10]:
            content.append(f"| {join.get('joined_table', 'N/A')} | {join.get('query_count', 0)} |")
    else:
        content.append("No common join patterns found.")
    content.append("")
    
    # Column Metadata
    content.append("### Column Metadata")
    content.append("")
    columns = metadata['column_metadata']
    if columns:
        content.append("| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |")
        content.append("|------------|-------------|---------|---------|-----------|----------------|---------|")
        for col in columns:
            usage_rank = col.get('usage_rank', 'N/A')
            col_name = col.get('column_name', 'N/A')
            queries = col.get('queries', 0)
            ordinal = col.get('ordinal_position', 'N/A')
            data_type = col.get('data_type', 'N/A')
            is_cluster = col.get('is_cluster_key', 0)
            comment = col.get('comment', '').replace('\n', ' ')[:100] if col.get('comment') else 'No comment'
            
            content.append(f"| {usage_rank} | {col_name} | {queries} | {ordinal} | {data_type} | {is_cluster} | {comment} |")
    else:
        content.append("No column metadata available.")
    content.append("")
    
    # Granularity Analysis
    content.append("## Granularity Analysis")
    content.append("")
    if granularity:
        if isinstance(granularity, dict):
            if granularity.get('explanation'):
                content.append(granularity['explanation'])
            elif granularity.get('summary'):
                content.append(granularity['summary'])
        else:
            content.append(str(granularity))
    else:
        content.append("Granularity analysis not available.")
    content.append("")
    
    # Sample Queries
    content.append("## Sample Queries")
    content.append("")
    if sample_queries:
        for i, query in enumerate(sample_queries, 1):
            content.append(f"### Query {i}")
            if query.get('latest_execution_time'):
                content.append(f"**Last Executed:** {query['latest_execution_time']}")
            content.append("")
            content.append("```sql")
            content.append(query.get('query_text', 'No query text available'))
            content.append("```")
            content.append("")
    else:
        content.append("No sample queries available.")
    
    return "\n".join(content)


def render_enhanced_markdown(output_dir: Path, enhanced_data: Dict[str, Any]) -> Path:
    """Render enhanced markdown to file."""
    table_overview = enhanced_data['table_overview']
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = f"{table_overview['database']}_{table_overview['schema']}_{table_overview['table']}.md"
    filepath = output_dir / filename
    
    # Generate content
    content = build_enhanced_markdown_content(enhanced_data)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main(
    table: str,
    database: Optional[str] = None,
    schema: Optional[str] = None,
    output_root: Optional[str] = None,
    sample_row_limit: int = 10,
    print_only: bool = False,
    verbose: bool = False,
) -> str | Path:
    # Load project .env for Snowflake/Confluence defaults as well
    try:
        project_root = Path(__file__).resolve().parents[2]
        env_path = project_root / "config" / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, override=True)
    except Exception:
        pass

    # Step 1: Resolve table name (handle both full and partial names)
    if verbose:
        print(f"🔍 STEP 1: Resolving table name for '{table}'...")
    
    with SnowflakeHook() as sf:
        full_table_name = resolve_table_name(sf, table, verbose=verbose)
        
        if verbose:
            print(f"✅ Resolved to: {full_table_name}")
        
        # Parse the resolved full table name
        parts = full_table_name.split('.')
        if len(parts) != 3:
            raise RuntimeError(f"Invalid table name format: {full_table_name}")
        
        resolved_database, resolved_schema, resolved_table = parts
        table_id = TableIdentifier(
            database=resolved_database,
            schema=resolved_schema,
            table=resolved_table
        )

    # Step 2: Confluence search (try both full table name and table name)
    if verbose:
        print(f"📚 STEP 2: Searching Confluence documentation...")
    
    confluence = ConfluenceSearcher.from_env()
    confluence_hits: Optional[List[Dict[str, Any]]] = None
    if confluence is not None:
        if verbose:
            print(f"   🔍 Searching for '{full_table_name}'...")
        # Search with full table name first
        confluence_hits = confluence.search_pages(query=full_table_name, limit=5)
        # If no results, try with just table name
        if not confluence_hits:
            if verbose:
                print(f"   🔍 No results, trying '{resolved_table}'...")
            confluence_hits = confluence.search_pages(query=resolved_table, limit=5)
        
        if verbose:
            count = len(confluence_hits) if confluence_hits else 0
            print(f"✅ Found {count} Confluence pages")
    else:
        if verbose:
            print("   ⚠️  Confluence not configured, skipping search")

    # Step 3: Fetch all metadata using Tyler's tables
    if verbose:
        print(f"📊 STEP 3: Fetching metadata from Tyler's tables...")
    
    with SnowflakeHook() as sf:
        # Table metadata with formatted row counts
        if verbose:
            print(f"   📋 Fetching table metadata...")
        overview = fetch_table_overview(sf, table_id.database, table_id.schema, table_id.table, verbose=verbose)
        
        # Enhanced column metadata with usage ranking
        if verbose:
            print(f"   📊 Fetching column metadata with usage ranking...")
        columns_meta_with_usage = fetch_columns_metadata_with_usage(sf, full_table_name, verbose=verbose)
        
        # Most commonly joined tables
        if verbose:
            print(f"   🔗 Fetching most common joins...")
        common_joins = fetch_most_common_joins(sf, full_table_name, limit=10, verbose=verbose)
        
        # Sample queries from most used user
        if verbose:
            print(f"   📝 Fetching sample queries...")
        sample_queries = fetch_sample_queries_from_most_used_user(sf, full_table_name, limit=2, verbose=verbose)
        
        # Legacy column metadata for granularity analysis compatibility
        columns_meta = fetch_columns_metadata(sf, table_id.database, table_id.schema, table_id.table)

        # Initialize LLM for granularity analysis
        try:
            llm = PortkeyLLM()
        except Exception:
            llm = None

        # Enhanced granularity analysis with business context
        try:
            if llm:
                # Build comprehensive business context for granularity analysis
                business_context = ""
                if confluence_hits:
                    # Include title and excerpt from top Confluence hit
                    top_hit = confluence_hits[0]
                    business_context = f"Business context from Confluence: {top_hit.get('title', '')} - {top_hit.get('excerpt', '')[:200]}... "
                if case_insensitive_get(overview, 'COMMENT'):
                    business_context += f"Table description: {case_insensitive_get(overview, 'COMMENT')} "
                
                # Get table row count for adaptive time filtering
                table_row_count = case_insensitive_get(overview, 'ROW_COUNT')
                
                granularity = enhanced_granularity_analysis(
                    sf, table_id.fqn, table_id.table, table_id.schema,
                    columns_meta, llm, sample_row_limit, business_context, 
                    verbose=verbose, table_row_count=table_row_count
                )
            else:
                raise Exception("LLM not available")
        except Exception:
            # Fallback to legacy approach
            if verbose:
                print("🔄 Enhanced granularity analysis failed, falling back to legacy approach...")
            candidate_keys = guess_key_columns(columns_meta)
            # Try to get time column and lookback days from LLM prediction for fallback
            time_column = None
            lookback_days = 7
            try:
                if llm:
                    from .snowflake_explorer import _predict_granularity_columns
                    table_row_count = case_insensitive_get(overview, 'ROW_COUNT')
                    _, time_column, lookback_days = _predict_granularity_columns(llm, table_id.table, table_id.schema, columns_meta, business_context, business_context, table_row_count)
            except:
                pass
            granularity = infer_granularity(sf, table_id.fqn, candidate_keys, sample_row_limit, verbose=verbose, time_column=time_column, lookback_days=lookback_days)

    # Step 4: Generate business context and table description
    if verbose:
        print(f"🤖 STEP 4: Generating business context with LLM...")
    
    payload_json = build_llm_context_payload(table_id, overview, columns_meta_with_usage, confluence_hits)
    narrative = safe_generate_narrative(payload_json, confluence_hits, verbose=verbose)

    # Step 5: Build enhanced report structure
    enhanced_data = {
        'table_overview': {
            'full_table_name': full_table_name,
            'database': table_id.database,
            'schema': table_id.schema,
            'table': table_id.table,
            'owner': case_insensitive_get(overview, 'TABLE_OWNER', 'TBD'),
            'row_count': case_insensitive_get(overview, 'FORMATTED_ROW_COUNT', 'Unknown'),
            'comment': case_insensitive_get(overview, 'COMMENT', 'No description available'),
            'created': case_insensitive_get(overview, 'CREATED'),
            'last_altered': case_insensitive_get(overview, 'LAST_ALTERED')
        },
        'business_context': narrative.get('narrative', 'TBD'),
        'metadata': {
            'table_metadata': overview,
            'most_common_joins': common_joins,
            'column_metadata': columns_meta_with_usage
        },
        'granularity_analysis': granularity,
        'sample_queries': sample_queries,
        'confluence_hits': confluence_hits or []
    }

    # Build markdown content with new structure
    content = build_enhanced_markdown_content(enhanced_data)

    if print_only:
        return content

    # Render to file
    output_dir = (
        Path(output_root)
        if output_root
        else Path(__file__).parent.parent / "context" / "analysis-context" / "snowflake-table-context"
    )
    md_path = render_enhanced_markdown(
        output_dir=output_dir,
        enhanced_data=enhanced_data
    )
    return md_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Snowflake table context markdown")
    parser.add_argument("table", help="Table name (bare or fully-qualified)")
    parser.add_argument("--database", default=None)
    parser.add_argument("--schema", default=None)
    parser.add_argument("--output-root", default=None)
    parser.add_argument("--sample-row-limit", type=int, default=10)
    parser.add_argument("--print-only", action="store_true", help="Print markdown instead of writing a file")
    parser.add_argument("--verbose", action="store_true", help="Show verbose output including SQL queries and LLM requests")
    args = parser.parse_args()

    result = main(
        table=args.table,
        database=args.database,
        schema=args.schema,
        output_root=args.output_root,
        sample_row_limit=args.sample_row_limit,
        print_only=args.print_only,
        verbose=args.verbose,
    )
    if args.print_only and isinstance(result, str):
        print(result)
    else:
        print(f"Wrote: {result}")

