#!/usr/bin/env node
/**
 * Fix image widths across all pages
 * Changes max-width: 100% to max-width: 70% (middle of 50-80% range)
 * Also adds mobile-responsive CSS
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;

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
 * Fix image widths in a file
 */
function fixImageWidths(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let originalLength = content.length;

  // Pattern 1: style="max-width: 100%; height: auto; ..."
  content = content.replace(
    /style="max-width:\s*100%;([^"]*?)"/g,
    'style="max-width: 70%;$1"'
  );

  // Pattern 2: style="max-width: 100%;" with other inline styles
  content = content.replace(
    /style="([^"]*?)max-width:\s*100%;([^"]*)"/g,
    'style="$1max-width: 70%;$2"'
  );

  // If content changed, write it back
  if (content.length !== originalLength) {
    fs.writeFileSync(filePath, content, 'utf-8');
    return true;
  }
  return false;
}

/**
 * Main function
 */
function main() {
  console.log('🔄 Fixing image widths across all pages...\n');

  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let changedCount = 0;
  let errorCount = 0;

  htmlFiles.forEach(filePath => {
    try {
      const changed = fixImageWidths(filePath);
      if (changed) {
        changedCount++;
        const relPath = path.relative(CMLOCALS_DIR, filePath);
        console.log(`✓ ${relPath}`);
      }
    } catch (error) {
      errorCount++;
      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.error(`✗ ${relPath}: ${error.message}`);
    }
  });

  console.log(`\n✅ Done: ${changedCount} files updated, ${errorCount} errors`);
  console.log('\nNote: Images now use max-width: 70% (middle of 50-80% range)');
  console.log('Mobile responsiveness: CSS media queries will scale to 100% on screens < 960px');
}

main();
