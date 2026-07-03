# Mini4WD Manual SDK — Status

**Version:** 2.4.1 | **Status:** Active | **Maturity:** Beta

> This document is updated at every release. For machine-readable metadata see `ReleaseInfo.yaml` and `SDK_CONTEXT.yaml`.

---

## Current Version

| Field | Value |
|-------|-------|
| Version | 2.4.1 |
| Codename | Operator (2.4.x family: CMS) |
| Release name | UX & Operator Workflow Update |
| Release date | 2026-07-02 |
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
| **2.5.0** | **Planned** | Compiler/, Prompt Orchestrator, Icon Library, Tutorials |

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

### CMS Layer (v2.4.0)
- ApprovedAssets/ — 7-file content modules per page for P001–P010
- content.yaml — primary source of truth, supersedes text.md as primary output
- Page lifecycle — draft → review → approved → locked → rendered → released → archived
- Content Validation suite — Tests/ContentValidation.md (7 validation suites)
- ApprovedAssets/index.yaml — global registry of all page module lifecycle states
- MigrationReport_v2.4.md — migration guide from v2.3.0 with workflow diagram

### Bootstrap System (v2.4.0)
- AI_ENTRYPOINT.md — official AI entry point with Bootstrap Contract, Golden Rules, First Response Policy
- SDK_CONTEXT.yaml — machine-readable SDK identity card
- BOOTSTRAP.md — AI operational guide (detailed pipeline, error table, document map)
- Docs/LOAD_ORDER.md — explicit 13-step context loading order with rationale
- RepositoryManifest.yaml — complete file and dependency map with AI load order
- Projects/PROJECT_BOOTSTRAP.md — new project guide
- Docs/AI_BOOTSTRAP_PROMPT.md — 6 official prompts for ChatGPT / Claude / Gemini (Prompt A–F)
- STATUS.md — this document
- ReleaseInfo.yaml — machine-readable release metadata

---

## Planned Features (v2.5.0)

| Feature | Description | Priority |
|---------|-------------|----------|
| Compiler/ | Automated pipeline executor (Project Loader, Context Builder, Page Generator, QA Engine, PDF Assembler) | High |
| Prompt Orchestrator | Manages LOAD sequence and context injection automatically | High |
| Icon Library | 15 SVG icons — currently using Unicode fallbacks | Medium |
| Docs/tutorial/ | End-to-end tutorial documents for new users | Medium |
| Release System | Automated release tagging and manifest update | Low |

---

## Known Issues

None currently documented.

---

## TODO

| ID | Description | Priority | Target Version |
|----|-------------|----------|----------------|
| TODO-001 | Create Compiler/ subsystem | High | v2.5.0 |
| TODO-002 | Create 15 SVG icons in Assets/DesignSystem/Icons/ | Medium | v2.5.0 |
| TODO-003 | Write Docs/tutorial/first-manual.md | Medium | v2.5.0 |
| TODO-004 | Write Docs/tutorial/render-generation.md | Medium | v2.5.0 |
| TODO-005 | Write Docs/tutorial/pdf-export.md | Medium | v2.5.0 |
| TODO-006 | Create Release System automation | Low | v2.5.0 |
| TODO-007 | Populate Projects/Proto_Emperor/Violet_Phantom/ApprovedText/ (v2.5.0 path; ApprovedAssets/ is deprecated and removed) | High | Active |
| TODO-008 | Populate Projects/Proto_Emperor/Violet_Phantom/ApprovedImages/ (v2.5.0 path; ApprovedAssets/ is deprecated and removed) | High | Active |

---

## Cross References

- Architecture decisions: `STYLE_DECISIONS.md` (ADR-001–ADR-021)
- Full version history: `CHANGELOG.md`
- Release metadata: `ReleaseInfo.yaml`
- SDK identity: `SDK_CONTEXT.yaml`
- AI entry point: `BOOTSTRAP.md`
- Loading order: `Docs/LOAD_ORDER.md`
- Full roadmap: `ROADMAP.md`
