"""
Embedding generation using BGE (Beijing Academy of Artificial Intelligence General Embedding) models
"""

import json
import os
import pickle
from pathlib import Path
from typing import List, Dict, Optional, Union
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    import torch
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    print("Warning: sentence-transformers not available. Install with: pip install sentence-transformers")
    EMBEDDINGS_AVAILABLE = False

from .config import BGE_MODEL_NAME, BGE_MODEL_LOCAL_PATH


class BGEEmbeddingGenerator:
    """Generate embeddings using BGE models from Hugging Face"""
    
    def __init__(self, model_name: str = BGE_MODEL_NAME, local_path: Optional[Path] = None):
        self.model_name = model_name
        self.local_path = local_path or BGE_MODEL_LOCAL_PATH
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu" if EMBEDDINGS_AVAILABLE else None
        
    def download_model(self) -> bool:
        """
        Download the BGE model if not already available locally
        
        Returns:
            True if model is available, False otherwise
        """
        if not EMBEDDINGS_AVAILABLE:
            print("sentence-transformers not available. Cannot download model.")
            return False
        
        try:
            # Create local path if it doesn't exist
            self.local_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"Downloading BGE model {self.model_name}...")
            
            # Download and save model locally
            model = SentenceTransformer(self.model_name, device=self.device)
            model.save(str(self.local_path))
            
            print(f"Model saved to {self.local_path}")
            return True
            
        except Exception as e:
            print(f"Error downloading model: {e}")
            return False
    
    def load_model(self) -> bool:
        """
        Load the BGE model (download if necessary)
        
        Returns:
            True if model loaded successfully, False otherwise
        """
        if not EMBEDDINGS_AVAILABLE:
            print("sentence-transformers not available. Cannot load model.")
            return False
        
        try:
            # Try to load from local path first
            if self.local_path.exists():
                print(f"Loading model from {self.local_path}")
                self.model = SentenceTransformer(str(self.local_path), device=self.device)
            else:
                # Download model first
                print(f"Model not found locally, downloading {self.model_name}")
                if not self.download_model():
                    return False
                self.model = SentenceTransformer(str(self.local_path), device=self.device)
            
            print(f"Model loaded successfully on device: {self.device}")
            return True
            
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def generate_embeddings(self, texts: List[str], query_prefix: Optional[str] = None) -> Optional[np.ndarray]:
        """
        Generate embeddings for a list of texts
        
        Args:
            texts: List of text strings to embed
            query_prefix: Optional prefix for query texts (BGE models benefit from this)
            
        Returns:
            numpy array of embeddings or None if failed
        """
        if not self.model:
            if not self.load_model():
                return None
        
        try:
            # Add query prefix if specified (BGE models perform better with this)
            if query_prefix:
                texts = [f"{query_prefix} {text}" for text in texts]
            
            # Generate embeddings
            embeddings = self.model.encode(
                texts,
                batch_size=32,
                show_progress_bar=True,
                convert_to_numpy=True,
                normalize_embeddings=True  # Normalize for cosine similarity
            )
            
            return embeddings
            
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            return None
    
    def generate_single_embedding(self, text: str, query_prefix: Optional[str] = None) -> Optional[np.ndarray]:
        """
        Generate embedding for a single text
        
        Args:
            text: Text string to embed
            query_prefix: Optional prefix for query text
            
        Returns:
            numpy array embedding or None if failed
        """
        embeddings = self.generate_embeddings([text], query_prefix)
        if embeddings is not None:
            return embeddings[0]
        return None
    
    def process_document_chunks(self, chunks: List[Dict]) -> List[Dict]:
        """
        Add embeddings to document chunks
        
        Args:
            chunks: List of document chunk dictionaries
            
        Returns:
            Updated chunks with embeddings added
        """
        if not chunks:
            return chunks
        
        print(f"Generating embeddings for {len(chunks)} document chunks...")
        
        # Extract text content for embedding
        texts = []
        for chunk in chunks:
            # Combine relevant text fields for embedding
            text_parts = [
                chunk.get('file_name', ''),
                chunk.get('relative_path', ''),
                chunk.get('content', '')
            ]
            # Add category-specific text
            if chunk.get('category') == 'table_context':
                if 'database' in chunk and 'schema' in chunk and 'table_name' in chunk:
                    text_parts.append(f"{chunk['database']}.{chunk['schema']}.{chunk['table_name']}")
            
            combined_text = ' '.join(filter(None, text_parts))
            texts.append(combined_text)
        
        # Generate embeddings
        embeddings = self.generate_embeddings(texts)
        
        if embeddings is None:
            print("Failed to generate embeddings")
            return chunks
        
        # Add embeddings to chunks
        for i, chunk in enumerate(chunks):
            chunk['embedding'] = embeddings[i].tolist()  # Convert to list for JSON serialization
            chunk['embedding_dim'] = len(embeddings[i])
        
        print(f"Successfully added embeddings to {len(chunks)} chunks")
        return chunks
    
    def save_embeddings_cache(self, chunks: List[Dict], cache_path: Path):
        """Save embeddings to cache file"""
        try:
            # Extract just the embeddings and metadata for caching
            cache_data = {
                'model_name': self.model_name,
                'chunks': [
                    {
                        'file_hash': chunk.get('file_hash'),
                        'chunk_id': chunk.get('chunk_id'),
                        'embedding': chunk.get('embedding')
                    }
                    for chunk in chunks if 'embedding' in chunk
                ]
            }
            
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f)
            
            print(f"Saved embeddings cache to {cache_path}")
            
        except Exception as e:
            print(f"Error saving embeddings cache: {e}")
    
    def load_embeddings_cache(self, cache_path: Path) -> Dict:
        """Load embeddings from cache file"""
        try:
            if not cache_path.exists():
                return {}
            
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            if cache_data.get('model_name') != self.model_name:
                print(f"Cache model mismatch: {cache_data.get('model_name')} vs {self.model_name}")
                return {}
            
            return cache_data
            
        except Exception as e:
            print(f"Error loading embeddings cache: {e}")
            return {}


def main():
    """Test the embedding generator"""
    generator = BGEEmbeddingGenerator()
    
    # Test model loading
    if not generator.load_model():
        print("Failed to load model")
        return
    
    # Test embedding generation
    test_texts = [
        "This is a test document about user analytics",
        "SQL query for calculating delivery metrics",
        "Table documentation for dimension_users"
    ]
    
    embeddings = generator.generate_embeddings(test_texts)
    
    if embeddings is not None:
        print(f"Generated embeddings shape: {embeddings.shape}")
        print(f"First embedding (first 5 dims): {embeddings[0][:5]}")
    else:
        print("Failed to generate embeddings")


if __name__ == "__main__":
    main()