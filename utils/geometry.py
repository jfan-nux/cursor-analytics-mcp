# ── utils/geometry.py ────────────────────────────────────────────────────────────
"""
Geometry utilities for Google Docs drawing extraction.

This module provides utilities for converting between Google Docs coordinate systems
and image pixel coordinates, and for cropping images based on geometric constraints.
"""

from pathlib import Path
from typing import Optional


def pt_to_px(pt: float, dpi: int = 96) -> int:
    """
    Convert points (1/72 inch) to integer pixels for a given DPI.
    
    Args:
        pt: Size in points (PostScript points, 1/72 inch)
        dpi: Dots per inch (default 96 for standard screen resolution)
        
    Returns:
        Size in pixels as integer
        
    Examples:
        >>> pt_to_px(72, 96)  # 1 inch at 96 DPI
        96
        >>> pt_to_px(36, 300)  # 0.5 inch at 300 DPI  
        150
    """
    return int(round(pt * dpi / 72))


def crop_image(source_path: Path, dest_path: Path,
               left: int, top: int, width: int, height: int) -> None:
    """
    Crop a rectangular region from source image and save to destination.
    
    Args:
        source_path: Path to source image file
        dest_path: Path where cropped image will be saved
        left: Left edge of crop region in pixels
        top: Top edge of crop region in pixels  
        width: Width of crop region in pixels
        height: Height of crop region in pixels
        
    Raises:
        ImportError: If PIL/Pillow is not installed
        IOError: If source image cannot be opened
        ValueError: If crop region is invalid
        
    Examples:
        >>> crop_image(Path("full.png"), Path("cropped.png"), 10, 20, 100, 50)
        # Crops 100x50 pixel region starting at (10, 20)
    """
    try:
        from PIL import Image
    except ImportError:
        raise ImportError(
            "Pillow is required for image cropping. Install with: pip install pillow"
        )
    
    # Validate inputs
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid crop dimensions: {width}x{height}")
    if left < 0 or top < 0:
        raise ValueError(f"Invalid crop position: ({left}, {top})")
    
    try:
        with Image.open(source_path) as im:
            # Validate crop region is within image bounds
            img_width, img_height = im.size
            if left + width > img_width or top + height > img_height:
                raise ValueError(
                    f"Crop region ({left}, {top}, {width}, {height}) "
                    f"exceeds image bounds ({img_width}, {img_height})"
                )
            
            # Perform crop: PIL crop takes (left, top, right, bottom)
            box = (left, top, left + width, top + height)
            cropped = im.crop(box)
            
            # Save cropped image
            cropped.save(dest_path)
            
    except Exception as e:
        raise IOError(f"Failed to crop image {source_path}: {e}")


def calculate_drawing_bounds(embedded_object: dict, dpi: int = 300) -> tuple[int, int, int, int]:
    """
    Calculate pixel coordinates for a Google Docs embedded object.
    
    Args:
        embedded_object: Google Docs embedded object with size and transform data
        dpi: Target DPI for pixel conversion
        
    Returns:
        Tuple of (left_px, top_px, width_px, height_px)
        
    Raises:
        KeyError: If required size information is missing
        ValueError: If size values are invalid
    """
    try:
        # Extract size in points
        size = embedded_object["size"]
        w_pt = size["width"]["magnitude"]
        h_pt = size["height"]["magnitude"]
        
        if w_pt <= 0 or h_pt <= 0:
            raise ValueError(f"Invalid object size: {w_pt}x{h_pt} points")
        
        # Convert to pixels
        w_px = pt_to_px(w_pt, dpi)
        h_px = pt_to_px(h_pt, dpi)
        
        # Calculate position
        left_px = 0
        top_px = 0
        
        # For positioned objects, use transform coordinates
        if "transform" in embedded_object:
            transform = embedded_object["transform"]
            left_px = pt_to_px(transform.get("translateX", 0), dpi)
            top_px = pt_to_px(transform.get("translateY", 0), dpi)
        
        # For inline objects, position is relative to paragraph
        # (we assume top-left of paragraph for now)
        
        return (left_px, top_px, w_px, h_px)
        
    except KeyError as e:
        raise KeyError(f"Missing required geometry data in embedded object: {e}")
