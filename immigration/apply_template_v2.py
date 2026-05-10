#!/usr/bin/env python3
"""
Phase 2 v2: Apply clean template - explicit metadata field extraction
"""

import os
import re
from pathlib import Path

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
    """Extract a single field from HTML content using regex."""
    match = re.search(pattern, content)
    return match.group(0) if match else None

def extract_metadata(page_content):
    """Explicitly extract each metadata field."""
    metadata_parts = []

    # Title
    title = extract_field(page_content, r'<title>.*?</title>')
    if title:
        metadata_parts.append(title)

    # Meta description
    meta_desc = extract_field(page_content, r'<meta name="description"[^>]*>')
    if meta_desc:
        metadata_parts.append(meta_desc)

    # Canonical
    canonical = extract_field(page_content, r'<link rel="canonical"[^>]*>')
    if canonical:
        metadata_parts.append(canonical)

    # OG type
    og_type = extract_field(page_content, r'<meta property="og:type"[^>]*>')
    if og_type:
        metadata_parts.append(og_type)

    # OG title
    og_title = extract_field(page_content, r'<meta property="og:title"[^>]*>')
    if og_title:
        metadata_parts.append(og_title)

    # OG description
    og_desc = extract_field(page_content, r'<meta property="og:description"[^>]*>')
    if og_desc:
        metadata_parts.append(og_desc)

    # Twitter card
    tw_card = extract_field(page_content, r'<meta property="twitter:card"[^>]*>')
    if tw_card:
        metadata_parts.append(tw_card)

    # Twitter title
    tw_title = extract_field(page_content, r'<meta property="twitter:title"[^>]*>')
    if tw_title:
        metadata_parts.append(tw_title)

    # Twitter description
    tw_desc = extract_field(page_content, r'<meta property="twitter:description"[^>]*>')
    if tw_desc:
        metadata_parts.append(tw_desc)

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

# Validate template
if template.count('<style>') != 1 or 'card-fixes.css' in template:
    print("ERROR: Template invalid")
    exit(1)

print("Phase 2 v2: Apply Template with Metadata Preservation")
print("=" * 60 + "\n")

# Split template into sections
head_end = template.find('</head>')
head_with_placeholder_meta = template[:head_end]

body_start = template.find('<body>')
hero_start = template.find('<section class="page-hero"')
body_section = template[body_start:hero_start]

footer_start = template.find('<footer class="site-footer"')
footer_section = template[footer_start:]

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

    if not article:
        print(f"[{done}/{total}] FAIL: {dirname} - no article found")
        continue

    if not page_metadata:
        print(f"[{done}/{total}] FAIL: {dirname} - no metadata found")
        continue

    # Build new file: head + metadata + </head> + body + article + footer
    new_content = head_with_placeholder_meta
    new_content += '\n' + page_metadata + '\n'
    new_content += '</head>\n'
    new_content += body_section
    new_content += article + '\n'
    new_content += '<script>\n'  # Closing placeholder
    new_content += footer_section

    # Quick validation
    if '<title>' not in page_metadata:
        print(f"[{done}/{total}] FAIL: {dirname} - title not extracted")
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
        new_content = head_with_placeholder_meta
        new_content += '\n' + page_metadata + '\n'
        new_content += '</head>\n'
        new_content += body_section
        new_content += article + '\n'
        new_content += '<script>\n'
        new_content += footer_section

        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[{done}/{total}] OK: main index")
    else:
        print(f"[{done}/{total}] FAIL: main index")

print("\nDone!")
