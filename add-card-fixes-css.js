#!/usr/bin/env node
/**
 * Add card-fixes.css to all HTML pages
 * Injects the shared CSS file link into the <head> section
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;
const CSS_LINK = '<link rel="stylesheet" href="/shared/css/card-fixes.css">';

/**
 * Get all HTML files recursively
 */
function getAllHtmlFiles(dir) {
  let results = [];
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      if (!file.startsWith('.') && file !== 'node_modules' && file !== 'dist' && !filePath.includes('worktree')) {
        results = results.concat(getAllHtmlFiles(filePath));
      }
    } else if (file.endsWith('.html') && file !== 'footer-template.html') {
      results.push(filePath);
    }
  });

  return results;
}

/**
 * Add card-fixes.css to page
 */
function addCardFixesCSS(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');

  // Skip if already added
  if (content.includes('card-fixes.css')) {
    return false;
  }

  // Find the closing </head> tag
  if (!content.includes('</head>')) {
    console.warn(`⚠ No </head> tag found in ${filePath}`);
    return false;
  }

  // Insert before </head>
  content = content.replace('</head>', `${CSS_LINK}\n</head>`);

  fs.writeFileSync(filePath, content, 'utf-8');
  return true;
}

/**
 * Main function
 */
function main() {
  console.log('🔄 Adding card-fixes.css to all pages...\n');

  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let successCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  htmlFiles.forEach(filePath => {
    try {
      const added = addCardFixesCSS(filePath);
      if (added) {
        successCount++;
        const relPath = path.relative(CMLOCALS_DIR, filePath);
        console.log(`✓ ${relPath}`);
      } else {
        skippedCount++;
      }
    } catch (error) {
      errorCount++;
      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.error(`✗ ${relPath}: ${error.message}`);
    }
  });

  console.log(`\n✅ Done: ${successCount} added, ${skippedCount} already have it, ${errorCount} errors`);
}

main();
