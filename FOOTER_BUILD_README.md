# CMLocals Footer Build System

Centralized footer management for CMLocals website. Ensures all footer links are always in sync, never broken, and use root-relative URLs.

## How It Works

1. **Single Source of Truth**: `footer-template.html` contains all footer links
2. **Root-Relative Links**: All links use `/pages/...` (not `../../`) so they work at any depth
3. **Per-Page Colors**: Footer background color auto-detected from each page's section (Chiang Mai = `#101585`, others = `#4F46E5`)
4. **Automated Injection**: Build script scans all HTML files and injects footer from template
5. **GitHub Actions**: Runs on every push, auto-commits footer changes, fails on errors

## Files

- **`footer-template.html`** — Canonical footer (one place to edit all links)
- **`build-footer.js`** — Node.js script that injects footer into all pages
- **`.github/workflows/build-footer.yml`** — GitHub Action that runs build on every push
- **`package.json`** — Dependencies (broken-link-checker for validation)

## How to Use

### Local Development

1. **Edit footer links** in `footer-template.html`
2. **Run build script** locally to test:
   ```bash
   npm install
   npm run build
   ```
3. **Verify changes** in any page's footer
4. **Commit and push** — GitHub Action will auto-inject footer into all pages

### What Happens on Every Push

1. GitHub Action checks out your code
2. Runs `npm run build` which:
   - Reads all HTML files in the project
   - Extracts each page's footer background color
   - Injects footer from template with correct color
   - Replaces old footer blocks in each page
3. If changes were made, auto-commits them with message: `build: auto-inject footer into all pages`
4. Pushes changes back to repository

### Color Detection

Footer background color is determined by page location:
- **Chiang Mai pages** (`pages/chiang-mai/*`): `#101585` (dark blue)
- **All other pages**: `#4F46E5` (indigo)

To override, add `--footer-bg` CSS variable or `data-footer-color` attribute to page.

## Adding New Footer Links

Edit `footer-template.html`:

```html
<!-- Column 4: Visa Guides -->
<div class="footer-col">
  <h3 class="footer-col-title">Visa Guides</h3>
  <ul class="footer-links">
    <li><a href="/pages/visas/index.html">All Visas</a></li>
    <!-- New link here -->
    <li><a href="/pages/visas/new-page.html">New Page</a></li>
  </ul>
</div>
```

**Important**: Always use **root-relative paths** starting with `/pages/...`

## Removing a Page

If you delete or rename a page:

1. Remove the link from `footer-template.html`
2. Commit and push
3. GitHub Action will re-inject footer into all pages with updated links
4. All footer links stay in sync automatically

## Broken Link Prevention

- **Root-relative links**: Work at any nesting depth
- **Single source**: Edit once, applies everywhere
- **Git tracking**: All changes tracked and committed
- **Validation**: Can add `broken-link-checker` to catch 404s

### Optional: Add Link Checker

To fail the build if footer has broken links:

```bash
npm install --save-dev broken-link-checker
```

Then in `.github/workflows/build-footer.yml`:

```yaml
- name: Check for broken links in footer
  run: |
    npm run build
    # Build a simple test to verify all footer links exist
    node scripts/verify-footer-links.js
```

## Troubleshooting

### Footer not updating on a page?

1. Ensure page has closing `</footer>` tag
2. Check `build-footer.js` console output for errors
3. Try running `npm run build` locally first

### Wrong footer color?

Check page path:
- Pages in `/pages/chiang-mai/` should get `#101585`
- All others should get `#4F46E5`

Override by adding to page's CSS:
```css
footer {
  background: #YOUR_COLOR !important;
}
```

### Links showing as relative paths (../../)?

The build script converts all links to root-relative (`/pages/...`). If you see relative paths:
- Run `npm run build` again
- Check `footer-template.html` doesn't have relative paths
- Verify your footer template file is correct

## FAQ

**Q: Do I need to run the build script manually?**
A: No! GitHub Action runs automatically on every push.

**Q: What if I want to edit the homepage footer differently?**
A: Edit `footer-template.html` to have different content for homepage, then add conditional logic to `build-footer.js`.

**Q: Can I have different footer colors per page?**
A: Yes! The script auto-detects colors. You can also add a `footer-colors.json` config file for granular control.

**Q: How do I test locally?**
A: Run `npm install && npm run build`, then open any HTML file in your browser.

## Maintenance

- Edit `footer-template.html` whenever footer links change
- Run `npm run build` locally before committing (optional — Action will do it)
- Review auto-generated commits from GitHub Action
- Keep `build-footer.js` logic updated if adding new page sections with custom colors
