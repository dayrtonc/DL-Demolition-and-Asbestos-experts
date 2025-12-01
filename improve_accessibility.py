import re
import os
import glob

def improve_accessibility(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # Add role="navigation" to nav elements without it
    if '<nav ' in content and 'role=' not in re.search(r'<nav[^>]*>', content).group():
        content = re.sub(r'<nav\s+', '<nav role="navigation" ', content, count=1)
        changes_made.append("Added role='navigation' to <nav>")
    
    # Add role="banner" to header if missing
    if '<header ' in content:
        header_match = re.search(r'<header[^>]*>', content)
        if header_match and 'role=' not in header_match.group():
            content = re.sub(r'<header\s+', '<header role="banner" ', content, count=1)
            changes_made.append("Added role='banner' to <header>")
    
    # Add role="main" to main content area if missing
    if '<main' in content:
        main_match = re.search(r'<main[^>]*>', content)
        if main_match and 'role=' not in main_match.group():
            content = re.sub(r'<main\s+', '<main role="main" ', content, count=1)
            changes_made.append("Added role='main' to <main>")
    
    # Add role="contentinfo" to footer if missing
    if '<footer ' in content:
        footer_match = re.search(r'<footer[^>]*>', content)
        if footer_match and 'role=' not in footer_match.group():
            content = re.sub(r'<footer\s+', '<footer role="contentinfo" ', content, count=1)
            changes_made.append("Added role='contentinfo' to <footer>")
    
    # Add aria-label to buttons without text or with only icons
    # Find buttons with only icons (fa- classes)
    icon_buttons = re.findall(r'<button[^>]*>[\s]*<i class="fa[^"]*"[^>]*></i>[\s]*</button>', content)
    for button in icon_buttons:
        if 'aria-label=' not in button:
            # Try to extract icon meaning from class
            icon_match = re.search(r'fa-(\w+)', button)
            if icon_match:
                icon_name = icon_match.group(1)
                label = icon_name.replace('-', ' ').title()
                new_button = button.replace('<button', f'<button aria-label="{label}"')
                content = content.replace(button, new_button, 1)
                changes_made.append(f"Added aria-label to icon button: {label}")
    
    # Add aria-label to mobile menu toggle if present
    if 'mobile-menu-toggle' in content:
        content = re.sub(
            r'(<button[^>]*id="mobile-menu-toggle"[^>]*)(>)',
            r'\1 aria-label="Toggle mobile menu" aria-expanded="false"\2',
            content
        )
        if 'aria-label="Toggle mobile menu"' in content:
            changes_made.append("Added aria-label to mobile menu toggle")
    
    # Add aria-label to WhatsApp floating button
    if 'whatsapp-float' in content or 'wa.me' in content:
        # Find WhatsApp links without aria-label
        wa_links = re.findall(r'<a[^>]*href="https://wa\.me/[^"]*"[^>]*>.*?</a>', content, re.DOTALL)
        for link in wa_links:
            if 'aria-label=' not in link:
                new_link = link.replace('<a ', '<a aria-label="Contact us on WhatsApp" ')
                content = content.replace(link, new_link, 1)
                changes_made.append("Added aria-label to WhatsApp link")
    
    # Add aria-label to phone links
    phone_links = re.findall(r'<a[^>]*href="tel:[^"]*"[^>]*>.*?</a>', content, re.DOTALL)
    for link in phone_links:
        if 'aria-label=' not in link and 'Call Now' not in link:
            new_link = link.replace('<a ', '<a aria-label="Call us now" ')
            content = content.replace(link, new_link, 1)
            changes_made.append("Added aria-label to phone link")
    
    # Save if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made
    return False, []

# Process all HTML files
html_files = glob.glob('*.html')
total_changes = 0

print("🔧 Improving Accessibility...")
print("=" * 60)

for file_path in html_files:
    changed, changes = improve_accessibility(file_path)
    if changed:
        print(f"\n✓ {file_path}")
        for change in changes:
            print(f"  - {change}")
        total_changes += len(changes)
    else:
        print(f"- {file_path} (no changes needed)")

print("\n" + "=" * 60)
print(f"✅ Accessibility improvements complete! ({total_changes} total changes)")
