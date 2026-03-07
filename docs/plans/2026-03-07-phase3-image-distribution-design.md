# Phase 3: Image Distribution + Alt-Text Standards Design
**Date:** 2026-03-07
**Project:** CMLocals Internal Linking & Image Optimization
**Phase:** 3 of 4
**Status:** Design Approved

---

## Overview

Distribute 89 available images from `/images/` directory across active website pages with:
- **2 images per page** (distributed in body sections)
- **Centered alignment** with responsive scaling
- **CMLocals-branded alt-text** following SEO + accessibility standards
- **Priority sequence:** ED visa programs first, then all other page types

---

## Scope

### In Scope
- All active pages under `/pages/` directory
- ED visa program pages (5 pages) — Phase 1
- Visa hub, short-stay, long-stay, ED visas pages
- Chiang Mai lifestyle pages (11 articles)
- Immigration compliance pages
- Culture/education pages
- Tools, checklists pages
- Total: ~40-50 active pages

### Out of Scope
- `_raw/` folder (archived WordPress content) — NO CHANGES
- Legacy/obsolete pages
- Image optimization/compression (use existing 89 WebP assets as-is)
- Image upload or new asset creation

---

## Image Asset Pool

**Total Available:** 89 images in `/images/` directory

**Format:** WebP (optimized, ready to use)

**Content Categories:**
- Martial arts & training (muay thai, hand-to-hand combat, self-defence)
- Language & education (classrooms, students, learning)
- Buddhist temples & culture (oil lamps, pagodas, sak yant)
- Visa & documentation (visa stickers, official documents)
- Markets & local life (street scenes, markets, neighborhoods)
- Restaurants & venues (establishments, signage)
- Local logos & organizations (ChiangMaiAmbassador, CNX Insure, etc.)
- Group photos & events (formal events, martial arts groups)

**Filename Convention:** Already prefixed with "CMLocals Chiang Mai Locals" — ideal for alt-text extraction.

---

## Placement Strategy

### Images Per Page: 2

1. **First Image (Mid-Article)**
   - Position: After 2-3 content sections
   - Purpose: Break up text, reinforce early concepts
   - Placement: `<figure>` block within article body

2. **Second Image (Near End)**
   - Position: Before final section, after main content
   - Purpose: Visual recap before Related Guides or footer
   - Placement: `<figure>` block before closing sections

### Alignment & Styling
- **Horizontal:** Centered on all viewport sizes
- **Vertical Margin:** 2rem above/below (clamp for mobile)
- **Border Radius:** 12px (subtle rounded corners)
- **Responsive:** `max-width: 100%; height: auto;`
- **Container:** Use `<figure>` semantic element

---

## Alt-Text Standard

### Format
```
CMLocals Chiang Mai Locals [page context] [image description + SEO keywords]
```

### Components
1. **Brand + Location:** "CMLocals Chiang Mai Locals" (constant)
2. **Page Context:** Page title or topic (e.g., "Thai Language ED Visa", "Where to Stay")
3. **Image Description + Keywords:** Descriptive phrase with SEO-relevant terms
   - What: object/action/scene
   - Who: people type (students, instructor, etc.)
   - Where: location (classroom, temple, market)
   - Context: relevance to visa/lifestyle topic

### Examples
- **ED Visa Language Page:**
  "CMLocals Chiang Mai Locals Thai Language ED Visa students studying with instructor in classroom"

- **Muay Thai Page:**
  "CMLocals Chiang Mai Locals Muay Thai ED Visa female student training with boxing sticks in gym"

- **Where to Stay Page:**
  "CMLocals Chiang Mai Locals busy market stall with colorful handmade bags and local vendor"

- **Temple/Culture Page:**
  "CMLocals Chiang Mai Locals close up of lighting oil lamps in Buddhist temple with golden details"

---

## Implementation Pattern

### HTML Structure
```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/[filename].webp"
    alt="CMLocals Chiang Mai Locals [page context] [description]"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

### Insertion Points
1. **After target section** (mid-article): Place `<figure>` after closing `</section>` or `</p>`
2. **Before Related Guides** (near end): Place `<figure>` between last content section and `<!-- RELATED GUIDES -->`
3. **Verify spacing:** Maintain consistent vertical rhythm with clamp-based margins

---

## Implementation Sequence

### Phase 3A: ED Visa Program Pages (Priority 1)
Pages: 5 ED visa pages
- muay-thai-ed-visa-chiang-mai.html
- thai-language-ed-visa-chiang-mai.html
- hand-to-hand-combat-ed-visa-chiang-mai.html
- emergency-self-defence-ed-visa-chiang-mai.html
- volunteer-non-o-visa-chiang-mai.html

Tasks:
1. Audit each page for content sections
2. Select 2 matching images from pool
3. Generate alt-text following standard
4. Insert centered figures with alt-text
5. Visual QA (mobile + desktop)

### Phase 3B: Remaining Page Types (Priority 2)
Pages: ~35 pages across:
- Visa hub & category pages (6 pages)
- Chiang Mai articles (11 pages)
- Immigration pages (5 pages)
- Culture pages (5 pages)
- Tools & checklists (3 pages)
- Other support pages (5 pages)

Process: Same as 3A, batch by page type

---

## Quality Assurance Checklist

- [ ] All images from `/images/` directory only
- [ ] No images from `_raw/` or other folders
- [ ] Alt-text follows CMLocals format consistently
- [ ] Alt-text includes relevant SEO keywords for page topic
- [ ] Images centered on all viewport sizes
- [ ] Border radius applied (12px)
- [ ] Margins consistent (2rem or clamp equivalent)
- [ ] Image load performance acceptable (WebP optimized)
- [ ] No broken image links
- [ ] Mobile responsiveness verified
- [ ] Semantic `<figure>` element used

---

## Success Criteria

1. **Coverage:** All active pages have 2 relevant images each
2. **Alt-Text:** 100% of images have CMLocals-branded, SEO-optimized alt-text
3. **Alignment:** All images centered, responsive
4. **Performance:** Page load times remain acceptable
5. **Visual Quality:** Images contextually relevant to page content
6. **Accessibility:** Alt-text provides meaningful context for screen readers

---

## Dependencies & Constraints

- Must use existing 89 images in `/images/` — no new uploads
- Do NOT touch `_raw/` folder under any circumstances
- Maintain existing page structure (don't restructure layouts)
- Preserve all internal links added in Phase 2
- Follow hero/footer color constraints (no color changes)

---

## Next Steps

1. Generate detailed implementation plan with task breakdown (writing-plans skill)
2. Execute Phase 3A (ED visa pages first)
3. Execute Phase 3B (remaining pages)
4. Phase 4: Footer restructuring (ED Visas column, remove legal links)
5. Phase 5: Additional header/navigation enhancements
