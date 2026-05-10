#!/usr/bin/env python3
"""
Phase 2: Apply clean template to all immigration pages with metadata preservation.
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

def validate_template(template):
    """Ensure template is clean."""
    style_count = template.count('<style>')
    if style_count != 1:
        raise ValueError(f"Template has {style_count} <style> tags, expected 1")

    if 'card-fixes.css' in template or 'responsive-images.css' in template:
        raise ValueError("Template still has broken CSS links")

    return True

def extract_metadata_from_page(page_content):
    """Extract unique metadata tags from a page."""
    lines = page_content.split('\n')
    metadata = []

    for i, line in enumerate(lines[5:15]):  # Typically lines 6-14 have metadata
        if any(tag in line for tag in ['<title>', '<meta name="description"',
                                        'rel="canonical"', 'property="og:',
                                        'property="twitter:']):
            metadata.append(line)

    return '\n'.join(metadata)

def extract_article_content(page_content):
    """Extract the article/content section from page-hero to before scripts."""
    # Find page-hero section
    hero_start = page_content.find('<section class="page-hero"')
    if hero_start == -1:
        raise ValueError("No page-hero section found")

    # Find the first <script> tag after hero (which comes before footer)
    script_start = page_content.find('<script>', hero_start)
    if script_start == -1:
        raise ValueError("No script tag found after hero")

    # Extract everything from hero to just before script
    article = page_content[hero_start:script_start].rstrip()

    return article

def extract_template_sections(template):
    """Extract and return template sections."""
    # Extract head section (up to and including </head>)
    head_end = template.find('</head>')
    if head_end == -1:
        raise ValueError("No </head> found in template")

    head_section = template[:head_end]

    # Extract body start (from <body> to just before page-hero)
    body_start_idx = template.find('<body>')
    hero_idx = template.find('<section class="page-hero"')
    body_start = template[body_start_idx:hero_idx]

    # Extract footer and closing (from footer to end)
    footer_start = template.find('<footer class="site-footer"')
    footer_section = template[footer_start:]

    return head_section, body_start, footer_section

def apply_template_to_page(page_path, template, head_section, body_start, footer_section):
    """Apply template to a single page."""
    with open(page_path, 'r', encoding='utf-8') as f:
        page_content = f.read()

    # Extract unique metadata and article
    metadata = extract_metadata_from_page(page_content)
    article = extract_article_content(page_content)

    # Build new file
    new_content = head_section
    new_content += '\n' + metadata + '\n'
    new_content += '\n</head>\n'
    new_content += body_start
    new_content += article
    new_content += '\n<script>'  # Closing script tag placeholder
    new_content += '\n' + footer_section

    # Validate
    if new_content.count('<style>') != 1:
        raise ValueError(f"Output has {new_content.count('<style>')} <style> tags")
    if new_content.count('</style>') != 1:
        raise ValueError(f"Output has {new_content.count('</style>')} </style> tags")
    if '</body>' not in new_content or '</html>' not in new_content:
        raise ValueError("Missing closing tags")
    if '<footer class="site-footer"' not in new_content:
        raise ValueError("Footer missing")

    # Check metadata was preserved
    if metadata and metadata not in new_content:
        raise ValueError("Metadata not preserved in output")

    # Write file
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

# Main execution
print("Phase 2: Apply Clean Template to All Pages")
print("==========================================\n")

# Load and validate template
print("Loading template...")
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

validate_template(template)
print("Template validation: PASS\n")

# Extract template sections
head_section, body_start, footer_section = extract_template_sections(template)

# Process each target directory
total = len(TARGET_DIRS) + 1
processed = 0

for dirname in TARGET_DIRS:
    page_file = f"{dirname}/index.html"
    processed += 1

    if not os.path.exists(page_file):
        print(f"[{processed}/{total}] SKIP: {dirname} (file not found)")
        continue

    try:
        apply_template_to_page(page_file, template, head_section, body_start, footer_section)
        print(f"[{processed}/{total}] OK: {dirname}")
    except Exception as e:
        print(f"[{processed}/{total}] FAIL: {dirname} - {str(e)}")

# Process main index.html
page_file = "index.html"
processed += 1

if os.path.exists(page_file):
    try:
        apply_template_to_page(page_file, template, head_section, body_start, footer_section)
        print(f"[{processed}/{total}] OK: main index")
    except Exception as e:
        print(f"[{processed}/{total}] FAIL: main index - {str(e)}")

print("\nPhase 2 complete.")
