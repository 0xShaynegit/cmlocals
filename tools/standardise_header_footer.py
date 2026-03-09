#!/usr/bin/env python3
"""
Batch-standardise header, mobile nav, and footer on all CMLocals pages.

- Replaces <header> with canonical header (depth-adjusted paths)
- Replaces mobile nav between </header> and <main with canonical accordion nav
- Replaces <footer> with canonical footer (depth-adjusted paths + hero bg colour)
- Injects canonical header+footer CSS as a late <style> block in <head>
  (cascade order ensures it overrides any conflicting earlier CSS)
- Fixes header-handler.js script path per depth
"""

import re
import sys
from pathlib import Path

CMLOCALS_ROOT = Path("C:/ZZZWebsites/cmlocals")

# Footer background colours by first subdirectory under pages/
FOOTER_COLORS = {
    "chiang-mai": "#101585",
}
DEFAULT_FOOTER_BG = "#0D1117"

# ---------------------------------------------------------------------------
# CANONICAL HEADER CSS
# ---------------------------------------------------------------------------
CANONICAL_HEADER_CSS = """/* ============================================================
   CANONICAL HEADER + NAV CSS (auto-injected – do not edit here)
   ============================================================ */
.site-header {
  background: white;
  border-bottom: 1px solid rgba(0,0,0,.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}
.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 70px;
}
.header-logo {
  text-decoration: none;
  display: flex;
  align-items: center;
}
.header-logo img {
  height: 40px;
  width: auto;
  display: block;
}
.header-logo-mark { display: none; }
.header-logo-text { display: none; }
.primary-nav {
  display: flex;
  gap: 3rem;
  flex: 1;
  justify-content: center;
  align-items: center;
}
.primary-nav a {
  position: relative;
  color: #111827;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  line-height: 1;
}
.primary-nav a:hover { color: var(--c-primary, #4F46E5); }
.header-ctas {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-shrink: 0;
}
.header-ctas .btn-wa {
  padding: 0.4rem 0.9rem;
  font-size: 0.9rem;
}
.header-fb-link { display: none; }
.header-hamburger {
  display: none; flex-direction: column; justify-content: center; align-items: center;
  width: 40px; height: 40px; gap: 5px;
  border-radius: 6px; cursor: pointer;
  background: transparent;
}
.header-hamburger span {
  display: block; width: 22px; height: 2px;
  background: #0D1117; border-radius: 2px;
  transition: transform .25s, opacity .25s;
}
.header-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.header-hamburger.open span:nth-child(2) { opacity: 0; }
.header-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
.mobile-nav {
  display: none; position: fixed; inset: 64px 0 0 0; z-index: 99;
  background: #FFFFFF; overflow-y: auto;
  padding: 1.5rem clamp(1.25rem, 4vw, 2.5rem) 3rem;
  border-top: 1px solid #E5E7EB;
}
.mobile-nav.open { display: block; }
.mobile-nav a {
  display: block; padding: .9rem 0;
  font-size: 0.9rem; font-weight: 500; color: #0D1117;
  text-decoration: none;
  border-bottom: 1px solid #E5E7EB;
}
.mobile-nav a:last-of-type { border-bottom: none; }
.mobile-nav a:hover { color: var(--c-primary, #4F46E5); }
.mobile-nav-ctas { display: flex; flex-direction: column; gap: .75rem; margin-top: 1.5rem; }
.mobile-nav-ctas .btn { justify-content: center; }
.nav-item {
  position: relative;
  display: inline-flex;
  align-items: center;
}
.nav-item > a.nav-link {
  position: relative;
  color: #111827;
  text-decoration: none;
  font-size: 1.2rem;
  font-weight: 500;
  padding: 0;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  line-height: 1;
}
.nav-item > a.nav-link:hover {
  text-decoration: underline;
  text-decoration-color: var(--c-primary, #4F46E5);
  text-underline-offset: 4px;
  color: var(--c-primary, #4F46E5);
}
.nav-item > a.nav-link.has-dropdown { cursor: pointer; }
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  border: 1px solid rgba(0,0,0,.1);
  border-radius: 0;
  box-shadow: 0 4px 12px rgba(0,0,0,.08);
  padding: 1.75rem 2rem;
  width: 350px;
  display: none;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.15s ease-out;
  margin-top: 0;
  z-index: 101;
}
.dropdown-menu[style*="display: block"] {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 2rem;
}
.mega-menu {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
}
.mega-menu:has(> .dropdown-section:nth-child(2)) {
  width: 600px !important;
}
.dropdown-section {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  flex: 1;
  min-width: 200px;
}
.dropdown-section:last-child { margin-bottom: 0; }
.dropdown-section h3 {
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--c-primary, #4F46E5);
  font-weight: 600;
  margin: 0 0 0.5rem 0;
  padding: 0;
  border: none;
}
.dropdown-section ul { list-style: none; padding: 0; margin: 0; }
.dropdown-section li a {
  color: #374151;
  text-decoration: none;
  font-size: 0.9rem;
  line-height: 1.2;
  transition: color 0.2s;
  display: block;
  padding: 0.1rem 0;
}
.dropdown-section li a:hover { color: var(--c-primary, #4F46E5); }
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  gap: 4px;
  padding: 0.5rem;
}
.mobile-menu-toggle span {
  width: 24px;
  height: 2px;
  background: #111827;
  transition: all 0.3s;
}
.mobile-menu-toggle.active span:nth-child(1) { transform: rotate(45deg) translate(8px, 8px); }
.mobile-menu-toggle.active span:nth-child(2) { opacity: 0; }
.mobile-menu-toggle.active span:nth-child(3) { transform: rotate(-45deg) translate(7px, -7px); }
@media (min-width: 1024px) {
  .desktop-only { display: flex !important; }
  .mobile-only { display: none !important; }
}
@media (max-width: 1023px) {
  .mobile-menu-toggle { display: flex; }
  .primary-nav { display: none; }
  .dropdown-menu { display: none; }
  .nav-mobile {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border-bottom: 1px solid rgba(0,0,0,.1);
    flex-direction: column;
    max-height: calc(100vh - 70px);
    overflow-y: auto;
    z-index: 999;
  }
  .nav-mobile.open { display: flex; }
  .nav-accordion {
    border-bottom: 1px solid rgba(0,0,0,.1);
    cursor: pointer;
    margin: 0;
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
    font-size: 0.9rem;
  }
  .nav-accordion summary::after {
    content: '▼';
    font-size: 0.9rem;
    transition: transform 0.3s;
  }
  .nav-accordion[open] summary::after { transform: rotate(180deg); }
  .nav-accordion ul {
    list-style: none;
    padding: 0;
    margin: 0;
    background: rgba(79, 70, 229, 0.02);
  }
  .nav-accordion li { border-bottom: 1px solid rgba(0,0,0,.05); }
  .nav-accordion li a {
    display: block;
    padding: 0.75rem 1rem;
    padding-left: 2rem;
    color: #374151;
    text-decoration: none;
    font-size: 0.9rem;
  }
  .nav-accordion li a:active {
    background: rgba(79, 70, 229, 0.1);
    color: var(--c-primary, #4F46E5);
  }
  .dropdown-menu { display: none !important; }
}
@media (max-width: 960px) {
  .primary-nav { display: none; }
  .header-hamburger { display: flex; }
}"""

# ---------------------------------------------------------------------------
# CANONICAL FOOTER CSS
# ---------------------------------------------------------------------------
CANONICAL_FOOTER_CSS = """/* ============================================================
   CANONICAL FOOTER CSS (auto-injected – do not edit here)
   ============================================================ */
.site-footer {
  background: var(--footer-bg, #0D1117);
  color: rgba(255, 255, 255, 0.92);
  padding: 3.6rem 0 0;
}
.footer-container {
  max-width: 1400px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 3.6rem;
  padding: 0 1.8rem 1.8rem;
  width: 80%;
}
.footer-col {
  display: flex;
  flex-direction: column;
  gap: 1.35rem;
}
.footer-col-cmlocals { gap: 1.8rem; }
.footer-logo a {
  font-size: 0.9rem;
  font-weight: bold;
  color: white;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}
.footer-logo img {
  height: 43.2px;
  width: auto;
  display: block;
}
.footer-tagline {
  font-size: 0.9rem;
  line-height: 1.6;
  margin: 0;
  color: rgba(255, 255, 255, 0.75);
}
.footer-socials {
  display: flex;
  gap: 1.35rem;
}
.social-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28.8px;
  height: 28.8px;
  color: rgba(255, 255, 255, 0.75);
  text-decoration: none;
  transition: filter 0.2s ease, color 0.2s ease;
  filter: grayscale(100%);
}
.social-icon:hover { color: currentColor; filter: grayscale(0%); }
.social-icon.social-whatsapp:hover { color: #25D366; }
.social-icon.social-facebook:hover { color: #1877F2; }
.social-icon.social-messenger:hover { color: #0084FF; }
.social-icon svg { width: 100%; height: 100%; }
.footer-col-title {
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255, 255, 255, 0.95);
  margin: 0;
}
.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.81rem;
}
.footer-links a {
  color: rgba(255, 255, 255, 0.75);
  text-decoration: none;
  font-size: 0.9rem;
  line-height: 1.5;
  transition: color 0.2s;
}
.footer-links a:hover { color: white; }
.footer-bottom-bar {
  max-width: 1400px;
  margin: 0 auto;
  padding: 1.8rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.8rem;
  width: 80%;
}
.footer-bottom-bar p {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
  margin: 0;
}
.footer-legal-links {
  display: flex;
  gap: 1.8rem;
}
.footer-legal-links a {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  transition: color 0.2s;
}
.footer-legal-links a:hover { color: rgba(255, 255, 255, 0.9); }
@media (max-width: 1024px) {
  .footer-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
  }
  .footer-bottom-bar { flex-direction: column; text-align: center; }
}
@media (max-width: 640px) {
  .site-footer { padding: 3rem 1.5rem 0; }
  .footer-container {
    grid-template-columns: 1fr;
    gap: 2rem;
    padding-bottom: 1.5rem;
  }
  .footer-col-title { font-size: 0.9rem; }
  .footer-links a { font-size: 0.9rem; }
  .footer-bottom-bar {
    padding: 1.5rem;
    flex-direction: column;
    gap: 1rem;
  }
  .footer-bottom-bar p { font-size: 0.9rem; }
  .footer-legal-links { gap: 1rem; }
  .footer-legal-links a { font-size: 0.9rem; }
}"""

# ---------------------------------------------------------------------------
# CANONICAL HEADER HTML  (use {P} as the root-relative prefix placeholder)
# ---------------------------------------------------------------------------
def canonical_header_html(p):
    """p = path prefix to reach site root e.g. '../../' for depth-2 pages."""
    return f"""<header class="site-header" id="site-header" role="banner">
<div class="header-inner">

  <!-- Logo -->
  <a href="{p}index.html" class="header-logo" aria-label="CMLocals – homepage">
    <img src="{p}images/cmlocals-chiang-mai-locals-logo.webp" alt="CMLocals – Thai visa guides and Chiang Mai living" />
  </a>

  <!-- Desktop Mega Menu Navigation -->
  <nav class="primary-nav desktop-only" aria-label="Primary navigation">
    <!-- ED VISAS -->
    <div class="nav-item">
      <a href="{p}pages/ed-visas/index.html" class="nav-link has-dropdown">ED Visas</a>
      <div class="dropdown-menu mega-menu" role="menu">
        <div class="dropdown-section">
          <ul>
            <li><a href="{p}pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Emergency Self Defence</a></li>
            <li><a href="{p}pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai</a></li>
            <li><a href="{p}pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language</a></li>
            <li><a href="{p}pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat</a></li>
            <li><a href="{p}pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O</a></li>
            <li><a href="{p}pages/ed-visas/index.html">All ED Visas</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- CHIANG MAI -->
    <div class="nav-item">
      <a href="{p}pages/chiang-mai/index.html" class="nav-link has-dropdown">Chiang Mai</a>
      <div class="dropdown-menu mega-menu chiang-mai-menu" role="menu">
        <div class="dropdown-section">
          <h3>Lifestyle</h3>
          <ul>
            <li><a href="{p}pages/chiang-mai/index.html">Overview</a></li>
            <li><a href="{p}pages/chiang-mai/why-chiang-mai-base.html">Why Base Here</a></li>
            <li><a href="{p}pages/chiang-mai/where-to-stay.html">Where to Stay</a></li>
            <li><a href="{p}pages/chiang-mai/long-term-living.html">Long-Term Living</a></li>
            <li><a href="{p}pages/chiang-mai/things-to-do.html">Things to Do</a></li>
            <li><a href="{p}pages/chiang-mai/digital-nomads.html">Digital Nomads</a></li>
            <li><a href="{p}pages/chiang-mai/cost-of-living.html">Cost of Living</a></li>
            <li><a href="{p}pages/chiang-mai/phones-and-banking.html">Phones &amp; Banking</a></li>
            <li><a href="{p}pages/chiang-mai/getting-around.html">Getting Around</a></li>
            <li><a href="{p}pages/chiang-mai/healthcare.html">Healthcare</a></li>
            <li><a href="{p}pages/chiang-mai/insurance.html">Insurance</a></li>
            <li><a href="{p}pages/chiang-mai/taxes.html">Taxes</a></li>
          </ul>
        </div>
        <div class="dropdown-section">
          <h3>Culture</h3>
          <ul>
            <li><a href="{p}pages/culture/index.html">Culture Guide</a></li>
            <li><a href="{p}pages/culture/customs-traditions-thailand.html">Customs &amp; Traditions</a></li>
            <li><a href="{p}pages/culture/thai-culture-etiquette.html">Etiquette</a></li>
            <li><a href="{p}pages/culture/festivals-events-chiang-mai.html">Festivals</a></li>
            <li><a href="{p}pages/culture/thai-food-culture.html">Thai Food</a></li>
            <li><a href="{p}pages/culture/temple-etiquette.html">Temple Etiquette</a></li>
            <li><a href="{p}pages/culture/sak-yant-chiang-mai.html">Sak Yant</a></li>
            <li><a href="{p}pages/culture/sak-yant-designs-and-meanings.html">Sak Yant Designs</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- VISA GUIDES -->
    <div class="nav-item">
      <a href="{p}pages/visas/index.html" class="nav-link has-dropdown">Visa Guides</a>
      <div class="dropdown-menu mega-menu" role="menu">
        <div class="dropdown-section">
          <h3>All Types</h3>
          <ul>
            <li><a href="{p}pages/visas/index.html">All Visas</a></li>
            <li><a href="{p}pages/visas/short-stay/index.html">Short-Stay</a></li>
            <li><a href="{p}pages/visas/long-stay/index.html">Long-Stay</a></li>
            <li><a href="{p}pages/visas/short-stay/dtv-destination-thailand-visa-thai-visa-advice-chiang-mai-cmlocals.html">DTV</a></li>
            <li><a href="{p}pages/visas/short-stay/tourist-visa.html">Tourist</a></li>
            <li><a href="{p}pages/visas/guides/which-visa.html">Which Visa?</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- IMMIGRATION -->
    <div class="nav-item">
      <a href="{p}pages/immigration/index.html" class="nav-link has-dropdown">Immigration</a>
      <div class="dropdown-menu mega-menu" role="menu">
        <div class="dropdown-section">
          <h3>Compliance</h3>
          <ul>
            <li><a href="{p}pages/immigration/index.html">All Immigration</a></li>
            <li><a href="{p}pages/immigration/90-day-reporting.html">90-Day Reporting</a></li>
            <li><a href="{p}pages/immigration/tm30-address-reporting.html">TM30 Registration</a></li>
            <li><a href="{p}pages/immigration/re-entry-permits.html">Re-Entry Permits</a></li>
            <li><a href="{p}pages/immigration/overstay-penalties.html">Overstay Penalties</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>

  <!-- CTAs & Mobile Toggle -->
  <div class="header-ctas">
    <a href="https://wa.me/66801202074" class="btn btn-wa" rel="noopener" target="_blank" title="Message on WhatsApp">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>
    <button class="mobile-menu-toggle" id="hamburger" aria-expanded="false" aria-controls="mobile-nav" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
  </div>

</div>
</header>"""


def canonical_mobile_nav_html(p):
    """Canonical accordion mobile nav. p = root prefix."""
    return f"""<nav class="nav-mobile mobile-only" id="mobile-nav" aria-label="Mobile navigation" hidden>
  <details class="nav-accordion" open>
    <summary>ED Visas (6)</summary>
    <ul>
      <li><a href="{p}pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Emergency Self Defence</a></li>
      <li><a href="{p}pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai</a></li>
      <li><a href="{p}pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language</a></li>
      <li><a href="{p}pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat</a></li>
      <li><a href="{p}pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O</a></li>
      <li><a href="{p}pages/ed-visas/index.html">All ED Visas</a></li>
    </ul>
  </details>
  <details class="nav-accordion">
    <summary>Chiang Mai</summary>
    <ul>
      <li><a href="{p}pages/chiang-mai/index.html">Overview</a></li>
      <li><a href="{p}pages/chiang-mai/why-chiang-mai-base.html">Why Base Here</a></li>
      <li><a href="{p}pages/chiang-mai/where-to-stay.html">Where to Stay</a></li>
      <li><a href="{p}pages/chiang-mai/long-term-living.html">Long-Term Living</a></li>
      <li><a href="{p}pages/chiang-mai/things-to-do.html">Things to Do</a></li>
      <li><a href="{p}pages/chiang-mai/digital-nomads.html">Digital Nomads</a></li>
      <li><a href="{p}pages/chiang-mai/cost-of-living.html">Cost of Living</a></li>
      <li><a href="{p}pages/chiang-mai/phones-and-banking.html">Phones &amp; Banking</a></li>
      <li><a href="{p}pages/chiang-mai/getting-around.html">Getting Around</a></li>
      <li><a href="{p}pages/chiang-mai/healthcare.html">Healthcare</a></li>
      <li><a href="{p}pages/chiang-mai/insurance.html">Insurance</a></li>
      <li><a href="{p}pages/chiang-mai/taxes.html">Taxes</a></li>
    </ul>
  </details>
  <details class="nav-accordion">
    <summary>Culture</summary>
    <ul>
      <li><a href="{p}pages/culture/index.html">Culture Guide</a></li>
      <li><a href="{p}pages/culture/customs-traditions-thailand.html">Customs &amp; Traditions</a></li>
      <li><a href="{p}pages/culture/thai-culture-etiquette.html">Etiquette</a></li>
      <li><a href="{p}pages/culture/festivals-events-chiang-mai.html">Festivals</a></li>
      <li><a href="{p}pages/culture/thai-food-culture.html">Thai Food</a></li>
      <li><a href="{p}pages/culture/temple-etiquette.html">Temple Etiquette</a></li>
      <li><a href="{p}pages/culture/sak-yant-chiang-mai.html">Sak Yant</a></li>
    </ul>
  </details>
  <details class="nav-accordion">
    <summary>Visa Guides</summary>
    <ul>
      <li><a href="{p}pages/visas/index.html">All Visas</a></li>
      <li><a href="{p}pages/visas/short-stay/index.html">Short-Stay</a></li>
      <li><a href="{p}pages/visas/long-stay/index.html">Long-Stay</a></li>
      <li><a href="{p}pages/visas/short-stay/dtv-destination-thailand-visa-thai-visa-advice-chiang-mai-cmlocals.html">DTV</a></li>
      <li><a href="{p}pages/visas/short-stay/tourist-visa.html">Tourist</a></li>
      <li><a href="{p}pages/visas/guides/which-visa.html">Which Visa?</a></li>
    </ul>
  </details>
  <details class="nav-accordion">
    <summary>Immigration</summary>
    <ul>
      <li><a href="{p}pages/immigration/index.html">All Immigration</a></li>
      <li><a href="{p}pages/immigration/90-day-reporting.html">90-Day Reporting</a></li>
      <li><a href="{p}pages/immigration/tm30-address-reporting.html">TM30 Registration</a></li>
      <li><a href="{p}pages/immigration/re-entry-permits.html">Re-Entry Permits</a></li>
      <li><a href="{p}pages/immigration/overstay-penalties.html">Overstay Penalties</a></li>
    </ul>
  </details>
</nav>"""


def canonical_footer_html(p, footer_bg):
    """Canonical footer HTML. p = root prefix, footer_bg = hex colour."""
    return f"""<footer class="site-footer" role="contentinfo" style="background: {footer_bg};">
<div class="footer-container">

  <!-- Column 1: CMLocals + Tagline + Social Icons -->
  <div class="footer-col footer-col-cmlocals">
    <div class="footer-logo">
      <a href="{p}index.html">
        <img src="{p}images/cmlocals-chiang-mai-locals-logo.webp" alt="CMLocals – Thai visa guides and Chiang Mai living" />
      </a>
    </div>
    <p class="footer-tagline">Independent Thai visa information hub for Chiang Mai and long-stay life in Thailand.</p>
    <div class="footer-socials">
      <a href="https://wa.me/66801202074" title="WhatsApp" class="social-icon social-whatsapp" target="_blank" rel="noopener noreferrer">
        <svg width="24" height="24" viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="19.4395" cy="19.4395" r="19.4395" fill="#25D366"/><path d="M19.5 9.5C14.253 9.5 10 13.753 10 19c0 1.67.436 3.285 1.265 4.717L10 29l5.418-1.234A9.454 9.454 0 0019.5 28.5c5.247 0 9.5-4.253 9.5-9.5s-4.253-9.5-9.5-9.5zm5.508 13.142c-.232.652-1.345 1.247-1.853 1.29-.508.043-.982.228-3.306-.688-2.806-1.107-4.573-3.974-4.71-4.16-.137-.186-1.12-1.49-1.12-2.843 0-1.352.71-2.018.96-2.293.25-.275.546-.344.728-.344.183 0 .365.002.525.01.168.007.394-.064.617.47.232.556.786 1.92.855 2.06.069.138.115.3.023.485-.093.186-.139.3-.275.462-.137.162-.288.362-.412.486-.137.137-.28.286-.12.56.16.275.71 1.173 1.525 1.9 1.047.933 1.93 1.222 2.205 1.36.275.137.435.115.595-.069.16-.185.686-.8.869-1.075.183-.275.365-.228.617-.137.25.092 1.595.752 1.868.889.275.137.457.206.526.32.068.115.068.663-.164 1.315z" fill="white"/></svg>
      </a>
      <a href="https://m.me/cmlocals" title="Messenger" class="social-icon social-messenger" target="_blank" rel="noopener noreferrer">
        <svg width="24" height="24" viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="19.4395" cy="19.4395" r="19.4395" fill="#0084FF"/><path d="M19.5 9.5C13.701 9.5 9 13.748 9 19.074c0 3.014 1.474 5.702 3.778 7.456V30l3.294-1.81c.878.244 1.81.376 2.778.376 5.799 0 10.5-4.248 10.5-9.574S25.299 9.5 19.5 9.5zm1.04 12.878l-2.674-2.852-5.22 2.852 5.74-6.096 2.74 2.852 5.154-2.852-5.74 6.096z" fill="white"/></svg>
      </a>
      <a href="https://www.facebook.com/chiangmailocals" title="Facebook" class="social-icon social-facebook" target="_blank" rel="noopener noreferrer">
        <svg width="24" height="24" viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="19.5" cy="19.5" r="19.5" fill="#1877F2"/><path d="M20.5 28v-8h2.5l.375-2.875h-2.875v-1.75c0-.75.25-1.25 1.375-1.25h1.5V10.625c-.25 0-1.125-.125-2.125-.125-2.125 0-3.625 1.375-3.625 3.875v2.125h-2.5v2.875h2.5v8h3z" fill="white"/></svg>
      </a>
    </div>
  </div>

  <!-- Column 2: ED Visas -->
  <div class="footer-col">
    <h3 class="footer-col-title">ED Visas</h3>
    <ul class="footer-links">
      <li><a href="{p}pages/ed-visas/emergency-self-defence-ed-visa-chiang-mai.html">Emergency Self Defence</a></li>
      <li><a href="{p}pages/ed-visas/muay-thai-ed-visa-chiang-mai.html">Muay Thai</a></li>
      <li><a href="{p}pages/ed-visas/thai-language-ed-visa-chiang-mai.html">Thai Language</a></li>
      <li><a href="{p}pages/ed-visas/hand-to-hand-combat-ed-visa-chiang-mai.html">Hand-to-Hand Combat</a></li>
      <li><a href="{p}pages/ed-visas/volunteer-non-o-visa-chiang-mai.html">Volunteer Non-O</a></li>
      <li><a href="{p}pages/ed-visas/index.html">All ED Visas</a></li>
    </ul>
  </div>

  <!-- Column 3: Chiang Mai -->
  <div class="footer-col">
    <h3 class="footer-col-title">Chiang Mai</h3>
    <ul class="footer-links">
      <li><a href="{p}pages/chiang-mai/index.html">Overview</a></li>
      <li><a href="{p}pages/chiang-mai/where-to-stay.html">Where to Stay</a></li>
      <li><a href="{p}pages/chiang-mai/cost-of-living.html">Cost of Living</a></li>
      <li><a href="{p}pages/chiang-mai/getting-around.html">Getting Around</a></li>
      <li><a href="{p}pages/chiang-mai/long-term-living.html">Long-Term Living</a></li>
      <li><a href="{p}pages/chiang-mai/healthcare.html">Healthcare</a></li>
    </ul>
  </div>

  <!-- Column 4: Visa Guides -->
  <div class="footer-col">
    <h3 class="footer-col-title">Visa Guides</h3>
    <ul class="footer-links">
      <li><a href="{p}pages/visas/index.html">All Visas</a></li>
      <li><a href="{p}pages/visas/short-stay/dtv-destination-thailand-visa-thai-visa-advice-chiang-mai-cmlocals.html">DTV</a></li>
      <li><a href="{p}pages/visas/short-stay/index.html">Short Stay</a></li>
      <li><a href="{p}pages/visas/long-stay/index.html">Long Stay</a></li>
      <li><a href="{p}pages/visas/short-stay/tourist-visa.html">Tourist Visa</a></li>
      <li><a href="{p}pages/checklists/index.html">Checklists</a></li>
    </ul>
  </div>

</div>

<!-- Bottom Legal Bar -->
<div class="footer-bottom-bar">
  <p>&copy; 2026 CMLocals. All rights reserved.</p>
  <div class="footer-legal-links">
    <a href="{p}pages/privacy-policy.html">Privacy</a>
    <a href="{p}pages/terms-of-service.html">Terms</a>
    <a href="{p}pages/disclaimer.html">Disclaimer</a>
  </div>
</div>

</footer>"""


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def get_depth_and_prefix(filepath):
    """
    Return (depth, prefix) where depth is number of directories below root
    and prefix is the relative path back to root.
    index.html → depth 0, prefix ''
    pages/x.html → depth 1, prefix '../'
    pages/sub/x.html → depth 2, prefix '../../'
    pages/sub/sub/x.html → depth 3, prefix '../../../'
    """
    rel = filepath.relative_to(CMLOCALS_ROOT)
    depth = len(rel.parts) - 1
    prefix = "../" * depth
    return depth, prefix


def get_footer_bg(filepath):
    """Determine footer background colour based on directory."""
    rel = filepath.relative_to(CMLOCALS_ROOT)
    parts = rel.parts
    # parts[0] is 'pages' for sub-pages, parts[1] is the section
    if len(parts) >= 2 and parts[0] == "pages":
        section = parts[1]
        return FOOTER_COLORS.get(section, DEFAULT_FOOTER_BG)
    return DEFAULT_FOOTER_BG


def get_script_path(depth):
    """Return relative path to header-handler.js from a given depth."""
    # shared/ is at ZZZWebsites/shared/, cmlocals is at ZZZWebsites/cmlocals/
    # From depth d within cmlocals: go up d levels to reach cmlocals root,
    # then one more level to ZZZWebsites, then shared/js/
    levels_to_zzz = depth + 1  # depth dirs inside cmlocals + cmlocals itself
    return "../" * levels_to_zzz + "shared/js/header-handler.js"


def process_file(filepath):
    """Apply all canonical replacements to a single HTML file."""
    depth, prefix = get_depth_and_prefix(filepath)
    footer_bg = get_footer_bg(filepath)
    script_path = get_script_path(depth)

    content = filepath.read_text(encoding="utf-8")

    # ── 1. Replace <header>...</header> ────────────────────────────────────
    new_header = canonical_header_html(prefix)
    content = re.sub(
        r'<header\b[^>]*>.*?</header>',
        new_header,
        content,
        flags=re.DOTALL,
    )

    # ── 2. Replace mobile nav between </header> and <main ──────────────────
    # Could be: <nav class="mobile-nav"...>, <nav class="nav-mobile"...>,
    # or entirely absent. We replace existing one OR insert after </header>.
    mobile_nav_new = "\n" + canonical_mobile_nav_html(prefix)

    # Try to replace existing mobile nav
    replaced = re.sub(
        r'\n?<nav\b[^>]*(?:mobile-nav|nav-mobile)[^>]*>.*?</nav>',
        mobile_nav_new,
        content,
        count=1,
        flags=re.DOTALL,
    )
    if replaced == content:
        # No mobile nav found – insert after </header>
        replaced = content.replace("</header>", "</header>" + mobile_nav_new, 1)
    content = replaced

    # ── 3. Replace <footer>...</footer> ────────────────────────────────────
    new_footer = canonical_footer_html(prefix, footer_bg)
    content = re.sub(
        r'<footer\b[^>]*>.*?</footer>',
        new_footer,
        content,
        flags=re.DOTALL,
    )

    # ── 4. Fix header-handler.js script path ───────────────────────────────
    content = re.sub(
        r'(?:\.\.\/)+shared\/js\/header-handler\.js',
        script_path,
        content,
    )
    # Also fix card-click-handler.js if present (same depth logic)
    card_script = script_path.replace("header-handler.js", "card-click-handler.js")
    content = re.sub(
        r'(?:\.\.\/)+shared\/js\/card-click-handler\.js',
        card_script,
        content,
    )

    # ── 5. Inject canonical CSS before </head> ─────────────────────────────
    # Remove any previously injected canonical block first to avoid duplicates
    content = re.sub(
        r'\n?<style>\s*/\* =+\s*CANONICAL HEADER \+ NAV CSS.*?</style>\n?',
        '',
        content,
        flags=re.DOTALL,
    )
    content = re.sub(
        r'\n?<style>\s*/\* =+\s*CANONICAL FOOTER CSS.*?</style>\n?',
        '',
        content,
        flags=re.DOTALL,
    )

    canonical_css_block = (
        "\n<style>\n"
        + CANONICAL_HEADER_CSS
        + "\n"
        + CANONICAL_FOOTER_CSS
        + "\n</style>"
    )
    content = content.replace("</head>", canonical_css_block + "\n</head>", 1)

    filepath.write_text(content, encoding="utf-8")
    print(f"  OK {filepath.relative_to(CMLOCALS_ROOT)}")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    html_files = sorted(CMLOCALS_ROOT.rglob("*.html"))
    # Skip the homepage
    skip = {CMLOCALS_ROOT / "index.html"}
    targets = [f for f in html_files if f not in skip]

    print(f"Processing {len(targets)} HTML files…\n")
    errors = []
    for filepath in targets:
        try:
            process_file(filepath)
        except Exception as exc:
            errors.append((filepath, exc))
            print(f"  ERR {filepath.relative_to(CMLOCALS_ROOT)}: {exc}")

    print(f"\nDone. {len(targets) - len(errors)} updated, {len(errors)} errors.")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
