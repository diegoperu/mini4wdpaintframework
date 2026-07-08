# Instructions for Claude Code (engineering assistant on this repo)

This file guides Claude Code when acting as software-engineering assistant on the
Mini4WD Manual SDK repository itself (docs, prompts, framework structure, releases).
It is separate from `AI_ENTRYPOINT.md`/`BOOTSTRAP.md`, which govern the AI persona that
*uses* the SDK to generate manual content — this file is about maintaining the SDK.

## Roadmap discipline

Before implementing a new feature or structural change, check `ROADMAP.md`:

- If the work overlaps a roadmap item, say so explicitly and ask whether to follow the
  roadmap's stated order or bring the item forward now.
- Flag conflicts or precedence: if the requested change depends on something roadmap
  lists as unscheduled or later, or if doing it now would make a planned item harder
  (or easier) to build later, surface that trade-off before implementing.
- If a change is genuinely new (no roadmap overlap), proceed normally, but consider
  whether it should be added to `ROADMAP.md` for future reference.
- Keep `ROADMAP.md` in sync when scope decided in conversation changes it — don't let it
  drift the way it did before the 2026-07-03 rewrite (see the note at the top of that file).

## Current architecture state (v2.5.5)

- Render Engine is split: `Scripts/render_page.py` (Jinja2/HTML/CSS + Playwright/Chromium)
  deterministically renders all page text/layout straight from `content.yaml` — zero AI,
  zero hallucination risk. AI is only used for single isolated illustrations (cover,
  orthographic views, detail photos), one per chat, via prompts in the per-project
  `MISSING_IMAGES_PROMPT.md`. Don't suggest going back to whole-page AI rendering — it
  was tried and abandoned (see `Docs/LOCAL_RENDER_NODE.md`, `UAT/UAT-002.md`).
- PDF export (fast preview): `Scripts/render_page.py {Model} {Variant} pdf` renders every
  page and merges them via `pdfunite` into one file in the project folder. No AI, no chat.
  This is separate from the formal multi-variant (screen/print/archive CMYK+bleed)
  production export in `Core/PDF_MASTER.md`, which is unchanged.
- Fonts are embedded as base64 `@font-face` inside `render_page.py` — Playwright's
  sandboxed Chromium has no system fonts, so a bare `font-family` name silently
  falls back. Font files live in `Assets/DesignSystem/Typography/Fonts/`.
- `Documentation/QualityManagement/` (20-doc QMS) is now the authoritative source for
  release classification — check `01_RELEASE_POLICY.md` (Patch/Minor/Major criteria)
  before bumping the version, not just gut feeling.
- Gemini is supported for Phase 4 only (single-illustration generation, `UAT-004`).
  Phase 1-3 (text/bootstrap) remain unverified for Gemini — don't extend that claim.
- Real project structure is `Projects/{Model}/{Variant}/Images/` (flat — reference
  photos and generated illustrations together). `ApprovedImages/` was planned in
  early v2.5.0 docs but never implemented; don't reintroduce it or trust old docs
  that mention it.
