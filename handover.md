# HANDOVER cmlocals

Sliding session log. Newest entry first. Update at end of every session.

## Current State (11/07/2026, later session)
- Mobile header sticky positioning was silently broken by `overflow-x: hidden` on `body` (an ancestor's non-visible overflow kills `position: sticky`). Fixed by switching `.site-header` to `position: fixed` under 1024px, with `body { padding-top: 76px }` to compensate. See css/mobile.css.
- progress-bar.js had a stale-cache bug: `documentHeight` was computed once on load and only refreshed on `resize`, so any page whose height changed post-load (lazy content, fonts, accordions) reported wrong scroll progress. Now recalculates `documentHeight` inside `updateProgress()` every call, plus added a `load` listener and a `ResizeObserver` on `document.body` to catch layout shifts resize doesn't fire for.
- `<script src="shared/js/progress-bar.js">` (and the `../../shared/...` relative variants on nested pages) were breaking on non-root pages — fixed to root-relative `/shared/js/progress-bar.js` across all 103 pages site-wide.
- Committed and pushed to origin/master, commit c373e0b (103 files changed, 241 insertions, 128 deletions).

## Next Steps
- Visually verify mobile header behaviour (fixed position, no content jump) and progress bar accuracy on a long page, in a real browser — not tested live since dev servers aren't run per project rules.
- Visually verify search.html nav (desktop + mobile) in a real browser before next deploy; not tested live since dev servers aren't run per project rules.
- mojibake_report.txt in the project root is a leftover scan artifact (untracked) - safe to delete once confirmed no longer needed.
- Check PHASE2-EXECUTION-CHECKLIST.md for outstanding outreach items before starting new work.

## Session Log
- 11/07/2026 (later) | Fixed mobile sticky header (overflow-x:hidden on body was killing position:sticky — switched to fixed), fixed progress-bar.js stale documentHeight cache, changed script src to root-relative across 103 pages so it resolves correctly on nested URLs. Committed and pushed (c373e0b).
- 11/07/2026 | Fixed mojibake corruption in 15 pages, rebuilt search.html nav to match site template, fixed dead analytics token on search.html. Committed and pushed (1f52c68).
- 07/07/2026 | Retrofit: rules.md and handover.md created, seeded from the PRD and phase documents in the folder.
