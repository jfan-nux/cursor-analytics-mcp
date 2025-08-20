# Document Indexer for Cursor Analytics MCP

This module provides hybrid search functionality combining BM25 and semantic embeddings using BGE (Beijing Academy of Artificial Intelligence General Embedding) models.

## Overview

The document indexer processes all documents in the `context/` folder, extracts metadata, generates embeddings using BGE-small-en-v1.5, and uploads everything to a Snowflake table for fast hybrid search.

## Components

### 1. Document Processor (`document_processor.py`)
- Scans context folder for supported file types (`.md`, `.sql`, `.txt`, `.json`, `.yaml`, `.yml`)
- Extracts metadata including category, file info, and content-specific metadata
- Chunks large documents for better search performance
- Preprocesses text for BM25 search

### 2. Embedding Generator (`embedding_generator.py`)
- Downloads and manages BGE-small-en-v1.5 model from Hugging Face
- Generates normalized embeddings for semantic search
- Caches embeddings to avoid reprocessing

### 3. Dual Table Uploader (`dual_table_uploader.py`)
- Creates and manages document index tables in Snowflake
- Uploads processed documents with embeddings in batches
- Provides table statistics and management

### 4. Dual Table Hybrid Search (`dual_table_search.py`)
- Combines BM25 (keyword) and embedding (semantic) search
- Queries Snowflake tables for fast retrieval
- Returns ranked results with relevance scores

## Setup

### Install Dependencies
Dependencies are now included in the main project `pyproject.toml`. Install with:
```bash
pip install -e .
```

### Configuration
The document indexer uses the following environment variables (configured via the main MCP server):
- `SNOWFLAKE_*` - Snowflake connection parameters
- `DOCUMENT_INDEX_TABLE` - Target table name (optional, defaults to `document_index`)
- `CHUNK_INDEX_TABLE` - Target chunk table name (optional, defaults to `chunk_index`)

### Required packages (now in pyproject.toml):
- `sentence-transformers>=2.2.0` - For BGE embeddings
- `torch>=1.9.0` - PyTorch backend
- `transformers>=4.21.0` - Hugging Face transformers
- `numpy>=1.24.0` - Numerical operations
- `pandas>=2.2.0` - Data manipulation
- `rank-bm25>=0.2.2` - BM25 implementation

## Usage

### 1. Index Documents
```bash
# Full indexing pipeline
python local_tools/document_indexer/index_documents_dual.py

# Clear existing table and reindex
python local_tools/document_indexer/index_documents_dual.py --clear-table

# Save processed documents to JSON for inspection
python local_tools/document_indexer/index_documents_dual.py --save-json processed_docs.json

# Skip embeddings (for testing)
python local_tools/document_indexer/index_documents_dual.py --skip-embeddings

# Run quick test
python local_tools/document_indexer/index_documents_dual.py test
```

### 2. Use Search Functions in MCP Server

The indexer provides five MCP tools for hybrid search:

#### `fetch_table_context(query, top_k=5, team=None, write_to_local=False)`
Search Snowflake table documentation:
```python
# Example queries:
"user dimensions table"
"delivery facts and metrics"
"consumer device settings"
```

#### `fetch_pod_queries(query, top_k=3, team=None)`  
Search validated master SQL queries:
```python
# Example queries:
"pricing analysis"
"affordability metrics" 
"delivery performance"
```

#### `fetch_user_context(query, top_k=5, team=None, write_to_local=False)`
Search user-specific context documents:
```python
# Example queries:
"notification analysis"
"user behavior patterns"
"experimental setup"
```

#### `fetch_experiment_readouts(query, top_k=5, team=None, write_to_local=False)`
Search experiment readout documents:
```python
# Example queries:
"iOS conversion test"
"checkout funnel experiment"
"mobile app experiment"
```

#### `fetch_deep_dives(query, top_k=5, team=None, write_to_local=False)`
Search deep dive analysis documents:
```python
# Example queries:
"MAU analysis"
"user retention study"
"experiment insights"
```

## Database Schema

The indexer creates a document index table with the following structure:

```sql
CREATE TABLE {database}.{schema}.document_index (
    -- Primary identifiers
    document_id VARCHAR(64) NOT NULL,
    file_hash VARCHAR(32) NOT NULL,
    chunk_id INTEGER NOT NULL,
    
    -- File information
    file_path VARCHAR(1000) NOT NULL,
    relative_path VARCHAR(500) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_stem VARCHAR(255) NOT NULL,
    file_extension VARCHAR(10),
    
    -- Content
    content TEXT NOT NULL,
    content_length INTEGER,
    
    -- Categorization
    category VARCHAR(50) NOT NULL,
    
    -- Search preprocessing
    bm25_text TEXT,
    bm25_tokens ARRAY,
    
    -- Embeddings (384-dimensional BGE vectors)
    embedding ARRAY,
    embedding_dim INTEGER,
    
    -- Table-specific metadata
    database_name VARCHAR(100),
    schema_name VARCHAR(100), 
    table_name VARCHAR(100),
    
    -- Query-specific metadata
    query_name VARCHAR(255),
    query_type VARCHAR(20),
    referenced_tables ARRAY,
    
    -- File metadata
    file_size INTEGER,
    last_modified TIMESTAMP,
    processed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    
    PRIMARY KEY (document_id, chunk_id)
)
```

## Document Categories

The indexer automatically categorizes documents based on their location:

- `table_context` - Snowflake table documentation (`context/snowflake-table-context/`)
- `pod_queries` - Validated master SQL queries (`context/pod-level-validated-master-queries/`)
- `user_context` - User-specific context documents (`context/user-context/`)
- `experiment_readouts` - Experiment analysis documents (`context/experiment-readouts/`)
- `deep_dives` - Deep dive analysis documents (`context/deep-dives/`)
- `analysis_context` - General analysis context (`context/analysis-context/`)

## Hybrid Search Algorithm

The search combines two approaches:

1. **BM25 (Keyword Search)**: Uses Snowflake's `CONTAINS` function for fast text matching
2. **Semantic Search**: Computes cosine similarity between query and document embeddings

Final score = `(bm25_weight * bm25_score) + (embedding_weight * embedding_score)`

Default weights:
- BM25: 0.3 (30%)
- Embedding: 0.7 (70%)

## Model Information

**BGE-small-en-v1.5** ([Hugging Face page](https://huggingface.co/BAAI/bge-small-en-v1.5)):
- 33.4M parameters (10x smaller than large model)
- 384-dimensional embeddings  
- Optimized for retrieval tasks
- Requires ~130MB disk space
- Fast inference on CPU, even faster with GPU

## Performance Considerations

- **Initial indexing**: Takes 5-15 minutes depending on document volume
- **Embedding generation**: ~100-500 docs/minute (GPU) or ~20-50 docs/minute (CPU)
- **Search latency**: < 1 second for most queries
- **Storage**: ~2KB per document chunk in Snowflake

## Troubleshooting

### Model Download Issues
```bash
# Manually download model
python -c "from local_tools.document_indexer.embedding_generator import BGEEmbeddingGenerator; BGEEmbeddingGenerator().download_model()"
```

### Snowflake Connection Issues
- Verify `utils/snowflake_connection.py` is configured correctly
- Check Snowflake credentials and permissions
- Ensure target database and schema exist and are accessible

### Memory Issues
- Reduce batch size in `index_documents_dual.py` script
- Use CPU instead of GPU if VRAM is limited
- Process documents in smaller batches

## Future Enhancements

- [ ] Support for additional embedding models
- [ ] Advanced BM25 implementation  
- [ ] Incremental indexing for changed documents
- [ ] Query expansion and reranking
- [ ] Cross-encoder reranking for top results