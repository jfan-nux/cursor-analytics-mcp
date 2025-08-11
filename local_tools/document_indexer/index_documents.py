#!/usr/bin/env python3
"""
Main document indexing script

This script processes all documents in the context folder, generates embeddings,
and uploads them to Snowflake for hybrid search functionality.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict

from .document_processor import DocumentProcessor
from .embedding_generator import BGEEmbeddingGenerator
from .snowflake_uploader import DocumentIndexUploader


def main():
    """Main indexing function"""
    parser = argparse.ArgumentParser(description="Index documents for hybrid search")
    parser.add_argument(
        "--context-root", 
        type=Path,
        default=Path(__file__).parent.parent.parent / "context",
        help="Path to context folder"
    )
    parser.add_argument(
        "--clear-table",
        action="store_true",
        help="Clear existing table before uploading"
    )
    parser.add_argument(
        "--skip-embeddings",
        action="store_true", 
        help="Skip embedding generation (for testing)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size for Snowflake uploads"
    )
    parser.add_argument(
        "--save-json",
        type=Path,
        help="Save processed documents to JSON file"
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting document indexing pipeline...")
    print(f"Context root: {args.context_root}")
    
    # Step 1: Process documents
    print("\n📄 Step 1: Processing documents...")
    processor = DocumentProcessor(args.context_root)
    chunks = processor.process_all_documents()
    
    if not chunks:
        print("❌ No documents found to process")
        return False
    
    print(f"✅ Processed {len(chunks)} document chunks")
    
    # Show category breakdown
    categories = {}
    for chunk in chunks:
        cat = chunk.get('category', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n📊 Category breakdown:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} chunks")
    
    # Step 2: Generate embeddings
    if not args.skip_embeddings:
        print("\n🧠 Step 2: Generating embeddings...")
        generator = BGEEmbeddingGenerator()
        
        if not generator.load_model():
            print("❌ Failed to load embedding model")
            return False
        
        chunks = generator.process_document_chunks(chunks)
        print("✅ Embeddings generated successfully")
    else:
        print("\n⏭️  Step 2: Skipping embedding generation")
    
    # Step 3: Save to JSON if requested
    if args.save_json:
        print(f"\n💾 Saving processed documents to {args.save_json}")
        processor.save_processed_documents(chunks, args.save_json)
    
    # Step 4: Upload to Snowflake
    print("\n❄️  Step 3: Uploading to Snowflake...")
    uploader = DocumentIndexUploader()
    
    # Clear table if requested
    if args.clear_table:
        print("🗑️  Clearing existing table...")
        if not uploader.clear_table():
            print("❌ Failed to clear table")
            return False
    
    # Upload chunks
    if not uploader.upload_chunks(chunks, batch_size=args.batch_size):
        print("❌ Failed to upload to Snowflake")
        return False
    
    print("✅ Upload completed successfully")
    
    # Step 5: Show final stats
    print("\n📈 Final statistics:")
    stats = uploader.get_table_stats()
    if stats:
        for key, value in stats.items():
            print(f"  {key}: {value}")
    
    print("\n🎉 Document indexing pipeline completed successfully!")
    return True


def run_quick_test():
    """Run a quick test of the indexing pipeline"""
    print("🧪 Running quick test...")
    
    # Test with a small subset
    context_root = Path(__file__).parent.parent.parent / "context"
    processor = DocumentProcessor(context_root)
    
    # Process just a few files for testing
    all_chunks = processor.process_all_documents()
    test_chunks = all_chunks[:5] if all_chunks else []
    
    if not test_chunks:
        print("❌ No test chunks available")
        return False
    
    print(f"✅ Test processing: {len(test_chunks)} chunks")
    
    # Test embedding generation
    generator = BGEEmbeddingGenerator()
    if generator.load_model():
        test_chunks = generator.process_document_chunks(test_chunks)
        print("✅ Test embeddings generated")
    else:
        print("⚠️  Embedding generation test skipped")
    
    # Test Snowflake connection (without uploading)
    uploader = DocumentIndexUploader()
    if uploader.create_table_if_not_exists():
        print("✅ Snowflake connection test passed")
        
        stats = uploader.get_table_stats()
        if stats:
            print("📊 Current table stats:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
    else:
        print("❌ Snowflake connection test failed")
        return False
    
    print("🎉 Quick test completed successfully!")
    return True


if __name__ == "__main__":
    import sys
    
    # Check if this is a test run
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        success = run_quick_test()
    else:
        success = main()
    
    sys.exit(0 if success else 1)