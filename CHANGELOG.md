# Changelog

- [2026-07-15] Repaired prompt tooling and made the browser app self-contained
    - What changed: Hardened TypeScript prompt parsing and validation, escaped generated script end tags, added exact Python tooling, compiled Tailwind 3.4.17 into a checked-in stylesheet, removed remote runtime assets, restored the mobile category/favorite row, and corrected themed primary text colors.
    - Why: Review found parser, validator, and generated-script defects. Rendered mobile testing then found that CDN failure destroyed the layout, mobile users could not add favorites, and High Contrast cards used light text on a light panel.
    - Files/areas touched: Prompt conversion and validation tools, tests, static app HTML and CSS, documentation, and QA evidence.
    - Tests run: Nine Python unit tests; prompt validation and source/embedded parity; Ruff; Markdownlint; JSON and JavaScript parsing; mobile viewports at 320×568, 390×844, and 430×932; desktop at 1440×1000; modal, search, favorite, Saved view, and theme persistence workflows; Gitleaks.
    - Result: 100 prompt-sheet entries validate with zero errors or warnings, all 973 embedded prompts render, the app has no remote runtime dependency, tested viewports have no horizontal overflow, and the browser reports no runtime errors or warnings.

- [2026-05-09 09:44:55 EDT] Imported all TEAR app themes into Mission Control
    - What changed: Added Light, Dark, System, FLOYD, Red Graphite, High Contrast, Charcoal, Solarized Light, Solarized Dark, and Dracula palettes; added a persistent TEAR theme selector; wired theme variables into the glass cockpit UI.
    - Why: Human operators need all available TEAR palettes usable from the single-file app, with durable selection across reloads.
    - Files/areas touched: `mission-control-prompt-library.html`
    - Tests run: Node inline script syntax validation; `git diff --check`; Puppeteer theme selector verification.
    - Result: 10/10 theme options rendered; Dracula and Solarized Dark changed computed palette values and persisted to localStorage.

- [2026-05-09 09:44:55 EDT] Started final push hardening cycle
    - What changed: Created QA evidence directory and baseline QA report for the final push workflow.
    - Why: Release readiness requires durable evidence, known issue tracking, and human-workflow testing artifacts.
    - Files/areas touched: `qa/final-push-20260509-094455/report.md`
    - Tests run: Puppeteer baseline pass; agent-browser initial snapshot and screenshot.
    - Result: Baseline test identified one invalid test path and drove a corrected workflow test.

- [2026-05-09 09:44:55 EDT] Fixed mobile header toggle visibility
    - What changed: Added a mobile media rule that displays the collapsible header toggle below the Tailwind `sm` breakpoint.
    - Why: Mobile verification showed the bottom navigation was visible, but the header collapse control was hidden by a custom `.header-toggle { display: none; }` rule.
    - Files/areas touched: `mission-control-prompt-library.html`
    - Tests run: Mobile viewport check before fix.
    - Result: Fix applied; post-fix verification pending.

- [2026-05-09 09:44:55 EDT] Removed local secret-bearing env file and added safe example
    - What changed: Deleted ignored `.env.local` after redacted secret scan flagged a JWT-shaped value; added `.env.example` with no required secrets and explicit safe-placeholder guidance.
    - Why: Release readiness requires no secrets in repo-local configs, logs, or committed files; future contributors need a safe configuration template.
    - Files/areas touched: `.env.local`, `.env.example`
    - Tests run: Redacted secret scan across tracked/untracked/non-gitignored and ignored local files; `git check-ignore -v .env.local`; `git ls-files -- .env.local`.
    - Result: `.env.local` was ignored and untracked, then removed; `.env.example` created without secret values.

- [2026-05-09 09:50:45 EDT] Enforced mobile viewport autoresize and fit behavior
    - What changed: Added mobile dynamic-viewport sizing rules for the app shell, hero cockpit, command panel, cards, modal, selectors, and bottom navigation; replaced modal `92vh` cap with `100dvh` safe-area-aware sizing.
    - Why: Each mobile app screen must resize to fit the active device viewport without horizontal overflow, hidden controls, or modal/card clipping.
    - Files/areas touched: `mission-control-prompt-library.html`
    - Tests run: Puppeteer mobile viewport matrix at 320×568 and 390×844; Node inline script syntax validation; `git diff --check`.
    - Result: No horizontal overflow, no non-filter overflowing elements, header toggle visible, bottom nav fit to viewport, modal fit within viewport, filter list constrained with internal vertical scrolling, syntax validation passed.

- [2026-05-09 10:02:38 EDT] Made prompt card category tags prominent
    - What changed: Replaced the tiny card category chip with a larger uppercase `.category-tag` treatment, stronger contrast, visible status dot, wrapping behavior, and theme-aware border/background colors.
    - Why: Daily users reported category tags were missing or visually obscured; prompt cards need category context visible at a glance.
    - Files/areas touched: `mission-control-prompt-library.html`
    - Tests run: Puppeteer UI baseline audits at 320×568, 390×844, 430×932, and 1440×900; corrected 390×844 workflow regression; Node inline script syntax validation; `git diff --check`; custom secret scan; Floyd proof runs.
    - Result: Category rail and card tags are visible without page/card overflow; 21 category pills render with first chip `All / 873`; sampled prompt cards had zero overflowing children; all visible controls are named; all interactive targets meet the 44px gate after active-state scaling; workflow regression loaded 873 payloads, filtered/searched to 96, opened/copy-ready modal, saved 1 card, persisted High Contrast, exported successfully, and rendered empty state.

- [2026-05-10] Changed category filters from hidden scroll rail to all-visible grid
    - What changed: Replaced the horizontally scrolling category rail with a wrapping grid, removed category deck clipping, and kept search/actions below the full category set.
    - Why: User inspection rejected hidden/obscured categories; all categories must be shown at once.
    - Files/areas touched: `mission-control-prompt-library.html`, `CHANGELOG.md`, `qa/final-push-20260509-094455/report.md`
    - Tests run: User visual inspection in default browser; Node inline script syntax validation; `git diff --check`; staged secret scan.
    - Result: User accepted the current all-visible category layout and requested commit.
