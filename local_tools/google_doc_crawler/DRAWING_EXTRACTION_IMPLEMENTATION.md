# Enhanced Google Docs Converter Implementation

## Overview

This implementation includes comprehensive improvements to the Google Docs crawler:

1. **Enhanced Drawing Extraction**: Following official Google Docs API patterns for reliable extraction of both embedded and Drive-linked drawings
2. **Experiment Readout Formatting**: Specialized formatting for data science experiment readouts with proper table formatting, collapsible sections, and mathematical notation
3. **Advanced Markdown Processing**: Intelligent bold formatting, spacing fixes, and structure optimization

## Key Features

### 1. Comprehensive Drawing Detection

The implementation now handles both types of drawings that Google Docs supports:

- **Embedded Drawings** (`Insert → Drawing → New`): Drawings that exist only within the document
- **Drive-linked Drawings** (`Insert → Drawing → From Drive`): Drawings that are separate Google Drawing files

### 2. Complete Object Coverage

The crawler now processes:

- **inlineObjects**: Drawings embedded inline with text
- **positionedObjects**: Absolutely positioned drawings (floating elements)

### 3. Proper Authentication

Uses OAuth 2.0 tokens properly for:
- Drive API exports for Drive-linked drawings
- Authenticated HTTP requests for embedded drawing contentUri URLs

## Implementation Details

### New Methods Added

#### `extract_all_drawings(document, image_folder)`
- Comprehensive method that processes all drawings in a document upfront
- Returns a mapping of object IDs to extracted image file paths
- Handles both `inlineObjects` and `positionedObjects`

#### `_is_drawing_object(embedded_object)`
- Intelligent detection of whether an embedded object contains a drawing
- Checks for drawing-specific properties and URI patterns

#### `_extract_single_drawing(embedded_object, obj_id, image_folder)`
- Extracts a single drawing using the appropriate method
- Automatically chooses between Drive API export or direct download

#### `_download_drive_linked_drawing_v2(drive_file_id, obj_id, image_folder)`
- Uses Drive API `files().export()` with `MediaIoBaseDownload`
- Exports as PNG format for consistent handling

#### `_download_embedded_drawing_v2(content_uri, obj_id, image_folder)`
- Downloads embedded drawings using their short-lived signed URLs
- Properly handles OAuth token authentication

### Integration with Existing Code

#### Enhanced `extract_image_info()` Method
- Now checks pre-extracted drawings first before falling back to legacy methods
- Avoids duplicate downloads and API calls
- Maintains backward compatibility

#### Updated `convert_document_to_markdown()` Method
- Performs comprehensive drawing extraction at the beginning of conversion
- Handles positioned objects separately as they don't belong to specific paragraphs
- Stores drawing map for efficient lookup during content processing

## Technical Implementation Details

### Authentication Flow
```python
# Get OAuth token from existing credentials
credentials = self.docs_service._http.credentials
if not credentials.token:
    credentials.refresh(Request())
token = credentials.token

# Use token for authenticated requests
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(content_uri, headers=headers)
```

### Drive API Export
```python
# Export Google Drawing as PNG
request = self.drive_service.files().export(fileId=drive_file_id, mimeType='image/png')

# Download using MediaIoBaseDownload
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
```

### Drawing Detection Logic
```python
def _is_drawing_object(self, embedded_object):
    # Check for drawing-specific properties
    has_drawing_props = 'embeddedDrawingProperties' in embedded_object
    has_linked_drawing = embedded_object.get('linkedContentReference', {}).get('driveFileId')
    has_drawing_content_uri = embedded_object.get('imageProperties', {}).get('contentUri')
    
    # Check URI patterns for Google drawings
    content_uri = embedded_object.get('imageProperties', {}).get('contentUri', '')
    is_drawing_uri = 'drawings.googleusercontent.com' in content_uri
    
    return has_drawing_props or has_linked_drawing or (has_drawing_content_uri and is_drawing_uri)
```

## Required OAuth Scopes

The implementation requires these OAuth 2.0 scopes:

```python
SCOPES = [
    "https://www.googleapis.com/auth/documents.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]
```

## Experiment Readout Formatting Features

### 1. Advanced Table Processing
- **Bold preservation**: Maintains bold formatting in table cells while fixing spacing issues
- **Proper alignment**: Ensures consistent spacing around table cell separators
- **Percentage formatting**: Correctly handles values like `**+2.64%**` and `**−0.69%**`
- **Currency formatting**: Properly formats values like `**+$3.2M**` and `**$543k**`

### 2. Collapsible Sections
- **Automatic detection**: Identifies sections like "Key metrics" that should be collapsible
- **Details/Summary blocks**: Converts appropriate sections to `<details><summary>` HTML
- **Smart boundaries**: Correctly determines section boundaries and content scope

### 3. Mathematical Notation Support
- **Delta symbols**: Preserves `Δ` and percentage change indicators
- **Statistical significance**: Proper spacing for checkmarks (✅) and crosses (❌)
- **Footnote references**: Maintains `[^1]` style footnote links with proper formatting

### 4. Bold Formatting Intelligence
- **Context-aware spacing**: Handles bold text differently in headers, lists, and tables
- **Symbol preservation**: Avoids breaking mathematical symbols and percentages
- **Merge detection**: Identifies and fixes merged bold elements

## Benefits of This Implementation

### 1. Reliability
- Follows official Google API patterns for drawing extraction
- Handles both embedded and Drive-linked drawings correctly
- Proper error handling and token refresh
- Specialized formatting for data science documents

### 2. Efficiency
- Extracts all drawings upfront to avoid redundant API calls
- Caches results to prevent duplicate downloads
- Uses optimized `MediaIoBaseDownload` for large files
- Multi-pass formatting engine for comprehensive cleanup

### 3. Completeness
- Covers both `inlineObjects` and `positionedObjects`
- Handles all drawing types that Google Docs supports
- Supports experiment readout specific formatting requirements
- Maintains existing functionality while adding new capabilities

### 4. Maintainability
- Clean separation of concerns with dedicated methods
- Comprehensive logging for debugging
- Backward compatibility with existing code
- Modular formatting system for easy extension

## Usage Example

```python
# Initialize converter
converter = EnhancedGoogleDocConverter()
converter.initialize_services(credentials)

# Get document
document = docs_service.documents().get(documentId=doc_id).execute()

# Extract all drawings comprehensively
image_folder = Path("output/images")
drawing_map = converter.extract_all_drawings(document, image_folder)

# Result: {'obj1': 'images/drawing_obj1.png', 'obj2': 'images/drawing_obj2.png'}
```

## Testing

A test script is provided (`test_drawing_extraction.py`) that:
- Tests the drawing detection logic with sample data
- Optionally tests with real Google Docs (requires OAuth)
- Validates the comprehensive extraction workflow

## Troubleshooting

### Common Issues

1. **403 export not allowed**: The Google Drawing file must be shared with the service account
2. **Empty contentUri**: The element may not be a drawing, check if it's a pasted image
3. **Token expiration**: The implementation automatically refreshes tokens when needed

### Debug Logging

The implementation includes comprehensive logging:
```python
self.logger.info(f"📁 Found Drive-linked drawing: {drive_file_id}")
self.logger.info(f"🖼️ Found embedded drawing with contentUri")
self.logger.info(f"✅ Successfully downloaded drawing: {filename}")
```

This allows easy debugging of the extraction process and identification of any issues.
