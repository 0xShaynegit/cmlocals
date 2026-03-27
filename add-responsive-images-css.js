#!/usr/bin/env node
/**
 * Add responsive-images.css to all HTML pages
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;
const CSS_LINK = '<link rel="stylesheet" href="/shared/css/responsive-images.css">';

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

function addResponsiveImagesCSS(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');

  if (content.includes('responsive-images.css')) {
    return false;
  }

  if (!content.includes('</head>')) {
    return false;
  }

  content = content.replace('</head>', `${CSS_LINK}\n</head>`);
  fs.writeFileSync(filePath, content, 'utf-8');
  return true;
}

function main() {
  console.log('🔄 Adding responsive-images.css to all pages...\n');

  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let successCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  htmlFiles.forEach(filePath => {
    try {
      const added = addResponsiveImagesCSS(filePath);
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
