#!/bin/bash

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

echo "Process: Get file → Backup → Copy template → Extract content from backup → Paste into template"
echo ""

total=$((${#TARGET_DIRS[@]} + 1))
done=0

for dir in "${TARGET_DIRS[@]}"; do
    PAGE="$dir/index.html"
    BACKUP="$dir/index.html.backup"
    done=$((done + 1))

    if [ ! -f "$PAGE" ]; then
        echo "[$done/$total] SKIP: $dir (file not found)"
        continue
    fi

    # Step 1: Make backup of original
    cp "$PAGE" "$BACKUP"

    # Step 2: Copy template over the file
    cp "$TEMPLATE" "$PAGE"

    # Step 3: Extract content section from backup (page-hero to before footer)
    BACKUP_START=$(grep -n '<section class="page-hero"' "$BACKUP" | cut -d: -f1)
    BACKUP_END=$(grep -n '<footer class="site-footer"' "$BACKUP" | cut -d: -f1)
    BACKUP_END=$((BACKUP_END - 1))

    # Step 4: Find where to insert in template
    TEMPLATE_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
    TEMPLATE_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
    TEMPLATE_END=$((TEMPLATE_END - 1))

    if [ -z "$BACKUP_START" ] || [ -z "$TEMPLATE_START" ]; then
        echo "[$done/$total] FAIL: $dir (boundaries not found)"
        rm "$BACKUP"
        git checkout "$PAGE"
        continue
    fi

    # Step 5: Extract backup content
    BACKUP_CONTENT=$(sed -n "${BACKUP_START},${BACKUP_END}p" "$BACKUP")

    # Step 6: Replace in template
    NEW_FILE=$(
        sed -n "1,$((TEMPLATE_START - 1))p" "$PAGE"
        echo "$BACKUP_CONTENT"
        sed -n "$((TEMPLATE_END + 1)),\$p" "$PAGE"
    )

    echo "$NEW_FILE" > "$PAGE"

    echo "[$done/$total] OK: $dir"
    rm "$BACKUP"
done

# Main index
PAGE="index.html"
BACKUP="index.html.backup"
done=$((done + 1))

if [ -f "$PAGE" ]; then
    cp "$PAGE" "$BACKUP"
    cp "$TEMPLATE" "$PAGE"

    BACKUP_START=$(grep -n '<section class="page-hero"' "$BACKUP" | cut -d: -f1)
    BACKUP_END=$(grep -n '<footer class="site-footer"' "$BACKUP" | cut -d: -f1)
    BACKUP_END=$((BACKUP_END - 1))

    TEMPLATE_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
    TEMPLATE_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
    TEMPLATE_END=$((TEMPLATE_END - 1))

    if [ -n "$BACKUP_START" ] && [ -n "$TEMPLATE_START" ]; then
        BACKUP_CONTENT=$(sed -n "${BACKUP_START},${BACKUP_END}p" "$BACKUP")

        NEW_FILE=$(
            sed -n "1,$((TEMPLATE_START - 1))p" "$PAGE"
            echo "$BACKUP_CONTENT"
            sed -n "$((TEMPLATE_END + 1)),\$p" "$PAGE"
        )

        echo "$NEW_FILE" > "$PAGE"
        echo "[$done/$total] OK: main index"
    fi

    rm "$BACKUP"
fi

echo ""
echo "Complete!"
