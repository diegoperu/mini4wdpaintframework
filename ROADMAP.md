# Roadmap

This document describes the planned direction for Mini4WD Manual SDK. It is a living document and reflects current intentions, not binding commitments.

To propose a feature, open a GitHub Issue and apply the `roadmap` label. See **How to Propose a Feature** at the bottom of this document.

> **2026-07-03 — Full revision.** Previous versions of this file had drifted badly from
> reality: duplicated v2.3.0/v3.0.0 sections with conflicting scopes, "Planned" entries
> for versions that had already shipped with completely different content, and no entry
> at all for the current next release. This revision reconciles the roadmap against
> `ReleaseInfo.yaml`, `SDK_CONTEXT.yaml`, and `CHANGELOG.md`, which are the actual sources
> of truth for what shipped. Going forward, keep this file in sync at every release —
> see `Documentation/QualityManagement/01_RELEASE_POLICY.md`.

---

## Vision

Mini4WD Manual SDK aims to become the canonical open framework for producing professional, archival-quality painting manuals for scale model hobby projects. The goal is a library of approved manuals, a community of contributors across multiple countries, and tooling that makes manual production as fast and consistent as a software build pipeline.

The SDK must remain model-agnostic at the AI layer. No feature will be added that requires a specific AI provider. See `Docs/RUNTIMES.md` for supported runtimes and `UAT/UAT-002.md` for why Gemini was degraded to unsupported.

---

## Released

| Version | Codename | Date | Theme |
|---|---|---|---|
| 2.1.0 | Foundation | 2026-06-30 | Initial release — Core framework, PromptEngine, Design Tokens, Component System |
| 2.2.0 | Pipeline | 2026-06-30 | Build pipeline, Config layer, Test suites, Knowledge base, AI Operating Rules |
| 2.3.0 | Editorial | 2026-07-01 | Text Engine, Italian-only language policy, LOAD sequence, editorial knowledge base |
| 2.4.0 | CMS | 2026-07-01 | CMS layer (`ApprovedAssets/`), content.yaml as source of truth, page lifecycle |
| 2.4.1 | Operator | 2026-07-02 | UX & Operator Workflow — START_HERE, OperatorGuide/, runtime-aware docs, UAT-001 fixes |
| 2.5.0 | MultiProject | 2026-07-03 | Multi-Project Content Isolation — per-variant `Projects/{Model}/{Variant}/` structure |

Full detail for each release: `CHANGELOG.md`. Machine-readable metadata for the current and prior releases: `ReleaseInfo.yaml`. Pre-2.1.0 history (1.0.0–2.0.0) exists only in `CHANGELOG.md` as early scaffolding and predates the current release process.

Governance note (2026-07-03): Gemini was degraded from "planned runtime" to "not supported" following 3 failed render attempts on UAT-002 (hallucinated output, leaked metadata, off-prompt responses). See `Docs/RUNTIMES.md` and `UAT/UAT-002.md`. This roadmap does not list unsupported runtimes as a target.

---

## Next Release — v2.6.0 (Planned)

**Target:** Q3 2026

- `Compiler/` — automated pipeline executor (Project Loader, Context Builder, Page Generator, QA Engine, PDF Assembler)
- Prompt Orchestrator — manages the LOAD sequence automatically instead of manual per-phase prompting
- `Documentation/OperationalManual/` — update all path references to v2.5.0 two-level project structure
- Icon Library — 15 SVG icons, replacing current Unicode fallbacks (see `Assets/DesignSystem/Icons/README.md`)
- Multi-language support: Italian, Japanese, English as selectable whole-document locales
- `Docs/tutorial/` — end-to-end tutorial documents
- Release system automation

> ⚠️ **Known drift:** `ReleaseInfo.yaml → next_release` and `SDK_CONTEXT.yaml → roadmap.next_planned`
> list slightly different feature sets for v2.6.0 (the list above is their union). Reconcile
> both files to a single authoritative list before v2.6.0 planning locks.
>
> ⚠️ **Open question — multi-language vs. RULE-058:** `Core/DESIGN_LANGUAGE.md` RULE-058
> mandates zero Japanese characters in any text element of an Italian manual. Multi-language
> support must mean a **whole document rendered in one selected locale** (a Japanese-locale
> manual has zero Italian text, and vice versa) — never mixed scripts within a single document.
> `Config/LANGUAGE_POLICY.yaml` is currently Italian-only by design (v2.3.0 architecture
> change) and will need explicit per-locale policy files before this feature can start.

---

## Planned — Unscheduled

Features with committed scope but no assigned version yet.

### Multi-Style / Theme System
Currently `Core/DESIGN_LANGUAGE.md` defines one fixed visual identity applied to every
project regardless of paint scheme mood (Rule 1/11/12: Tamiya-catalog aesthetic, white
background, function over fashion). Add a `paintScheme.style` or `project.theme` field in
`PROJECT.yaml` allowing a project to select among multiple sanctioned visual themes, each
with its own token set in `Assets/DesignSystem/Tokens/`.

Originated from a 2026-07-03 UX review of two designer mockups (`Brocken Gigant` cover +
P002) that proposed a dark/high-contrast/action-poster style incompatible with the current
default skin. Two new components are candidates to ship alongside this system, not before it
(they only make sense once a manual can opt into a non-neutral tone):
- **Painting Highlight** — 3-photo glamour grid with title + caption, tone-dependent
- **CTA footer banner** — motivational closing strip, tone-dependent

Each new theme must still pass Rule 1 (function over decoration) for whatever tone it targets.

**Manual frame chrome must become config-driven, not prompt-hardcoded.** Today the page
frame itself (background, header/footer color) is literal text in the Fase 4 prompt —
e.g. `Docs/AI_BOOTSTRAP_PROMPT.md`: *"Sfondo bianco puro. Pannello header viola
(token.PrimaryViolet)"*, duplicated in `OperatorGuide/Runtimes/Claude_Code.md` 10c. There
is no config layer resolving which token applies; the prompt names `PrimaryViolet`
directly. This must move to a per-project (or per-series) config value that the prompt
*resolves* instead of hardcodes.

**New hierarchy level: series/collection ("collana").** A theme should be settable once
for a whole series of models and inherited by every project under it, not just per single
project. This requires a config layer above `PROJECT.yaml` that does not exist today —
the SDK only has `Projects/{Model}/{Variant}/`, no collection/series grouping. Candidate
shape: a `Collections/{CollanaName}/COLLECTION.yaml` (or similar) declaring the default
theme, with `PROJECT.yaml` gaining an optional `collana` reference and an optional
override if a single project needs to deviate from its series' theme.

### P002 Layout — Compact Orthogonal View Row
Independent of the theme system. Current P002 shows front/side/top renders as three large
vertical panels. Alternate layout: same `renders.front/side/top` data from `content.yaml`,
displayed as a compact thumbnail row alongside the color legend. Pure layout variant, no new
content.yaml fields, no theme dependency — can ship whenever.

### Extended Page Set (P011–P015)
- P011: Tools & Equipment reference page
- P012: Common Mistakes & Troubleshooting
- P013: Advanced Techniques (airbrushing, candy coat, metallics)
- P014: Custom Part Painting (chassis, rollers, motor cover)
- P015: Photography & Display guide

### Component Extensions (C016–C020)
- C016: Comparison Table (before/after paint stages)
- C017: Difficulty Rating badge
- C018: Compatibility Matrix (paint brands)
- C019: QR Code block (links to video companion)
- C020: Author/Contributor credit block

### Automation & Tooling
- Automated PDF pipeline (pandoc + LaTeX, or headless Chromium/Puppeteer)
- `Build/CI.md` — CI/CD integration guide
- `Config/environments/` — local dev/staging/production overrides
- Automated `Tests/ContentValidation.md` and `Tests/TextValidation.md` runners (script-based, not manual AI checklist)
- Automated `ApprovedAssets/index.yaml` / project index updater

### Platform Features (Breaking — would require a MAJOR version bump)
- Web-based Prompt Runner — browser tool that fills `PromptEngine/` templates from `PROJECT.yaml`, no server required
- Plugin system for custom component/page types via `plugins/` directory (`plugin.yaml` manifest; `COMPONENT_SYSTEM.md` schema gains a `source` field)
- Token Inheritance — `PROJECT.yaml` gains optional `tokenOverrides`, changing token resolution order (project overrides → SDK defaults)

---

## Long-Term Vision

By full maturity, the SDK should support:
- A large library of approved model manuals across multiple contributors and countries
- Multiple languages as first-class, non-mixed locales (see multi-language open question above)
- An automated end-to-end pipeline: `PROJECT.yaml` → published PDF in one command
- A community governance model for reviewing and merging contributed manuals
- Extensibility beyond Mini4WD to any Tamiya kit family

### Community Model Library
Public repository of approved manuals contributed by the community. Submission via PR to an approved-manuals directory with completed `PROJECT.yaml` and QA log; community review before merge; web index of available manuals.

### Video Manual Support
Page specifications for video companion guides, not just static PDF: storyboard template, script template, frame-by-frame annotation system.

### Tactile/Print-Optimized Variant
High-contrast print variant for accessibility; spiral-bound single-page print format; lamination-safe PDF variant (no dark backgrounds on the back of a page).

### CLI Tool
Command-line interface (`mini4wd-sdk init`, `mini4wd-sdk qa`, `mini4wd-sdk export`) that reads `PROJECT.yaml`, validates against schema, and outputs a QA report.

---

## What Will Not Be Added

- **Model-specific content** — The SDK contains no Mini4WD model data. Models live in `Projects/`.
- **AI provider integrations** — No API keys, no provider SDKs, no direct AI calls. The SDK is prompt text, not software.
- **Paint brand recommendations** — The SDK describes how to represent colors; it does not endorse brands.
- **Racing or performance content** — This SDK covers painting manuals only. Motor tuning, gear ratios, and track setups are out of scope.

---

## How to Propose a Feature

1. Open a GitHub Issue with the title format: `[Feature] Short description`
2. Apply the `roadmap` label
3. In the issue body, describe:
   - **Problem:** What cannot be done today?
   - **Proposed solution:** What should the SDK support?
   - **Affected components:** Which `Core/` documents, pages, or components are involved?
   - **Fits the philosophy?** How does it align with `Core/DESIGN_LANGUAGE.md`?
   - **Breaking?** Would this require a MAJOR version bump?
4. Reference any relevant ADRs in `STYLE_DECISIONS.md`.
5. Maintainers will triage and assign to a version milestone, or mark `wontfix` with a reason.
