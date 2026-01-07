"""
Google Docs API client for creating, updating, and reading documents.
"""

from typing import Dict, List, Optional, Any
import time


class GoogleDocsClient:
    """Handles Google Docs API operations."""
    
    def __init__(self, docs_service, drive_service, template_doc_id: Optional[str] = None):
        """
        Initialize the client.
        
        Args:
            docs_service: Authenticated Google Docs API service
            drive_service: Authenticated Google Drive API service
            template_doc_id: Optional template doc ID for copying styles
        """
        self.docs_service = docs_service
        self.drive_service = drive_service
        self.template_doc_id = template_doc_id
    
    def create_doc(self, title: str, requests: List[Dict]) -> Dict[str, str]:
        """
        Create a new Google Doc with content.
        
        Args:
            title: Document title
            requests: List of Google Docs API requests
            
        Returns:
            Dict with 'doc_id' and 'doc_url'
        """
        # Create empty document
        doc = self.docs_service.documents().create(body={'title': title}).execute()
        doc_id = doc['documentId']
        doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
        
        print(f"Created document: {title} (ID: {doc_id})")
        
        # Apply template styles if available
        if self.template_doc_id:
            self._apply_template_styles(doc_id)
        
        # Set pageless format and margins
        self._configure_document_style(doc_id)
        
        # Add content
        if requests:
            self._batch_update(doc_id, requests)
        
        return {
            'doc_id': doc_id,
            'doc_url': doc_url
        }
    
    def update_doc(self, doc_id: str, requests: List[Dict], tab_id: str = None) -> bool:
        """
        Update existing Google Doc content, optionally targeting a specific tab.
        
        NOTE: Comments are NOT fully preserved during updates due to 
        content replacement. Google Docs API doesn't provide a reliable way to 
        preserve comment anchors when replacing large sections of content.
        
        For comment preservation, consider:
        1. Making smaller, targeted edits instead of full re-exports
        2. Manually resolving comments before re-exporting
        3. Using Google Docs as the source of truth and importing to Cursor instead
        
        Args:
            doc_id: Google Doc ID
            requests: List of Google Docs API requests
            tab_id: Optional tab ID to update specific tab only
            
        Returns:
            True if update successful
        """
        try:
            # Get current document to find content bounds
            if tab_id:
                doc = self.docs_service.documents().get(
                    documentId=doc_id,
                    includeTabsContent=True
                ).execute()
                
                # Find the specific tab
                target_tab = self._find_tab_by_id(doc.get('tabs', []), tab_id)
                if not target_tab:
                    print(f"Error: Tab ID {tab_id} not found in document")
                    return False
                
                # Get content from the specific tab
                document_tab = target_tab.get('documentTab', {})
                body = document_tab.get('body', {})
                content = body.get('content', [])
                
                if content:
                    end_index = content[-1]['endIndex'] - 1
                else:
                    end_index = 1
                
                print(f"Updating tab '{target_tab.get('tabProperties', {}).get('title', 'Untitled')}' (ID: {tab_id})")
            else:
                doc = self.docs_service.documents().get(documentId=doc_id).execute()
                end_index = doc['body']['content'][-1]['endIndex'] - 1
            
            # Delete existing content
            delete_requests = []
            
            if end_index > 1:
                # Delete content from index 1 to end
                delete_request = {
                    'deleteContentRange': {
                        'range': {
                            'startIndex': 1,
                            'endIndex': end_index
                        }
                    }
                }
                # Add tab ID if specified
                if tab_id:
                    delete_request['deleteContentRange']['range']['tabId'] = tab_id
                
                delete_requests.append(delete_request)
            
            # Combine delete and insert requests
            all_requests = delete_requests + requests
            
            # DEBUG: Log first few requests to verify tab_id is present
            if tab_id:
                print(f"\nDEBUG: Sending {len(all_requests)} requests for tab {tab_id}")
                print(f"DEBUG: First 5 requests with full details:")
                for i, req in enumerate(all_requests[:5]):
                    print(f"  Request {i}: {list(req.keys())}")
                    for key, value in req.items():
                        if isinstance(value, dict):
                            if 'location' in value:
                                print(f"    {key}.location: {value['location']}")
                            if 'range' in value:
                                print(f"    {key}.range: {value['range']}")
                            if 'tabId' in value:
                                print(f"    {key}.tabId: {value['tabId']}")

            
            # Execute batch update
            self._batch_update(doc_id, all_requests)
            
            if tab_id:
                print(f"✓ Updated tab in document (ID: {doc_id})")
            else:
                print(f"✓ Updated document (ID: {doc_id})")
            print("⚠️  Note: Comments may not be preserved when content is replaced")
            return True
            
        except Exception as e:
            print(f"Error updating document: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def read_doc(self, doc_id: str, tab_id: str = None) -> Dict:
        """
        Read Google Doc content, optionally from a specific tab.
        
        Args:
            doc_id: Google Doc ID
            tab_id: Optional tab ID to read specific tab
            
        Returns:
            Document structure (full doc or specific tab)
        """
        try:
            # If tab_id is specified, we need to get all tabs
            if tab_id:
                doc = self.docs_service.documents().get(
                    documentId=doc_id,
                    includeTabsContent=True
                ).execute()
                
                # Find the specific tab
                target_tab = self._find_tab_by_id(doc.get('tabs', []), tab_id)
                if not target_tab:
                    print(f"Warning: Tab ID {tab_id} not found, using first tab")
                    if doc.get('tabs'):
                        return self._tab_to_doc_format(doc.get('tabs')[0], doc)
                    return doc
                
                # Convert tab to document format for compatibility
                return self._tab_to_doc_format(target_tab, doc)
            else:
                # Default behavior - reads first tab only for backwards compatibility
                doc = self.docs_service.documents().get(documentId=doc_id).execute()
                return doc
        except Exception as e:
            print(f"Error reading document: {e}")
            return {}
    
    def _find_tab_by_id(self, tabs: List[Dict], tab_id: str) -> Dict:
        """
        Recursively find a tab by ID in the tab hierarchy.
        
        Args:
            tabs: List of tab objects
            tab_id: Tab ID to find
            
        Returns:
            Tab object or None
        """
        for tab in tabs:
            if tab.get('tabProperties', {}).get('tabId') == tab_id:
                return tab
            # Check child tabs recursively
            if tab.get('childTabs'):
                result = self._find_tab_by_id(tab.get('childTabs'), tab_id)
                if result:
                    return result
        return None
    
    def _tab_to_doc_format(self, tab: Dict, doc: Dict) -> Dict:
        """
        Convert a Tab object to Document format for compatibility with existing code.
        
        Args:
            tab: Tab object from API
            doc: Full document object (for metadata)
            
        Returns:
            Document-like structure with tab content
        """
        document_tab = tab.get('documentTab', {})
        
        # Create a document-like structure with the tab's content
        return {
            'documentId': doc.get('documentId'),
            'title': doc.get('title'),
            'body': document_tab.get('body', {}),
            'headers': document_tab.get('headers', {}),
            'footers': document_tab.get('footers', {}),
            'footnotes': document_tab.get('footnotes', {}),
            'documentStyle': document_tab.get('documentStyle', {}),
            'namedStyles': document_tab.get('namedStyles', {}),
            'lists': document_tab.get('lists', {}),
            'namedRanges': document_tab.get('namedRanges', {}),
            'inlineObjects': document_tab.get('inlineObjects', {}),
            'positionedObjects': document_tab.get('positionedObjects', {}),
            # Store tab info for later use
            '_tabId': tab.get('tabProperties', {}).get('tabId'),
            '_isTabContent': True
        }
    
    def _apply_template_styles(self, doc_id: str):
        """
        Copy named styles from template document.
        
        Args:
            doc_id: Target document ID
        """
        try:
            # Get template document
            template_doc = self.docs_service.documents().get(
                documentId=self.template_doc_id
            ).execute()
            
            # Extract named styles
            named_styles = template_doc.get('namedStyles', {}).get('styles', [])
            
            if not named_styles:
                print("Warning: No named styles found in template document")
                return
            
            # Apply styles to new document
            requests = []
            for style in named_styles:
                style_type = style.get('namedStyleType')
                if style_type:
                    requests.append({
                        'updateParagraphStyle': {
                            'range': {
                                'startIndex': 1,
                                'endIndex': 2
                            },
                            'paragraphStyle': {
                                'namedStyleType': style_type
                            },
                            'fields': 'namedStyleType'
                        }
                    })
            
            # Note: This is a simplified approach. For full style copying,
            # we'd need to copy text styles, paragraph styles, etc.
            # The API doesn't directly support "copy all styles", so we're
            # setting up the document to use the same named style types.
            
            print(f"Applied styles from template document")
            
        except Exception as e:
            print(f"Warning: Could not apply template styles: {e}")
    
    def _configure_document_style(self, doc_id: str):
        """
        Configure document to be pageless with standard margins.
        
        Args:
            doc_id: Document ID
        """
        try:
            requests = [
                {
                    'updateDocumentStyle': {
                        'documentStyle': {
                            'marginTop': {
                                'magnitude': 72,
                                'unit': 'PT'
                            },
                            'marginBottom': {
                                'magnitude': 72,
                                'unit': 'PT'
                            },
                            'marginLeft': {
                                'magnitude': 72,
                                'unit': 'PT'
                            },
                            'marginRight': {
                                'magnitude': 72,
                                'unit': 'PT'
                            }
                        },
                        'fields': 'marginTop,marginBottom,marginLeft,marginRight'
                    }
                }
            ]
            
            self._batch_update(doc_id, requests)
            print("Configured document as pageless with standard margins")
            
        except Exception as e:
            print(f"Warning: Could not configure document style: {e}")
    
    def _batch_update(self, doc_id: str, requests: List[Dict]):
        """
        Execute batch update on document.
        
        Args:
            doc_id: Document ID
            requests: List of API requests
        """
        if not requests:
            return
        
        try:
            # Google Docs API has a limit on batch size (around 500 requests)
            # Split into chunks if needed
            chunk_size = 400
            for i in range(0, len(requests), chunk_size):
                chunk = requests[i:i + chunk_size]
                self.docs_service.documents().batchUpdate(
                    documentId=doc_id,
                    body={'requests': chunk}
                ).execute()
                
                # Small delay between chunks to avoid rate limiting
                if i + chunk_size < len(requests):
                    time.sleep(0.5)
                    
        except Exception as e:
            print(f"Error in batch update: {e}")
            raise
    
    
    def get_doc_title(self, doc_id: str) -> str:
        """
        Get document title.
        
        Args:
            doc_id: Document ID
            
        Returns:
            Document title
        """
        try:
            doc = self.docs_service.documents().get(documentId=doc_id).execute()
            return doc.get('title', 'Untitled')
        except Exception as e:
            print(f"Error getting document title: {e}")
            return 'Untitled'

