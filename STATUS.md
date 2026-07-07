# Mini4WD Manual SDK — Status

**Version:** 2.5.5 | **Status:** Active | **Maturity:** Beta

> This document is updated at every release. For machine-readable metadata see `ReleaseInfo.yaml` and `SDK_CONTEXT.yaml`.

---

## Current Version

| Field | Value |
|-------|-------|
| Version | 2.5.5 |
| Codename | MultiProject (2.5.x family) |
| Release name | Deterministic Rendering & Runtime Consistency |
| Release date | 2026-07-07 |
| Branch | main |
| Repository | https://github.com/diegoperu/mini4wdpaintframework |
| Bootstrap entry (AI) | AI_ENTRYPOINT.md |
| Entry point (human) | START_HERE.md |

---

## Roadmap

| Version | Status | Key Feature |
|---------|--------|-------------|
| 2.1.0 | Released 2026-06-30 | Core framework — Design Language, Component System, Design Tokens, PromptEngine |
| 2.2.0 | Released 2026-06-30 | Build pipeline, Config layer, Test suites, Knowledge base, AI Operating Rules |
| 2.3.0 | Released 2026-07-01 | Text Engine, Editorial Pipeline, Italian-only language policy, LOAD sequence |
| 2.4.0 | Released 2026-07-01 | CMS layer (ApprovedAssets/), content.yaml as source of truth, page lifecycle |
| 2.4.1 | Released 2026-07-02 | UX & Operator Workflow Update — START_HERE, OperatorGuide/, tutorials, single image convention, validation scoping (UAT-001) |
| 2.5.0 | Released 2026-07-03 | Multi-Project Content Isolation — per-variant `Projects/{Model}/{Variant}/` structure |
| **2.5.5** | **Released 2026-07-07** | Deterministic Rendering — `Scripts/render_page.py` template replaces whole-page AI rendering, custom fonts, PDF merge, Gemini restored for Fase 4 (UAT-004) |
| 2.6.0 | Planned | Compiler/, Prompt Orchestrator, Icon Library, Documentation/OperationalManual/ full audit |

---

## Implemented Features

### Core Framework (v2.1.0)
- Specification layer — Core/ with 15 authoritative documents
- Design Language — 65 rules governing all design decisions
- Style Guide — color palette, typography, grid, spacing
- Component System — C001–C015 with full specifications
- Design Tokens — all visual values referenced by token name
- PromptEngine — 10 model-agnostic prompts for P001–P010
- Templates — PROJECT.yaml, COLOR_SCHEME.yaml, PDF_CONFIG.yaml

### Build and Config (v2.2.0)
- Build pipeline — Build/Pipeline.md (8 phases, Phase 0 → Phase 7)
- Config layer — Config/ with 5 global configuration files
- Test suites — Tests/ with 9 suites and 110+ quality checks
- Knowledge base — Knowledge/ with 14 technical documents
- AI Operating Rules — 100 behavioral rules for AI models
- MANIFEST.yaml — machine-readable SDK descriptor

### Text Engine and Editorial (v2.3.0)
- Text Engine — Core/TEXT_ENGINE.md with content.yaml as primary output
- Italian-only language policy — Config/LANGUAGE_POLICY.yaml
- Editorial knowledge — EditorialStyle.md, GlossaryIT.md, Terminology.md, ForbiddenWords.md
- AI Operating Rules expanded — Rules 059–100: text rendering rules
- Design Language expanded — Rules 55–65: editorial identity vs Japanese aesthetic
- LOAD sequence — defined and documented in PromptEngine/README.md
- Text Validation suite — Tests/TextValidation.md (9 Italian compliance tests)

### CMS Layer (v2.4.0, superseded by v2.5.0)
- content.yaml — primary source of truth, supersedes text.md as primary output
- Page lifecycle — draft → review → approved → locked → rendered → released → archived
- Content Validation suite — Tests/ContentValidation.md (7 validation suites)
- MigrationReport_v2.4.md — migration guide from v2.3.0 with workflow diagram
- `ApprovedAssets/` (global shared directory) — **removed in v2.5.0**, see below

### Bootstrap System (v2.4.0)
- AI_ENTRYPOINT.md — official AI entry point with Bootstrap Contract, Golden Rules, First Response Policy
- SDK_CONTEXT.yaml — machine-readable SDK identity card
- BOOTSTRAP.md — AI operational guide (detailed pipeline, error table, document map)
- Docs/LOAD_ORDER.md — explicit context loading order with rationale
- RepositoryManifest.yaml — complete file and dependency map with AI load order
- Projects/PROJECT_BOOTSTRAP.md — new project guide
- Docs/AI_BOOTSTRAP_PROMPT.md — official prompts per phase (ChatGPT / Claude — Gemini limited to Fase 4, see v2.5.5)
- STATUS.md — this document
- ReleaseInfo.yaml — machine-readable release metadata

### Multi-Project Content Isolation (v2.5.0)
- `Projects/{Model}/{Variant}/` two-level structure — variants of the same model coexist without conflict
- `paintScheme.slug` (kebab-case) required field in PROJECT.yaml
- `ApprovedText/` per-project-variant (replaces global `ApprovedAssets/Text/`)
- `Scripts/generate_prompts.py` — pre-filled prompt generator reading PROJECT.yaml
- `Docs/RUNTIMES.md` — runtime concept, ChatGPT Web vs Claude Code comparison
- `OperatorGuide/Runtimes/` — standalone per-runtime guides

### Deterministic Rendering (v2.5.5)
- `Scripts/render_page.py` — Jinja2/HTML/CSS template + Playwright/Chromium; reads
  `content.yaml` directly and produces every page's text/layout with **zero AI
  involvement** — no risk of hallucinated hex codes, names, or off-language text
- Illustrations (cover, orthographic views, detail photos) live in
  `Projects/{Model}/{Variant}/Images/` — **not** `ApprovedImages/P{NNN}/` (that path
  was planned in v2.5.0 but never implemented; the actual mechanism uses `Images/`
  directly, path declared by `Scripts/render_page.py` → `image_slots()`)
- `Scripts/package_handoff.sh` — narrowed to illustration-only handoff (no longer
  bundles `ApprovedText/`, `COMPONENT_SYSTEM.md`, `QA_SYSTEM.md` — an AI never
  touches page text/layout anymore)
- `MISSING_IMAGES.md` / `MISSING_IMAGES_PROMPT.md` / `MISSING_IMAGES.json` —
  auto-generated per project: what's missing, ready-to-paste prompts, and a
  machine-readable format for a future local generation node
- Custom fonts embedded via `@font-face` (base64) — `Assets/DesignSystem/Typography/Fonts/`
  (J Audio Cassette as TitleFont, Bebas Neue/Source Sans Pro/JetBrains Mono as real
  fallbacks, not just names in a CSS stack that were never actually available)
- PDF merge via `pdfunite` — `Scripts/render_page.py {Model} {Variant} pdf` produces
  one unified preview PDF per project
- Gemini restored as a supported runtime, **limited to Fase 4** (single-illustration
  generation) — see `UAT/UAT-004.md`. UAT-002's finding stands for the old
  whole-page scope; Fase 1-3 (text/bootstrap) remain unverified on Gemini
- `Docs/LOCAL_RENDER_NODE.md` — evidence and input/output contract for a future
  local AI generation node (not yet built — see ROADMAP.md)

---

## Planned Features (v2.6.0)

| Feature | Description | Priority |
|---------|-------------|----------|
| Compiler/ | Automated pipeline executor (Project Loader, Context Builder, Page Generator, QA Engine, PDF Assembler) | High |
| Prompt Orchestrator | Manages LOAD sequence and context injection automatically | High |
| Icon Library | 15 SVG icons — currently using Unicode fallbacks | Medium |
| Documentation/OperationalManual/ audit | Full pass to remove remaining v2.4.x path references (KI-004) | Medium |
| Release System | Automated release tagging and manifest update | Low |

---

## Known Issues

See `Documentation/QualityManagement/07_KNOWN_ISSUES.md` for the live registry
(KI-001 through KI-004 open, KI-005 resolved in v2.5.5 — see UAT-004).

---

## TODO

| ID | Description | Priority | Target Version |
|----|-------------|----------|----------------|
| TODO-001 | Create Compiler/ subsystem | High | v2.6.0 |
| TODO-002 | Create 15 SVG icons in Assets/DesignSystem/Icons/ | Medium | v2.6.0 |
| TODO-006 | Create Release System automation | Low | v2.6.0 |
| TODO-007 | Populate Projects/Proto_Emperor/Violet_Phantom/ApprovedText/ with a full P001-P010 set | Medium | Active |
| TODO-009 | Add Scripts/render_page.py, package_handoff.sh, Assets/DesignSystem/Typography/Fonts/ entries to RepositoryManifest.yaml | Low | v2.6.0 |

---

## Cross References

- Architecture decisions: `STYLE_DECISIONS.md` (ADR-001–ADR-021)
- Full version history: `CHANGELOG.md`
- Release metadata: `ReleaseInfo.yaml`
- SDK identity: `SDK_CONTEXT.yaml`
- AI entry point: `BOOTSTRAP.md`
- Loading order: `Docs/LOAD_ORDER.md`
- Full roadmap: `ROADMAP.md`
- Deterministic rendering evidence: `Docs/LOCAL_RENDER_NODE.md`
