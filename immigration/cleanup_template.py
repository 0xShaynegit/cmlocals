#!/usr/bin/env python3
"""
Phase 1 cleanup: Remove duplicate style block and clean up chiang-mai-office/index.html template.
"""

import re

file_path = "chiang-mai-office/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("Starting cleanup...")
print(f"Original file size: {len(content)} characters")

# 1. Remove the entire second <style> block (from line 815 to line 1232)
# Pattern: Everything from the opening <style> tag that starts with CANONICAL HEADER
# through to the closing </style> tag
pattern_duplicate_style = r'\n<style>\n/\* ={60}\n   CANONICAL HEADER \+ NAV CSS \(auto-injected.*?</style>'
content = re.sub(pattern_duplicate_style, '', content, flags=re.DOTALL)
print("[DONE] Removed duplicate <style> block")

# 2. Remove the two broken CSS file link references
content = re.sub(r'<link rel="stylesheet" href="/shared/css/card-fixes\.css">\n', '', content)
print("[DONE] Removed card-fixes.css link")
content = re.sub(r'<link rel="stylesheet" href="/shared/css/responsive-images\.css">\n', '', content)
print("[DONE] Removed responsive-images.css link")

# 3. Remove inline style from footer element
content = re.sub(r'<footer class="site-footer" role="contentinfo" style="background: #202A6C;">',
                 '<footer class="site-footer" role="contentinfo">', content)
print("[DONE] Removed inline footer style attribute")

# 4. Verify CSS rule for footer background exists in main style block
if 'background: var(--footer-bg, #202A6C);' not in content:
    print("[WARNING] Footer background CSS rule not found, adding it...")
    # Find the .site-footer rule and ensure it has the correct background
    if '.site-footer {' in content:
        content = content.replace(
            '.site-footer {',
            '.site-footer {\n  background: var(--footer-bg, #202A6C);'
        )

# 5. Remove triple-duplicated /* HEADER */ comment (keep only first occurrence)
pattern_triple_header = r'((/\* HEADER \*/\n)+)'
matches = list(re.finditer(pattern_triple_header, content))
if len(matches) > 0:
    # Find the first occurrence and check if there are duplicates
    first_match = matches[0]
    # Count how many times we have the comment
    header_count = content.count('/* HEADER */')
    if header_count > 1:
        print(f"[INFO] Found {header_count} occurrences of /* HEADER */ comment - keeping first only")
        # Replace multiple consecutive occurrences with single
        content = re.sub(r'(/* HEADER */\n)+', '/* HEADER */\n', content)

print(f"Final file size: {len(content)} characters")
print(f"Size reduction: {len(content) - len(open(file_path).read())} bytes")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n[SUCCESS] Cleanup complete!")
print("Verification:")
print(f"  - Number of <style> tags: {content.count('<style>')}")
print(f"  - Number of </style> tags: {content.count('</style>')}")
print(f"  - 'card-fixes.css' references: {content.count('card-fixes.css')}")
print(f"  - 'responsive-images.css' references: {content.count('responsive-images.css')}")
print(f"  - Footer inline style attributes: {content.count('style=\"background: #202A6C;\"')}")
