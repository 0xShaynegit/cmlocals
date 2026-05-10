#!/bin/bash

# Simple: Extract white content area from each page and insert into template

TEMPLATE="chiang-mai-office/index.html"

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

# Get the white content area from template (page-hero to footer)
TEMPLATE_CONTENT_START=$(grep -n '<section class="page-hero"' "$TEMPLATE" | cut -d: -f1)
TEMPLATE_CONTENT_END=$(grep -n '<footer class="site-footer"' "$TEMPLATE" | cut -d: -f1)
TEMPLATE_CONTENT_END=$((TEMPLATE_CONTENT_END - 1))

echo "Template content: lines $TEMPLATE_CONTENT_START to $TEMPLATE_CONTENT_END"
echo ""

total=$((${#TARGET_DIRS[@]} + 1))
done=0

for dir in "${TARGET_DIRS[@]}"; do
    PAGE="$dir/index.html"
    done=$((done + 1))

    if [ ! -f "$PAGE" ]; then
        echo "[$done/$total] SKIP: $dir"
        continue
    fi

    # Get line numbers for this page's content
    PAGE_CONTENT_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
    PAGE_CONTENT_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
    PAGE_CONTENT_END=$((PAGE_CONTENT_END - 1))

    if [ -z "$PAGE_CONTENT_START" ] || [ -z "$PAGE_CONTENT_END" ]; then
        echo "[$done/$total] FAIL: $dir (content boundaries not found)"
        continue
    fi

    # Extract the white content area from this page
    PAGE_CONTENT=$(sed -n "${PAGE_CONTENT_START},${PAGE_CONTENT_END}p" "$PAGE")

    # Build new file:
    # 1. Template lines 1 to TEMPLATE_CONTENT_START - 1
    # 2. PAGE_CONTENT
    # 3. Template lines TEMPLATE_CONTENT_END + 1 to end

    NEW_FILE=$(
        sed -n "1,$((TEMPLATE_CONTENT_START - 1))p" "$TEMPLATE"
        echo "$PAGE_CONTENT"
        sed -n "$((TEMPLATE_CONTENT_END + 1)),\$p" "$TEMPLATE"
    )

    # Write
    echo "$NEW_FILE" > "$PAGE"

    echo "[$done/$total] OK: $dir"
done

# Main index
PAGE="index.html"
done=$((done + 1))

PAGE_CONTENT_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
PAGE_CONTENT_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
PAGE_CONTENT_END=$((PAGE_CONTENT_END - 1))

if [ -n "$PAGE_CONTENT_START" ] && [ -n "$PAGE_CONTENT_END" ]; then
    PAGE_CONTENT=$(sed -n "${PAGE_CONTENT_START},${PAGE_CONTENT_END}p" "$PAGE")

    NEW_FILE=$(
        sed -n "1,$((TEMPLATE_CONTENT_START - 1))p" "$TEMPLATE"
        echo "$PAGE_CONTENT"
        sed -n "$((TEMPLATE_CONTENT_END + 1)),\$p" "$TEMPLATE"
    )

    echo "$NEW_FILE" > "$PAGE"
    echo "[$done/$total] OK: main index"
fi

echo ""
echo "Done!"
