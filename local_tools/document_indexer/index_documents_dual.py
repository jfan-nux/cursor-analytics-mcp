#!/usr/bin/env python3
"""
Enhanced document indexer with dual-table structure (document_index + chunk_index)
"""

import sys
import argparse
from pathlib import Path
from collections import defaultdict

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from document_processor import DocumentProcessor
    from embedding_generator import BGEEmbeddingGenerator
    from dual_table_uploader import DualTableUploader
    from config import CONTEXT_CATEGORIES, SUPPORTED_EXTENSIONS
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you're running from the document_indexer directory")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Index documents with dual-table structure')
    parser.add_argument('--context-root', required=True, 
                       help='Root directory containing context folders')
    parser.add_argument('--clear-tables', action='store_true',
                       help='Clear existing tables before indexing')
    parser.add_argument('--dry-run', action='store_true',
                       help='Process documents but do not upload to Snowflake')
    
    args = parser.parse_args()
    context_root = Path(args.context_root)
    
    if not context_root.exists():
        print(f"❌ Context root directory not found: {context_root}")
        return False
    
    print("🚀 Starting enhanced document indexing with dual-table structure")
    print(f"📁 Context root: {context_root}")
    print(f"🗑️  Clear tables: {args.clear_tables}")
    print(f"🔍 Dry run: {args.dry_run}")
    print("=" * 60)
    
    # Step 1: Process documents
    print("📄 Step 1: Processing documents...")
    processor = DocumentProcessor(context_root)
    
    # Process all documents at once using the standard API
    chunks = processor.process_all_documents()
    
    if not chunks:
        print("❌ No documents found to process")
        return False
    
    print(f"✅ Processed {len(chunks)} document chunks")
    
    # Group chunks by document for dual-table structure
    documents_chunks = defaultdict(list)
    
    for chunk in chunks:
        # Use relative_path as the document identifier
        relative_path = chunk.get('relative_path')
        if relative_path:
            documents_chunks[relative_path].append(chunk)
    
    print(f"📊 Grouped into {len(documents_chunks)} documents")
    
    # Category breakdown
    category_counts = defaultdict(int)
    for doc_chunks in documents_chunks.values():
        if doc_chunks:
            category = doc_chunks[0].get('category', 'unknown')
            category_counts[category] += len(doc_chunks)
    
    print("📊 Category breakdown:")
    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count} chunks")
    
    if args.dry_run:
        print("\n🔍 Dry run completed - no upload to Snowflake")
        return True
    
    # Step 2: Generate embeddings
    print("\n🧠 Step 2: Generating embeddings...")
    embedding_generator = BGEEmbeddingGenerator()
    
    if not embedding_generator.load_model():
        print("❌ Failed to load embedding model")
        return False
    
    # Generate embeddings for all chunks at once
    chunks = embedding_generator.process_document_chunks(chunks)
    
    print("✅ Embeddings generated successfully")
    
    # Re-group chunks after embedding generation 
    documents_chunks = defaultdict(list)
    for chunk in chunks:
        # Use relative_path as the document identifier
        relative_path = chunk.get('relative_path')
        if relative_path:
            documents_chunks[relative_path].append(chunk)
    
    # Step 3: Upload to Snowflake
    print("\n❄️  Step 3: Uploading to Snowflake...")
    uploader = DualTableUploader()
    
    if args.clear_tables:
        print("🗑️  Clearing existing tables...")
        if not uploader.clear_tables():
            print("❌ Failed to clear tables")
            return False
        print("✅ Tables cleared")
    
    # Upload documents and chunks
    success = uploader.upload_documents_and_chunks(documents_chunks)
    if not success:
        print("❌ Upload failed")
        return False
    
    print("✅ Upload completed successfully")
    
    # Final statistics
    print("\n📈 Final statistics:")
    stats = uploader.get_table_stats()
    if stats:
        print(f"📄 Documents: {stats['documents']}")
        print(f"📝 Chunks: {stats['chunks']}")
        print(f"📊 Avg chunks per document: {stats['chunks'] / stats['documents']:.1f}")
    
    print("\n🎉 Document indexing completed successfully!")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
