# Google Docs Crawler and Markdown Converter

A comprehensive tool for crawling Google Docs links and converting them to well-formatted markdown files with team-based organization.

## Features

### 🔗 **Link Crawling**
- Extracts all Google Docs links from a master document
- Handles various Google Docs URL formats
- Recursive link discovery from tables and paragraphs

### 📝 **Markdown Conversion**
- Preserves text formatting (bold, italic, highlights)
- Converts tables to markdown syntax
- Maintains bullet points and numbered lists
- Handles headings (H1-H4)
- Preserves links and footnotes
- Supports highlighted text with HTML `<mark>` tags

### 🏢 **Team Organization**
- Automatically organizes files by team structure
- Supports nested teams (e.g., `growth/nux`, `consumer/search`)
- Creates appropriate directory structures
- Handles images in team-specific folders

### 🖼️ **Image Handling**
- Downloads images from Google Drive
- Organizes images in team-specific folders
- Maintains relative paths in markdown
- Graceful fallback for failed downloads

## Team Structure

The tool automatically categorizes documents based on keywords in titles:

```
growth/
├── nux/
├── onboarding/
└── activation/

consumer/
├── search/
├── discovery/
└── recommendations/

merchant/
├── acquisition/
├── retention/
└── tools/

logistics/
├── delivery/
├── assignment/
└── eta/

platform/
├── infrastructure/
├── data/
└── ml/

general/  # Fallback for unrecognized teams
```

## MCP Tools Available

### 1. `crawl_and_convert_google_docs`
**Purpose:** Complete batch processing workflow

**Parameters:**
- `master_doc_url`: URL of Google Doc containing links
- `output_path`: Base directory for saving files (default: "context/experiment-readouts")

**Example Usage:**
```python
crawl_and_convert_google_docs(
    master_doc_url="https://docs.google.com/document/d/1ABC123/edit",
    output_path="context/experiment-readouts"
)
```

### 2. `convert_single_google_doc_to_markdown`
**Purpose:** Convert individual document

**Parameters:**
- `doc_url`: URL of single Google Doc to convert
- `output_path`: Base directory for saving file

**Example Usage:**
```python
convert_single_google_doc_to_markdown(
    doc_url="https://docs.google.com/document/d/1XYZ789/edit",
    output_path="context/experiment-readouts"
)
```

### 3. `get_google_doc_links`
**Purpose:** Preview links without conversion

**Parameters:**
- `doc_url`: URL of Google Doc to scan

**Example Usage:**
```python
get_google_doc_links(
    doc_url="https://docs.google.com/document/d/1ABC123/edit"
)
```

## Example Output Structure

After processing, your files will be organized like this:

```
context/experiment-readouts/
├── growth/
│   ├── nux/
│   │   ├── images/
│   │   │   ├── onboarding-flow.png
│   │   │   └── conversion-chart.png
│   │   ├── App-Download-Prompt-Experiment.md
│   │   └── NUX-Conversion-Analysis.md
│   └── activation/
│       ├── images/
│       └── Activation-Funnel-Study.md
├── consumer/
│   ├── search/
│   │   ├── images/
│   │   └── Search-Algorithm-Improvements.md
│   └── discovery/
│       ├── images/
│       └── Restaurant-Discovery-Analysis.md
└── general/
    ├── images/
    └── Miscellaneous-Experiment.md
```

## Markdown Format Examples

### Text Formatting
```markdown
# Main Heading

## Secondary Heading

This is **bold text** and this is *italic text*.

<mark>This text is highlighted</mark> for emphasis.

[This is a link](https://example.com)
```

### Tables
```markdown
| Metric | Treatment | Control | % Change | Significance |
| --- | --- | --- | --- | --- |
| Order Rate | 15.89% | 15.28% | +2.64% | YES |
| MAU | 11.30% | 11.28% | +0.18% | NO |
```

### Lists
```markdown
- Bullet point 1
- Bullet point 2
  - Nested bullet point
  - Another nested point

1. Numbered item 1
2. Numbered item 2
   1. Nested numbered item
```

### Images
```markdown
![Chart Description](images/conversion-chart.png)
```

## Configuration

The tool uses the same Google credentials configuration as other MCP tools:

1. **Environment Variables** (preferred):
   - `GOOGLE_CREDENTIALS_JSON`: Full JSON credentials as string
   - `GOOGLE_SHEET_CREDENTIALS_FILE`: Path to credentials file

2. **Default File Location**:
   - `credentials/google_sheets_credentials.json`

## Error Handling

The tool includes comprehensive error handling:

- **Invalid URLs**: Graceful handling with clear error messages
- **Access Denied**: Proper error reporting for permission issues
- **Network Issues**: Retry logic for image downloads
- **Malformed Documents**: Continues processing other documents
- **Missing Images**: Fallback text indicators

## Logging

All operations are logged with appropriate levels:
- **INFO**: Successful operations and progress
- **WARNING**: Non-critical issues (e.g., missing images)
- **ERROR**: Critical failures that stop processing

## Usage Tips

1. **Batch Processing**: Use the master document approach for processing multiple experiment readouts
2. **Team Keywords**: Include team names in document titles for proper organization
3. **Image Quality**: Images are downloaded in their original quality
4. **Large Documents**: Processing may take time for documents with many images
5. **Permissions**: Ensure the service account has read access to all documents

## Troubleshooting

### Common Issues:

1. **"Service not initialized"**
   - Check Google credentials configuration
   - Verify service account permissions

2. **"No links found"**
   - Ensure master document contains actual Google Docs links
   - Check that links are properly formatted

3. **"Access denied"**
   - Share documents with the service account email
   - Verify document permissions

4. **"Image download failed"**
   - Check internet connectivity
   - Verify image URLs are accessible

## Dependencies

- `google-api-python-client`: Google API access
- `google-auth`: Authentication
- `requests`: Image downloading
- `pathlib`: File system operations
