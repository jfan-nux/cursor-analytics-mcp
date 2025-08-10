#!/usr/bin/env python3
"""
PortkeyLLM Utility Class

Shared utility for accessing Portkey LLM services for both text and image analysis.
Supports multiple LLM providers through Portkey gateway.
"""

import os
import base64
from typing import Dict, Any, List, Optional, Union
from pathlib import Path

from utils.logger import get_logger

try:
    from portkey_ai import Portkey
    PORTKEY_AVAILABLE = True
except ImportError:
    PORTKEY_AVAILABLE = False


class PortkeyLLM:
    """
    Shared LLM utility class for text and vision analysis using Portkey.
    
    Supports:
    - Text analysis and extraction
    - Image analysis and OCR
    - Multiple LLM providers (OpenAI, Claude, etc.)
    - Configurable models for different tasks
    """
    
    def __init__(self):
        """Initialize the PortkeyLLM client."""
        self.logger = get_logger(__name__)
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Portkey client with configuration from environment."""
        if not PORTKEY_AVAILABLE:
            self.logger.debug("Portkey AI library not available. Please install portkey-ai")
            return
        
        try:
            # Get Portkey configuration from environment
            base_url = os.getenv('PORTKEY_BASE_URL')
            api_key = os.getenv('PORTKEY_API_KEY')
            virtual_key = os.getenv('PORTKEY_OPENAI_VIRTUAL_KEY')
            
            if not all([base_url, api_key, virtual_key]):
                self.logger.debug("Missing Portkey configuration in environment variables - LLM features disabled")
                return
            
            self.client = Portkey(
                base_url=base_url,
                api_key=api_key,
                virtual_key=virtual_key
            )
            
            self.logger.info("Successfully initialized Portkey client")
            
        except Exception as e:
            self.logger.debug(f"Failed to initialize Portkey client: {e}")
    
    def analyze_text(self, 
                    text: str, 
                    prompt: str, 
                    model: str = "gpt-4o-mini",
                    max_tokens: int = 1000,
                    temperature: float = 0.1) -> Optional[str]:
        """
        Analyze text using LLM.
        
        Args:
            text: Text content to analyze
            prompt: Analysis prompt/instruction
            model: LLM model to use
            max_tokens: Maximum response tokens
            temperature: Response randomness (0.0-1.0)
            
        Returns:
            LLM response or None if failed
        """
        if not self.client:
            self.logger.debug("Portkey client not initialized - LLM analysis unavailable")
            return None
        
        try:
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ]
            
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            result = response.choices[0].message.content
            self.logger.info(f"Text analysis completed: {len(text)} chars -> {len(result)} chars")
            return result
            
        except Exception as e:
            self.logger.error(f"Error in text analysis: {e}")
            return None
    
    def analyze_image(self, 
                     image_path: Union[str, Path], 
                     prompt: str,
                     model: str = "gpt-4o",
                     max_tokens: int = 1000,
                     temperature: float = 0.1) -> Optional[str]:
        """
        Analyze image using vision LLM.
        
        Args:
            image_path: Path to image file
            prompt: Analysis prompt/instruction
            model: Vision-capable LLM model to use
            max_tokens: Maximum response tokens
            temperature: Response randomness (0.0-1.0)
            
        Returns:
            LLM response or None if failed
        """
        if not self.client:
            self.logger.debug("Portkey client not initialized - LLM analysis unavailable")
            return None
        
        try:
            image_path = Path(image_path)
            if not image_path.exists():
                self.logger.error(f"Image file not found: {image_path}")
                return None
            
            # Read and encode image
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            
            # Determine image format
            image_format = image_path.suffix.lower().lstrip('.')
            if image_format == 'jpg':
                image_format = 'jpeg'
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{image_format};base64,{image_base64}"
                            }
                        }
                    ]
                }
            ]
            
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            result = response.choices[0].message.content
            self.logger.info(f"Image analysis completed: {image_path.name} -> {len(result)} chars")
            return result
            
        except Exception as e:
            self.logger.error(f"Error in image analysis: {e}")
            return None
    
    def analyze_images_batch(self, 
                           image_paths: List[Union[str, Path]], 
                           prompt: str,
                           model: str = "gpt-4o",
                           max_tokens: int = 1500,
                           temperature: float = 0.1) -> List[Optional[str]]:
        """
        Analyze multiple images in batch.
        
        Args:
            image_paths: List of paths to image files
            prompt: Analysis prompt/instruction
            model: Vision-capable LLM model to use
            max_tokens: Maximum response tokens
            temperature: Response randomness (0.0-1.0)
            
        Returns:
            List of LLM responses (same order as input)
        """
        results = []
        
        for image_path in image_paths:
            result = self.analyze_image(
                image_path=image_path,
                prompt=prompt,
                model=model,
                max_tokens=max_tokens,
                temperature=temperature
            )
            results.append(result)
        
        self.logger.info(f"Batch image analysis completed: {len(image_paths)} images")
        return results
    
    def extract_structured_data(self, 
                              text: str, 
                              schema_description: str,
                              model: str = "gpt-4o-mini",
                              max_tokens: int = 1000) -> Optional[str]:
        """
        Extract structured data from text using LLM.
        
        Args:
            text: Text content to analyze
            schema_description: Description of expected output structure
            model: LLM model to use
            max_tokens: Maximum response tokens
            
        Returns:
            Structured data as string (JSON, CSV, etc.) or None if failed
        """
        prompt = f"""
Extract structured data from the following text according to this schema:

{schema_description}

Please respond with ONLY the structured data, no explanations or additional text.

Text to analyze:
"""
        
        return self.analyze_text(
            text=text,
            prompt=prompt,
            model=model,
            max_tokens=max_tokens,
            temperature=0.0  # Use deterministic output for structured data
        )
    
    def is_available(self) -> bool:
        """Check if PortkeyLLM is available and properly configured."""
        return self.client is not None


# Global instance for shared use
_portkey_instance = None

def get_portkey_llm() -> PortkeyLLM:
    """
    Get shared PortkeyLLM instance (singleton pattern).
    
    Returns:
        PortkeyLLM instance
    """
    global _portkey_instance
    if _portkey_instance is None:
        _portkey_instance = PortkeyLLM()
    return _portkey_instance
