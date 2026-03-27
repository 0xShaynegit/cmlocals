#!/usr/bin/env node
/**
 * Remove all 90-day reporting pro tip remnants from pages
 * Keep visa expiry pro tips intact
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;

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

function removeNineDayRemnants(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let changed = false;

  // Remove the 90-day pro-tip bubble (the entire card with input and message)
  // Match: <!-- 90-DAY PRO TIP --> through closing </div>
  const bubbleRegex = /<!-- 90-DAY PRO TIP -->\s*<div[^>]*>[\s\S]*?proTipSubmitBtn[\s\S]*?<\/div>\s*<\/div>/;
  if (bubbleRegex.test(content)) {
    content = content.replace(bubbleRegex, '');
    changed = true;
    console.log(`✓ Removed 90-day pro-tip bubble from: ${path.relative(CMLOCALS_DIR, filePath)}`);
  }

  // Remove the pro-tip-modal div for 90-day reporting (calendar chooser)
  // Match: <!-- Pro Tip Modal --> through closing </div> for that modal
  const modalRegex = /<!-- Pro Tip Modal -->\s*<div id="proTipModal" class="pro-tip-modal">[\s\S]*?<\/div>\s*<\/div>/;
  if (modalRegex.test(content)) {
    content = content.replace(modalRegex, '');
    changed = true;
    console.log(`✓ Removed pro-tip-modal from: ${path.relative(CMLOCALS_DIR, filePath)}`);
  }

  // Remove 90-day specific JavaScript code
  // Match: the entire script tag containing formatDateForICS and generateICS functions
  const ninetyDayScriptRegex = /<script>\s*function formatDateForICS[\s\S]*?<\/script>/;
  if (ninetyDayScriptRegex.test(content)) {
    content = content.replace(ninetyDayScriptRegex, '');
    changed = true;
    console.log(`✓ Removed 90-day JS logic from: ${path.relative(CMLOCALS_DIR, filePath)}`);
  }

  if (changed) {
    fs.writeFileSync(filePath, content, 'utf-8');
  }

  return changed;
}

function main() {
  console.log('🗑️  Removing 90-day reporting remnants...\n');
  console.log('- Remove: Pro Tip Modal (Add to Calendar box)');
  console.log('- Remove: 90-day calculation JavaScript');
  console.log('- Keep: Visa expiry pro tips\n');

  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let updateCount = 0;
  let errorCount = 0;

  htmlFiles.forEach(filePath => {
    try {
      const updated = removeNineDayRemnants(filePath);
      if (updated) {
        updateCount++;
      }
    } catch (error) {
      errorCount++;
      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.error(`✗ ${relPath}: ${error.message}`);
    }
  });

  console.log(`\n✅ Done: ${updateCount} files updated, ${errorCount} errors`);
}

main();
