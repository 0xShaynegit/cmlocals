# CMLocals Legal Pages Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create three comprehensive legal pages (Privacy Policy, Terms of Service, Disclaimer) using CMLocals homepage design system with gradient hero + structured content layout.

**Architecture:** Each page reuses the homepage header/footer, CSS variables, and typography system. Pages share common structure: dark gradient hero section, centered content container (max 900px), semantic section structure with H2 headings, responsive spacing using clamp() functions.

**Tech Stack:** Plain HTML5, CSS (reusing homepage variables), Newsreader + DM Sans fonts (already loaded on homepage)

---

## Task 1: Analyze Homepage Structure

**Files:**
- Read: `C:\ZZZWebsites\cmlocals\index.html` (lines 1-300, header/footer/CSS structure)

**Step 1: Open homepage and identify key sections**

Read the homepage file to understand:
- Header structure (sticky header, logo, nav, buttons)
- Footer structure (grid layout, links)
- CSS variables (colors, spacing, typography)
- Reusable classes (.container, .btn, .label-tag, etc.)

**Expected outcome:** Understand exact HTML structure and CSS tokens to reuse across legal pages.

**Step 2: Note the CSS variable names**

Document from homepage:
- Color tokens: `--c-dark`, `--c-dark-2`, `--c-primary`, `--c-white`, `--c-body`, `--c-border`
- Font tokens: `--font-display`, `--font-body`
- Spacing tokens: `--edge`, `--section-py`, `--max-w`
- Radius/shadow tokens: `--radius-sm`, `--radius-md`, `--shadow-md`

---

## Task 2: Create CSS for Legal Pages Section Structure

**Files:**
- Create: `C:\ZZZWebsites\cmlocals\pages\legal-pages.css` (shared CSS for all legal pages)

**Step 1: Create the legal pages CSS file**

```css
/* ============================================================
   CMLocals Legal Pages – Shared Styles
   Privacy Policy, Terms of Service, Disclaimer
   ============================================================ */

/* --- HERO SECTION --- */
.legal-hero {
  background: linear-gradient(135deg, #0D1117 0%, #141922 100%);
  overflow: hidden;
  position: relative;
  padding-block: clamp(4rem, 8vw, 6rem);
}

.legal-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse 65% 80% at 90% 30%, rgba(255,255,255,.08) 0%, transparent 65%),
    radial-gradient(ellipse 50% 70% at 0% 90%, rgba(124,58,237,.12) 0%, transparent 65%);
}

.legal-hero-inner {
  position: relative;
  z-index: 1;
  max-width: 900px;
  padding-inline: var(--edge);
  margin-inline: auto;
}

.legal-hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 4vw, 3rem);
  font-weight: 400;
  line-height: 1.15;
  color: rgba(255,255,255,.92);
  letter-spacing: -.02em;
  margin-bottom: 1rem;
}

.legal-hero-lead {
  font-family: var(--font-body);
  font-size: clamp(.95rem, 1.5vw, 1.1rem);
  color: rgba(255,255,255,.82);
  line-height: 1.75;
  max-width: 65ch;
}

/* --- CONTENT SECTION --- */
.legal-content {
  width: 100%;
  max-width: 900px;
  padding-inline: var(--edge);
  padding-block: clamp(3rem, 5vw, 4.5rem);
  margin-inline: auto;
}

.legal-section {
  margin-bottom: clamp(2.5rem, 4vw, 3.5rem);
}

.legal-section h2 {
  font-family: var(--font-display);
  font-size: 1.75rem;
  font-weight: 400;
  color: var(--c-primary);
  letter-spacing: -.01em;
  margin-bottom: 1.25rem;
  padding-top: 1rem;
}

.legal-section h2:first-child {
  padding-top: 0;
}

.legal-section p {
  margin-bottom: 1rem;
  color: var(--c-body);
  line-height: 1.75;
  max-width: 75ch;
}

.legal-section ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

.legal-section li {
  margin-bottom: .75rem;
  color: var(--c-body);
  line-height: 1.75;
}

/* --- INTRO SECTION (special styling) --- */
.legal-intro {
  background: var(--c-subtle);
  padding: 2rem;
  border-radius: var(--radius-md);
  margin-bottom: 3rem;
}

.legal-intro p {
  color: var(--c-dark);
  font-size: 1.05rem;
  line-height: 1.75;
}

/* --- QUESTIONS FOOTER --- */
.legal-questions {
  background: var(--c-off-white);
  border: 1px solid var(--c-border);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  margin-top: 4rem;
  text-align: center;
}

.legal-questions h3 {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 400;
  color: var(--c-dark);
  margin-bottom: 1rem;
  letter-spacing: -.01em;
}

.legal-questions p {
  color: var(--c-muted);
  margin-bottom: 1.5rem;
  max-width: none;
}

.legal-questions-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.legal-questions-links a {
  display: inline-flex;
  align-items: center;
  gap: .5em;
  padding: .65em 1.4em;
  background: var(--c-primary);
  color: var(--c-white);
  border-radius: var(--radius-sm);
  text-decoration: none;
  font-weight: 600;
  font-size: .9rem;
  transition: background .18s, transform .12s;
}

.legal-questions-links a:hover {
  background: #4338CA;
  transform: translateY(-1px);
}

/* --- METADATA --- */
.legal-updated {
  font-size: .85rem;
  color: var(--c-muted);
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid var(--c-border);
  text-align: center;
}

/* --- RESPONSIVE --- */
@media (max-width: 768px) {
  .legal-hero h1 {
    font-size: 1.75rem;
  }

  .legal-section h2 {
    font-size: 1.5rem;
  }

  .legal-questions {
    padding: 1.5rem;
  }

  .legal-questions-links {
    gap: 1rem;
  }
}
```

**Step 2: Verify CSS file is created**

Check: `C:\ZZZWebsites\cmlocals\pages\legal-pages.css` exists and contains legal page styles.

---

## Task 3: Create Privacy Policy Page

**Files:**
- Create: `C:\ZZZWebsites\cmlocals\pages\privacy-policy.html`

**Step 1: Create privacy-policy.html with header/footer from homepage and content**

```html
<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Privacy Policy – CMLocals</title>
<meta name="description" content="Privacy Policy for CMLocals. How we collect, use, and protect your personal information. Last updated March 2026."/>
<link rel="canonical" href="https://www.cmlocals.com/pages/privacy-policy.html"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet"/>

<style>
/* ============================================================
   CMLocals – Homepage Design Tokens
   ============================================================ */
:root {
  --c-dark:          #0D1117;
  --c-dark-2:        #141922;
  --c-dark-3:        #1E2532;
  --c-primary:       #4F46E5;
  --c-primary-h:     #4338CA;
  --c-primary-glow:  rgba(79,70,229,.18);
  --c-violet:        #7C3AED;
  --c-violet-l:      #EDE9FE;
  --c-white:         #FFFFFF;
  --c-off-white:     #F8F7FF;
  --c-subtle:        #F1EFFF;
  --c-body:          #374151;
  --c-muted:         #6B7280;
  --c-border:        #E5E7EB;
  --c-border-dark:   rgba(255,255,255,.1);
  --c-wa:            #25D366;
  --c-wa-h:          #1aaa55;
  --c-fb:            #1877F2;
  --c-fb-h:          #1565d8;
  --radius-sm:       6px;
  --radius-md:       10px;
  --radius-lg:       16px;
  --shadow-sm:       0 1px 3px rgba(0,0,0,.08), 0 1px 2px rgba(0,0,0,.06);
  --shadow-md:       0 4px 16px rgba(0,0,0,.10), 0 2px 6px rgba(0,0,0,.06);
  --shadow-lg:       0 12px 40px rgba(0,0,0,.14);
  --font-display:    'Newsreader', Georgia, serif;
  --font-body:       'DM Sans', system-ui, sans-serif;
  --max-w:           1200px;
  --edge:            clamp(1.25rem, 4vw, 2.5rem);
  --section-py:      clamp(3rem, 5vw, 4.5rem);
}

/* --- RESET --- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
body { font-family: var(--font-body); font-size: 1rem; line-height: 1.65; color: var(--c-body); background: var(--c-white); -webkit-font-smoothing: antialiased; }
img { max-width: 100%; display: block; height: auto; }
a { color: inherit; }
ul { list-style: none; }
button { font-family: inherit; cursor: pointer; border: none; background: none; }

/* --- HEADER --- */
.site-header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(255,255,255,.92);
  backdrop-filter: blur(14px) saturate(180%);
  -webkit-backdrop-filter: blur(14px) saturate(180%);
  border-bottom: 1px solid var(--c-border);
  transition: box-shadow .25s;
}
.site-header.scrolled { box-shadow: 0 2px 20px rgba(0,0,0,.09); }
.header-inner {
  display: flex; align-items: center; justify-content: space-between;
  height: 54px; gap: 0.6rem; width: 100%; max-width: var(--max-w);
  margin-inline: auto; padding-inline: var(--edge);
}
.header-logo {
  text-decoration: none; flex-shrink: 0;
  display: flex; align-items: center; gap: .5rem;
}
.header-logo-mark {
  width: 32px; height: 32px; border-radius: 7px;
  background: linear-gradient(135deg, var(--c-primary) 0%, var(--c-violet) 100%);
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-family: var(--font-display); font-size: 1.05rem;
  font-weight: 500; font-style: italic; letter-spacing: -.01em;
}
.header-logo-text {
  font-family: var(--font-body); font-weight: 700; font-size: 1.05rem;
  color: var(--c-dark); letter-spacing: -.02em;
}
.primary-nav { display: flex; align-items: center; justify-content: center; gap: .4rem; flex: 1; }
.primary-nav a {
  font-size: 1rem; font-weight: 500; color: var(--c-body);
  padding: .5em .85em; border-radius: var(--radius-sm);
  text-decoration: none; white-space: nowrap;
  transition: color .15s, background .15s;
}
.primary-nav a:hover, .primary-nav a.active { color: var(--c-primary); background: var(--c-off-white); }
.header-ctas { display: flex; align-items: center; gap: .6rem; flex-shrink: 0; }
.btn {
  display: inline-flex; align-items: center; gap: .5em;
  padding: .65em 1.4em; border-radius: var(--radius-sm);
  font-family: var(--font-body); font-size: .9rem; font-weight: 600;
  line-height: 1.3; text-decoration: none; border: 1.5px solid transparent;
  transition: background .18s, transform .12s; white-space: nowrap;
}
.btn:hover { transform: translateY(-1px); }
.btn-wa { background: var(--c-wa); color: var(--c-white); border-color: var(--c-wa); }
.btn-wa:hover { background: var(--c-wa-h); border-color: var(--c-wa-h); }

/* --- LEGAL PAGES STYLES --- */
.legal-hero {
  background: linear-gradient(135deg, #0D1117 0%, #141922 100%);
  overflow: hidden; position: relative;
  padding-block: clamp(4rem, 8vw, 6rem);
}
.legal-hero::before {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 65% 80% at 90% 30%, rgba(255,255,255,.08) 0%, transparent 65%),
    radial-gradient(ellipse 50% 70% at 0% 90%, rgba(124,58,237,.12) 0%, transparent 65%);
}
.legal-hero-inner {
  position: relative; z-index: 1; max-width: 900px;
  padding-inline: var(--edge); margin-inline: auto;
}
.legal-hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 4vw, 3rem);
  font-weight: 400; line-height: 1.15;
  color: rgba(255,255,255,.92);
  letter-spacing: -.02em; margin-bottom: 1rem;
}
.legal-hero-lead {
  font-family: var(--font-body);
  font-size: clamp(.95rem, 1.5vw, 1.1rem);
  color: rgba(255,255,255,.82);
  line-height: 1.75; max-width: 65ch;
}

.legal-content {
  width: 100%; max-width: 900px;
  padding-inline: var(--edge);
  padding-block: var(--section-py);
  margin-inline: auto;
}
.legal-section { margin-bottom: clamp(2.5rem, 4vw, 3.5rem); }
.legal-section h2 {
  font-family: var(--font-display);
  font-size: 1.75rem; font-weight: 400;
  color: var(--c-primary);
  letter-spacing: -.01em;
  margin-bottom: 1.25rem; padding-top: 1rem;
}
.legal-section h2:first-child { padding-top: 0; }
.legal-section p {
  margin-bottom: 1rem; color: var(--c-body);
  line-height: 1.75; max-width: 75ch;
}
.legal-section ul { margin-left: 1.5rem; margin-bottom: 1rem; }
.legal-section li {
  margin-bottom: .75rem; color: var(--c-body);
  line-height: 1.75;
}

.legal-intro {
  background: var(--c-subtle);
  padding: 2rem; border-radius: var(--radius-md);
  margin-bottom: 3rem;
}
.legal-intro p {
  color: var(--c-dark); font-size: 1.05rem;
  line-height: 1.75; margin: 0;
}

.legal-questions {
  background: var(--c-off-white);
  border: 1px solid var(--c-border);
  border-radius: var(--radius-md);
  padding: 2.5rem; margin-top: 4rem;
  text-align: center;
}
.legal-questions h3 {
  font-family: var(--font-display);
  font-size: 1.5rem; font-weight: 400;
  color: var(--c-dark);
  margin-bottom: 1rem;
  letter-spacing: -.01em;
}
.legal-questions p {
  color: var(--c-muted); margin-bottom: 1.5rem;
}
.legal-questions-links {
  display: flex; align-items: center;
  justify-content: center; gap: 1.5rem;
  flex-wrap: wrap;
}
.legal-questions-links a {
  display: inline-flex; align-items: center;
  gap: .5em; padding: .65em 1.4em;
  background: var(--c-primary);
  color: var(--c-white);
  border-radius: var(--radius-sm);
  text-decoration: none; font-weight: 600;
  font-size: .9rem;
  transition: background .18s, transform .12s;
}
.legal-questions-links a:hover {
  background: #4338CA; transform: translateY(-1px);
}

.legal-updated {
  font-size: .85rem; color: var(--c-muted);
  margin-top: 3rem; padding-top: 2rem;
  border-top: 1px solid var(--c-border);
  text-align: center;
}

/* --- FOOTER --- */
.site-footer {
  background: var(--c-dark-2);
  padding-block: var(--section-py);
  color: rgba(255,255,255,.92);
  margin-top: var(--section-py);
}
.footer-inner { width: 100%; max-width: var(--max-w); margin-inline: auto; padding-inline: var(--edge); }
.footer-top {
  display: grid; grid-template-columns: 1.6fr repeat(4, 1fr);
  gap: 3rem; padding-bottom: 3rem;
  border-bottom: 1px solid rgba(255,255,255,.1);
}
.footer-logo {
  display: flex; align-items: center;
  gap: .5rem; text-decoration: none;
  margin-bottom: .8rem;
}
.footer-logo-mark {
  width: 30px; height: 30px; border-radius: 6px;
  background: linear-gradient(135deg, var(--c-primary) 0%, var(--c-violet) 100%);
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-family: var(--font-display);
  font-size: .95rem; font-weight: 500; font-style: italic;
}
.footer-logo-text {
  font-family: var(--font-body); font-weight: 700;
  font-size: .95rem; color: var(--c-white);
}
.footer-tagline {
  font-size: .82rem; line-height: 1.6;
  max-width: 240px;
  color: rgba(255,255,255,.88);
}
.footer-col-title {
  font-size: .72rem; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase;
  color: rgba(255,255,255,.70);
  margin-bottom: 1.1rem;
}
.footer-col ul {
  display: flex; flex-direction: column;
  gap: .55rem;
}
.footer-col a {
  font-size: .83rem;
  color: rgba(255,255,255,.88);
  text-decoration: none;
  transition: color .15s;
}
.footer-col a:hover { color: var(--c-white); }
.footer-bottom {
  display: flex; align-items: center;
  justify-content: space-between;
  padding-top: 2rem; gap: 1rem;
  flex-wrap: wrap;
}
.footer-copy { font-size: .8rem; }

@media (max-width: 960px) {
  .primary-nav { display: none; }
  .footer-top { grid-template-columns: 1fr 1fr; gap: 2rem; }
}
@media (max-width: 640px) {
  .legal-hero h1 { font-size: 1.75rem; }
  .legal-section h2 { font-size: 1.5rem; }
  .footer-top { grid-template-columns: 1fr; }
  .legal-questions { padding: 1.5rem; }
  .legal-questions-links { gap: 1rem; }
}
</style>
</head>

<body>

<header class="site-header" id="site-header">
<div class="header-inner">
  <a href="/" class="header-logo">
    <div class="header-logo-mark">C</div>
    <span class="header-logo-text">CMLocals</span>
  </a>
  <nav class="primary-nav">
    <a href="/">Home</a>
    <a href="/pages/visas/index.html">Visas</a>
    <a href="/pages/checklists/index.html">Checklists</a>
    <a href="/pages/immigration/index.html">Immigration</a>
    <a href="/pages/chiang-mai/index.html">Chiang Mai</a>
  </nav>
  <div class="header-ctas">
    <a href="https://wa.me/66801202074" class="btn btn-wa" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</div>
</header>

<section class="legal-hero">
<div class="legal-hero-inner">
  <h1>Privacy Policy</h1>
  <p class="legal-hero-lead">How we collect, use, and protect your personal information when you visit CMLocals.</p>
</div>
</section>

<main class="legal-content">

<div class="legal-intro">
<p>At CMLocals, we're committed to transparency about how we handle your data. This policy explains what information we collect, why we collect it, and how we protect it. Your privacy matters to us.</p>
</div>

<section class="legal-section">
<h2>Information We Collect</h2>
<p>We collect information in several ways to improve your experience and communicate with you:</p>
<ul>
<li><strong>Contact Form Submissions:</strong> When you fill out our contact form, we collect your name, email address, and message content.</li>
<li><strong>Newsletter Signups:</strong> If you subscribe to our email newsletter, we collect your email address and optional name.</li>
<li><strong>WhatsApp & Messenger Links:</strong> Clicking our WhatsApp or Messenger links directs you to external platforms. We can see aggregated click statistics but not personal messages.</li>
<li><strong>Analytics Data:</strong> We use Google Analytics to track how visitors interact with our site — pages viewed, time spent, device type, browser type, and general location (country/city level).</li>
<li><strong>Cookies:</strong> Our site uses cookies to remember preferences and improve your experience.</li>
</ul>
</section>

<section class="legal-section">
<h2>How We Use Your Information</h2>
<p>We use the information we collect for specific purposes related to our site and services:</p>
<ul>
<li><strong>Newsletter Delivery:</strong> Email addresses are used only to send you our newsletter and updates you've subscribed to.</li>
<li><strong>Communication:</strong> Contact form submissions help us respond to questions and feedback.</li>
<li><strong>Site Improvements:</strong> Analytics help us understand which content is useful, what needs improvement, and how to better serve our audience.</li>
<li><strong>User Experience:</strong> Cookies help us remember your preferences (theme, language, etc.) across sessions.</li>
</ul>
<p>We do not sell, trade, or share your personal information with third parties for marketing purposes.</p>
</section>

<section class="legal-section">
<h2>Third-Party Services</h2>
<p>Our website uses third-party services that may collect data:</p>
<ul>
<li><strong>Google Analytics:</strong> Tracks anonymous visitor behavior. <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google's privacy policy</a> governs this data.</li>
<li><strong>Email Service Provider:</strong> We use a reputable email service to deliver newsletters. Your email is protected under their privacy practices.</li>
<li><strong>Messaging Platforms:</strong> WhatsApp and Messenger are third-party platforms. Clicking our links directs you to their services. We recommend reviewing their privacy policies.</li>
</ul>
<p>We've chosen these providers based on their security and privacy standards, but we recommend reviewing their individual policies.</p>
</section>

<section class="legal-section">
<h2>Your Rights</h2>
<p>You have control over your personal information:</p>
<ul>
<li><strong>Access:</strong> You can request a copy of the information we hold about you.</li>
<li><strong>Deletion:</strong> You can request deletion of your email address from our newsletter at any time. Click "unsubscribe" in any newsletter email or contact us directly.</li>
<li><strong>Opt-Out:</strong> You can opt out of analytics tracking using browser settings or Google's browser extension.</li>
<li><strong>Contact:</strong> For any data requests, email us at contact@cmlocals.com or message us on WhatsApp.</li>
</ul>
</section>

<section class="legal-section">
<h2>Cookies & Tracking</h2>
<p>Our website uses cookies and similar tracking technologies:</p>
<ul>
<li><strong>Essential Cookies:</strong> Required for site functionality (session, CSRF protection).</li>
<li><strong>Analytics Cookies:</strong> Google Analytics cookies track your browsing behavior to help us improve the site.</li>
<li><strong>Preference Cookies:</strong> Remember your settings across sessions.</li>
</ul>
<p>You can disable cookies in your browser settings, though some site features may not work properly without them. Most browsers also allow you to control which cookies you accept.</p>
</section>

<section class="legal-section">
<h2>Data Security</h2>
<p>We take data security seriously. We use HTTPS encryption to protect data in transit and maintain reasonable security measures. However, no online transmission is 100% secure. We cannot guarantee absolute security against all threats.</p>
<p>If you believe your information has been compromised, please contact us immediately.</p>
</section>

<section class="legal-section">
<h2>Changes to This Policy</h2>
<p>We may update this privacy policy periodically to reflect changes in our practices or legal requirements. When we make material changes, we'll notify users via email or a prominent notice on our site. Your continued use of the site after changes constitutes acceptance of the updated policy.</p>
<p><strong>Last Updated:</strong> March 5, 2026</p>
</section>

<div class="legal-questions">
<h3>Questions About Your Privacy?</h3>
<p>If you have concerns or questions about how we handle your information, we're happy to help. Contact us using any of these methods:</p>
<div class="legal-questions-links">
  <a href="https://wa.me/66801202074" target="_blank" rel="noopener">WhatsApp</a>
  <a href="https://m.me/cmlocals" target="_blank" rel="noopener">Messenger</a>
</div>
</div>

<p class="legal-updated">Last updated: March 5, 2026</p>

</main>

<footer class="site-footer">
<div class="footer-inner">
  <div class="footer-top">
    <div>
      <a href="/" class="footer-logo">
        <div class="footer-logo-mark">C</div>
        <span class="footer-logo-text">CMLocals</span>
      </a>
      <p class="footer-tagline">Immigration guides, visa strategies, and Thailand resources—by residents, for residents.</p>
    </div>
    <div>
      <h3 class="footer-col-title">Visas</h3>
      <ul>
        <li><a href="/pages/visas/index.html">Visa Overview</a></li>
        <li><a href="/pages/visas/long-stay/index.html">Long Stay</a></li>
        <li><a href="/pages/ed-visas/index.html">ED Visa</a></li>
      </ul>
    </div>
    <div>
      <h3 class="footer-col-title">Immigration</h3>
      <ul>
        <li><a href="/pages/immigration/index.html">Immigration Home</a></li>
        <li><a href="/pages/immigration/entry-strategy-guide.html">Entry Strategy</a></li>
        <li><a href="/pages/immigration/90-day-reporting.html">90-Day Reporting</a></li>
      </ul>
    </div>
    <div>
      <h3 class="footer-col-title">Tools</h3>
      <ul>
        <li><a href="/pages/checklists/index.html">Checklists</a></li>
        <li><a href="/pages/tools/index.html">Tools</a></li>
        <li><a href="/pages/privacy-policy.html">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h3 class="footer-col-title">Support</h3>
      <ul>
        <li><a href="/pages/terms-of-service.html">Terms of Service</a></li>
        <li><a href="/pages/disclaimer.html">Disclaimer</a></li>
        <li><a href="https://www.facebook.com/chiangmailocals" target="_blank" rel="noopener">Facebook</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">&copy; 2026 CMLocals. All rights reserved.</div>
  </div>
</div>
</footer>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const header = document.getElementById('site-header');
  window.addEventListener('scroll', function() {
    if (window.scrollY > 10) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
});
</script>

</body>
</html>
```

**Step 2: Verify file is created and readable**

Check: `C:\ZZZWebsites\cmlocals\pages\privacy-policy.html` exists (2400+ lines with full content).

---

## Task 4: Create Terms of Service Page

**Files:**
- Create: `C:\ZZZWebsites\cmlocals\pages\terms-of-service.html`

**Step 1: Create terms-of-service.html with same header/footer structure**

Use the same header, footer, and CSS as privacy-policy.html (from Task 3), but with these content sections:

```html
<section class="legal-hero">
<div class="legal-hero-inner">
  <h1>Terms of Service</h1>
  <p class="legal-hero-lead">Please read these terms carefully before using CMLocals. By accessing our site, you agree to comply with these terms.</p>
</div>
</section>

<main class="legal-content">

<div class="legal-intro">
<p>These Terms of Service ("Terms") govern your use of CMLocals and all content, services, and products available through our website. By accessing or using CMLocals, you agree to be bound by these Terms. If you do not agree to these Terms, do not use this site.</p>
</div>

<section class="legal-section">
<h2>1. Acceptance of Terms</h2>
<p>By accessing and using CMLocals, you accept and agree to be bound by the Terms and the Privacy Policy. If you do not agree to abide by the above, please do not use this service. These Terms apply to all users of the site, including without limitation users who are browsers, vendors, customers, merchants, and/or contributors of content.</p>
</section>

<section class="legal-section">
<h2>2. Use License</h2>
<p>Permission is granted to temporarily download one copy of the materials (information or software) on CMLocals for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:</p>
<ul>
<li>Modify or copy the materials</li>
<li>Use the materials for any commercial purpose or for any public display</li>
<li>Attempt to decompile or reverse engineer any software contained on CMLocals</li>
<li>Remove any copyright or other proprietary notations from the materials</li>
<li>Transfer the materials to another person or "mirror" the materials on any other server</li>
<li>Scrape, crawl, or use automated tools to access the site</li>
<li>Violate any applicable laws or regulations in your use of the materials</li>
</ul>
<p>This license shall automatically terminate if you violate any of these restrictions and may be terminated by CMLocals at any time. Upon termination of your viewing of these materials or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.</p>
</section>

<section class="legal-section">
<h2>3. Disclaimer of Warranties</h2>
<p>The materials on CMLocals are provided on an "as is" basis. CMLocals makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>
<p><strong>Important:</strong> CMLocals is not a law firm. The information provided on this site is not legal advice and does not create an attorney-client relationship. We are not licensed to practice law in any jurisdiction. You should not rely on information from this site as a substitute for professional legal advice. Consult a qualified immigration lawyer for your specific situation.</p>
</section>

<section class="legal-section">
<h2>4. Limitations of Liability</h2>
<p>In no event shall CMLocals or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on CMLocals, even if CMLocals or an authorized representative has been notified orally or in writing of the possibility of such damage.</p>
<p>Because some jurisdictions do not allow limitations on implied warranties, or limitations of liability for consequential or incidental damages, these limitations may not apply to you.</p>
</section>

<section class="legal-section">
<h2>5. Accuracy of Materials</h2>
<p>The materials appearing on CMLocals could include technical, typographical, or photographic errors. CMLocals does not warrant that any of the materials on its website are accurate, complete, or current. CMLocals may make changes to the materials contained on its website at any time without notice. However, CMLocals does not commit to updating the materials.</p>
</section>

<section class="legal-section">
<h2>6. Links</h2>
<p>CMLocals has not reviewed all of the sites linked to its website and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by CMLocals of the site. Use of any such linked website is at the user's own risk.</p>
</section>

<section class="legal-section">
<h2>7. Modifications</h2>
<p>CMLocals may revise these Terms at any time without notice. By using this website, you are agreeing to be bound by the then current version of these Terms of Service.</p>
</section>

<section class="legal-section">
<h2>8. Governing Law</h2>
<p>These Terms and conditions are governed by and construed in accordance with the laws of Thailand, and you irrevocably submit to the exclusive jurisdiction of the courts in Thailand.</p>
</section>

<section class="legal-section">
<h2>9. User Conduct</h2>
<p>You agree not to use CMLocals:</p>
<ul>
<li>For any unlawful purpose or in violation of any laws or regulations</li>
<li>To harass, threaten, embarrass, or cause distress or discomfort to any person</li>
<li>To impersonate or attempt to impersonate any person or entity</li>
<li>To upload, transmit, or distribute any harmful, malicious, or deceptive content</li>
<li>To collect or track personal information of others without consent</li>
<li>For any commercial purpose without explicit permission</li>
</ul>
</section>

<section class="legal-section">
<h2>10. Intellectual Property Rights</h2>
<p>Unless otherwise stated, CMLocals and/or its licensors own the intellectual property rights for all material on the website. All intellectual property rights are reserved. You may view and print pages from the website for personal, non-commercial use, subject to restrictions set in these Terms and Conditions.</p>
<p>You must not:</p>
<ul>
<li>Republish material from this website without proper attribution</li>
<li>Sell, rent, or sub-license material from the website</li>
<li>Reproduce, duplicate, or copy material from this site for commercial purposes</li>
<li>Redistribute content unless content is specifically made for redistribution</li>
</ul>
</section>

<div class="legal-questions">
<h3>Questions About These Terms?</h3>
<p>If you have questions or concerns about these Terms of Service, please reach out to us:</p>
<div class="legal-questions-links">
  <a href="https://wa.me/66801202074" target="_blank" rel="noopener">WhatsApp</a>
  <a href="https://m.me/cmlocals" target="_blank" rel="noopener">Messenger</a>
</div>
</div>

<p class="legal-updated">Last updated: March 5, 2026</p>

</main>
```

**Step 2: Verify file created**

Check: `C:\ZZZWebsites\cmlocals\pages\terms-of-service.html` exists with full content.

---

## Task 5: Create Disclaimer Page

**Files:**
- Create: `C:\ZZZWebsites\cmlocals\pages\disclaimer.html`

**Step 1: Create disclaimer.html with same header/footer structure**

Use the same header, footer, and CSS as previous pages, with these content sections:

```html
<section class="legal-hero">
<div class="legal-hero-inner">
  <h1>Disclaimer</h1>
  <p class="legal-hero-lead">Important disclaimers about the accuracy and use of information on CMLocals.</p>
</div>
</section>

<main class="legal-content">

<div class="legal-intro">
<p>CMLocals provides immigration and lifestyle information for Thailand based on first-hand experience and research. However, immigration laws and policies change frequently. This page outlines important limitations and disclaimers about the information we provide.</p>
</div>

<section class="legal-section">
<h2>Information Accuracy & Currency</h2>
<p>We make every effort to provide accurate, up-to-date information about Thai immigration, visa requirements, and Chiang Mai lifestyle. However, immigration regulations change frequently and may vary by immigration office or embassy.</p>
<p><strong>You should verify all information with official sources:</strong></p>
<ul>
<li>Thai Immigration Bureau: <a href="https://www.immigration.go.th/" target="_blank" rel="noopener">immigration.go.th</a></li>
<li>Your nearest Thai embassy or consulate</li>
<li>Official government announcements and directives</li>
</ul>
<p>Do not assume that information on this site is current or applies to your specific situation without independent verification.</p>
</section>

<section class="legal-section">
<h2>Not Legal Advice</h2>
<p><strong>CMLocals is not a law firm and does not provide legal services.</strong> The information on this website is educational material only and should not be construed as legal advice or professional counsel. No attorney-client relationship is formed by using this site or contacting us through it.</p>
<p>Immigration law is complex and individual circumstances vary significantly. For matters affecting your visa status, legal rights, or residency, you should consult with a qualified immigration lawyer licensed to practice in Thailand.</p>
</section>

<section class="legal-section">
<h2>Thai Immigration Law Changes</h2>
<p>Thai immigration policies, visa types, requirements, and fees change frequently. Sometimes changes are announced with little notice. Policies may also differ between immigration offices.</p>
<p>We cannot guarantee that information will remain accurate after publication. Immigration law is not static, and what was true when written may be superseded by new regulations or policy changes.</p>
</section>

<section class="legal-section">
<h2>Individual Circumstances Vary</h2>
<p>Visa decisions and immigration outcomes depend on many individual factors:</p>
<ul>
<li>Your nationality and passport</li>
<li>Your personal history and background</li>
<li>Specific immigration office policies and interpretations</li>
<li>Individual officer discretion</li>
<li>Changing legal standards and precedents</li>
<li>Your specific life situation and financial circumstances</li>
</ul>
<p>Information that applies to one person may not apply to another. Always assess your individual situation with professional help.</p>
</section>

<section class="legal-section">
<h2>No Liability</h2>
<p>CMLocals and its contributors are not responsible for any outcomes, consequences, or damages arising from your use of information on this site or your decisions based on that information. This includes but is not limited to:</p>
<ul>
<li>Visa rejections or denials</li>
<li>Immigration fines or penalties</li>
<li>Overstay consequences</li>
<li>Deportation or blacklisting</li>
<li>Financial losses due to immigration changes</li>
<li>Incorrect decisions made based on outdated information</li>
</ul>
<p><strong>You use this site and its information entirely at your own risk.</strong> You are responsible for verifying all information and seeking appropriate professional advice before making immigration decisions.</p>
</section>

<section class="legal-section">
<h2>External Links & Third-Party Content</h2>
<p>CMLocals provides links to external websites and resources (Thai Immigration Bureau, embassies, etc.). We are not responsible for the accuracy, completeness, or reliability of content on external sites. Linking to a third-party site does not constitute an endorsement of that site or its content.</p>
<p>External links may become broken or outdated. We do not maintain or monitor external sites. Always verify official information directly with authoritative sources.</p>
</section>

<section class="legal-section">
<h2>Visa Requirements & Policy Interpretation</h2>
<p>Visa requirements listed on this site are based on our understanding of current Thai immigration law and regulations. However:</p>
<ul>
<li>Immigration officers have discretion in interpreting requirements</li>
<li>Requirements may be applied differently at different immigration offices</li>
<li>New directives or policy changes may supersede published rules</li>
<li>Official sources (immigration.go.th, embassies) should be considered authoritative</li>
<li>Any specific questions about your eligibility should be directed to Thai immigration officials</li>
</ul>
<p>Always verify requirements with the specific immigration office or embassy handling your case.</p>
</section>

<section class="legal-section">
<h2>Professional Consultation Recommended</h2>
<p>For any visa matters affecting your status in Thailand, we strongly recommend consulting with:</p>
<ul>
<li><strong>Immigration Lawyers:</strong> Licensed to practice immigration law in Thailand</li>
<li><strong>Thai Immigration Bureau:</strong> Direct contact via official channels</li>
<li><strong>Your Embassy or Consulate:</strong> For guidance on entry and visa options</li>
<li><strong>Qualified Visa Agents:</strong> Licensed by Thai immigration authorities</li>
</ul>
<p>Professional guidance is especially important if your situation is complex, involves previous immigration issues, or carries significant consequences.</p>
</section>

<section class="legal-section">
<h2>Experience & Context</h2>
<p>CMLocals is run by residents with 16+ years of personal experience living in Thailand and Chiang Mai. While our experience is real and genuine, it is not universal. Your situation may differ significantly. Experience should inform decisions, not determine them—especially when legal status is at stake.</p>
</section>

<div class="legal-questions">
<h3>Have Immigration Questions?</h3>
<p>For professional guidance on your specific situation, consult with a qualified immigration lawyer or contact Thai immigration directly. We're here for general information and community perspective, but cannot substitute for professional legal advice.</p>
<div class="legal-questions-links">
  <a href="https://www.immigration.go.th/" target="_blank" rel="noopener">Thai Immigration</a>
  <a href="https://wa.me/66801202074" target="_blank" rel="noopener">Contact Us</a>
</div>
</div>

<p class="legal-updated">Last updated: March 5, 2026</p>

</main>
```

**Step 2: Verify file created**

Check: `C:\ZZZWebsites\cmlocals\pages\disclaimer.html` exists with full content.

---

## Task 6: Test All Three Pages

**Files:**
- Test: `C:\ZZZWebsites\cmlocals\pages\privacy-policy.html`
- Test: `C:\ZZZWebsites\cmlocals\pages\terms-of-service.html`
- Test: `C:\ZZZWebsites\cmlocals\pages\disclaimer.html`

**Step 1: Open each page in a browser**

Open each file in a web browser and verify:
- Hero section displays with gradient background and white text
- Content sections are readable with proper spacing
- Links work (header nav, footer links, external links)
- "Questions?" section displays with button links
- Mobile responsiveness (shrink window, hero and headings scale down)
- Footer displays correctly with all columns

**Step 2: Verify responsive behavior**

- At 1200px+: Full layout with proper spacing
- At 768px: Sections stack, hero scales, footer grid collapses to 2 columns
- At 640px: Hero very compact, font sizes reduce, footer single column

**Step 3: Verify accessibility**

- Check contrast ratios (white text on dark hero background should be good)
- Headings use proper semantic hierarchy (h1 > h2)
- Links are understandable and keyboard-navigable
- No color-only information (all lists are bulleted/text)

---

## Task 7: Update Homepage Footer with Legal Links

**Files:**
- Modify: `C:\ZZZWebsites\cmlocals\index.html` (footer section, around line 600-700)

**Step 1: Add legal pages to homepage footer**

In the footer's Tools or Support column, add links to the three legal pages:

```html
<div>
  <h3 class="footer-col-title">Legal</h3>
  <ul>
    <li><a href="/pages/privacy-policy.html">Privacy Policy</a></li>
    <li><a href="/pages/terms-of-service.html">Terms of Service</a></li>
    <li><a href="/pages/disclaimer.html">Disclaimer</a></li>
  </ul>
</div>
```

Or add to an existing column (Tools/Support) if one exists.

**Step 2: Verify homepage displays correctly**

Open homepage in browser and verify:
- Footer displays all columns correctly
- New links are clickable and navigate to legal pages
- Footer styling is consistent

---

## Task 8: Final Quality Check

**Files:**
- Verify: All three legal pages
- Verify: Homepage footer

**Step 1: Cross-page link verification**

- [ ] Privacy Policy header nav links work
- [ ] Terms of Service header nav links work
- [ ] Disclaimer header nav links work
- [ ] All three pages' footer links work
- [ ] Footer legal links navigate correctly
- [ ] External links (Thai Immigration, etc.) open in new tabs

**Step 2: Content verification**

- [ ] All seven Privacy Policy sections present and readable
- [ ] All ten Terms of Service sections present and readable
- [ ] All eight Disclaimer sections present and readable
- [ ] No typos or formatting issues
- [ ] Lists are properly formatted with bullets
- [ ] Last updated dates correct (March 5, 2026)

**Step 3: Visual consistency**

- [ ] All three pages use same hero gradient
- [ ] H1 and H2 sizing matches design spec
- [ ] Section spacing consistent across pages
- [ ] Questions footer styling matches across pages
- [ ] Footer appears identical on all pages

---

## Success Criteria

✅ Three legal pages created with comprehensive content
✅ Hero sections use gradient background matching homepage
✅ Content organized in clear, readable sections
✅ Responsive design works on mobile, tablet, desktop
✅ All internal and external links functional
✅ Footer links added to homepage
✅ WCAG AA accessibility standards met
✅ Page load times fast (all static HTML/CSS)

---

## Timeline

- Task 1-2: 5 minutes (analyze + CSS)
- Task 3-5: 30 minutes (create three pages with full content)
- Task 6: 5 minutes (test all pages)
- Task 7: 5 minutes (update homepage footer)
- Task 8: 5 minutes (final quality check)

**Total estimated time: 50 minutes**
