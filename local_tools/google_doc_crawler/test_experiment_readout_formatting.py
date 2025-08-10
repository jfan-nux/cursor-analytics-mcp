#!/usr/bin/env python3
"""
Test script for experiment readout formatting improvements.
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.enhanced_converter import EnhancedGoogleDocConverter


def test_table_formatting():
    """Test table formatting with bold elements."""
    
    sample_table_markdown = """
| Metric | Treatment | Control | Δ | Sig |
| --- | --- | --- | --- | --- |
| ** Order rate** | 15.69 % | 15.28 % | **+2.64 %** | ✅ |
| MAU | 11.30 % | 11.28 % | +0.18 % | ❌ |
"""
    
    converter = EnhancedGoogleDocConverter()
    
    # Test the aggressive markdown fixes
    fixed_content, fixes_applied = converter._aggressive_md_fixes(sample_table_markdown)
    
    print("Original table:")
    print(sample_table_markdown)
    print("\nFixed table:")
    print(fixed_content)
    print(f"\nFixes applied: {fixes_applied}")


def test_collapsible_detection():
    """Test collapsible section detection."""
    
    sample_content = """
# Experiment Readout: Test

## Results Summary

The experiment generated positive results.

### Key metrics

| Metric | Treatment | Control | Δ | Sig |
| --- | --- | --- | --- | --- |
| **Order rate** | 15.69% | 15.28% | **+2.64%** | ✅ |
| MAU | 11.30% | 11.28% | +0.18% | ❌ |

### Check metrics

| Metric | Treatment | Control | Δ | Sig |
| --- | --- | --- | --- | --- |
| Sign-ups | 5.87% | 5.91% | −0.69% | ❌ |
| Logins | 14.32% | 14.54% | −1.54% | ✅ |

## Next Steps

Continue with the experiment.
"""
    
    converter = EnhancedGoogleDocConverter()
    
    # Test collapsible section detection
    collapsible_content = converter.detect_and_convert_collapsible_sections(sample_content)
    
    print("Original content:")
    print(sample_content)
    print("\nContent with collapsible sections:")
    print(collapsible_content)


def test_bold_formatting_fixes():
    """Test bold formatting specific to experiment readouts."""
    
    test_cases = [
        "**+2.64 %**",           # Should become **+2.64%**
        "**$3.2 M**",            # Should become **$3.2M**
        "**Order rate**15.69%",  # Should become **Order rate** 15.69%
        "- ** Problem:**We",     # Should become - **Problem:** We
        "✅Success",             # Should become ✅ Success
    ]
    
    converter = EnhancedGoogleDocConverter()
    
    print("Testing bold formatting fixes:")
    for test_case in test_cases:
        fixed, fixes = converter._aggressive_md_fixes(test_case)
        print(f"  '{test_case}' → '{fixed}'")
        if fixes:
            print(f"    Fixes: {fixes}")


if __name__ == "__main__":
    print("🧪 Testing Experiment Readout Formatting Improvements")
    print("=" * 60)
    
    print("\n1. Testing Table Formatting:")
    print("-" * 30)
    test_table_formatting()
    
    print("\n\n2. Testing Collapsible Section Detection:")
    print("-" * 40)
    test_collapsible_detection()
    
    print("\n\n3. Testing Bold Formatting Fixes:")
    print("-" * 35)
    test_bold_formatting_fixes()
    
    print("\n✅ All tests completed!")
