"""
Snowflake uploader for document index
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Optional
import pandas as pd
from datetime import datetime

# Add utils to path for importing snowflake connection
sys.path.append(str(Path(__file__).parent.parent))

try:
    from snowflake_connection import SnowflakeHook
except ImportError:
    print("Warning: Could not import SnowflakeHook. Make sure snowflake_connection.py is available.")
    SnowflakeHook = None

from .config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_TABLE


class DocumentIndexUploader:
    """Upload processed documents with embeddings to Snowflake"""
    
    def __init__(self, database: str = SNOWFLAKE_DATABASE, schema: str = SNOWFLAKE_SCHEMA, table: str = SNOWFLAKE_TABLE):
        self.database = database
        self.schema = schema
        self.table = table
        self.full_table_name = f"{database}.{schema}.{table}"
        self.hook = None
        
    def get_snowflake_hook(self) -> Optional[SnowflakeHook]:
        """Get Snowflake connection hook"""
        if SnowflakeHook is None:
            print("SnowflakeHook not available")
            return None
        
        try:
            if not self.hook:
                self.hook = SnowflakeHook()
            return self.hook
        except Exception as e:
            print(f"Error connecting to Snowflake: {e}")
            return None
    
    def create_table_if_not_exists(self) -> bool:
        """
        Create the document index table if it doesn't exist
        
        Returns:
            True if table exists or was created successfully
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        try:
            # Create database and schema if they don't exist
            hook.query(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            hook.query(f"CREATE SCHEMA IF NOT EXISTS {self.database}.{self.schema}")
            
            # Create table with all necessary columns
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {self.full_table_name} (
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
                
                -- Chunking information
                chunk_count INTEGER,
                chunk_start INTEGER,
                chunk_end INTEGER,
                
                -- Search preprocessing
                bm25_text TEXT,
                bm25_tokens ARRAY,
                
                -- Embeddings
                embedding ARRAY,
                embedding_dim INTEGER,
                
                -- Table-specific metadata (nullable)
                database_name VARCHAR(100),
                schema_name VARCHAR(100),
                table_name VARCHAR(100),
                
                -- Query-specific metadata (nullable)
                query_name VARCHAR(255),
                query_type VARCHAR(20),
                referenced_tables ARRAY,
                
                -- File metadata
                file_size INTEGER,
                last_modified TIMESTAMP,
                processed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
                
                -- Constraints
                PRIMARY KEY (document_id, chunk_id)
            )
            """
            
            hook.query(create_table_sql)
            print(f"Table {self.full_table_name} created/verified successfully")
            return True
            
        except Exception as e:
            print(f"Error creating table: {e}")
            return False
    
    def generate_document_id(self, chunk: Dict) -> str:
        """Generate a unique document ID based on file path and hash"""
        file_path = chunk.get('relative_path', '')
        file_hash = chunk.get('file_hash', '')
        return f"{file_hash[:16]}_{abs(hash(file_path)) % 1000000:06d}"
    
    def prepare_chunk_for_upload(self, chunk: Dict) -> Dict:
        """
        Prepare a document chunk for Snowflake upload
        
        Args:
            chunk: Document chunk dictionary
            
        Returns:
            Dictionary formatted for Snowflake
        """
        # Generate document ID
        document_id = self.generate_document_id(chunk)
        
        # Prepare base record
        record = {
            'DOCUMENT_ID': document_id,
            'FILE_HASH': chunk.get('file_hash', ''),
            'CHUNK_ID': chunk.get('chunk_id', 0),
            'FILE_PATH': chunk.get('file_path', ''),
            'RELATIVE_PATH': chunk.get('relative_path', ''),
            'FILE_NAME': chunk.get('file_name', ''),
            'FILE_STEM': chunk.get('file_stem', ''),
            'FILE_EXTENSION': chunk.get('file_extension', ''),
            'CONTENT': chunk.get('content', ''),
            'CONTENT_LENGTH': len(chunk.get('content', '')),
            'CATEGORY': chunk.get('category', 'general'),
            'CHUNK_COUNT': chunk.get('chunk_count', 1),
            'CHUNK_START': chunk.get('chunk_start', 0),
            'CHUNK_END': chunk.get('chunk_end', 0),
            'BM25_TEXT': chunk.get('bm25_text', ''),
            'BM25_TOKENS': chunk.get('bm25_tokens', []),
            'EMBEDDING': chunk.get('embedding', []),
            'EMBEDDING_DIM': chunk.get('embedding_dim', 0),
            'FILE_SIZE': chunk.get('file_size', 0),
            'LAST_MODIFIED': chunk.get('last_modified'),
            'PROCESSED_AT': chunk.get('processed_at', datetime.now().isoformat())
        }
        
        # Add table-specific metadata
        record.update({
            'DATABASE_NAME': chunk.get('database'),
            'SCHEMA_NAME': chunk.get('schema'),
            'TABLE_NAME': chunk.get('table_name')
        })
        
        # Add query-specific metadata
        record.update({
            'QUERY_NAME': chunk.get('query_name'),
            'QUERY_TYPE': chunk.get('query_type'),
            'REFERENCED_TABLES': chunk.get('referenced_tables', [])
        })
        
        return record
    
    def upload_chunks(self, chunks: List[Dict], batch_size: int = 100) -> bool:
        """
        Upload document chunks to Snowflake
        
        Args:
            chunks: List of processed document chunks
            batch_size: Number of records to upload in each batch
            
        Returns:
            True if upload successful
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        if not chunks:
            print("No chunks to upload")
            return True
        
        # Create table if needed
        if not self.create_table_if_not_exists():
            return False
        
        try:
            print(f"Uploading {len(chunks)} chunks to {self.full_table_name}")
            
            # Prepare records for upload
            records = [self.prepare_chunk_for_upload(chunk) for chunk in chunks]
            
            # Create DataFrame
            df = pd.DataFrame(records)
            
            # Upload in batches
            total_uploaded = 0
            for i in range(0, len(df), batch_size):
                batch_df = df.iloc[i:i + batch_size]
                
                # Upload batch using snowflake hook
                result = hook.upload_dataframe_to_table(
                    dataframe=batch_df,
                    table_name=self.table,
                    schema_name=self.schema,
                    database_name=self.database,
                    if_exists='replace' if i == 0 else 'append'  # Replace on first batch, append others
                )
                
                if result:
                    total_uploaded += len(batch_df)
                    print(f"Uploaded batch {i//batch_size + 1}: {len(batch_df)} records")
                else:
                    print(f"Failed to upload batch {i//batch_size + 1}")
                    return False
            
            print(f"Successfully uploaded {total_uploaded} document chunks")
            return True
            
        except Exception as e:
            print(f"Error uploading chunks: {e}")
            return False
    
    def clear_table(self) -> bool:
        """Clear the document index table"""
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        try:
            hook.query(f"DELETE FROM {self.full_table_name}")
            print(f"Cleared table {self.full_table_name}")
            return True
        except Exception as e:
            print(f"Error clearing table: {e}")
            return False
    
    def get_table_stats(self) -> Optional[Dict]:
        """Get statistics about the document index table"""
        hook = self.get_snowflake_hook()
        if not hook:
            return None
        
        try:
            stats_query = f"""
            SELECT 
                COUNT(*) as total_chunks,
                COUNT(DISTINCT file_hash) as unique_files,
                COUNT(DISTINCT category) as categories,
                AVG(content_length) as avg_content_length,
                MIN(processed_at) as first_processed,
                MAX(processed_at) as last_processed
            FROM {self.full_table_name}
            """
            
            result = hook.query(stats_query, return_results=True)
            if result and len(result) > 0:
                return dict(zip([col.name for col in result.description], result.fetchone()))
            
        except Exception as e:
            print(f"Error getting table stats: {e}")
        
        return None


def main():
    """Test the uploader"""
    uploader = DocumentIndexUploader()
    
    # Test table creation
    if uploader.create_table_if_not_exists():
        print("Table creation test passed")
        
        # Get table stats
        stats = uploader.get_table_stats()
        if stats:
            print("Current table stats:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
        else:
            print("Table is empty or stats unavailable")
    else:
        print("Table creation test failed")


if __name__ == "__main__":
    main()