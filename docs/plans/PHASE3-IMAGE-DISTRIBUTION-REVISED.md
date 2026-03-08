# Phase 3: Image Distribution (Revised) — 3 Images Per Page

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Distribute 169 available WebP images across ~75 active pages (3 images per page where feasible, 2 minimum) with CMLocals-branded alt-text and centered responsive alignment.

**Architecture:** Page-by-page execution with consistent `<figure>` placement pattern. Insert images in article body (mid-section + later sections), maintain hero-to-footer flow. Use GROQ query to automate image-filename-to-alt-text mapping where possible.

**Tech Stack:** HTML5 `<figure>` semantic element, CSS Grid/flexbox for centering, WebP image format (already optimized), alt-text SEO standards.

**Constraints:**
- ✅ 169 images in `/images/` directory (WebP format)
- ❌ DO NOT touch ED visa pages (5 pages complete)
- ❌ DO NOT touch checklists (no images)
- ❌ DO NOT touch `_raw/` folder (archived content)

---

## Inventory & Feasibility

| Metric | Count |
|--------|-------|
| Total images available | 169 |
| Active pages (excluding ED visas + checklists) | ~75 |
| Target distribution | 2-3 per page |
| Total capacity @ 2 per page | 150 (✅ achievable) |
| Total capacity @ 3 per page | 225 (⚠️ limited to ~56 pages) |

**Strategy:** Prioritize 3 images on high-value pages:
- **Tier 1 (3 images):** 11 Chiang Mai lifestyle, 6 visa hub/category, 8 immigration pages = 25 pages
- **Tier 2 (2 images):** Remaining ~50 pages

**Result:** ~119 images on Tier 1 (avg 4.8 per page, distribute), ~50 images on Tier 2

---

## Page Priority Sequence

### Phase 3A: Chiang Mai Lifestyle Pages (Tier 1) — 11 pages

1. `pages/chiang-mai/why-chiang-mai-base.html` — 3 images
2. `pages/chiang-mai/where-to-stay.html` — 3 images
3. `pages/chiang-mai/long-term-living.html` — 3 images
4. `pages/chiang-mai/things-to-do.html` — 3 images
5. `pages/chiang-mai/digital-nomads.html` — 3 images
6. `pages/chiang-mai/cost-of-living.html` — 3 images
7. `pages/chiang-mai/phones-and-banking.html` — 3 images
8. `pages/chiang-mai/getting-around.html` — 3 images
9. `pages/chiang-mai/healthcare.html` — 3 images
10. `pages/chiang-mai/insurance.html` — 3 images
11. `pages/chiang-mai/taxes.html` — 3 images

**Total images:** 33 images
**Image theme:** Markets, temples, people, lifestyle scenes, healthcare facilities, banking/phones, transportation, local venues

---

### Phase 3B: Visa Hub & Category Pages (Tier 1) — 6 pages

1. `pages/visas/index.html` (hub) — 3 images
2. `pages/visas/short-stay/index.html` (category hub) — 3 images
3. `pages/visas/short-stay/visa-exempt-entry.html` — 2 images
4. `pages/visas/short-stay/tourist-visa.html` — 2 images
5. `pages/visas/short-stay/visa-on-arrival.html` — 2 images
6. `pages/visas/short-stay/visa-extensions.html` — 2 images

**Total images:** 14 images
**Image theme:** Passport stamps, official documents, borders, travelers

---

### Phase 3C: Short-Stay Visa Pages (Tier 2) — 4 pages

7. `pages/visas/short-stay/border-runs.html` — 2 images
8. `pages/visas/long-stay/index.html` (hub) — 2 images
9. `pages/visas/long-stay/retirement-visa.html` — 2 images
10. `pages/visas/long-stay/long-stay-visa.html` — 2 images

**Total images:** 8 images
**Image theme:** Borders, visa documentation, retirees, expat life

---

### Phase 3D: Immigration Compliance Pages (Tier 1) — 8 pages

1. `pages/immigration/90-day-reporting.html` — 3 images
2. `pages/immigration/tm30-registration.html` — 3 images
3. `pages/immigration/overstay-penalties.html` — 2 images
4. `pages/immigration/immigration-guide.html` — 3 images
5. `pages/immigration/visa-rules.html` — 2 images
6. `pages/immigration/document-requirements.html` — 2 images
7. `pages/immigration/re-entry-permits.html` — 2 images
8. `pages/immigration/departure-procedures.html` — 2 images

**Total images:** 19 images
**Image theme:** Official documents, passport stamps, immigration offices, procedures

---

### Phase 3E: Culture & Education Pages (Tier 2) — ~8 pages

1. `pages/culture/buddhism.html` — 2 images
2. `pages/culture/thai-festivals.html` — 2 images
3. `pages/culture/local-customs.html` — 2 images
4. `pages/culture/thai-language.html` — 2 images
5. `pages/culture/art-crafts.html` — 2 images
... + 3 more similar pages

**Total images:** ~16 images
**Image theme:** Temples, festivals, monks, traditional crafts, language learning, cultural events

---

### Phase 3F: Tools & Other Pages (Tier 2) — ~15 pages

- `pages/tools/visa-calculator.html` — 2 images
- `pages/tools/packing-guide.html` — 2 images
- `pages/tools/currency-converter.html` — 2 images
- `pages/tools/weather-planner.html` — 2 images
- `index.html` (homepage) — 2-3 images (if not already populated)
- FAQ pages, blogs, support pages — 2 each

**Total images:** ~30 images
**Image theme:** Local life, practical activities, Chiang Mai scenes

---

## Implementation Tasks

### Task 1: Audit Page Structure & Build Image Mapping

**Files:**
- Audit: All 75 target pages (identify existing images, section placement)
- Create: `docs/IMAGE-MAPPING.csv` — page | section_count | recommended_positions | image_count

**Step 1: Create audit spreadsheet**

Format:
```
page_path,sections,recommended_image_positions,target_count,status
pages/chiang-mai/why-chiang-mai-base.html,6,"After Section 2, Before Section 5",3,pending
pages/visas/short-stay/visa-exempt-entry.html,5,"After Section 1, Before Section 4",2,pending
...
```

**Step 2: Map content structure**

For each page in Phase 3A-F:
1. Read the page
2. Count `<section>` or `<h2>` tags (content divisions)
3. Identify ideal insertion points (after 2-3 sections for first image, before Related Guides for last)
4. Add to spreadsheet

**Step 3: Verify insertion points work**

- First image: After 2-3 content sections (mid-article)
- Second image (if 2): Before final section or Related Guides
- Third image (if 3): Distribute between first and last (after section 4-5 in long articles)

**Step 4: Save audit**

```bash
git add docs/IMAGE-MAPPING.csv
git commit -m "docs: audit page structure for image distribution"
```

---

### Task 2: Build Image Filename-to-Alt-Text Mapping

**Files:**
- Create: `docs/IMAGE-ALT-TEXT-POOL.txt` — filename | topic | suggested_alt_text

**Step 1: List all image filenames**

```bash
ls -1 /images/*.webp | sed 's|.*/||' > /tmp/images.txt
```

**Step 2: Group by content theme**

Read all filenames and categorize:
- **Temples/Buddha:** temple, pagoda, sak yant, monk, oil lamp, prayer, buddha, shrine
- **Markets/Local:** market, vendor, shop, street, restaurant, cafe, signage
- **People/Groups:** students, instructor, group, family, worker, locals
- **Visa/Documents:** passport, visa, document, official, stamp, border
- **Transport:** motorbike, tuk-tuk, car, bicycle, scooter, bus, songthaew
- **Healthcare:** hospital, clinic, doctor, pharmacy, medical
- **Education:** classroom, learning, study, training, gym, martial, boxing
- **Landscape/Nature:** temple, shrine, garden, park, sunset, water, mountain

**Step 3: Create mapping file**

```
cmlocals chiang mai locals muay thai ed visa...webp | Muay Thai ED Visa | "CMLocals Chiang Mai Locals Muay Thai ED Visa students training in gym with boxing equipment"
cmlocals chiang mai locals temple...webp | Temples/Culture | "CMLocals Chiang Mai Locals traditional Buddhist temple with ornate golden details and oil lamps"
...
```

**Step 4: Save & verify**

```bash
git add docs/IMAGE-ALT-TEXT-POOL.txt
git commit -m "docs: create image-to-alt-text mapping pool"
```

---

### Task 3: Implement Phase 3A — Chiang Mai Lifestyle Pages (11 pages × 3 images)

For each of the 11 Chiang Mai pages:

#### Chiang Mai Page Template

**Files:**
- Modify: `pages/chiang-mai/[page].html`

**Example: why-chiang-mai-base.html**

**Step 1: Read page & identify sections**

```bash
# Count content sections
grep -c "<section\|<h2" pages/chiang-mai/why-chiang-mai-base.html
```

Expected: 5-8 content sections

**Step 2: Plan image positions**

- Image 1: After section 2 (intro + first benefit)
- Image 2: After section 4-5 (mid-content)
- Image 3: Before Related Guides section (recap)

**Step 3: Select matching images**

Choose from pool:
- Template tags to search: marketplace scenes, people, street life, temples, locals, vibrant

**Step 4: Write HTML `<figure>` blocks**

```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/cmlocals-chiang-mai-locals-market-vendor-smiling.webp"
    alt="CMLocals Chiang Mai Locals Why Chiang Mai Base daily market interaction with friendly local vendor"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

**Step 5: Insert after target section**

Locate closing tag of target section (e.g., `</section>` or `</p>` after section 2), insert `<figure>` block immediately after.

**Step 6: Verify spacing**

- Check margins don't collapse with existing section margins
- Verify image doesn't overlap with sidebar (if applicable)
- Mobile: scroll through rendered page to confirm centered

**Step 7: Commit**

```bash
git add pages/chiang-mai/why-chiang-mai-base.html
git commit -m "feat: add 3 centered images with alt-text to why-chiang-mai-base page"
```

**Repeat for all 11 Chiang Mai pages** (why-chiang-mai-base, where-to-stay, long-term-living, things-to-do, digital-nomads, cost-of-living, phones-and-banking, getting-around, healthcare, insurance, taxes)

---

### Task 4: Implement Phase 3B — Visa Hub & Category Pages (6 pages)

**Files:**
- Modify: `pages/visas/index.html`, `pages/visas/short-stay/index.html`, `pages/visas/short-stay/visa-exempt-entry.html`, etc.

**Repeat Task 3 pattern** for 6 visa hub/category pages:
- Hub pages: 3 images each (broader content)
- Short-stay visa detail pages: 2 images each (focused content)

**Image themes:** Passport stamps, borders, official documents, travelers at checkpoints

**Total commits:** 6 commits (one per page)

---

### Task 5: Implement Phase 3C-D — Remaining Visa & Immigration Pages

**Files:**
- Modify: 12 additional visa + immigration pages

**Repeat Task 3 pattern** for:
- Short-stay detail pages (border-runs, extensions, etc.)
- Immigration compliance pages (90-day reporting, TM30, overstay, etc.)

**Image themes:** Official stamps, immigration office scenes, documentation, borders, expat activities

**Total commits:** 12 commits

---

### Task 6: Implement Phase 3E-F — Culture, Tools & Other Pages

**Files:**
- Modify: ~20 pages (culture pages, tools pages, FAQ, support)

**Repeat Task 3 pattern**:
- Culture pages: 2 images each
- Tools/support pages: 2 images each

**Image themes:** Temples, festivals, local crafts, practical Chiang Mai scenes

**Total commits:** 20 commits

---

### Task 7: Visual QA & Verification

**Test on mobile (375px), tablet (768px), desktop (1200px+):**

For each updated page:
1. Open in browser DevTools (iPhone 12 emulation)
2. Scroll through page — verify images are centered, not stretched
3. Check alt-text in source (`F12 > Inspector`)
4. Desktop view — confirm sidebar doesn't overlap images (if applicable)
5. Page load: Measure total image load time (WebP should be <3s on 4G)

**Checklist per page:**
- [ ] All 2-3 images centered on all viewports
- [ ] Alt-text matches CMLocals format
- [ ] No broken image links
- [ ] Border radius applied (12px)
- [ ] Margins consistent (2rem or clamp)
- [ ] Page structure unchanged (hero, content, footer intact)

**Step 1: QA spreadsheet**

Create `docs/QA-RESULTS.csv`:
```
page_path,images_count,alt_text_compliant,mobile_centered,desktop_load_time,status
pages/chiang-mai/why-chiang-mai-base.html,3,✅,✅,2.1s,pass
...
```

**Step 2: Run visual tests on all 75 pages**

Automate with screenshot tool (optional):
```bash
# Pseudo-code: iterate pages, screenshot 375px view
for page in pages/**/*.html; do
  echo "Testing $page"
  # Screenshot logic (use Puppeteer, Playwright, or manual)
done
```

**Step 3: Final commit**

```bash
git add docs/QA-RESULTS.csv
git commit -m "test: complete visual QA for image distribution across all pages"
```

---

### Task 8: Final Audit & Summary

**Files:**
- Create: `docs/PHASE3-COMPLETION-REPORT.md`

**Report contents:**
```markdown
# Phase 3 Completion Report

## Coverage
- Pages with 3 images: 25 (Tier 1 high-value)
- Pages with 2 images: 50 (Tier 2 standard)
- Total pages updated: 75
- Total images distributed: 165/169 (97%)
- Images remaining in pool: 4 (buffer)

## Quality Metrics
- Alt-text compliance: 100%
- Mobile responsiveness: 100%
- Broken links: 0
- Page load impact: <500ms per page average

## Next Phase (Phase 4)
- Footer restructuring (ED Visas column, remove legal links)
- Navigation enhancements
- SEO metadata updates

## Commits
- Total commits: ~80 (1 per page + QA + audit)
- Branch: Phase-3-image-distribution
- Ready for: Code review & merge
```

**Step 1: Generate report**

Count actual pages updated, images used, QA results. Document any edge cases.

**Step 2: Final commit**

```bash
git add docs/PHASE3-COMPLETION-REPORT.md
git commit -m "docs: complete Phase 3 image distribution"
```

---

## Execution Flow

1. **Task 1:** Audit structure → `IMAGE-MAPPING.csv`
2. **Task 2:** Build image pool → `IMAGE-ALT-TEXT-POOL.txt`
3. **Tasks 3-6:** Implement pages (Chiang Mai → Visas → Immigration → Culture/Tools)
4. **Task 7:** Visual QA all pages
5. **Task 8:** Final report & summary

---

## Success Criteria

- [x] All 75 pages have 2-3 relevant images
- [x] 100% alt-text CMLocals-branded & SEO-optimized
- [x] All images centered, responsive, border-radius 12px
- [x] No broken links or missing images
- [x] Page load impact minimal (<500ms per page)
- [x] Mobile + desktop verified
- [x] ~80 targeted commits (one per page + audits)

---

## Rollback Plan

If issues arise:
1. `git diff HEAD~N` (inspect last N commits)
2. `git revert COMMIT_SHA` (revert specific page commits)
3. Or restart Task from issue point

All commits are atomic (one page per commit) for easy rollback.
