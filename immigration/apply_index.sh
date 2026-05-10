#!/bin/bash

TEMPLATE="chiang-mai-office/index.html"
PAGE="index.html"
BACKUP="index.backup.html"

# Backup current
cp "$PAGE" "$BACKUP"

# Extract metadata (lines 6-17 from backup - unique per page)
META_START=$(sed -n '6p' "$BACKUP" | head -c 1)
if [ "$META_START" = "<" ]; then
  META_END_LINE=$(grep -n "^<style>" "$BACKUP" | head -1 | cut -d: -f1)
  META_END_LINE=$((META_END_LINE - 1))
  META=$(sed -n "6,${META_END_LINE}p" "$BACKUP")
else
  META=$(sed -n "6,17p" "$BACKUP")
fi

# Extract content area (page-hero to before footer scripts - the white section)
CONTENT_START=$(grep -n '<section class="page-hero"' "$BACKUP" | head -1 | cut -d: -f1)
CONTENT_END=$(grep -n '^<script>' "$BACKUP" | head -1 | cut -d: -f1)
CONTENT_END=$((CONTENT_END - 1))

if [ -z "$CONTENT_START" ] || [ -z "$CONTENT_END" ]; then
  echo "ERROR: Could not find content boundaries"
  exit 1
fi

CONTENT=$(sed -n "${CONTENT_START},${CONTENT_END}p" "$BACKUP")

# Build new file: template head + unique metadata + template nav + unique content + template footer
{
  # Template lines 1-5 (DOCTYPE through viewport)
  sed -n "1,5p" "$TEMPLATE"
  
  # UNIQUE METADATA from backup
  echo "$META"
  
  # Template lines through to body opening (everything in head and header/nav)
  BODY_START=$(grep -n "^<body>" "$TEMPLATE" | head -1 | cut -d: -f1)
  sed -n "18,$((BODY_START - 1))p" "$TEMPLATE"
  
  echo "<body>"
  
  # Skip template's header through to after nav (find where main content starts in template)
  MAIN_START=$(grep -n '<main id="main-content">' "$TEMPLATE" | head -1 | cut -d: -f1)
  sed -n "$((BODY_START + 1)),$((MAIN_START - 1))p" "$TEMPLATE"
  
  echo '<main id="main-content">'
  
  # UNIQUE CONTENT from backup (page-hero through before scripts)
  echo "$CONTENT"
  echo ""
  echo "</main>"
  
  # Template footer and closing
  FOOTER_START=$(grep -n '^<script>' "$TEMPLATE" | head -1 | cut -d: -f1)
  sed -n "${FOOTER_START},$p" "$TEMPLATE"
  
} > "$PAGE"

echo "OK: index.html rebuilt with template structure and immigration card content"
