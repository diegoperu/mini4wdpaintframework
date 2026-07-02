# Mini4WD Manual SDK

**Version 2.4.1** | Apache 2.0 | Open Source | Language: Italian (it)

---

> ## 🚀 New user? Start from **[START_HERE.md](START_HERE.md)**
>
> You do not need to read this README to produce a manual. The operator path is:
> `START_HERE.md` → `OperatorGuide/01_Primo_Manuale.md` → `FIRST_PROJECT.md`.
> This README describes the architecture, for contributors and developers.
>
> Operator documents (v2.4.1): [START_HERE.md](START_HERE.md) ·
> [OperatorGuide/](OperatorGuide/) · [WORKFLOW.md](WORKFLOW.md) ·
> [LIFECYCLE.md](LIFECYCLE.md) · [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) ·
> [FILE_MATRIX.md](FILE_MATRIX.md) · [WHO_MODIFIES_WHAT.md](WHO_MODIFIES_WHAT.md) ·
> [OPERATOR_PROFILE.md](OPERATOR_PROFILE.md) · tutorials [FIRST_PROJECT.md](FIRST_PROJECT.md),
> [FIRST_RENDER.md](FIRST_RENDER.md), [FIRST_PDF.md](FIRST_PDF.md)
>
> Note: operator-facing guides are written in Italian — the working language of the
> manuals and their operators. Framework and architecture docs are in English.

---

## Mission

Mini4WD Manual SDK is an open-source framework that enables any AI model to generate professional illustrated painting manuals for Tamiya Mini4WD models, maintaining consistent editorial and graphic standards across hundreds of projects.

The SDK provides a specification layer, component system, prompt engine, design tokens, text engine, and CMS layer required to produce manuals that are visually coherent, technically accurate, and immediately recognizable — regardless of which AI model, tool, or contributor generated them.

---

## Design Philosophy

This framework draws inspiration from Tamiya's technical catalogs and instruction sheets of the 1990s: clean white backgrounds, precise callout boxes, numbered steps, and a sense of craft that communicated both information and enthusiasm. That foundation is reinterpreted with modern graphic design sensibilities — structured grid systems, a systematic color palette anchored in violet, typographic hierarchy, and render-quality illustrations.

The result is a manual system that feels timeless without feeling dated. Every page should look like it was designed by the same studio, whether it was produced in 2024 or 2034.

All editorial text is produced in **Italian only**. No Japanese scripts (kanji, hiragana, katakana), no English body text, no Lorem ipsum placeholders are permitted in released pages.

---

## Architecture (v2.4.0)

The SDK separates content generation into three independent engines that execute in strict sequence:

```
TEXT ENGINE  →  QA ENGINE  →  RENDER ENGINE  →  PDF
```

### Text Engine
Generates all editorial text from PROJECT.yaml and Knowledge/ inputs. Output is a validated `content.yaml` file — the **primary source of truth** for every page. `text.md` is derived from `content.yaml` and is secondary.

### QA Engine
Validates `content.yaml` against the Content Validation suite (7 checks: schema, language, data completeness, metadata, manifest, component mapping, cross-page consistency) and the Text Validation suite (9 Italian-language compliance checks). A page cannot proceed to rendering until both suites pass.

### Render Engine
Reads `content.yaml` exclusively. Never reads `text.md` directly. Generates the illustrated page using Design Tokens, Component System, and Render Guide specifications.

### CMS Layer (ApprovedAssets/)
Each page is stored as a self-contained content module with 7 files:

```
ApprovedAssets/Text/P001/
├── content.yaml    ← PRIMARY source of truth
├── text.md         ← derived, read-only after approval
├── metadata.yaml   ← page lifecycle state
├── manifest.yaml   ← components, images, tokens, dependencies
├── changelog.md    ← revision history
├── notes.md        ← editorial annotations (not rendered)
└── README.md       ← module documentation
```

### Page Lifecycle

```
draft → review → approved → locked → rendered → released → archived
```

A page advances through the lifecycle only after passing QA at each gate. Locked pages cannot be edited without a formal revision.

### Prompt LOAD Sequence

Every PromptEngine/ prompt must load context in this order before generating:

```
DESIGN_LANGUAGE → COMPONENT_SYSTEM → TOKENS → TEXT_ENGINE →
LANGUAGE_POLICY → AI_OPERATING_RULES → PROJECT.yaml → GENERATE
```

---

## Quick Start

**Step 1 — Clone the SDK**
```bash
git clone https://github.com/diegoperu/mini4wdpaintframework.git
cd mini4wdpaintframework
```

**Step 2 — Create a project**
```bash
cp Templates/PROJECT.yaml Projects/MyModel/PROJECT.yaml
```
Edit `Projects/MyModel/PROJECT.yaml` with your model name, series, paint scheme, and render paths.

**Step 3 — Run the Text Engine (Phase 2a)**

For each page P001–P010, load the prompt from `PromptEngine/` following the LOAD sequence above. The Text Engine generates `ApprovedAssets/Text/P00x/content.yaml`.

**Step 4 — Run Content and Text QA (Phase 2b–2c)**

Validate each `content.yaml` against `Tests/ContentValidation.md` (7 suites) and `Tests/TextValidation.md` (9 suites). Fix all blocking failures before proceeding.

**Step 5 — Seal Approved Assets (Phase 2d)**

Set `metadata.yaml → status: locked` for each page that passes QA. Locked content cannot be modified without a changelog entry.

**Step 6 — Run the Render Engine (Phase 3)**

Submit the render prompt with the locked `content.yaml` as input. The Render Engine generates the illustrated page.

**Step 7 — Image and Page QA (Phase 4)**

Validate all renders against `Core/QA_SYSTEM.md` (110-item checklist) and the visual tests in `Tests/`.

**Step 8 — Export PDF (Phase 5)**

Once all 10 pages pass QA, export using `Templates/PDF_CONFIG.yaml`. See `Core/PDF_MASTER.md` for the full export specification.

For the full pipeline with all phases, see `Build/Pipeline.md`.

---

## Quick Start — For an AI Model

> If you are an AI model (ChatGPT, Claude, Gemini, or any other), read these files in order before generating anything. Do not skip steps.

**Step 1 — Read `AI_ENTRYPOINT.md`**

The official SDK entry point. Contains the Bootstrap Contract (binding rules for the entire session), mission, source-of-truth hierarchy, pipeline overview, Golden Rules, and the First Response Policy. After reading this file, produce a Bootstrap Report and wait for user approval before generating any content.

**Step 2 — Read `SDK_CONTEXT.yaml`**

Machine-readable SDK identity card. Confirms the version, pipeline sequence, source-of-truth hierarchy, and load order. Use this to verify you have the correct version of the SDK.

**Step 3 — Follow `BOOTSTRAP.md`**

Operational guide — expands on the rules and workflow from AI_ENTRYPOINT.md. Contains the detailed pipeline, page/component index, common errors to avoid, and document map.

**Step 4 — Read `Projects/{ModelName}/PROJECT.yaml`**

Project configuration for the current model. Contains the model name, paint colors (Tamiya codes + Italian names), and render paths. All content.yaml fields are populated from this file.

**Step 5 — Read `ApprovedAssets/Text/{page}/`**

Existing sealed content for each page. If `metadata.yaml → status: locked`, the page is already approved — proceed directly to rendering. Never regenerate locked content.

**Step 6 — Load Reference Images**

Photography of the physical Mini4WD model. Required by the Render Engine to ensure renders match the real product exactly. Do not modify the model's shape.

After loading all documents: produce a **Bootstrap Report** (format defined in `AI_ENTRYPOINT.md`) and wait for user approval before generating any content.

For the full AI context loading order with rationale, see `Docs/LOAD_ORDER.md`.
For ready-to-use prompts (ChatGPT, Claude, Gemini), see `Docs/AI_BOOTSTRAP_PROMPT.md`.
For step-by-step project creation, see `Projects/PROJECT_BOOTSTRAP.md`.

---

## Directory Structure

```
mini4wdpaintframework/
│
├── README.md                    ← You are here (human contributors)
├── BOOTSTRAP.md                 ← AI entry point — read THIS first (AI models)
├── SDK_CONTEXT.yaml             ← SDK identity card — version, pipeline, load order
├── STATUS.md                    ← Implementation status, roadmap, known issues
├── ReleaseInfo.yaml             ← Machine-readable release metadata
├── RepositoryManifest.yaml      ← Complete file and dependency map
├── CHANGELOG.md                 ← Version history
├── VERSION                      ← Current version (2.4.0)
├── MANIFEST.yaml                ← Full SDK descriptor (components, tokens, pages)
├── LICENSE                      ← Apache 2.0
├── STYLE_DECISIONS.md           ← Architecture Decision Records (ADR-001–ADR-021)
├── ROADMAP.md                   ← Planned features and future direction
├── MigrationReport_v2.4.md      ← Migration guide from v2.3.0 to v2.4.0
│
├── Core/                        ← Authoritative specification layer (Core/ always wins)
│   ├── DESIGN_LANGUAGE.md       ← 65 philosophical rules governing all design decisions
│   ├── STYLE_GUIDE.md           ← Colors, typography, grid, spacing
│   ├── COLOR_SYSTEM.md          ← Full color palette and usage rules
│   ├── MANUAL_SYSTEM.md         ← Architecture overview and lifecycle
│   ├── PAGE_SYSTEM.md           ← P001–P010 specifications
│   ├── COMPONENT_SYSTEM.md      ← C001–C015 specifications with content.yaml field mapping
│   ├── TEXT_ENGINE.md           ← Text Engine spec; content.yaml as primary output
│   ├── AI_OPERATING_RULES.md    ← 100 rules for AI model behavior (Rules 059–100: text rendering)
│   ├── RENDER_GUIDE.md          ← Rendering standards and AI render prompts
│   ├── PDF_MASTER.md            ← Export specification
│   ├── QA_SYSTEM.md             ← 110-item quality checklist
│   ├── WORKFLOW.md              ← End-to-end process documentation
│   ├── NAMING_CONVENTION.md     ← File and folder naming rules
│   ├── DOCUMENTATION_STYLE.md   ← How to write SDK documentation
│   └── DEFINITION_OF_DONE.md    ← Completion criteria
│
├── Config/                      ← Global SDK configuration
│   ├── sdk.yaml                 ← Global parameters and version
│   ├── render.yaml              ← Camera angles, lighting rigs, resolution
│   ├── pdf.yaml                 ← Export variants (screen / print / archive)
│   ├── quality.yaml             ← QA thresholds, blocking/non-blocking classification
│   └── LANGUAGE_POLICY.yaml     ← Italian-only policy, forbidden languages, approved placeholders
│
├── PromptEngine/                ← Page-specific AI prompts (model-agnostic)
│   ├── README.md                ← LOAD sequence and usage instructions
│   ├── Cover.md                 ← P001
│   ├── ColorScheme.md           ← P002
│   ├── Materials.md             ← P003
│   ├── Preparation.md           ← P004
│   ├── Painting.md              ← P005
│   ├── Masking.md               ← P006
│   ├── Details.md               ← P007
│   ├── Decals.md                ← P008
│   ├── Premium.md               ← P009
│   └── FinalChecklist.md        ← P010
│
├── ApprovedAssets/              ← CMS layer — sealed content modules per page (NEW v2.4.0)
│   ├── index.yaml               ← Registry of all page modules and their lifecycle state
│   ├── Text/
│   │   ├── P001/                ← Page module (7 files each: content.yaml, text.md,
│   │   ├── P002/                    metadata.yaml, manifest.yaml, changelog.md,
│   │   ├── ...                      notes.md, README.md)
│   │   └── P010/
│   ├── Images/                  ← Approved render images
│   ├── Components/              ← Approved component exports
│   ├── Templates/               ← Page layout templates
│   └── References/              ← Reference photography
│
├── Templates/                   ← Starter files for new projects
│   ├── PROJECT.yaml             ← Project configuration template
│   ├── PROJECT.md               ← Human-readable project brief template
│   ├── CHECKLIST.md             ← Per-project QA checklist
│   ├── COLOR_SCHEME.yaml        ← Paint scheme definition template
│   └── PDF_CONFIG.yaml          ← PDF export configuration
│
├── Projects/                    ← One subfolder per Mini4WD model
│   ├── PROJECT_BOOTSTRAP.md     ← Step-by-step guide for starting a new project
│   └── Proto_Emperor/           ← Reference project (read-only)
│       ├── PROJECT.yaml
│       ├── Images/
│       ├── Output/
│       ├── Notes/
│       └── ApprovedText/        ← Legacy path (v2.3.0); superseded by ApprovedAssets/
│
├── Assets/                      ← Design system, references, approved output
│   ├── DesignSystem/
│   │   ├── Tokens/              ← Design tokens (tokens.example.yaml, tokens.schema.yaml)
│   │   ├── Components/          ← Component wireframes and specs
│   │   ├── Palette/             ← Color swatch references
│   │   ├── Typography/          ← Font specimens
│   │   ├── Icons/               ← Icon library (planned v2.5.0; interim: Unicode symbols)
│   │   └── Layout/              ← Grid and wireframe templates
│   ├── ReferenceModels/         ← Reference photography per model
│   ├── ApprovedManual/          ← Production-approved manual output
│   └── Examples/                ← Example pages for onboarding
│
├── Build/                       ← Build pipeline documentation
│   └── Pipeline.md              ← 8-phase production pipeline (Phase 0 → Phase 7)
│
├── Tests/                       ← QA test suites (9 suites)
│   ├── ContentValidation.md     ← 7 suites validating content.yaml (NEW v2.4.0)
│   ├── TextValidation.md        ← 9 Italian-language compliance tests
│   ├── FrameworkIntegrity.md    ← SDK self-consistency
│   ├── PromptValidation.md
│   ├── LayoutValidation.md
│   ├── NamingValidation.md
│   ├── ColorValidation.md
│   ├── PDFValidation.md
│   └── AssetsValidation.md
│
├── Knowledge/                   ← Technical and editorial knowledge base (14 documents)
│   ├── Paints.md                ← Paint types, properties, compatibility
│   ├── Masking.md               ← Masking techniques
│   ├── Preparation.md           ← Surface preparation
│   ├── Painting.md              ← Painting techniques
│   ├── Decals.md                ← Decal application
│   ├── ClearCoat.md             ← Clear coat finishing
│   ├── Troubleshooting.md       ← Common issues and fixes
│   ├── Glossary.md              ← Technical glossary (EN)
│   ├── GlossaryIT.md            ← Technical glossary (IT)
│   ├── FAQ.md
│   ├── BestPractices.md
│   ├── EditorialStyle.md        ← Italian editorial voice and style
│   ├── Terminology.md           ← Approved Italian terminology
│   └── ForbiddenWords.md        ← Words and phrases never to use
│
└── Docs/                        ← Extended documentation and guides
    ├── LOAD_ORDER.md            ← Explicit AI context loading order with rationale
    ├── AI_BOOTSTRAP_PROMPT.md   ← Ready-to-use prompts for ChatGPT, Claude, Gemini
    └── migration/
        └── v1-to-v2.md          ← Migration guide: SDK v1.x → v2.x
```

---

## Core Documentation

### Bootstrap System

| Document | Purpose |
|---|---|
| [BOOTSTRAP.md](BOOTSTRAP.md) | **AI entry point** — rules, pipeline, page index, errors to avoid |
| [SDK_CONTEXT.yaml](SDK_CONTEXT.yaml) | SDK identity card — version, pipeline, source of truth |
| [Docs/LOAD_ORDER.md](Docs/LOAD_ORDER.md) | Explicit context loading order with rationale |
| [Docs/AI_BOOTSTRAP_PROMPT.md](Docs/AI_BOOTSTRAP_PROMPT.md) | Ready-to-use prompts for ChatGPT, Claude, Gemini |
| [Projects/PROJECT_BOOTSTRAP.md](Projects/PROJECT_BOOTSTRAP.md) | Step-by-step new project guide |
| [STATUS.md](STATUS.md) | Implementation status, roadmap, known issues |
| [ReleaseInfo.yaml](ReleaseInfo.yaml) | Machine-readable release metadata |
| [RepositoryManifest.yaml](RepositoryManifest.yaml) | Complete file and dependency map |

### Core Specifications

| Document | Purpose |
|---|---|
| [Core/DESIGN_LANGUAGE.md](Core/DESIGN_LANGUAGE.md) | 65 rules governing every design decision |
| [Core/STYLE_GUIDE.md](Core/STYLE_GUIDE.md) | Color, typography, grid, spacing specifications |
| [Core/PAGE_SYSTEM.md](Core/PAGE_SYSTEM.md) | Specification for pages P001–P010 |
| [Core/COMPONENT_SYSTEM.md](Core/COMPONENT_SYSTEM.md) | Specification for components C001–C015 |
| [Core/TEXT_ENGINE.md](Core/TEXT_ENGINE.md) | Text Engine spec; content.yaml as primary output |
| [Core/AI_OPERATING_RULES.md](Core/AI_OPERATING_RULES.md) | 100 behavioral rules for AI models |
| [Core/RENDER_GUIDE.md](Core/RENDER_GUIDE.md) | Illustration standards and AI render prompts |
| [Core/QA_SYSTEM.md](Core/QA_SYSTEM.md) | 110-item quality checklist |
| [Core/WORKFLOW.md](Core/WORKFLOW.md) | End-to-end production workflow |
| [Config/LANGUAGE_POLICY.yaml](Config/LANGUAGE_POLICY.yaml) | Italian-only policy and forbidden language rules |
| [Build/Pipeline.md](Build/Pipeline.md) | 8-phase production pipeline |

---

## Versioning Policy

This project follows [Semantic Versioning 2.0.0](https://semver.org/).

- **MAJOR** version: breaking changes to page IDs, component IDs, token names, or PROJECT.yaml schema
- **MINOR** version: new pages, components, tokens, or layers added in a backwards-compatible manner
- **PATCH** version: bug fixes, clarifications, typo corrections

Version is stored in `VERSION` and `MANIFEST.yaml`. Every release is documented in `CHANGELOG.md`. Breaking changes include a migration guide in `Docs/migration/`.

| Version | Key Addition |
|---------|-------------|
| 2.1.0 | Core framework: Design Language, Component System, Design Tokens, PromptEngine |
| 2.2.0 | Build pipeline, Config layer, Test suites, AI Operating Rules, Knowledge base |
| 2.3.0 | Text Engine, Editorial Pipeline, Italian language policy, LOAD sequence |
| 2.4.0 | CMS layer (ApprovedAssets/), content.yaml as source of truth, page lifecycle |
| 2.4.1 | UX & Operator Workflow Update: START_HERE, OperatorGuide/, tutorials, single image convention, validation scoping |

---

## Contributing

Contributions are welcome. Before opening a pull request:

1. Read `Core/DOCUMENTATION_STYLE.md` to match the existing documentation voice
2. For any change to `Core/`, file an Architecture Decision Record in `STYLE_DECISIONS.md`
3. Update `CHANGELOG.md` under `[Unreleased]`
4. Ensure your changes pass the test suites in `Tests/`
5. Ensure your changes meet the criteria in `Core/DEFINITION_OF_DONE.md`

Open issues and feature requests are tracked on GitHub. Tag feature requests with the `roadmap` label. See `ROADMAP.md` for what is already planned.

---

## License

Copyright 2024 Mini4WD Manual SDK Contributors.

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full terms.

---

*Mini4WD Manual SDK is not affiliated with Tamiya Inc. "Mini 4WD" is a trademark of Tamiya Inc. This SDK is an independent open-source project for hobbyist documentation.*
