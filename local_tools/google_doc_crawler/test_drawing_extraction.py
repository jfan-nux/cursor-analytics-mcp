#!/usr/bin/env python3
"""
Test script for the new comprehensive drawing extraction method.
"""

import sys
import json
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.enhanced_converter import EnhancedGoogleDocConverter
from local_tools.google_doc_crawler.oauth_credentials_config import get_oauth_credentials


def test_drawing_detection():
    """Test the new drawing detection on a sample document structure."""
    
    # Sample document structure with both inline and positioned objects
    sample_document = {
        "title": "Test Document with Drawings",
        "inlineObjects": {
            "obj1": {
                "inlineObjectProperties": {
                    "embeddedObject": {
                        "imageProperties": {
                            "contentUri": "https://lh3.googleusercontent.com/drawings/sample1"
                        },
                        "embeddedDrawingProperties": {
                            "id": "drawing_123"
                        }
                    }
                }
            },
            "obj2": {
                "inlineObjectProperties": {
                    "embeddedObject": {
                        "linkedContentReference": {
                            "driveFileId": "1ABC123_sample_drive_drawing"
                        },
                        "imageProperties": {}
                    }
                }
            }
        },
        "positionedObjects": {
            "obj3": {
                "positionedObjectProperties": {
                    "embeddedObject": {
                        "imageProperties": {
                            "contentUri": "https://lh3.googleusercontent.com/drawings/sample3"
                        },
                        "embeddedDrawingProperties": {
                            "id": "positioned_drawing_456"
                        }
                    }
                }
            }
        }
    }
    
    # Create converter instance
    converter = EnhancedGoogleDocConverter()
    
    # Test drawing detection without actual API calls
    print("Testing drawing detection logic...")
    
    # Test inline objects
    inline_objects = sample_document.get('inlineObjects', {})
    print(f"Found {len(inline_objects)} inline objects")
    
    for obj_id, obj in inline_objects.items():
        inline_props = obj.get('inlineObjectProperties', {})
        embedded_object = inline_props.get('embeddedObject', {})
        
        is_drawing = converter._is_drawing_object(embedded_object)
        print(f"  {obj_id}: is_drawing = {is_drawing}")
        
        if is_drawing:
            # Check detection method
            linked_content = embedded_object.get('linkedContentReference', {})
            drive_file_id = linked_content.get('driveFileId')
            
            image_props = embedded_object.get('imageProperties', {})
            content_uri = image_props.get('contentUri')
            
            if drive_file_id:
                print(f"    -> Drive-linked drawing: {drive_file_id}")
            elif content_uri:
                print(f"    -> Embedded drawing: {content_uri}")
    
    # Test positioned objects
    positioned_objects = sample_document.get('positionedObjects', {})
    print(f"\nFound {len(positioned_objects)} positioned objects")
    
    for obj_id, obj in positioned_objects.items():
        positioned_props = obj.get('positionedObjectProperties', {})
        embedded_object = positioned_props.get('embeddedObject', {})
        
        is_drawing = converter._is_drawing_object(embedded_object)
        print(f"  {obj_id}: is_drawing = {is_drawing}")
        
        if is_drawing:
            image_props = embedded_object.get('imageProperties', {})
            content_uri = image_props.get('contentUri')
            print(f"    -> Positioned drawing: {content_uri}")
    
    print("\n✅ Drawing detection logic test completed!")


def test_with_real_document(doc_url: str):
    """Test with a real Google Doc (requires OAuth credentials)."""
    
    try:
        # Initialize converter
        converter = EnhancedGoogleDocConverter()
        
        # Get OAuth credentials
        credentials = get_oauth_credentials()
        converter.initialize_services(credentials)
        
        # Extract document ID
        doc_id = converter.extract_doc_id(doc_url)
        
        # Get document
        document = converter.docs_service.documents().get(documentId=doc_id).execute()
        
        # Test the new extraction method
        temp_folder = Path("/tmp/test_drawings")
        temp_folder.mkdir(exist_ok=True)
        
        print(f"Testing comprehensive drawing extraction on: {document.get('title')}")
        drawing_map = converter.extract_all_drawings(document, temp_folder)
        
        print(f"✅ Successfully extracted {len(drawing_map)} drawings:")
        for obj_id, path in drawing_map.items():
            print(f"  {obj_id} -> {path}")
            
    except Exception as e:
        print(f"❌ Error testing with real document: {e}")


if __name__ == "__main__":
    # Test the drawing detection logic
    test_drawing_detection()
    
    # Optionally test with a real document
    if len(sys.argv) > 1:
        doc_url = sys.argv[1]
        print(f"\nTesting with real document: {doc_url}")
        test_with_real_document(doc_url)
    else:
        print("\nTo test with a real document, provide a Google Docs URL as argument:")
        print("python test_drawing_extraction.py 'https://docs.google.com/document/d/YOUR_DOC_ID/edit'")
