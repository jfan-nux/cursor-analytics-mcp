#!/usr/bin/env python3
"""
Test script for document indexer components
"""

import sys
from pathlib import Path

def test_document_processor():
    """Test document processing"""
    print("Testing document processor...")
    
    try:
        from .document_processor import DocumentProcessor
        
        # Test with context folder
        context_root = Path(__file__).parent.parent.parent / "context" 
        processor = DocumentProcessor(context_root)
        
        # Process a small subset
        chunks = processor.process_all_documents()
        
        if chunks:
            print(f"✅ Processed {len(chunks)} chunks")
            
            # Show categories
            categories = {}
            for chunk in chunks:
                cat = chunk.get('category', 'unknown')
                categories[cat] = categories.get(cat, 0) + 1
            
            print("Categories found:")
            for cat, count in categories.items():
                print(f"  {cat}: {count}")
                
            return True
        else:
            print("❌ No chunks processed")
            return False
            
    except Exception as e:
        print(f"❌ Document processor test failed: {e}")
        return False

def test_embedding_generator():
    """Test embedding generation"""
    print("\nTesting embedding generator...")
    
    try:
        from .embedding_generator import BGEEmbeddingGenerator
        
        generator = BGEEmbeddingGenerator()
        
        # Test model loading
        if generator.load_model():
            print("✅ Model loaded successfully")
            
            # Test embedding generation
            test_texts = [
                "This is a test document about user analytics",
                "SQL query for delivery metrics"
            ]
            
            embeddings = generator.generate_embeddings(test_texts)
            
            if embeddings is not None:
                print(f"✅ Generated embeddings shape: {embeddings.shape}")
                return True
            else:
                print("❌ Failed to generate embeddings")
                return False
        else:
            print("❌ Failed to load model")
            return False
            
    except Exception as e:
        print(f"❌ Embedding generator test failed: {e}")
        return False

def test_snowflake_uploader():
    """Test Snowflake connection and table creation"""
    print("\nTesting Snowflake uploader...")
    
    try:
        from .snowflake_uploader import DocumentIndexUploader
        
        uploader = DocumentIndexUploader()
        
        # Test table creation
        if uploader.create_table_if_not_exists():
            print("✅ Table creation successful")
            
            # Get stats
            stats = uploader.get_table_stats()
            if stats:
                print("Current table stats:")
                for key, value in stats.items():
                    print(f"  {key}: {value}")
            
            return True
        else:
            print("❌ Table creation failed")
            return False
            
    except Exception as e:
        print(f"❌ Snowflake uploader test failed: {e}")
        return False

def test_hybrid_search():
    """Test hybrid search functionality"""
    print("\nTesting hybrid search...")
    
    try:
        from .hybrid_search import HybridSearcher
        
        searcher = HybridSearcher(database="proddb", schema="fionafan", table="document_index")
        
        # Test search (will be empty if no data indexed yet)
        results = searcher.search_documents("test query", top_k=1)
        
        print(f"✅ Search executed, found {len(results)} results")
        
        if results:
            result = results[0]
            print(f"Sample result: {result.get('file_name', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Hybrid search test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running Document Indexer Tests\n")
    
    tests = [
        test_document_processor,
        test_embedding_generator,
        test_snowflake_uploader,
        test_hybrid_search
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The document indexer is ready.")
        return True
    else:
        print("❌ Some tests failed. Check the setup and dependencies.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)