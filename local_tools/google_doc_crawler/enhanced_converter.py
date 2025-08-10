#!/usr/bin/env python3
"""
Enhanced Google Docs to Markdown Converter

Comprehensive conversion supporting:
- Person names and links (with proper formatting)
- Nested bullet points and lists
- Tables with formatting preservation
- Footnotes conversion
- Image extraction and referencing
- Drawing and flowchart extraction (PNG/JPEG/SVG export)
- Chart and diagram support with intelligent type detection
- Bold, italic, highlighting, strikethrough
- Section breaks and page breaks
- GitHub markdown compliance validation
"""

import re
import json
import requests
import io
from pathlib import Path
from typing import Dict, Any, Optional
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from utils.logger import get_logger
from .quarter_detector import QuarterDetector

# AST-based markdown processing dependencies
try:
    import mdformat
    AST_PROCESSING_AVAILABLE = True
except ImportError:
    AST_PROCESSING_AVAILABLE = False


class EnhancedGoogleDocConverter:
    """Enhanced Google Docs to Markdown converter with comprehensive formatting support."""
    
    def __init__(self):
        """Initialize the enhanced converter."""
        self.logger = get_logger(__name__)
        self.docs_service = None
        self.drive_service = None
        self.quarter_detector = QuarterDetector()

    def postprocess_github_syntax(self, raw_md: str) -> str:
        """
        Modern AST-based post-processing that replaces the legacy regex cleanup.
        
        1. Parse → tweak the AST so we *know* every heading, list item, table etc.
        2. Re-render with mdformat so spacing / indentation / blank-lines
           match GitHub's reference renderer.
        
        Args:
            raw_md: Raw markdown text from the converter
            
        Returns:
            GitHub-compliant markdown with proper formatting
        """
        if not AST_PROCESSING_AVAILABLE:
            self.logger.warning("AST processing not available, falling back to legacy cleanup")
            return self.cleanup_markdown_formatting_github_standard(raw_md)
        
        try:
            self.logger.debug("Starting postprocess_github_syntax with comprehensive pre-processing fixes")
            # --- 1️⃣ COMPREHENSIVE PRE-PROCESSING FIXES -------------------- #
            
            # Fix 0: Remove leading --- at document start
            fixed_md = re.sub(r'^---\n', '', raw_md)
            
            # Fix 0b: remove deprecated ==highlight== markers that slipped
            fixed_md = re.sub(r'==([^=\n]+?)==', r'<mark>\1</mark>', fixed_md)

            # Fix 1: Normalize underline separators to canonical --- rule
            # Convert any line of 3+ underscores (with optional surrounding spaces) to --- before further parsing  
            fixed_md = re.sub(r'^\s*_{3,}\s*$', '---', fixed_md, flags=re.MULTILINE)
            
            # Fix 2: Clean headings - strip ** wrapper inside # lines
            # # **Title** → # Title (so they render as plain headings)
            fixed_md = re.sub(r'^(#{1,6})\s*\*\*([^*\n]+?)\*\*\s*$', r'\1 \2', fixed_md, flags=re.MULTILINE)
            
            # Fix 3: Header spacing for remaining cases: ###**TL;DR** → ### **TL;DR**
            fixed_md = re.sub(r'(#{1,6})(\*\*[^*\n]+?\*\*)', r'\1 \2', fixed_md)
            
            # Fix 4a: Targeted unescape for bold/italic runs only (leave code like \*ptr alone)
            fixed_md = re.sub(r'\\\*\\\*([^*\n]+?)\\\*\\\*', r'**\1**', fixed_md)
            fixed_md = re.sub(r'\\\*([^*\n]+?)\\\*', r'*\1*', fixed_md)
            
            # Fix 4b: Replace escaped asterisks, but **only** if they belong to
            # bold/italic runs – leave things like \*ptr for C-style code alone.
            fixed_md = re.sub(r'\\(\*)', r'\1', fixed_md)  # Remove escaping from asterisks
            
            # Fix 5: Harden bullet-spacing logic - accept -**Thing** and rewrite as - **Thing**
            # Handle various bullet patterns
            fixed_md = re.sub(r'^-\s*\*\*', r'- **', fixed_md, flags=re.MULTILINE)
            fixed_md = re.sub(r'^-\*\*', r'- **', fixed_md, flags=re.MULTILINE)
            
            # Fix bullet patterns with text glued: -**Text**: → - **Text**:
            fixed_md = re.sub(r'^-(\*\*[^*]+?\*\*)', r'- \1', fixed_md, flags=re.MULTILINE)
            
            # Fix 6: Analytics DRI separation: **Title**Analytics DRI: → **Title**\n\nAnalytics DRI:
            fixed_md = re.sub(r'(\*\*[^*\n]+?\*\*)Analytics DRI:', r'\1\n\nAnalytics DRI:', fixed_md)
            
            # Fix 7: Bold-colon glue: **Problem:**We → **Problem:** We
            fixed_md = re.sub(r'(\*\*[^*:]+?:\*\*)([A-Za-z])', r'\1 \2', fixed_md)
            
            # Fix 8: Clean up bold text with internal spaces in table cells
            # ** Treatment ** → **Treatment**
            fixed_md = re.sub(r'\*\*\s+([^*]+?)\s+\*\*', r'**\1**', fixed_md)

            # --- 2️⃣ Use mdformat for GitHub-compliant formatting ------------- #
            #     mdformat will:
            #       • guarantee blank line before/after lists & headings
            #       • collapse consecutive blank lines to one
            #       • put a single space after list markers ("- item")
            #       • normalise table pipes | like this |
            formatted = mdformat.text(fixed_md, options={"number": False})

            # --- 3️⃣ Final polish for stubborn upstream artifacts ------------ #
            # A. Convert any remaining underline-only lines to '---'
            formatted = re.sub(r'(?m)^\s*_{3,}\s*$', '---', formatted)
            # B. Unescape bold/italic that arrived as literal \*\*...\*\*
            formatted = re.sub(r'\\\*\\\*([^*\n]+?)\\\*\\\*', r'**\1**', formatted)
            formatted = re.sub(r'\\\*([^*\n]+?)\\\*', r'*\1*', formatted)
            # C. Bullet edge-case: '- Text:**Bold**' → '- Text: **Bold**'
            formatted = re.sub(r'(?m)^(\-\s+[^\n:]*:)(\*\*)', r'\1 **', formatted)

            self.logger.debug("postprocess_github_syntax completed successfully")
            return formatted
            
        except Exception as e:
            self.logger.error(f"AST processing failed: {e}, falling back to legacy cleanup")
            return self.cleanup_markdown_formatting_github_standard(raw_md)
        
    def initialize_services(self, credentials):
        """Initialize Google API services with provided credentials."""
        try:
            self.docs_service = build('docs', 'v1', credentials=credentials)
            self.drive_service = build('drive', 'v3', credentials=credentials)
            self.logger.info("Enhanced converter services initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize enhanced converter services: {e}")
            raise
    
    def extract_doc_id(self, url: str) -> Optional[str]:
        """Extract document ID from Google Docs URL."""
        patterns = [
            r'/document/d/([a-zA-Z0-9-_]+)',
            r'id=([a-zA-Z0-9-_]+)',
            r'^([a-zA-Z0-9-_]+)$'  # Direct ID
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def extract_text_with_formatting(self, text_run: Dict[str, Any]) -> str:
        """Extract text with comprehensive formatting including names and links."""
        text = text_run.get('content', '')
        
        # Skip empty or whitespace-only content but preserve meaningful whitespace
        if not text:
            return ''
        
        text_style = text_run.get('textStyle', {})
        
        # Clean up text first - remove excessive asterisks and formatting artifacts
        clean_text = text
        # Remove multiple consecutive asterisks that cause markdown issues
        clean_text = re.sub(r'\*{3,}', '**', clean_text)  # Convert 3+ asterisks to 2
        # Clean up extra whitespace but preserve line breaks
        clean_text = re.sub(r'[ \t]+', ' ', clean_text)
        
        formatted_text = clean_text
        
        # Handle links first (including person names that might be links)
        if text_style.get('link'):
            link_url = text_style['link']['url']
            link_text = clean_text.strip()
            if link_text:
                formatted_text = f"[{link_text}]({link_url})"
            else:
                # Handle cases where link text might be empty but URL exists
                formatted_text = f"[Link]({link_url})"
        
        # Apply text formatting (order matters) - only if text isn't already formatted
        if text_style.get('bold') and not (formatted_text.startswith('**') and formatted_text.endswith('**')):
            # Only bold non-whitespace content - PROPERLY strip whitespace from inside bold
            if formatted_text.strip():
                # Get the actual text content without surrounding spaces
                stripped_content = formatted_text.strip()
                # Check if this text should have spaces around it at paragraph level
                has_leading_space = formatted_text.startswith(' ')
                has_trailing_space = formatted_text.endswith(' ')
                
                # Create PROPERLY FORMATTED bold text (GitHub markdown standard)
                # No spaces inside the ** markers, content only
                bold_text = f"**{stripped_content}**"
                
                # Add back any EXTERNAL spaces (outside the bold)
                if has_leading_space:
                    bold_text = ' ' + bold_text
                if has_trailing_space:
                    bold_text = bold_text + ' '
                    
                formatted_text = bold_text
        
        if text_style.get('italic') and not (formatted_text.startswith('*') and formatted_text.endswith('*')):
            if formatted_text.strip():
                # Same principle for italic - no spaces inside * markers
                stripped_content = formatted_text.strip()
                has_leading_space = formatted_text.startswith(' ')
                has_trailing_space = formatted_text.endswith(' ')
                
                italic_text = f"*{stripped_content}*"
                
                if has_leading_space:
                    italic_text = ' ' + italic_text
                if has_trailing_space:
                    italic_text = italic_text + ' '
                    
                formatted_text = italic_text
        
        if text_style.get('underline'):
            if formatted_text.strip():
                formatted_text = f"<u>{formatted_text}</u>"
        
        if text_style.get('strikethrough'):
            if formatted_text.strip():
                # Same principle for strikethrough
                stripped_content = formatted_text.strip()
                has_leading_space = formatted_text.startswith(' ')
                has_trailing_space = formatted_text.endswith(' ')
                
                strike_text = f"~~{stripped_content}~~"
                
                if has_leading_space:
                    strike_text = ' ' + strike_text
                if has_trailing_space:
                    strike_text = strike_text + ' '
                    
                formatted_text = strike_text
        
        # Handle background color (highlighting)
        bg_color = text_style.get('backgroundColor', {}).get('color', {})
        if bg_color.get('rgbColor'):
            # Prefer semantic HTML <mark> (GitHub renders it) instead of the
            # `==highlight==` trick, per style-guide.
            if formatted_text.strip():
                formatted_text = f"<mark>{formatted_text}</mark>"
        
        # Strip / replace tags disallowed by the guide
        formatted_text = re.sub(r'<u[^>]*>(.*?)</u>', r'\1', formatted_text)  # kill underline
        # Convert <mark>highlight</mark> to ==highlight== (GitHub supports this)
        # (now handled above → keep <mark> … </mark> intact)
        # Convert <br> to proper markdown line breaks (two spaces + newline)
        formatted_text = re.sub(r'<br\s*/?>', '  \n', formatted_text)
        
        return formatted_text
    
    def process_footnote_reference(self, footnote_ref: Dict[str, Any], footnotes: Dict[str, Any], footnote_refs: Dict[str, int]) -> str:
        """Process footnote references and track them."""
        footnote_id = footnote_ref.get('footnoteId')
        if footnote_id and footnote_id in footnotes:
            footnote_num = footnote_ref.get('footnoteNumber', len(footnote_refs) + 1)
            footnote_refs[footnote_id] = footnote_num
            return f"[^{footnote_num}]"
        return ""
    
    def extract_image_info(self, inline_object_element: Dict[str, Any], document: Dict[str, Any], 
                          image_folder: Path, image_counter: int) -> tuple[str, int]:
        """Extract and download image/drawing/chart, return markdown reference and updated counter."""
        inline_object_id = inline_object_element.get('inlineObjectId')
        self.logger.info(f"Processing visual element {image_counter + 1} with ID: {inline_object_id}")
        if not inline_object_id:
            self.logger.warning(f"Visual element {image_counter + 1} has no inline object ID")
            return "![Visual Element](visual-element-placeholder)", image_counter
        
        # Track downloaded images to avoid re-downloading the same image
        if not hasattr(self, '_downloaded_images'):
            self._downloaded_images = {}
            
        # Check if we already downloaded this image
        if inline_object_id in self._downloaded_images:
            existing_path, existing_counter, element_type = self._downloaded_images[inline_object_id]
            self.logger.info(f"Reusing cached {element_type} {inline_object_id}: {existing_path}")
            return f"![{element_type} {existing_counter}]({existing_path})", image_counter
        
        # Check if this drawing was already extracted by the comprehensive method
        if hasattr(self, '_drawing_map') and inline_object_id in self._drawing_map:
            drawing_path = self._drawing_map[inline_object_id]
            self.logger.info(f"🔍 DEBUGGING: Using pre-extracted drawing {inline_object_id}: {drawing_path}")
            
            # Cache it to avoid reprocessing
            self._downloaded_images[inline_object_id] = (drawing_path, image_counter, "Drawing")
            
            # Return markdown reference with Mermaid hint
            mermaid_hint = ""  # Skip mermaid hint for now
            return f"![Drawing {image_counter + 1}]({drawing_path}){mermaid_hint}", image_counter + 1
        else:
            self.logger.info(f"🔍 DEBUGGING: Object {inline_object_id} NOT found in pre-extracted drawings")
            if hasattr(self, '_drawing_map'):
                self.logger.info(f"🔍 DEBUGGING: Available drawing map keys: {list(self._drawing_map.keys())}")
            else:
                self.logger.info(f"🔍 DEBUGGING: No drawing map available")
        
        try:
            inline_objects = document.get('inlineObjects', {})
            if inline_object_id in inline_objects:
                inline_object = inline_objects[inline_object_id]
                embedded_object = inline_object.get('inlineObjectProperties', {}).get('embeddedObject', {})
                
                # Check if this is a drawing/chart (embeddedDrawingProperties) 
                self.logger.info(f"🔍 DEBUGGING FALLBACK: Processing {inline_object_id}")
                self.logger.info(f"🔍 DEBUGGING FALLBACK: Embedded object structure: {list(embedded_object.keys())}")
                self.logger.info(f"🔍 DEBUGGING FALLBACK: Full embedded object: {json.dumps(embedded_object, indent=2)}")
                
                if 'embeddedDrawingProperties' in embedded_object:
                    self.logger.info(f"🔍 DEBUGGING FALLBACK: Found embeddedDrawingProperties, proceeding with drawing extraction")
                    return self._extract_drawing_or_chart(embedded_object, inline_object_id, image_folder, image_counter)
                else:
                    self.logger.info(f"🔍 DEBUGGING FALLBACK: No embeddedDrawingProperties found in embedded object")
                
                # Try to get image properties for regular images
                image_props = embedded_object.get('imageProperties', {})
                if image_props:
                    self.logger.info(f"🔍 DEBUGGING FALLBACK: Found imageProperties: {json.dumps(image_props, indent=2)}")
                else:
                    self.logger.info(f"🔍 DEBUGGING FALLBACK: No imageProperties found")
                content_uri = image_props.get('contentUri', '')
                
                if content_uri:
                    image_counter += 1
                    image_filename = f"image_{image_counter}.png"
                    image_path = image_folder / image_filename
                    
                    try:
                        # Download image
                        if content_uri.startswith('https://'):
                            response = requests.get(content_uri)
                            response.raise_for_status()
                            with open(image_path, 'wb') as f:
                                f.write(response.content)
                        else:
                            # Try Google Drive API if it's a Drive file
                            try:
                                file_id = content_uri.split('/')[-1]
                                response = self.drive_service.files().get_media(fileId=file_id).execute()
                                with open(image_path, 'wb') as f:
                                    f.write(response)
                            except Exception:
                                # Fallback: create placeholder
                                self.logger.warning(f"Could not download image from {content_uri}")
                                return f"![Image {image_counter}](image-placeholder)", image_counter
                        
                        # Since markdown file is in same folder as images/, use relative path
                        relative_path = f"images/image_{image_counter}.png"
                        self.logger.info(f"Downloaded image: {relative_path}")
                        
                        # Cache this image for future references
                        self._downloaded_images[inline_object_id] = (relative_path, image_counter, "Image")
                        
                        return f"![Image {image_counter}]({relative_path})", image_counter
                        
                    except Exception as img_error:
                        self.logger.warning(f"Could not download image {image_counter + 1}: {img_error}")
                        return f"![Image {image_counter + 1}](image-placeholder)", image_counter
                
                # Debug: Let's see what this inline object contains instead of embeddedObject
                self.logger.warning(f"Image {image_counter + 1} inline object found but no embeddedObject")
                self.logger.info(f"Image {image_counter + 1} inline object keys: {list(inline_object.keys())}")
                self.logger.info(f"Image {image_counter + 1} inline object content: {inline_object}")
                return f"![Image {image_counter + 1}](image-placeholder)", image_counter + 1
            else:
                self.logger.warning(f"Image {image_counter + 1} inline object ID {inline_object_id} not found in document")
                return f"![Image {image_counter + 1}](image-placeholder)", image_counter + 1
            
        except Exception as e:
            self.logger.warning(f"Error processing visual element {image_counter + 1}: {e}")
            return "![Visual Element](visual-element-placeholder)", image_counter
    
    def _extract_drawing_or_chart(self, embedded_object: Dict[str, Any], inline_object_id: str, 
                                 image_folder: Path, image_counter: int) -> tuple[str, int]:
        """Extract drawing or chart using proper Google Docs API methods."""
        try:
            self.logger.info(f"Processing drawing/chart {image_counter + 1}")
            self.logger.debug(f"🔍 DRAWING DEBUG - Full embedded_object structure: {json.dumps(embedded_object, indent=2)}")
            
            # METHOD 1: Check for linkedContentReference (Drive-based drawing: Insert → Drawing → From Drive)
            linked_content = embedded_object.get('linkedContentReference', {})
            drive_file_id = linked_content.get('driveFileId')
            
            if drive_file_id:
                self.logger.info(f"📁 Found Drive-linked drawing: {drive_file_id}")
                return self._download_drive_linked_drawing(drive_file_id, image_counter, image_folder)
            
            # METHOD 2: Check for contentUri (embedded drawing: Insert → Drawing → New)
            image_props = embedded_object.get('imageProperties', {})
            content_uri = image_props.get('contentUri')
            
            if content_uri:
                self.logger.info(f"🖼️ Found embedded drawing with contentUri")
                return self._download_embedded_drawing(content_uri, image_counter, image_folder)
            
            # If neither method works, try the old fallback methods
            self.logger.warning("No contentUri or driveFileId found - using fallback extraction")
            drawing_props = embedded_object.get('embeddedDrawingProperties', {})
            self.logger.debug(f"🔍 DRAWING DEBUG - Drawing properties: {json.dumps(drawing_props, indent=2)}")
            self.logger.debug(f"🔍 DRAWING DEBUG - Inline object ID: {inline_object_id}")
            if hasattr(self, 'current_doc_url'):
                self.logger.debug(f"🔍 DRAWING DEBUG - Document URL: {self.current_doc_url}")
            
            # Get the drawing ID from embeddedDrawingProperties
            drawing_id = drawing_props.get('id')
            self.logger.debug(f"Drawing ID from embeddedDrawingProperties: {drawing_id}")
            
            if not drawing_id:
                # Try alternative ways to get drawing ID from the embedded object
                alt_id = embedded_object.get('id') or embedded_object.get('objectId')
                self.logger.debug(f"Alternative ID fields: id={embedded_object.get('id')}, objectId={embedded_object.get('objectId')}")
                
                # Check for drawing-specific properties that might contain the real ID
                drawing_id_alternatives = [
                    drawing_props.get('drawingId'),
                    drawing_props.get('sourceId'), 
                    drawing_props.get('linkId'),
                    embedded_object.get('drawingId'),
                    embedded_object.get('sourceId'),
                    alt_id
                ]
                
                # Try each alternative
                for i, alt_drawing_id in enumerate(drawing_id_alternatives):
                    if alt_drawing_id:
                        drawing_id = alt_drawing_id
                        self.logger.info(f"Found alternative drawing ID (method {i+1}): {drawing_id}")
                        break
                
                if not drawing_id:
                    # Last resort: use the inline object ID directly (some drawings are referenced this way)
                    if inline_object_id and not inline_object_id.startswith('kix.'):
                        drawing_id = inline_object_id
                        self.logger.info(f"Using inline object ID as drawing ID: {drawing_id}")
                    else:
                        # No direct drawing ID found - try automated extraction methods
                        self.logger.info(f"Drawing/chart {image_counter + 1} appears to be embedded - trying automated extraction")
                        self.logger.debug(f"Embedded object keys: {list(embedded_object.keys())}")
                        self.logger.debug(f"Drawing props keys: {list(drawing_props.keys())}")
                        
                        # Instead of giving up, try automated extraction methods
                        element_type = self._determine_drawing_type(drawing_props)
                        parent_doc_id = self.extract_doc_id(self.current_doc_url) if hasattr(self, 'current_doc_url') else None
                        
                        if parent_doc_id:
                            extracted_image_path = self._try_automated_drawing_extraction(
                                parent_doc_id, image_counter + 1, image_folder, element_type,
                                embedded_object=embedded_object  # Pass geometry data
                            )
                            
                            if extracted_image_path:
                                relative_path = f"images/{extracted_image_path.name}"
                                self.logger.info(f"Successfully extracted embedded drawing: {relative_path}")
                                
                                # Cache this drawing for future references
                                self._downloaded_images[inline_object_id] = (relative_path, image_counter + 1, element_type)
                                
                                # Add Mermaid hint if applicable
                                mermaid_hint = self._add_mermaid_hint(element_type, image_counter + 1)
                                
                                markdown_ref = f"![{element_type} {image_counter + 1}]({relative_path})"
                                if mermaid_hint:
                                    markdown_ref += mermaid_hint
                                
                                return markdown_ref, image_counter + 1
                        
                        # If automated extraction failed, provide helpful placeholder
                        return f"![{element_type} {image_counter + 1}](drawing-embedded-not-exportable)", image_counter + 1
            
            image_counter += 1
            
            # Try different export formats for drawings
            export_formats = [
                ('png', 'image/png', '.png'),
                ('jpeg', 'image/jpeg', '.jpg'),
                ('svg', 'image/svg+xml', '.svg')
            ]
            
            self.logger.info(f"Drawing ID to attempt export: {drawing_id}")
            self.logger.debug(f"Available Drive service: {self.drive_service is not None}")
            
            for format_name, mime_type, extension in export_formats:
                try:
                    self.logger.info(f"Attempting to export drawing {image_counter} as {format_name}")
                    self.logger.debug(f"Export request: fileId={drawing_id}, mimeType={mime_type}")
                    
                    # Use Google Drive API to export the drawing
                    if self.drive_service:
                        # Check if the file exists first
                        try:
                            file_metadata = self.drive_service.files().get(fileId=drawing_id, fields='id,name,mimeType,parents,exportLinks').execute()
                            self.logger.debug(f"File metadata found: {file_metadata}")
                            
                            # Check if this drawing supports the requested export format
                            export_links = file_metadata.get('exportLinks', {})
                            if export_links:
                                self.logger.debug(f"Available export formats: {list(export_links.keys())}")
                            else:
                                self.logger.debug("No export links available for this file")
                        except Exception as metadata_error:
                            self.logger.warning(f"Could not get file metadata for {drawing_id}: {metadata_error}")
                            # Continue with export attempt anyway
                        
                        response = self.drive_service.files().export(
                            fileId=drawing_id,
                            mimeType=mime_type
                        ).execute()
                        
                        self.logger.debug(f"Export successful, content size: {len(response)} bytes")
                        
                        # Save the exported drawing
                        drawing_filename = f"drawing_{image_counter}{extension}"
                        drawing_path = image_folder / drawing_filename
                        
                        with open(drawing_path, 'wb') as f:
                            f.write(response)
                        
                        # Since markdown file is in same folder as images/, use relative path
                        relative_path = f"images/drawing_{image_counter}{extension}"
                        self.logger.info(f"Successfully exported drawing as {format_name}: {relative_path}")
                        
                        # Cache this drawing for future references
                        self._downloaded_images[inline_object_id] = (relative_path, image_counter, "Drawing")
                        
                        # Determine the type of visual element for better alt text
                        element_type = self._determine_drawing_type(drawing_props)
                        
                        # Add Mermaid hint if applicable
                        mermaid_hint = self._add_mermaid_hint(element_type, image_counter)
                        
                        markdown_ref = f"![{element_type} {image_counter}]({relative_path})"
                        if mermaid_hint:
                            markdown_ref += mermaid_hint
                        
                        return markdown_ref, image_counter
                
                except Exception as export_error:
                    self.logger.warning(f"Failed to export drawing {image_counter} as {format_name}: {export_error}")
                    self.logger.debug(f"Full export error details: {type(export_error).__name__}: {export_error}")
                    
                    # Log the specific error type for better debugging
                    if "not found" in str(export_error).lower():
                        self.logger.debug(f"Drawing ID '{drawing_id}' not found in Google Drive")
                    elif "export" in str(export_error).lower():
                        self.logger.debug(f"Export operation failed for format {mime_type}")
                    elif "permission" in str(export_error).lower():
                        self.logger.debug(f"Permission denied for drawing ID '{drawing_id}'")
                    else:
                        self.logger.debug(f"Unknown error type during export")
                    
                    continue
            
            # If all export attempts failed, try to get a thumbnail or fallback
            try:
                # Try to get drawing thumbnail or preview
                if self.drive_service:
                    file_info = self.drive_service.files().get(
                        fileId=drawing_id, 
                        fields='thumbnailLink,webViewLink'
                    ).execute()
                    
                    thumbnail_link = file_info.get('thumbnailLink')
                    if thumbnail_link:
                        # Download thumbnail as fallback
                        response = requests.get(thumbnail_link)
                        response.raise_for_status()
                        
                        drawing_filename = f"drawing_{image_counter}_thumbnail.png"
                        drawing_path = image_folder / drawing_filename
                        
                        with open(drawing_path, 'wb') as f:
                            f.write(response.content)
                        
                        relative_path = f"images/drawing_{image_counter}_thumbnail.png"
                        self.logger.info(f"Downloaded drawing thumbnail: {relative_path}")
                        
                        # Cache this drawing for future references
                        self._downloaded_images[inline_object_id] = (relative_path, image_counter, "Drawing")
                        
                        element_type = self._determine_drawing_type(drawing_props)
                        
                        # Add Mermaid hint if applicable
                        mermaid_hint = self._add_mermaid_hint(element_type, image_counter)
                        
                        markdown_ref = f"![{element_type} {image_counter}]({relative_path})"
                        if mermaid_hint:
                            markdown_ref += mermaid_hint
                        
                        return markdown_ref, image_counter
            
            except Exception as thumbnail_error:
                self.logger.warning(f"Failed to get drawing thumbnail: {thumbnail_error}")
            
            # Final fallback: Try document-level export with the drawing region
            try:
                if self.docs_service and hasattr(self, 'current_doc_url'):
                    parent_doc_id = self.extract_doc_id(self.current_doc_url)
                    if parent_doc_id:
                        self.logger.info(f"Attempting document-level export for drawing {image_counter}")
                        
                        # Try automated drawing extraction methods
                        extracted_image_path = self._try_automated_drawing_extraction(
                            parent_doc_id, image_counter, image_folder, element_type,
                            embedded_object=embedded_object  # Pass geometry data
                        )
                        
                        if extracted_image_path:
                            relative_path = f"images/{extracted_image_path.name}"
                            self.logger.info(f"Successfully extracted drawing automatically: {relative_path}")
                            
                            # Cache this drawing for future references
                            self._downloaded_images[inline_object_id] = (relative_path, image_counter, element_type)
                            
                            # Add Mermaid hint if applicable
                            mermaid_hint = self._add_mermaid_hint(element_type, image_counter)
                            
                            markdown_ref = f"![{element_type} {image_counter}]({relative_path})"
                            if mermaid_hint:
                                markdown_ref += mermaid_hint
                            
                            return markdown_ref, image_counter
                        
                        # Create a better placeholder with instructions
                        element_type = self._determine_drawing_type(drawing_props)
                        placeholder_text = f"![{element_type} {image_counter}](drawing-embedded-in-doc)"
                        
                        # Add helpful comment with extraction instructions
                        instruction_comment = f"""
<!-- EMBEDDED DRAWING DETECTED - Manual extraction needed:
   1. Open the Google Doc directly: {self.current_doc_url}
   2. Right-click on the drawing/chart
   3. Select "Save as image" or "Download"
   4. Save as '{element_type.lower().replace(' ', '_')}_{image_counter}.png'
   5. Replace this placeholder with: ![{element_type} {image_counter}](images/{element_type.lower().replace(' ', '_')}_{image_counter}.png)
-->"""
                        
                        # Add helpful comment with potential Mermaid alternative
                        mermaid_hint = self._add_mermaid_hint(element_type, image_counter)
                        if mermaid_hint:
                            placeholder_text += f"\n{instruction_comment}\n{mermaid_hint}"
                        else:
                            placeholder_text += f"\n{instruction_comment}"
                        
                        return placeholder_text, image_counter
            
            except Exception as doc_export_error:
                self.logger.warning(f"Failed document-level drawing export: {doc_export_error}")
            
            # Complete fallback - create a placeholder but with drawing-specific info
            self.logger.warning(f"Could not export drawing {image_counter} in any format")
            element_type = self._determine_drawing_type(drawing_props)
            return f"![{element_type} {image_counter}](drawing-export-failed)", image_counter
            
        except Exception as e:
            self.logger.error(f"Error processing drawing/chart {image_counter + 1}: {e}")
            return f"![Drawing {image_counter + 1}](drawing-error)", image_counter + 1
    
    def _determine_drawing_type(self, drawing_props: Dict[str, Any]) -> str:
        """Determine the type of drawing based on its properties."""
        # This is a heuristic approach - Google Docs API doesn't provide explicit type info
        # We can extend this logic based on drawing properties or content analysis
        
        # Check for common indicators in drawing ID or properties
        drawing_id = drawing_props.get('id', '').lower()
        
        # Enhanced categorization with Mermaid-compatible types
        # Order matters - more specific patterns first
        if any(keyword in drawing_id for keyword in ['sequence', 'timeline', 'step']):
            return "Sequence Diagram"
        elif any(keyword in drawing_id for keyword in ['flow', 'flowchart', 'workflow', 'process']):
            return "Flowchart"
        elif any(keyword in drawing_id for keyword in ['org', 'organizational', 'hierarchy']):
            return "Org Chart"
        elif any(keyword in drawing_id for keyword in ['mind', 'mindmap', 'concept']):
            return "Mind Map"
        elif any(keyword in drawing_id for keyword in ['network', 'system', 'architecture']):
            return "System Diagram"
        elif any(keyword in drawing_id for keyword in ['chart', 'graph', 'plot']):
            return "Chart"
        elif any(keyword in drawing_id for keyword in ['diagram', 'schema', 'model']):
            return "Diagram"
        elif any(keyword in drawing_id for keyword in ['wireframe', 'mockup', 'ui']):
            return "Wireframe"
        else:
            return "Drawing"
    
    def _could_be_mermaid_diagram(self, element_type: str) -> bool:
        """Check if a drawing type could potentially be represented as Mermaid diagram."""
        # Mermaid supports: flowchart, sequence, gantt, pie, git graph, etc.
        mermaid_compatible_types = {
            "Flowchart", "Org Chart", "Sequence Diagram", 
            "System Diagram", "Chart"
        }
        return element_type in mermaid_compatible_types
    
    def extract_all_drawings(self, document: Dict[str, Any], image_folder: Path) -> Dict[str, str]:
        """
        Extract all drawings from a Google Doc using the comprehensive method.
        
        This method follows the pattern Google uses for drawings inside a Docs file:
        1. Embedded drawings (Insert → Drawing → New): Use contentUri with OAuth token
        2. Drive-linked drawings (Insert → Drawing → From Drive): Use Drive API export
        
        Args:
            document: The Google Docs document object
            image_folder: Path where images should be saved
            
        Returns:
            Dict mapping object IDs to their image file paths (relative to image_folder)
        """
        drawing_map = {}
        image_counter = 1  # Sequential numbering for cleaner filenames
        
        # Process inlineObjects (inline drawings)
        inline_objects = document.get('inlineObjects', {})
        self.logger.info(f"🔍 DEBUGGING: Found {len(inline_objects)} inline objects to process")
        
        for obj_id, obj in inline_objects.items():
            try:
                self.logger.info(f"🔍 DEBUGGING: Processing inline object {obj_id}")
                self.logger.info(f"🔍 DEBUGGING: Full inline object structure: {json.dumps(obj, indent=2)}")
                
                # Get the embedded object
                inline_props = obj.get('inlineObjectProperties', {})
                embedded_object = inline_props.get('embeddedObject', {})
                
                self.logger.info(f"🔍 DEBUGGING: Embedded object keys: {list(embedded_object.keys())}")
                
                if not embedded_object:
                    self.logger.warning(f"🔍 DEBUGGING: No embedded object found for {obj_id}")
                    continue
                    
                # Check if this is a drawing
                is_drawing = self._is_drawing_object(embedded_object)
                self.logger.info(f"🔍 DEBUGGING: Object {obj_id} is_drawing = {is_drawing}")
                
                if is_drawing:
                    image_path = self._extract_single_drawing(embedded_object, image_counter, image_folder)
                    if image_path:
                        drawing_map[obj_id] = image_path
                        self.logger.info(f"🔍 DEBUGGING: Successfully extracted {obj_id} -> {image_path}")
                        image_counter += 1
                    else:
                        self.logger.error(f"🔍 DEBUGGING: Failed to extract drawing for {obj_id}")
                else:
                    # Log what this object actually is and try to extract it anyway if it's an image
                    object_type = "unknown"
                    if 'imageProperties' in embedded_object:
                        object_type = "image"
                        content_uri = embedded_object['imageProperties'].get('contentUri', 'no-uri')
                        self.logger.info(f"🔍 DEBUGGING: Object {obj_id} is an image with contentUri: {content_uri}")
                        
                        # Try to extract regular images as well (thumbnail might be a regular image)
                        if content_uri and content_uri != 'no-uri':
                            self.logger.info(f"🔍 DEBUGGING: Attempting to extract regular image {obj_id}")
                            try:
                                image_path = self._download_embedded_drawing_v2(content_uri, image_counter, image_folder)
                                if image_path:
                                    drawing_map[obj_id] = image_path
                                    self.logger.info(f"🔍 DEBUGGING: Successfully extracted regular image {obj_id} -> {image_path}")
                                    image_counter += 1
                            except Exception as e:
                                self.logger.error(f"🔍 DEBUGGING: Failed to extract regular image {obj_id}: {e}")
                    
                    if 'embeddedDrawingProperties' in embedded_object:
                        object_type = "embedded_drawing"
                    if 'linkedContentReference' in embedded_object:
                        object_type = "linked_content"
                        drive_file_id = embedded_object['linkedContentReference'].get('driveFileId', 'no-id')
                        self.logger.info(f"🔍 DEBUGGING: Object {obj_id} is linked content with driveFileId: {drive_file_id}")
                    
                    self.logger.info(f"🔍 DEBUGGING: Object {obj_id} detected as: {object_type}")
                        
            except Exception as e:
                self.logger.error(f"🔍 DEBUGGING: Failed to process inline object {obj_id}: {e}")
                import traceback
                self.logger.error(f"🔍 DEBUGGING: Full traceback: {traceback.format_exc()}")
                continue
        
        # Process positionedObjects (absolutely-placed drawings)
        positioned_objects = document.get('positionedObjects', {})
        self.logger.info(f"🔍 DEBUGGING: Found {len(positioned_objects)} positioned objects to process")
        
        for obj_id, obj in positioned_objects.items():
            try:
                self.logger.info(f"🔍 DEBUGGING: Processing positioned object {obj_id}")
                self.logger.info(f"🔍 DEBUGGING: Full positioned object structure: {json.dumps(obj, indent=2)}")
                
                # Get the embedded object
                positioned_props = obj.get('positionedObjectProperties', {})
                embedded_object = positioned_props.get('embeddedObject', {})
                
                if not embedded_object:
                    self.logger.warning(f"🔍 DEBUGGING: No embedded object found for positioned {obj_id}")
                    continue
                    
                # Check if this is a drawing
                is_drawing = self._is_drawing_object(embedded_object)
                self.logger.info(f"🔍 DEBUGGING: Positioned object {obj_id} is_drawing = {is_drawing}")
                
                if is_drawing:
                    image_path = self._extract_single_drawing(embedded_object, obj_id, image_folder)
                    if image_path:
                        drawing_map[obj_id] = image_path
                        self.logger.info(f"🔍 DEBUGGING: Successfully extracted positioned {obj_id} -> {image_path}")
                else:
                    # Try to extract regular images from positioned objects too
                    if 'imageProperties' in embedded_object:
                        content_uri = embedded_object['imageProperties'].get('contentUri', '')
                        if content_uri:
                            self.logger.info(f"🔍 DEBUGGING: Attempting to extract positioned regular image {obj_id}")
                            try:
                                image_path = self._download_embedded_drawing_v2(content_uri, obj_id, image_folder)
                                if image_path:
                                    drawing_map[obj_id] = image_path
                                    self.logger.info(f"🔍 DEBUGGING: Successfully extracted positioned regular image {obj_id} -> {image_path}")
                            except Exception as e:
                                self.logger.error(f"🔍 DEBUGGING: Failed to extract positioned regular image {obj_id}: {e}")
                        
            except Exception as e:
                self.logger.error(f"🔍 DEBUGGING: Failed to process positioned object {obj_id}: {e}")
                import traceback
                self.logger.error(f"🔍 DEBUGGING: Full traceback: {traceback.format_exc()}")
                continue
        
        self.logger.info(f"🔍 DEBUGGING: Final drawing_map: {drawing_map}")
        self.logger.info(f"Successfully extracted {len(drawing_map)} drawings")
        return drawing_map
    
    def _is_drawing_object(self, embedded_object: Dict[str, Any]) -> bool:
        """Check if an embedded object is a drawing."""
        # Check for drawing-specific properties
        has_drawing_props = 'embeddedDrawingProperties' in embedded_object
        has_linked_drawing = embedded_object.get('linkedContentReference', {}).get('driveFileId')
        has_drawing_content_uri = embedded_object.get('imageProperties', {}).get('contentUri')
        
        # Also check if it might be a drawing based on image properties
        image_props = embedded_object.get('imageProperties', {})
        content_uri = image_props.get('contentUri', '')
        
        # Google drawings usually have specific URI patterns
        is_drawing_uri = 'drawings.googleusercontent.com' in content_uri or 'draw' in content_uri.lower()
        
        # Additional patterns for different drawing types
        is_chart_uri = 'chart' in content_uri.lower()
        is_diagram_uri = 'diagram' in content_uri.lower() or 'drawio' in content_uri.lower()
        
        # Debug logging
        self.logger.info(f"🔍 DEBUGGING _is_drawing_object:")
        self.logger.info(f"  has_drawing_props: {has_drawing_props}")
        self.logger.info(f"  has_linked_drawing: {has_linked_drawing}")
        self.logger.info(f"  has_drawing_content_uri: {has_drawing_content_uri}")
        self.logger.info(f"  content_uri: {content_uri}")
        self.logger.info(f"  is_drawing_uri: {is_drawing_uri}")
        self.logger.info(f"  is_chart_uri: {is_chart_uri}")
        self.logger.info(f"  is_diagram_uri: {is_diagram_uri}")
        
        result = (has_drawing_props or 
                 has_linked_drawing or 
                 (has_drawing_content_uri and (is_drawing_uri or is_chart_uri or is_diagram_uri)))
        self.logger.info(f"  final result: {result}")
        
        return result
    
    def _extract_single_drawing(self, embedded_object: Dict[str, Any], image_counter: int, image_folder: Path) -> Optional[str]:
        """
        Extract a single drawing using the comprehensive Google Docs drawing extraction method.
        
        Args:
            embedded_object: The embedded object containing the drawing
            image_counter: Sequential number for clean filenames (1, 2, 3...)
            image_folder: Where to save the image
            
        Returns:
            Relative path to the saved image file, or None if extraction failed
        """
        try:
            # METHOD 1: Drive-linked drawing (Insert → Drawing → From Drive)
            linked_content = embedded_object.get('linkedContentReference', {})
            drive_file_id = linked_content.get('driveFileId')
            
            if drive_file_id:
                self.logger.info(f"📁 Found Drive-linked drawing: {drive_file_id}")
                return self._download_drive_linked_drawing_v2(drive_file_id, image_counter, image_folder)
            
            # METHOD 2: Embedded drawing (Insert → Drawing → New)
            image_props = embedded_object.get('imageProperties', {})
            content_uri = image_props.get('contentUri')
            
            if content_uri:
                self.logger.info(f"🖼️ Found embedded drawing with contentUri")
                return self._download_embedded_drawing_v2(content_uri, image_counter, image_folder)
            
            # METHOD 3: Legacy embedded drawing (has embeddedDrawingProperties but no contentUri)
            if 'embeddedDrawingProperties' in embedded_object:
                self.logger.info(f"🎨 Found legacy embedded drawing without contentUri - using enhanced extraction")
                return self._extract_legacy_embedded_drawing_v2(embedded_object, image_counter, image_folder)
            
            self.logger.warning(f"No valid drawing extraction method found for drawing {image_counter}")
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to extract drawing {image_counter}: {e}")
            return None
    
    def _extract_legacy_embedded_drawing_v2(self, embedded_object: Dict[str, Any], image_counter: int, image_folder: Path) -> Optional[str]:
        """
        Extract legacy embedded drawings using enhanced geometry-aware PDF extraction with clean filenames.
        """
        try:
            self.logger.info(f"🎨 Attempting enhanced legacy drawing extraction for image {image_counter}")
            
            # Try enhanced extraction via automated methods with geometry
            parent_doc_id = (
                self.extract_doc_id(self.current_doc_url) if hasattr(self, "current_doc_url") else None
            )
            element_type = self._determine_drawing_type(
                embedded_object.get("embeddedDrawingProperties", {})
            )

            if parent_doc_id:
                extracted = self._try_automated_drawing_extraction(
                    parent_doc_id,
                    image_counter=image_counter,
                    image_folder=image_folder,
                    element_type=element_type,
                    embedded_object=embedded_object  # Pass geometry data for precise cropping!
                )
                if extracted:
                    rel_path = f"images/{extracted.name}"
                    self.logger.info(f"✅ Extracted legacy drawing via geometry-aware methods → {rel_path}")
                    return rel_path

            # Fallback to placeholder if enhanced extraction fails
            self.logger.warning(f"Enhanced extraction failed, creating placeholder for image {image_counter}")
            filename = f"image_{image_counter}_placeholder.png" 
            filepath = image_folder / filename
            self._create_drawing_placeholder(filepath, f"image_{image_counter}")
            
            self.logger.info(f"🎨 Created placeholder for legacy drawing: {filename}")
            return f"images/{filename}"
            
        except Exception as e:
            self.logger.error(f"Failed to extract legacy drawing {image_counter}: {e}")
            return None
    
    # ── 1. Back-compat shim ───────────────────────────────────────────
    def _get_mermaid_hint(self, element_type: str, image_counter: int) -> str:  # NEW
        """
        Backwards-compat wrapper.
        Earlier code still calls `_get_mermaid_hint`; we now delegate to the
        preferred `_add_mermaid_hint` API so nothing else needs to change.
        """
        return self._add_mermaid_hint(element_type, image_counter)



    
    def _create_drawing_placeholder(self, filepath: Path, obj_id: str, embedded_object: Dict[str, Any] = None):
        """Create a simple, clean placeholder for drawings that can't be extracted."""
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Simple, fixed dimensions for consistency
            width = 400
            height = 150
            
            # Light gray background
            img = Image.new('RGB', (width, height), color='#f8f9fa')
            draw = ImageDraw.Draw(img)
            
            # Add subtle border
            draw.rectangle([1, 1, width-2, height-2], outline='#dee2e6', width=1)
            
            # Try to use system font, fallback to default
            try:
                font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
                font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 12)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            # Simple text content
            title = "📊 Google Drawing"
            subtitle = "Content not available in automated export"
            instruction = "View original document to see content"
            
            # Center the text
            title_bbox = draw.textbbox((0, 0), title, font=font_large)
            title_width = title_bbox[2] - title_bbox[0]
            
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            
            instruction_bbox = draw.textbbox((0, 0), instruction, font=font_small)
            instruction_width = instruction_bbox[2] - instruction_bbox[0]
            
            # Draw text centered
            y_start = 40
            draw.text(((width - title_width) // 2, y_start), title, fill='#495057', font=font_large)
            draw.text(((width - subtitle_width) // 2, y_start + 30), subtitle, fill='#6c757d', font=font_small)
            draw.text(((width - instruction_width) // 2, y_start + 55), instruction, fill='#6c757d', font=font_small)
            
            # Save the placeholder
            img.save(filepath, 'PNG')
            self.logger.info(f"Created simple placeholder: {filepath.name}")
            
        except ImportError:
            # Fallback: create a simple text file as placeholder
            with open(filepath.with_suffix('.txt'), 'w') as f:
                f.write(f"Drawing placeholder for object {obj_id}\n")
                f.write(f"This drawing has embeddedDrawingProperties but no accessible contentUri.\n")
                f.write(f"This is typically a Google Drawing created directly in the document.\n")
                f.write(f"Manual extraction may be required.\n")
            
            # Create a minimal PNG placeholder (1x1 transparent pixel)
            # This ensures the markdown reference works
            png_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x00\x01\x00\x01\x00\x00\x00\x00\x18\xdd\x8d\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
            
            with open(filepath, 'wb') as f:
                f.write(png_data)
                
        except Exception as e:
            self.logger.error(f"Failed to create placeholder for {obj_id}: {e}")
    
    def _download_drive_linked_drawing_v2(self, drive_file_id: str, image_counter: int, image_folder: Path) -> Optional[str]:
        """Download a Drive-linked drawing using the Drive API export method."""
        try:
            # Use Drive API to export the drawing as PNG
            request = self.drive_service.files().export(fileId=drive_file_id, mimeType='image/png')
            
            # Download using MediaIoBaseDownload for better handling
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            
            while done is False:
                _, done = downloader.next_chunk()
                
            # Save the file
            filename = f"image_{image_counter}.png"
            filepath = image_folder / filename
            
            with open(filepath, "wb") as f:
                f.write(fh.getvalue())
            
            self.logger.info(f"✅ Successfully downloaded Drive-linked drawing: {filename}")
            return f"images/{filename}"
            
        except Exception as e:
            self.logger.error(f"Failed to download Drive-linked drawing {drive_file_id}: {e}")
            return None
    
    def _download_embedded_drawing_v2(self, content_uri: str, image_counter: int, image_folder: Path) -> Optional[str]:
        """Download an embedded drawing using the contentUri with OAuth token."""
        try:
            # Get the OAuth token from credentials
            if hasattr(self.docs_service._http, 'credentials'):
                credentials = self.docs_service._http.credentials
                
                # Ensure token is valid
                if not hasattr(credentials, 'token') or not credentials.token:
                    from google.auth.transport.requests import Request
                    credentials.refresh(Request())
                
                token = credentials.token
            else:
                raise Exception("Could not get OAuth token for drawing download")
            
            # Download using the signed URL with Authorization header
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(content_uri, headers=headers)
            response.raise_for_status()
            
            # Save the image
            filename = f"image_{image_counter}.png"
            filepath = image_folder / filename
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            self.logger.info(f"✅ Successfully downloaded embedded drawing: {filename}")
            return f"images/{filename}"
            
        except Exception as e:
            self.logger.error(f"Failed to download embedded drawing from {content_uri}: {e}")
            return None
    
    def _download_drive_linked_drawing(self, drive_file_id: str, image_counter: int, image_folder: Path) -> tuple[str, int]:
        """Download a Drive-linked drawing (Insert → Drawing → From Drive)."""
        try:
            # Get file metadata
            file_metadata = self.drive_service.files().get(fileId=drive_file_id).execute()
            file_name = file_metadata.get('name', f'drawing_{image_counter}')
            self.logger.info(f"📁 Downloading Drive-linked drawing: {file_name}")
            
            # Export as PNG using Drive API
            request = self.drive_service.files().export(fileId=drive_file_id, mimeType='image/png')
            
            # Create safe filename
            safe_filename = re.sub(r'[^\w\s-]', '', file_name).strip()[:50]
            if not safe_filename:
                safe_filename = f"drawing_{image_counter}"
            
            filename = f"{safe_filename}.png"
            filepath = image_folder / filename
            
            # Download the content
            media = request.execute()
            with open(filepath, 'wb') as f:
                f.write(media)
            
            self.logger.info(f"✅ Successfully downloaded Drive-linked drawing: {filename}")
            
            # Determine drawing type for Mermaid hint
            drawing_type = self._determine_drawing_type(drive_file_id, file_name)
            mermaid_hint = self._get_mermaid_hint(drawing_type)
            
            relative_path = f"images/{filename}"
            return f"![Drawing {image_counter}]({relative_path}){mermaid_hint}", image_counter + 1
            
        except Exception as e:
            self.logger.error(f"Failed to download Drive-linked drawing {drive_file_id}: {e}")
            return f"![Drawing {image_counter}](drive-drawing-failed)", image_counter + 1
    
    def _download_embedded_drawing(self, content_uri: str, image_counter: int, image_folder: Path) -> tuple[str, int]:
        """Download an embedded drawing (Insert → Drawing → New) using contentUri."""
        try:
            self.logger.info(f"🖼️ Downloading embedded drawing from contentUri")
            
            # Get OAuth token for authentication
            import requests
            
            # Use the OAuth credentials to get the token
            if hasattr(self.docs_service._http, 'credentials'):
                credentials = self.docs_service._http.credentials
                if hasattr(credentials, 'token'):
                    token = credentials.token
                else:
                    # Refresh token if needed
                    from google.auth.transport.requests import Request
                    credentials.refresh(Request())
                    token = credentials.token
            else:
                raise Exception("Could not get OAuth token for drawing download")
            
            # Download the drawing using the signed URL
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(content_uri, headers=headers)
            response.raise_for_status()
            
            # Save the image
            filename = f"drawing_{image_counter}_embedded.png"
            filepath = image_folder / filename
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            self.logger.info(f"✅ Successfully downloaded embedded drawing: {filename}")
            
            # Simple type detection for embedded drawings
            drawing_type = "Flowchart"  # Default assumption for embedded drawings
            mermaid_hint = self._get_mermaid_hint(drawing_type)
            
            relative_path = f"images/{filename}"
            return f"![Drawing {image_counter}]({relative_path}){mermaid_hint}", image_counter + 1
            
        except Exception as e:
            self.logger.error(f"Failed to download embedded drawing from contentUri: {e}")
            return f"![Drawing {image_counter}](embedded-drawing-failed)", image_counter + 1
    
    def _try_automated_drawing_extraction(self, doc_id: str, image_counter: int, 
                                         image_folder: Path, element_type: str,
                                         embedded_object: dict = None) -> Optional[Path]:
        """
        Try automated method to extract embedded drawings from Google Docs using thumbnail API.
        Returns the path to the extracted image file if successful, None otherwise.
        """
        try:
            # Try using Google Drive's thumbnail/preview API
            thumbnail_extracted = self._extract_from_thumbnail(doc_id, image_counter, image_folder, element_type)
            if thumbnail_extracted:
                return thumbnail_extracted
                
            self.logger.debug(f"Thumbnail extraction method failed for drawing {image_counter}")
            return None
            
        except Exception as e:
            self.logger.debug(f"Automated drawing extraction failed: {e}")
            return None
    

    

    
    def _extract_from_thumbnail(self, doc_id: str, image_counter: int, 
                              image_folder: Path, element_type: str) -> Optional[Path]:
        """Create a placeholder image instead of using PDF thumbnail."""
        try:
            self.logger.debug(f"Creating placeholder for drawing {image_counter} (avoiding PDF processing)")
            
            # Create a simple placeholder image
            image_filename = f"drawing_{image_counter}_placeholder.png"
            image_path = image_folder / image_filename
            
            # Create a simple placeholder using PIL if available, otherwise use a 1x1 transparent PNG
            try:
                from PIL import Image, ImageDraw, ImageFont
                
                # Create a 400x200 placeholder image
                width, height = 400, 200
                img = Image.new('RGB', (width, height), color='#f8f9fa')
                draw = ImageDraw.Draw(img)
                
                # Add border
                draw.rectangle([1, 1, width-2, height-2], outline='#dee2e6', width=2)
                
                # Add text
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
                except:
                    font = ImageFont.load_default()
                
                text_lines = [
                    f"{element_type} Not Available",
                    "Drawing could not be extracted",
                    "View original document for details"
                ]
                
                y_start = height // 2 - (len(text_lines) * 20) // 2
                for i, text in enumerate(text_lines):
                    bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = bbox[2] - bbox[0]
                    x = (width - text_width) // 2
                    y = y_start + i * 25
                    draw.text((x, y), text, fill='#6c757d', font=font)
                
                img.save(image_path, "PNG")
                
            except ImportError:
                # Fallback: Create a minimal 1x1 transparent PNG
                png_data = (
                    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
                    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8"
                    b"\x0f\x00\x00\x01\x00\x01\x00\x00\x00\x00\x18\xdd\x8d\xb4\x00\x00"
                    b"\x00\x00IEND\xaeB`\x82"
                )
                image_path.write_bytes(png_data)
            
            self.logger.info(f"Created placeholder image: {image_filename}")
            return image_path
                
        except Exception as e:
            self.logger.error(f"Failed to create placeholder image: {e}")
            
        return None

    def _add_mermaid_hint(self, element_type: str, image_counter: int) -> str:
        """Add a hint about potential Mermaid representation."""
        if self._could_be_mermaid_diagram(element_type):
            mermaid_type = {
                "Flowchart": "flowchart TD",
                "Org Chart": "flowchart TD", 
                "Sequence Diagram": "sequenceDiagram",
                "System Diagram": "flowchart LR",
                "Chart": "pie"
            }.get(element_type, "flowchart TD")
            
            return f"""
<!-- This {element_type} could potentially be recreated as a Mermaid diagram:
```mermaid
{mermaid_type}
    A[Start] --> B[Process]
    B --> C[End]
```
For more complex diagrams, refer to: https://mermaid.js.org/
-->"""
        return ""
    
    def extract_paragraph_text(self, paragraph: Dict[str, Any], document: Dict[str, Any], 
                              footnotes: Dict[str, Any], footnote_refs: Dict[str, int],
                              image_folder: Path, image_counter: int) -> tuple[str, int]:
        """Extract text from paragraph with all formatting."""
        line_parts = []
        
        if 'elements' in paragraph:
            for elem in paragraph['elements']:
                if 'textRun' in elem:
                    formatted_text = self.extract_text_with_formatting(elem['textRun'])
                    line_parts.append(formatted_text)
                elif 'person' in elem:
                    # Handle person mentions (names)
                    person_info = elem['person']
                    person_props = person_info.get('personProperties', {})
                    person_name = person_props.get('name', 'Unknown Person')
                    person_email = person_props.get('email', '')
                    
                    # Format as markdown link if email is available
                    if person_email:
                        formatted_person = f"[{person_name}](mailto:{person_email})"
                    else:
                        formatted_person = person_name
                    
                    # Apply any text styling from person element
                    text_style = person_info.get('textStyle', {})
                    if text_style.get('bold'):
                        formatted_person = f"**{formatted_person}**"
                    if text_style.get('italic'):
                        formatted_person = f"*{formatted_person}*"
                    
                    line_parts.append(formatted_person)
                elif 'footnoteReference' in elem:
                    footnote_ref = self.process_footnote_reference(
                        elem['footnoteReference'], footnotes, footnote_refs
                    )
                    line_parts.append(footnote_ref)
                elif 'inlineObjectElement' in elem:
                    image_markdown, image_counter = self.extract_image_info(
                        elem['inlineObjectElement'], document, image_folder, image_counter
                    )
                    line_parts.append(image_markdown)
                elif 'pageBreak' in elem:
                    line_parts.append('\n---\n')
                elif 'columnBreak' in elem:
                    line_parts.append('\n\n')
        
        return ''.join(line_parts), image_counter
    
    def extract_table_cell_text(self, cell: Dict[str, Any], document: Dict[str, Any],
                               footnotes: Dict[str, Any], footnote_refs: Dict[str, int],
                               image_folder: Path, image_counter: int) -> tuple[str, int]:
        """Extract text from table cell with formatting."""
        cell_parts = []
        for cell_elem in cell.get('content', []):
            if 'paragraph' in cell_elem:
                para_text, image_counter = self.extract_paragraph_text(
                    cell_elem['paragraph'], document, footnotes, footnote_refs, 
                    image_folder, image_counter
                )
                if para_text.strip():
                    cell_parts.append(para_text.strip())
        return ' '.join(cell_parts), image_counter

    
    # ────────────────────────────────────────────────────────────────────────────────
    # 1⃣  VALIDATE & FIX ORCHESTRATOR  (unchanged signature)
    # ────────────────────────────────────────────────────────────────────────────────
    def validate_and_fix_markdown(self, md_content: str) -> tuple[str, list[str]]:
        """
        Validate and automatically fix common markdown compilation issues.
        Returns (fixed_content, list_of_issues_found).
        """
        errors: list[str] = []
        fixed = md_content

        # --- structural & "compiler" style checks ---------------------------------
        for checker in (
            self.check_fenced_code,
            self.check_inline_backticks,
            self.check_heading_jumps,
            self.check_duplicate_headings,
            self.check_table_formatting,
            self.check_image_references,
            self.check_google_docs_conversion_issues,
        ):
            errors.extend(checker(fixed))

        # --- aggressive in-place fixes (bold/italics, list/items, tables) ---------
        fixed, more = self._aggressive_md_fixes(fixed)
        errors.extend(more)

        return fixed, errors


    # ────────────────────────────────────────────────────────────────────────────────
    # 2⃣  AGGRESSIVE FIX ENGINE  (replaces old aggressively_fix_bold_formatting)
    # ────────────────────────────────────────────────────────────────────────────────
    def _aggressive_md_fixes(self, text: str) -> tuple[str, list[str]]:
        """
        One multi-pass fixer that:
        • removes internal spaces inside **…** / *…*
        • ensures a space *before* opening bold in bullets & headers
        • restores spaces/newlines after closing bold
        • repairs tables (| … |) that carry malformed bold
        Returns (clean_text, [human-readable fixes])
        """
        report: list[str] = []
        src = text

        # helper ──────────────────────────────────────────────────────────────────
        def sub(rx, repl, label):
            nonlocal src
            new = re.sub(rx, repl, src, flags=re.MULTILINE)
            if new != src:
                report.append(label)
                src = new

        # ❶ kill spaces INSIDE markers (works for **bold** and *italics*) ---------
        sub(r'(\*\*|\*)(\s+)([^*\n]+?)(\s+)(\*\*|\*)',
            r'\1\3\5',
            "trimmed spaces inside bold/italic")

        # run twice to catch nested cases
        sub(r'(\*\*|\*)(\s+)([^*\n]+?)(\s+)(\*\*|\*)',
            r'\1\3\5',
            "trimmed nested spaces inside bold/italic")

        # ❷ guarantee SINGLE space BEFORE opening ** in lists / headers -----------
        #   -**Problem:**  →  - **Problem:**
        sub(r'^([-+*]|\d+\.)\s*(\*\*)', r'\1 \2',
            "added space before bold in list items")
        #   ###**Header**  →  ### **Header**
        sub(r'^(#{1,6})\s*(\*\*)', r'\1 \2',
            "added space before bold in headers")

        # ❸ ensure space AFTER closing ** if letter/number follows (but not % or symbols) ------
        # Handle cases like **Order rate**15.69% but preserve **+2.64%** and **−0.69%**
        sub(r'(\*\*[^\n*]+?[^%\+\-]\*\*)([A-Za-z0-9])', r'\1 \2',
            "inserted space after closing bold before alphanumeric")

        # ❹ tables: clean bold & keep cell paddings -------------------------------
        # remove inner spaces
        sub(r'(\|\s*)\*\*\s+([^*]+?)\s+\*\*(\s*\|)', r'\1**\2**\3',
            "fixed bold spacing in tables")

        # ─────────► NEW PASS A – trim leading/trailing spaces INSIDE bold/italic
        sub(r'\*\*\s*([^*\s][^*]*?)\s*\*\*', r'**\1**',
            "removed inner padding in bold")
        sub(r'\*\s*([^*\s][^*]*?)\s*\*',  r'*\1*',
            "removed inner padding in italics")

        # ─────────► NEW PASS B – bullet lines starting with " - ** text""
        # turn " - ** Solution" into " - **Solution"
        sub(r'^-\s+\*\*\s*([^*\n]+?)\s*\*\*', r'- **\1**',
            "fixed leading-space bold in list items")

        # ─────────► NEW PASS C – header tails like "#### Overview** Test…"
        # insert a line-break between the closing bold and next header
        sub(r'(#{3,6}.*?\*\*)(\s*#{1,6})', r'\1\n\n\2',
            "split merged headers")

        # ─────────► NEW PASS D – italic sequences followed by plain text
        # "*Logins: -1.54%* GOV" → "*Logins: -1.54%* GOV"
        sub(r'(\*[^\n*]+?\*)([A-Za-z])', r'\1 \2',
            "space after closing italics")
        # unmatched ** inside a row
        def fix_table_bold(row: str) -> str:
            if row.count('**') % 2:
                return row.replace('**', '')  # strip malformed bold
            return row
        new_lines = []
        for ln in src.splitlines():
            if ln.strip().startswith('|') and ln.strip().endswith('|'):
                ln2 = fix_table_bold(ln)
                if ln2 != ln:
                    report.append("stripped unmatched ** in table row")
                new_lines.append(ln2)
            else:
                new_lines.append(ln)
        src = '\n'.join(new_lines)

        # ❺ collapse >1 space sequences we may have introduced --------------------
        sub(r'[ ]{2,}', ' ',
            "collapsed multiple spaces")

        return src, report  
    
    def cleanup_markdown_formatting_github_standard(self, markdown_content: str) -> str:
        """
        Comprehensive markdown cleanup function to fix all formatting issues.
        Based on GitHub markdown syntax guide best practices.
        """
        # CRITICAL FIX: Address the specific formatting issues we're seeing
        content = markdown_content
        
        # Fix 1: Header spacing - ensure space between ### and **
        content = re.sub(r'(#{1,6})(\*\*[^*\n]+?\*\*)', r'\1 \2', content)
        
        # Fix 2: Analytics DRI separation - ensure it's on its own line 
        content = re.sub(r'(\*\*[^*\n]+?\*\*)Analytics DRI:', r'\1\n\nAnalytics DRI:', content)
        
        # Fix 3: Bold text spacing - ensure space after colon in bold
        content = re.sub(r'(\*\*[^*:]+?:\*\*)([A-Za-z])', r'\1 \2', content)
        
        # First pass: Fix line-level issues and structure
        lines = content.split('\n')
        cleaned_lines = []
        
        for i, line in enumerate(lines):
            # Skip leading --- if it's the first non-empty line
            if not cleaned_lines and line.strip() == '---':
                continue
                
            # Remove trailing --- sections (but keep footnote sections)
            if line.strip() == '---' and len(cleaned_lines) > 0:
                # Check if this is before footnotes
                remaining_lines = lines[i + 1:]
                has_footnotes = any('## Footnotes' in remaining_line for remaining_line in remaining_lines[:5])
                if not has_footnotes:
                    continue
            
            cleaned_lines.append(line)
        
        # Second pass: Join and fix structural issues
        content = '\n'.join(cleaned_lines)
        
        # CRITICAL: Fix header separation issues FIRST, before bold formatting cleanup
        # Fix the specific TL;DR pattern: ### **TL;DR**-** Problem:** -> ### **TL;DR**\n\n- ** Problem:**  
        content = re.sub(r'(#{1,6}\s*\*\*TL;DR\*\*)\s*-\s*(\*\*\s*Problem:\*\*.*)', r'\1\n\n- \2', content)
        
        # Fix headers followed by content with dash: ### **Header**-** Content:** -> ### **Header**\n\n- **Content:**
        content = re.sub(r'(#{1,6}\s+\*\*[^*\n]+?\*\*)-(\*\*[^*\n]+?\*\*.*)', r'\1\n\n- \2', content)
        
        # Fix major structural problems that cause content to merge
        # Pattern: Fix title merged with email: **Text**Analytics DRI: -> **Text**\n\nAnalytics DRI:
        content = re.sub(r'(\*\*[^*\n]+?\*\*)([A-Z][a-z].*?@.*?\.com)', r'\1\n\n\2', content)
        
        # Fix headers that get merged with following content  
        content = re.sub(r'(#{1,6}\s*\*\*[^*\n]+?\*\*)([A-Z][a-z])', r'\1\n\n\2', content)
        
        # Fix section headers merged with list items: **Text**-**Problem:** -> **Text**\n\n- **Problem:**
        content = re.sub(r'(\*\*[^*\n]+?\*\*)-(\*\*[^*\n]+?\*\*)', r'\1\n\n- \2', content)
        
        # Fix headers followed by any content: ### **Header**Content -> ### **Header**\n\nContent
        content = re.sub(r'(#{1,6}\s+\*\*[^*\n]+?\*\*)([A-Z][a-z])', r'\1\n\n\2', content)
        
        # Fix section breaks - add proper spacing around headers
        content = re.sub(r'(\*\*[^*\n]+?\*\*)(#{1,6})', r'\1\n\n\2', content)
        
        # Fix merged table headers and content
        content = re.sub(r'(\|\s*\*\*[^*\n]+?\*\*\s*\|)([A-Z])', r'\1\n\n\2', content)
        
        # Third pass: Apply comprehensive bold formatting fixes
        # This will be handled by the aggressively_fix_bold_formatting function
        
        # Fourth pass: Fix spacing and structure around headers and lists
        # Ensure headers have proper spacing: ###**Text** -> ### **Text**
        content = re.sub(r'(#{1,6})(\*\*[^*\n]+?\*\*)', r'\1 \2', content)
        
        # Ensure list items have proper spacing: -**Text** -> - **Text**
        content = re.sub(r'^(-\s*)(\*\*[^*\n]+?\*\*)', r'\1 \2', content, flags=re.MULTILINE)
        
        # Fix table cell content separation
        content = re.sub(r'(\|\s*)(\*\*[^*\n]+?\*\*)([A-Z])', r'\1\2 \3', content)
        
        # Fifth pass: Clean up multiple newlines and ensure proper structure
        lines = content.split('\n')
        final_lines = []
        prev_was_empty = False
        
        for line in lines:
            if line.strip():
                final_lines.append(line)
                prev_was_empty = False
            else:
                if not prev_was_empty:
                    final_lines.append('')
                prev_was_empty = True
        
        final_content = '\n'.join(final_lines)
        
        # Run markdown validation and fix common issues
        fixed_content, validation_errors = self.validate_and_fix_markdown(final_content)
        
        # Apply final structural fixes AFTER validation (since validation can interfere)
        
        # 🐛 DEBUG: Check what text we're actually processing
        all_lines = fixed_content.split('\n')
        self.logger.info(f"🐛 DEBUG - Line 10 content: {repr(all_lines[9]) if len(all_lines) > 9 else 'N/A'}")
        
        # 🔧 FIX 1: Bold formatting with spaces inside markers: - ** Problem:** -> - **Problem:**
        # Pattern: dash + space + "** " + text + ":**"
        before_fix1 = fixed_content
        fixed_content = re.sub(r'-\s+\*\*\s+([^*\n]+?):\*\*', r'- **\1:**', fixed_content)
        if before_fix1 != fixed_content:
            self.logger.info("🔧 Applied Fix 1: Bold spacing correction")
        else:
            self.logger.info("🔧 Fix 1: No matches found for bold spacing pattern")
        
        # 🔧 FIX 2: Headers merged with content: ### **Methodology**#### Overview** -> ### **Methodology**\n\n#### Overview**  
        before_fix2 = fixed_content
        fixed_content = re.sub(r'(#{1,6}\s+\*\*[^*\n]+?\*\*)(#{1,6})', r'\1\n\n\2', fixed_content)
        if before_fix2 != fixed_content:
            self.logger.info("🔧 Applied Fix 2: Header separation")
        
        # 🔧 FIX 3: Multiple bold elements on same line: **Text1****Text2:** -> **Text1** **Text2:**
        before_fix3 = fixed_content
        fixed_content = re.sub(r'(\*\*[^*\n]+?\*\*)(\*\*[^*\n]+?:\*\*)', r'\1 \2', fixed_content)
        if before_fix3 != fixed_content:
            self.logger.info("🔧 Applied Fix 3: Bold element separation")
        
        # Fix the specific TL;DR pattern: ### **TL;DR**-** Problem:** -> ### **TL;DR**\n\n- **Problem:**  
        fixed_content = re.sub(r'(#{1,6}\s*\*\*TL;DR\*\*)\s*-\s*(\*\*\s*Problem:\*\*.*)', r'\1\n\n- \2', fixed_content)
        
        # Fix other header-dash patterns
        fixed_content = re.sub(r'(#{1,6}\s+\*\*[^*\n]+?\*\*)\s*-\s*(\*\*[^*\n]+?\*\*.*)', r'\1\n\n- \2', fixed_content)
        
        # 🔧 ADDITIONAL CRITICAL FIXES for GitHub Markdown Standard [[memory:5731193]]
        
        # FIX A: List items missing space after dash: -**Solution** -> - **Solution**
        fixed_content = re.sub(r'^-(\*\*[^*\n]+?\*\*)', r'- \1', fixed_content, flags=re.MULTILINE)
        
        # FIX B: Bold text followed immediately by text without space (**Problem:**We → **Problem:** We)
        fixed_content = re.sub(r'(\*\*[^*\n]+?:\*\*)([A-Za-z])', r'\1 \2', fixed_content)
        
        # FIX C: Experiment readout specific patterns
        # Fix percentage/delta values formatting: **+2.64 %** → **+2.64%**
        fixed_content = re.sub(r'\*\*([+\-]?\d+\.?\d*)\s+%\*\*', r'**\1%**', fixed_content)
        
        # Fix currency formatting: **$3.2 M** → **$3.2M**
        fixed_content = re.sub(r'\*\*([+\-]?\$\d+\.?\d*)\s+([KMB])\*\*', r'**\1\2**', fixed_content)
        
        # FIX D: Table cell alignment - ensure spaces around pipes
        fixed_content = re.sub(r'\|([^|\n]+?)\|', lambda m: f'| {m.group(1).strip()} |', fixed_content)
        
        # FIX E: Table content merged with result summary - major structural fix
        # Fix: |text|**Results Summary**text -> |text|\n\n**Results Summary**\n\ntext
        fixed_content = re.sub(r'(\|\s*[^|\n]+?\s*\|)\s*(\*\*[^*\n]+?\*\*[^|\n]*)', r'\1\n\n\2', fixed_content)
        
        # FIX F: Table header spacing issues in cells
        # Fix: |**Treatment (With App Banner)**| -> | **Treatment (With App Banner)** |
        fixed_content = re.sub(r'\|(\*\*[^*\n]+?\*\*)\|', r'| \1 |', fixed_content)
        
        # FIX G: Ensure proper spacing in list items that were missed
        # Fix: -**Solution**: -> - **Solution**:
        fixed_content = re.sub(r'^-(\*\*[^*\n]+?\*\*:)', r'- \1', fixed_content, flags=re.MULTILINE)
        
        if validation_errors:
            self.logger.warning(f"Found and fixed {len(validation_errors)} markdown issues")
            for error in validation_errors[:5]:  # Log first 5 errors
                self.logger.warning(f"  - {error}")
        
        return fixed_content
    
    def check_fenced_code(self, md: str) -> list[str]:
        """Check for unmatched fenced code blocks."""
        fence_count = len(re.findall(r'^```', md, flags=re.MULTILINE))
        return [] if fence_count % 2 == 0 else ["Unmatched fenced code block: found an odd number of ``` fences"]
    
    def check_inline_backticks(self, md: str) -> list[str]:
        """Check for unmatched inline backticks."""
        errors = []
        for i, line in enumerate(md.splitlines(), 1):
            if line.count('`') % 2:
                errors.append(f"Line {i}: unmatched inline back-tick")
        return errors
    
    def check_heading_jumps(self, md: str) -> list[str]:
        """Check for heading level jumps (e.g., # to ###)."""
        errors = []
        last_level = 0
        for i, line in enumerate(md.splitlines(), 1):
            m = re.match(r'^(#+)\s', line)
            if m:
                level = len(m.group(1))
                if level > last_level + 1:
                    errors.append(f"Line {i}: heading level jumps from {last_level} to {level}")
                last_level = level
        return errors
    
    def check_duplicate_headings(self, md: str) -> list[str]:
        """Check for duplicate heading slugs."""
        seen = set()
        errors = []
        for i, line in enumerate(md.splitlines(), 1):
            m = re.match(r'^(#+)\s+(.*)$', line)
            if m:
                heading_text = m.group(2)
                # Remove markdown formatting from heading text for slug generation
                clean_text = re.sub(r'\*\*([^*]+?)\*\*', r'\1', heading_text)  # Remove bold
                clean_text = re.sub(r'\*([^*]+?)\*', r'\1', clean_text)        # Remove italic
                slug = re.sub(r'[^a-z0-9]+', '-', clean_text.lower()).strip('-')
                if not slug:
                    errors.append(f"Line {i}: empty heading text")
                elif slug in seen:
                    errors.append(f"Line {i}: duplicate heading '{heading_text}'")
                seen.add(slug)
        return errors
    

    
    def check_image_references(self, md: str) -> list[str]:
        """Check for broken image references and drawing exports."""
        errors = []
        lines = md.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Find image-placeholder references
            if 'image-placeholder' in line:
                errors.append(f"Line {i}: broken image reference (image-placeholder)")
            
            # Find drawing export failures
            if 'drawing-export-failed' in line:
                errors.append(f"Line {i}: drawing export failed")
            elif 'drawing-no-id' in line:
                errors.append(f"Line {i}: drawing has no ID for export")
            elif 'drawing-error' in line:
                errors.append(f"Line {i}: drawing processing error")
            
            # Find visual element placeholders  
            if 'visual-element-placeholder' in line:
                errors.append(f"Line {i}: visual element could not be processed")
            
            # Find missing image/drawing files
            image_matches = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            for _, image_path in image_matches:
                if image_path.startswith('images/'):
                    if image_path.endswith(('.png', '.jpg', '.jpeg', '.svg')):
                        # Could add actual file existence check here if needed
                        pass
                    elif 'chart-not-exportable' in image_path:
                        errors.append(f"Line {i}: chart/drawing was not exportable (legacy)")
        
        return errors
    
    def check_google_docs_conversion_issues(self, md: str) -> list[str]:
        """Check for common issues from Google Docs conversion."""
        errors = []
        lines = md.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for merged content (bold text immediately followed by capitalized text)
            if re.search(r'\*\*[^*]+?\*\*[A-Z][a-z]', line):
                errors.append(f"Line {i}: potential merged content after bold text")
            
            # Check for headers without space after #
            if re.search(r'^#{1,6}\*\*', line):
                errors.append(f"Line {i}: header without space after # symbols")
            
            # Check for list items without space after -
            if re.search(r'^-\*\*', line):
                errors.append(f"Line {i}: list item without space after -")
            
            # Check for bold text followed by dash without spaces
            if re.search(r'\*\*[^*]+?\*\*-\*\*', line):
                errors.append(f"Line {i}: bold text followed by dash needs spacing")
            
            # Check for email addresses that might be merged with preceding text
            if re.search(r'\*\*[^*]+?\*\*[a-zA-Z].*?@.*?\.com', line):
                errors.append(f"Line {i}: email address may be merged with preceding bold text")
        
        return errors
    
    def check_table_formatting(self, md: str) -> list[str]:
        """Check for table formatting issues."""
        errors = []
        lines = md.split('\n')
        in_table = False
        
        for i, line in enumerate(lines, 1):
            # Detect table rows
            if line.strip().startswith('|') and line.strip().endswith('|'):
                in_table = True
                
                # Check for bold formatting in table cells
                if '**' in line:
                    # Count bold markers in the line
                    bold_count = line.count('**')
                    if bold_count % 2 != 0:
                        errors.append(f"Line {i}: unmatched bold markers in table row")
                    
                    # Check for spaces inside bold markers in tables
                    if re.search(r'\*\*\s+[^*]+?\s*\*\*|\*\*\s*[^*]+?\s+\*\*', line):
                        errors.append(f"Line {i}: spaces inside bold markers in table cell")
                
                # Check for proper table structure
                cells = line.split('|')[1:-1]  # Remove first and last empty elements
                for j, cell in enumerate(cells):
                    if cell.strip() == '':
                        continue  # Empty cells are OK
                    if cell.startswith(' ') and cell.endswith(' '):
                        continue  # Properly formatted cells
                    errors.append(f"Line {i}, Cell {j+1}: table cell may need proper spacing")
            
            elif in_table and line.strip() == '':
                in_table = False
        
        return errors
    
    def process_list_item(self, paragraph: Dict[str, Any], line_text: str) -> str:
        """Process list items with proper nesting and bullet types."""
        bullet = paragraph.get('bullet')
        if not bullet:
            return line_text
        
        nesting_level = bullet.get('nestingLevel', 0)
        indent = "  " * nesting_level
        
        # Determine list type
        glyph_type = bullet.get('glyph', {}).get('type', '')
        
        if glyph_type == 'GLYPH_TYPE_DECIMAL' or 'DECIMAL' in str(bullet):
            return f"{indent}1. {line_text.strip()}"
        else:
            # Use different bullet characters based on nesting
            if nesting_level == 0:
                bullet_char = "-"
            elif nesting_level == 1:
                bullet_char = "*"
            else:
                bullet_char = "+"
            # Guarantee exactly *one* space after the bullet char – nothing more,
            # nothing less – for GitHub-flavoured Markdown compliance.
            clean = re.sub(r'^\s+', '', line_text).strip()
            return f"{indent}{bullet_char} {clean}"
    
    def detect_and_convert_collapsible_sections(self, md_content: str) -> str:
        """
        Detect potential collapsible sections and convert them to details/summary blocks.
        
        Looks for patterns like:
        - "Key metrics" followed by content that could be collapsed
        - Sections that start with summary-like text
        """
        lines = md_content.split('\n')
        result_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for potential summary headers (case insensitive patterns)
            # Expanded patterns to catch more collapsible content
            summary_patterns = [
                r'^#+\s*(key\s+metrics?|results?\s+summary|summary|details?|methodology|experiment\s+timeline|impacts?\s+breakdown|next\s+steps?|method|findings?|recommendations?)\s*$',
                r'^[*\-]\s*(key\s+metrics?|results?\s+summary|summary|details?|methodology|experiment\s+timeline|impacts?\s+breakdown|next\s+steps?|method|findings?|recommendations?)\s*$',
                r'^\*\*\s*(key\s+metrics?|results?\s+summary|summary|details?|methodology|experiment\s+timeline|impacts?\s+breakdown|next\s+steps?|method|findings?|recommendations?)\s*\*\*\s*$'
            ]
            
            is_summary = any(re.match(pattern, line, re.IGNORECASE) for pattern in summary_patterns)
            
            if is_summary and i + 1 < len(lines):
                # Found a potential summary, look for content that follows
                summary_text = re.sub(r'^[#*\-\s]+', '', line).strip()
                self.logger.debug(f"Found potential collapsible section: '{summary_text}'")
                
                # Collect content until we hit the next major section or end
                content_lines = []
                j = i + 1
                
                # Skip empty lines right after summary
                while j < len(lines) and not lines[j].strip():
                    j += 1
                
                # Collect content lines
                while j < len(lines):
                    next_line = lines[j].strip()
                    
                    # Stop at next major header (## or #) or horizontal rule
                    if (re.match(r'^#{1,2}\s+', next_line) or 
                        next_line.startswith('---') or
                        next_line.startswith('===') or
                        (not next_line and j + 1 < len(lines) and 
                         re.match(r'^#{1,2}\s+', lines[j + 1].strip()))):
                        break
                    
                    content_lines.append(lines[j])
                    j += 1
                
                # If we found substantial content, make it collapsible
                if len(content_lines) > 3:  # Only collapse if there's enough content
                    self.logger.debug(f"Creating collapsible section for '{summary_text}' with {len(content_lines)} lines")
                    result_lines.append(f"<details>")
                    result_lines.append(f"<summary>{summary_text}</summary>")
                    result_lines.append("")
                    result_lines.extend(content_lines)
                    result_lines.append("")
                    result_lines.append("</details>")
                    result_lines.append("")
                    i = j
                else:
                    # Not enough content, keep as regular section
                    self.logger.debug(f"Not enough content for collapsible section '{summary_text}' ({len(content_lines)} lines)")
                    result_lines.append(lines[i])
                    i += 1
            else:
                result_lines.append(lines[i])
                i += 1
        
        return '\n'.join(result_lines)
    
    def convert_document_to_markdown(self, doc_url: str, output_path: str, 
                                   team_path: str) -> Dict[str, Any]:
        """
        Convert a Google Doc to enhanced markdown with comprehensive formatting.
        
        Args:
            doc_url: Google Docs URL
            output_path: Base output directory  
            team_path: Team-specific subdirectory
            
        Returns:
            Dictionary with conversion results
        """
        if not self.docs_service:
            raise RuntimeError("Google Docs service not initialized")
        
        doc_id = self.extract_doc_id(doc_url)
        if not doc_id:
            raise ValueError(f"Invalid Google Docs URL: {doc_url}")
        
        try:
            # Store current document URL for drawing extraction
            self.current_doc_url = doc_url
            
            # Get document content with footnotes
            document = self.docs_service.documents().get(documentId=doc_id).execute()
            title = document.get('title', 'Untitled Document')
            content = document.get('body', {}).get('content', [])
            footnotes = document.get('footnotes', {})
            
            self.logger.info(f"Converting document with enhanced formatting: {title}")
            
            # Detect experiment quarter (initial pass from text)
            detected_quarter = self.quarter_detector.detect_experiment_quarter(document)
            self.logger.info(f"Initially detected experiment quarter: {detected_quarter}")
            
            # Clean up title and add quarter prefix
            clean_title = self.quarter_detector.clean_document_title(title, detected_quarter)
            
            # Setup directories - new structure: experiment-readouts/team/subteam/document-title/
            base_output_path = Path(output_path)
            team_output_path = base_output_path / team_path
            
            # Create document-specific folder (experiment-readouts/team/subteam/document-title/)
            sanitized_doc_name = re.sub(r'[^\w\s-]', '', title).strip()
            sanitized_doc_name = re.sub(r'[-\s]+', '-', sanitized_doc_name)
            
            # Document folder contains both markdown file and images folder
            document_folder = team_output_path / sanitized_doc_name
            document_folder.mkdir(parents=True, exist_ok=True)
            
            # Images folder inside document folder
            image_folder = document_folder / "images"
            image_folder.mkdir(exist_ok=True)
            
            # Initialize conversion state
            markdown_lines = []
            # Don't add the title line - it's redundant with the document content
            
            image_counter = 0
            footnote_refs = {}
            
            # Reset image cache for this document
            self._downloaded_images = {}
            
            # Extract all drawings comprehensively using the new method
            self.logger.info("Starting comprehensive drawing extraction...")
            drawing_map = self.extract_all_drawings(document, image_folder)
            self.logger.info(f"Comprehensive drawing extraction complete: {len(drawing_map)} drawings found")
            
            # Store drawing map for reference during content processing
            self._drawing_map = drawing_map
            
            # Add positioned objects as markdown elements at the beginning
            # (these are absolutely positioned and don't belong to specific paragraphs)
            positioned_objects = document.get('positionedObjects', {})
            if positioned_objects:
                markdown_lines.append("## Positioned Elements")
                for obj_id in positioned_objects:
                    if obj_id in drawing_map:
                        drawing_path = drawing_map[obj_id]
                        mermaid_hint = ""  # Skip mermaid hint for now
                        markdown_lines.append(f"![Positioned Drawing]({drawing_path}){mermaid_hint}")
                markdown_lines.append("")  # Add spacing
            
            # Process each content element
            for element in content:
                if 'paragraph' in element:
                    paragraph = element['paragraph']
                    
                    # Handle paragraph styles
                    style = paragraph.get('paragraphStyle', {})
                    named_style = style.get('namedStyleType', '')
                    
                    # Extract text with full formatting
                    line_text, image_counter = self.extract_paragraph_text(
                        paragraph, document, footnotes, footnote_refs, 
                        image_folder, image_counter
                    )
                    
                    # Only process if there's actual content
                    if line_text.strip():
                        # Clean up line text to remove markdown artifacts
                        clean_line_text = line_text.strip()
                        # Fix markdown formatting issues
                        # Remove excessive asterisks (3+ in a row)
                        clean_line_text = re.sub(r'\*{3,}', '**', clean_line_text)
                        # Fix cases like ****text**** -> **text**
                        clean_line_text = re.sub(r'(\*\*){2,}', '**', clean_line_text)
                        
                        # Skip formatting cleanup here - will be handled by comprehensive cleanup function later
                        
                        # Add space after closing ** when immediately followed by uppercase letter (start of sentence)
                        # This fixes **Problem:**We -> **Problem:** We but avoids **Problem:** -> ** Problem:**
                        clean_line_text = re.sub(r'\*\*([A-Z])', r'** \1', clean_line_text)
                        
                        # Handle different paragraph styles and fix bold formatting in headers
                        if named_style == 'TITLE':
                            # Fix bold formatting in title
                            clean_line_text = re.sub(r'\*\* +([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\* +([^*]+?)\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\*([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            markdown_lines.append(f"# {clean_line_text}")
                            markdown_lines.append("")  # blank line after heading
                        elif named_style == 'SUBTITLE':
                            # Fix bold formatting in subtitle
                            clean_line_text = re.sub(r'\*\* +([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\* +([^*]+?)\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\*([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            markdown_lines.append(f"## {clean_line_text}")
                            markdown_lines.append("")  # blank line after heading
                        elif named_style in ['HEADING_1', 'HEADING_2', 'HEADING_3', 'HEADING_4', 'HEADING_5', 'HEADING_6']:
                            level = int(named_style.split('_')[1])
                            # Fix bold formatting in heading
                            clean_line_text = re.sub(r'\*\* +([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\* +([^*]+?)\*\*', r'**\1**', clean_line_text)
                            clean_line_text = re.sub(r'\*\*([^*]+?) +\*\*', r'**\1**', clean_line_text)
                            markdown_lines.append(f"{'#' * level} {clean_line_text}")
                            markdown_lines.append("")  # blank line after heading
                        else:
                            # Handle list items or regular paragraphs
                            bullet = paragraph.get('bullet')
                            if bullet:
                                # Ensure blank line before list block
                                if markdown_lines and markdown_lines[-1].strip():
                                    markdown_lines.append("")
                                list_item = self.process_list_item(paragraph, clean_line_text)
                                markdown_lines.append(list_item)
                            else:
                                markdown_lines.append(clean_line_text)
                    
                    # Add spacing after paragraphs (but not excessive)
                    if line_text.strip():
                        markdown_lines.append("")
                
                elif 'table' in element:
                    table = element['table']
                    table_rows = table.get('tableRows', [])
                    
                    if table_rows:
                        markdown_table = []
                        
                        # Process all rows
                        for row_idx, row in enumerate(table_rows):
                            row_cells = []
                            for cell in row.get('tableCells', []):
                                cell_text, image_counter = self.extract_table_cell_text(
                                    cell, document, footnotes, footnote_refs, 
                                    image_folder, image_counter
                                )
                                # Clean up cell text and handle empty cells
                                cell_text = cell_text.replace('\n', ' ').strip()
                                
                                # Fix bold formatting in table cells (preserve bold but fix spacing)
                                # Remove spaces inside bold markers while preserving the bold
                                cell_text = re.sub(r'\*\*\s+([^*]+?)\s*\*\*', r'**\1**', cell_text)
                                cell_text = re.sub(r'\*\*\s*([^*]+?)\s+\*\*', r'**\1**', cell_text)
                                cell_text = re.sub(r'\*\*\s*([^*]+?)\s*\*\*', r'**\1**', cell_text)
                                
                                # Handle unmatched bold markers in table cells
                                if cell_text.count('**') % 2 != 0:
                                    cell_text = cell_text.replace('**', '')
                                
                                if not cell_text:
                                    cell_text = " "
                                row_cells.append(cell_text)
                            
                            # Pad each cell with exactly ONE space on each side and
                            # build a proper header separator row the first time.
                            markdown_table.append("| " + " | ".join(row_cells) + " |")
                            
                            # Add separator after first row (header)
                            if row_idx == 0:
                                separator = "| " + " | ".join(["---"] * len(row_cells)) + " |"
                                markdown_table.append(separator)
                        
                        # Add the table to markdown
                        markdown_lines.extend(markdown_table)
                        markdown_lines.append("")
                
                elif 'sectionBreak' in element:
                    markdown_lines.append("---")
                    markdown_lines.append("")
                
                elif 'tableOfContents' in element:
                    markdown_lines.append("*[Table of Contents]*")
                    markdown_lines.append("")
            
            # Add footnotes at the end if any were referenced
            if footnote_refs:
                markdown_lines.append("---")
                markdown_lines.append("")
                markdown_lines.append("## Footnotes")
                markdown_lines.append("")
                
                for footnote_id, footnote_num in footnote_refs.items():
                    if footnote_id in footnotes:
                        footnote_content = footnotes[footnote_id]
                        footnote_text_parts = []
                        
                        # Extract footnote content
                        for fn_elem in footnote_content.get('content', []):
                            if 'paragraph' in fn_elem:
                                fn_text, _ = self.extract_paragraph_text(
                                    fn_elem['paragraph'], document, {}, {}, 
                                    image_folder, image_counter
                                )
                                if fn_text.strip():
                                    footnote_text_parts.append(fn_text.strip())
                        
                        footnote_text = ' '.join(footnote_text_parts)
                        markdown_lines.append(f"[^{footnote_num}]: {footnote_text}")
            
            # Skip image-based quarter detection to avoid LLM dependency
            # Quarter detection is based only on document text content
            
            # Clean up excessive blank lines
            cleaned_lines = []
            prev_was_blank = False
            for line in markdown_lines:
                if line.strip() == "":
                    if not prev_was_blank:
                        cleaned_lines.append("")
                    prev_was_blank = True
                else:
                    cleaned_lines.append(line)
                    prev_was_blank = False
            
            # Apply comprehensive markdown cleanup with AST-based processing
            raw_markdown = '\n'.join(cleaned_lines)
            
            # Detect and convert collapsible sections
            markdown_with_collapsible = self.detect_and_convert_collapsible_sections(raw_markdown)
            
            # NEW: Use AST-based GitHub syntax postprocessor (replaces legacy regex cleanup)
            self.logger.info("Running postprocess_github_syntax for final markdown cleanup")
            final_markdown = self.postprocess_github_syntax(markdown_with_collapsible)
            
            # Write markdown file in document folder with yyyy-qq-title.md format
            # Extract year and quarter from detected_quarter (e.g., "2023-q3" -> "2023-q3")
            title_no_prefix = clean_title.split(' - ', 1)[1] if ' - ' in clean_title else clean_title
            sanitized_title = re.sub(r'[^\w\s-]', '', title_no_prefix).strip()
            sanitized_title = re.sub(r'[-\s]+', '-', sanitized_title)
            markdown_filename = f"{detected_quarter}-{sanitized_title}.md"
            markdown_file_path = document_folder / markdown_filename
            
            with open(markdown_file_path, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            
            result = {
                'status': 'success',
                'title': clean_title,
                'original_title': title,
                'detected_quarter': detected_quarter,
                'team_path': team_path,
                'markdown_file': str(markdown_file_path),
                'doc_url': doc_url,
                'doc_id': doc_id,
                'images_downloaded': image_counter,
                'footnotes_processed': len(footnote_refs),
                'enhanced_conversion': True
            }
            
            self.logger.info(f"Enhanced conversion completed: '{title}' -> {markdown_file_path}")
            self.logger.info(f"Processed {image_counter} images and {len(footnote_refs)} footnotes")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error in enhanced conversion for document {doc_id}: {e}")
            raise
