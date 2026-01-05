# Cursor Analytics MCP Server - Usage Examples

This document provides practical examples of using the cursor-analytics-mcp server tools.

## Quick Start

1. **Install the MCP server**:
   ```bash
   cd cursor-analytics-mcp
   ./install.sh
   ```

2. **Activate environment and test**:
   ```bash
   source venv/bin/activate
   python tests/test_server.py
   ```

## Tool Usage Examples

### 📊 Table Context Generation

#### Generate Table Context Documentation
```json
{
  "name": "generate_snowflake_table_context",
  "arguments": {
    "table_name": "dimension_deliveries",
    "output_format": "markdown",
    "sample_row_limit": 10,
    "verbose": false
  }
}
```

#### Save Table Context to File
```json
{
  "name": "save_snowflake_table_context",
  "arguments": {
    "table_name": "iguazu.consumer.m_card_view",
    "output_directory": "context/analysis-context/snowflake-table-context",
    "sample_row_limit": 5,
    "verbose": true
  }
}
```

#### Check Table Context System Status
```json
{
  "name": "get_table_context_status",
  "arguments": {}
}
```

**Example Response:**
```json
{
  "table_context_agent_available": true,
  "dependencies": {
    "snowflake_connection": true,
    "confluence_client": true,
    "portkey_llm": true
  },
  "features": [
    "Table name resolution and validation",
    "Business context generation with LLM",
    "Metadata analysis and formatting",
    "Granularity detection and analysis",
    "Large table performance optimization (>10B rows)",
    "Sample query extraction",
    "Confluence documentation integration",
    "Case-insensitive field access",
    "Markdown and JSON output formats"
  ],
  "version": "1.0.0",
  "status": "ready",
  "message": "Table context agent is fully operational"
}
```

### 🗄️ Snowflake Operations

#### Execute a Simple Query
```json
{
  "name": "snowflake_query",
  "arguments": {
    "query": "SELECT COUNT(*) as delivery_count FROM proddb.public.dimension_deliveries WHERE active_date >= '2024-01-01'",
    "method": "pandas"
  }
}
```

#### Create a Table from Data
```json
{
  "name": "snowflake_create_table",
  "arguments": {
    "table_name": "my_analysis_results",
    "data": "[{\"metric\": \"conversion_rate\", \"value\": 0.15}, {\"metric\": \"order_rate\", \"value\": 0.08}]",
    "schema": "my_personal_schema"
  }
}
```

#### Drop a Table
```json
{
  "name": "snowflake_drop_table",
  "arguments": {
    "table_name": "temporary_analysis",
    "schema": "my_personal_schema"
  }
}
```

### 🔍 Query Search

#### Search for Delivery-Related Queries
```json
{
  "name": "query_search",
  "arguments": {
    "keywords": ["delivery", "assignment", "eta"],
    "limit": 10,
    "save_to_context": true
  }
}
```

#### Search for Pizza Business Queries
```json
{
  "name": "query_search",
  "arguments": {
    "keywords": ["pizza", "ent_pizza_biz"],
    "limit": 5
  }
}
```

### 📊 Curie Experiment Export

#### Get Experiment Metadata First
```json
{
  "name": "curie_get_metadata",
  "arguments": {
    "experiment_name": "drive_pizza_bag_preference_toggle"
  }
}
```

#### Simple Curie Export
```json
{
  "name": "curie_export",
  "arguments": {
    "experiment_name": "drive_pizza_bag_preference_toggle",
    "primary_metrics": ["store_level_page_conversion", "dsmp_order_rate_7d"],
    "dimension_names": ["ent_pizza_biz"],
    "use_oauth": true
  }
}
```

#### Advanced Curie Export with Multiple Categories
```json
{
  "name": "curie_export",
  "arguments": {
    "experiment_name": "consumer_ox_dish_exp_pizza_ui__Android_run3",
    "primary_metrics": ["store_level_page_conversion", "item_level_page_conversion"],
    "secondary_metrics": ["sub_avg_item_price", "variable_profit_per_order"],
    "guardrail_metrics": ["cx_app_quality_crash_android"],
    "dimension_names": ["ent_pizza_biz", "pizza_transformed"],
    "selected_columns": ["metric_name", "dimension_cut_name", "control_value", "treatment_value", "relative_impact", "p_value", "stat_sig", "relative_impact_ci_lower", "relative_impact_ci_upper"],
    "share_email": "your.email@doordash.com",
    "use_oauth": true
  }
}
```

### 📚 Context Management

#### List All Available Context Sources
```json
{
  "name": "list_context_sources",
  "arguments": {
    "source_type": "all"
  }
}
```

#### Fetch Table Context
```json
{
  "name": "fetch_table_context",
  "arguments": {
    "database": "proddb",
    "schema": "public",
    "table": "dimension_deliveries"
  }
}
```

#### List Available Pod Queries
```json
{
  "name": "fetch_pod_queries",
  "arguments": {
    "query_name": "list"
  }
}
```

#### Fetch Specific Pod Query
```json
{
  "name": "fetch_pod_queries",
  "arguments": {
    "query_name": "pricing-and-affordability"
  }
}
```

#### List User Context
```json
{
  "name": "fetch_user_context",
  "arguments": {
    "context_path": "list"
  }
}
```

#### Fetch Specific User Context
```json
{
  "name": "fetch_user_context",
  "arguments": {
    "context_path": "analysis_guides/delivery_analysis.md"
  }
}
```

#### List Cursor Rules
```json
{
  "name": "fetch_cursor_rules",
  "arguments": {
    "rule_name": "list"
  }
}
```

#### Fetch Specific Cursor Rule
```json
{
  "name": "fetch_cursor_rules",
  "arguments": {
    "rule_name": "global"
  }
}
```

## Common Workflows

### 🔄 Full Analysis Workflow

1. **Search for related queries**:
   ```json
   {"name": "query_search", "arguments": {"keywords": ["pizza", "conversion"]}}
   ```

2. **Get table context**:
   ```json
   {"name": "fetch_table_context", "arguments": {"database": "proddb", "schema": "public", "table": "dimension_deliveries"}}
   ```

3. **Execute analysis query**:
   ```json
   {"name": "snowflake_query", "arguments": {"query": "SELECT business_name, COUNT(*) FROM proddb.public.dimension_deliveries WHERE business_name LIKE '%pizza%' GROUP BY 1"}}
   ```

4. **Save results**:
   ```json
   {"name": "snowflake_create_table", "arguments": {"table_name": "pizza_analysis", "data": "[results from previous query]"}}
   ```

### 🧪 Experiment Analysis Workflow

1. **Get experiment metadata**:
   ```json
   {"name": "curie_get_metadata", "arguments": {"experiment_name": "your_experiment"}}
   ```

2. **Check cursor rules for experiment analysis**:
   ```json
   {"name": "fetch_cursor_rules", "arguments": {"rule_name": "curie_export_rules"}}
   ```

3. **Export results**:
   ```json
   {"name": "curie_export", "arguments": {"experiment_name": "your_experiment", "primary_metrics": ["metric1", "metric2"]}}
   ```

### 📝 Google Docs Integration Workflow

1. **Export markdown to Google Docs** (any local file):
   ```json
   {
     "name": "export_markdown_to_google_doc",
     "arguments": {
       "markdown_path": "/Users/fiona.fan/Documents/my_analysis.md",
       "open_browser": false
     }
   }
   ```

   **Response:**
   ```
   ✅ Markdown exported to Google Docs successfully!

   📄 **Title:** My Analysis
   📝 **Document ID:** 1sx4JaaKcMbNYOS-kwUPTuIvL5ard-RiN_B0ZxgEFwv4
   🔗 **URL:** https://docs.google.com/document/d/1sx4JaaKcMbNYOS-kwUPTuIvL5ard-RiN_B0ZxgEFwv4/edit
   🔄 **Action:** Created new document
   💾 **Mapping:** Automatically created for future exports
   ```

2. **Import Google Doc to markdown**:
   ```json
   {
     "name": "import_google_doc_to_markdown",
     "arguments": {
       "doc_url": "https://docs.google.com/document/d/DOC_ID/edit",
       "markdown_path": "/Users/fiona.fan/Documents/imported_doc.md"
     }
   }
   ```

3. **Check sync status**:
   ```json
   {
     "name": "show_markdown_google_doc_status",
     "arguments": {
       "markdown_path": "/Users/fiona.fan/Documents/my_analysis.md"
     }
   }
   ```

4. **List all tracked files**:
   ```json
   {"name": "list_markdown_google_doc_mappings"}
   ```

**Key Features:**
- ✅ Works with any local file path (not just current directory)
- ✅ Non-interactive, fully automated
- ✅ Auto-creates/updates Google Docs
- ✅ Local mapping file (`.gdocs_sync_mappings.json` in current directory)
- ✅ Returns document ID and URL
- ✅ Supports images and tables (with Apps Script)

## Error Handling

The MCP server provides detailed error messages for common issues:

- **Missing credentials**: Check your SNOWFLAKE_USER and SNOWFLAKE_PAT environment variables
- **Invalid experiment name**: Verify the experiment exists in Curie
- **Missing context**: Context files may not exist for all tables/queries
- **Permission errors**: Ensure you have proper Snowflake and Google Sheets permissions

## Integration Tips

### With Claude/AI Assistants
- Use the `list_context_sources` tool first to understand what's available
- Always check experiment metadata before exporting
- Leverage query search to find patterns before writing new SQL

### With Cursor IDE
- The MCP server integrates seamlessly with Cursor's workflow
- Use cursor rules to maintain consistency
- Save results to user-context for team collaboration

### With Data Analysis
- Combine Snowflake queries with context fetching for comprehensive analysis
- Use table context to understand join patterns and data quality
- Leverage pod queries as starting points for new analysis