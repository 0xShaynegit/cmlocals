"""Rebuild search-index.json from the site's HTML.

Run from anywhere:  python _scripts/build-search-index.py   (CMLocals: python scripts/build-search-index.py)

One entry per indexable page: title, description, url, words.
words = unique lowercase tokens of 3+ characters from <main> only (nav and footer are left out,
otherwise every page would match every menu label). Hyphenated terms also get a joined form,
so "e-gates" is findable as "egates".
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMLOCALS = os.path.basename(ROOT).lower() == 'cmlocals'
SKIP_DIRS = {'node_modules', '_archive', '.git', '.md', '.ua', '.github', 'chatbot', 'functions', 'shared',
             'css', 'js', 'fonts', 'images', 'templates', '_scripts', 'scripts', 'wp-content'}
SKIP_FILES = {'404.html', 'search.html', 'blog-template.html', 'page-template.html', 'template.html'}


# Common misspellings people type: a page containing the key is also found by the value.
ALIASES = {'smoky': 'smokey'}


def url_for(rel):
    if not CMLOCALS:
        return rel
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-len('index.html')]
    return '/' + rel


def clean(text):
    return re.sub(r'\s+', ' ', html.unescape(text)).strip()


def words_from(main_html):
    body = re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>', ' ', main_html)
    body = re.sub(r'(?s)<!--.*?-->', ' ', body)
    body = re.sub(r'(?is)<(header|nav|footer)\b.*?</\1>', ' ', body)
    body = re.sub(r'(?is)<details class="nav-accordion">.*?</details>', ' ', body)
    text = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', body)).lower()
    words = set(re.findall(r'[a-z0-9]{3,}', text))
    for tok in re.findall(r'[a-z0-9]+(?:-[a-z0-9]+)+', text):
        words.add(tok)
        words.add(tok.replace('-', ''))
    for word, alias in ALIASES.items():
        if word in words:
            words.add(alias)
    return sorted(w for w in words if len(w) >= 3)


entries = []
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for name in files:
        if not name.endswith('.html') or name in SKIP_FILES:
            continue
        path = os.path.join(dirpath, name)
        rel = os.path.relpath(path, ROOT).replace('\\', '/')
        src = open(path, encoding='utf-8', errors='replace').read()
        if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', src, re.I):
            continue
        t = re.search(r'(?is)<title>(.*?)</title>', src)
        d = re.search(r'(?is)<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', src)
        m = re.search(r'(?is)<main\b.*?</main>', src)
        entries.append({
            'title': clean(t.group(1)) if t else rel,
            'description': clean(d.group(1)) if d else '',
            'url': url_for(rel),
            'words': words_from(m.group(0) if m else src),
        })

entries.sort(key=lambda e: (e['url'].count('/'), e['url']))
out = os.path.join(ROOT, 'search-index.json')
with open(out, 'w', encoding='utf-8', newline='') as f:
    json.dump(entries, f, ensure_ascii=False, separators=(',', ':'))
print(f'{len(entries)} pages, {os.path.getsize(out) // 1024} KB -> {out}')
