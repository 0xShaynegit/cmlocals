#!/bin/bash

TEMPLATE="chiang-mai-office/index.html"

TARGET_DIRS=(
    "90-day-reporting" "address-change" "best-practices" "blacklist-status"
    "common-rejections" "digital-arrival-card" "document-requirements"
    "entry-strategy" "financial-requirements" "land-border-vs-air"
    "legal-rights" "overstay-penalties" "queue-strategy"
    "re-entry-permits" "tm30-registration"
)

echo "Workflow: Backup → Extract metadata + content → Copy template → Restore metadata + content"
echo ""

total=$((${#TARGET_DIRS[@]} + 1))
done=0

for dir in "${TARGET_DIRS[@]}"; do
    PAGE="$dir/index.html"
    BACKUP="$dir/index.html.backup"
    done=$((done + 1))

    [ ! -f "$PAGE" ] && echo "[$done/$total] SKIP: $dir" && continue

    # Step 1: Backup original
    cp "$PAGE" "$BACKUP"

    # Step 2: Extract metadata from backup (lines 6-14: title through last meta tag)
    BACKUP_META=$(sed -n '6,14p' "$BACKUP")

    # Step 3: Extract content from backup
    BACKUP_CONTENT_START=$(grep -n '<section class="page-hero"' "$BACKUP" | cut -d: -f1)
    BACKUP_CONTENT_END=$(grep -n '<footer class="site-footer"' "$BACKUP" | cut -d: -f1)
    BACKUP_CONTENT_END=$((BACKUP_CONTENT_END - 1))

    BACKUP_CONTENT=$(sed -n "${BACKUP_CONTENT_START},${BACKUP_CONTENT_END}p" "$BACKUP")

    # Step 4: Copy template
    cp "$TEMPLATE" "$PAGE"

    # Step 5: Find template sections to replace
    TEMPLATE_META_END=14
    TEMPLATE_CONTENT_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
    TEMPLATE_CONTENT_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
    TEMPLATE_CONTENT_END=$((TEMPLATE_CONTENT_END - 1))

    if [ -z "$BACKUP_CONTENT_START" ] || [ -z "$TEMPLATE_CONTENT_START" ]; then
        echo "[$done/$total] FAIL: $dir"
        rm "$BACKUP"
        git checkout "$PAGE" 2>/dev/null
        continue
    fi

    # Step 6: Build final file with backup metadata + content
    NEW_FILE=$(
        sed -n "1,5p" "$PAGE"  # DOCTYPE through viewport
        echo "$BACKUP_META"     # Backup metadata
        sed -n "15,$((TEMPLATE_CONTENT_START - 1))p" "$PAGE"  # Style and header
        echo "$BACKUP_CONTENT"  # Backup content
        sed -n "$((TEMPLATE_CONTENT_END + 1)),\$p" "$PAGE"  # Footer onwards
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
    BACKUP_META=$(sed -n '6,14p' "$BACKUP")
    BACKUP_CONTENT_START=$(grep -n '<section class="page-hero"' "$BACKUP" | cut -d: -f1)
    BACKUP_CONTENT_END=$(grep -n '<footer class="site-footer"' "$BACKUP" | cut -d: -f1)
    [ -n "$BACKUP_CONTENT_START" ] && BACKUP_CONTENT_END=$((BACKUP_CONTENT_END - 1))

    cp "$TEMPLATE" "$PAGE"

    TEMPLATE_CONTENT_START=$(grep -n '<section class="page-hero"' "$PAGE" | cut -d: -f1)
    TEMPLATE_CONTENT_END=$(grep -n '<footer class="site-footer"' "$PAGE" | cut -d: -f1)
    [ -n "$TEMPLATE_CONTENT_END" ] && TEMPLATE_CONTENT_END=$((TEMPLATE_CONTENT_END - 1))

    if [ -n "$BACKUP_CONTENT_START" ] && [ -n "$TEMPLATE_CONTENT_START" ]; then
        BACKUP_CONTENT=$(sed -n "${BACKUP_CONTENT_START},${BACKUP_CONTENT_END}p" "$BACKUP")

        NEW_FILE=$(
            sed -n "1,5p" "$PAGE"
            echo "$BACKUP_META"
            sed -n "15,$((TEMPLATE_CONTENT_START - 1))p" "$PAGE"
            echo "$BACKUP_CONTENT"
            sed -n "$((TEMPLATE_CONTENT_END + 1)),\$p" "$PAGE"
        )

        echo "$NEW_FILE" > "$PAGE"
        echo "[$done/$total] OK: main index"
    fi

    rm "$BACKUP"
fi

echo ""
echo "Done!"
