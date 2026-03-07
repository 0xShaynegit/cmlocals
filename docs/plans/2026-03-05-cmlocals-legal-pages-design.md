# CMLocals Legal Pages Design

**Date:** March 5, 2026
**Scope:** Privacy Policy, Terms of Service, Disclaimer
**Layout Approach:** Gradient hero + structured content sections (homepage style)

---

## Overview

Create three comprehensive legal pages for CMLocals using the existing homepage design system. All pages follow a consistent visual pattern: gradient hero section + structured content blocks with clear typography hierarchy.

---

## Design Approach

**Selected:** Gradient Hero + Structured Content (Approach 3)
- Large hero section matching homepage visual language
- Gradient background with dark base (#0D1117 to #141922)
- White text on gradient for high contrast
- Content organized into visually distinct sections
- Maintains CMLocals brand consistency throughout

---

## Hero Section Specification

- **Height:** `clamp(4rem, 8vw, 6rem)` — smaller than homepage hero but visually consistent
- **Background:** Dark gradient (`linear-gradient(135deg, #0D1117 0%, #141922 100%)`)
- **Content Layout:**
  - Centered, full-width container
  - H1 title (Newsreader, responsive sizing)
  - Lead paragraph (DM Sans, 1-2 lines max)
- **Text Color:** `rgba(255,255,255,.92)` for accessibility
- **Padding:** Uses `--edge` variable for responsive horizontal spacing

---

## Content Section Structure

Each page follows this pattern:

### 1. Introduction Section
- Brief brand statement (2-3 sentences)
- Establishes tone and values
- No complex legal jargon in intro

### 2. Main Content Sections
- Clear H2 headings (Newsreader, color: primary indigo #4F46E5)
- Short paragraphs (max 150 words per section)
- Unordered lists for itemized information
- Section spacing: `clamp(2.5rem, 4vw, 3.5rem)` between sections
- Line-height: 1.75 for legal content readability

### 3. Contact/Questions Footer
- "Questions?" section at bottom
- Links to WhatsApp/email for clarification
- Styling: Subtle background, centered alignment

---

## Privacy Policy — Sections

1. **Information We Collect**
   - Contact form submissions
   - Email newsletter signups
   - WhatsApp/Messenger link clicks
   - Analytics (Google Analytics)
   - Device/browser information

2. **How We Use Information**
   - Newsletter delivery and communication
   - Site improvements and analytics
   - User experience optimization

3. **Third-Party Services**
   - Analytics provider details
   - Email service provider
   - Messaging platforms (WhatsApp, Messenger)
   - Third-party obligations

4. **Your Rights**
   - Data access requests
   - Deletion/opt-out options
   - Contact method for requests

5. **Cookies & Tracking**
   - Types of cookies used
   - Duration and purpose
   - How to disable cookies

6. **Data Security**
   - Security measures in place
   - Limitations and risks

7. **Changes to This Policy**
   - Last updated timestamp
   - Notification process for changes

---

## Terms of Service — Sections

1. **Acceptance of Terms**
   - Binding agreement statement
   - Scope of application

2. **Use License**
   - Personal, non-commercial use only
   - Restrictions: no scraping, automated access, reverse engineering
   - No resale or redistribution

3. **Disclaimers**
   - Not legal advice
   - Not a law firm or legal service
   - User responsibility for verification

4. **Intellectual Property**
   - Copyright ownership (CMLocals)
   - Fair use for sharing/linking
   - Attribution requirements
   - User content ownership

5. **User Conduct**
   - No harassment, hate speech, or illegal content
   - No misrepresentation or fraud
   - No commercial use without permission
   - Compliance with laws

6. **Limitation of Liability**
   - CMLocals not liable for user decisions
   - Information provided "as is"
   - Use at user's own risk

7. **Indemnification**
   - User indemnifies CMLocals for violations
   - Defense of claims

8. **Termination**
   - Right to terminate access
   - Basis for termination

---

## Disclaimer Page — Sections

1. **Information Accuracy**
   - Immigration laws change frequently
   - Best-effort currency maintenance
   - Recommendation to verify independently

2. **Not Legal Advice**
   - CMLocals is not a law firm
   - No attorney-client relationship
   - Professional consultation recommended

3. **Immigration Policy Changes**
   - Thai immigration policies are fluid
   - Official sources recommended
   - Nothing guaranteed or promised

4. **Personal Circumstances Vary**
   - Each visa case is unique
   - Individual situations differ
   - Professional advice essential

5. **No Liability**
   - CMLocals not responsible for consequences
   - Use information at own risk
   - Independent verification essential

6. **External Links**
   - Not responsible for third-party content
   - Links provided for convenience only
   - Third-party policy acknowledgment

7. **Visa Requirements**
   - Requirements subject to change
   - Embassy/immigration office authority
   - Always verify with official sources

---

## Styling & Typography

**Colors:**
- Dark base: `#0D1117` (hero background)
- Primary accent: `#4F46E5` (section headings, links)
- Body text: `#374151` (var(--c-body))
- Muted text: `#6B7280` (var(--c-muted))

**Typography:**
- Display (headings): Newsreader (serif)
- Body: DM Sans (sans-serif)
- Hero H1: `clamp(2.2rem, 4vw, 3rem)`
- Section H2: `1.75rem`
- Body text: `1rem` with `line-height: 1.75`

**Spacing:**
- Container max-width: 900px (slightly wider than article pages)
- Horizontal edge: `var(--edge)` (clamp responsive padding)
- Section padding: `clamp(2.5rem, 4vw, 3.5rem)`
- Line height: 1.75 (legal content readability)

**Layout:**
- Full-width hero section
- Centered content container below hero
- Footer matches homepage footer style
- Sticky header with homepage styling

---

## File Structure

```
pages/
├── privacy-policy.html
├── terms-of-service.html
└── disclaimer.html
```

---

## Technical Implementation

- **Template Base:** Homepage (index.html) color tokens and typography system
- **Reusable Elements:** Header, footer, CSS variables, button styles
- **Responsive:** Mobile-first, clamp() functions for fluid scaling
- **Accessibility:** WCAG AA contrast ratios, semantic HTML, proper heading hierarchy
- **SEO:** Proper title tags, meta descriptions, schema markup

---

## Success Criteria

✓ All three pages created with comprehensive legal coverage
✓ Consistent visual design matching homepage
✓ Responsive across mobile, tablet, desktop
✓ WCAG AA accessibility standards
✓ Proper internal linking (footer links, navigation)
✓ Fast load times (minimal dependencies)

---

## Next Steps

1. Create implementation plan with file-by-file breakdown
2. Build three pages with hero + content structure
3. Integrate with homepage header/footer
4. Add footer links and navigation references
5. Test responsive behavior and accessibility
