# Legacy Mission Control — Prompt Library

Legacy Mission Control is a static prompt library for daily operator use. It ships as an HTML file with embedded prompt data and local assets, cockpit-style glass UI, persistent controls, TEAR theme palettes, and mobile viewport fit behavior.

## What this app provides

- 973 prompt payloads embedded directly in the page.
- Category filters, live search, and persistent sort order.
- Prompt detail modal with copy-to-clipboard workflow and usage tracking.
- Favorites, Saved/All view modes, JSON export, and durable local state.
- TEAR palettes: Light, Dark, System, FLOYD, Red Graphite, High Contrast, Charcoal, Solarized Light, Solarized Dark, and Dracula.
- Mobile-first viewport fitting using dynamic viewport units and safe-area insets.
- Keyboard-visible focus states, skip link, named controls, and modal focus behavior.

## Requirements

- A modern browser with JavaScript enabled.
- Keep the checked-in `assets/` directory next to the HTML file.
- No network access, local server, package install, build step, or runtime secrets are required.

## Open locally

From macOS Finder or a terminal, open the HTML file directly:

```bash
open "file:///Volumes/Storage/PromptBook/mission-control-prompt-library.html"
```

To force Google Chrome Beta:

```bash
open -a "Google Chrome Beta" "file:///Volumes/Storage/PromptBook/mission-control-prompt-library.html"
```

## Daily operator workflow

### 1. Discover payloads

Use the category pills, search box, and sort selector to narrow the library. The status line reports visible payloads, active category, search term, sort mode, and saved count.

### 2. Inspect and copy

Open a payload card to inspect its contract and content in the modal. The copy action writes the payload to the clipboard, increments local usage count, and shows toast feedback.

### 3. Save, export, and theme

Favorite payloads for the Saved view, export the current saved set as JSON, and select any TEAR palette from the theme selector. Favorites, view mode, sort mode, search/category state, usage counts, and theme selection persist in browser local storage.

## Configuration and storage

The app currently requires no runtime environment variables. `.env.example` exists only to document that future configuration must use safe placeholder values.

Browser local storage keys used by the app:

| Key | Purpose |
|---|---|
| `legacy_mc_usage` | Copy/open usage counts by payload. |
| `legacy_mc_favs` | Favorite payload IDs. |
| `legacy_mc_category` | Last active category. |
| `legacy_mc_search` | Last search query. |
| `legacy_mc_sort` | Last sort mode. |
| `legacy_mc_view` | Last All/Saved view mode. |
| `legacy_mc_theme` | Last selected TEAR theme. |

If a browser blocks or clears local storage, the app still renders but preferences reset to defaults.

## Mobile viewport behavior

Mobile screens are expected to fit the active device viewport without horizontal page overflow. The app uses `100dvh`, safe-area inset variables, constrained panels, and internal scrolling for dense mobile regions such as filters, command controls, prompt cards, and modals.

Verification should include at least these viewport sizes:

- 320 × 568
- 390 × 844
- 430 × 932

Expected result: no horizontal overflow, header toggle visible, bottom navigation inside the viewport, and modal content internally scrollable without clipping.

## Testing and QA

Run these checks before release or after any UI/data change.

### Prompt source maintenance

`RUST-PROMPTS.md` preserves the human-readable source for prompt IDs 774–873.
`data.ts` contains the two harness prompt categories at IDs 874–973. Validate and
convert the TypeScript prompt sheet with:

```bash
uv sync --frozen
uv run --frozen python validate-prompt-sheet.py data.ts
uv run --frozen python convert_prompts.py data.ts > /tmp/promptbook-prompts.js
uv run --frozen python -m unittest discover -s tests -v
uv run --frozen ruff check .
uv run --frozen ruff format --check .
```

The converter writes compact JavaScript objects to standard output for review
and insertion into the static application; it does not modify the HTML.
It accepts normal TypeScript trailing commas and escapes HTML script end tags
inside generated string literals.

### JavaScript syntax validation

```bash
node - <<'NODE'
const fs = require('fs');
const html = fs.readFileSync('mission-control-prompt-library.html', 'utf8');
const scripts = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)]
  .map(m => m[1]);
for (const [index, script] of scripts.entries()) {
  new Function(script);
  console.log(`script ${index + 1}: syntax ok (${script.length} chars)`);
}
console.log(`scripts validated: ${scripts.length}`);
NODE
```

### Whitespace and patch hygiene

```bash
git diff --check -- mission-control-prompt-library.html README.md CHANGELOG.md qa/final-push-20260509-094455/report.md .env.example
```

### Human workflow regression

Use a browser automation pass to verify:

1. 973 payloads render initially.
2. Category filter, search, and sort produce non-empty filtered results.
3. Modal opens, labels itself with the prompt title, and focuses the close button.
4. Copy action changes usage state and displays feedback.
5. Favorites persist and Saved view shows the saved payload.
6. Theme selector lists all 10 TEAR themes and persists the chosen palette after reload.
7. Export produces feedback.
8. Empty search state renders clearly.
9. Duplicate IDs, unnamed buttons, and unnamed inputs/selects remain at zero.
10. Mobile viewport matrix has no horizontal overflow.

### Agent-browser smoke test

```bash
agent-browser --session promptbook-release open "file:///Volumes/Storage/PromptBook/mission-control-prompt-library.html"
agent-browser --session promptbook-release wait --load networkidle
agent-browser --session promptbook-release screenshot --annotate "/Volumes/Storage/PromptBook/qa/final-push-20260509-094455/screenshots/release-smoke.png"
agent-browser --session promptbook-release errors
agent-browser --session promptbook-release console
```

## Security and secrets hygiene

- No runtime secrets are required.
- `.env*.local` files are ignored and must never be committed.
- `.env.example` must contain placeholders only.
- Release scans should check staged files and the working tree for API keys, tokens, passwords, private keys, JWTs, connection strings, and provider credentials.
- Prompt payload text may intentionally contain placeholder strings such as `{signed_jwt}` as examples. Treat these as non-secrets only when they are template placeholders, not live credentials.

## Static styling

`assets/tailwind-3.4.17.css` is the compiled, minified Tailwind stylesheet used
by the page. It is checked in so opening the page never depends on the Tailwind
CDN or a local build tool. The page uses its declared system font fallbacks and
does not fetch web fonts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Theme or favorites reset | Browser local storage was cleared or blocked. | Re-select the theme and favorites; allow local storage for the file origin. |
| Layout is unstyled | The `assets/` directory is missing or was moved away from the HTML file. | Restore `assets/tailwind-3.4.17.css` beside the application. |
| Copy does not work | Browser clipboard permission blocked the file origin. | Use a browser that permits clipboard writes for the opened file, or serve the file from a trusted local/static origin. |
| Mobile controls feel clipped | Viewport not reloaded after browser chrome/orientation changes. | Reload and rerun viewport matrix; file a regression if horizontal overflow appears. |

## Release checklist

- JavaScript syntax validation passes.
- `git diff --check` reports no output.
- Human workflow regression passes for discovery, inspect/copy, and saved/export/theme persistence.
- Mobile viewport matrix passes at 320 × 568, 390 × 844, and 430 × 932.
- Agent-browser console has no runtime errors or warnings.
- Redacted secret scan reports no live secrets.
- QA evidence and changelog entries are updated before commit.
