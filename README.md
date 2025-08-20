# Cursor Analytics MCP Server 🚀

A comprehensive Model Context Protocol (MCP) server providing analytics tools for Snowflake operations, experiment analysis, document management, and context retrieval.

## Table of Contents

- [Overview](#overview)
- [Setup and Installation](#setup-and-installation)
- [MCP Tools Available](#mcp-tools-available)
- [Context Management System](#context-management-system)
- [Architecture](#architecture)
- [Integrations](#integrations)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)

## Overview

The Cursor Analytics MCP Server is a standalone MCP server built with FastMCP that provides:

- **Snowflake Operations**: Execute queries, manage tables, and retrieve data
- **Query Search**: Find historical queries by table name or keywords
- **Curie Experiment Export**: Export experiment results to Google Sheets
- **Google Docs Integration**: Convert and crawl Google Docs to markdown
- **Hybrid Context Search**: AI-powered document search with BM25 + embeddings
- **Table Context Generation**: Automated documentation for Snowflake tables

## Setup and Installation

### 0) Prerequisites

- Python 3.10+ (recommended)
- Access to Snowflake with appropriate credentials
- Google API credentials for Sheets/Docs integration

### 1) Run as MCP Server

#### Automatic Installation

```bash
# Clone and install everything
git clone <repository-url>
cd cursor-analytics-mcp
./install.sh
```

The installation script will:
- Install `uv` package manager if needed
- Create a Python 3.10+ virtual environment
- Install all dependencies including FastMCP
- Set up the project structure

#### Manual Installation

```bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .
```

### 2) Configure Credentials

Create a `config/.env` file like config/.env.template.


### 3) Test the Server

```bash
source venv/bin/activate
cursor-analytics-mcp
```

### 4) Add to MCP Client Configuration

Add to your MCP client (like Cursor) configuration:

```json
{
  "mcpServers": {
    "cursor-analytics": {
      "command": "/path/to/cursor-analytics-mcp/venv/bin/cursor-analytics-mcp",
      "env": {
        "SNOWFLAKE_USER": "your.username",
        "SNOWFLAKE_PASSWORD": "your_secure_password",
        "SNOWFLAKE_DATABASE": "proddb",
        "SNOWFLAKE_SCHEMA": "your_schema",
        "SNOWFLAKE_WAREHOUSE": "YOUR_WAREHOUSE",
        "SNOWFLAKE_ROLE": "your_role",
        "SNOWFLAKE_ACCOUNT": "your_account",
        "DOCUMENT_INDEX_TABLE": "document_index_community",
        "CHUNK_INDEX_TABLE": "chunk_index_community",
        "GITHUB_REPO": "your-org/cursor-analytics-mcp",
        "GITHUB_BRANCH": "main",
        "PORTKEY_BASE_URL": "https://your-portkey-gateway.com/v1",
        "PORTKEY_API_KEY": "your_portkey_api_key",
        "PORTKEY_OPENAI_VIRTUAL_KEY": "your_openai_virtual_key",
        "OPENAI_VIRTUAL_KEY": "sk-proj-your_openai_api_key_here",
        "CONFLUENCE_BASE_URL": "https://your-org.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_confluence_api_token",
        "GOOGLE_SHEET_CREDENTIALS_FILE": "config/credentials/google_oauth_credentials.json",
        "GOOGLE_DOCS_CREDENTIALS_FILE": "config/credentials/google_doc_credentials.json"
      }
    }
  }
}
```

## MCP Tools Available

### Snowflake Operations

#### `execute_snowflake_query(query, method="pandas", database=None, schema=None, warehouse=None)`
Execute SQL queries on Snowflake with multiple processing backends.

**Parameters:**
- `query`: SQL query to execute
- `method`: Processing method (`"pandas"`, `"spark"`, `"polars"`)
- `database`, `schema`, `warehouse`: Optional overrides

**Example:**
```sql
SELECT * FROM dimension_users LIMIT 10
```

### Query Discovery

#### `search_queries_by_table_name(table_name, limit=5)`
Find the most frequently used queries for a specific table.

**Example:**
```python
search_queries_by_table_name("dimension_deliveries", limit=3)
```

#### `search_queries_by_keyword(keywords, limit=5)`
Find queries containing all specified keywords.

**Example:**
```python
search_queries_by_keyword(["conversion", "funnel"], limit=5)
```

### Data Export

#### `execute_sql_and_upload_to_google_sheet(query, tab_name, spreadsheet_id=None, max_rows=20000, spreadsheet_title=None)`
Execute a SQL query and upload results directly to Google Sheets.

### Experiment Analysis (Curie)

#### `export_curie_experiment_to_sheet(experiment_name, primary_metrics=None, secondary_metrics=None, ...)`
Export Curie experiment results to Google Sheets with formatting.

#### `curie_get_metadata(experiment_name)`
Get comprehensive metadata about a Curie experiment including variants, metrics, and dimensions.

### Google Docs Integration

#### `crawl_and_convert_google_docs(master_doc_url, output_path="context/experiment-readouts")`
Crawl all Google Docs links from a master document and convert them to markdown.

#### `convert_single_google_doc_to_markdown(doc_url, output_path="context/experiment-readouts")`
Convert a single Google Doc to markdown with team-based organization.

#### `convert_google_doc_to_markdown(doc_url, write_file=False, output_path="context/experiment-readouts")`
Convert a Google Doc to markdown content (returns as string).

### Context Search & Management

#### `fetch_table_context(query, top_k=5, team=None, write_to_local=False)`
Search Snowflake table documentation using hybrid search.

**Example queries:**
- `"user dimensions table"`
- `"delivery facts and metrics"`
- `"consumer device settings"`

#### `fetch_pod_queries(query, top_k=3, team=None)`
Search validated master SQL queries.

**Example queries:**
- `"pricing analysis"`
- `"affordability metrics"`

#### `fetch_user_context(query, top_k=5, team=None, write_to_local=False)`
Search user-specific context documents.

#### `fetch_experiment_readouts(query, top_k=5, team=None, write_to_local=False)`
Search experiment readout documents.

#### `fetch_deep_dives(query, top_k=5, team=None, write_to_local=False)`
Search deep dive analysis documents.

#### `fetch_cursor_rules(rule_name)`
Fetch Cursor rules from `.cursor/rules/` directory. Use `rule_name="list"` to see available rules.

### Table Documentation

#### `describe_table(table_name, output_format="markdown", sample_row_limit=10, verbose=False)`
Generate comprehensive documentation for a Snowflake table including business context, metadata analysis, and granularity detection.

#### Table Context Agent Architecture

The Table Context Agent uses a sophisticated 6-step process to generate comprehensive table documentation:

![Table Context Agent Flow](local_tools/table_context_agent/table_context_agent_flow.png)

**Process Overview:**
1. **Table Resolution** - Resolves partial names using Tyler's usage analytics
2. **Documentation Search** - Searches Confluence for existing documentation  
3. **Metadata Collection** - Gathers comprehensive table and column metadata
4. **Granularity Analysis** - AI-powered detection of data granularity and patterns
5. **AI Enhancement** - Generates business context using GPT-4o-mini
6. **Report Generation** - Renders structured markdown documentation

#### Granularity Analysis Engine

The system includes an intelligent granularity analysis engine that determines what each row represents:

![Granularity Analysis Flow](local_tools/table_context_agent/granularity_analysis_flow.png)

**Key Features:**
- **Performance-Aware Processing** - Lightweight analysis for massive tables (>10B rows)
- **AI-Powered Predictions** - Uses LLM to predict entity and time columns
- **Pattern Recognition** - Detects SCDs, event logs, status tracking, and more
- **Business Context Generation** - Explains complex patterns in user-friendly language

## Context Management System

The system uses a sophisticated **dual-table hybrid search** approach combining:

### 1. Document Categories

Documents are automatically categorized based on location:

- **`table_context`** - Snowflake table documentation (`context/snowflake-table-context/`)
- **`pod_queries`** - Validated master SQL queries (`context/pod-level-validated-master-queries/`)
- **`user_context`** - User-specific context documents (`context/user-context/`)
- **`experiment_readouts`** - Experiment analysis documents (`context/experiment-readouts/`)
- **`deep_dives`** - Deep dive analysis documents (`context/deep-dives/`)

### 2. Hybrid Search Algorithm

The search combines two approaches:

1. **BM25 (Keyword Search)**: Fast text matching using Snowflake's `CONTAINS` function
2. **Semantic Search**: Cosine similarity between query and document embeddings using BGE-small-en-v1.5

**Final score** = `(0.3 × BM25_score) + (0.7 × Embedding_score)`

### 3. Document Processing Pipeline

Documents are processed through:
1. **Document Processor** - Scans context folder, extracts metadata, chunks large documents
2. **BGE Embeddings** - Generates 384-dimensional embeddings using BGE-small-en-v1.5 model
3. **BM25 Preprocessing** - Tokenizes and preprocesses text for keyword search
4. **Snowflake Storage** - Uploads to `proddb.fionafan.document_index` table

### 4. Snowflake Storage Schema

Documents are stored in `proddb.fionafan.document_index` with:

```sql
CREATE TABLE document_index (
    document_id VARCHAR(64),
    file_path VARCHAR(1000),
    content TEXT,
    category VARCHAR(50),
    embedding ARRAY,           -- 384-dim BGE vectors
    bm25_tokens ARRAY,        -- Preprocessed tokens
    database_name VARCHAR(100), -- For table context
    schema_name VARCHAR(100),   -- For table context
    table_name VARCHAR(100),    -- For table context
    -- ... additional metadata
)
```

### 5. Setting Up Document Indexing

```bash
# Index all documents for hybrid search
python local_tools/document_indexer/index_documents_dual.py

# Clear and reindex
python local_tools/document_indexer/index_documents_dual.py --clear-table
```

## Architecture

The system is organized into several key layers:

```
┌─────────────────────┐
│   MCP Client        │  ← Cursor IDE
│   (Cursor)          │
└─────────┬───────────┘
          │ MCP Protocol
┌─────────▼───────────┐
│   FastMCP Server    │  ← src/cursor_analytics_mcp/server.py
│   (Tool Registry)   │
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│   Core Tools        │  ← local_tools/ modules
│   - Snowflake Ops   │
│   - Query Search    │
│   - Curie Export    │
│   - Google Docs     │
│   - Context Search  │
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│   Data Sources      │
│   - Snowflake DW    │
│   - Indexed Documents │
└─────────────────────┘
```

### Key Components

- **MCP Server** (`src/cursor_analytics_mcp/server.py`): FastMCP-based server with tool registry
- **Snowflake Integration** (`utils/snowflake_connection.py`): Multi-backend query execution
- **Document Indexing** (`local_tools/document_indexer/`): BGE embeddings + BM25 hybrid search
- **Context Management** (`context/`): Organized document repositories
- **Tool Modules** (`local_tools/`): Specialized functionality modules


### File Structure

```
cursor-analytics-mcp/
├── src/cursor_analytics_mcp/    # MCP server implementation
├── local_tools/                 # Tool implementations
│   ├── curie_export/           # Curie experiment analysis
│   ├── document_indexer/       # Hybrid search system
│   ├── google_doc_crawler/     # Google Docs integration
│   ├── sql_to_sheets/          # Direct SQL→Sheets export
│   └── table_context_agent/    # Table documentation
├── utils/                      # Core utilities
│   ├── snowflake_connection.py # Snowflake integration
│   └── logger.py               # Logging setup
├── context/                    # Document repositories
│   ├── snowflake-table-context/
│   ├── user-context/
│   ├── experiment-readouts/
│   ├── deep-dives/
│   └── pod-level-validated-master-queries/
├── config/                     # Configuration files
└── user-analysis/             # Analysis outputs
```

## Usage Examples

### Basic Snowflake Query

```python
# Execute a simple query
result = execute_snowflake_query(
    "SELECT COUNT(*) as user_count FROM dimension_users WHERE active = true"
)
```

### Find Table Usage Patterns

```python
# Find how a table is commonly used
queries = search_queries_by_table_name("fact_deliveries", limit=5)
```

### Export Analysis to Google Sheets

```python
# Create analysis and export to sheets
export_url = execute_sql_and_upload_to_google_sheet(
    query="""
    SELECT 
        date_trunc('month', delivery_date) as month,
        COUNT(*) as delivery_count,
        AVG(delivery_time_minutes) as avg_delivery_time
    FROM fact_deliveries 
    WHERE delivery_date >= '2024-01-01'
    GROUP BY 1
    ORDER BY 1
    """,
    tab_name="Monthly_Delivery_Metrics",
    spreadsheet_title="Q1 2024 Delivery Analysis"
)
```

### Smart Context Search

```python
# Find relevant table documentation
tables = fetch_table_context("user engagement metrics", top_k=3)

# Find validated queries
queries = fetch_pod_queries("conversion funnel analysis", top_k=2)

# Search experiment results
experiments = fetch_experiment_readouts("iOS conversion test", top_k=5)
```

### Curie Experiment Analysis

```python
# Get experiment metadata first
metadata = curie_get_metadata("ios_checkout_experiment_2024")

# Export results to sheets
export_url = export_curie_experiment_to_sheet(
    experiment_name="ios_checkout_experiment_2024",
    primary_metrics=["conversion_rate", "revenue_per_user"],
    secondary_metrics=["session_duration", "cart_abandonment"],
    share_email="team@company.com"
)
```

## Troubleshooting

### Snowflake Connection Issues

```bash
# Test connection
python -c "from utils.snowflake_connection import SnowflakeHook; hook = SnowflakeHook(); hook.connect(); print('Success!')"

# Check credentials
env | grep SNOWFLAKE
```

### Google API Issues

```bash
# Verify credentials file
cat $GOOGLE_SHEET_CREDENTIALS_FILE | jq .type  # Should show "service_account"

# Test permissions
python -c "from local_tools.curie_export.config import get_service_account_file; print(get_service_account_file())"
```

### Document Indexing Issues

```bash
# Rebuild document index
python local_tools/document_indexer/index_documents_dual.py --clear-table

# Test BGE model
python -c "from local_tools.document_indexer.embedding_generator import BGEEmbeddingGenerator; gen = BGEEmbeddingGenerator(); print('Model loaded:', gen.load_model())"
```

### Performance Optimization

- **Spark**: For large datasets, use `method="spark"` in queries
- **Batch Processing**: Use batch operations for multiple document conversions
- **Connection Pooling**: Reuse Snowflake connections with context managers
- **Model Caching**: BGE embeddings are cached locally to avoid reprocessing

---

**Built with ❤️ for data-driven analytics at scale**
