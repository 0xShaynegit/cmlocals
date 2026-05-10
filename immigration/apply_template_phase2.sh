#!/bin/bash

# Phase 2: Apply clean template to all 15 immigration pages
# Template source: chiang-mai-office/index.html
# Target pages: 15 subdirectories + main index.html

set -e

TEMPLATE_DIR="chiang-mai-office"
TEMPLATE_FILE="$TEMPLATE_DIR/index.html"
TARGET_DIRS=(
    "90-day-reporting"
    "address-change"
    "best-practices"
    "blacklist-status"
    "common-rejections"
    "digital-arrival-card"
    "document-requirements"
    "entry-strategy"
    "financial-requirements"
    "land-border-vs-air"
    "legal-rights"
    "overstay-penalties"
    "queue-strategy"
    "re-entry-permits"
    "tm30-registration"
)

# Verify template exists and is clean
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "ERROR: Template not found at $TEMPLATE_FILE"
    exit 1
fi

STYLE_COUNT=$(grep -c "<style>" "$TEMPLATE_FILE")
if [ "$STYLE_COUNT" -ne 1 ]; then
    echo "ERROR: Template has $STYLE_COUNT <style> tags, expected 1"
    exit 1
fi

BROKEN_LINKS=$(grep -c "card-fixes.css\|responsive-images.css" "$TEMPLATE_FILE" || true)
if [ "$BROKEN_LINKS" -gt 0 ]; then
    echo "ERROR: Template still has broken CSS links"
    exit 1
fi

echo "Template validation: PASS"
echo ""

# Extract template sections
# Section 1: Everything from start to end of head (line 1 to </head>)
HEAD_SECTION=$(sed -n '1,/<\/head>/p' "$TEMPLATE_FILE")

# Section 2: Everything after head opening tag through footer (header + nav + article placeholder area)
# This is from <body> to just before the article content
BODY_START=$(sed -n '/<body>/,/<section class="page-hero"/p' "$TEMPLATE_FILE" | head -n -1)

# Section 3: Footer and closing
FOOTER_SECTION=$(sed -n '/<footer class="site-footer"/,/<\/html>/p' "$TEMPLATE_FILE")

TOTAL_TARGETS=$((${#TARGET_DIRS[@]} + 1))
PROCESSED=0

# Process each target directory
for dir in "${TARGET_DIRS[@]}"; do
    PAGE_FILE="$dir/index.html"
    PROCESSED=$((PROCESSED + 1))

    if [ ! -f "$PAGE_FILE" ]; then
        echo "[$PROCESSED/$TOTAL_TARGETS] SKIP: $dir (file not found)"
        continue
    fi

    # Extract meta tags from current file (lines 6-14, but handle variations)
    # Look for title, meta description, canonical, og tags, twitter tags
    META_TAGS=$(sed -n '/<title>/,/<\/title>/p' "$PAGE_FILE"; \
                sed -n '/name="description"/p' "$PAGE_FILE"; \
                sed -n '/rel="canonical"/p' "$PAGE_FILE"; \
                sed -n '/property="og:/p' "$PAGE_FILE"; \
                sed -n '/property="twitter:/p' "$PAGE_FILE")

    # Extract article content (from page-hero to just before first script tag after article)
    ARTICLE_CONTENT=$(sed -n '/<section class="page-hero"/,/<script>/p' "$PAGE_FILE" | head -n -1)

    # Verify we got content
    if [ -z "$ARTICLE_CONTENT" ]; then
        echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: $dir (no article content found)"
        continue
    fi

    # Build new file
    NEW_FILE="$HEAD_SECTION"
    NEW_FILE="$NEW_FILE"$'\n'"$META_TAGS"
    NEW_FILE="$NEW_FILE"$'\n'"</head>"
    NEW_FILE="$NEW_FILE"$'\n'"$BODY_START"
    NEW_FILE="$NEW_FILE"$'\n'"$ARTICLE_CONTENT"
    NEW_FILE="$NEW_FILE"$'\n'"<script>"
    NEW_FILE="$NEW_FILE"$'\n'"$FOOTER_SECTION"

    # Validation
    if ! echo "$NEW_FILE" | grep -q "</body>"; then
        echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: $dir (missing </body>)"
        continue
    fi

    if ! echo "$NEW_FILE" | grep -q "</html>"; then
        echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: $dir (missing </html>)"
        continue
    fi

    if ! echo "$NEW_FILE" | grep -q "<footer class=\"site-footer\""; then
        echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: $dir (missing footer)"
        continue
    fi

    # Write file (UTF-8)
    echo -n "$NEW_FILE" > "$PAGE_FILE"

    echo "[$PROCESSED/$TOTAL_TARGETS] OK: $dir"
done

# Process main index.html
PAGE_FILE="index.html"
PROCESSED=$((PROCESSED + 1))

if [ -f "$PAGE_FILE" ]; then
    META_TAGS=$(sed -n '/<title>/,/<\/title>/p' "$PAGE_FILE"; \
                sed -n '/name="description"/p' "$PAGE_FILE"; \
                sed -n '/rel="canonical"/p' "$PAGE_FILE"; \
                sed -n '/property="og:/p' "$PAGE_FILE"; \
                sed -n '/property="twitter:/p' "$PAGE_FILE")

    ARTICLE_CONTENT=$(sed -n '/<section class="page-hero"/,/<script>/p' "$PAGE_FILE" | head -n -1)

    if [ -n "$ARTICLE_CONTENT" ]; then
        NEW_FILE="$HEAD_SECTION"
        NEW_FILE="$NEW_FILE"$'\n'"$META_TAGS"
        NEW_FILE="$NEW_FILE"$'\n'"</head>"
        NEW_FILE="$NEW_FILE"$'\n'"$BODY_START"
        NEW_FILE="$NEW_FILE"$'\n'"$ARTICLE_CONTENT"
        NEW_FILE="$NEW_FILE"$'\n'"<script>"
        NEW_FILE="$NEW_FILE"$'\n'"$FOOTER_SECTION"

        if echo "$NEW_FILE" | grep -q "</body>" && echo "$NEW_FILE" | grep -q "</html>" && echo "$NEW_FILE" | grep -q "<footer class=\"site-footer\""; then
            echo -n "$NEW_FILE" > "$PAGE_FILE"
            echo "[$PROCESSED/$TOTAL_TARGETS] OK: main index"
        else
            echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: main index (validation failed)"
        fi
    else
        echo "[$PROCESSED/$TOTAL_TARGETS] FAIL: main index (no article content)"
    fi
fi

echo ""
echo "Phase 2 complete. All pages updated with clean template."
