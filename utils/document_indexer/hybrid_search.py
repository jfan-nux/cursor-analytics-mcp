"""
Hybrid search functionality combining BM25 and embedding similarity
"""

import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import numpy as np

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from snowflake_connection import SnowflakeHook
except ImportError:
    print("Warning: Could not import SnowflakeHook")
    SnowflakeHook = None

from .embedding_generator import BGEEmbeddingGenerator
from .config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_TABLE


class HybridSearcher:
    """Hybrid search using BM25 and embedding similarity"""
    
    def __init__(self, database: str = SNOWFLAKE_DATABASE, schema: str = SNOWFLAKE_SCHEMA, table: str = SNOWFLAKE_TABLE):
        self.database = database
        self.schema = schema
        self.table = table
        self.full_table_name = f"{database}.{schema}.{table}"
        self.hook = None
        self.embedding_generator = None
        
    def get_snowflake_hook(self) -> Optional[SnowflakeHook]:
        """Get Snowflake connection hook"""
        if SnowflakeHook is None:
            return None
        
        try:
            if not self.hook:
                self.hook = SnowflakeHook()
            return self.hook
        except Exception as e:
            print(f"Error connecting to Snowflake: {e}")
            return None
    
    def get_embedding_generator(self) -> Optional[BGEEmbeddingGenerator]:
        """Get embedding generator (lazy loading)"""
        if not self.embedding_generator:
            self.embedding_generator = BGEEmbeddingGenerator()
            if not self.embedding_generator.load_model():
                print("Warning: Could not load embedding model, semantic search disabled")
                return None
        return self.embedding_generator
    
    def calculate_cosine_similarity(self, query_embedding: np.ndarray, doc_embeddings: List[List[float]]) -> List[float]:
        """
        Calculate cosine similarity between query and document embeddings
        
        Args:
            query_embedding: Query embedding vector
            doc_embeddings: List of document embedding vectors
            
        Returns:
            List of cosine similarity scores
        """
        if not doc_embeddings:
            return []
        
        try:
            # Convert to numpy arrays
            query_vec = np.array(query_embedding)
            doc_vecs = np.array(doc_embeddings)
            
            # Calculate cosine similarity
            # Since embeddings are normalized, cosine similarity = dot product
            similarities = np.dot(doc_vecs, query_vec)
            
            return similarities.tolist()
            
        except Exception as e:
            print(f"Error calculating cosine similarity: {e}")
            return [0.0] * len(doc_embeddings)
    
    def search_documents(
        self, 
        query: str, 
        category: Optional[str] = None, 
        top_k: int = 5,
        bm25_weight: float = 0.3,
        embedding_weight: float = 0.7
    ) -> List[Dict]:
        """
        Perform hybrid search combining BM25 and embedding similarity
        
        Args:
            query: Search query string
            category: Optional category filter
            top_k: Number of top results to return
            bm25_weight: Weight for BM25 score (0.0 to 1.0)
            embedding_weight: Weight for embedding similarity (0.0 to 1.0)
            
        Returns:
            List of search results with scores
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return []
        
        try:
            # Build base query
            where_clause = ""
            if category:
                where_clause = f"WHERE category = '{category}'"
            
            # First, get documents with BM25 search using SQL CONTAINS
            # This is a simplified BM25 - Snowflake doesn't have full BM25 but CONTAINS is decent
            bm25_query = f"""
            SELECT 
                document_id,
                file_hash,
                chunk_id,
                relative_path,
                file_name,
                category,
                content,
                bm25_text,
                embedding,
                content_length,
                database_name,
                schema_name,
                table_name,
                query_name,
                query_type,
                referenced_tables,
                last_modified,
                processed_at,
                -- Simple text search score (not true BM25 but workable)
                CASE 
                    WHEN CONTAINS(UPPER(bm25_text), UPPER('{query}')) THEN 1.0
                    WHEN CONTAINS(UPPER(content), UPPER('{query}')) THEN 0.8
                    WHEN CONTAINS(UPPER(file_name), UPPER('{query}')) THEN 0.6
                    ELSE 0.0
                END as bm25_score
            FROM {self.full_table_name}
            {where_clause}
            ORDER BY bm25_score DESC
            LIMIT {top_k * 3}  -- Get more for re-ranking
            """
            
            result = hook.query(bm25_query, return_results=True)
            if not result:
                return []
            
            # Convert results to dictionaries
            columns = [col.name.lower() for col in result.description]
            documents = []
            for row in result.fetchall():
                doc = dict(zip(columns, row))
                documents.append(doc)
            
            if not documents:
                return []
            
            # Generate query embedding for semantic search
            embedding_generator = self.get_embedding_generator()
            query_embedding = None
            
            if embedding_generator:
                query_embedding = embedding_generator.generate_single_embedding(
                    query, 
                    query_prefix="Represent this sentence for searching relevant passages:"
                )
            
            # Calculate combined scores
            final_results = []
            for doc in documents:
                try:
                    # Get BM25 score
                    bm25_score = float(doc.get('bm25_score', 0.0))
                    
                    # Get embedding similarity score
                    embedding_score = 0.0
                    if query_embedding is not None and doc.get('embedding'):
                        try:
                            doc_embedding = doc['embedding']
                            if isinstance(doc_embedding, str):
                                # Parse JSON array if stored as string
                                import json
                                doc_embedding = json.loads(doc_embedding)
                            
                            similarities = self.calculate_cosine_similarity(query_embedding, [doc_embedding])
                            if similarities:
                                embedding_score = similarities[0]
                        except Exception as e:
                            print(f"Error processing embedding for doc {doc.get('document_id')}: {e}")
                            embedding_score = 0.0
                    
                    # Calculate combined score
                    combined_score = (bm25_weight * bm25_score) + (embedding_weight * embedding_score)
                    
                    # Add scores to document
                    doc['bm25_score'] = bm25_score
                    doc['embedding_score'] = embedding_score
                    doc['combined_score'] = combined_score
                    
                    final_results.append(doc)
                    
                except Exception as e:
                    print(f"Error processing document {doc.get('document_id', 'unknown')}: {e}")
                    continue
            
            # Sort by combined score and return top_k
            final_results.sort(key=lambda x: x['combined_score'], reverse=True)
            return final_results[:top_k]
            
        except Exception as e:
            print(f"Error in hybrid search: {e}")
            return []
    
    def search_table_context(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search table context documents"""
        return self.search_documents(query, category="table_context", top_k=top_k)
    
    def search_pod_queries(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search pod-level queries"""
        return self.search_documents(query, category="pod_queries", top_k=top_k)
    
    def search_user_context(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search user context documents"""
        return self.search_documents(query, category="user_context", top_k=top_k)
    
    def get_full_document_content(self, document_id: str) -> List[Dict]:
        """
        Get all chunks for a specific document ID to provide full context
        
        Args:
            document_id: The document ID to fetch all chunks for
            
        Returns:
            List of all chunks for the document, sorted by chunk_id
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return []
        
        try:
            query = f"""
            SELECT 
                document_id,
                file_hash,
                chunk_id,
                relative_path,
                file_name,
                category,
                content,
                chunk_count,
                chunk_start,
                chunk_end,
                database_name,
                schema_name,
                table_name,
                query_name,
                query_type,
                referenced_tables,
                last_modified,
                processed_at
            FROM {self.full_table_name}
            WHERE document_id = '{document_id}'
            ORDER BY chunk_id
            """
            
            result = hook.query(query, return_results=True)
            if not result:
                return []
            
            # Convert results to dictionaries
            columns = [col.name.lower() for col in result.description]
            chunks = []
            for row in result.fetchall():
                chunk = dict(zip(columns, row))
                chunks.append(chunk)
            
            return chunks
            
        except Exception as e:
            print(f"Error getting full document content: {e}")
            return []
    
    def format_search_results(self, results: List[Dict], query: str) -> str:
        """
        Format search results for display, including full document context
        
        Args:
            results: List of search result dictionaries
            query: Original search query
            
        Returns:
            Formatted string for display
        """
        if not results:
            return f"No results found for query: '{query}'"
        
        response = f"Search results for '{query}':\n\n"
        
        for i, result in enumerate(results, 1):
            # Basic info
            response += f"**{i}. {result.get('file_name', 'Unknown')}**\n"
            response += f"Path: {result.get('relative_path', 'Unknown')}\n"
            response += f"Category: {result.get('category', 'Unknown')}\n"
            
            # Scores
            response += f"Scores: BM25={result.get('bm25_score', 0):.3f}, "
            response += f"Embedding={result.get('embedding_score', 0):.3f}, "
            response += f"Combined={result.get('combined_score', 0):.3f}\n"
            
            # Category-specific info
            if result.get('database_name') and result.get('schema_name') and result.get('table_name'):
                response += f"Table: {result['database_name']}.{result['schema_name']}.{result['table_name']}\n"
            
            if result.get('query_name'):
                response += f"Query: {result['query_name']}\n"
            
            if result.get('query_type'):
                response += f"Query Type: {result['query_type']}\n"
            
            # Show matched chunk content first
            matched_content = result.get('content', '')
            chunk_info = ""
            if result.get('chunk_count', 1) > 1:
                chunk_info = f" (Chunk {result.get('chunk_id', 0) + 1}/{result.get('chunk_count', 1)})"
            
            if len(matched_content) > 500:
                matched_content = matched_content[:500] + "..."
            response += f"Matched Content{chunk_info}: {matched_content}\n\n"
            
            # Get and display full document content
            document_id = result.get('document_id')
            if document_id:
                try:
                    full_document_chunks = self.get_full_document_content(document_id)
                    
                    if full_document_chunks:
                        # Combine all chunks to reconstruct the full document
                        full_content = ""
                        for chunk in full_document_chunks:
                            chunk_content = chunk.get('content', '')
                            full_content += chunk_content
                            if not chunk_content.endswith('\n'):
                                full_content += '\n'
                        
                        response += f"**Full Document Content:**\n{full_content.strip()}\n\n"
                    else:
                        # Fallback to just the matched chunk if we can't get full document
                        response += f"**Full Content (chunk only):**\n{result.get('content', '')}\n\n"
                        
                except Exception as e:
                    print(f"Error getting full document for {document_id}: {e}")
                    # Fallback to just the matched chunk
                    response += f"**Content (matched chunk only):**\n{result.get('content', '')}\n\n"
            else:
                response += f"**Content:**\n{result.get('content', '')}\n\n"
            
            response += "---\n\n"  # Separator between results
        
        return response


def main():
    """Test the hybrid searcher"""
    searcher = HybridSearcher()
    
    # Test searches
    test_queries = [
        ("user analytics", "table_context"),
        ("pricing queries", "pod_queries"), 
        ("delivery metrics", None)
    ]
    
    for query, category in test_queries:
        print(f"\nTesting search: '{query}' in category '{category}'")
        results = searcher.search_documents(query, category=category, top_k=3)
        
        if results:
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result.get('file_name')} (score: {result.get('combined_score', 0):.3f})")
        else:
            print("No results found")


if __name__ == "__main__":
    main()