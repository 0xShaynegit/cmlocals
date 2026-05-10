#!/bin/bash

TEMPLATE="chiang-mai-office/index.html"
INDEX="index.html"
BACKUP="index.html.backup"

# Backup original
cp "$INDEX" "$BACKUP"

# Extract template's style block
TEMPLATE_STYLE_START=$(grep -n '<style>' "$TEMPLATE" | head -1 | cut -d: -f1)
TEMPLATE_STYLE_END=$(grep -n '</style>' "$TEMPLATE" | head -1 | cut -d: -f1)

TEMPLATE_STYLE=$(sed -n "${TEMPLATE_STYLE_START},${TEMPLATE_STYLE_END}p" "$TEMPLATE")

# Find style block in index
INDEX_STYLE_START=$(grep -n '<style>' "$INDEX" | head -1 | cut -d: -f1)
INDEX_STYLE_END=$(grep -n '</style>' "$INDEX" | head -1 | cut -d: -f1)

# Build new index with template's style
NEW_FILE=$(
    sed -n "1,$((INDEX_STYLE_START - 1))p" "$INDEX"
    echo "$TEMPLATE_STYLE"
    sed -n "$((INDEX_STYLE_END + 1)),\$p" "$INDEX"
)

echo "$NEW_FILE" > "$INDEX"

echo "Updated index.html with template's CSS (colors, design system)"
echo "Kept original card structure"

rm "$BACKUP"
