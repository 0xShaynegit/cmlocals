# Visa Pages Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor all current visa pages from `oldpages/` into clean, updated, merged static HTML pages in `pages/`, following the CMLocals Thai Visa Hub 2026 PRD.

**Architecture:** Static HTML pages using the existing Kadence theme CSS (linked via `../css/`). Each page follows a standard template: SEO head, Kadence header/nav, hero, content area, footer, Chaty widget. Pages merge related oldpage sources and follow the PRD's structure rules, content rules, and internal linking guidelines.

**Tech Stack:** Static HTML, Kadence theme CSS (global.min.css, header.min.css, content.min.css, footer.min.css), WEBP images from `../images/`, no new frameworks.

---

## Shared Rules (Apply to Every Task)

These rules apply across all tasks. Read them before each task:

### Template Structure
Every page uses this shell (copied from index.html pattern):
```
<!DOCTYPE html>
<html lang="en-US">
<head>
  <!-- SEO meta, Open Graph, Schema.org -->
  <!-- CSS links: ../css/global.min.css, ../css/header.min.css, ../css/content.min.css, ../css/footer.min.css -->
  <!-- Inline Kadence CSS vars (copy from any oldpage head) -->
</head>
<body>
  <!-- #masthead header with nav -->
  <!-- .entry-hero hero band -->
  <!-- .content-area main content -->
  <!-- #colophon footer -->
  <!-- Chaty widget -->
</body>
</html>
```

### Navigation (exact order per PRD)
```html
<ul class="menu" id="primary-menu">
  <li><a href="../index.html">Home</a></li>
  <li><a href="thai-visa-stay-in-chiang-mai.html">Visa Overview</a></li>
  <li><a href="thai-visa-comparisons.html">Long Stay Visas</a></li>
  <li><a href="#">Short Stay and Tourist</a></li>
  <li><a href="#">Special Programs</a></li>
  <li><a href="#">Tools and Checklists</a></li>
  <li><a href="#">Permanent Residence</a></li>
  <li><a href="../contact.html">Contact</a></li>
</ul>
```
Note: Items without a target page yet use `#`. Update when those pages exist.

### Content Constraints (MUST follow)
- No em dashes anywhere
- No "Not affiliated with immigration, MFA, or Thai Privilege Card" language
- No "commission" or "affiliate" phrasing
- Replace with: "Helped hundreds of successful students and volunteers for the last 10 years."
- No change log section
- Calm, neutral, practical tone
- No invented visas, prices, or procedures

### Internal Links (per page)
Each visa page must include 3-4 contextual internal links:
- 1 link up to its hub (visa overview or comparisons page)
- 2-3 links sideways to related visa pages

### Images
- All images are WEBP, in `../images/`
- Filename pattern: `cmlocals chiang mai locals N.webp` (numbered)
- Use descriptive alt text based on filename + page context
- Check `images/` directory for actual filenames before writing `<img>` tags

### Footer Structure (per PRD)
```
Column 1: Brand + tagline + Facebook/WhatsApp links
Column 2: Visa topics
Column 3: Tools & Resources
Column 4: About & Policy
Column 5: Contact
```
No change log link. No affiliation disclaimer.

### Chaty Widget
Copy the Chaty widget HTML from any oldpage (bottom of body). Keep Facebook Messenger and WhatsApp links unchanged.

---

## Page Mapping

| Output file | Source files (in oldpages/) | Priority |
|---|---|---|
| `pages/thai-visa-stay-in-chiang-mai.html` | thai-visa-stay-in-chiang-mai.html + thai-visa-options-in-chiang-mai.html + thailand-visa.html | Hub page |
| `pages/thai-visa-comparisons.html` | thai-visa-comparisons.html | Comparison hub |
| `pages/ed-visa-thai-language.html` | ed-visa-thai-language.html + ed-visa.html | ED Thai Language |
| `pages/ed-visa-hand-to-hand-combat.html` | 1-year-ed-visa-hand-to-hand-combat.html + 1-year-muay-thai-ed-visa.html + hand-to-hand-combat.html + combat-class-chiang-mai.html | ED Combat |
| `pages/thai-non-o-volunteer-visa.html` | thai-non-o-volunteer-visa.html + non-o-volunteer-visa.html + non-o-visa.html | Non-O Volunteer |
| `pages/best-digital-nomad-visa.html` | best-digital-nomad-visa.html + digital-nomad-visa.html + digital-nomad-visa-thailand.html + digital-nomad.html | Digital Nomad/DTV |
| `pages/elite-visa.html` | elite-visa.html | Elite/Privilege |
| `pages/sak-yant-chiang-mai.html` | sak-yant-chiang-mai.html + sak-yant.html + sak-yant-designs-and-meanings.html | Sak Yant (no menu) |

---

## Task 1: Create Shared Page Template

**Goal:** Create a reusable HTML shell that all other tasks copy from.

**Files:**
- Create: `pages/_template.html`
- Reference: `oldpages/thai-non-o-volunteer-visa.html` (lines 1-220 for head/header, lines 410-570 for footer/chaty)

**Step 1: Read the head section of any oldpage**

Read `oldpages/thai-non-o-volunteer-visa.html` lines 1-220 to extract:
- Inline Kadence CSS vars (the large `<style id="kadence-global-inline-css">` block)
- CSS link tags (global.min.css, header.min.css, content.min.css, footer.min.css)
- Header HTML with nav, logo, social links

**Step 2: Read the footer section**

Read `oldpages/thai-non-o-volunteer-visa.html` lines 410-end to extract:
- Footer HTML with columns
- Chaty widget HTML

**Step 3: Write the template**

Create `pages/_template.html` with:
```html
<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport"/>
<title>PAGE_TITLE | CMLocals</title>
<meta content="PAGE_DESCRIPTION" name="description"/>
<meta content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large" name="robots"/>
<link href="https://www.cmlocals.com/PAGE_SLUG/" rel="canonical"/>
<meta content="en_US" property="og:locale"/>
<meta content="article" property="og:type"/>
<meta content="PAGE_TITLE" property="og:title"/>
<meta content="PAGE_DESCRIPTION" property="og:description"/>
<meta content="https://www.cmlocals.com/PAGE_SLUG/" property="og:url"/>
<meta content="Chiang Mai Locals" property="og:site_name"/>
<!-- [Kadence inline CSS block copied from oldpage] -->
<!-- [CSS links with ../css/ paths] -->
</head>
<body class="page-template content-style-unboxed transparent-header">
<!-- HEADER -->
<!-- HERO BAND -->
<!-- MAIN CONTENT -->
<!-- FOOTER -->
<!-- CHATY -->
</body>
</html>
```

Update the nav to match PRD nav order exactly (8 items listed above in Shared Rules).
Update the footer to match PRD footer structure (5 columns, no change log, no affiliation disclaimer).

**Step 4: Verify template looks correct**

Open `pages/_template.html` in a text editor and check:
- CSS links point to `../css/`
- Image links point to `../images/`
- Nav has 8 correct items
- Footer has 5 columns

---

## Task 2: Visa Overview Hub Page

**Source:** `oldpages/thai-visa-stay-in-chiang-mai.html` (primary) + `oldpages/thai-visa-options-in-chiang-mai.html` + `oldpages/thailand-visa.html`
**Output:** `pages/thai-visa-stay-in-chiang-mai.html`

**Step 1: Read all three source files**

Read each source to extract content. Focus on the `.entry-content` div in each. Key content to find:
- Overview of Thai visa types for Chiang Mai
- Descriptions of long-stay options
- Short-stay and tourist options
- Any Chiang Mai-specific advice

**Step 2: Plan merged content structure**

Following PRD rules, structure the merged page as:
1. Who this is for + At a glance summary (new intro section)
2. Long stay visa options overview (6 types per PRD, with PRD priority order)
3. Short stay options overview
4. Chiang Mai-specific notes
5. How to choose your visa (brief decision guide)
6. FAQ (3-5 questions pulled from existing content)
7. Contact CTA

**Step 3: Write the page**

Copy `pages/_template.html` and fill with merged, refactored content.

SEO meta:
- Title: "Thai Visa Guide for Chiang Mai 2026 | CMLocals"
- Description: "Complete guide to Thai visa options for living in Chiang Mai in 2026. Compare long-stay, short-stay and special program visas."
- Canonical: `https://www.cmlocals.com/thai-visa-stay-in-chiang-mai/`

Internal links to include:
- Link to `thai-visa-comparisons.html` (compare long-stay options)
- Link to `ed-visa-thai-language.html` (ED Thai language visa)
- Link to `thai-non-o-volunteer-visa.html` (volunteer visa)
- Link to `best-digital-nomad-visa.html` (digital nomad options)

Content rules:
- No em dashes
- No affiliation disclaimers
- 2026 context: mention longer visa-exempt stays for many nationalities as of 2026
- DTV mentioned as active option
- Use cautious wording for anything uncertain ("check official sources for current requirements")

Image: Use an appropriate image from `../images/` (check available files). Suggest `cmlocals chiang mai locals 1.webp` or similar Chiang Mai overview image.

**Step 4: Verify output**

Check that:
- Page opens correctly in browser
- Nav is correct
- No em dashes in content
- 4 internal links present
- Images load (paths correct)

---

## Task 3: Long Stay Visa Comparison Hub

**Source:** `oldpages/thai-visa-comparisons.html`
**Output:** `pages/thai-visa-comparisons.html`

**Step 1: Read source file**

Read `oldpages/thai-visa-comparisons.html` - extract the content section comparing visa options.

**Step 2: Plan merged content structure**

1. Who this is for + At a glance (intro)
2. Comparison table or card grid: ED, Volunteer, DTV, LTR, Retirement, Marriage (in PRD priority order)
3. Key factors to consider (duration, cost, requirements, flexibility)
4. Chiang Mai-specific context
5. FAQ
6. Contact CTA

Card order per PRD:
1. Education (ED visa) - link to ed-visa-thai-language.html and ed-visa-hand-to-hand-combat.html
2. Volunteer (Non-O) - link to thai-non-o-volunteer-visa.html
3. DTV (Destination Thailand Visa) - link to best-digital-nomad-visa.html
4. LTR (Long-Term Resident)
5. Retirement (Non-OA) - with disclaimer: "General advice only - Our in-depth knowledge base focuses on ED, Volunteer, DTV, and LTR visas."
6. Marriage/Family (Non-O) - with same disclaimer

**Step 3: Write the page**

SEO meta:
- Title: "Thai Visa Comparisons: Long Stay Options for Chiang Mai 2026 | CMLocals"
- Description: "Compare long-stay Thai visa options for Chiang Mai in 2026. Education, Volunteer, DTV, LTR, Retirement and Marriage visas compared."
- Canonical: `https://www.cmlocals.com/thai-visa-comparisons/`

Internal links:
- Link to `thai-visa-stay-in-chiang-mai.html` (visa overview hub)
- Link to `ed-visa-thai-language.html`
- Link to `thai-non-o-volunteer-visa.html`
- Link to `best-digital-nomad-visa.html`

**Step 4: Verify output**

---

## Task 4: ED Visa Thai Language Page

**Source:** `oldpages/ed-visa-thai-language.html` (primary visa page) + `oldpages/ed-visa.html` (information/archive page)
**Output:** `pages/ed-visa-thai-language.html`

**Step 1: Read both source files**

Read `oldpages/ed-visa-thai-language.html` - this is the main visa page with:
- School options and pricing
- Application process (steps 1-8)
- Benefits list
- FAQ questions

Read `oldpages/ed-visa.html` - this is the archive/category page listing ED visa options. Extract any additional explanatory content.

**Step 2: Plan merged content structure**

Per PRD merge rule: visa page URL is canonical, information page enriches it.

1. **Who this is for** - people wanting to stay 1 year+ in Chiang Mai, learn Thai, integrate into community
2. **At a glance** - 1 year (3-month extensions), ~35,000-50,000 baht, 2x2hrs/week class
3. **Eligibility** - most nationalities (note: some nationalities apply from home embassy)
4. **What you get** - list benefits (Thai license, cheaper rates, community integration, etc.)
5. **School options in Chiang Mai** - 3 school options (Nimman, Ruam Chok, Night Bazaar) with prices where available
6. **Required documents** - passport, photos, fees
7. **Application steps** - numbered process (outside Thailand path vs inside Thailand changeover)
8. **Chiang Mai specifics** - Immigration visits every 3 months, half-day affair, re-entry permit option
9. **FAQ** - 5-8 questions from existing content
10. **Contact CTA**

Content to update for 2026:
- Prices shown are approximate - use "approximately" language
- Reference that 2026 immigration rules may affect process - check current requirements
- Remove any "2023" or "2024" year references, update to 2026

**Step 3: Write the page**

SEO meta:
- Title: "ED Visa Thai Language Chiang Mai 2026 | CMLocals"
- Description: "Get a 1-year ED visa to learn Thai language in Chiang Mai. Schools, costs, application steps and 2026 requirements explained."
- Canonical: `https://www.cmlocals.com/ed-visa-thai-language/`

Internal links:
- Link to `thai-visa-comparisons.html` (compare all long-stay visa options)
- Link to `ed-visa-hand-to-hand-combat.html` (alternative ED visa via combat)
- Link to `thai-non-o-volunteer-visa.html` (alternative if you want more community involvement)
- Link to `thai-visa-stay-in-chiang-mai.html` (full visa overview)

**Step 4: Verify**

---

## Task 5: ED Visa Hand-to-Hand Combat Page

**Source:**
- `oldpages/1-year-ed-visa-hand-to-hand-combat.html` (primary visa page)
- `oldpages/1-year-muay-thai-ed-visa.html` (related muay thai variant)
- `oldpages/hand-to-hand-combat.html` (information page)
- `oldpages/combat-class-chiang-mai.html` (information about the class)

**Output:** `pages/ed-visa-hand-to-hand-combat.html`

**Step 1: Read all source files**

Read each file's content section. Note which information appears in the "visa" pages vs "information" pages. The visa pages take priority.

**Step 2: Plan merged content structure**

1. **Who this is for** - people wanting 1-year visa with interest in martial arts / self-defense
2. **At a glance** - 1 year, what's included, class frequency
3. **What the class covers** - hand-to-hand combat / emergency self-defense / Muay Thai context
4. **Eligibility**
5. **Required documents**
6. **Application steps**
7. **Chiang Mai specifics** - where classes are held, schedule
8. **FAQ**
9. **Contact CTA**

Note: Page may cover both "hand-to-hand combat" and "Muay Thai ED visa" variants since sources overlap. Merge sensibly.

**Step 3: Write the page**

SEO meta:
- Title: "ED Visa Hand-to-Hand Combat Chiang Mai 2026 | CMLocals"
- Description: "1-year ED visa through hand-to-hand combat or Muay Thai classes in Chiang Mai. Requirements, costs and application steps."
- Canonical: `https://www.cmlocals.com/ed-visa-hand-to-hand-combat/`

Internal links:
- Link to `thai-visa-comparisons.html`
- Link to `ed-visa-thai-language.html` (alternative ED route)
- Link to `thai-non-o-volunteer-visa.html`
- Link to `thai-visa-stay-in-chiang-mai.html`

**Step 4: Verify**

---

## Task 6: Thai Non-O Volunteer Visa Page

**Source:**
- `oldpages/thai-non-o-volunteer-visa.html` (primary visa page - most detailed)
- `oldpages/non-o-volunteer-visa.html` (secondary)
- `oldpages/non-o-visa.html` (general Non-O info)

**Output:** `pages/thai-non-o-volunteer-visa.html`

**Step 1: Read all source files**

From `thai-non-o-volunteer-visa.html`, extract (lines ~307-410):
- Step-by-step process (8 steps from Laos visa run through work permit)
- Document list (passport photos, degrees, medical cert, etc.)
- FAQ questions
- Benefits

From the other two files, extract any additional context.

**Step 2: Plan merged content structure**

1. **Who this is for** - people who want to volunteer with an NPO in Chiang Mai for 1+ years
2. **At a glance** - 1 year + renewable, includes work permit, NPO-based
3. **Benefits** - list (work permit, 3+ year renewability, multi-entry option)
4. **Eligibility**
5. **The volunteering arrangement** - what NPO means, how it works
6. **Required documents** - detailed list (passport, photos, degrees, medical cert from hospital, etc.)
7. **Application steps** - 8-step process (document prep, Laos visa run, return, work permit, immigration visit)
8. **Renewals** - no need to leave Thailand for renewal, renewable 3+ years
9. **Chiang Mai specifics** - Immigration co-visit with NPO
10. **FAQ**
11. **Contact CTA**

Content rule: Replace "commission" with "Helped hundreds of successful students and volunteers for the last 10 years."

**Step 3: Write the page**

SEO meta:
- Title: "Thai Non-O Volunteer Visa Chiang Mai 2026 | CMLocals"
- Description: "Get a 1-year Thai Non-O Volunteer Visa with work permit in Chiang Mai. Step-by-step process, documents and NPO arrangement explained."
- Canonical: `https://www.cmlocals.com/thai-non-o-volunteer-visa/`

Internal links:
- Link to `thai-visa-comparisons.html`
- Link to `ed-visa-thai-language.html` (alternative long-stay via learning)
- Link to `best-digital-nomad-visa.html` (if remote work is the goal)
- Link to `thai-visa-stay-in-chiang-mai.html`

**Step 4: Verify**

---

## Task 7: Digital Nomad / DTV Page

**Source:**
- `oldpages/best-digital-nomad-visa.html` (primary - likely most content-rich)
- `oldpages/digital-nomad-visa.html`
- `oldpages/digital-nomad-visa-thailand.html`
- `oldpages/digital-nomad.html`

**Output:** `pages/best-digital-nomad-visa.html`

**Step 1: Read all source files**

Focus on best-digital-nomad-visa.html first. Note any DTV-specific content across all files.

**Step 2: Plan merged content structure**

The DTV (Destination Thailand Visa) is a 2024/2025 addition - may have limited coverage in old pages.

1. **Who this is for** - remote workers, freelancers, digital nomads wanting to base in Chiang Mai
2. **At a glance** - DTV: 5-year validity, 180-day stays; other options compared
3. **DTV overview** - what it is, who qualifies, key requirements (180-day income threshold, etc.)
4. **Comparing options for digital nomads** - DTV vs tourist/visa-exempt vs Elite/Privilege
5. **Chiang Mai as a digital nomad base** - brief practical context
6. **How to apply** - general steps, refer to official sources for current details
7. **FAQ**
8. **Contact CTA**

Content rules for DTV:
- DTV is real and active as of 2026
- Be factual but cautious: "Requirements and processing times can change - verify current details at the Thai embassy or consulate"
- Do not invent specific DTV prices or exact rules if not in source material

**Step 3: Write the page**

SEO meta:
- Title: "Best Visa for Digital Nomads in Chiang Mai 2026 | CMLocals"
- Description: "Compare visa options for digital nomads in Chiang Mai 2026 including the Destination Thailand Visa (DTV) and other long-stay routes."
- Canonical: `https://www.cmlocals.com/best-digital-nomad-visa/`

Internal links:
- Link to `thai-visa-comparisons.html`
- Link to `thai-visa-stay-in-chiang-mai.html`
- Link to `elite-visa.html` (premium option for longer stays)
- Link to `thai-non-o-volunteer-visa.html` (if interested in community involvement)

**Step 4: Verify**

---

## Task 8: Thailand Privilege/Elite Visa Page

**Source:** `oldpages/elite-visa.html`
**Output:** `pages/elite-visa.html`

**Step 1: Read source file**

Read `oldpages/elite-visa.html` content section.

**Step 2: Plan content structure**

1. **Who this is for** - people wanting premium long-stay with concierge services
2. **At a glance** - various tiers, 5-20 years, premium pricing
3. **Membership tiers** (whatever is in the source - don't invent tiers)
4. **Benefits** - airport services, VIP immigration, no mandatory classes
5. **How to apply** - refer to Thailand Privilege Card official source
6. **Chiang Mai notes**
7. **FAQ**
8. **Contact CTA**

Content rule: "General advice only - Our in-depth knowledge base focuses on ED, Volunteer, DTV, and LTR visas." (This is a Priority 2 page.)

**Step 3: Write the page**

SEO meta:
- Title: "Thailand Privilege Visa (Elite Visa) Chiang Mai 2026 | CMLocals"
- Description: "Overview of the Thailand Privilege Visa (formerly Elite Visa) for long-stay in Chiang Mai. Tiers, costs and how to apply."
- Canonical: `https://www.cmlocals.com/elite-visa/`

Internal links:
- Link to `thai-visa-comparisons.html`
- Link to `best-digital-nomad-visa.html`
- Link to `thai-visa-stay-in-chiang-mai.html`

**Step 4: Verify**

---

## Task 9: Sak Yant Page (No Homepage Links)

**Source:**
- `oldpages/sak-yant-chiang-mai.html` (primary)
- `oldpages/sak-yant.html`
- `oldpages/sak-yant-designs-and-meanings.html`
- `oldpages/etiquette-when-visiting-a-sak-yant-monk.html`
- `oldpages/meaning.html` (possibly sak yant meanings)
- `oldpages/tattoo.html`

**Output:** `pages/sak-yant-chiang-mai.html`

**IMPORTANT:** This page must NOT be linked from:
- The homepage
- The main navigation menu

It CAN be linked from other content pages where appropriate.

**Step 1: Read source files**

Read each source file's content section. Primary focus on sak-yant-chiang-mai.html.

**Step 2: Plan merged content structure**

1. **What is Sak Yant** - brief intro
2. **Who gets Sak Yant in Chiang Mai**
3. **Finding a Sak Yant monk in Chiang Mai**
4. **Etiquette and preparation** - from etiquette source
5. **Designs and meanings** - from designs source
6. **What to expect** - the experience
7. **FAQ**

This is a special interest page, not a visa page. Tone should be respectful and informational.

**Step 3: Write the page**

SEO meta:
- Title: "Sak Yant Tattoo Chiang Mai 2026 | CMLocals"
- Description: "Guide to getting a Sak Yant tattoo in Chiang Mai. Finding a monk, etiquette, designs and what to expect."
- Canonical: `https://www.cmlocals.com/sak-yant-chiang-mai/`

Internal links (within content pages, not nav):
- This page links back to `thai-visa-stay-in-chiang-mai.html` or general Chiang Mai content
- Other pages can link here if contextually appropriate

**Step 4: Verify - confirm page has no link from nav or homepage**

---

## Task 10: Final Cross-Linking Check

After all pages are written:

**Step 1: Check all internal links resolve**

For each page in `pages/`, verify that every `href` in anchor tags points to a file that exists either in `pages/` or as `../index.html`.

```bash
grep -h 'href="[^h#]' pages/*.html | grep -v 'http' | sort -u
```

**Step 2: Fix any broken links**

If any links point to nonexistent files, either:
- Update the href to the correct filename
- Use `#` as a placeholder with a TODO comment

**Step 3: Verify Sak Yant is not in nav**

```bash
grep -l "sak-yant" pages/*.html | xargs grep "primary-menu"
```

If sak-yant appears in any primary-menu nav, remove it.

**Step 4: Spot-check content rules**

```bash
# Check for em dashes
grep -rn "—\|&mdash;" pages/*.html

# Check for banned phrases
grep -rn "affiliated with immigration\|commission\|affiliate" pages/*.html
```

Fix any violations found.

---

## Execution Notes

**Page template reuse:** Once Task 1 creates `_template.html`, Tasks 2-9 should copy it and fill the content. Do NOT copy from oldpages HTML wholesale - the oldpage CSS and WordPress markup should NOT be in the new pages. The new pages use only the Kadence CSS vars block + CSS file links, with clean semantic HTML for content.

**Content extraction strategy:** When reading oldpages, focus only on the `.entry-content` div area. Skip the 200+ lines of WordPress CSS. The useful content starts around line 300-320 in most oldpages.

**Image selection:** Since images are numbered (`cmlocals chiang mai locals N.webp`) without descriptive names, pick images by number range:
- Lower numbers (1-30) tend to be earlier/more general Chiang Mai images
- Check the `_raw/images/` directory if it contains original filenames for context
- Use the image that best fits the page context based on surrounding content in oldpages

**2026 updates to make:**
- Visa exempt stays: many nationalities now get 60 days (updated from 30) as of 2025/2026
- DTV: active and real, 5-year multi-entry, 180 days per stay
- Reference "check current official requirements" for anything date-sensitive
- Remove specific year references like "2023 rules" or "2024 process" - use "current" or "2026"

---

Plan complete and saved to `docs/plans/2026-02-20-visa-pages-refactor.md`.
