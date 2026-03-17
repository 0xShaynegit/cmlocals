#!/usr/bin/env node
/**
 * Footer Injection Build Script
 *
 * Reads footer-template.html and injects it into all HTML pages.
 * Automatically extracts footer background color from each page's style section.
 *
 * Usage: node build-footer.js
 */

const fs = require('fs');
const path = require('path');

const CMLOCALS_DIR = __dirname;
const FOOTER_TEMPLATE_PATH = path.join(CMLOCALS_DIR, 'footer-template.html');

// Default footer color (fallback)
const DEFAULT_FOOTER_COLOR = '#0D1117';

// Color mapping for sections
const SECTION_COLORS = {
  'chiang-mai': '#101585',
  'ed-visas': '#4F46E5',
  'visas': '#4F46E5',
  'checklists': '#4F46E5',
  'immigration': '#4F46E5',
  'culture': '#4F46E5',
  'tools': '#4F46E5',
  'default': '#4F46E5'
};

/**
 * Determine footer color based on file path
 */
function getFooterColorForFile(filePath) {
  // Homepage special case
  if (path.basename(filePath) === 'index.html' && path.dirname(filePath) === CMLOCALS_DIR) {
    return '#4F46E5';
  }

  // Chiang Mai pages
  if (filePath.includes('chiang-mai')) {
    return '#101585';
  }

  // Default for all other pages
  return '#4F46E5';
}

/**
 * Extract footer background color from page's existing style
 */
function extractFooterColorFromPage(content) {
  // Look for footer background color in inline style attribute or CSS
  const styleMatch = content.match(/footer[^}]*style="[^"]*background:\s*([^;}"]+)/i);
  if (styleMatch) {
    return styleMatch[1].trim();
  }

  // Look for --footer-bg CSS variable
  const varMatch = content.match(/--footer-bg:\s*([^;]+)/);
  if (varMatch) {
    return varMatch[1].trim();
  }

  // Fallback to section-based color
  return null;
}

/**
 * Replace footer in HTML content
 */
function injectFooter(htmlContent, filePath, footerHtml) {
  // Get the appropriate footer color
  let footerColor = extractFooterColorFromPage(htmlContent);
  if (!footerColor) {
    footerColor = getFooterColorForFile(filePath);
  }

  // Replace {{FOOTER_BG_COLOR}} placeholder
  const customizedFooter = footerHtml.replace(/{{FOOTER_BG_COLOR}}/g, footerColor);

  // Remove old footer (match opening <footer> tag through closing </footer>)
  const footerRegex = /<footer[^>]*role="contentinfo"[^>]*>[\s\S]*?<\/footer>/i;

  if (footerRegex.test(htmlContent)) {
    // Replace existing footer
    return htmlContent.replace(footerRegex, customizedFooter);
  } else {
    // No footer found - append before closing </body>
    return htmlContent.replace(/<\/body>/i, `\n${customizedFooter}\n</body>`);
  }
}

/**
 * Get all HTML files recursively
 */
function getAllHtmlFiles(dir) {
  let results = [];
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    // Skip worktrees and build directories
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
 * Main build function
 */
function build() {
  console.log('🔄 Building footer injection...\n');

  // Check if footer template exists
  if (!fs.existsSync(FOOTER_TEMPLATE_PATH)) {
    console.error('❌ Error: footer-template.html not found at', FOOTER_TEMPLATE_PATH);
    process.exit(1);
  }

  // Read footer template
  const footerTemplate = fs.readFileSync(FOOTER_TEMPLATE_PATH, 'utf-8');
  console.log('✓ Loaded footer template');

  // Get all HTML files
  const htmlFiles = getAllHtmlFiles(CMLOCALS_DIR);
  console.log(`✓ Found ${htmlFiles.length} HTML files\n`);

  let successCount = 0;
  let errorCount = 0;

  // Process each HTML file
  htmlFiles.forEach(filePath => {
    try {
      const htmlContent = fs.readFileSync(filePath, 'utf-8');
      const updatedContent = injectFooter(htmlContent, filePath, footerTemplate);

      fs.writeFileSync(filePath, updatedContent, 'utf-8');
      successCount++;

      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.log(`✓ ${relPath}`);
    } catch (error) {
      errorCount++;
      const relPath = path.relative(CMLOCALS_DIR, filePath);
      console.error(`✗ ${relPath}: ${error.message}`);
    }
  });

  console.log(`\n✅ Build complete: ${successCount} updated, ${errorCount} errors`);

  if (errorCount > 0) {
    process.exit(1);
  }
}

// Run build
build();
