# Roadmap

This document describes the planned direction for Mini4WD Manual SDK. It is a living document and reflects current intentions, not binding commitments.

To propose a feature, open a GitHub Issue and apply the `roadmap` label. Include: the problem you are solving, your proposed approach, and which existing SDK components would be affected.

---

## Vision

Mini4WD Manual SDK aims to become the canonical open framework for producing professional, archival-quality painting manuals for scale model hobby projects. By 2028, the goal is a library of 200+ approved manuals, a community of contributors across multiple countries, and tooling that makes manual production as fast and consistent as a software build pipeline.

The SDK must remain model-agnostic at the AI layer. No feature will be added that requires a specific AI provider.

---

## Status Update — v2.2.0 [RELEASED]

The following v2.2.0 features are now complete:
- ✅ Build system (Build/Pipeline.md)
- ✅ Configuration layer (Config/)
- ✅ Test suite framework (Tests/)
- ✅ AI Operating Rules (Core/AI_OPERATING_RULES.md)
- ✅ Knowledge Base (Knowledge/)
- ✅ MANIFEST.yaml

---

## v2.2.0 — Planned (original scope, partially superseded above)

**Target:** Q3 2024

### Multi-language Support
- `Core/DOCUMENTATION_STYLE.md` extended with translation guidelines
- `Templates/PROJECT.yaml` gains optional `locale` field (e.g., `it`, `en`, `ja`)
- `PromptEngine/` prompts will include localization token `{{project.locale}}`
- Initial language packs: Italian (it), English (en), Japanese (ja)
- No automatic translation — manual localization only

### SVG Icon Library
- New directory: `Assets/DesignSystem/Icons/svg/`
- Icons for: Warning, Tip, Note, Step, Time, Check, Brush, Spray, Mask, Decal
- All icons at 24×24px base, scalable
- Color variants: white (on violet), violet (on white), gold (on white), red (on white)
- Usage documented in `Core/COMPONENT_SYSTEM.md` and `Assets/DesignSystem/Icons/README.md`

### Automated PDF Pipeline
- `Docs/guides/automated-pdf.md` — guide for pandoc + LaTeX pipeline
- Reference `Makefile` in `Templates/`
- CSS print stylesheet for browser-based PDF generation
- Integration guide for Affinity Publisher scripting

---

## v2.3.0 — Planned

**Target:** Q4 2024

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

---

## v3.0.0 — Planned (Breaking)

**Target:** 2025

### Web-Based Prompt Runner
- Browser application that reads PROJECT.yaml and injects tokens into PromptEngine/ prompts
- Outputs filled prompts ready to paste into any AI chat interface
- No server required — runs entirely in-browser via JavaScript

### Plugin System
- Third-party component definitions via `plugins/` directory
- Plugin manifest format: `plugin.yaml`
- Plugin registry documentation
- Breaking: `COMPONENT_SYSTEM.md` schema extended with `source` field (built-in vs plugin)

### Token Inheritance
- Projects can override individual tokens without duplicating the full token file
- `PROJECT.yaml` gains optional `tokenOverrides` block
- Breaking: token resolution order changes (project overrides → sdk defaults)

---

## Long-Term Goals (No Version Assigned)

### Community Model Library
- Public repository of approved manuals contributed by the community
- Submission process: PR to `Assets/ApprovedManual/` with completed PROJECT.yaml and QA log
- Community review process before merge
- Web index of all available manuals

### Video Manual Support
- Page specifications for video companion guides (not just static PDF)
- Storyboard template: `Templates/STORYBOARD.yaml`
- Script template: `Templates/SCRIPT.md`
- Frame-by-frame annotation system

### Tactile/Print-Optimized Variant
- High-contrast print variant for accessibility
- Spiral-bound print format (single-page, no spreads)
- Lamination-safe PDF variant (no dark backgrounds on back of page)

### CLI Tool
- Command-line interface: `mini4wd-sdk init`, `mini4wd-sdk qa`, `mini4wd-sdk export`
- Reads PROJECT.yaml and validates against schema
- Outputs QA report to `Projects/{Model}/Notes/qa_log.md`

---

## How to Propose a Feature

1. Open a GitHub Issue with the title format: `[Feature] Short description`
2. Apply the `roadmap` label
3. In the issue body, describe:
   - **Problem:** What cannot be done today?
   - **Proposed solution:** What should the SDK support?
   - **Affected components:** Which Core/ documents, pages, or components are involved?
   - **Breaking?:** Would this require a MAJOR version bump?
4. Maintainers will triage and assign to a milestone or mark `wontfix` with a reason.

---

## v2.3.0 — Automation & Tooling (Updated Scope)

**Target:** Q4 2024  
**Theme:** Automation & Tooling

### Features
- `Build/scripts/` — Shell/Python scripts for token substitution automation
- `Assets/DesignSystem/Icons/` — SVG icon library (warning, tip, info, brush, airbrush, clock, check, star, sandpaper, decal)
- Multi-language support: `Templates/PROJECT.yaml` language field activation for EN/JA/FR/DE
- `Config/environments/` — Local environment overrides (dev, staging, production)
- CI/CD integration guide (`Build/CI.md`)
- Automated QA report generator specification
- Extended Page Set (P011–P015)
- Component Extensions (C016–C020)

### Breaking Changes
None planned.

---

## v3.0.0 — Platform & Community

**Target:** 2025  
**Theme:** Platform & Community

### Features
- Web-based prompt runner (browser tool for non-technical users)
- Plugin system for custom page types (P011+)
- Community model library (centralized approved manuals registry)
- Video manual support (animated step-by-step)
- Automated PDF pipeline (headless Chromium or Puppeteer)
- API specification for SDK integrations
- Token Inheritance: Projects can override individual tokens without duplicating the full token file

### Breaking Changes
- Plugin API will require new PROJECT.yaml fields (migration guide will be provided)
- Component ID namespace may be extended with plugin prefixes
- `tokenOverrides` block in PROJECT.yaml changes token resolution order

---

## Long-Term Vision (Updated)

The Mini4WD Manual SDK aims to become the definitive open-source editorial platform for scale model painting documentation — not limited to Mini4WD but extensible to any Tamiya kit family.

By v4.0.0, the SDK should support:
- 500+ approved model manuals
- 6+ languages
- Automated end-to-end pipeline (PROJECT.yaml → published PDF in one command)
- Community governance model

---

## Contributing to the Roadmap

To propose a feature for an upcoming version:
1. Open a GitHub Issue with label `roadmap`
2. Describe the feature, use case, and how it fits the SDK philosophy (`Core/DESIGN_LANGUAGE.md`)
3. Reference any relevant ADRs in `STYLE_DECISIONS.md`
4. A maintainer will triage and assign to a version milestone

---

## What Will Not Be Added

The following are explicitly out of scope for this SDK:

- **Model-specific content** — The SDK contains no Mini4WD model data. Models live in `Projects/`.
- **AI provider integrations** — No API keys, no provider SDKs, no direct AI calls. The SDK is prompt text, not software.
- **Paint brand recommendations** — The SDK describes how to represent colors; it does not endorse brands.
- **Racing or performance content** — This SDK covers painting manuals only. Motor tuning, gear ratios, and track setups are out of scope.

---

## Status Update — v2.3.0 [RELEASED]

All v2.3.0 features are complete:
- ✅ Text Engine (Core/TEXT_ENGINE.md)
- ✅ Language Policy (Config/LANGUAGE_POLICY.yaml)
- ✅ Text Validation suite (Tests/TextValidation.md)
- ✅ Italian Knowledge Base (GlossaryIT, EditorialStyle, Terminology, ForbiddenWords)
- ✅ DESIGN_LANGUAGE update (editorial identity rules 55–65)
- ✅ STYLE_GUIDE Typography Rules
- ✅ COMPONENT_SYSTEM text source mapping
- ✅ AI_OPERATING_RULES TEXT RENDERING RULES (Rules 059–100)
- ✅ Build/Pipeline.md Text Engine phases (2/2a/2b/2c)
- ✅ PromptEngine LOAD sequence

## Status Update — v2.4.0 [RELEASED]

All v2.4.0 features are complete:
- ✅ `ApprovedAssets/` CMS layer (P001–P010 page modules × 7 files each)
- ✅ `ApprovedAssets/index.yaml` — global registry
- ✅ `Tests/ContentValidation.md` — 7 test suites (CV-001 through CV-007)
- ✅ `Core/TEXT_ENGINE.md` — content.yaml as primary output
- ✅ `Core/COMPONENT_SYSTEM.md` — content.yaml field mapping per component
- ✅ `Core/PAGE_SYSTEM.md` — Page-as-module architecture, lifecycle states
- ✅ `Build/Pipeline.md` — CMS pipeline phases 2b/2c/2d; Render Engine contract
- ✅ `PromptEngine/README.md` — 9-step LOAD sequence; content.yaml generation mode
- ✅ `STYLE_DECISIONS.md` — ADR-019, ADR-020, ADR-021
- ✅ `MigrationReport_v2.4.md`

---

## v2.5.0 — Planned

**Target:** Q3 2026
**Theme:** Automation & Tooling

### Features
- `Build/scripts/` — Python/Shell scripts for token substitution and content.yaml generation
- `Assets/DesignSystem/Icons/` — SVG icon library (10 icons: warning, tip, info, check, brush, airbrush, clock, star, sandpaper, decal)
- Automated `Tests/ContentValidation.md` runner — validates content.yaml schema, language compliance, component-field mapping via script
- Automated `Tests/TextValidation.md` execution — checks for Japanese Unicode ranges (U+3000–U+9FFF)
- `Config/environments/` — local dev overrides (dev/staging/production config switching)
- CI/CD integration guide (`Build/CI.md`)
- Expanded `Knowledge/` with airbrush technique guide and color mixing reference
- Automated `ApprovedAssets/index.yaml` updater — regenerates index from directory scan

### Non-Breaking Changes Only
All v2.4.0 projects remain compatible. content.yaml schema is extended only with optional fields.
