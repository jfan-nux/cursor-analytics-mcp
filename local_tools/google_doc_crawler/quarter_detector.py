#!/usr/bin/env python3
"""
Quarter and Date Detection for Experiment Readouts

Detects DoorDash quarters from experiment documents using:
1. Text analysis (dates, quarters, timelines)
2. Image recognition (timeline diagrams)
3. Document metadata

DoorDash Quarters:
- Q1: January, February, March
- Q2: April, May, June  
- Q3: July, August, September
- Q4: October, November, December
"""

import re
import os
import json
from datetime import datetime, date
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path

from utils.logger import get_logger
from utils.portkey_llm import get_portkey_llm


class QuarterDetector:
    """Detects experiment quarters from Google Docs content."""
    
    def __init__(self):
        """Initialize the quarter detector."""
        self.logger = get_logger(__name__)
        try:
            self.llm = get_portkey_llm()
        except Exception as e:
            self.logger.debug(f"LLM initialization failed: {e}")
            self.llm = None
        
        # Quarter mappings for DoorDash fiscal quarters
        self.quarter_months = {
            'q1': [1, 2, 3],     # Jan, Feb, Mar
            'q2': [4, 5, 6],     # Apr, May, Jun
            'q3': [7, 8, 9],     # Jul, Aug, Sep
            'q4': [10, 11, 12]   # Oct, Nov, Dec
        }
        
        self.month_names = {
            'january': 1, 'jan': 1,
            'february': 2, 'feb': 2,
            'march': 3, 'mar': 3,
            'april': 4, 'apr': 4,
            'may': 5,
            'june': 6, 'jun': 6,
            'july': 7, 'jul': 7,
            'august': 8, 'aug': 8,
            'september': 9, 'sep': 9, 'sept': 9,
            'october': 10, 'oct': 10,
            'november': 11, 'nov': 11,
            'december': 12, 'dec': 12
        }
    
    def get_quarter_from_month(self, month: int, year: int = None) -> str:
        """Convert month number to DoorDash quarter in yyyy-qq format."""
        if year is None:
            year = datetime.now().year
            
        for quarter, months in self.quarter_months.items():
            if month in months:
                return f"{year}-{quarter}"
        return f"{year}-q1"  # Default fallback
    
    def extract_dates_from_text(self, text: str) -> List[Tuple[int, int]]:
        """
        Extract dates from text content.
        
        Returns:
            List of (month, year) tuples
        """
        dates = []
        
        # Pattern 1: MM/DD/YYYY or MM/DD/YY
        date_patterns = [
            r'(\d{1,2})/(\d{1,2})/(\d{4})',           # 7/25/2023
            r'(\d{1,2})/(\d{1,2})/(\d{2})',            # 7/25/23
            r'(\d{1,2})-(\d{1,2})-(\d{4})',            # 7-25-2023
            r'(\d{1,2})-(\d{1,2})-(\d{2})',            # 7-25-23
            r'(\d{1,2})\.(\d{1,2})\.(\d{4})',          # 7.25.2023
            r'(\d{1,2})\.(\d{1,2})\.(\d{2})',          # 7.25.23
        ]
        
        for pattern in date_patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                try:
                    month = int(match.group(1))
                    year = int(match.group(3))
                    if year < 100:  # Convert 2-digit year
                        year = 2000 + year if year < 50 else 1900 + year
                    if 1 <= month <= 12:
                        dates.append((month, year))
                except (ValueError, IndexError):
                    continue
        
        # Pattern 2: Month name + year
        month_year_pattern = r'(\w+)\s+(\d{4})'
        matches = re.finditer(month_year_pattern, text.lower())
        for match in matches:
            month_name = match.group(1)
            year = int(match.group(2))
            if month_name in self.month_names:
                month = self.month_names[month_name]
                dates.append((month, year))
        
        # Pattern 3: Just year (use current month as fallback)
        year_pattern = r'\b(20\d{2})\b'
        matches = re.finditer(year_pattern, text)
        current_month = datetime.now().month
        for match in matches:
            year = int(match.group(1))
            if 2020 <= year <= 2030:  # Reasonable range
                dates.append((current_month, year))
        
        return list(set(dates))  # Remove duplicates
    
    def detect_quarter_from_timeline_text(self, text: str) -> Optional[str]:
        """
        Detect quarter from timeline-specific text patterns.
        
        Args:
            text: Text content from the document
            
        Returns:
            Quarter string (Q1, Q2, Q3, Q4) or None
        """
        # Look for specific timeline indicators
        timeline_patterns = [
            r'test\s+launched[:\s]*(\d{1,2})/(\d{1,2})/(\d{2,4})',  # "Test Launched: 7/25/23"
            r'final\s+readout[:\s]*(\d{1,2})/(\d{1,2})/(\d{2,4})',  # "Final Readout: 8/1/2023"
            r'experiment\s+timeline[:\s]*.*?(\d{1,2})/(\d{1,2})/(\d{2,4})',
            r'measurement\s+period[:\s]*.*?(\d{1,2})/(\d{1,2})/(\d{2,4})',
        ]
        
        for pattern in timeline_patterns:
            matches = re.finditer(pattern, text.lower())
            for match in matches:
                try:
                    month = int(match.group(1))
                    year = int(match.group(3))
                    if year < 100:
                        year = 2000 + year if year < 50 else 1900 + year
                    if 1 <= month <= 12:
                        quarter = self.get_quarter_from_month(month, year)
                        self.logger.info(f"Found timeline date: {month}/{year} -> {quarter}")
                        return quarter
                except (ValueError, IndexError):
                    continue
        
        return None
    
    def extract_dates_with_llm(self, text: str) -> Optional[str]:
        """
        Use LLM to intelligently extract experiment dates from document text.
        
        Args:
            text: Document text content
            
        Returns:
            Quarter in yyyy-qq format or None if not found
        """
        if not self.llm or not self.llm.is_available():
            self.logger.warning("LLM not available, falling back to regex extraction")
            return None
        
        prompt = """
You are analyzing an experiment readout document to extract the experiment timeline dates.

Look for any dates related to:
- Test launch date
- Experiment start/end dates  
- Final readout date
- Measurement period
- Timeline diagrams
- Any other relevant experiment dates

DoorDash quarters are:
- Q1: January, February, March
- Q2: April, May, June  
- Q3: July, August, September
- Q4: October, November, December

Return ONLY the quarter in yyyy-qq format (e.g., "2023-q3") based on the most relevant experiment date you find.
If you cannot find any clear experiment dates, return "NONE".

Example responses:
- "2023-q3" (for July 2023)
- "2024-q1" (for February 2024)
- "NONE" (if no dates found)
"""
        
        try:
            response = self.llm.analyze_text(
                text=text,
                prompt=prompt,
                model="gpt-4o-mini",
                max_tokens=50,
                temperature=0.0
            )
            
            if response and response.strip() != "NONE":
                # Validate the format
                quarter_pattern = r'^\d{4}-q[1-4]$'
                clean_response = response.strip().lower()
                # Remove any quotes or extra characters
                clean_response = re.sub(r'["\'\s]', '', clean_response)
                if re.match(quarter_pattern, clean_response):
                    self.logger.info(f"LLM extracted quarter: {clean_response}")
                    return clean_response
                else:
                    self.logger.warning(f"LLM returned invalid quarter format: '{response}' -> '{clean_response}'")
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error in LLM date extraction: {e}")
            return None
    
    def analyze_document_content(self, document: Dict[str, Any]) -> Optional[str]:
        """
        Analyze document content to detect experiment quarter.
        
        Args:
            document: Google Docs API document object
            
        Returns:
            Quarter string (Q1, Q2, Q3, Q4) or None
        """
        # Extract all text from document
        full_text = ""
        content = document.get('body', {}).get('content', [])
        
        for element in content:
            if 'paragraph' in element:
                paragraph = element['paragraph']
                if 'elements' in paragraph:
                    for elem in paragraph['elements']:
                        if 'textRun' in elem:
                            text = elem['textRun'].get('content', '')
                            full_text += text
        
        self.logger.info(f"Analyzing document text ({len(full_text)} characters) for quarter detection")
        
        # Try LLM-powered extraction first (most intelligent)
        quarter = self.extract_dates_with_llm(full_text)
        if quarter:
            return quarter
        
        # Fallback: Try timeline-specific detection
        quarter = self.detect_quarter_from_timeline_text(full_text)
        if quarter:
            return quarter
        
        # Extract all dates from text
        dates = self.extract_dates_from_text(full_text)
        
        if not dates:
            self.logger.warning("No dates found in document text")
            return None
        
        # Find the most likely experiment date (most recent or most common)
        date_counts = {}
        for month, year in dates:
            quarter = self.get_quarter_from_month(month, year)
            date_counts[quarter] = date_counts.get(quarter, 0) + 1
        
        if date_counts:
            # Get the most frequently mentioned quarter
            most_common = max(date_counts.items(), key=lambda x: x[1])
            quarter = most_common[0]
            
            self.logger.info(f"Detected experiment quarter: {quarter} (mentioned {most_common[1]} times)")
            return quarter
        
        return None
    

    
    def detect_experiment_quarter(self, document: Dict[str, Any], 
                                image_folder: Optional[Path] = None) -> str:
        """
        Detect experiment quarter using multiple methods.
        
        Args:
            document: Google Docs API document object
            image_folder: Optional path to images for timeline analysis
            
        Returns:
            Quarter string (Q1, Q2, Q3, Q4), defaults to current quarter if detection fails
        """
        # Method 1: Analyze document text content
        quarter = self.analyze_document_content(document)
        if quarter:
            self.logger.info(f"Quarter detected from text: {quarter}")
            return quarter
        
        # Method 2: Image analysis removed - no longer using LLM for image analysis
        
        # Fallback: Use current quarter
        current_month = datetime.now().month
        current_year = datetime.now().year
        current_quarter = self.get_quarter_from_month(current_month, current_year)
        self.logger.warning(f"Could not detect quarter, using current quarter: {current_quarter}")
        
        return current_quarter
    
    def clean_document_title(self, title: str, quarter: str) -> str:
        """
        Clean document title and add quarter prefix.
        
        Args:
            title: Original document title
            quarter: Detected quarter
            
        Returns:
            Cleaned title with quarter prefix
        """
        # Remove "Experiment Readout:" prefix if present
        clean_title = title
        prefixes_to_remove = [
            'experiment readout:',
            'experiment readout -',
            'experiment readout',
            'readout:',
            'readout -',
        ]
        
        for prefix in prefixes_to_remove:
            if clean_title.lower().startswith(prefix):
                clean_title = clean_title[len(prefix):].strip()
                break
        
        # Add quarter prefix (extract just the quarter part from yyyy-qq format)
        quarter_part = quarter.split('-')[1].upper()  # Convert 2023-q3 -> Q3
        final_title = f"{quarter_part} - {clean_title}"
        
        self.logger.info(f"Title transformation: '{title}' -> '{final_title}' (quarter: {quarter})")
        return final_title
