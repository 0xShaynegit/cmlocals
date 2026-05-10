#!/usr/bin/env python3
"""
Phase 2 v3: Apply clean template - remove template metadata from head first
"""

import os
import re

TEMPLATE_PATH = "chiang-mai-office/index.html"
TARGET_DIRS = [
    "90-day-reporting",
    "address-change",
    "best-practices",
    "blacklist-status",
    "common-rejections",
    "digital-arrival-card",
    "document-requirements",
    "entry-strategy",
    "financial-requirements",
    "land-border-vs-air",
    "legal-rights",
    "overstay-penalties",
    "queue-strategy",
    "re-entry-permits",
    "tm30-registration",
]

def extract_field(content, pattern):
    """Extract a single field using regex."""
    match = re.search(pattern, content)
    return match.group(0) if match else None

def extract_metadata(page_content):
    """Extract each metadata field explicitly."""
    metadata_parts = []

    patterns = [
        r'<title>.*?</title>',
        r'<meta name="description"[^>]*>',
        r'<link rel="canonical"[^>]*>',
        r'<meta property="og:type"[^>]*>',
        r'<meta property="og:title"[^>]*>',
        r'<meta property="og:description"[^>]*>',
        r'<meta property="twitter:card"[^>]*>',
        r'<meta property="twitter:title"[^>]*>',
        r'<meta property="twitter:description"[^>]*>',
    ]

    for pattern in patterns:
        match = re.search(pattern, page_content)
        if match:
            metadata_parts.append(match.group(0))

    return '\n'.join(metadata_parts)

def extract_article(page_content):
    """Extract article from page-hero to before scripts."""
    hero_match = re.search(r'<section class="page-hero".*?(?=\n<script>)', page_content, re.DOTALL)
    if not hero_match:
        return None
    return hero_match.group(0)

# Load template
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# Validate
if template.count('<style>') != 1 or 'card-fixes.css' in template:
    print("ERROR: Template invalid")
    exit(1)

print("Phase 2 v3: Apply Template with Proper Metadata Replacement")
print("=" * 60 + "\n")

# Extract template head WITHOUT its metadata
# Find the lines from <head> to first <title>
head_start = template.find('<head>')
title_start = template.find('<title>')

# Start from head, take everything up to title
head_opening = template[head_start:title_start]

# Find where metadata ends (just before <style>)
style_start = template.find('<style>')
style_tag_line = template.rfind('\n', 0, style_start) + 1  # Find last newline before <style>

# Everything from style onwards to footer
style_to_footer_start = template[style_start:template.find('<footer')]

footer_start = template.find('<footer class="site-footer"')
footer_section = template[footer_start:]

body_start = template.find('<body>')
hero_start = template.find('<section class="page-hero"')
body_section = template[body_start:hero_start]

total = len(TARGET_DIRS) + 1
done = 0

for dirname in TARGET_DIRS:
    page_file = f"{dirname}/index.html"
    done += 1

    if not os.path.exists(page_file):
        print(f"[{done}/{total}] SKIP: {dirname}")
        continue

    with open(page_file, 'r', encoding='utf-8') as f:
        page_content = f.read()

    # Extract unique fields
    page_metadata = extract_metadata(page_content)
    article = extract_article(page_content)

    if not article or not page_metadata:
        print(f"[{done}/{total}] FAIL: {dirname}")
        continue

    # Build: DOCTYPE + head opening + UNIQUE METADATA + style + body + article + footer
    new_content = "<!DOCTYPE html>\n<html lang=\"en-US\">\n"
    new_content += head_opening
    new_content += page_metadata + "\n\n\n"
    new_content += style_to_footer_start
    new_content += body_section
    new_content += article + "\n"
    new_content += "<script>\n"
    new_content += footer_section

    # Verify
    if new_content.count('<title>') != 1:
        print(f"[{done}/{total}] FAIL: {dirname} (title count mismatch)")
        continue

    if page_metadata not in new_content:
        print(f"[{done}/{total}] FAIL: {dirname} (metadata not in output)")
        continue

    # Write
    with open(page_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[{done}/{total}] OK: {dirname}")

# Main index
page_file = "index.html"
done += 1

if os.path.exists(page_file):
    with open(page_file, 'r', encoding='utf-8') as f:
        page_content = f.read()

    page_metadata = extract_metadata(page_content)
    article = extract_article(page_content)

    if article and page_metadata:
        new_content = "<!DOCTYPE html>\n<html lang=\"en-US\">\n"
        new_content += head_opening
        new_content += page_metadata + "\n\n\n"
        new_content += style_to_footer_start
        new_content += body_section
        new_content += article + "\n"
        new_content += "<script>\n"
        new_content += footer_section

        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[{done}/{total}] OK: main index")
    else:
        print(f"[{done}/{total}] FAIL: main index")

print("\nPhase 2 complete!")
