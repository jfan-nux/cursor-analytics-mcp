"""
Document processing module for extracting, chunking, and preparing documents for indexing
"""

import hashlib
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime

try:
    from .config import (
        CHUNK_SIZE, CHUNK_OVERLAP, SUPPORTED_EXTENSIONS, CONTEXT_CATEGORIES,
        BM25_MIN_TOKEN_LENGTH, BM25_STOPWORDS, CONTENT_TYPE_MAPPING
    )
except ImportError:
    from config import (
        CHUNK_SIZE, CHUNK_OVERLAP, SUPPORTED_EXTENSIONS, CONTEXT_CATEGORIES,
        BM25_MIN_TOKEN_LENGTH, BM25_STOPWORDS, CONTENT_TYPE_MAPPING
    )


class DocumentProcessor:
    """Processes documents from the context folder for indexing"""
    
    def __init__(self, context_root: Path):
        self.context_root = Path(context_root)
        
    def extract_metadata(self, file_path: Path) -> Dict:
        """
        Extract metadata from a file path and content (UPDATED)
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary containing metadata
        """
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            relative_path = file_path.relative_to(self.context_root)
            
            # Determine category based on path
            category = self._determine_category(relative_path)
            
            # Extract subcategory and document title
            subcategory, document_title = self._extract_subcategory_and_title(relative_path, category)
            
            # Create hashes for change detection
            file_hash = hashlib.md5(content.encode()).hexdigest()
            document_hash = hashlib.sha256(content.encode()).hexdigest()
            
            # Basic metadata
            metadata = {
                'file_path': str(file_path),
                'relative_path': str(relative_path),
                'file_name': file_path.name,
                'file_stem': file_path.stem,
                'file_extension': file_path.suffix,
                'category': category,
                'subcategory': subcategory,
                'document_title': document_title,
                'content_type': CONTENT_TYPE_MAPPING.get(file_path.suffix, 'unknown'),
                'file_size': file_path.stat().st_size,
                'file_hash': file_hash,
                'document_hash': document_hash,
                'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                'processed_at': datetime.now().isoformat()
            }
            
            # Extract additional metadata based on category
            if category == "table_context":
                metadata.update(self._extract_table_metadata(relative_path))
            elif category == "pod_queries":
                metadata.update(self._extract_query_metadata(content, file_path.stem))
            
            return metadata
            
        except Exception as e:
            print(f"Error extracting metadata from {file_path}: {e}")
            return {}
    
    def _determine_category(self, relative_path: Path) -> str:
        """Determine document category based on path"""
        path_str = str(relative_path)
        
        for path_pattern, category in CONTEXT_CATEGORIES.items():
            if path_pattern in path_str:
                return category
        
        return "general"
    
    def _extract_subcategory_and_title(self, relative_path: Path, category: str) -> Tuple[Optional[str], str]:
        """
        Extract subcategory (organizational path) and document title from path
        
        Examples:
        - deep-dives/growth/nux/Road-to-MAU-Deep-Dive/report.md
          → subcategory: "growth/nux", document_title: "Road-to-MAU-Deep-Dive"
        - pod-level-validated-master-queries/growth/nux/queries.sql  
          → subcategory: "growth/nux", document_title: "queries.sql"
        - snowflake-table-context/edw/consumer/users.md
          → subcategory: "edw/consumer", document_title: "users.md"
        """
        path_parts = relative_path.parts
        
        # Find the category folder in the path
        category_folder = None
        for cat_path, cat_name in CONTEXT_CATEGORIES.items():
            if cat_name == category and cat_path in str(relative_path):
                category_folder = cat_path
                break
        
        if not category_folder:
            return None, relative_path.name
        
        # Find where the category ends in the path
        category_parts = category_folder.split('/')
        category_end_idx = None
        
        # Look for the category path in the file path
        for i, part in enumerate(path_parts):
            if part == category_parts[-1]:
                # Check if this matches the full category path
                if len(category_parts) == 1 or (i > 0 and path_parts[i-len(category_parts)+1:i+1] == tuple(category_parts)):
                    category_end_idx = i
                    break
        
        if category_end_idx is None:
            return None, relative_path.name
        
        # Extract parts after category
        remaining_parts = path_parts[category_end_idx + 1:]
        
        if not remaining_parts:
            return None, relative_path.name
        
        # The logic: stop subcategory at organizational level, not document-specific folders
        if len(remaining_parts) == 1:
            # Direct file in category folder: no subcategory
            subcategory = None
            document_title = remaining_parts[0]
        elif len(remaining_parts) == 2:
            # One level deep: subcategory is the folder, title is the file
            subcategory = remaining_parts[0]
            document_title = remaining_parts[1]
        else:
            # Multiple levels: need to distinguish organizational vs document folders
            # Heuristic: if the second-to-last part looks like a document folder, 
            # it becomes the document title
            
            # Document folder patterns: starts with capital, contains dashes, looks like a project name
            second_to_last = remaining_parts[-2]
            last_part = remaining_parts[-1]
            
            # Check if second-to-last looks like a document/project folder
            # More specific patterns to avoid false positives like "pricing-and-affordability"
            is_document_folder = (
                # Contains "Experiment-Readout" pattern (very specific)
                'Experiment-Readout' in second_to_last or
                # Contains "Road-to" pattern (very specific)
                'Road-to' in second_to_last or
                # Other very specific document patterns
                any(pattern in second_to_last for pattern in ['Deep-Dive', 'Analysis-Report']) or
                # Starts with year pattern (e.g., "2025-q3-...")
                (len(second_to_last) > 4 and second_to_last[:4].isdigit()) or
                # Multiple uppercase words separated by hyphens (title case naming)
                (second_to_last.count('-') >= 2 and 
                 any(part[0].isupper() for part in second_to_last.split('-')[1:]))
            )
            
            if is_document_folder:
                # Second-to-last is a document folder, so subcategory stops before it
                subcategory = '/'.join(remaining_parts[:-2])
                document_title = second_to_last  # Document folder name is the title
            else:
                # All parts except filename are organizational
                subcategory = '/'.join(remaining_parts[:-1])
                document_title = last_part
        
        return subcategory, document_title
    
    def _extract_table_metadata(self, relative_path: Path) -> Dict:
        """Extract table-specific metadata from path"""
        parts = relative_path.parts
        
        metadata = {}
        # Updated to work with new category structure: snowflake-table-context/database/schema/table.md
        if len(parts) >= 4 and "snowflake-table-context" in parts:
            table_context_idx = None
            for i, part in enumerate(parts):
                if part == "snowflake-table-context":
                    table_context_idx = i
                    break
            
            if table_context_idx is not None and len(parts) >= table_context_idx + 4:
                # database/schema/table.md after snowflake-table-context
                metadata.update({
                    'database': parts[table_context_idx + 1],
                    'schema': parts[table_context_idx + 2], 
                    'table_name': Path(parts[table_context_idx + 3]).stem
                })
        
        return metadata
    
    def _extract_query_metadata(self, content: str, file_stem: str) -> Dict:
        """Extract query-specific metadata from SQL content"""
        metadata = {'query_name': file_stem}
        
        # Extract common SQL patterns
        content_lower = content.lower()
        
        # Check for common table patterns
        table_patterns = re.findall(r'from\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content_lower)
        if table_patterns:
            metadata['referenced_tables'] = list(set(table_patterns))
        
        # Check for common keywords to infer query type
        if any(word in content_lower for word in ['select', 'from', 'where']):
            metadata['query_type'] = 'SELECT'
        elif 'create' in content_lower:
            metadata['query_type'] = 'CREATE'
        elif 'insert' in content_lower:
            metadata['query_type'] = 'INSERT'
        elif 'update' in content_lower:
            metadata['query_type'] = 'UPDATE'
        
        return metadata
    
    def chunk_content(self, content: str, metadata: Dict) -> List[Dict]:
        """
        Split large content into chunks for better search
        
        Args:
            content: Document content
            metadata: Document metadata
            
        Returns:
            List of chunk dictionaries
        """
        if len(content) <= CHUNK_SIZE:
            # Small document, return as single chunk
            chunk_metadata = metadata.copy()
            chunk_metadata.update({
                'chunk_id': 0,
                'chunk_count': 1,
                'chunk_start': 0,
                'chunk_end': len(content),
                'content': content
            })
            return [chunk_metadata]
        
        # Split into overlapping chunks
        chunks = []
        chunk_id = 0
        start = 0
        
        while start < len(content):
            end = min(start + CHUNK_SIZE, len(content))
            
            # Try to break at word boundaries
            if end < len(content):
                # Look for the last space or newline in the chunk
                last_break = max(
                    content.rfind(' ', start, end),
                    content.rfind('\n', start, end)
                )
                if last_break > start + CHUNK_SIZE // 2:  # Only use if break is not too early
                    end = last_break
            
            chunk_content = content[start:end].strip()
            if chunk_content:  # Only add non-empty chunks
                chunk_metadata = metadata.copy()
                chunk_metadata.update({
                    'chunk_id': chunk_id,
                    'chunk_count': -1,  # Will be updated after all chunks are created
                    'chunk_start': start,
                    'chunk_end': end,
                    'content': chunk_content
                })
                chunks.append(chunk_metadata)
                chunk_id += 1
            
            # Move start position with overlap
            start = max(start + CHUNK_SIZE - CHUNK_OVERLAP, end)
        
        # Update chunk counts
        total_chunks = len(chunks)
        for chunk in chunks:
            chunk['chunk_count'] = total_chunks
        
        return chunks
    
    def preprocess_text_for_bm25(self, text: str) -> List[str]:
        """
        Preprocess text for BM25 indexing
        
        Args:
            text: Raw text content
            
        Returns:
            List of processed tokens
        """
        # Convert to lowercase
        text = text.lower()
        
        # Replace punctuation and special characters with spaces
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        
        # Split into tokens
        tokens = text.split()
        
        # Filter tokens
        processed_tokens = []
        for token in tokens:
            # Remove short tokens and stopwords
            if len(token) >= BM25_MIN_TOKEN_LENGTH and token not in BM25_STOPWORDS:
                processed_tokens.append(token)
        
        return processed_tokens
    
    def process_all_documents(self) -> List[Dict]:
        """
        Process all documents in the context folder
        
        Returns:
            List of processed document chunks with metadata
        """
        all_chunks = []
        
        if not self.context_root.exists():
            print(f"Context root {self.context_root} does not exist")
            return all_chunks
        
        # Find all supported files
        for extension in SUPPORTED_EXTENSIONS:
            for file_path in self.context_root.rglob(f"*{extension}"):
                try:
                    print(f"Processing: {file_path}")
                    
                    # Extract metadata
                    metadata = self.extract_metadata(file_path)
                    if not metadata:
                        continue
                    
                    # Read content
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    
                    # Create chunks
                    chunks = self.chunk_content(content, metadata)
                    
                    # Add BM25 tokens to each chunk
                    for chunk in chunks:
                        chunk['bm25_tokens'] = self.preprocess_text_for_bm25(
                            f"{chunk['file_name']} {chunk['relative_path']} {chunk['content']}"
                        )
                        chunk['bm25_text'] = ' '.join(chunk['bm25_tokens'])
                    
                    all_chunks.extend(chunks)
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue
        
        print(f"Processed {len(all_chunks)} document chunks from {self.context_root}")
        return all_chunks
    
    def save_processed_documents(self, chunks: List[Dict], output_path: Path):
        """Save processed documents to JSON file for inspection"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(chunks, f, indent=2, ensure_ascii=False)
            print(f"Saved {len(chunks)} chunks to {output_path}")
        except Exception as e:
            print(f"Error saving processed documents: {e}")


def main():
    """Test the document processor"""
    from pathlib import Path
    
    # Test with the context folder
    context_root = Path(__file__).parent.parent.parent / "context"
    processor = DocumentProcessor(context_root)
    
    chunks = processor.process_all_documents()
    
    # Save results for inspection
    output_path = Path(__file__).parent / "processed_documents.json"
    processor.save_processed_documents(chunks, output_path)
    
    print(f"\nProcessing complete!")
    print(f"Total chunks: {len(chunks)}")
    
    # Show category breakdown
    categories = {}
    for chunk in chunks:
        cat = chunk.get('category', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nCategory breakdown:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()