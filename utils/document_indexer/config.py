"""
Configuration for document indexing system
"""

import os
from pathlib import Path

# Model configuration
BGE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
BGE_MODEL_LOCAL_PATH = Path(__file__).parent / "models" / "bge-small-en-v1.5"

# Document processing configuration
CHUNK_SIZE = 1000  # Characters per chunk for large documents
CHUNK_OVERLAP = 200  # Overlap between chunks
SUPPORTED_EXTENSIONS = ['.md', '.sql', '.txt', '.json', '.yaml', '.yml']

# Snowflake configuration
SNOWFLAKE_DATABASE = "proddb"
SNOWFLAKE_SCHEMA = "fionafan"
SNOWFLAKE_TABLE = "document_index"

# Context categories mapping
CONTEXT_CATEGORIES = {
    "analysis-context/snowflake-table-context": "table_context",
    "pod-level-validated-master-queries": "pod_queries", 
    "user-context": "user_context",
    "analysis-context": "analysis_context",
    "logistics": "logistics",
    "training-materials": "training_materials",
    "doordash-etl": "doordash_etl",
    "query_search": "query_search"
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