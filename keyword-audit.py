#!/usr/bin/env python3
import os
import re
from pathlib import Path

CMLOCALS_ROOT = Path("C:/ZZZWebsites/cmlocals")

# Target keywords by page type
TARGET_KEYWORDS = {
    "dtv": ["DTV visa", "Destination Thailand Visa", "digital nomad visa", "Chiang Mai"],
    "ed": ["ED visa", "education visa", "Chiang Mai", "Thailand"],
    "90-day": ["90-day reporting", "Thailand immigration", "Chiang Mai"],
    "immigration": ["Thailand immigration", "Chiang Mai immigration", "visa extension"],
    "checklist": ["visa checklist", "documentation", "requirements"],
    "guide": ["visa guide", "Thailand", "2026"],
}

def extract_meta_values(html_content):
    """Extract title, description, and H1 from HTML."""
    title = re.search(r'<title>(.*?)</title>', html_content)
    desc = re.search(r'<meta name="description" content="(.*?)"', html_content)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)

    return {
        'title': title.group(1) if title else '',
        'description': desc.group(1) if desc else '',
        'h1': re.sub(r'<[^>]*>', '', h1.group(1)).strip() if h1 else ''
    }

def get_page_category(file_path):
    """Categorize page by its path."""
    path_str = str(file_path).lower()
    if 'dtv' in path_str:
        return 'dtv'
    elif 'ed' in path_str:
        return 'ed'
    elif '90-day' in path_str:
        return '90-day'
    elif 'immigration' in path_str:
        return 'immigration'
    elif 'checklist' in path_str:
        return 'checklist'
    elif 'guide' in path_str:
        return 'guide'
    return None

def keyword_appears(text, keyword):
    """Check if keyword appears in text (case-insensitive)."""
    return keyword.lower() in text.lower()

def score_keyword_optimization(meta, category):
    """Score keyword optimization 0-10."""
    if not category:
        return 0

    keywords = TARGET_KEYWORDS.get(category, [])
    score = 0

    # Title keyword presence (0-3 points)
    for kw in keywords[:2]:
        if keyword_appears(meta['title'], kw):
            score += 1.5

    # H1 keyword presence (0-3 points)
    for kw in keywords[:2]:
        if keyword_appears(meta['h1'], kw):
            score += 1.5

    # Description keyword presence (0-2 points)
    for kw in keywords[:2]:
        if keyword_appears(meta['description'], kw):
            score += 1

    # Location specificity (0-2 points)
    location_kws = ['Chiang Mai', 'Thailand', '2026']
    for loc in location_kws:
        if keyword_appears(meta['title'], loc) or keyword_appears(meta['h1'], loc):
            score += 0.67

    return min(10, score)

# Run audit
results = []
all_files = list(CMLOCALS_ROOT.glob("**/*.html"))

for file_path in all_files:
    if file_path.name != "index.html" or "docs/" in str(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = extract_meta_values(content)
    category = get_page_category(file_path)
    score = score_keyword_optimization(meta, category)

    if score < 8:  # Flag pages with suboptimal keyword targeting
        rel_path = str(file_path.relative_to(CMLOCALS_ROOT))
        results.append({
            'path': rel_path,
            'category': category,
            'score': score,
            'title': meta['title'][:60],
            'h1': meta['h1'][:60],
            'missing_keywords': TARGET_KEYWORDS.get(category, [])
        })

# Sort by score
results.sort(key=lambda x: x['score'])

# Report
print("=" * 80)
print("KEYWORD OPTIMIZATION AUDIT - CMLocals")
print("=" * 80)
print()

print(f"Pages with suboptimal keyword targeting (<8/10): {len(results)}")
print()

for i, page in enumerate(results[:30], 1):
    print(f"{i}. {page['path']}")
    print(f"   Score: {page['score']:.1f}/10 | Category: {page['category']}")
    print(f"   Title: {page['title']}")
    print(f"   H1: {page['h1']}")
    print(f"   Missing: {', '.join(page['missing_keywords'][:2])}")
    print()

# High-priority recommendations
print("=" * 80)
print("HIGH-PRIORITY OPTIMIZATIONS (Top 15 pages)")
print("=" * 80)
print()

for page in results[:15]:
    category = page['category']
    path = page['path'].replace("\\", "/").replace("/index.html", "").replace("cmlocals/", "")

    print(f"FIX: /{path}")
    print(f"Current Title: {page['title']}")

    if category == 'dtv':
        print(f"Suggested: 'DTV Visa Chiang Mai 2026: Financial Requirements & Application Guide'")
    elif category == 'ed':
        print(f"Suggested: 'ED Visa Chiang Mai: Schools, Costs & Eligibility 2026'")
    elif category == 'guide':
        print(f"Suggested: Add 'Chiang Mai' and '2026' to title if applicable")
    elif category == 'checklist':
        print(f"Suggested: Add 'checklist' and 'documents needed' explicitly")

    print()

print(f"\nTotal audit coverage: {len(list(CMLOCALS_ROOT.glob('**/*.html')))} pages")
print("Target: 90% of pages scoring 8+/10 on keyword optimization")
