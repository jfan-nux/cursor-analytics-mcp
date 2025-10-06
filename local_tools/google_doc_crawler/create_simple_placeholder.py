#!/usr/bin/env python3
"""
Create a simple, clean placeholder for Google Drawings that can't be extracted.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def create_simple_placeholder():
    """Create a simple, professional placeholder image."""
    
    # Create a clean, simple image
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
    
    # Add simple text
    title = "Drawing Not Available"
    subtitle = "Google Drawing plugin not supported"
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
    
    return img

if __name__ == "__main__":
    # Create the placeholder
    placeholder = create_simple_placeholder()
    
    # Save to the experiment readout folder
    output_path = Path("context/experiment-readouts/growth/nux/Experiment-Readout-App-Download-Prompt-From-Store-Page/images/drawing_2_thumbnail.png")
    
    placeholder.save(output_path, "PNG")
    print(f"✅ Created simple placeholder: {output_path}")
    print(f"📊 Size: {output_path.stat().st_size:,} bytes")
