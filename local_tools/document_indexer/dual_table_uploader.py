"""
Dual-table uploader for document indexing
Handles document_index and chunk_index tables separately
"""

import sys
from pathlib import Path
from typing import List, Dict, Optional
import pandas as pd
from datetime import datetime
import hashlib

# Handle imports for both direct execution and module import
try:
    from .config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, DOCUMENT_TABLE, CHUNK_TABLE, GITHUB_REPO, GITHUB_BRANCH
except ImportError:
    from config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, DOCUMENT_TABLE, CHUNK_TABLE, GITHUB_REPO, GITHUB_BRANCH

# Add utils to path for SnowflakeHook
try:
    from utils.snowflake_connection import SnowflakeHook
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from utils.snowflake_connection import SnowflakeHook


class DualTableUploader:
    """Handles uploading to separate document_index and chunk_index tables"""
    
    def __init__(self, database: str = SNOWFLAKE_DATABASE, schema: str = SNOWFLAKE_SCHEMA,
                 document_table: str = DOCUMENT_TABLE, chunk_table: str = CHUNK_TABLE):
        self.database = database
        self.schema = schema
        self.document_table = document_table
        self.chunk_table = chunk_table
        self.document_full_table = f"{database}.{schema}.{document_table}"
        self.chunk_full_table = f"{database}.{schema}.{chunk_table}"
        self.hook = None
        
    def get_snowflake_hook(self) -> Optional[SnowflakeHook]:
        """Get Snowflake connection hook with correct database/schema context"""
        try:
            if not self.hook:
                self.hook = SnowflakeHook(
                    database=self.database,
                    schema=self.schema
                )
            return self.hook
        except Exception as e:
            print(f"Error connecting to Snowflake: {e}")
            return None
    
    def create_document_table(self) -> bool:
        """Create the document_index table"""
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        # Drop existing table first
        try:
            hook.query_without_result(f"DROP TABLE IF EXISTS {self.document_full_table}")
            print(f"Dropped existing table {self.document_full_table}")
        except Exception as e:
            print(f"Note: Could not drop table (may not exist): {e}")
        
        create_table_sql = f"""
        CREATE TABLE {self.document_full_table} (
            -- Document Identity & Metadata
            document_id VARCHAR(64) PRIMARY KEY,
            document_hash VARCHAR(64) NOT NULL,
            relative_path TEXT NOT NULL,
            file_path TEXT,
            file_name VARCHAR(255),
            file_stem VARCHAR(255),
            file_extension VARCHAR(10),
            category VARCHAR(50),
            subcategory VARCHAR(200),
            document_title VARCHAR(500),
            content_type VARCHAR(50),
            
            -- GitHub Integration
            github_repo VARCHAR(200),
            github_branch VARCHAR(100) DEFAULT 'main',
            github_commit_sha VARCHAR(40),
            github_pr_number INTEGER,
            github_file_url TEXT,
            github_author VARCHAR(100),
            github_commit_message TEXT,
            
            -- Document Versioning & Lifecycle
            document_version INTEGER DEFAULT 1,
            is_latest_version BOOLEAN DEFAULT TRUE,
            superseded_at TIMESTAMP,
            change_type VARCHAR(20) DEFAULT 'created',
            
            -- Document Content & Summary
            full_content TEXT,
            chunk_count INTEGER DEFAULT 1,
            file_size INTEGER,
            last_modified TIMESTAMP,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            indexed_by VARCHAR(50) DEFAULT 'local',
            
            -- Legacy Schema Support (Document-level)
            database_name VARCHAR(100),
            schema_name VARCHAR(100),
            table_name VARCHAR(100),
            query_name VARCHAR(200),
            query_type VARCHAR(50),
            referenced_tables ARRAY
        )
        """
        
        try:
            hook.query_without_result(create_table_sql)
            print(f"Table {self.document_full_table} created/verified successfully")
            return True
        except Exception as e:
            print(f"Error creating document table: {e}")
            return False
    
    def create_chunk_table(self) -> bool:
        """Create the chunk_index table"""
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        # Drop existing table first
        try:
            hook.query_without_result(f"DROP TABLE IF EXISTS {self.chunk_full_table}")
            print(f"Dropped existing table {self.chunk_full_table}")
        except Exception as e:
            print(f"Note: Could not drop table (may not exist): {e}")
        
        create_table_sql = f"""
        CREATE TABLE {self.chunk_full_table} (
            -- Chunk Identity
            chunk_id VARCHAR(64) PRIMARY KEY,
            document_id VARCHAR(64) NOT NULL,
            chunk_hash VARCHAR(64) NOT NULL,
            
            -- Chunk Content & Position
            content TEXT NOT NULL,
            content_length INTEGER,
            chunk_start INTEGER,
            chunk_end INTEGER,
            
            -- Search & ML Features
            bm25_text TEXT,
            bm25_tokens ARRAY,
            embedding ARRAY,
            embedding_dim INTEGER,
            
            -- Foreign Key to document_index table
            FOREIGN KEY (document_id) REFERENCES {self.document_full_table}(document_id)
        )
        """
        
        try:
            hook.query_without_result(create_table_sql)
            print(f"Table {self.chunk_full_table} created/verified successfully")
            return True
        except Exception as e:
            print(f"Error creating chunk table: {e}")
            return False
    
    def create_tables(self) -> bool:
        """Create both tables"""
        print("🏗️  Creating document and chunk tables...")
        
        # Create document table first (parent)
        if not self.create_document_table():
            return False
        
        # Create chunk table second (child with FK)
        if not self.create_chunk_table():
            return False
        
        print("✅ Both tables created successfully")
        return True
    
    def clear_tables(self) -> bool:
        """Clear both tables"""
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        try:
            # Clear child table first due to FK constraint
            hook.query_without_result(f"DELETE FROM {self.chunk_full_table}")
            hook.query_without_result(f"DELETE FROM {self.document_full_table}")
            print(f"Cleared both tables")
            return True
        except Exception as e:
            print(f"Error clearing tables: {e}")
            return False
    
    def prepare_document_record(self, chunks: List[Dict]) -> Dict:
        """Prepare a document record from the first chunk (document-level data)"""
        if not chunks:
            return {}
        
        first_chunk = chunks[0]
        relative_path = first_chunk.get('relative_path', '')
        
        # Generate document ID from relative path
        document_id = hashlib.sha256(relative_path.encode('utf-8')).hexdigest()
        
        # Create GitHub URL
        github_file_url = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/context/{relative_path}"
        
        # Concatenate all chunk content to create full document content
        full_content = '\n\n'.join([chunk.get('content', '') for chunk in chunks])
        
        return {
            'DOCUMENT_ID': document_id,
            'DOCUMENT_HASH': first_chunk.get('document_hash', ''),
            'RELATIVE_PATH': relative_path,
            'FILE_PATH': first_chunk.get('file_path', ''),
            'FILE_NAME': first_chunk.get('file_name', ''),
            'FILE_STEM': first_chunk.get('file_stem', ''),
            'FILE_EXTENSION': first_chunk.get('file_extension', ''),
            'CATEGORY': first_chunk.get('category', 'general'),
            'SUBCATEGORY': first_chunk.get('subcategory'),
            'DOCUMENT_TITLE': first_chunk.get('document_title'),
            'CONTENT_TYPE': first_chunk.get('content_type', 'unknown'),
            'FULL_CONTENT': full_content,
            'GITHUB_REPO': GITHUB_REPO,
            'GITHUB_BRANCH': GITHUB_BRANCH,
            'GITHUB_FILE_URL': github_file_url,
            'GITHUB_COMMIT_SHA': None,
            'GITHUB_PR_NUMBER': None,
            'GITHUB_AUTHOR': None,
            'GITHUB_COMMIT_MESSAGE': None,
            'DOCUMENT_VERSION': 1,
            'IS_LATEST_VERSION': True,
            'CHANGE_TYPE': 'created',
            'CHUNK_COUNT': len(chunks),
            'FILE_SIZE': first_chunk.get('file_size', 0),
            'LAST_MODIFIED': first_chunk.get('last_modified'),
            'PROCESSED_AT': datetime.now().isoformat(),
            'INDEXED_BY': 'local',
            'DATABASE_NAME': first_chunk.get('database'),
            'SCHEMA_NAME': first_chunk.get('schema'),
            'TABLE_NAME': first_chunk.get('table_name'),
            'QUERY_NAME': first_chunk.get('query_name'),
            'QUERY_TYPE': first_chunk.get('query_type'),
            'REFERENCED_TABLES': first_chunk.get('referenced_tables', [])
        }
    
    def prepare_chunk_record(self, chunk: Dict, document_id: str) -> Dict:
        """Prepare a chunk record"""
        chunk_content = chunk.get('content', '')
        chunk_id_base = f"{document_id}_{chunk.get('chunk_id', 0)}"
        chunk_hash = hashlib.sha256(chunk_id_base.encode('utf-8')).hexdigest()
        
        return {
            'CHUNK_ID': chunk_hash,
            'DOCUMENT_ID': document_id,
            'CHUNK_HASH': chunk_hash,
            'CONTENT': chunk_content,
            'CONTENT_LENGTH': len(chunk_content),
            'CHUNK_START': chunk.get('chunk_start', 0),
            'CHUNK_END': chunk.get('chunk_end', 0),
            'BM25_TEXT': chunk.get('bm25_text', ''),
            'BM25_TOKENS': chunk.get('bm25_tokens', []),
            'EMBEDDING': chunk.get('embedding', []),
            'EMBEDDING_DIM': chunk.get('embedding_dim', 0)
        }
    
    def upload_documents_and_chunks(self, documents_chunks: Dict[str, List[Dict]], batch_size: int = 100) -> bool:
        """
        Upload documents and their chunks to the two-table structure
        
        Args:
            documents_chunks: Dict mapping document_id -> list of chunks
            batch_size: Batch size for uploads
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return False
        
        if not documents_chunks:
            print("No documents to upload")
            return True
        
        # Create tables if needed
        if not self.create_tables():
            return False
        
        try:
            print(f"📄 Uploading {len(documents_chunks)} documents and their chunks...")
            
            # Prepare document records
            document_records = []
            chunk_records = []
            
            for doc_chunks in documents_chunks.values():
                if not doc_chunks:
                    continue
                
                # Prepare document record
                doc_record = self.prepare_document_record(doc_chunks)
                document_records.append(doc_record)
                document_id = doc_record['DOCUMENT_ID']
                
                # Prepare chunk records
                for chunk in doc_chunks:
                    chunk_record = self.prepare_chunk_record(chunk, document_id)
                    chunk_records.append(chunk_record)
            
            # Upload documents first
            print(f"📄 Uploading {len(document_records)} document records...")
            doc_df = pd.DataFrame(document_records)
            hook.write_to_snowflake(df=doc_df, table_name=self.document_table, mode='append')
            print(f"✅ Uploaded {len(document_records)} documents")
            
            # Upload chunks in batches
            print(f"📝 Uploading {len(chunk_records)} chunk records...")
            for i in range(0, len(chunk_records), batch_size):
                batch = chunk_records[i:i + batch_size]
                batch_df = pd.DataFrame(batch)
                hook.write_to_snowflake(df=batch_df, table_name=self.chunk_table, mode='append')
                print(f"Uploaded chunk batch {i//batch_size + 1}: {len(batch)} records")
            
            print(f"✅ Successfully uploaded {len(document_records)} documents and {len(chunk_records)} chunks")
            return True
            
        except Exception as e:
            print(f"❌ Error uploading documents and chunks: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_table_stats(self) -> Optional[Dict]:
        """Get statistics for both tables"""
        hook = self.get_snowflake_hook()
        if not hook:
            return None
        
        try:
            doc_stats = hook.query_snowflake(f"SELECT COUNT(*) as doc_count FROM {self.document_full_table}")
            chunk_stats = hook.query_snowflake(f"SELECT COUNT(*) as chunk_count FROM {self.chunk_full_table}")
            
            return {
                'documents': doc_stats.iloc[0, 0],
                'chunks': chunk_stats.iloc[0, 0]
            }
        except Exception as e:
            print(f"Error getting table stats: {e}")
            return None
