# Changelog

All notable changes to Mini4WD Manual SDK are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.5.5] - 2026-07-07 — Deterministic Rendering & Runtime Consistency

Fase 4 (rendering) no longer asks an AI to generate an entire page. Extensive
testing (`UAT/UAT-002.md`, ChatGPT/Gemini test sessions on Cotton Candy Drift)
showed that no generative model can reliably produce exact text/tables/hex codes
inside a generated image. `Scripts/render_page.py` now produces every page's
text and layout deterministically from `content.yaml`; an AI model is only
needed for isolated illustrations (cover, orthographic views, detail photos).
No change to `content.yaml`/`PROJECT.yaml` schema — only to how Fase 4 works.

### Added
- `Scripts/render_page.py` — Jinja2/HTML/CSS template + Playwright/Chromium, generates PNG/PDF per page directly from `content.yaml`
- `Scripts/templates/P001.html.jinja` … `P010.html.jinja` — one template per page type
- `Scripts/package_handoff.sh` (rewritten) — now bundles only what an AI needs to generate a single illustration (style guides + `PROJECT.yaml` + reference photos), not page text/layout
- `Projects/{Model}/{Variant}/MISSING_IMAGES.md` — auto-generated report of missing illustrations, regenerated every run
- `Projects/{Model}/{Variant}/MISSING_IMAGES_PROMPT.md` — ready-to-paste prompt + file list per missing illustration slot
- `Projects/{Model}/{Variant}/MISSING_IMAGES.json` — same data, structured, for a future local batch generation node
- `Assets/DesignSystem/Typography/Fonts/` — J Audio Cassette, Bebas Neue, Source Sans Pro (4 weights), JetBrains Mono, embedded via `@font-face` (base64), all SIL OFL 1.1
- `Docs/LOCAL_RENDER_NODE.md` — evidence for the architecture split, plus the input/output contract shared by ChatGPT/Gemini today and a future local node
- `UAT/UAT-004.md` — Gemini retest under the new narrow Fase 4 scope: PASS, restoring Gemini as a supported runtime limited to Fase 4

### Changed
- `Docs/AI_BOOTSTRAP_PROMPT.md` — Fase 4 rewritten as the single source of truth for the render prompt (4a template, 4b single illustration, 4c future local node)
- `Docs/RENDER_HANDOFF_CONTEXT.md` — role rewritten from "render the whole page" to "generate only the isolated illustration"
- `OperatorGuide/Runtimes/Claude_Code.md`, `ChatGPT_Web.md` — Fase 4 sections rewritten for the new flow; Gemini re-added as an option with the same instructions
- `FIRST_RENDER.md`, `FIRST_PDF.md` — rewritten (were still describing the pre-refactor whole-page flow)
- `OperatorGuide/01_Primo_Manuale.md`, `02_Workflow.md`, `05_Checklist.md` — Fase 4/5 sections aligned to the script-based flow
- `Documentation/OperationalManual/09_ApprovedAssets.md` — rewritten for `Projects/{Model}/{Variant}/ApprovedText/`; `ApprovedAssets/` (removed in v2.5.0) no longer described as current structure
- `ROADMAP.md` — Local AI Render Node entry updated (deterministic half shipped, in production use)
- `Docs/RUNTIMES.md`, `SDK_CONTEXT.yaml`, `README.md`, `PromptEngine/README.md`, FAQ files — Gemini compatibility corrected (Fase 4 only, not full pipeline)
- `Documentation/QualityManagement/07_KNOWN_ISSUES.md` — KI-005 (Gemini) moved to resolved archive

### Fixed
- P001 cover illustration: `object-fit: cover` cropped the model to fill the frame — changed to `contain` so the whole model is visible, fit to width
- P001 empty space above the cover render — filled with a fixed "Guida alla Verniciatura" kicker (invariant SDK copy, not project data — same treatment as the header wordmark)
- PNG output had a fractional-pixel white sliver on the right/bottom edge on every page — `mm()` now rounds to whole pixels, and the Playwright viewport is set explicitly instead of relying on the default
- PDF output opened as 2 pages per manual page — Chromium's PDF export interprets CSS px at 96dpi regardless of our 150dpi screenshot convention; added `scale=96/150` to `page.pdf()`
- `render_page.py` now accepts `.jpg`/`.jpeg` in addition to `.png` for illustration files at the same base name
- P004 (Preparazione) illustration prompts no longer describe the painted color scheme — this phase happens before painting (Fase 5); prompts now describe bare ABS plastic or white primer instead
- Detail thumbnails (P004/P006/P007/P008) doubled in size (24×17mm → 48×34mm, same position) — were too small to be useful

### Documentation Consistency Pass
- Version bumped to 2.5.5 across `VERSION`, `SDK_CONTEXT.yaml`, `ReleaseInfo.yaml`, `MANIFEST.yaml`, `README.md`, `Templates/PROJECT.yaml`, `STATUS.md` (was stale at 2.4.1), `RepositoryManifest.yaml` (was stale at 2.4.1), `Projects/Proto_Emperor/*/PROJECT.yaml` (were stale at 2.4.1), 20 `Documentation/QualityManagement/*.md` headers (were stale at 2.4.1)
- `STATUS.md` — full rewrite, was an entire version behind (still said 2.4.1/Planned for a 2.5.0 already released) and listed "Known Issues: None" despite 5 tracked KIs

---

## [2.5.0] - 2026-07-03 — Multi-Project Content Isolation

Breaking change: per-project content isolation. `ApprovedAssets/Text/` and
`ApprovedAssets/Images/` (global) replaced by per-variant directories inside
each project. No functional change to Prompt Engine, Text Engine, or QA logic.

### Breaking Changes
- Content path: `ApprovedAssets/Text/P{NNN}/` → `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/`
- Images path: `ApprovedAssets/Images/P{NNN}/` → `Projects/{Model}/{Variant}/ApprovedImages/P{NNN}/`
- Index path: `ApprovedAssets/index.yaml` → `Projects/{Model}/{Variant}/index.yaml`
- `paintScheme.slug` field now REQUIRED in PROJECT.yaml

### Added
- `Projects/{Model}/{Variant}/` two-level project structure: model folder + variant folder
- `paintScheme.slug` field in `Templates/PROJECT.yaml` (kebab-case, source for variant folder name)
- `Core/NAMING_CONVENTION.md §3.1` — variant folder naming rule and examples
- `Projects/Proto_Emperor/Violet_Phantom/` — reference project migrated to v2.5.0 structure

### Changed
- `PromptEngine/*.md` (all 10) — `Save output to:` path updated to `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml`
- `Core/TEXT_ENGINE.md` — v2.5.0 row added to output format table; Render Engine contract path updated
- `Core/PAGE_SYSTEM.md` — module storage path updated
- `AI_ENTRYPOINT.md` — Bootstrap Contract `required_read_order` path updated
- `BOOTSTRAP.md` — Phase 2a output, Phase 3 output, Phase 7 index paths updated
- `Docs/LOAD_ORDER.md` — Step 12 path updated
- `Docs/AI_BOOTSTRAP_PROMPT.md` — Fase 2 write path and Fase 4 output path updated
- `Scripts/generate_prompts.py` — path construction dynamic from PROJECT.yaml location; variant folder derived from parent dir; paintScheme.slug cross-check; output saved to project dir by default
- `VERSION` → 2.5.0; `SDK_CONTEXT.yaml` version updated

### Migration from v2.4.x
For each existing project `Projects/{Model}/`:
1. Create subfolder `Projects/{Model}/{Variant}/` (variant = paintScheme.name in Title_Case_Underscore)
2. Move `PROJECT.yaml`, `Images/`, `Output/`, `Notes/` into the variant folder
3. Add `paintScheme.slug: "variant-slug"` to PROJECT.yaml
4. Move any existing `ApprovedAssets/Text/` content to `Projects/{Model}/{Variant}/ApprovedText/`

---

## [Unreleased]

### Fixed — ChatGPT Web UX (2026-07-03, da UR-0001 UAT session)
- `OperatorGuide/Runtimes/ChatGPT_Web.md` PASSO 11 — riscritto completamente: prompt Fase 2 e Fase 3 ora embedded copia-incolla; PASSO 11 diviso in 11a (Genera) / 11b (QA) / 11c (Sigilla) / 11d (pagina successiva); tabella pagina→PromptEngine file; warning esplicito su `TODO:` (dato mancante in PROJECT.yaml, non errore); riferimento "allegato" corretto in "dallo ZIP che hai già caricato"
- `Docs/AI_BOOTSTRAP_PROMPT.md` + `OperatorGuide/Runtimes/ChatGPT_Web.md` Prompt Fase 2 — aggiunto step 3 esplicito: l'AI deve risolvere riferimenti `colorId` → `paintScheme.colors[id]` per estrarre `paintCode`/`paintName`/`finish`/`hex` prima di scrivere il content.yaml; causa root del TODO: massiccio in UR-0001 nonostante PROJECT.yaml completo
- `Templates/PROJECT.yaml`, `PDF_CONFIG.yaml`, `APPROVED_TEXT.md`, `COLOR_SCHEME.yaml`, `CHECKLIST.md`, `PROJECT.md`, `README.md` — bumped `sdk_version` da 2.4.0 a 2.4.1; nuovi progetti copiati dai template partono con versione corretta
- `Projects/Proto_Emperor/PROJECT.yaml` — bumped `sdk_version` da 2.4.0 a 2.4.1

### Added — Runtime-Aware Documentation
- `Docs/RUNTIMES.md` — Runtime concept: definition, comparison table (ChatGPT Web vs Claude Code), selection guide, future runtime roadmap (Claude Web, Gemini, Ollama, Open WebUI, vLLM)
- `OperatorGuide/Runtimes/ChatGPT_Web.md` — standalone step-by-step guide for ChatGPT Web: download ZIP, extract only PROJECT.yaml template, upload ZIP + PROJECT.yaml + images, bootstrap via Prompt E, per-phase file requirements
- `OperatorGuide/Runtimes/Claude_Code.md` — standalone step-by-step guide for Claude Code: clone repo, create project, direct file access, AI writes to repo
- `Documentation/QualityManagement/Reports/UR-0001.md` — first user report; score 1/5; documents path ambiguity in OperatorGuide/ and missing runtime distinction as root cause

### Changed — Runtime-Aware Documentation
- `START_HERE.md` — added PASSO 0 (runtime selection) before all other steps; directs to runtime-specific guides
- `Projects/PROJECT_BOOTSTRAP.md` — added runtime warning box at top: procedure dipende dal runtime; links to ChatGPT_Web.md and Claude_Code.md
- `Docs/AI_BOOTSTRAP_PROMPT.md` — FASE 1 split into §ChatGPT Web and §Claude Code sections; Prompt E renamed to "Bootstrap Minimo (ChatGPT Web / ZIP)" with updated description; tabella riassuntiva adds Runtime column
- `FILE_MATRIX.md` — added Runtime column per file: ChatGPT Web access pattern (ZIP / Allegato / In chat) vs Claude Code access pattern (Diretto / Nel repo)
- `WORKFLOW.md` — added state 0 SCELTA RUNTIME before NUOVO PROGETTO; BOOTSTRAP state documents runtime-specific input
- `Knowledge/FAQ.md` — added §Runtime section with 4 new questions: ZIP vs file singoli, Claude Code no allegati, ChatGPT nuova chat obbligatoria, prompt cross-runtime
- `Documentation/QualityManagement/07_KNOWN_ISSUES.md` — added KI-003: documentazione pre-runtime-aware ambigua per ChatGPT Web (da UR-0001)
- `OperatorGuide/01_Primo_Manuale.md` — path fixes: FIRST_PROJECT.md → ../FIRST_PROJECT.md, PROJECT_STRUCTURE.md → ../PROJECT_STRUCTURE.md, Docs/ → ../Docs/, BOOTSTRAP.md → ../BOOTSTRAP.md, FIRST_RENDER.md → ../FIRST_RENDER.md, FIRST_PDF.md → ../FIRST_PDF.md
- `OperatorGuide/06_Errori_Comuni.md` — path fixes: PROJECT_STRUCTURE.md → ../PROJECT_STRUCTURE.md, Docs/AI_BOOTSTRAP_PROMPT.md → ../Docs/AI_BOOTSTRAP_PROMPT.md

No functional change to the framework: Prompt Engine, Text Engine, Rendering Engine, and pipeline are untouched.

### Added — Quality Management System
- `Documentation/QualityManagement/` — 20-document Quality Management System:
  release policy and criteria (01–02), feedback templates (03–06, 13–15),
  living registers (07–12, 17), operator feedback process (16), documentation
  policy (18), README and index (19–20). The framework is now STABLE: every
  future change must be justified by documented evidence (confirmed bugs, UAT,
  unachievable Golden Projects, AI model changes, or approved functional
  requirements). No functional change to the framework: Prompt Engine, Text
  Engine, Rendering Engine, and pipeline are untouched.

### Planned
- Compiler/ and Prompt Orchestrator (v2.5.0)
- Multi-language support (Italian, Japanese, English)
- SVG icon library for C006 Callout and C008 Warning components
- Automated PDF pipeline via pandoc + LaTeX

---

## [2.4.1] - 2026-07-02 — UX & Operator Workflow Update

UX-only release driven by UAT-001 (first external-operator test). No framework
behavior, architecture, Prompt Engine, Text Engine, Component System, Page System,
or ApprovedAssets structure changes. Documentation, onboarding, and validation
scoping only.

### Added — Operator Layer
- `START_HERE.md` — first document for new users: checklist, diagram, do/don't table, chat map (max 2 pages)
- `OperatorGuide/` — 7-document operator guide: `01_Primo_Manuale.md`, `02_Workflow.md`, `03_File_da_Modificare.md`, `04_File_da_NON_Modificare.md`, `05_Checklist.md`, `06_Errori_Comuni.md`, `07_FAQ.md` (+ README)
- `WORKFLOW.md` (root) — operational state machine: Nuovo Progetto → Bootstrap → Testi → QA → Approved Text → Rendering → QA → Approved Images → PDF → Golden Project, with obiettivo/input/output/prossimo stato per state
- `FILE_MATRIX.md` — per-file matrix: modificabile SÌ/NO, quando, da chi, in quale fase
- `PROJECT_STRUCTURE.md` — folders to create / NOT create; **single image convention**: all operator images in `Projects/{Model}/Images/`; `Assets/ReferenceModels/` reserved to Maintainer
- `FIRST_PROJECT.md` — tutorial: folder creation → Bootstrap OK, with real examples
- `FIRST_RENDER.md` — tutorial: Approved Text → first rendered page
- `FIRST_PDF.md` — tutorial: rendering → 3 PDF variants
- `WHO_MODIFIES_WHAT.md` — artifact → role responsibility table
- `LIFECYCLE.md` — manual (macro) and page (micro) lifecycle
- `OPERATOR_PROFILE.md` — roles: Operatore, Reviewer, Maintainer, Developer (responsibilities, editable files, required skills)
- `UAT/UAT-001.md` — real-world operator test report: 8 errors with descrizione/causa/correzione/documento aggiornato

### Changed — Documentation & Onboarding
- `Projects/PROJECT_BOOTSTRAP.md` — fully rewritten as operational guide (PASSO 1…8), Italian, single image convention, explicit "generate before validate" rule
- `Docs/AI_BOOTSTRAP_PROMPT.md` — restructured by phase (Bootstrap → Testi → QA → Rendering → PDF); each phase declares Input, Output, Prompt, Nuova chat SÌ/NO; summary table; Prompt E/F retained as service prompts
- `README.md` — operator entry banner (START_HERE.md), v2.4.1, version table
- Folder READMEs (`Core/`, `Config/`, `PromptEngine/`, `ApprovedAssets/`, `ApprovedAssets/Text/`, `Templates/`, `Projects/`, `Assets/`, `Assets/ReferenceModels/`, `Build/`, `Tests/`, `Knowledge/`, `Docs/`) — standard header: a cosa serve / chi la modifica / quando
- `Core/WORKFLOW.md` §0.4 and `Build/Pipeline.md` §Phase 1 — aligned to the single image convention (`Projects/{Model}/Images/`)
- `AI_ENTRYPOINT.md` — `required_read_order` reference-images path aligned to `Projects/{ModelName}/Images/`
- `Projects/README.md` — minimal file set defined (`PROJECT.yaml` + `Images/` + `Output/` + `Notes/`); image convention note
- `Templates/PROJECT.yaml` — `text.approved_text_dir` marked LEGACY (v2.3.0 compatibility); v2.4.x output path documented

### Changed — Language Policy & Validation Scoping (UAT-001 fixes)
- `Config/LANGUAGE_POLICY.yaml` (v2.4.1) — §exceptions split into 5 explicit language-neutral categories: paint codes (TS-37, XF-1, X-10, X-11…), technical terms (Primer, Topcoat, Masking Tape…), commercial names (Chrome Silver, Gun Metal, Semi Gloss Black, Flat Black…), YAML keys/schema values, structural metadata (Header, Footer, draft…); new §validation_scope; scope clarification header
- `Tests/ContentValidation.md` — new **§Validation Scope**: Template vs Draft vs Approved; templates (status draft + empty fields) are never validated as final content; language exceptions restated
- `Tests/TextValidation.md` — same §Validation Scope; v2.4.x target clarified (content.yaml; `ApprovedText/` legacy-only); TX-001-K whitelist extended

### Release metadata
- `VERSION` → 2.4.1; `MANIFEST.yaml`, `SDK_CONTEXT.yaml`, `ReleaseInfo.yaml` updated

---

### Added — Bootstrap System v2 (pre-2.4.1, previously Unreleased)
- `AI_ENTRYPOINT.md` — official AI entry point; Bootstrap Contract (YAML), mission, source-of-truth hierarchy, pipeline, AI operating mode (Text/Render), editorial philosophy, language rules, Golden Rules (G01–G10), completion checklist, First Response Policy with Bootstrap Report format
- `BOOTSTRAP.md` — AI operational guide; detailed pipeline, page/component index, common errors, document map
- `SDK_CONTEXT.yaml` — machine-readable SDK identity card; version, pipeline, architecture, source-of-truth hierarchy, load order, roadmap
- `STATUS.md` — implementation status, feature matrix by version, roadmap, known issues, TODO list
- `ReleaseInfo.yaml` — machine-readable release metadata; version, date, breaking changes, migration notes, compatibility
- `RepositoryManifest.yaml` — complete file and dependency map; every file with type, role, AI load order, and dependency graph
- `Docs/LOAD_ORDER.md` — explicit 14-step context loading order (Step 0: AI_ENTRYPOINT.md) with rationale; phase-specific minimum requirements
- `Docs/AI_BOOTSTRAP_PROMPT.md` — 6 ready-to-use prompts for ChatGPT, Claude, Gemini (Prompt A–F: full bootstrap, single page, QA, render, minimal, continuity)
- `Projects/PROJECT_BOOTSTRAP.md` — step-by-step guide for creating a new Mini4WD project

### Changed — Bootstrap System v2
- `README.md` — "Quick Start for AI Models" updated: AI_ENTRYPOINT.md as Step 1, Bootstrap Report requirement added; Bootstrap System in directory tree and documentation table
- `BOOTSTRAP.md` — subtitle changed from "Primary AI Entry Point" to "AI Operational Guide"; header updated to point to AI_ENTRYPOINT.md
- `SDK_CONTEXT.yaml` — `bootstrap.official_entrypoint` set to `AI_ENTRYPOINT.md`
- `Docs/LOAD_ORDER.md` — AI_ENTRYPOINT.md added as Step 0; Abbreviated LOAD updated; Phase table updated
- `RepositoryManifest.yaml` — AI_ENTRYPOINT.md added; dependency_graph root updated
- `STATUS.md` — Bootstrap System section updated with AI_ENTRYPOINT.md
- `Core/WORKFLOW.md` — cross-reference to AI_ENTRYPOINT.md
- `Core/TEXT_ENGINE.md` — cross-reference to AI_ENTRYPOINT.md in header
- `Config/LANGUAGE_POLICY.yaml` — bootstrap note added to header

---

## [2.4.0] - 2026-07-01

### Added
- `ApprovedAssets/` directory — CMS layer; pages are now structured content modules, not just images
- `ApprovedAssets/Text/P001/` through `P010/` — 10 page modules, each containing: `content.yaml`, `text.md`, `metadata.yaml`, `manifest.yaml`, `changelog.md`, `notes.md`, `README.md`
- `ApprovedAssets/index.yaml` — global content, manual, and image registry
- `Tests/ContentValidation.md` — 7 content QA test suites (CV-001 through CV-007): schema validation, language compliance, data accuracy, metadata integrity, manifest consistency, component-field mapping, cross-page consistency
- `MigrationReport_v2.4.md` — detailed migration log from v2.3.0 to v2.4.0
- Build/Pipeline.md — added §CMS Pipeline v2.4.0: phases 2b (Content QA), 2c (Text QA renamed), 2d (Approved Assets Sealing), updated Phase 3 (Render Engine reads content.yaml not PROJECT.yaml)
- PromptEngine/README.md — added §content.yaml Generation Mode: updated 9-step LOAD sequence, text-mode vs render-mode distinction, field name vs value rule, sealing workflow

### Changed
- `Core/TEXT_ENGINE.md` — added §content.yaml as Primary Output (v2.4.0): structured YAML supersedes Markdown; text.md is derived not primary; Render Engine contract updated
- `Core/COMPONENT_SYSTEM.md` — added §content.yaml Field Mapping (v2.4.0): per-component field declarations, Render Engine access pattern, read-only contract
- `Core/PAGE_SYSTEM.md` — added §Page-as-Module Architecture (v2.4.0): lifecycle states (draft→review→approved→locked→rendered→released→archived), reusability, module directory structure
- `VERSION` — bumped from 2.3.0 to 2.4.0
- `MANIFEST.yaml` — updated version, added ApprovedAssets/ to directory map, added content.yaml to supported formats

### Architecture Change
SDK evolves from editorial framework to full CMS. Pages are now structured content modules with lifecycle management:
- `content.yaml` is the primary source of truth for all page content
- `metadata.yaml` tracks lifecycle state, approval, QA status, lock flag
- Render Engine reads `ApprovedAssets/Text/P{NNN}/content.yaml` exclusively — never PROJECT.yaml
- Field names are English (structural keys); field values are Italian (editorial content)
- Approved Assets Sealing (Phase 2d) is a mandatory gate before rendering

### Migration from v2.3.0
No breaking changes. All v2.3.0 projects are compatible.

**Optional migration steps:**
1. Create `ApprovedAssets/Text/P{NNN}/` module directories for each page
2. Move content from `ApprovedText/` to `ApprovedAssets/Text/` (if using v2.3.0 text modules)
3. Convert existing `.md` text files to `content.yaml` format (see Templates)
4. Update prompts to use 9-step LOAD sequence (Step 8 added for updates)
5. Regenerate pages using Render Engine reading content.yaml (not PROJECT.yaml)

---

## [2.3.0] - 2026-07-01

### Added
- `Core/TEXT_ENGINE.md` — complete Text Engine specification; establishes editorial layer as fully independent from Render Engine
- `Config/LANGUAGE_POLICY.yaml` — machine-readable language enforcement; zero tolerance for Japanese scripts, English body text, and fake text; approved placeholder system
- `Tests/TextValidation.md` — 40-item editorial QA suite (TEST-TX-001 through TEST-TX-009); blocking/non-blocking classification
- `Knowledge/EditorialStyle.md` — Italian editorial style guide: voice, tone, register, sentence structure, abbreviations, number formatting
- `Knowledge/GlossaryIT.md` — authoritative Italian terminology with page labels, component labels, and finish type translations
- `Knowledge/Terminology.md` — technical term Italian equivalents with usage notes
- `Knowledge/ForbiddenWords.md` — explicit forbidden words/phrases/scripts catalog with replacements
- `Templates/APPROVED_TEXT.md` — template for Text Engine output files with YAML frontmatter
- `Projects/Proto_Emperor/ApprovedText/README.md` — ApprovedText directory for example project

### Changed
- `Core/DESIGN_LANGUAGE.md` — added Rules 55–65: editorial identity principles (visual Japanese aesthetic + Italian editorial language)
- `Core/STYLE_GUIDE.md` — added §Typography Rules: full type hierarchy table, capitalization rules, max text lengths, spacing, forbidden typography
- `Core/COMPONENT_SYSTEM.md` — added §Text Source Declaration: per-component text source mapping to ApprovedText sections
- `Core/AI_OPERATING_RULES.md` — added Rules 059–100: TEXT RENDERING RULES (42 new rules governing Italian-only output, fake text prohibition, Render Engine behavior)
- `Build/Pipeline.md` — added §Extended Pipeline v2.3.0: phases 2/2a/2b/2c (Knowledge Load, Text Engine, Editorial QA, Approved Text)
- `PromptEngine/README.md` — added LOAD Sequence definition, text-mode vs render-mode distinction, updated token reference table
- `Templates/PROJECT.yaml` — added `text:` section with language enforcement fields

### Architecture Change
SDK evolves from documentation framework to editorial framework. Text and rendering are now fully decoupled:
- Text Engine generates and validates Italian content independently
- Render Engine receives only pre-approved text from `ApprovedText/`
- Language policy is machine-enforced via `Config/LANGUAGE_POLICY.yaml`

### Migration from v2.2.0
No breaking changes. All v2.2.0 projects are compatible.

**Optional migration steps:**
1. Add `text:` section to existing `PROJECT.yaml` files (see `Templates/PROJECT.yaml`)
2. Create `ApprovedText/` directory in project folder
3. Regenerate pages using updated LOAD sequence (better language compliance)

---

## [2.2.0] - 2024-06-30

### Added
- `Build/` directory with `Pipeline.md` — complete 7-phase production pipeline documentation
- `Config/` directory with `sdk.yaml`, `render.yaml`, `pdf.yaml`, `quality.yaml` — machine-readable runtime configuration for all SDK processes
- `Tests/` directory with 7 validation test suites (FrameworkIntegrity, PromptValidation, LayoutValidation, NamingValidation, ColorValidation, PDFValidation, AssetsValidation)
- `Core/AI_OPERATING_RULES.md` — 58 mandatory behavioral rules for AI models operating within the SDK
- `Knowledge/` directory with 10 technical reference documents (Paints, Masking, Preparation, Painting, Decals, ClearCoat, Troubleshooting, Glossary, FAQ, BestPractices)
- `MANIFEST.yaml` — SDK manifest with directory map, supported types, AI requirements, compatibility matrix

### Changed
- `STYLE_DECISIONS.md` — converted to full ADR registry format; added ADR-011 through ADR-015
- All existing documents retain full backward compatibility

### Migration
No breaking changes. All v2.1.0 projects are fully compatible with v2.2.0.
Optionally adopt `Config/sdk.yaml` for schema validation of PROJECT.yaml files.

---

## [2.1.0] - 2024-01-15

### Added
- `Assets/DesignSystem/Tokens/tokens.example.yaml` — full example token file with all 24 documented tokens
- `Assets/DesignSystem/Tokens/tokens.schema.yaml` — JSON Schema validation for token files
- `Core/QA_SYSTEM.md` — comprehensive quality assurance checklist with 110 items across 11 categories
- `Core/DEFINITION_OF_DONE.md` — completion criteria at manual, page, and framework levels
- `Core/DOCUMENTATION_STYLE.md` — style guide for writing SDK documentation
- Page P009 Premium Variant — specification for premium/limited edition manual variant
- Component C015 Notes — freeform annotated note block component
- `Docs/` directory with README

### Changed
- `Core/PAGE_SYSTEM.md` — added dependency graph, input/output specification, and component list per page
- `Core/STYLE_GUIDE.md` — expanded typography section with full fallback font stacks and line-height values
- `Core/RENDER_GUIDE.md` — added three named lighting rigs (Studio Neutral, Drama, Detail)
- `Core/COMPONENT_SYSTEM.md` — added ASCII wireframe diagrams for all components

### Fixed
- `Core/COLOR_SYSTEM.md` — corrected Pantone reference for VioletPrimary (was 2685 C, now 2627 C)
- `PromptEngine/Cover.md` — fixed token reference from `{{modelName}}` to `{{project.modelName}}` to match schema
- `Core/NAMING_CONVENTION.md` — clarified image versioning suffix format (v1 not _001)

---

## [2.0.0] - 2023-09-01

### Breaking Changes

- **Component IDs renamed:** All component identifiers changed from `COMP_HEADER` style to `C001` format. Update all template references.
- **PROJECT.yaml schema:** Field `car_name` renamed to `modelName`. Field `color_scheme` renamed to `paintScheme`. Existing project files must be migrated.
- **Page IDs changed:** Pages previously numbered `01`, `02`, etc. now use the permanent format `P001`, `P002`, etc. Affects file naming in `Assets/ApprovedManual/`.

### Migration Guide
See `Docs/migration/v1-to-v2.md` for step-by-step migration instructions.

### Added
- Full Component System specification (C001–C015) in `Core/COMPONENT_SYSTEM.md`
- `PromptEngine/` directory with individual prompt files for all 10 pages
- `Assets/DesignSystem/Tokens/` — Design Token architecture
- `Core/COLOR_SYSTEM.md` — dedicated color system specification (previously inline in STYLE_GUIDE.md)
- `Core/RENDER_GUIDE.md` — rendering standards extracted from STYLE_GUIDE.md and expanded
- `Core/NAMING_CONVENTION.md`
- `STYLE_DECISIONS.md` with initial 10 ADRs
- `Templates/COLOR_SCHEME.yaml`
- `Templates/PDF_CONFIG.yaml`
- `Projects/` directory structure documentation

### Changed
- `Core/STYLE_GUIDE.md` — restructured into numbered sections, removed render content (moved to RENDER_GUIDE.md)
- `Core/PAGE_SYSTEM.md` — complete rewrite using permanent P### IDs
- `README.md` — full rewrite for v2 architecture

### Removed
- `Prompts/` directory — replaced by `PromptEngine/`
- `Components/` root-level directory — moved to `Assets/DesignSystem/Components/`
- `StyleGuide.pdf` binary — replaced by Markdown source in `Core/STYLE_GUIDE.md`

---

## [1.1.0] - 2023-06-20

### Added
- Pages P07 (Details) and P08 (Decals) specifications
- Basic typography documentation
- `Templates/PROJECT.yaml` starter file

### Fixed
- Page margins corrected for US Letter format (was using A4 values only)

---

## [1.0.0] - 2023-03-10

### Added
- Initial release of Mini4WD Manual SDK
- Basic page templates for pages 01–06
- Core style guide (colors, typography, grid)
- `Templates/PROJECT.yaml` v1 schema
- `Assets/` directory skeleton
- Apache 2.0 license
