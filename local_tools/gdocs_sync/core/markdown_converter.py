"""
Converts between Markdown and Google Docs format.
"""

import re
from typing import List, Dict, Any, Tuple, Optional


class MarkdownConverter:
    """Handles conversion between Markdown and Google Docs structured format."""
    
    def __init__(self):
        self.index = 1  # Track position in document
        self.tab_id = None  # Tab ID for all requests
    
    def markdown_to_gdocs(self, markdown_content: str, image_paths: Dict[str, Dict[str, str]] = None, tab_id: str = None) -> List[Dict]:
        """
        Convert markdown to Google Docs requests.
        Images are inserted as [img][drive_path] markers for Apps Script processing.
        
        Args:
            markdown_content: Markdown text
            image_paths: Dict mapping image paths to {'file_id': id, 'drive_path': path}
            tab_id: Optional tab ID to target specific tab
            
        Returns:
            List of Google Docs API requests
        """
        if image_paths is None:
            image_paths = {}
        
        # Set tab_id for all requests created during this conversion
        self.tab_id = tab_id
        
        requests = []
        self.index = 1
        
        # Split into lines and process
        lines = markdown_content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Skip empty lines
            if not line.strip():
                requests.extend(self._create_paragraph('\n', 'NORMAL_TEXT'))
                i += 1
                continue
            
            # Headers
            if line.startswith('#'):
                level, text = self._parse_header(line)
                requests.extend(self._create_paragraph(text + '\n', f'HEADING_{level}'))
                i += 1
                # Skip blank line after heading (Google Docs has built-in heading spacing)
                if i < len(lines) and not lines[i].strip():
                    i += 1
                continue
            
            # Unordered lists
            if line.strip().startswith(('- ', '* ', '+ ')):
                list_items, i = self._parse_list(lines, i, ordered=False)
                requests.extend(self._create_list(list_items, ordered=False))
                continue
            
            # Ordered lists
            if re.match(r'^\d+\.\s', line.strip()):
                list_items, i = self._parse_list(lines, i, ordered=True)
                requests.extend(self._create_list(list_items, ordered=True))
                continue
            
            # Code blocks
            if line.strip().startswith('```'):
                code_block, i = self._parse_code_block(lines, i)
                requests.extend(self._create_code_block(code_block))
                continue
            
            # Horizontal rules (---, ***, ___)
            if re.match(r'^[\s]*[-*_]{3,}[\s]*$', line):
                requests.extend(self._create_horizontal_rule())
                i += 1
                # Skip blank line after horizontal rule if next non-blank line is a heading
                if i < len(lines) and not lines[i].strip():
                    # Peek ahead to see if next non-blank line is a heading
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].startswith('#'):
                        i += 1  # Skip the blank line
                continue
            
            # Images - insert as [img][drive_path] markers
            image_match = re.match(r'!\[([^\]]*)\]\(([^\)]+)\)', line.strip())
            if image_match:
                alt_text = image_match.group(1)
                image_ref = image_match.group(2)
                
                # Check if we have a Drive path for this image
                drive_path = None
                for img_path, img_info in image_paths.items():
                    if image_ref in img_path or img_path.endswith(image_ref):
                        drive_path = img_info.get('drive_path')
                        break
                
                if drive_path:
                    # Insert marker for Apps Script to process
                    marker = f'[img][{drive_path}]\n'
                    requests.extend(self._create_paragraph(marker, 'NORMAL_TEXT'))
                else:
                    # External image or not found
                    if image_ref.startswith(('http://', 'https://')):
                        requests.extend(self._create_paragraph(f'[Image: {alt_text}]({image_ref})\n', 'NORMAL_TEXT'))
                    else:
                        # Image not found, add as text
                        requests.extend(self._create_paragraph(f'[Image not found: {alt_text}]\n', 'NORMAL_TEXT'))
                
                i += 1
                continue
            
            # Tables (basic support)
            if '|' in line and i + 1 < len(lines) and '|' in lines[i + 1]:
                table_lines, i = self._parse_table(lines, i)
                requests.extend(self._create_table(table_lines))
                continue
            
            # Regular paragraph with inline formatting
            requests.extend(self._create_paragraph_with_formatting(line + '\n'))
            i += 1
        
        return requests
    
    def _parse_header(self, line: str) -> Tuple[int, str]:
        """Parse header level and text."""
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            return min(level, 6), text
        return 1, line
    
    def _parse_list(self, lines: List[str], start_idx: int, ordered: bool) -> Tuple[List[Tuple[str, int]], int]:
        """
        Parse consecutive list items with indentation levels.
        
        Returns:
            Tuple of (list of (text, indent_level) tuples, next_index)
            indent_level is 0 for top-level, 1 for first nesting, etc.
        """
        items = []
        i = start_idx
        
        if ordered:
            pattern = r'^\d+\.\s+(.*)'
        else:
            pattern = r'^[-*+]\s+(.*)'
        
        while i < len(lines):
            line = lines[i]
            stripped_line = line.strip()
            
            if not stripped_line:
                i += 1
                break
            
            # Calculate indentation level (number of leading spaces divided by 2)
            leading_spaces = len(line) - len(line.lstrip())
            indent_level = leading_spaces // 2
            
            match = re.match(pattern, stripped_line)
            if match:
                items.append((match.group(1), indent_level))
                i += 1
            else:
                break
        
        return items, i
    
    def _parse_code_block(self, lines: List[str], start_idx: int) -> Tuple[str, int]:
        """Parse code block."""
        code_lines = []
        i = start_idx + 1  # Skip opening ```
        
        while i < len(lines):
            if lines[i].strip().startswith('```'):
                i += 1
                break
            code_lines.append(lines[i])
            i += 1
        
        return '\n'.join(code_lines), i
    
    def _parse_table(self, lines: List[str], start_idx: int) -> Tuple[List[List[str]], int]:
        """Parse markdown table."""
        table_rows = []
        i = start_idx
        
        while i < len(lines) and '|' in lines[i]:
            # Skip separator line
            if re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i]):
                i += 1
                continue
            
            # Parse row - handle escaped pipes \|
            # First, temporarily replace \| with a placeholder
            row_text = lines[i].replace(r'\|', '{{PIPE}}')
            # Split on unescaped pipes
            cells = [cell.strip() for cell in row_text.split('|')[1:-1]]
            # Restore the literal pipes
            cells = [cell.replace('{{PIPE}}', '|') for cell in cells]
            if cells:
                table_rows.append(cells)
            i += 1
        
        return table_rows, i
    
    def _make_location(self, index: int = None) -> Dict:
        """
        Create a location object, optionally including tab_id.
        
        Args:
            index: Document index (uses self.index if not provided)
            
        Returns:
            Location dict with index and optional tab_id
        """
        if index is None:
            index = self.index
        
        location = {'index': index}
        if self.tab_id:
            location['tabId'] = self.tab_id
        return location
    
    def _make_range(self, start_index: int, end_index: int) -> Dict:
        """
        Create a range object, optionally including tab_id.
        
        Args:
            start_index: Start index
            end_index: End index
            
        Returns:
            Range dict with indices and optional tab_id
        """
        range_obj = {
            'startIndex': start_index,
            'endIndex': end_index
        }
        if self.tab_id:
            range_obj['tabId'] = self.tab_id
        return range_obj
    
    def _create_paragraph(self, text: str, style: str) -> List[Dict]:
        """Create a simple paragraph."""
        requests = [
            {
                'insertText': {
                    'location': self._make_location(),
                    'text': text
                }
            }
        ]
        
        text_len = len(text)
        
        if style != 'NORMAL_TEXT':
            requests.append({
                'updateParagraphStyle': {
                    'range': self._make_range(self.index, self.index + text_len),
                    'paragraphStyle': {
                        'namedStyleType': style
                    },
                    'fields': 'namedStyleType'
                }
            })
        
        self.index += text_len
        return requests
    
    def _create_paragraph_with_formatting(self, text: str) -> List[Dict]:
        """Create paragraph with inline formatting (bold, italic, links)."""
        requests = []
        
        # First, collect all formatting markers and their positions in ORIGINAL text
        bold_ranges = []
        italic_ranges = []
        link_ranges = []
        
        # Find bold markers
        for match in re.finditer(r'\*\*(.+?)\*\*', text):
            bold_ranges.append((match.start(), match.end(), match.group(1)))
        
        # Find italic markers (not part of bold)
        for match in re.finditer(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', text):
            italic_ranges.append((match.start(), match.end(), match.group(1)))
        
        # Find links (separate mailto links for person chip handling)
        person_ranges = []
        for match in re.finditer(r'\[([^\]]+)\]\(mailto:([^\)]+)\)', text):
            person_ranges.append((match.start(), match.end(), match.group(1), match.group(2)))
        
        # Find regular links (exclude mailto links which are handled separately)
        for match in re.finditer(r'\[([^\]]+)\]\(([^\)]+)\)', text):
            url = match.group(2)
            if not url.startswith('mailto:'):
                link_ranges.append((match.start(), match.end(), match.group(1), url))
        
        # Remove markdown formatting from text, converting mailto links to person markers
        clean_text = text
        # Remove bold markers
        clean_text = re.sub(r'\*\*(.+?)\*\*', r'\1', clean_text)
        # Remove italic markers
        clean_text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\1', clean_text)
        # Convert mailto links to person markers for Apps Script processing
        clean_text = re.sub(r'\[([^\]]+)\]\(mailto:([^\)]+)\)', r'[person:\2:\1]', clean_text)
        # Remove regular link markers but keep text
        clean_text = re.sub(r'\[([^\]]+)\]\((?!mailto:)[^\)]+\)', r'\1', clean_text)
        
        # Insert clean text
        requests.append({
            'insertText': {
                'location': self._make_location(),
                'text': clean_text
            }
        })
        
        start_index = self.index
        
        # Now apply formatting to the clean text positions
        # We need to calculate new positions after removing markers
        offset = 0
        
        # Apply bold formatting
        for orig_start, orig_end, content in bold_ranges:
            # Calculate position in clean text
            markers_before = clean_text[:orig_start - offset].count('**') * 2
            actual_start = start_index + orig_start - offset
            actual_end = actual_start + len(content)
            
            # Find actual position in clean text
            clean_pos = 0
            orig_pos = 0
            while orig_pos < orig_start:
                if text[orig_pos:orig_pos+2] == '**':
                    orig_pos += 2
                else:
                    clean_pos += 1
                    orig_pos += 1
            
            actual_start = start_index + clean_pos
            actual_end = actual_start + len(content)
            
            requests.append({
                'updateTextStyle': {
                    'range': self._make_range(actual_start, actual_end),
                    'textStyle': {
                        'bold': True
                    },
                    'fields': 'bold'
                }
            })
        
        # Apply italic formatting
        for orig_start, orig_end, content in italic_ranges:
            # Calculate position in clean text
            clean_pos = 0
            orig_pos = 0
            while orig_pos < orig_start:
                if text[orig_pos:orig_pos+2] == '**':
                    orig_pos += 2
                elif text[orig_pos] == '*':
                    orig_pos += 1
                else:
                    clean_pos += 1
                    orig_pos += 1
            
            actual_start = start_index + clean_pos
            actual_end = actual_start + len(content)
            
            requests.append({
                'updateTextStyle': {
                    'range': self._make_range(actual_start, actual_end),
                    'textStyle': {
                        'italic': True
                    },
                    'fields': 'italic'
                }
            })
        
        # Apply links
        for orig_start, orig_end, link_text, url in link_ranges:
            # Calculate position in clean text
            clean_pos = 0
            orig_pos = 0
            while orig_pos < orig_start:
                if text[orig_pos:orig_pos+2] == '**':
                    orig_pos += 2
                elif text[orig_pos] == '*':
                    orig_pos += 1
                elif text[orig_pos] == '[':
                    # Part of a link
                    clean_pos += 1
                    orig_pos += 1
                else:
                    clean_pos += 1
                    orig_pos += 1
            
            actual_start = start_index + clean_pos
            actual_end = actual_start + len(link_text)
            
            requests.append({
                'updateTextStyle': {
                    'range': self._make_range(actual_start, actual_end),
                    'textStyle': {
                        'link': {
                            'url': url
                        }
                    },
                    'fields': 'link'
                }
            })
        
        self.index += len(clean_text)
        return requests
    
    def _create_list(self, items: List[Tuple[str, int]], ordered: bool) -> List[Dict]:
        """
        Create bulleted or numbered list with proper nesting levels.
        
        Per Google Docs API best practice: insert ALL text at once with tabs for nesting,
        then apply createParagraphBullets to the entire range.
        
        Args:
            items: List of (text, indent_level) tuples
            ordered: True for numbered lists, False for bullet lists
        """
        requests = []
        
        if not items:
            return requests
        
        # Step 1: Build the full list text with tabs for nesting
        # Also track formatting positions for bold/italic
        # Note: tabs will be consumed by createParagraphBullets, so we track
        # positions in the "post-consumption" text (without tabs)
        full_text = ""
        formatting_info = []  # List of (offset_after_tabs_consumed, item_text, clean_item)
        content_position = 0  # Track position in text AFTER tabs are consumed
        
        for item_text, indent_level in items:
            # Remove markdown formatting from item text
            clean_item = item_text
            clean_item = re.sub(r'\*\*(.+?)\*\*', r'\1', clean_item)
            clean_item = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\1', clean_item)
            # Convert mailto links to person markers for Apps Script processing
            clean_item = re.sub(r'\[([^\]]+)\]\(mailto:([^\)]+)\)', r'[person:\2:\1]', clean_item)
            # Remove regular link markers but keep text
            clean_item = re.sub(r'\[([^\]]+)\]\((?!mailto:)[^\)]+\)', r'\1', clean_item)
            
            # Prepend tabs for nesting level
            tabs = '\t' * indent_level
            line = tabs + clean_item + '\n'
            
            # Track where this item's content starts AFTER tabs are consumed
            formatting_info.append((content_position, item_text, clean_item))
            
            # Update content_position for next item (tabs don't count, they get consumed)
            content_position += len(clean_item) + 1  # +1 for newline
            
            full_text += line
        
        # Step 2: Insert all text at once
        start_index = self.index
        requests.append({
            'insertText': {
                'location': self._make_location(),
                'text': full_text
            }
        })
        
        # Step 3: Apply bullets to the entire range - this converts tabs to nesting
        requests.append({
            'createParagraphBullets': {
                'range': self._make_range(start_index, start_index + len(full_text)),
                'bulletPreset': 'NUMBERED_DECIMAL_NESTED' if ordered else 'BULLET_DISC_CIRCLE_SQUARE'
            }
        })
        
        # Step 4: Apply bold/italic formatting to each item
        # content_offset is the position in the document AFTER tabs are consumed
        for content_offset, item_text, clean_item in formatting_info:
            item_start = start_index + content_offset
            
            # Apply bold formatting
            for match in re.finditer(r'\*\*(.+?)\*\*', item_text):
                clean_pos = 0
                orig_pos = 0
                while orig_pos < match.start():
                    if item_text[orig_pos:orig_pos+2] == '**':
                        orig_pos += 2
                    else:
                        clean_pos += 1
                        orig_pos += 1
                
                content = match.group(1)
                actual_start = item_start + clean_pos
                actual_end = actual_start + len(content)
                
                requests.append({
                    'updateTextStyle': {
                        'range': self._make_range(actual_start, actual_end),
                        'textStyle': {'bold': True},
                        'fields': 'bold'
                    }
                })
            
            # Apply italic formatting
            for match in re.finditer(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', item_text):
                clean_pos = 0
                orig_pos = 0
                while orig_pos < match.start():
                    if item_text[orig_pos:orig_pos+2] == '**':
                        orig_pos += 2
                    elif item_text[orig_pos] == '*':
                        orig_pos += 1
                    else:
                        clean_pos += 1
                        orig_pos += 1
                
                content = match.group(1)
                actual_start = item_start + clean_pos
                actual_end = actual_start + len(content)
                
                requests.append({
                    'updateTextStyle': {
                        'range': self._make_range(actual_start, actual_end),
                        'textStyle': {'italic': True},
                        'fields': 'italic'
                    }
                })
        
        # Update index - tabs are consumed by createParagraphBullets
        # Count actual characters after tab consumption
        total_content_len = sum(len(clean) + 1 for _, _, clean in formatting_info)  # +1 for newlines
        self.index += total_content_len
        
        return requests
    
    def _create_code_block(self, code: str) -> List[Dict]:
        """Create code block (as monospace text)."""
        text = code + '\n'
        requests = [
            {
                'insertText': {
                    'location': self._make_location(),
                    'text': text
                }
            },
            {
                'updateTextStyle': {
                    'range': self._make_range(self.index, self.index + len(text)),
                    'textStyle': {
                        'weightedFontFamily': {
                            'fontFamily': 'Courier New'
                        },
                        'fontSize': {
                            'magnitude': 10,
                            'unit': 'PT'
                        }
                    },
                    'fields': 'weightedFontFamily,fontSize'
                }
            }
        ]
        
        self.index += len(text)
        return requests
    
    def _create_horizontal_rule(self) -> List[Dict]:
        """Create a horizontal rule."""
        # Insert a horizontal line using a paragraph with bottom border
        text = '\n'
        requests = [
            {
                'insertText': {
                    'location': self._make_location(),
                    'text': text
                }
            },
            {
                'updateParagraphStyle': {
                    'range': self._make_range(self.index, self.index + len(text)),
                    'paragraphStyle': {
                        'borderBottom': {
                            'color': {
                                'color': {
                                    'rgbColor': {
                                        'red': 0.8,
                                        'green': 0.8,
                                        'blue': 0.8
                                    }
                                }
                            },
                            'width': {
                                'magnitude': 1.5,
                                'unit': 'PT'
                            },
                            'dashStyle': 'SOLID',
                            'padding': {
                                'magnitude': 2,
                                'unit': 'PT'
                            }
                        }
                    },
                    'fields': 'borderBottom'
                }
            }
        ]
        
        self.index += len(text)
        return requests
    
    def _create_image(self, file_id: str, alt_text: str) -> List[Dict]:
        """Create inline image from Drive file."""
        requests = [
            {
                'insertInlineImage': {
                    'location': self._make_location(),
                    'uri': f'https://drive.google.com/uc?id={file_id}',
                    'objectSize': {
                        'width': {
                            'magnitude': 400,
                            'unit': 'PT'
                        }
                    }
                }
            }
        ]
        
        self.index += 1  # Images take 1 character
        
        # Add newline after image
        requests.append({
            'insertText': {
                'location': self._make_location(),
                'text': '\n'
            }
        })
        self.index += 1
        
        return requests
    
    def _create_image_by_url(self, url: str, alt_text: str) -> List[Dict]:
        """Create inline image from external URL."""
        return self._create_paragraph(f'[Image: {alt_text}]({url})\n', 'NORMAL_TEXT')
    
    def _create_table(self, rows: List[List[str]]) -> List[Dict]:
        """Create table marker for Apps Script to process."""
        requests = []
        
        if not rows:
            return requests
        
        # Detect repeated values in first column for cell merging
        # Track runs of identical values in column 0
        merge_info = {}  # {row_index: merge_count} for cells that start a merge
        if len(rows) > 1:
            i = 1  # Start from second row (skip header)
            while i < len(rows):
                if rows[i] and rows[i][0]:
                    current_val = rows[i][0].strip()
                    # Look for consecutive identical values
                    merge_count = 1
                    j = i + 1
                    while j < len(rows) and rows[j] and rows[j][0] and rows[j][0].strip() == current_val:
                        merge_count += 1
                        j += 1
                    if merge_count > 1:
                        merge_info[i] = merge_count
                        i = j  # Skip past the merged rows
                    else:
                        i += 1
                else:
                    i += 1
        
        # Convert table to format with row markers for Apps Script
        csv_rows = []
        for row_idx, row in enumerate(rows):
            # Escape special characters in cells and convert markdown formatting to markers
            escaped_cells = []
            for col_idx, cell in enumerate(row):
                # Convert markdown formatting to markers that survive pipe-escaping
                clean_cell = cell
                clean_cell = re.sub(r'\*\*(.+?)\*\*', r'{B}\1{/B}', clean_cell)  # Bold -> {B}text{/B}
                clean_cell = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'{I}\1{/I}', clean_cell)  # Italic
                # Convert mailto links to person markers
                clean_cell = re.sub(r'\[([^\]]+)\]\(mailto:([^\)]+)\)', r'[person:\2:\1]', clean_cell)
                # Strip regular links
                clean_cell = re.sub(r'\[([^\]]+)\]\((?!mailto:)[^\)]+\)', r'\1', clean_cell)
                
                # Replace | with &#124; and newlines with spaces
                escaped = clean_cell.replace('|', '&#124;').replace('\n', ' ').strip()
                
                # Add merge marker for first column cells that start a merge
                if col_idx == 0 and row_idx in merge_info:
                    escaped = f'[merge:{merge_info[row_idx]}]{escaped}'
                # Mark cells that are part of a merge (should be empty after merging)
                elif col_idx == 0:
                    for start_row, count in merge_info.items():
                        if start_row < row_idx < start_row + count:
                            escaped = '[merged]'  # This cell will be merged away
                            break
                
                escaped_cells.append(escaped)
            # Prefix each row with [row] marker for identification during cleanup
            csv_rows.append('[row]' + '|'.join(escaped_cells))
        
        table_data = '\n'.join(csv_rows)
        
        # Insert marker for Apps Script to process
        marker = f'[table]\n{table_data}\n[/table]\n'
        requests.extend(self._create_paragraph(marker, 'NORMAL_TEXT'))
        
        return requests
    
    def gdocs_to_markdown(self, doc_content: Dict) -> str:
        """
        Convert Google Docs content to Markdown.
        
        Args:
            doc_content: Google Docs document structure
            
        Returns:
            Markdown text
        """
        markdown_lines = []
        
        body = doc_content.get('body', {})
        content = body.get('content', [])
        
        for element in content:
            if 'paragraph' in element:
                md_line = self._paragraph_to_markdown(element['paragraph'])
                if md_line:
                    markdown_lines.append(md_line)
            elif 'table' in element:
                md_table = self._table_to_markdown(element['table'])
                # Add blank line before table if previous line isn't empty
                if markdown_lines and markdown_lines[-1].strip():
                    markdown_lines.append('')
                markdown_lines.extend(md_table)
                # Add blank line after table
                markdown_lines.append('')
            elif 'sectionBreak' in element:
                markdown_lines.append('')
        
        return '\n'.join(markdown_lines)
    
    def _paragraph_to_markdown(self, paragraph: Dict) -> str:
        """Convert paragraph to markdown."""
        elements = paragraph.get('elements', [])
        style = paragraph.get('paragraphStyle', {})
        named_style = style.get('namedStyleType', 'NORMAL_TEXT')
        
        # Build text with formatting
        text_parts = []
        for element in elements:
            text_run = element.get('textRun')
            if text_run:
                content = text_run.get('content', '')
                text_style = text_run.get('textStyle', {})
                
                # Apply inline formatting while preserving leading/trailing whitespace
                # This prevents "**word1****word2**" when words should be "**word1** **word2**"
                if text_style.get('bold') or text_style.get('italic') or 'link' in text_style:
                    # Extract leading/trailing whitespace
                    leading_space = ''
                    trailing_space = ''
                    stripped = content.strip()
                    if content and stripped:
                        leading_space = content[:len(content) - len(content.lstrip())]
                        trailing_space = content[len(content.rstrip()):]
                    
                    if stripped:  # Only wrap if there's actual content
                        if text_style.get('bold') and text_style.get('italic'):
                            content = f'{leading_space}***{stripped}***{trailing_space}'
                        elif text_style.get('bold'):
                            content = f'{leading_space}**{stripped}**{trailing_space}'
                        elif text_style.get('italic'):
                            content = f'{leading_space}*{stripped}*{trailing_space}'
                        else:
                            content = f'{leading_space}{stripped}{trailing_space}'
                        
                        # Handle links (apply after bold/italic)
                        if 'link' in text_style:
                            url = text_style['link'].get('url', '')
                            # Re-wrap with link, preserving spaces outside
                            inner = content.strip()
                            content = f'{leading_space}[{inner}]({url}){trailing_space}'
                
                text_parts.append(content)
            
            # Handle inline objects (images)
            inline_object = element.get('inlineObjectElement')
            if inline_object:
                text_parts.append('[Image]')
            
            # Handle person chips (email mentions / @mentions)
            person = element.get('person')
            if person:
                person_props = person.get('personProperties', {})
                name = person_props.get('name', '')
                email = person_props.get('email', '')
                if name and email:
                    # Format as a mailto link with the person's name
                    text_parts.append(f'[{name}](mailto:{email})')
                elif email:
                    text_parts.append(f'[{email}](mailto:{email})')
                elif name:
                    text_parts.append(name)
            
            # Handle rich links (document links, smart chips for URLs)
            rich_link = element.get('richLink')
            if rich_link:
                link_props = rich_link.get('richLinkProperties', {})
                title = link_props.get('title', '')
                uri = link_props.get('uri', '')
                if title and uri:
                    text_parts.append(f'[{title}]({uri})')
                elif uri:
                    text_parts.append(f'[{uri}]({uri})')
                elif title:
                    text_parts.append(title)
        
        text = ''.join(text_parts).strip()
        
        # Apply paragraph style
        if named_style.startswith('HEADING_'):
            level = named_style.split('_')[1]
            return f'{"#" * int(level)} {text}'
        elif 'bullet' in paragraph:
            # List item with nesting level
            bullet = paragraph.get('bullet', {})
            nesting_level = bullet.get('nestingLevel', 0)
            indent = '  ' * nesting_level  # 2 spaces per nesting level
            return f'{indent}- {text}'
        else:
            return text
    
    def _table_to_markdown(self, table: Dict) -> List[str]:
        """Convert table to markdown with proper handling of merged cells."""
        rows = table.get('tableRows', [])
        md_rows = []
        
        # First pass: determine the actual number of columns and build cell grid
        # Track cells that span multiple rows so we can repeat their content
        num_cols = 0
        for row in rows:
            col_count = 0
            for cell in row.get('tableCells', []):
                col_span = cell.get('tableCellStyle', {}).get('columnSpan', 1)
                col_count += col_span
            num_cols = max(num_cols, col_count)
        
        # Track row spans: {(row_idx, col_idx): (content, remaining_rows)}
        row_span_tracker = {}
        
        for row_idx, row in enumerate(rows):
            cells = row.get('tableCells', [])
            cell_texts = []
            col_idx = 0
            cell_iter = iter(cells)
            
            while col_idx < num_cols:
                # Check if there's a row span from a previous row
                if (row_idx, col_idx) in row_span_tracker:
                    content, remaining = row_span_tracker[(row_idx, col_idx)]
                    cell_texts.append(content)
                    # Propagate to next row if still spanning
                    if remaining > 1:
                        row_span_tracker[(row_idx + 1, col_idx)] = (content, remaining - 1)
                    # Consume the placeholder cell from the iterator (Google Docs includes empty cells for merged positions)
                    try:
                        next(cell_iter)
                    except StopIteration:
                        pass
                    col_idx += 1
                    continue
                
                # Get next cell from iterator
                try:
                    cell = next(cell_iter)
                except StopIteration:
                    # No more cells, fill with empty
                    cell_texts.append('')
                    col_idx += 1
                    continue
                
                # Extract cell content
                content_elements = cell.get('content', [])
                cell_text = ''
                for element in content_elements:
                    if 'paragraph' in element:
                        cell_text += self._paragraph_to_markdown(element['paragraph'])
                cell_text = cell_text.strip()
                
                # Get span info
                cell_style = cell.get('tableCellStyle', {})
                col_span = cell_style.get('columnSpan', 1)
                row_span = cell_style.get('rowSpan', 1)
                
                # Add the cell content
                cell_texts.append(cell_text)
                
                # If row span > 1, track for subsequent rows
                if row_span > 1:
                    for future_row in range(1, row_span):
                        row_span_tracker[(row_idx + future_row, col_idx)] = (cell_text, row_span - future_row)
                
                col_idx += 1
                
                # Handle column span by adding empty cells
                for _ in range(1, col_span):
                    if col_idx < num_cols:
                        cell_texts.append('')
                        col_idx += 1
            
            # Ensure consistent column count
            while len(cell_texts) < num_cols:
                cell_texts.append('')
            
            md_rows.append('| ' + ' | '.join(cell_texts) + ' |')
            
            # Add separator after header row
            if row_idx == 0:
                md_rows.append('|' + '---|' * len(cell_texts))
        
        # Trim trailing empty columns from all rows
        if md_rows:
            # Find the last column with any content
            max_content_col = 0
            for row in md_rows:
                if row.startswith('|') and not row.startswith('|---'):
                    cells = [c.strip() for c in row.split('|')[1:-1]]  # Skip first/last empty from split
                    for i, cell in enumerate(cells):
                        if cell:
                            max_content_col = max(max_content_col, i)
            
            # Rebuild rows with only needed columns (at least max_content_col + 1 columns)
            trimmed_rows = []
            for row in md_rows:
                if row.startswith('|---'):
                    # Separator row - adjust to match column count
                    trimmed_rows.append('|' + '---|' * (max_content_col + 1))
                else:
                    cells = [c.strip() for c in row.split('|')[1:-1]]
                    trimmed_cells = cells[:max_content_col + 1]
                    trimmed_rows.append('| ' + ' | '.join(trimmed_cells) + ' |')
            md_rows = trimmed_rows
        
        return md_rows
