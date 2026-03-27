#!/usr/bin/env node
/**
 * Add local fonts.css to all pages and remove Google Fonts link
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;
const FONTS_CSS_LINK = '<link rel="stylesheet" href="/shared/css/fonts.css">';
const GOOGLE_FONTS_REGEX = /<link[^>]*href="https:\/\/fonts\.googleapis\.com[^>]*>/g;

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

function updateFontsInPage(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let changed = false;

  // Remove Google Fonts link
  if (GOOGLE_FONTS_REGEX.test(content)) {
    content = content.replace(GOOGLE_FONTS_REGEX, '');
    changed = true;
  }

  // Add local fonts.css if not already present
  if (!content.includes('fonts.css')) {
    if (content.includes('</head>')) {
      content = content.replace('</head>', `${FONTS_CSS_LINK}\n</head>`);
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(filePath, content, 'utf-8');
  }
  return changed;
}

function main() {
  console.log('🔤 Updating fonts across all pages...\n');
  console.log('- Remove: Google Fonts CDN link');
  console.log('- Add: Local fonts.css link\n');

  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let updateCount = 0;
  let errorCount = 0;

  htmlFiles.forEach(filePath => {
    try {
      const updated = updateFontsInPage(filePath);
      if (updated) {
        updateCount++;
        const relPath = path.relative(CMLOCALS_DIR, filePath);
        console.log(`✓ ${relPath}`);
      }
    } catch (error) {
      errorCount++;
      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.error(`✗ ${relPath}: ${error.message}`);
    }
  });

  console.log(`\n✅ Done: ${updateCount} files updated, ${errorCount} errors`);
  console.log('\nPerformance improvement:');
  console.log('- ✅ Removed: Google Fonts CDN requests');
  console.log('- ✅ Added: Local, cached fonts');
  console.log('- ✅ Faster: No external DNS/network requests');
}

main();
