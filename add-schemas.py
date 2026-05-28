#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Base paths
CMLOCALS_ROOT = Path("C:/ZZZWebsites/cmlocals")

def get_url_from_path(file_path):
    """Convert file path to URL."""
    relative = file_path.relative_to(CMLOCALS_ROOT)
    if str(relative) == "index.html":
        return "https://www.cmlocals.com/"
    parts = str(relative).replace("\\", "/").replace("/index.html", "").split("/")
    return f"https://www.cmlocals.com/{'/'.join(parts)}/"

def get_breadcrumb_schema(url):
    """Generate BreadcrumbList schema."""
    parts = url.replace("https://www.cmlocals.com/", "").strip("/").split("/")
    if not parts[0]:
        return None

    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.cmlocals.com/"}]
    path = "https://www.cmlocals.com"

    for i, part in enumerate(parts):
        if not part:
            continue
        path += f"/{part}"
        items.append({
            "@type": "ListItem",
            "position": i + 2,
            "name": part.replace("-", " ").title(),
            "item": path + "/" if i == len(parts) - 1 else path
        })

    if len(items) == 1:
        return None

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }
    return schema

def get_faq_schema(title, file_content):
    """Generate FAQ schema for checklist pages."""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"What documents are required for {title}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Check the complete requirements on this page for all required documents and supporting materials."
                }
            },
            {
                "@type": "Question",
                "name": f"How do I complete the {title} process?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Follow the step-by-step checklist on this page to ensure you have everything needed."
                }
            }
        ]
    }
    return schema

def get_article_schema(title, url):
    """Generate Article schema for guide pages."""
    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": title,
        "url": url,
        "datePublished": "2026-05-01",
        "dateModified": "2026-05-16",
        "author": {
            "@type": "Person",
            "name": "CMLocals Visa Specialist"
        },
        "publisher": {
            "@type": "Organization",
            "name": "CMLocals",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.cmlocals.com/logo.png"
            }
        },
        "description": "Comprehensive guide to Thailand visa options and immigration procedures."
    }
    return schema

def get_localbusiness_schema():
    """Generate LocalBusiness schema for immigration office."""
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Chiang Mai Immigration Office",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "71 M.3 Airport Road",
            "addressLocality": "Chiang Mai",
            "addressRegion": "Chiang Mai",
            "postalCode": "50200",
            "addressCountry": "TH"
        },
        "telephone": "+66-53-211-300",
        "url": "https://www.cmlocals.com/immigration/chiang-mai-office/",
        "priceRange": "Free",
        "areaServed": "Thailand",
        "description": "Official immigration office serving Chiang Mai province with visa extensions, re-entry permits, and address changes."
    }
    return schema

def insert_schema(file_path, schema, schema_type):
    """Insert schema before </head> tag. Allows multiple schemas."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if this specific schema type already exists
    search_str = f'"@type": "{schema_type}"'
    if search_str in content:
        return False

    schema_str = f'<script type="application/ld+json">\n{to_json(schema)}\n</script>\n\n'

    # Insert before </head>
    head_close = content.find('</head>')
    if head_close == -1:
        return False

    new_content = content[:head_close] + schema_str + content[head_close:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def to_json(obj):
    """Convert to JSON string."""
    import json
    return json.dumps(obj, indent=2)

def get_title_from_html(file_content):
    """Extract title from HTML."""
    match = re.search(r'<title>(.*?)</title>', file_content)
    if match:
        return match.group(1).replace(" - CMLocals", "").strip()
    return "Page"

# Process files
checklist_files = list(CMLOCALS_ROOT.glob("checklists/*/index.html"))
guide_files = list(CMLOCALS_ROOT.glob("guides/*/index.html"))
immigration_office = CMLOCALS_ROOT / "immigration" / "chiang-mai-office" / "index.html"

print(f"Found {len(checklist_files)} checklist pages")
print(f"Found {len(guide_files)} guide pages")
print(f"Immigration office: {immigration_office.exists()}")

# Process all pages for BreadcrumbList
all_html_files = list(CMLOCALS_ROOT.glob("**/*.html"))
breadcrumb_count = 0

for file_path in all_html_files:
    if file_path.name != "index.html":
        continue
    if "docs/" in str(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    url = get_url_from_path(file_path)
    schema = get_breadcrumb_schema(url)

    if schema and insert_schema(file_path, schema, "BreadcrumbList"):
        breadcrumb_count += 1

print(f"Added BreadcrumbList to {breadcrumb_count} pages")

# Process checklist pages for FAQ
faq_count = 0
for file_path in checklist_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title = get_title_from_html(content)
    schema = get_faq_schema(title, content)

    if insert_schema(file_path, schema, "FAQPage"):
        faq_count += 1

print(f"Added FAQ schema to {faq_count} checklist pages")

# Process guide pages for Article
article_count = 0
for file_path in guide_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    url = get_url_from_path(file_path)
    title = get_title_from_html(content)
    schema = get_article_schema(title, url)

    if insert_schema(file_path, schema, "NewsArticle"):
        article_count += 1

print(f"Added Article schema to {article_count} guide pages")

# Process immigration office page
if immigration_office.exists():
    with open(immigration_office, 'r', encoding='utf-8') as f:
        content = f.read()

    schema = get_localbusiness_schema()
    if insert_schema(immigration_office, schema, "LocalBusiness"):
        print("Added LocalBusiness schema to immigration office page")

print("\nSchema addition complete!")
