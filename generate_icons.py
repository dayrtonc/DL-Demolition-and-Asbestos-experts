#!/usr/bin/env python3.11
from PIL import Image, ImageDraw
import os

# Load the DL Demolition logo
logo_path = 'assets/images/logo_header_optimized.png'
logo = Image.open(logo_path)

# Define icon configurations
# Format: (filename, size, background_color, has_padding, is_maskable)
icon_configs = [
    ('apple-touch-icon.png', 180, (18, 18, 18), True, False),
    ('icon-192.png', 192, (18, 18, 18), True, False),
    ('icon-256.png', 256, (18, 18, 18), True, False),
    ('icon-384.png', 384, (18, 18, 18), True, False),
    ('icon-512.png', 512, (18, 18, 18), True, False),
    ('icon-192-maskable.png', 192, (18, 18, 18), True, True),
    ('icon-512-maskable.png', 512, (18, 18, 18), True, True),
]

def create_icon(filename, size, bg_color, has_padding, is_maskable):
    """Create an icon with the DL Demolition logo"""
    
    # Create background
    if is_maskable:
        # Maskable icons need more padding (safe zone)
        img = Image.new('RGB', (size, size), bg_color)
        # Maskable icons use 80% of the space (20% safe zone)
        logo_size = int(size * 0.6)
    else:
        img = Image.new('RGB', (size, size), bg_color)
        # Regular icons use 70% of the space
        logo_size = int(size * 0.7)
    
    # Resize logo maintaining aspect ratio
    logo_copy = logo.copy()
    aspect_ratio = logo_copy.height / logo_copy.width
    new_width = logo_size
    new_height = int(new_width * aspect_ratio)
    
    # If height is too large, scale by height instead
    if new_height > logo_size:
        new_height = logo_size
        new_width = int(new_height / aspect_ratio)
    
    logo_resized = logo_copy.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Calculate position to center the logo
    x = (size - new_width) // 2
    y = (size - new_height) // 2
    
    # Paste logo (handle transparency)
    if logo_resized.mode == 'RGBA':
        img.paste(logo_resized, (x, y), logo_resized)
    else:
        img.paste(logo_resized, (x, y))
    
    # Save the icon
    output_path = f'assets/images/{filename}'
    img.save(output_path, 'PNG', optimize=True)
    print(f'✓ Created: {output_path} ({size}x{size})')

# Generate all icons
print('Generating DL Demolition branded icons...\n')

for config in icon_configs:
    create_icon(*config)

print('\n✅ All icons generated successfully!')
