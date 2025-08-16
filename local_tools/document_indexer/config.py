"""
Configuration for document indexing system
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from cursor-analytics-mcp/config/.env
# Navigate up from local_tools/document_indexer/ to project root, then to config/
env_path = Path(__file__).parent.parent.parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

# Model configuration
BGE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
BGE_MODEL_LOCAL_PATH = Path(__file__).parent / "models" / "bge-small-en-v1.5"

# Document processing configuration
CHUNK_SIZE = 1000  # Characters per chunk for large documents
CHUNK_OVERLAP = 200  # Overlap between chunks
SUPPORTED_EXTENSIONS = ['.md', '.sql', '.txt', '.json', '.yaml', '.yml']

# Snowflake configuration (now configurable via .env)
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "proddb")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "fionafan")
DOCUMENT_TABLE = os.getenv("DOCUMENT_INDEX_TABLE", "document_index_community")
CHUNK_TABLE = os.getenv("CHUNK_INDEX_TABLE", "chunk_index_community")

# GitHub configuration
GITHUB_REPO = os.getenv("GITHUB_REPO", "jfan-nux/cursor-analytics-mcp")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

# Context categories mapping - enhanced for community content
CONTEXT_CATEGORIES = {
    "snowflake-table-context": "table_context",
    "pod-level-validated-master-queries": "pod_queries", 
    "user-context": "user_context",
    "deep-dives": "deep_dives",
    "experiment-readouts": "experiment_readouts",
    # Legacy categories
    "analysis-context": "analysis_context",
    "training-materials": "training_materials",
    "doordash-etl": "doordash_etl",
    "query_search": "query_search",
    "logistics": "logistics"
}

# Content type mapping
CONTENT_TYPE_MAPPING = {
    '.md': 'markdown',
    '.sql': 'sql', 
    '.json': 'json',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.txt': 'text',
    '.py': 'python',
    '.ipynb': 'notebook'
}

# BM25 preprocessing configuration
BM25_MIN_TOKEN_LENGTH = 2
BM25_STOPWORDS = {
    'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
    'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
    'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
    'from', 'up', 'out', 'down', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'just',
    'now', 'before', 'after', 'above', 'below', 'between', 'during', 'through'
}