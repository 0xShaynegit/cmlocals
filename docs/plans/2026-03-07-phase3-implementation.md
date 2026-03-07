# Phase 3: Image Distribution + Alt-Text Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Distribute 89 available images from `/images/` directory across 40-50 active website pages with centered alignment and CMLocals-branded alt-text, prioritizing ED visa program pages.

**Architecture:** Audit pages by type (ED visas → visas → chiang-mai → immigration → culture/other), select contextually relevant images from pool, insert `<figure>` blocks with centered CSS and SEO-optimized alt-text following "CMLocals Chiang Mai Locals [context] [description]" format.

**Tech Stack:** HTML5, CSS (inline styling for centering), WebP images, responsive design patterns

---

## Task 1: Create Image Selection Reference Document

**Files:**
- Create: `docs/plans/2026-03-07-phase3-image-mapping.md`

**Step 1: Analyze available images and create selection guide**

Create a reference document that maps page types to suitable image categories from the 89-image pool. This will guide selection for all subsequent tasks.

```markdown
# Phase 3 Image Selection Reference

## Image Categories Available (89 total)

**Martial Arts & Training (15 images)**
- muay-thai-ed-visa-group.webp
- female-student-training-with-boxing-sticks.webp
- combat-demo-group-watching-instructor.webp
- hand-to-hand-combat-training-sequence.webp
- emergency-self-defence-demonstration.webp

**Language & Education (10 images)**
- english-camp-primary-school-students-group-photo.webp
- students-studying-with-instructor-in-classroom.webp
- formal-event-group-photo-movie-style-backdrop.webp

**Temples & Culture (12 images)**
- close-up-of-lighting-oil-lamps-in-buddhist-temple.webp
- circular-geometrical-mandala-sak-yant-tattoo-design.webp
- collage-of-sak-yant-tattoo-process-and-monk-ritual.webp
- female-celebrity-with-sak-yant-tattoos-on-back.webp
- doi-inthanon-twin-pagodas-sunset-landscape.webp

**Visas & Documentation (8 images)**
- closeup-of-thailand-visa-sticker-background.webp
- get-your-visa-sorted-today-promo-flyer-graphics.webp

**Local Life & Markets (12 images)**
- busy-market-stall-colorful-handmade-bags.webp
- auf-der-au-garden-german-buffet-restaurant-sign-wat-ket.webp
- chiang-mai-local-services-street-scene.webp

**Logos & Organizations (8 images)**
- chiang-mai-ambassador-connector-helper-guru-logo.webp
- chiang-mai-clean-city-official-purple-circle-logo.webp
- cnx-insure-company-logo-blue-brush-stroke.webp

## Page-to-Image Recommendations

### ED Visa Program Pages
- **muay-thai-ed-visa-chiang-mai.html**
  - Image 1: female-student-training-with-boxing-sticks.webp
  - Image 2: martial-arts-group-training-demonstration.webp

- **thai-language-ed-visa-chiang-mai.html**
  - Image 1: students-studying-with-instructor-in-classroom.webp
  - Image 2: english-camp-primary-school-students-group-photo.webp

- **hand-to-hand-combat-ed-visa-chiang-mai.html**
  - Image 1: combat-demo-group-watching-instructor.webp
  - Image 2: hand-to-hand-combat-training-sequence.webp

- **emergency-self-defence-ed-visa-chiang-mai.html**
  - Image 1: emergency-self-defence-demonstration.webp
  - Image 2: female-student-training-with-boxing-sticks.webp

- **volunteer-non-o-visa-chiang-mai.html**
  - Image 1: formal-event-group-photo-movie-style-backdrop.webp
  - Image 2: chiang-mai-local-services-street-scene.webp

### Visa Hub & Category Pages
- **pages/visas/index.html**
  - Image 1: closeup-of-thailand-visa-sticker-background.webp
  - Image 2: get-your-visa-sorted-today-promo-flyer-graphics.webp

[... continue for other page types ...]
```

**Step 2: Save reference document**

Save the mapping guide to `docs/plans/2026-03-07-phase3-image-mapping.md`

**Step 3: Verify all mapped images exist in /images/ directory**

Run: `ls /c/ZZZWebsites/cmlocals/images/ | grep -i "muay-thai\|students-studying\|combat-demo" | head -10`

Expected: Confirmation that mapped images exist

---

## Task 2: Implement ED Visa Page 1 (Muay Thai) - Template Example

**Files:**
- Modify: `C:\ZZZWebsites\cmlocals\pages\ed-visas\muay-thai-ed-visa-chiang-mai.html:1-50` (analyze structure)
- Modify: Insert images with alt-text in body sections

**Step 1: Read the page structure to identify insertion points**

Run: `head -100 C:\ZZZWebsites\cmlocals\pages\ed-visas\muay-thai-ed-visa-chiang-mai.html | grep -E "section|<h2|<p"` (or use Read tool)

Expected: Identify where sections begin/end for image placement

**Step 2: Locate the section that should have the first image (mid-article)**

Find: The closing `</section>` or `</p>` tag after 2-3 content sections (approximately halfway through article)

Example insertion point: After "Why Muay Thai for ED Visa" section, before "Program Structure" section

**Step 3: Write the first image figure block**

Insert at identified location:

```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/cmlocals chiang mai locals female student training with martial arts sticks in gym.webp"
    alt="CMLocals Chiang Mai Locals Muay Thai ED Visa female student training with boxing sticks in gym"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

**Step 4: Locate the section for the second image (near end)**

Find: The last major content section, before "Related Guides" or final footer section

Example insertion point: Before `<!-- RELATED GUIDES -->` comment

**Step 5: Write the second image figure block**

Insert at identified location:

```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/cmlocals chiang mai locals education visas available now martial arts group.webp"
    alt="CMLocals Chiang Mai Locals Muay Thai ED Visa group of martial arts students during training demonstration"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

**Step 6: Verify images display correctly**

Check: Open page in browser (or inspect HTML) to confirm:
- [ ] Images centered on desktop (text-align: center)
- [ ] Images responsive on mobile (max-width: 100%)
- [ ] Proper spacing above/below (2rem margin)
- [ ] Border radius applied (12px)
- [ ] No broken image links

**Step 7: Commit the changes**

```bash
git add pages/ed-visas/muay-thai-ed-visa-chiang-mai.html
git commit -m "feat: add centered images with alt-text to Muay Thai ED Visa page"
```

---

## Task 3: Implement Remaining ED Visa Pages (2-5)

**Files:**
- Modify: `pages/ed-visas/thai-language-ed-visa-chiang-mai.html`
- Modify: `pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html`
- Modify: `pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html`
- Modify: `pages/ed-visas/volunteer-non-o-visa-chiang-mai.html`

**Step 1: Apply template pattern to Thai Language ED Visa page**

Using the same pattern from Task 2:
1. Read page structure
2. Identify mid-article insertion point (after 2-3 sections)
3. Insert first `<figure>` with students-studying image
4. Identify near-end insertion point (before Related Guides)
5. Insert second `<figure>` with classroom/group image
6. Verify display on mobile/desktop
7. Commit

**Step 2: Apply template pattern to Hand-to-Hand Combat page**

Repeat Step 1 process with combat-related images

**Step 3: Apply template pattern to Emergency Self-Defence page**

Repeat Step 1 process with self-defence demonstration images

**Step 4: Apply template pattern to Volunteer Non-O Visa page**

Repeat Step 1 process with group/organization images

**Step 5: Batch commit all ED visa pages**

```bash
git add pages/ed-visas/*.html
git commit -m "feat: add centered images with SEO alt-text to all ED Visa program pages"
```

---

## Task 4: Implement Visa Hub & Category Pages

**Files:**
- Modify: `pages/visas/index.html`
- Modify: `pages/visas/short-stay/index.html`
- Modify: `pages/visas/long-stay/index.html`
- Modify: `pages/visas/long-stay/dtv-digital-nomad/index.html`
- Modify: `pages/visas/long-stay/permanent-residence/index.html`

**Step 1: For each visa category page, apply image insertion pattern**

1. Read page structure
2. Select 2 visa-relevant images from pool (visa stickers, documentation, informational graphics)
3. Insert mid-article image (after 2-3 sections)
4. Insert near-end image (before final section)
5. Apply centered figure styling
6. Generate alt-text: "CMLocals Chiang Mai Locals [Visa Type] [image description]"
7. Verify mobile responsiveness
8. Commit per file or batch

**Step 2: Example alt-text for visa pages**

- DTV page: "CMLocals Chiang Mai Locals DTV Digital Nomad Visa documentation with official Thailand sticker"
- Long-Stay: "CMLocals Chiang Mai Locals Long-Stay Visa requirements checklist and application documentation"
- Permanent Residence: "CMLocals Chiang Mai Locals Thailand Permanent Residence official documentation and visa sticker"

**Step 3: Batch commit visa pages**

```bash
git add pages/visas/*.html pages/visas/**/*.html
git commit -m "feat: add centered images with alt-text to visa hub and category pages"
```

---

## Task 5: Implement Chiang Mai Lifestyle Pages (11 articles)

**Files:**
- Modify: `pages/chiang-mai/why-chiang-mai-base.html`
- Modify: `pages/chiang-mai/where-to-stay.html`
- Modify: `pages/chiang-mai/cost-of-living.html`
- Modify: `pages/chiang-mai/long-term-living.html`
- Modify: `pages/chiang-mai/healthcare.html`
- Modify: `pages/chiang-mai/insurance.html`
- Modify: `pages/chiang-mai/taxes.html`
- Modify: `pages/chiang-mai/phones-and-banking.html`
- Modify: `pages/chiang-mai/getting-around.html`
- Modify: `pages/chiang-mai/things-to-do.html`
- Modify: `pages/chiang-mai/digital-nomads.html`

**Step 1: For each Chiang Mai article, apply image insertion pattern**

For each of the 11 pages:
1. Read article content
2. Select 2 contextually relevant images:
   - **why-chiang-mai-base:** Local life, temples, neighborhoods
   - **where-to-stay:** Markets, streets, local scenes
   - **cost-of-living:** Markets, vendors, local commerce
   - **long-term-living:** Expat-friendly locations, neighborhoods
   - **healthcare:** Hospital/clinic scenes (if available) or professional settings
   - **insurance:** Official/professional imagery
   - **taxes:** Business/professional imagery
   - **phones-and-banking:** Technology, local services
   - **getting-around:** Transport scenes, scooters, streets
   - **things-to-do:** Temples, markets, activities
   - **digital-nomads:** Cafes, coworking spaces, laptops

3. Insert images following template pattern
4. Generate alt-text: "CMLocals Chiang Mai Locals [Article Topic] [image description]"
5. Verify mobile responsiveness
6. Commit per article or batch by topic

**Step 2: Example alt-text for lifestyle pages**

- Why Chiang Mai: "CMLocals Chiang Mai Locals neighborhood street scene with local residents and green spaces"
- Where to Stay: "CMLocals Chiang Mai Locals busy market stall with colorful handmade bags and local vendor"
- Things to Do: "CMLocals Chiang Mai Locals close up of lighting oil lamps in Buddhist temple with golden decorations"
- Digital Nomads: "CMLocals Chiang Mai Locals formal event group photo in professional conference setting backdrop"

**Step 3: Batch commit Chiang Mai articles**

```bash
git add pages/chiang-mai/*.html
git commit -m "feat: add centered lifestyle images with SEO alt-text to all Chiang Mai guides"
```

---

## Task 6: Implement Immigration, Culture, & Other Pages

**Files:**
- Modify: `pages/immigration/index.html`
- Modify: `pages/immigration/90-day-reporting/index.html`
- Modify: `pages/immigration/tm30-registration/index.html`
- Modify: `pages/immigration/overstay-penalties/index.html`
- Modify: `pages/immigration/chiang-mai-immigration-guide/index.html`
- Modify: `pages/culture/*.html` (sak-yant, temples, food culture, etiquette, festivals, etc.)
- Modify: `pages/checklists/index.html`
- Modify: `pages/tools/visa-quiz/index.html`
- Modify: `pages/about-cmlocals.html`

**Step 1: Immigration pages - use visa/documentation imagery**

For each immigration page:
1. Select images: visa stickers, documentation, official signage
2. Insert with alt-text: "CMLocals Chiang Mai Locals [Immigration Topic] [description]"
3. Example: "CMLocals Chiang Mai Locals 90-Day Reporting Thailand immigration form and official documentation"

**Step 2: Culture pages - use temple, tattoo, festival imagery**

For each culture page:
1. Select images: temples, oil lamps, sak yant, festivals, food
2. Insert with alt-text: "CMLocals Chiang Mai Locals [Culture Topic] [scene description]"
3. Example: "CMLocals Chiang Mai Locals Sak Yant collage showing tattoo process with monk ritual and golden temple"

**Step 3: Tools, checklists, other pages - use relevant graphics/scenes**

1. Visa Quiz: use visa/checklist imagery
2. Checklists: use documentation imagery
3. About: use group photos, professional backdrops

**Step 4: Batch commit remaining pages**

```bash
git add pages/immigration/*.html pages/immigration/**/*.html
git commit -m "feat: add images with alt-text to immigration compliance pages"
```

```bash
git add pages/culture/*.html
git commit -m "feat: add cultural and educational images with alt-text to culture pages"
```

```bash
git add pages/checklists/*.html pages/tools/*.html pages/about-cmlocals.html
git commit -m "feat: add images with alt-text to tools, checklists, and support pages"
```

---

## Task 7: Quality Assurance & Verification

**Files:**
- Verify: All modified HTML files
- Test: Mobile responsiveness, image loading, alt-text accuracy

**Step 1: Verify all images load correctly**

Run a spot-check on each page type:
- Open 1 ED visa page in browser → check image display, centering, alt-text in inspector
- Open 1 Chiang Mai article → check image display, centering
- Open 1 immigration page → check image display
- Open 1 culture page → check image display

Expected: All images centered, responsive, no broken links, alt-text visible in dev inspector

**Step 2: Mobile responsiveness check**

For each page type (sample 1-2 pages):
1. Open in mobile viewport (375px width)
2. Verify images stack properly (max-width: 100%)
3. Verify text wrapping around images (or images full-width on mobile)
4. Verify margins and padding (2rem or clamp equivalent)

Expected: Clean layout, no horizontal scrolling, proper spacing

**Step 3: Alt-text accuracy verification**

Audit 10 random images across page types:
- [ ] Format follows "CMLocals Chiang Mai Locals [context] [description]"
- [ ] Contains relevant SEO keywords for page topic
- [ ] Descriptive enough for screen readers
- [ ] No technical jargon or overly generic text

**Step 4: Image file integrity check**

Run: `find /c/ZZZWebsites/cmlocals/pages -name "*.html" -exec grep -l "src=\"/images/" {} \; | wc -l`

Expected: Count of pages with images (should match ~40-50 pages)

Run: `grep -r "src=\"/images/" pages/ | grep -o "/images/[^\"]*" | sort -u | wc -l`

Expected: Count of unique images used (should be subset of 89)

**Step 5: Verify no broken img tags**

Run: `grep -r "<img" pages/ | grep -v "alt=" | head -5`

Expected: No results (all images have alt-text)

**Step 6: Create QA summary report**

Document findings in `docs/plans/2026-03-07-phase3-qa-report.md`:
- Pages audited
- Issues found (if any)
- Sample alt-text examples verified
- Mobile responsiveness confirmed
- Recommendation for deployment

---

## Task 8: Final Cleanup & Review

**Files:**
- Verify: All commits complete
- Review: Phase 2 links still intact
- Ensure: No _raw/ folder touched

**Step 1: Verify Phase 2 internal links not affected**

Run: `grep -r "href=\"/pages/chiang-mai/\"" pages/ | head -5`

Expected: Hub links still present from Phase 2

Run: `grep -r "related-guides-section" pages/chiang-mai/ | wc -l`

Expected: 11 matches (all Chiang Mai articles have related guides from Phase 2)

**Step 2: Confirm _raw/ folder untouched**

Run: `git status | grep "_raw"`

Expected: No output (no changes to _raw/)

**Step 3: View commit log for Phase 3**

Run: `git log --oneline | grep -E "images|alt-text" | head -10`

Expected: List of all Phase 3 image commits

**Step 4: Final summary**

Create comprehensive summary of Phase 3 completion:
- [ ] All 40-50 active pages now have 2 centered images each
- [ ] All images use alt-text following CMLocals format
- [ ] All images from `/images/` directory only
- [ ] Mobile responsiveness verified
- [ ] Phase 2 internal links preserved
- [ ] No changes to _raw/ or legacy folders
- [ ] All commits completed with clear messages

---

## Success Criteria Checklist

- [ ] ED visa program pages (5) complete with images + alt-text
- [ ] Visa hub/category pages complete with images + alt-text
- [ ] Chiang Mai lifestyle articles (11) complete with images + alt-text
- [ ] Immigration pages complete with images + alt-text
- [ ] Culture pages complete with images + alt-text
- [ ] Tools/checklists pages complete with images + alt-text
- [ ] All images centered with 12px border radius
- [ ] All images responsive (max-width: 100%)
- [ ] Alt-text follows "CMLocals Chiang Mai Locals [context] [description]" format
- [ ] Alt-text includes SEO keywords relevant to page topic
- [ ] No broken image links
- [ ] Mobile responsiveness confirmed
- [ ] Phase 2 internal links preserved
- [ ] No changes to _raw/ folder
- [ ] All changes committed with clear messages

---

## Next Phases

After Phase 3 completion:
- **Phase 4:** Footer restructuring (ED Visas column, remove legal links)
- **Phase 5:** Header/navigation ED Visas prominence enhancements
