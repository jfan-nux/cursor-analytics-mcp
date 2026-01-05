"""
Client for calling Apps Script to process documents.
"""

from typing import Dict, Optional
from googleapiclient.discovery import build


class AppsScriptClient:
    """Calls Apps Script functions using the Apps Script API."""
    
    def __init__(self, script_service, script_id: str):
        """
        Initialize Apps Script client.
        
        Args:
            script_service: Authenticated Apps Script API service
            script_id: The Script ID (not the deployment ID)
        """
        self.script_service = script_service
        self.script_id = script_id
    
    def process_document(self, document_id: str, template_doc_id: Optional[str] = None, tab_id: Optional[str] = None) -> Dict:
        """
        Call Apps Script to process a document.
        Replaces [img][path] markers with images and applies template styles.
        
        Args:
            document_id: Google Doc ID to process
            template_doc_id: Optional template doc ID for styles
            tab_id: Optional tab ID to process only a specific tab
            
        Returns:
            Dict with processing results
        """
        try:
            # Call the Apps Script function
            request = {
                'function': 'processDocument',
                'parameters': [document_id, template_doc_id, tab_id]
            }
            
            response = self.script_service.scripts().run(
                scriptId=self.script_id,
                body=request
            ).execute()
            
            # Check for errors
            if 'error' in response:
                error = response['error']
                error_message = error.get('details', [{}])[0].get('errorMessage', str(error))
                return {
                    'success': False,
                    'message': f'Apps Script error: {error_message}'
                }
            
            # Get the result
            result = response.get('response', {}).get('result', {})
            
            # If result is None, the function returned void - assume success
            if result is None:
                result = {'success': True, 'message': 'Processed successfully'}
            
            return result
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Error calling Apps Script: {e}'
            }


