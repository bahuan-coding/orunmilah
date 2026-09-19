# Building the Welcome Kit

Source of truth: `welcome-kit/*.md`. Output: `dist/` (ignored by git).

## Commands

- First time: `npm install` (installs `marked`).
- Check: `node scripts/build-kit.mjs check` — exits non-zero on any failure; prints one line per check.
- Build: `node scripts/build-kit.mjs build` — runs check first, then writes one PDF per document and `dist/SambaPay-Welcome-Kit.pdf`.

## What check verifies

1. Every `welcome-kit/NN-*.md` starts with `# NN · Title`, has a blank line 2 and `Status: Settled|In discussion|Open` on line 3.
2. No line contains André Silva's name together with a rank word (the list is `TITLE_WORDS_KIT` inside the script). The same test runs over `company-os/` and `.cursor/skills/` with `TITLE_WORDS_OS`. The rule file `.cursor/rules/sambapay-voice.mdc` is excluded on purpose.
3. Word count: 650 maximum; 1,800 for `04` and `09`. The glossary keeps every term in full; 06 keeps the eight titled roles in full. Do not cut facts to hit the old 600 / 1,600 caps.
4. No emojis, no exclamation marks.
5. Portuguese leakage: none of the words " não ", " você ", " também ", " então ", " porque ", " para " appear (with spaces around them).
6. Glossary coverage: every jargon term in the fixed list that appears in `01`–`08` has an entry in `09-glossary.md`.
7. Board view: none of `SPA`, `Side Letter`, `Exhibit E`, `Units`, `Group Holdings`, the payroll run-rate or the legacy-balance figures appear in any kit file (list `BOARD_ONLY` in the script).

## Fixing failures

- Status line missing → add line 3 exactly. Word count over the cap → raise the cap in `scripts/build-kit.mjs`, do not cut facts. Glossary → add the term to `09` in one sentence. Title near the name → remove the title, keep the name.

## PDF engine

`marked` converts Markdown to HTML with embedded CSS; Google Chrome headless prints it to PDF (`--headless=new --print-to-pdf`). Chrome path: `/usr/bin/google-chrome`. If Chrome is missing, install it or set `CHROME=/path/to/chrome`.
