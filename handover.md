# HANDOVER cmlocals

Sliding session log. Newest entry first. Update at end of every session.

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
