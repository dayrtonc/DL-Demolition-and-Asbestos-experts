#!/usr/bin/env python3.11
from PIL import Image, ImageDraw, ImageFont
import os
import shutil

# Backup old image first if it exists
output_path = 'assets/images/og-image.jpg'
backup_path = 'assets/images/og-image-breathesafe-backup.jpg'

if os.path.exists(output_path) and not os.path.exists(backup_path):
    shutil.copy2(output_path, backup_path)
    print(f"Old image backed up to: {backup_path}")

# Create a 1200x630 image (standard OG image size)
width = 1200
height = 630

# Create image with DL Demolition brand colors
# Background: dark gray/black
bg_color = (18, 18, 18)
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Add red stripe at bottom (DL Demolition brand color)
red_color = (225, 6, 0)
stripe_height = 80
draw.rectangle([(0, height - stripe_height), (width, height)], fill=red_color)

# Load and resize the logo
logo_path = 'assets/images/logo_header_optimized.png'
try:
    logo = Image.open(logo_path)
    # Resize logo to fit nicely (max 400px wide, maintain aspect ratio)
    logo_max_width = 400
    aspect_ratio = logo.height / logo.width
    new_width = logo_max_width
    new_height = int(new_width * aspect_ratio)
    logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Center the logo
    logo_x = (width - new_width) // 2
    logo_y = 80  # Position from top
    
    # Paste logo (handle transparency if present)
    if logo.mode == 'RGBA':
        img.paste(logo, (logo_x, logo_y), logo)
    else:
        img.paste(logo, (logo_x, logo_y))
except Exception as e:
    print(f"Error loading logo: {e}")

# Add text below logo
try:
    # Try to use a system font
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
except:
    # Fallback to default font
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()

# Text content
text1 = "DL Demolition and Asbestos Experts"
text2 = "Professional Demolition & Asbestos Removal"
text3 = "Gold Coast • Sunshine Coast • Brisbane"

# Calculate text positions (centered)
text_y = 350

# Draw text with white color
text_color = (255, 255, 255)

# Get text bounding boxes for centering
bbox1 = draw.textbbox((0, 0), text1, font=font_large)
text1_width = bbox1[2] - bbox1[0]
text1_x = (width - text1_width) // 2

bbox2 = draw.textbbox((0, 0), text2, font=font_medium)
text2_width = bbox2[2] - bbox2[0]
text2_x = (width - text2_width) // 2

bbox3 = draw.textbbox((0, 0), text3, font=font_medium)
text3_width = bbox3[2] - bbox3[0]
text3_x = (width - text3_width) // 2

# Draw the text
draw.text((text1_x, text_y), text1, fill=text_color, font=font_large)
draw.text((text2_x, text_y + 60), text2, fill=text_color, font=font_medium)
draw.text((text3_x, text_y + 110), text3, fill=text_color, font=font_medium)

# Save the image
img.save(output_path, 'JPEG', quality=95, optimize=True)
print(f"Open Graph image created successfully: {output_path}")
