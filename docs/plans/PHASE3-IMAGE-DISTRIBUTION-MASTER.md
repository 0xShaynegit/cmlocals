# Phase 3: Image Distribution - Master Specification Document

**Project:** CMLocals Image Distribution & Alt-Text Standardization
**Phase:** 3 of 4
**Status:** PAUSED - 60+ images complete, resuming with better images
**Last Updated:** 2026-03-07
**Document Type:** Master reference consolidating design, planning, status, and execution specs

---

## ⚡ QUICK START FOR NEXT SESSION

1. **Check `/images/` folder** for any new/better images you've added
2. **Review Remaining Work** section below (16 immigration + 10 culture pages)
3. **Copy HTML Pattern** from Specifications section
4. **Follow Edit Workflow** section
5. **Use Image Recommendations** from page-by-page mappings below

---

## PROJECT OVERVIEW

### Goal
Distribute 89 available images across 40-50 active website pages with:
- **2 images per page** (mid-article and near-end placement)
- **Centered alignment** with responsive scaling
- **CMLocals-branded alt-text** following SEO + accessibility standards

### Scope: IN
- All active pages under `/pages/` directory
- ED visa program pages (5 pages) ✅ DONE
- Visa hub pages (3 pages) ✅ DONE
- Chiang Mai lifestyle pages (11 pages) ✅ DONE
- Immigration compliance pages (16 pages) ⏳ TODO
- Culture/education pages (10 pages) ⏳ TODO
- Tools & support pages (~5 pages) ⏳ TODO

### Scope: OUT
- `_raw/` folder (archived WordPress content) — NO CHANGES
- Image optimization or compression (use existing 89 WebP as-is)
- New image creation or upload

---

## ✅ COMPLETED WORK

### Task 1: Image Reference Document ✅
- Created: `/docs/plans/PHASE3-IMAGE-DISTRIBUTION-MASTER.md` (THIS FILE)
- All 89 images catalogued and mapped (see section below)

### Task 2-3: ED Visa Pages (5 pages, 15+ images) ✅
- [x] muay-thai-ed-visa-chiang-mai.html
- [x] thai-language-ed-visa-chiang-mai.html
- [x] hand-to-hand-combat-ed-visa-chiang-mai.html
- [x] emergency-self-defence-ed-visa-chiang-mai.html
- [x] volunteer-non-o-visa-chiang-mai.html

### Task 4: Visa Hub Pages (3 pages, 6 images) ✅
- [x] pages/visas/index.html
- [x] pages/visas/short-stay/index.html
- [x] pages/visas/long-stay/index.html

### Task 5: Chiang Mai Lifestyle Pages (11 pages, 21 images) ✅
- [x] cost-of-living.html (2 images)
- [x] digital-nomads.html (2 images)
- [x] getting-around.html (2 images)
- [x] healthcare.html (2 images)
- [x] insurance.html (2 images)
- [x] long-term-living.html (2 images)
- [x] phones-and-banking.html (2 images)
- [x] taxes.html (2 images)
- [x] things-to-do.html (2 images)
- [x] why-chiang-mai-base.html (2 images)
- [x] where-to-stay.html (1 image)

**Total Completed:** 19 pages, 60+ images
**Latest Commit:** `499f2fb` - Phase 3 integration

---

## ⏳ REMAINING WORK

### Task 6: Immigration Pages (16 pages, ~32 images)
**Status:** Not started
**Pages:** Each needs 2 images

- [ ] pages/immigration/90-day-reporting.html
- [ ] pages/immigration/address-change.html
- [ ] pages/immigration/blacklist-status.html
- [ ] pages/immigration/common-rejections.html
- [ ] pages/immigration/document-requirements.html
- [ ] pages/immigration/entry-strategy-guide.html
- [ ] pages/immigration/financial-requirements.html
- [ ] pages/immigration/immigration-best-practices.html
- [ ] pages/immigration/legal-rights.html
- [ ] pages/immigration/overstay-penalties.html
- [ ] pages/immigration/queue-strategy.html
- [ ] pages/immigration/re-entry-permits.html
- [ ] pages/immigration/thailand-digital-arrival-card.html
- [ ] pages/immigration/tm30-address-reporting.html
- [ ] pages/immigration/visa-border-runs.html
- [ ] pages/immigration/visa-extensions.html

**Suggested Image Types:**
- Visa documentation and official stamps
- Immigration forms and official signage
- Compliance and procedural imagery
- From image pool: visa/documentation category (11 images available)

### Task 6b: Culture Pages (10 pages, ~20 images)
**Status:** Not started
**Pages:** Each needs 2 images

- [ ] pages/culture/customs-traditions-thailand.html
- [ ] pages/culture/etiquette-when-visiting-a-sak-yant-monk.html
- [ ] pages/culture/festivals-events-chiang-mai.html
- [ ] pages/culture/sak-yant-chiang-mai.html
- [ ] pages/culture/sak-yant-designs-and-meanings.html
- [ ] pages/culture/sak-yant-getting.html
- [ ] pages/culture/temple-etiquette.html
- [ ] pages/culture/thai-culture-etiquette.html
- [ ] pages/culture/thai-food-culture.html
- [ ] pages/culture/index.html

**Suggested Image Types:**
- Buddhist temples and sacred sites
- Sak yant tattoo process and design
- Cultural festivals and celebrations
- Traditional ceremonies
- From image pool: temples/culture (13 images), festivals (7 images), sak yant (6 images)

---

## IMAGE SPECIFICATIONS & PROCESSING

### HTML Pattern (EXACT - copy/paste ready for all pages)

```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/[filename].webp"
    alt="CMLocals Chiang Mai Locals [context] [description]"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

### CSS Properties Breakdown

| Property | Value | Why It Matters |
|----------|-------|---------------|
| `text-align: center` | center | Horizontally centers image within figure element |
| `margin: 2rem 0` | 2rem vertical, 0 horizontal | Consistent spacing above/below (NOT 1.5rem or 2.5rem) |
| `max-width: 100%` | 100% | Responsive: fills container on mobile, respects max on desktop |
| `height: auto` | auto | Maintains aspect ratio on all screen sizes |
| `border-radius: 12px` | 12px | Soft corners matching CMLocals design system |

### Alt-Text Pattern (MANDATORY)

**Format:** `CMLocals Chiang Mai Locals [page topic] [image description]`

**Rules:**
- ALWAYS start with `CMLocals Chiang Mai Locals`
- Include page topic/category (e.g., "immigration", "culture", "healthcare")
- Add descriptive phrase of image content (e.g., "visa document", "temple ceremony")
- No marketing adjectives ("best", "amazing", "ultimate")
- No rhetorical questions
- Target: 10-15 words total
- Screen-reader friendly & accessible

**Examples:**
- ✅ `CMLocals Chiang Mai Locals immigration 90-day reporting official form documentation`
- ✅ `CMLocals Chiang Mai Locals culture sak yant tattoo monk ritual ceremony`
- ❌ `CMLocals Chiang Mai Locals the most amazing festival celebration ever`
- ❌ `Image of temple`

### Image Format & Location

- **Format:** `.webp` (optimized, modern)
- **Location:** `/images/` directory only
- **Naming Convention:** `cmlocals chiang mai locals [descriptor].webp`
- **Total Available:** 89 images (see catalog below)

---

## IMAGE CATALOG & RECOMMENDATIONS

### Image Categories (88 total available)

#### Martial Arts & Combat Training (20 images)
Primary use: ED visa pages, culture pages, activity sections
- combat demo group watching instructor
- education visas available now martial arts group
- female student training with martial arts sticks in gym
- hand to hand combat self defense school chiang mai
- hand to hand combat training session exercise (2 variants)
- martial arts group photo with education visa banner (2 variants)
- martial arts students group watching instructor performance
- muay thai fighters clashing in muay thai ring competition
- muay thai group photo in ring after training (2 variants)
- muay thai training session demo in chiang mai gym
- man and woman in muay thai ring wearing gloves
- self defence class
- two men sparring in martial arts gym
- two people training with martial arts sticks in gym (2 variants)
- two women sparring in muay thai ring
- women training with foam knives in self defense class

#### Language & Education (13 images)
Primary use: ED visa language pages, culture/education sections
- english camp primary school students group photo
- students stretching on mat in gym thai flag (2 variants)
- teacher pointing to whiteboard in thai language class (2 variants)
- teacher teaching thai children at outdoor school table
- thai language class (jpg)
- thai language course teacher
- volunteers and children english camp classroom activities
- volunteers distributing food and drinks to children school (2 variants)
- volunteers distributing snacks to thai school children
- volunteers with children at school english camp

#### Temples & Sacred Culture (14 images)
Primary use: Culture pages, wellness/spirituality sections
- circular geometrical mandala sak yant tattoo design
- close up of lighting oil lamps in a buddhist temple (3 variants)
- collage of sak yant tattoo process and monk ritual
- collage of sak yant tattoo ritual and golden temple
- doi inthanon twin pagodas sunset landscape (2 variants)
- get genuine sak yant tattoo monk banner
- monk performing sacred sak yant tattoo ritual on back
- monk ritual tattooing sacred sak yant on back
- monk tattooing traditional sak yant on mans back
- three tourists sitting with monks in buddhist temple
- wat phra singh golden buddha statue interior chiang mai

#### Sak Yant Tattoo Culture (6 images)
Primary use: Culture/sak yant specific pages
- female celebrity with sak yant tattoos on back
- prohibited outfits sign for visitors at thai temple entryway
- traditional vertical sak yant tattoo symbols artwork (2 variants)
- offering bowl with white and green lotus flowers
- yi peng festival celebrations with hundreds of lanterns

#### Visa & Documentation (11 images)
Primary use: Immigration pages, visa pages
- closeup of thailand visa sticker background
- get your visa sorted today promo flyer graphics (3 variants)
- non immigrant business visa stamp phnom penh 2015
- thai e-visa application template document portal (2 variants)
- thai non immigrant education visa stamp closeup
- thai tourist visa stamp phnom penh 2012
- thailand elite club membership card closeup
- thailand elite club membership card design detail

#### Local Life & Markets (3 images)
Primary use: Cost of living, where to stay, lifestyle pages
- busy market stall colorful handmade bags
- auf der au garden german buffet restaurant sign wat ket (2 variants)

#### Logos & Organizations (9 images)
Primary use: Partner references, service pages
- chiang mai ambassador connector helper guru logo
- chiang mai clean city official purple circle logo
- chiang mai safe city public awareness logo (2 variants)
- cnx insure company logo blue brush stroke
- expat auto chiang mai logo with red wings
- mango scooter rental mascot logo character (2 variants)
- the dukes steaks ribs seafood pizza restaurant logo

#### Travel & Transportation (7 images)
Primary use: Getting around, travel pages
- happy group of travelers in back of pickup truck
- happy travelers in back of pickup truck group shot
- map of chiang mai city zones color coded
- map of chiang mai city zones google maps
- traveler looking at airport departure flight board (2 variants)
- white sign advertising accommodation pointing right

#### Lifestyle & Events (7 images)
Primary use: Things to do, lifestyle sections, formal events
- formal event group photo movie style backdrop (2 variants)
- sunset view with man silhouette arms outstretched beach
- yi peng festival hundreds of sky lanterns over temple night
- yi peng festival hundreds of sky lanterns over temple
- yi peng lantern festival night celebration in chiang mai (2 variants)

---

## PAGE-TO-IMAGE RECOMMENDATIONS (COMPLETED)

### ED Visa Pages (✅ COMPLETED)

**muay-thai-ed-visa-chiang-mai.html**
- Image 1: muay thai group photo in ring after training.webp
- Image 2: muay thai training session demo in chiang mai gym.webp

**thai-language-ed-visa-chiang-mai.html**
- Image 1: teacher pointing to whiteboard in thai language class.webp
- Image 2: thai language course teacher.webp

**hand-to-hand-combat-ed-visa-chiang-mai.html**
- Image 1: hand to hand combat training session exercise.webp
- Image 2: martial arts students group watching instructor performance.webp

**emergency-self-defence-ed-visa-chiang-mai.html**
- Image 1: women training with foam knives in self defense class.webp
- Image 2: two men sparring in martial arts gym.webp

**volunteer-non-o-visa-chiang-mai.html**
- Image 1: volunteers with children at school english camp.webp
- Image 2: formal event group photo movie style backdrop.webp

### Visa Hub Pages (✅ COMPLETED)

**pages/visas/index.html**
- Image 1: closeup of thailand visa sticker background.webp
- Image 2: education visas available now martial arts group.webp

**pages/visas/short-stay/index.html**
- Image 1: get your visa sorted today promo flyer graphics.webp
- Image 2: get your visa sorted today promo flyer graphics 2.webp

**pages/visas/long-stay/index.html**
- Image 1: education visas available now martial arts group.webp
- Image 2: formal event group photo movie style backdrop.webp

### Chiang Mai Pages (✅ COMPLETED)

**cost-of-living.html**
- Image 1: busy market stall colorful handmade bags.webp
- Image 2: auf der au garden german buffet restaurant sign wat ket.webp

**digital-nomads.html**
- Image 1: education visas available now martial arts group.webp
- Image 2: sunset view with man silhouette arms outstretched beach.webp

**getting-around.html**
- Image 1: happy travelers in back of pickup truck group shot.webp
- Image 2: map of chiang mai city zones color coded.webp

**healthcare.html**
- Image 1: wat phra singh golden buddha statue interior chiang mai.webp
- Image 2: close up of lighting oil lamps in a buddhist temple.webp

**insurance.html**
- Image 1: cnx insure company logo blue brush stroke.webp
- Image 2: chiang mai safe city public awareness logo.webp

**long-term-living.html**
- Image 1: chiang mai ambassador connector helper guru logo.webp
- Image 2: martial arts students group watching instructor performance.webp

**phones-and-banking.html**
- Image 1: mango scooter rental mascot logo character.webp
- Image 2: expat auto chiang mai logo with red wings.webp

**taxes.html**
- Image 1: thailand elite club membership card closeup.webp
- Image 2: formal event group photo movie style backdrop.webp

**things-to-do.html**
- Image 1: yi peng lantern festival night celebration in chiang mai.webp
- Image 2: muay thai training session demo in chiang mai gym.webp

**why-chiang-mai-base.html**
- Image 1: busy market stall colorful handmade bags.webp
- Image 2: doi inthanon twin pagodas sunset landscape.webp

**where-to-stay.html**
- Image 1: busy market stall colorful handmade bags.webp

---

## EXECUTION WORKFLOW

### Before Each Session

1. **Verify image files exist**
   ```bash
   ls -1 /c/ZZZWebsites/cmlocals/images/ | grep "[search-term]"
   ```

2. **Check updated image pool** (in case you've added new images)
   ```bash
   ls -1 /c/ZZZWebsites/cmlocals/images/ | wc -l
   ```

### Edit Workflow (For Each Page)

**Step 1: Read the target file**
- Use Read tool to access page content
- Identify H2 section headers
- Find closing article tag

**Step 2: Identify insertion points**
Use grep to find optimal locations:
```bash
# Find all section headers
grep -n "<h2>" /c/ZZZWebsites/cmlocals/pages/[path]/[file].html

# Find closing article tag
grep -n "</article>" /c/ZZZWebsites/cmlocals/pages/[path]/[file].html

# Find Related Guides section
grep -n "related-guides-section" /c/ZZZWebsites/cmlocals/pages/[path]/[file].html
```

**Step 3: Prepare edit replacement**
- Image 1: After 2-3 sections, before major H2 break
- Image 2: After final content section, before `</div></article>`

**Step 4: Copy the HTML pattern**
```html
<figure style="text-align: center; margin: 2rem 0;">
  <img
    src="/images/[EXACT-FILENAME].webp"
    alt="CMLocals Chiang Mai Locals [topic] [description]"
    style="max-width: 100%; height: auto; border-radius: 12px;"
  />
</figure>
```

**Step 5: Execute edit**
- Find unique string to match (5-10 lines of context)
- Replace with: existing content + figure block
- Verify filename exists in `/images/`

**Step 6: Commit after batch**
- Commit after 3-4 pages or one section
- Use consistent commit message format

### Insertion Point Rules

**Image 1 (Mid-Article):**
- After 2-3 major content sections (NOT at beginning)
- Before major section break (new `<h2>`)
- Typically after tables/data if section has them

**Image 2 (Near-End):**
- After final major content section
- BEFORE `</div></article>` closing tags
- NOT within visa-section, tools-section, or related-guides-section
- Usually before final `</div>` of article body

**Special Cases:**
- Pages with few sections: 1-2 images acceptable
- Checklist pages: NO images (per scope)
- Legal/disclaimer pages: NO images (per scope)

### Consistency Checklist

Before committing each batch:
- [ ] All images use `<figure>` wrapper (not bare `<img>`)
- [ ] All images centered (`text-align: center`)
- [ ] All images responsive (`max-width: 100%; height: auto`)
- [ ] All images have `border-radius: 12px` (NOT 10px, NOT 15px)
- [ ] All margins are `2rem 0` (NOT 1.5rem, NOT 2.5rem)
- [ ] All alt-text starts with `CMLocals Chiang Mai Locals`
- [ ] All alt-text is 10-15 words
- [ ] No broken image paths (file verified in `/images/`)
- [ ] Images placed between logical sections (not mid-paragraph)

### Responsive Behavior Verification

What users see across devices:
- **Desktop (1024px+):** Images ~600-700px wide, centered
- **Tablet (640-1023px):** Images scale to ~500px, maintain aspect ratio
- **Mobile (<640px):** Images scale to ~90% container width, full responsive
- **All screens:** No distortion, maintains aspect ratio

---

## NEXT SESSION CHECKLIST

When resuming work:

- [ ] 1. Check `/images/` folder for new/better images user added
- [ ] 2. Review this master document (you're reading it!)
- [ ] 3. Pick Task 6 (Immigration) or Task 6b (Culture)
- [ ] 4. Use page-to-image recommendations above
- [ ] 5. Follow exact edit workflow with HTML pattern
- [ ] 6. Verify consistency before each commit
- [ ] 7. Continue until all remaining pages have images

**Estimated remaining time:**
- Immigration pages (16): ~1.5-2 hours
- Culture pages (10): ~1-1.5 hours
- Can do both in one extended session if tokens available

---

## GIT HISTORY & COMMITS

**Initial Phase 3 Setup:**
- `e232f9c` - Add images to all Chiang Mai lifestyle pages

**Integration & Documentation:**
- `7283c70` - Add Phase 3 completion checklist with specs
- `499f2fb` - Integrate Phase 3 planning documents

**Current:** PAUSED - ready to resume with this master document

---

**Document Status:** Complete & Ready for Next Session ✅
**Last Verified:** 2026-03-07
**Scope:** All Phase 3 specs consolidated into single reference file
