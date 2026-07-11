# HANDOVER cmlocals

Sliding session log. Newest entry first. Update at end of every session.

## Current State (12/07/2026, later session)
- Mobile menu sticky-header follow-up. Header pinning was already solid (`.site-header { position: fixed !important }` in css/mobile.css beats every page's local `position: sticky`), but hardened two weak spots and closed three gaps:
  - css/mobile.css: `.site-header` z-index changed to `1001 !important` (11 pages had an inline `z-index: 1000` loaded after mobile.css that only cleared the drawer by 1).
  - css/mobile.css: `.nav-mobile` gained a `100dvh`-based max-height (falls back to the existing vh value on browsers without dvh support), since plain `100vh` ignores the mobile URL bar and could clip the bottom of the drawer while the scroll lock is active.
  - 4 pages had their own bare inline hamburger-toggle script with no scroll lock and no single-open accordion behaviour: guides/border-runs, guides/business-visa-work-permit, guides/ed-vs-dtv-comparison, visas/comparison-matrix. Removed the inline script, added the shared `shared/js/header-handler.js` include to match the other 96 pages.
  - immigration/queue-strategy/index.html: hamburger button and drawer markup existed but no script loaded it at all, dead button. Added the shared header-handler.js include.
  - resources/index.html: hamburger button existed with no `#mobile-nav` element and no script. Added the full mega-menu drawer markup (copied from checklists/index.html, all root-relative links so no path changes needed) plus the shared header-handler.js include.
- Not touched: the duplicated "CANONICAL HEADER + NAV CSS (auto-injected)" inline block still present per-page (some pages carry two generations of it, an old `position: absolute` version and a newer `position: fixed` one). Currently neutralised by the mobile.css `!important` overrides but worth consolidating in a future pass.

## Current State (12/07/2026)
- Fixed a site-wide unescaped-ampersand bug: bare `&` in visible text (nav labels, headings, body copy) across all 103 live pages was invalid HTML — should have been the `&amp;` entity. Wrote a script that walks each file, splits tags from text nodes, and only replaces `&` inside text nodes/attributes (not inside `<script>`/`<style>` blocks, so JS `&&` operators and JSON-LD strings were left untouched — verified byte-identical before/after on all raw blocks). 1,609 replacements across 103 files.
- Same commit also carried forward in-progress header/footer/nav changes that were already sitting uncommitted in the working tree before this session started: `fetchpriority="high"` on the header logo `<img>`, several new links added to the Guides mega-menu (DTV 180-Day Extension, DTV vs Business Permit, Border Runs Strategy, ED Visa Cost & Budget, Business Visa & Work Permit, ED vs DTV Comparison), footer logo path fixed from relative to root-relative on at least one page, and a malformed `</nav>` tag (missing newline before the search-icon markup) cleaned up.
- Committed and pushed: 415e91c (102 files, +4179/-1920).
- Excluded from the ampersand fix: `_archive/` and `docs/index.backup.html` (not live pages).

## Current State (11/07/2026, later session)
- Sticky nav header (desktop AND mobile) fixed. Root cause: `overflow-x: hidden` on `body` in css/mobile.css has no media query, so it silently breaks `position: sticky` on `.site-header` at every viewport width, not just mobile. First pass only scoped the `position: fixed` override to `max-width: 1023px`, which left desktop still broken.
  - Fix: `.site-header { position: fixed !important }` now applies unconditionally in css/mobile.css, with `body { padding-top: ... }` tracking the header's own two real height states — 71px above 960px (70px `.header-inner` + 1px border), 85px at/below 960px (0.75rem top/bottom padding + 60px `.header-inner` + 1px border).
  - Confirmed no per-page `!important` on `position` fights this — some inner pages (e.g. immigration/tm30-registration) redeclare `.site-header { position: sticky }` inside their own `max-width:1023px` block with a different z-index/padding, but none use `!important`, so the shared mobile.css rule always wins.
  - Confirmed header-handler.js only toggles a `.scrolled` class (for a shadow effect that currently has no CSS rule attached — separate minor gap, not a positioning issue) and never sets inline `style.position`.
  - Committed and pushed, commit 7d9d128.
- Mobile header sticky positioning was silently broken by the same `overflow-x: hidden` cause. Fixed by switching `.site-header` to `position: fixed`. See css/mobile.css.
- progress-bar.js had a stale-cache bug: `documentHeight` was computed once on load and only refreshed on `resize`, so any page whose height changed post-load (lazy content, fonts, accordions) reported wrong scroll progress. Now recalculates `documentHeight` inside `updateProgress()` every call, plus added a `load` listener and a `ResizeObserver` on `document.body` to catch layout shifts resize doesn't fire for.
- `<script src="shared/js/progress-bar.js">` (and the `../../shared/...` relative variants on nested pages) were breaking on non-root pages — fixed to root-relative `/shared/js/progress-bar.js` across all 103 pages site-wide.
- Committed and pushed to origin/master: c373e0b (progress-bar/paths, 103 files), 32196cc (handover), 7d9d128 (desktop sticky fix).

## Next Steps
- Verify the new Guides mega-menu links (DTV 180-Day Extension, DTV vs Business Permit, Border Runs Strategy, ED Visa Cost & Budget, Business Visa & Work Permit, ED vs DTV Comparison) all resolve correctly and match the intended nav structure — these were folded into this session's commit as-is from a prior uncommitted state, not authored or reviewed this session.
- Visually verify sticky header on both desktop and mobile, and progress bar accuracy on a long page, in a real browser — not tested live since dev servers aren't run per project rules.
- Minor unrelated finding: `.site-header.scrolled` class is toggled by JS but has no CSS rule — the intended scroll shadow effect currently does nothing. Not fixed, out of scope for the sticky-nav ask.
- Minor unrelated finding: `.mobile-nav { inset: 64px 0 0 0 }` on index.html assumes a 64px header, but the real mobile header height is 85px — could leave a ~21px gap/overlap when the mobile menu opens. Not fixed, out of scope.
- Visually verify search.html nav (desktop + mobile) in a real browser before next deploy; not tested live since dev servers aren't run per project rules.
- mojibake_report.txt in the project root is a leftover scan artifact (untracked) - safe to delete once confirmed no longer needed.
- Check PHASE2-EXECUTION-CHECKLIST.md for outstanding outreach items before starting new work.

## Session Log
- 11/07/2026 (later, round 2) | Desktop sticky header was still broken after round 1 — overflow-x:hidden has no media query so it broke sticky at all widths, not just mobile. Made position:fixed unconditional in css/mobile.css. Committed and pushed (7d9d128).
- 11/07/2026 (later) | Fixed mobile sticky header (overflow-x:hidden on body was killing position:sticky — switched to fixed), fixed progress-bar.js stale documentHeight cache, changed script src to root-relative across 103 pages so it resolves correctly on nested URLs. Committed and pushed (c373e0b).
- 11/07/2026 | Fixed mojibake corruption in 15 pages, rebuilt search.html nav to match site template, fixed dead analytics token on search.html. Committed and pushed (1f52c68).
- 07/07/2026 | Retrofit: rules.md and handover.md created, seeded from the PRD and phase documents in the folder.
