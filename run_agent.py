#!/usr/bin/env python3
"""
Comprehensive test script for the table context agent.
Tests various scenarios including different table name formats, error handling, and output options.
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from local_tools.table_context_agent.agent import main
from utils.snowflake_connection import SnowflakeHook

def print_header(title: str):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n📋 {title}")
    print("-" * 60)

def test_table_resolution():
    """Test table name resolution functionality."""
    print_section("Testing Table Name Resolution")
    
    test_tables = [
        "dimension_deliveries",
        "dimension_consumer_push_settings_scd3", 
        "unified_consumer_events",
        "dimension_users"
    ]
    
    for table in test_tables:
        print(f"\n🔍 Testing resolution for: {table}")
        try:
            with SnowflakeHook() as sf:
                from local_tools.table_context_agent.tyler_sources import resolve_table_name
                resolved = resolve_table_name(sf, table, verbose=True)
                print(f"✅ Resolved to: {resolved}")
        except Exception as e:
            print(f"❌ Error resolving {table}: {str(e)}")

def test_agent_basic():
    """Test basic agent functionality with different table formats."""
    print_section("Testing Basic Agent Functionality")
    
    test_cases = [
        {
            "table": "dimension_deliveries",
            "description": "Partial table name - should resolve automatically",
            "expected": "Should find edw.finance.dimension_deliveries"
        },
        {
            "table": "edw.finance.dimension_deliveries", 
            "description": "Full table name - should use as-is",
            "expected": "Should use the exact table specified"
        },
        {
            "table": "dimension_consumer_push_settings_scd3",
            "description": "Another partial table name",
            "expected": "Should resolve to correct schema"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 Test Case {i}: {test_case['description']}")
        print(f"   Input: {test_case['table']}")
        print(f"   Expected: {test_case['expected']}")
        
        try:
            result = main(
                table=test_case['table'],
                print_only=True,
                sample_row_limit=3,
                verbose=True
            )
            
            # Show preview of result
            lines = result.split('\n')
            preview_lines = lines[:15] if len(lines) > 15 else lines
            preview = '\n'.join(preview_lines)
            if len(lines) > 15:
                preview += f"\n... ({len(lines) - 15} more lines)"
            
            print("✅ Success! Report preview:")
            print(preview)
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print(f"   Error type: {type(e).__name__}")

def test_agent_with_output():
    """Test agent with file output."""
    print_section("Testing Agent with File Output")
    
    test_table = "dimension_deliveries"
    output_dir = project_root / "test_outputs"
    
    print(f"🔍 Testing file output for: {test_table}")
    print(f"📁 Output directory: {output_dir}")
    
    try:
        # Ensure output directory exists
        output_dir.mkdir(exist_ok=True)
        
        result_path = main(
            table=test_table,
            output_root=str(output_dir),
            sample_row_limit=5,
            verbose=True
        )
        
        print(f"✅ Success! File written to: {result_path}")
        
        # Verify file exists and show stats
        if isinstance(result_path, Path) and result_path.exists():
            file_size = result_path.stat().st_size
            print(f"📊 File size: {file_size} bytes")
            
            # Show first few lines
            with open(result_path, 'r', encoding='utf-8') as f:
                first_lines = [f.readline().strip() for _ in range(5)]
            print("📄 First few lines:")
            for line in first_lines:
                if line:
                    print(f"   {line}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_error_handling():
    """Test error handling with invalid inputs."""
    print_section("Testing Error Handling")
    
    error_test_cases = [
        {
            "table": "nonexistent_table_xyz",
            "description": "Non-existent table"
        },
        {
            "table": "",
            "description": "Empty table name"
        },
        {
            "table": "invalid.schema.table.extra",
            "description": "Malformed table name"
        }
    ]
    
    for test_case in error_test_cases:
        print(f"\n🧪 Testing: {test_case['description']}")
        print(f"   Input: '{test_case['table']}'")
        
        try:
            result = main(
                table=test_case['table'],
                print_only=True,
                sample_row_limit=3
            )
            print("⚠️  Unexpected success - this should have failed")
            
        except Exception as e:
            print(f"✅ Expected error caught: {type(e).__name__}: {str(e)}")

def test_confluence_integration():
    """Test Confluence integration if available."""
    print_section("Testing Confluence Integration")
    
    try:
        from local_tools.table_context_agent.confluence_client import ConfluenceSearcher
        confluence = ConfluenceSearcher.from_env()
        
        if confluence is None:
            print("⚠️  Confluence not configured - skipping integration test")
            return
        
        print("✅ Confluence client initialized successfully")
        
        # Test search functionality
        test_query = "dimension_deliveries"
        print(f"🔍 Testing search for: {test_query}")
        
        results = confluence.search_pages(query=test_query, limit=3)
        if results:
            print(f"✅ Found {len(results)} Confluence pages")
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                url = result.get('url', 'No URL')
                print(f"   {i}. {title[:50]}{'...' if len(title) > 50 else ''}")
        else:
            print("ℹ️  No Confluence pages found for test query")
        
    except Exception as e:
        print(f"❌ Confluence integration error: {str(e)}")

def test_performance():
    """Test performance with different sample limits."""
    print_section("Testing Performance with Different Sample Limits")
    
    test_table = "dimension_deliveries"
    sample_limits = [1, 5, 10, 20]
    
    for limit in sample_limits:
        print(f"\n⏱️  Testing with sample_row_limit={limit}")
        
        start_time = datetime.now()
        try:
            result = main(
                table=test_table,
                print_only=True,
                sample_row_limit=limit,
                verbose=False  # Reduce noise for performance test
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            # Count lines in result
            line_count = len(result.split('\n'))
            
            print(f"✅ Completed in {duration:.2f}s, generated {line_count} lines")
            
        except Exception as e:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            print(f"❌ Failed after {duration:.2f}s: {str(e)}")

def run_interactive_test():
    """Run an interactive test where user can specify table name."""
    print_section("Interactive Test")
    
    try:
        table_name = input("\n📝 Enter a table name to test (or press Enter for default): ").strip()
        if not table_name:
            table_name = "dimension_deliveries"
        
        print(f"🔍 Testing table: {table_name}")
        
        verbose = input("Enable verbose output? (y/N): ").strip().lower() == 'y'
        
        print("\n🚀 Running agent...")
        result = main(
            table=table_name,
            print_only=True,
            sample_row_limit=5,
            verbose=verbose
        )
        
        print("\n📄 Generated Report:")
        print("=" * 80)
        print(result)
        
    except KeyboardInterrupt:
        print("\n⚠️  Interactive test cancelled by user")
    except Exception as e:
        print(f"\n❌ Interactive test error: {str(e)}")

def main_test_suite():
    """Run the complete test suite."""
    print_header("Table Context Agent Test Suite")
    print(f"🕐 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Project root: {project_root}")
    
    # Test 1: Table resolution
    try:
        test_table_resolution()
    except Exception as e:
        print(f"❌ Table resolution test failed: {str(e)}")
    
    # Test 2: Basic functionality
    try:
        test_agent_basic()
    except Exception as e:
        print(f"❌ Basic functionality test failed: {str(e)}")
    
    # Test 3: File output
    try:
        test_agent_with_output()
    except Exception as e:
        print(f"❌ File output test failed: {str(e)}")
    
    # Test 4: Error handling
    try:
        test_error_handling()
    except Exception as e:
        print(f"❌ Error handling test failed: {str(e)}")
    
    # Test 5: Confluence integration
    try:
        test_confluence_integration()
    except Exception as e:
        print(f"❌ Confluence integration test failed: {str(e)}")
    
    # Test 6: Performance
    try:
        test_performance()
    except Exception as e:
        print(f"❌ Performance test failed: {str(e)}")
    
    print_header("Test Suite Complete")
    print(f"🕐 Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive_test()
    else:
        main_test_suite()
        
        # Offer interactive mode
        print("\n" + "=" * 80)
        run_interactive = input("Would you like to run an interactive test? (y/N): ").strip().lower() == 'y'
        if run_interactive:
            run_interactive_test()
