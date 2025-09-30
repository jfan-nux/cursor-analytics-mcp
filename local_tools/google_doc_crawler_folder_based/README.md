# Google Drive Folder-Based Crawler

A tool for crawling Google Drive folders and converting all documents to markdown while preserving the exact folder structure.

## Features

### 📁 **Folder Traversal**
- Crawls entire Google Drive folder hierarchies
- Supports recursive subfolder navigation
- Mirrors exact Drive folder structure locally

### 📝 **Markdown Conversion**
- Converts all Google Docs to markdown
- Preserves formatting (bold, italic, highlights, tables, lists)
- Downloads and organizes images
- Handles complex document structures

### 🗂️ **Structure Preservation**
- Replicates exact folder hierarchy from Google Drive
- No keyword-based team detection
- Uses actual folder names from Drive
- Maintains relative paths

### 🎯 **Selective Processing**
- Can target specific subfolders
- Navigate to nested folders by path
- Process only what you need

## Usage

### Basic Usage

```python
from local_tools.google_doc_crawler_folder_based import process_google_drive_folder

# Process entire folder
result = process_google_drive_folder(
    folder_url="https://drive.google.com/drive/folders/YOUR_FOLDER_ID",
    output_path="context"
)
```

### Process Specific Subfolder

```python
# Process only a specific subfolder
result = process_google_drive_folder(
    folder_url="https://drive.google.com/drive/folders/YOUR_FOLDER_ID",
    output_path="context",
    subfolder_path="Cx/Growth Product/New User Experience"
)
```

### Using the Class Directly

```python
from local_tools.google_doc_crawler_folder_based import GoogleDriveFolderCrawler

crawler = GoogleDriveFolderCrawler()

# Process folder
result = crawler.process_folder(
    folder_url="https://drive.google.com/drive/folders/YOUR_FOLDER_ID",
    output_path="context",
    subfolder_path="Cx/Growth Product/New User Experience"
)

print(f"Converted {result['documents_converted']} documents")
print(f"Processed {result['folders_processed']} folders")
```

## Output Structure

The tool mirrors the exact folder structure from Google Drive:

```
context/
└── Cx/
    └── Growth Product/
        └── New User Experience/
            ├── images/
            │   ├── chart1.png
            │   └── diagram2.png
            ├── Document-1.md
            ├── Document-2.md
            └── Subfolder/
                ├── images/
                └── Document-3.md
```

## Folder Navigation

Navigate to specific subfolders using slash-separated paths:

```python
# Navigate through multiple levels
subfolder_path="Cx/Growth Product/New User Experience"

# Or deeper nesting
subfolder_path="Team/Project/Phase/Experiments"
```

## Key Differences from Link-Based Crawler

| Feature | Link-Based Crawler | Folder-Based Crawler |
|---------|-------------------|----------------------|
| **Input** | Google Doc with links | Google Drive folder URL |
| **Discovery** | Parse document for links | Drive API folder listing |
| **Organization** | Keyword-based team detection | Exact folder structure mirror |
| **Traversal** | Single-level | Recursive |
| **Output Path** | `context/experiment-readouts/{team}` | `context/{actual_folder_path}` |

## Authentication

Uses the same credential system as the original crawler:

1. Set environment variable: `GOOGLE_DOCS_CREDENTIALS_FILE` or `GOOGLE_SHEET_CREDENTIALS_FILE`
2. Service account needs read access to the Drive folder
3. Supports both OAuth2 and service account credentials

## File Naming

- Uses actual document names from Google Drive
- Sanitizes filenames for filesystem compatibility
- Preserves original folder names
- No quarter detection or title transformation

## Error Handling

- Gracefully handles inaccessible files
- Continues processing if individual documents fail
- Logs detailed error messages
- Returns summary with success/failure counts

## Example Output

```json
{
  "status": "completed",
  "folder_url": "https://drive.google.com/drive/folders/...",
  "subfolder_path": "Cx/Growth Product/New User Experience",
  "output_path": "context/Cx/Growth Product/New User Experience",
  "folders_processed": 5,
  "documents_converted": 23,
  "documents_failed": 1,
  "details": [...]
}
```

## Limitations

- Only processes Google Docs (not Sheets, Slides, etc.)
- Requires Drive API access
- Large folders may take time to process
- Rate limits may apply for very large folders

## Dependencies

- `google-api-python-client`: Google API access
- `google-auth`: Authentication
- All dependencies from `google_doc_crawler` for conversion

## Troubleshooting

### "Folder not found"
- Verify the folder URL is correct
- Check subfolder path spelling and case sensitivity
- Ensure service account has access to the folder

### "Service not initialized"
- Check Google credentials configuration
- Verify Drive API is enabled in your Google Cloud project

### "Access denied"
- Share the folder with the service account email
- Verify folder permissions include read access
