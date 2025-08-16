"""
Hybrid search functionality for dual-table structure (document_index + chunk_index)
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import numpy as np
import json

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from snowflake_connection import SnowflakeHook
except ImportError:
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent.parent))
        from utils.snowflake_connection import SnowflakeHook
    except ImportError:
        print("Warning: Could not import SnowflakeHook")
        SnowflakeHook = None

try:
    from .embedding_generator import BGEEmbeddingGenerator
    from .config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, DOCUMENT_TABLE, CHUNK_TABLE
except ImportError:
    from embedding_generator import BGEEmbeddingGenerator
    from config import SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, DOCUMENT_TABLE, CHUNK_TABLE


class DualTableHybridSearcher:
    """Hybrid search using BM25 and embedding similarity with dual-table structure"""
    
    def __init__(self, database: str = SNOWFLAKE_DATABASE, schema: str = SNOWFLAKE_SCHEMA,
                 document_table: str = DOCUMENT_TABLE, chunk_table: str = CHUNK_TABLE):
        self.database = database
        self.schema = schema
        self.document_table = document_table
        self.chunk_table = chunk_table
        self.document_full_table = f"{database}.{schema}.{document_table}"
        self.chunk_full_table = f"{database}.{schema}.{chunk_table}"
        self.hook = None
        self.embedding_generator = None
        
    def get_snowflake_hook(self) -> Optional[SnowflakeHook]:
        """Get Snowflake connection hook with correct database/schema context"""
        if SnowflakeHook is None:
            return None
        
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
    
    def extract_keywords(self, query: str) -> List[str]:
        """Extract meaningful keywords from a search query"""
        # Convert to uppercase for matching
        query_upper = query.upper()
        
        # Remove common stop words and extract words
        stopwords = {'THE', 'IS', 'FOR', 'OF', 'AND', 'OR', 'BUT', 'IN', 'ON', 'AT', 'TO', 'A', 'AN', 'WHAT', 'WHERE', 'HOW', 'WHEN', 'WHY'}
        
        # Extract words (alphanumeric sequences of 3+ characters)
        words = re.findall(r'\b[A-Z]{3,}\b', query_upper)
        
        # Filter out stop words and return unique keywords
        keywords = [word for word in words if word not in stopwords]
        return list(set(keywords))  # Remove duplicates
    
    def build_keyword_regex(self, keywords: List[str]) -> str:
        """Build a regex pattern for keyword matching"""
        if not keywords:
            return ''
        # Don't escape keywords since they're already clean, just join them
        return '(' + '|'.join(keywords) + ')'

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
    
    def search_documents_with_context(
        self, 
        query: str, 
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        top_k: int = 5,
        bm25_weight: float = 0.3,
        embedding_weight: float = 0.7,
        context_window: int = 2
    ) -> List[Dict]:
        """
        Enhanced hybrid search with context windows
        
        1. Filter documents first based on category/subcategory
        2. Join filtered documents to chunks
        3. Run hybrid search on chunks
        4. Return selected chunk + adjacent chunks (context window)
        
        Args:
            query: Search query string
            category: Optional category filter
            subcategory: Optional subcategory filter (team)
            top_k: Number of top results to return
            bm25_weight: Weight for BM25 score (0.0 to 1.0)
            embedding_weight: Weight for embedding similarity (0.0 to 1.0)
            context_window: Number of chunks before/after to include (default: 2)
            
        Returns:
            List of search results with context chunks
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return []
        
        try:
            # Step 1: Filter documents first
            doc_filter_conditions = []
            if category:
                doc_filter_conditions.append(f"category = '{category}'")
            if subcategory:
                doc_filter_conditions.append(f"subcategory = '{subcategory}'")
            
            doc_where_clause = ""
            if doc_filter_conditions:
                doc_where_clause = f"WHERE {' AND '.join(doc_filter_conditions)}"
            
            # Extract keywords from query
            keywords = self.extract_keywords(query)
            if not keywords:
                return []
            
            keyword_regex = self.build_keyword_regex(keywords)
            
            # Step 2: Get filtered documents and their chunks with hybrid search
            hybrid_search_query = f"""
            WITH filtered_documents AS (
                SELECT document_id, document_hash, chunk_count, full_content,
                       relative_path, file_name, category, subcategory, document_title,
                       content_type, github_file_url, github_branch, last_modified
                FROM {self.document_full_table}
                {doc_where_clause}
            ),
            filtered_chunks AS (
                SELECT 
                    fd.document_id,
                    fd.document_hash,
                    fd.chunk_count,
                    fd.full_content,
                    fd.relative_path,
                    fd.file_name,
                    fd.category,
                    fd.subcategory,
                    fd.document_title,
                    fd.content_type,
                    fd.github_file_url,
                    fd.github_branch,
                    fd.last_modified,
                    c.chunk_id,
                    c.chunk_hash,
                    c.content,
                    c.bm25_text,
                    c.embedding,
                    c.content_length,
                    c.chunk_start,
                    c.chunk_end,
                    -- Calculate BM25 score using dynamic keyword matching
                    (REGEXP_COUNT(UPPER(c.bm25_text), '{keyword_regex}') * 0.4 +
                     REGEXP_COUNT(UPPER(c.content), '{keyword_regex}') * 0.3 +
                     REGEXP_COUNT(UPPER(fd.document_title), '{keyword_regex}') * 0.2 +
                     REGEXP_COUNT(UPPER(fd.file_name), '{keyword_regex}') * 0.1) as bm25_score,
                    -- Add row number for chunk ordering within document
                    ROW_NUMBER() OVER (PARTITION BY fd.document_id ORDER BY c.chunk_start) as chunk_order
                FROM filtered_documents fd
                JOIN {self.chunk_full_table} c ON fd.document_id = c.document_id
            )
            SELECT *
            FROM filtered_chunks
            WHERE bm25_score > 0
            ORDER BY bm25_score DESC
            LIMIT {top_k * 3}  -- Get more for re-ranking with embeddings
            """
            
            result = hook.query_snowflake(hybrid_search_query)
            if result is None or result.empty:
                return []
            
            # Convert to dictionaries
            chunks = result.to_dict('records')
            
            if not chunks:
                return []
            
            # Step 3: Add semantic search scoring
            embedding_generator = self.get_embedding_generator()
            query_embedding = None
            
            if embedding_generator:
                query_embedding = embedding_generator.generate_single_embedding(query)
            
            # Calculate combined scores and add semantic similarity
            for chunk in chunks:
                semantic_score = 0.0
                
                if query_embedding is not None and chunk.get('embedding'):
                    try:
                        # Parse embedding from database (stored as JSON string)
                        doc_embedding = chunk['embedding']
                        if isinstance(doc_embedding, str):
                            # Parse JSON string to list
                            doc_embedding = json.loads(doc_embedding) if doc_embedding.startswith('[') else None
                        
                        if doc_embedding and isinstance(doc_embedding, list) and len(doc_embedding) > 1:
                            # Calculate cosine similarity
                            doc_emb_array = np.array(doc_embedding, dtype=float)
                            query_emb_array = np.array(query_embedding, dtype=float)
                            
                            # Normalize vectors
                            doc_norm = np.linalg.norm(doc_emb_array)
                            query_norm = np.linalg.norm(query_emb_array)
                            
                            if doc_norm > 0 and query_norm > 0:
                                semantic_score = np.dot(doc_emb_array, query_emb_array) / (doc_norm * query_norm)
                                semantic_score = max(0, semantic_score)  # Ensure non-negative
                    except Exception as e:
                        print(f"Error calculating cosine similarity: {e}")
                        semantic_score = 0.0
                
                # Combine BM25 and semantic scores
                bm25_score = float(chunk.get('bm25_score', 0.0))
                combined_score = (bm25_weight * bm25_score) + (embedding_weight * semantic_score)
                
                chunk['semantic_score'] = semantic_score
                chunk['combined_score'] = combined_score
            
            # Step 4: Re-rank by combined score and take top_k
            chunks.sort(key=lambda x: x['combined_score'], reverse=True)
            top_chunks = chunks[:top_k]
            
            # Step 5: Get context windows for each selected chunk
            results_with_context = []
            
            for selected_chunk in top_chunks:
                context_result = self._get_chunk_context_window(
                    hook, 
                    selected_chunk, 
                    context_window
                )
                results_with_context.append(context_result)
            
            return results_with_context
            
        except Exception as e:
            print(f"Error in enhanced hybrid search: {e}")
            return []

    def _get_chunk_context_window(self, hook: SnowflakeHook, selected_chunk: Dict, context_window: int = 2) -> Dict:
        """
        Get context window around a selected chunk (selected + preceding + following chunks)
        
        Args:
            hook: Snowflake connection hook
            selected_chunk: The main chunk that was found by search
            context_window: Number of chunks before/after to include
            
        Returns:
            Dictionary with selected chunk + context chunks + metadata
        """
        try:
            document_id = selected_chunk['document_id']
            chunk_count = selected_chunk['chunk_count'] 
            selected_chunk_order = selected_chunk['chunk_order']
            
            # If document has 5 or fewer chunks, return all chunks
            if chunk_count <= 5:
                context_query = f"""
                SELECT 
                    c.chunk_id,
                    c.chunk_hash,
                    c.content,
                    c.content_length,
                    c.chunk_start,
                    c.chunk_end,
                    ROW_NUMBER() OVER (ORDER BY c.chunk_start) as chunk_order
                FROM {self.chunk_full_table} c
                WHERE c.document_id = '{document_id}'
                ORDER BY c.chunk_start
                """
            else:
                # Get context window: selected chunk ± context_window
                start_order = max(1, selected_chunk_order - context_window)
                end_order = min(chunk_count, selected_chunk_order + context_window)
                
                context_query = f"""
                WITH ordered_chunks AS (
                    SELECT 
                        c.chunk_id,
                        c.chunk_hash,
                        c.content,
                        c.content_length,
                        c.chunk_start,
                        c.chunk_end,
                        ROW_NUMBER() OVER (ORDER BY c.chunk_start) as chunk_order
                    FROM {self.chunk_full_table} c
                    WHERE c.document_id = '{document_id}'
                )
                SELECT *
                FROM ordered_chunks
                WHERE chunk_order BETWEEN {start_order} AND {end_order}
                ORDER BY chunk_order
                """
            
            context_result = hook.query_snowflake(context_query)
            
            if context_result is None or context_result.empty:
                # Fallback to just the selected chunk
                context_chunks = [selected_chunk]
            else:
                context_chunks = context_result.to_dict('records')
            
            # Combine selected chunk metadata with context chunks
            result = {
                # Document-level metadata from selected chunk
                'document_id': selected_chunk['document_id'],
                'document_hash': selected_chunk['document_hash'], 
                'document_title': selected_chunk['document_title'],
                'relative_path': selected_chunk['relative_path'],
                'file_name': selected_chunk['file_name'],
                'category': selected_chunk['category'],
                'subcategory': selected_chunk['subcategory'],
                'content_type': selected_chunk['content_type'],
                'github_file_url': selected_chunk['github_file_url'],
                'github_branch': selected_chunk['github_branch'],
                'last_modified': selected_chunk['last_modified'],
                
                # Search-specific metadata
                'selected_chunk_id': selected_chunk['chunk_id'],
                'bm25_score': selected_chunk.get('bm25_score', 0.0),
                'semantic_score': selected_chunk.get('semantic_score', 0.0),
                'combined_score': selected_chunk.get('combined_score', 0.0),
                
                # Context information
                'chunk_count': chunk_count,
                'context_window_size': len(context_chunks),
                'is_full_document': chunk_count <= 5,
                
                # All chunks in context window
                'context_chunks': context_chunks,
                
                # Combined content from context window
                'context_content': '\n\n'.join([chunk['content'] for chunk in context_chunks]),
                
                # Full document content (if available)
                'full_content': selected_chunk.get('full_content', '')
            }
            
            return result
            
        except Exception as e:
            print(f"Error getting chunk context window: {e}")
            # Fallback to just the selected chunk
            return {
                'document_id': selected_chunk.get('document_id'),
                'document_title': selected_chunk.get('document_title'),
                'github_file_url': selected_chunk.get('github_file_url'),
                'github_branch': selected_chunk.get('github_branch'),
                'category': selected_chunk.get('category'),
                'subcategory': selected_chunk.get('subcategory'),
                'selected_chunk_id': selected_chunk.get('chunk_id'),
                'context_chunks': [selected_chunk],
                'context_content': selected_chunk.get('content', ''),
                'error': str(e)
            }

    def search_documents(
        self, 
        query: str, 
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        top_k: int = 5,
        bm25_weight: float = 0.3,
        embedding_weight: float = 0.7
    ) -> List[Dict]:
        """
        Perform hybrid search combining BM25 and embedding similarity
        
        Args:
            query: Search query string
            category: Optional category filter
            subcategory: Optional subcategory filter (team)
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
            # Build WHERE clause with category and subcategory filtering
            where_conditions = []
            if category:
                where_conditions.append(f"d.category = '{category}'")
            if subcategory:
                where_conditions.append(f"d.subcategory = '{subcategory}'")
            
            where_clause = ""
            if where_conditions:
                where_clause = f"WHERE {' AND '.join(where_conditions)}"
            
            # Enhanced BM25 search using SQL CONTAINS with dual-table join
            bm25_query = f"""
            SELECT 
                d.document_id,
                d.document_hash,
                c.chunk_id,
                c.chunk_hash,
                d.relative_path,
                d.file_name,
                d.file_path,
                d.category,
                d.subcategory,
                d.document_title,
                d.content_type,
                c.content,
                c.bm25_text,
                c.embedding,
                c.content_length,
                d.database_name,
                d.schema_name,
                d.table_name,
                d.query_name,
                d.query_type,
                d.referenced_tables,
                d.github_file_url,
                d.github_branch,
                d.github_commit_sha,
                d.last_modified,
                d.processed_at,
                -- Enhanced text search score with new fields
                CASE 
                    WHEN CONTAINS(UPPER(c.bm25_text), UPPER('{query}')) THEN 1.0
                    WHEN CONTAINS(UPPER(c.content), UPPER('{query}')) THEN 0.8
                    WHEN CONTAINS(UPPER(d.document_title), UPPER('{query}')) THEN 0.7
                    WHEN CONTAINS(UPPER(d.file_name), UPPER('{query}')) THEN 0.6
                    WHEN CONTAINS(UPPER(d.subcategory), UPPER('{query}')) THEN 0.5
                    ELSE 0.0
                END as bm25_score
            FROM {self.document_full_table} d
            JOIN {self.chunk_full_table} c ON d.document_id = c.document_id
            {where_clause}
            ORDER BY bm25_score DESC
            LIMIT {top_k * 3}  -- Get more for re-ranking
            """
            
            result = hook.query_snowflake(bm25_query)
            if result is None or result.empty:
                return []
            
            # Convert pandas DataFrame to dictionaries
            documents = result.to_dict('records')
            
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
                    
                    # Calculate embedding similarity if available
                    embedding_score = 0.0
                    if query_embedding is not None and doc.get('embedding'):
                        try:
                            doc_embedding = doc['embedding']
                            
                            # Parse embedding from database (stored as JSON string)
                            if isinstance(doc_embedding, str):
                                doc_embedding = json.loads(doc_embedding) if doc_embedding.startswith('[') else None
                            
                            if doc_embedding and isinstance(doc_embedding, list) and len(doc_embedding) > 1:
                                similarities = self.calculate_cosine_similarity(query_embedding, [doc_embedding])
                                embedding_score = similarities[0] if similarities else 0.0
                        except Exception as e:
                            print(f"Error calculating embedding similarity for chunk {doc.get('chunk_id', 'unknown')}: {e}")
                            embedding_score = 0.0
                    
                    # Combined score
                    combined_score = (bm25_weight * float(bm25_score)) + (embedding_weight * embedding_score)
                    
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
    
    def search_table_context(self, query: str, top_k: int = 5, team: Optional[str] = None, with_context: bool = True) -> List[Dict]:
        """
        Search table context documents
        
        Args:
            query: Search query
            top_k: Number of results to return
            team: Optional team/subcategory filter (e.g., 'growth/nux', 'edw/consumer')
            with_context: Whether to include context windows (default: True)
        """
        if with_context:
            return self.search_documents_with_context(query, category="table_context", subcategory=team, top_k=top_k)
        else:
            return self.search_documents(query, category="table_context", subcategory=team, top_k=top_k)
    
    def search_pod_queries(self, query: str, top_k: int = 5, team: Optional[str] = None) -> List[Dict]:
        """
        Search pod-level queries
        
        Args:
            query: Search query
            top_k: Number of results to return
            team: Optional team/subcategory filter (e.g., 'growth/nux', 'growth/pricing-and-affordability')
        """
        return self.search_documents(query, category="pod_queries", subcategory=team, top_k=top_k)
    
    def search_user_context(self, query: str, top_k: int = 5, team: Optional[str] = None) -> List[Dict]:
        """
        Search user context documents
        
        Args:
            query: Search query
            top_k: Number of results to return
            team: Optional team/subcategory filter (e.g., 'fiona.fan', 'team.lead')
        """
        return self.search_documents(query, category="user_context", subcategory=team, top_k=top_k)
    
    def search_experiment_readouts(self, query: str, top_k: int = 5, team: Optional[str] = None, with_context: bool = True) -> List[Dict]:
        """
        Search experiment readout documents
        
        Args:
            query: Search query
            top_k: Number of results to return
            team: Optional team/subcategory filter (e.g., 'growth/nux')
            with_context: Whether to include context windows (default: True)
        """
        if with_context:
            return self.search_documents_with_context(query, category="experiment_readouts", subcategory=team, top_k=top_k)
        else:
            return self.search_documents(query, category="experiment_readouts", subcategory=team, top_k=top_k)
    
    def search_deep_dives(self, query: str, top_k: int = 5, team: Optional[str] = None) -> List[Dict]:
        """
        Search deep dive analysis documents
        
        Args:
            query: Search query
            top_k: Number of results to return
            team: Optional team/subcategory filter (e.g., 'growth/nux')
        """
        return self.search_documents(query, category="deep_dives", subcategory=team, top_k=top_k)
    
    def get_full_document_content(self, document_id: str) -> List[Dict]:
        """
        Get all chunks for a specific document ID to provide full context
        
        Args:
            document_id: The document ID to fetch all chunks for
            
        Returns:
            List of all chunks for the document, sorted by chunk_start
        """
        hook = self.get_snowflake_hook()
        if not hook:
            return []
        
        try:
            query = f"""
            SELECT 
                d.document_id,
                d.document_hash,
                c.chunk_id,
                c.chunk_hash,
                d.relative_path,
                d.file_name,
                d.file_path,
                d.category,
                d.subcategory,
                d.document_title,
                d.content_type,
                c.content,
                d.chunk_count,
                c.chunk_start,
                c.chunk_end,
                d.database_name,
                d.schema_name,
                d.table_name,
                d.query_name,
                d.query_type,
                d.referenced_tables,
                d.github_file_url,
                d.github_branch,
                d.github_commit_sha,
                d.last_modified,
                d.processed_at
            FROM {self.document_full_table} d
            JOIN {self.chunk_full_table} c ON d.document_id = c.document_id
            WHERE d.document_id = '{document_id}'
            ORDER BY c.chunk_start
            """
            
            result = hook.query_snowflake(query)
            if result is None or result.empty:
                return []
            
            # Convert pandas DataFrame to dictionaries
            return result.to_dict('records')
            
        except Exception as e:
            print(f"Error getting full document content: {e}")
            return []
    
    def format_search_results(self, results: List[Dict], query: str) -> str:
        """Format search results for display"""
        if not results:
            return f"No results found for query: '{query}'"
        
        formatted = f"🔍 Search Results for: '{query}'\n"
        formatted += f"📊 Found {len(results)} results\n\n"
        
        for i, result in enumerate(results, 1):
            formatted += f"**Result {i}:**\n"
            formatted += f"📄 **{result.get('document_title', result.get('file_name', 'Unknown'))}**\n"
            formatted += f"📂 Category: {result.get('category', 'N/A')}"
            if result.get('subcategory'):
                formatted += f" | Team: {result.get('subcategory')}"
            formatted += "\n"
            formatted += f"🔗 [View on GitHub]({result.get('github_file_url', '#')})\n"
            formatted += f"📍 Path: `{result.get('relative_path', 'N/A')}`\n"
            
            # Add content preview (handle both context and regular results)
            if 'context_content' in result:
                # Enhanced search with context window
                context_size = result.get('context_window_size', 0)
                is_full_doc = result.get('is_full_document', False)
                context_info = "full document" if is_full_doc else f"{context_size} chunks"
                formatted += f"📝 **Content ({context_info}):**\n"
                
                content = result.get('context_content', '')
                if content:
                    preview = content[:5000] + "..." if len(content) > 5000 else content
                    formatted += f"```\n{preview}\n```\n"
            else:
                # Regular search result
                content = result.get('content', '')
                if content:
                    preview = content[:5000] + "..." if len(content) > 5000 else content
                    formatted += f"📝 **Content Preview:**\n```\n{preview}\n```\n"
            
            # Add relevance scores (handle different score keys)
            combined_score = result.get('combined_score', 0)
            bm25_score = result.get('bm25_score', 0)
            semantic_score = result.get('semantic_score', result.get('embedding_score', 0))
            
            formatted += f"🎯 **Relevance:** "
            formatted += f"Combined: {combined_score:.3f} "
            formatted += f"(BM25: {bm25_score:.3f}, "
            formatted += f"Semantic: {semantic_score:.3f})\n\n"
        
        return formatted
