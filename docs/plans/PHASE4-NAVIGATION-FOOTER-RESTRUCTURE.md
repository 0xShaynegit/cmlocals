# Phase 4: Navigation & Footer Restructuring — Mega Menu + ED Visa Priority

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to execute this plan task-by-task.

**Goal:** Overhaul header navigation with mega menu (desktop) + accordion drawer (mobile) featuring all 60+ pages organized by category, and restructure footer with ED Visas as left-column priority.

**Architecture:**
- Header: Responsive mega menu with 6 category sections (ED Visas, Chiang Mai, Visa Guides, Immigration, Culture, Tools). Desktop displays categorized grid dropdown; mobile displays accordion drawer with smooth expand/collapse.
- Footer: 6-column layout with ED Visas prominent left column, followed by Chiang Mai, Visa Guides, Immigration, Culture/Tools, Contact. Links organized hierarchically.
- Mobile-first CSS: Stack footer vertically on mobile with ED Visas expanding first; horizontal grid on desktop.

**Tech Stack:** HTML5 semantic nav, vanilla CSS (no JS required for mobile accordion via details/summary), CSS custom properties for design tokens.

---

## Current State

### Header (Status: Needs Overhaul)
Current structure:
```
Logo | Visa Guides | Chiang Mai | Tools | About & Legal | Contact
```

Issues:
- ED Visas not prominent (buried in Tools)
- Only 5 top-level links, 60+ pages hidden
- No accordion drawer on mobile
- Mobile nav collapse unclear

### Footer (Status: Needs Restructuring)
Current structure:
```
| Visa Guides | Tools & Resources | About & Legal | Contact |
```

Issues:
- ED Visas scattered (ED Visa Guide in Tools, specific programs buried)
- No dedicated Education column
- Chiang Mai pages not listed (only in main content links)
- Legal links take up space

---

## Inventory: Pages by Category

### Category 1: ED VISAS (5 pages) — LEFT COLUMN, PRIORITY
1. Muay Thai ED Visa
2. Thai Language ED Visa
3. Hand-to-Hand Combat ED Visa
4. Emergency Self-Defence ED Visa
5. Volunteer Non-O Visa

### Category 2: CHIANG MAI (11 pages)
1. Chiang Mai Hub
2. Why Chiang Mai Base
3. Where to Stay
4. Long-Term Living
5. Things to Do
6. Digital Nomads
7. Cost of Living
8. Phones & Banking
9. Getting Around
10. Healthcare
11. Insurance
12. Taxes

### Category 3: VISA GUIDES (14 pages)
**Short-Stay:**
1. Visa Exempt Entry
2. Tourist Visa
3. Visa on Arrival
4. Visa Extensions
5. Border Runs
6. DTV (Destination Thailand Visa)

**Long-Stay:**
7. Retirement Visa
8. Business Visa (Non-B)
9. Marriage Visa (Non-O)
10. LTR (Long-Term Resident)
11. Thailand Privilege Visa (Elite)

**Guides:**
12. Which Visa?
13. Visa Comparisons
14. Visa Stay Chiang Mai
15. Visa Options Chiang Mai
16. Extension vs Re-Entry
17. Entry Requirements 2026

### Category 4: IMMIGRATION (18 pages)
1. 90-Day Reporting
2. TM30 Address Reporting
3. Overstay Penalties
4. Document Requirements
5. Financial Requirements
6. Visa Extensions
7. Re-Entry Permits
8. Address Change
9. Land Border vs Air Entry
10. Entry Strategy Guide
11. Queue Strategy
12. Common Rejections
13. Blacklist Status
14. Visa Border Runs
15. Legal Rights
16. Immigration Best Practices
17. Thailand Digital Arrival Card
18. Immigration Hub

### Category 5: CULTURE (10 pages)
1. Culture Hub
2. Customs & Traditions
3. Festivals & Events
4. Thai Culture & Etiquette
5. Temple Etiquette
6. Sak Yant Chiang Mai
7. Sak Yant Designs & Meanings
8. Sak Yant Getting
9. Etiquette When Visiting Sak Yant Monk
10. Thai Food Culture

### Category 6: TOOLS (2 pages)
1. Tools Hub
2. (Checklists, Calculators, Quizzes as sublinks)

**Total Pages:** 60+ across 6 categories

---

## Implementation Tasks

### Task 1: Design Header HTML Structure & Mega Menu Markup

**Files:**
- Modify: `index.html` header section (lines ~50-150, approx)
- Modify: All other pages' header sections (same structure)

**Step 1: Design mega menu HTML**

Create responsive header structure with:
- Logo/home link (left)
- 6 category nav items (center)
- Mega menu dropdowns (desktop only, display: none on mobile)
- Mobile hamburger toggle (mobile only)
- Mobile accordion drawer (mobile only, initially hidden)

**HTML structure:**

```html
<header class="site-header">
  <div class="header-container">
    <!-- Logo -->
    <a href="/" class="logo">CMLocals</a>

    <!-- Desktop Mega Menu -->
    <nav class="nav-primary desktop-only">
      <a href="/pages/ed-visas/" class="nav-link has-dropdown">
        ED Visas
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- 5 ED visa links in grid -->
        <div class="dropdown-section">
          <h3>ED Visa Programs</h3>
          <ul>
            <li><a href="/pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai</a></li>
            <li><a href="/pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language</a></li>
            <li><a href="/pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat</a></li>
            <li><a href="/pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Self-Defence</a></li>
            <li><a href="/pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O</a></li>
          </ul>
        </div>
        <div class="dropdown-section">
          <a href="/pages/ed-visas/" class="section-link">All ED Visas →</a>
        </div>
      </div>

      <a href="/pages/chiang-mai/" class="nav-link has-dropdown">
        Chiang Mai
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- Similar structure with 11 Chiang Mai links -->
      </div>

      <a href="/pages/visas/" class="nav-link has-dropdown">
        Visa Guides
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- Similar structure with 14 visa guide links -->
      </div>

      <a href="/pages/immigration/" class="nav-link has-dropdown">
        Immigration
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- Similar structure with 18 immigration links -->
      </div>

      <a href="/pages/culture/" class="nav-link has-dropdown">
        Culture
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- Similar structure with 10 culture links -->
      </div>

      <a href="/pages/tools/" class="nav-link has-dropdown">
        Tools
      </a>
      <div class="dropdown-menu mega-menu">
        <!-- 2 tools links -->
      </div>
    </nav>

    <!-- Mobile Menu Toggle -->
    <button class="mobile-menu-toggle" aria-label="Toggle menu">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </div>

  <!-- Mobile Accordion Drawer (hidden by default) -->
  <nav class="nav-mobile mobile-only" id="mobile-nav">
    <details class="nav-accordion">
      <summary>ED Visas (5)</summary>
      <ul>
        <li><a href="/pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai ED Visa</a></li>
        <li><a href="/pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language ED Visa</a></li>
        <li><a href="/pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat ED Visa</a></li>
        <li><a href="/pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Emergency Self-Defence ED Visa</a></li>
        <li><a href="/pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O Visa</a></li>
      </ul>
    </details>
    <!-- Repeat for other 5 categories -->
  </nav>
</header>
```

**Step 2: Verify HTML structure**
- All 60+ pages reachable from nav
- Mega menu sections organized by category
- Mobile accordion with all categories
- Semantic nav element used
- ARIA labels for accessibility

**Step 3: Commit**

```bash
git add index.html pages/**/*.html
git commit -m "feat: add mega menu header structure with mobile accordion (all 60+ pages linked)"
```

---

### Task 2: Style Mega Menu (Desktop) with CSS

**Files:**
- Modify: `styles/main.css` (or appropriate CSS file)
- Add: Header/nav-specific rules under `/* NAVIGATION */` section

**Step 1: Write mega menu desktop CSS**

```css
/* NAVIGATION: Mega Menu Desktop */

.site-header {
  background: white;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 4rem;
}

.logo {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: bold;
  color: #4F46E5; /* Primary indigo */
  text-decoration: none;
}

.nav-primary {
  display: flex;
  gap: 2rem;
  flex: 1;
  justify-content: center;
}

.nav-link {
  position: relative;
  color: #111827;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.5rem 0;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s;
}

.nav-link:hover,
.nav-link.active {
  border-bottom-color: #4F46E5;
}

.nav-link.has-dropdown {
  cursor: pointer;
}

/* Mega Menu Dropdown */
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  border: 1px solid rgba(0,0,0,0.1);
  border-radius: 8px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
  padding: 2rem;
  min-width: 600px;
  display: none;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s, visibility 0.2s;
  margin-top: 0.5rem;
}

.nav-link.has-dropdown:hover + .dropdown-menu,
.dropdown-menu:hover {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 2rem;
  opacity: 1;
  pointer-events: auto;
}

.dropdown-section {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.dropdown-section h3 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #4F46E5;
  font-weight: 600;
  margin: 0;
}

.dropdown-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dropdown-section li a {
  color: #374151;
  text-decoration: none;
  font-size: 0.9rem;
  line-height: 1.6;
  transition: color 0.2s;
}

.dropdown-section li a:hover {
  color: #4F46E5;
}

.section-link {
  color: #4F46E5 !important;
  font-weight: 600;
  padding-top: 0.5rem;
  border-top: 1px solid rgba(0,0,0,0.1);
}

/* Mobile Menu Toggle */
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  gap: 4px;
}

.mobile-menu-toggle span {
  width: 24px;
  height: 2px;
  background: #111827;
  transition: all 0.3s;
}

.mobile-menu-toggle.active span:nth-child(1) {
  transform: rotate(45deg) translate(8px, 8px);
}

.mobile-menu-toggle.active span:nth-child(2) {
  opacity: 0;
}

.mobile-menu-toggle.active span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -7px);
}

/* Desktop Only */
@media (min-width: 1024px) {
  .desktop-only {
    display: flex !important;
  }

  .mobile-only {
    display: none !important;
  }
}
```

**Step 2: Test mega menu**
- Hover over each nav item, dropdown appears
- All 60 pages visible in dropdown grid
- Section titles and links properly styled
- No layout breaks

**Step 3: Commit**

```bash
git add styles/main.css
git commit -m "feat: style mega menu dropdown with organized category grid"
```

---

### Task 3: Style Mobile Accordion Drawer with CSS

**Files:**
- Modify: `styles/main.css` (add mobile accordion styles)

**Step 1: Write mobile accordion CSS**

```css
/* NAVIGATION: Mobile Accordion Drawer */

@media (max-width: 1023px) {
  .mobile-menu-toggle {
    display: flex;
  }

  .nav-primary {
    display: none;
  }

  .nav-mobile {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border-bottom: 1px solid rgba(0,0,0,0.1);
    flex-direction: column;
    max-height: calc(100vh - 4rem);
    overflow-y: auto;
  }

  .nav-mobile.open {
    display: flex;
  }

  .nav-accordion {
    border-bottom: 1px solid rgba(0,0,0,0.1);
    cursor: pointer;
  }

  .nav-accordion summary {
    padding: 1rem;
    font-weight: 600;
    color: #111827;
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    user-select: none;
    transition: background 0.2s;
  }

  .nav-accordion summary:hover {
    background: rgba(79, 70, 229, 0.05);
  }

  .nav-accordion summary::after {
    content: '▼';
    font-size: 0.75rem;
    transition: transform 0.3s;
  }

  .nav-accordion[open] summary::after {
    transform: rotate(180deg);
  }

  .nav-accordion ul {
    list-style: none;
    padding: 0;
    margin: 0;
    background: rgba(79, 70, 229, 0.02);
  }

  .nav-accordion li {
    border-bottom: 1px solid rgba(0,0,0,0.05);
  }

  .nav-accordion li a {
    display: block;
    padding: 0.75rem 1rem;
    padding-left: 2rem;
    color: #374151;
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.2s, background 0.2s;
  }

  .nav-accordion li a:active {
    background: rgba(79, 70, 229, 0.1);
    color: #4F46E5;
  }
}
```

**Step 2: Add mobile toggle JavaScript**

Minimal JS for hamburger toggle (add to scripts section):

```html
<script>
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.mobile-menu-toggle');
  const nav = document.getElementById('mobile-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('active');
      nav.classList.toggle('open');
    });

    // Close menu when link clicked
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        toggle.classList.remove('active');
        nav.classList.remove('open');
      });
    });
  }
});
</script>
```

**Step 3: Test mobile accordion**
- Hamburger icon opens drawer
- Accordions expand/collapse smoothly
- Each category shows all links
- Links are tappable (44px+ touch targets)
- Menu closes when link is tapped

**Step 4: Commit**

```bash
git add styles/main.css
git commit -m "feat: add mobile accordion drawer with smooth expand/collapse"
```

---

### Task 4: Restructure Footer HTML — ED Visas LEFT Column Priority

**Files:**
- Modify: `index.html` footer section (~lines 1800+, approx)
- Modify: All page templates with footer includes

**Step 1: Design new footer HTML structure**

```html
<footer class="site-footer">
  <div class="footer-container">

    <!-- Column 1: ED VISAS (LEFT, PRIORITY) -->
    <div class="footer-col">
      <h3 class="footer-title">ED Visas</h3>
      <ul class="footer-links">
        <li><a href="/pages/ed-visas/">All ED Visas</a></li>
        <li><a href="/pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai</a></li>
        <li><a href="/pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language</a></li>
        <li><a href="/pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat</a></li>
        <li><a href="/pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Self-Defence</a></li>
        <li><a href="/pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O</a></li>
      </ul>
    </div>

    <!-- Column 2: CHIANG MAI -->
    <div class="footer-col">
      <h3 class="footer-title">Chiang Mai Life</h3>
      <ul class="footer-links">
        <li><a href="/pages/chiang-mai/">Overview</a></li>
        <li><a href="/pages/chiang-mai/why-chiang-mai-base.html">Why Base Here</a></li>
        <li><a href="/pages/chiang-mai/where-to-stay.html">Where to Stay</a></li>
        <li><a href="/pages/chiang-mai/long-term-living.html">Long-Term Living</a></li>
        <li><a href="/pages/chiang-mai/things-to-do.html">Things to Do</a></li>
        <li><a href="/pages/chiang-mai/digital-nomads.html">Digital Nomads</a></li>
        <li><a href="/pages/chiang-mai/cost-of-living.html">Cost of Living</a></li>
        <li><a href="/pages/chiang-mai/phones-and-banking.html">Phones & Banking</a></li>
        <li><a href="/pages/chiang-mai/getting-around.html">Getting Around</a></li>
        <li><a href="/pages/chiang-mai/healthcare.html">Healthcare</a></li>
        <li><a href="/pages/chiang-mai/insurance.html">Insurance</a></li>
        <li><a href="/pages/chiang-mai/taxes.html">Taxes</a></li>
      </ul>
    </div>

    <!-- Column 3: VISA GUIDES -->
    <div class="footer-col">
      <h3 class="footer-title">Visa Guides</h3>
      <ul class="footer-links">
        <li><a href="/pages/visas/">All Visas</a></li>
        <li><a href="/pages/visas/short-stay/">Short-Stay</a></li>
        <li><a href="/pages/visas/short-stay/visa-exempt-entry.html">Visa Exempt</a></li>
        <li><a href="/pages/visas/short-stay/tourist-visa.html">Tourist Visa</a></li>
        <li><a href="/pages/visas/short-stay/visa-on-arrival.html">Visa on Arrival</a></li>
        <li><a href="/pages/visas/short-stay/dtv-destination-thailand-visa-thai-visa-advice-chiang-mai-cmlocals.html">DTV</a></li>
        <li><a href="/pages/visas/long-stay/">Long-Stay</a></li>
        <li><a href="/pages/visas/long-stay/retirement-visa-thai-visa-advice-chiang-mai-cmlocals.html">Retirement</a></li>
        <li><a href="/pages/visas/long-stay/business-visa-non-b-thai-visa-advice-chiang-mai-cmlocals.html">Business (Non-B)</a></li>
        <li><a href="/pages/visas/long-stay/marriage-visa-non-o-thai-visa-advice-chiang-mai-cmlocals.html">Marriage (Non-O)</a></li>
        <li><a href="/pages/visas/long-stay/ltr-long-term-resident-visa-thai-visa-advice-chiang-mai-cmlocals.html">LTR</a></li>
      </ul>
    </div>

    <!-- Column 4: IMMIGRATION -->
    <div class="footer-col">
      <h3 class="footer-title">Immigration</h3>
      <ul class="footer-links">
        <li><a href="/pages/immigration/">All Immigration</a></li>
        <li><a href="/pages/immigration/90-day-reporting.html">90-Day Reporting</a></li>
        <li><a href="/pages/immigration/tm30-address-reporting.html">TM30 Registration</a></li>
        <li><a href="/pages/immigration/overstay-penalties.html">Overstay Penalties</a></li>
        <li><a href="/pages/immigration/document-requirements.html">Documents</a></li>
        <li><a href="/pages/immigration/re-entry-permits.html">Re-Entry Permits</a></li>
        <li><a href="/pages/immigration/land-border-vs-air-entry.html">Entry Strategy</a></li>
        <li><a href="/pages/immigration/thailand-digital-arrival-card.html">Digital Arrival</a></li>
      </ul>
    </div>

    <!-- Column 5: CULTURE & TOOLS -->
    <div class="footer-col">
      <h3 class="footer-title">Culture & Tools</h3>
      <ul class="footer-links">
        <li><a href="/pages/culture/">Culture Guide</a></li>
        <li><a href="/pages/culture/sak-yant-chiang-mai.html">Sak Yant</a></li>
        <li><a href="/pages/culture/festivals-events-chiang-mai.html">Festivals</a></li>
        <li><a href="/pages/culture/thai-food-culture.html">Thai Food</a></li>
        <li><a href="/pages/tools/">Tools Hub</a></li>
        <li><a href="/pages/checklists/">Checklists</a></li>
      </ul>
    </div>

    <!-- Column 6: CONTACT -->
    <div class="footer-col">
      <h3 class="footer-title">Contact</h3>
      <ul class="footer-links">
        <li><a href="https://wa.me/66801202074" target="_blank">WhatsApp</a></li>
        <li><a href="https://m.me/cmlocals" target="_blank">Messenger</a></li>
        <li><a href="https://www.facebook.com/chiangmailocals" target="_blank">Facebook</a></li>
      </ul>
      <div class="footer-legal">
        <p><a href="/pages/about.html">About CMLocals</a></p>
        <p><a href="/pages/privacy-policy.html">Privacy Policy</a></p>
      </div>
    </div>

  </div>

  <!-- Bottom Bar -->
  <div class="footer-bottom">
    <p>&copy; 2026 CMLocals. Independent information hub for Thailand visa & Chiang Mai living.</p>
  </div>
</footer>
```

**Step 2: Verify footer structure**
- ED Visas column is first (left position)
- All 60+ pages linked in footer
- Chiang Mai column has all 11 pages
- Visa guides organized (short-stay, long-stay)
- Immigration key pages listed
- Culture/tools consolidated
- Contact info present

**Step 3: Commit**

```bash
git add index.html pages/**/*.html
git commit -m "feat: restructure footer with ED Visas as left column priority, add all 60+ pages"
```

---

### Task 5: Style Footer with CSS — Responsive Grid

**Files:**
- Modify: `styles/main.css` (add footer section)

**Step 1: Write footer CSS**

```css
/* FOOTER: Layout & Styling */

.site-footer {
  background: #0D1275; /* Dark footer */
  color: rgba(255, 255, 255, 0.92);
  padding: 3rem 1rem 1rem;
  margin-top: 6rem;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 3rem;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.footer-title {
  font-size: 0.95rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid rgba(79, 70, 229, 0.5);
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.75);
  text-decoration: none;
  font-size: 0.9rem;
  line-height: 1.4;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: rgba(79, 70, 229, 1);
}

.footer-legal {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-legal p {
  margin: 0.5rem 0;
}

.footer-legal a {
  color: rgba(255, 255, 255, 0.65) !important;
  font-size: 0.85rem;
}

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  padding: 1rem 0;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
}

/* Mobile Footer */
@media (max-width: 640px) {
  .footer-container {
    grid-template-columns: 1fr;
    gap: 2rem;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
  }

  .footer-title {
    font-size: 0.9rem;
  }

  .footer-links {
    gap: 0.5rem;
  }

  .footer-links a {
    font-size: 0.85rem;
  }
}

/* Tablet Footer */
@media (max-width: 1024px) and (min-width: 641px) {
  .footer-container {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

**Step 2: Test footer**
- Desktop: 6 columns visible
- Tablet (1024px): 2-3 columns
- Mobile (640px): 1 column stacked
- ED Visas column always prominent
- All links clickable (44px+ targets)
- Color contrast meets WCAG AA

**Step 3: Commit**

```bash
git add styles/main.css
git commit -m "feat: style responsive footer grid with ED Visas priority positioning"
```

---

### Task 6: Update All 60+ Pages with New Header/Footer

**Files:**
- Modify: Every page in `/pages/**/*.html` (60+ pages)

**Step 1: Update header on all pages**
- Replace old header markup with new mega menu structure
- Ensure mega menu dropdowns functional
- Test mobile accordion on sample pages

**Step 2: Update footer on all pages**
- Replace old footer with new 6-column structure
- Verify ED Visas column first (left)
- Test responsive stacking

**Step 3: Batch commit per directory**

```bash
# Chiang Mai pages
git add pages/chiang-mai/*.html
git commit -m "feat: update Chiang Mai pages with new header mega menu and restructured footer"

# Visa pages
git add pages/visas/**/*.html
git commit -m "feat: update visa pages with new header mega menu and restructured footer"

# Immigration pages
git add pages/immigration/*.html
git commit -m "feat: update immigration pages with new header mega menu and restructured footer"

# Culture pages
git add pages/culture/*.html
git commit -m "feat: update culture pages with new header mega menu and restructured footer"

# ED visa pages
git add pages/ed-visas/*.html
git commit -m "feat: update ED visa pages with new header mega menu and restructured footer"

# Tools & other
git add pages/tools/*.html pages/checklists/*.html pages/*.html
git commit -m "feat: update all remaining pages with new header mega menu and restructured footer"
```

---

### Task 7: Visual QA — Header & Footer on All Pages

**Files:**
- Test: All 60+ pages (manual browser testing)

**Step 1: Desktop verification (1200px+)**
- Mega menu appears on hover
- All 6 categories visible
- ED Visas prominent
- Footer displays 6 columns
- ED Visas column first (left)
- All links clickable

**Step 2: Mobile verification (375px)**
- Hamburger icon visible
- Menu opens/closes smoothly
- All accordions expand/collapse
- Each category fully accessible
- Footer stacks vertically
- Touch targets 44px+
- No horizontal scroll

**Step 3: Tablet verification (1024px)**
- Mega menu functional
- Footer 2-3 columns
- Navigation clear

**Step 4: Create QA report**

File: `C:\ZZZWebsites\cmlocals\docs\PHASE4-QA-RESULTS.csv`

```
page_path,header_mega_menu,mobile_accordion,footer_ed_first,footer_responsive,issues,status
pages/chiang-mai/why-chiang-mai-base.html,✅,✅,✅,✅,none,pass
pages/visas/index.html,✅,✅,✅,✅,none,pass
... (60 rows)
```

**Step 5: Commit QA results**

```bash
git add docs/PHASE4-QA-RESULTS.csv
git commit -m "test: complete QA verification for Phase 4 header/footer restructure"
```

---

### Task 8: Final Phase 4 Report

**Files:**
- Create: `C:\ZZZWebsites\cmlocals\docs\PHASE4-COMPLETION-REPORT.md`

**Report contents:**

```markdown
# Phase 4: Navigation & Footer Restructuring — Complete

## Status: ✅ COMPLETE

### Coverage
- Pages updated: 63 (100% of eligible pages)
- Header: Mega menu (desktop) + accordion drawer (mobile)
- Footer: 6-column layout with ED Visas priority

### Implementation Details

**Header Navigation**
- Desktop: Mega menu with 6 categories (ED Visas, Chiang Mai, Visa Guides, Immigration, Culture, Tools)
- Mobile: Accordion drawer with smooth expand/collapse
- All 60+ pages linked and discoverable
- ED Visas prominent (first category)

**Footer Restructuring**
- 6-column layout: ED Visas (left, priority) → Chiang Mai → Visa Guides → Immigration → Culture/Tools → Contact
- All 60+ pages linked in footer
- Responsive: 6 columns (desktop) → 2-3 columns (tablet) → 1 column (mobile)
- ED Visas always first/top

### QA Results
✅ Desktop mega menu (1200px+) functional
✅ Mobile accordion drawer working smoothly
✅ Footer responsive and properly organized
✅ All 60+ pages accessible from header and footer
✅ Touch targets 44px+ (mobile)
✅ WCAG AA compliant
✅ Zero critical issues

### Commits
- Task 1: Header HTML structure (mega menu + accordion markup) — 1 commit
- Task 2: Mega menu styling (desktop dropdown) — 1 commit
- Task 3: Mobile accordion styling — 1 commit
- Task 4: Footer HTML restructuring — 1 commit
- Task 5: Footer CSS styling — 1 commit
- Task 6: Update all 60+ pages — 6 commits (by directory)
- Task 7: QA verification — 1 commit
- Task 8: Completion report — 1 commit
- **Total: 14+ commits**

### Next Steps
1. User review of header/footer design
2. Test on staging environment
3. Deploy to production
4. Phase 5: Enhanced content & SEO metadata (if planned)

---

**Phase 4 is production-ready.** All 60+ pages now feature:
- Unified mega menu navigation
- Mobile-friendly accordion drawer
- Restructured footer with ED Visas priority
- Full site discoverability from header/footer
```

**Step 1: Create report file**

**Step 2: Commit final report**

```bash
git add docs/PHASE4-COMPLETION-REPORT.md
git commit -m "docs: complete Phase 4 navigation and footer restructuring report"
```

---

## Execution Flow Summary

1. ✅ **Task 1:** Header HTML structure (mega menu + accordion)
2. ✅ **Task 2:** Mega menu CSS (desktop dropdown styling)
3. ✅ **Task 3:** Mobile accordion CSS (expand/collapse)
4. ✅ **Task 4:** Footer HTML (ED Visas priority, 6-column layout)
5. ✅ **Task 5:** Footer CSS (responsive grid)
6. ✅ **Task 6:** Update all 60+ pages with new header/footer
7. ✅ **Task 7:** Visual QA across all pages
8. ✅ **Task 8:** Final completion report

**Total Commits:** 14+
**Total Pages Updated:** 63
**All Links Added:** 60+
**Time Estimate:** 180-240 minutes (3-4 hours)

---

## Success Criteria — All to be Verified

- ✅ Header mega menu displays all 6 categories
- ✅ All 60+ pages accessible from header
- ✅ ED Visas prominent (first category)
- ✅ Mobile accordion drawer smooth and functional
- ✅ Footer restructured with ED Visas as left column
- ✅ All 60+ pages linked in footer
- ✅ Footer responsive (6 columns → 2-3 → 1)
- ✅ 100% of pages updated (no orphaned old headers/footers)
- ✅ Zero broken navigation links
- ✅ WCAG AA accessible (keyboard nav, color contrast, semantic HTML)
- ✅ Mobile-optimized (touch targets 44px+, no horizontal scroll)
- ✅ All commits atomic and logically ordered
