# BOOTSTRAP.md
# Mini4WD Manual SDK — AI Operational Guide

> **AI models: read `AI_ENTRYPOINT.md` before this document.**
> `AI_ENTRYPOINT.md` is the official entry point — it contains the Bootstrap Contract,
> Golden Rules, and First Response Policy. This document expands on the operational
> details after you have read the entrypoint.

---

## What is the Mini4WD Manual SDK?

The **Mini4WD Manual SDK** is an open-source editorial framework that enables any AI model — ChatGPT, Claude, or any future model — to generate professional illustrated painting manuals for Tamiya Mini4WD scale models. (Gemini: non supportato — vedi `UAT/UAT-002.md`.)

It is a **specification-first system**: the SDK defines every design rule, editorial rule, component, and workflow in authoritative documents. The AI's role is to execute these specifications, not to invent them.

The current version is **2.5.0** (codename: MultiProject — Multi-Project Content Isolation; 2.5.x family: per-variant CMS)..

---

## What this SDK is NOT

| It is NOT | It IS |
|-----------|-------|
| A generative free-form system | A specification-driven framework |
| A Stable Diffusion plugin | A set of structured prompts for any AI model |
| A 3D modeling tool | An illustration and editorial framework |
| An automatic pipeline | A guided manual process (v2.5.0 will add automation) |
| A Japanese-aesthetic system | A Tamiya-inspired, Italian-editorial system |
| A replacement for human review | A tool that produces QA-ready drafts for review |

---

## Core Rules (Non-Negotiable)

Before doing anything, internalize these rules:

1. **Language is Italian (it).** All editorial text — titles, subtitles, captions, steps, callouts — must be in Italian. No Japanese. No English body text. No Lorem ipsum.
2. **content.yaml is the source of truth.** Generate `content.yaml` first. The Render Engine reads `content.yaml` only — never `text.md` directly.
3. **Do not invent data.** If PROJECT.yaml does not specify a value, use `TODO:` as placeholder. Never fabricate model names, colors, or technical data.
4. **Do not modify the model's shape.** Renders must match the physical model. No creative liberties with form or structure.
5. **Design Tokens are mandatory.** All colors, sizes, and spacing must reference token names (e.g., `{{token.PrimaryViolet}}`), never hardcoded values.
6. **Core/ is authoritative.** Nothing in Docs/, Templates/, or any other directory overrides Core/.
7. **Page IDs and Component IDs are permanent.** P001–P010 and C001–C015 never change, never get renumbered.
8. **QA is blocking.** A page cannot be rendered until it passes `Tests/ContentValidation.md` and `Tests/TextValidation.md`. A page cannot be released until it passes `Core/QA_SYSTEM.md`.
9. **The Render Engine does not write text.** It places text that already exists in `content.yaml` onto the page — nothing more.
10. **LOAD sequence is mandatory.** Load context in the order defined in `Docs/LOAD_ORDER.md`. Never skip steps.

---

## Pipeline Overview

The production pipeline runs in strict sequence. Never run stages out of order.

```
Phase 0: Project Setup
         └─ Create PROJECT.yaml from Templates/PROJECT.yaml

Phase 1: Reference Models
         └─ Load reference images of the Mini4WD model

Phase 2: Knowledge Load
         └─ Load Core/ specs + Knowledge/ documents

Phase 2a: Text Engine
          └─ Generate content.yaml for each page P001–P010
          └─ Output: Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml

Phase 2b: Content QA
          └─ Validate content.yaml with Tests/ContentValidation.md (7 suites)
          └─ BLOCKING: fix all failures before proceeding

Phase 2c: Text QA
          └─ Validate with Tests/TextValidation.md (9 Italian compliance tests)
          └─ BLOCKING: fix all failures before proceeding

Phase 2d: Approved Assets Sealing
          └─ Set metadata.yaml → status: locked
          └─ Locked pages cannot be edited without changelog entry

Phase 3: Render Engine
         └─ Generate illustrated page from locked content.yaml
         └─ Input: content.yaml ONLY
         └─ Output: Projects/{Model}/{Variant}/ApprovedImages/P00x/

Phase 4: Image and Page QA
         └─ Validate with Core/QA_SYSTEM.md (110-item checklist)

Phase 5: PDF Generation
         └─ Assemble all 10 pages with Templates/PDF_CONFIG.yaml

Phase 6: Approved Manual
         └─ Output: Assets/ApprovedManual/{ModelName}/

Phase 7: Release
         └─ Tag release, update Projects/{Model}/{Variant}/index.yaml
```

Full details: `Build/Pipeline.md`

---

## How to Start

### Path A — From the GitHub repository

```
1. Clone: git clone https://github.com/diegoperu/mini4wdpaintframework.git
2. Read:  SDK_CONTEXT.yaml
3. Read:  BOOTSTRAP.md  (this file)
4. Follow: Docs/LOAD_ORDER.md
5. Start:  Projects/PROJECT_BOOTSTRAP.md
```

### Path B — From the SDK ZIP

```
1. Unzip the SDK
2. Read:  SDK_CONTEXT.yaml
3. Read:  BOOTSTRAP.md  (this file)
4. Follow: Docs/LOAD_ORDER.md
5. Start:  Projects/PROJECT_BOOTSTRAP.md
```

### Path C — AI model receiving only BOOTSTRAP.md and SDK_CONTEXT.yaml

If you received only these two files, you have enough to understand the framework structure. Request the following files before generating any page:

```
Required minimum:
- Core/AI_OPERATING_RULES.md
- Config/LANGUAGE_POLICY.yaml
- Core/TEXT_ENGINE.md
- Core/DESIGN_LANGUAGE.md
- Core/STYLE_GUIDE.md
- Core/COMPONENT_SYSTEM.md
- Core/PAGE_SYSTEM.md
- PromptEngine/{page}.md
- Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml
```

See `Docs/AI_BOOTSTRAP_PROMPT.md` for the ready-to-use prompt to request these files.

---

## Context Loading Order

Load documents in this exact sequence. See `Docs/LOAD_ORDER.md` for full details.

```
1.  SDK_CONTEXT.yaml          ← SDK identity, version, pipeline overview
2.  BOOTSTRAP.md              ← This file — rules, workflow, how to start
3.  Core/AI_OPERATING_RULES.md ← 100 behavioral rules for AI models
4.  Config/LANGUAGE_POLICY.yaml ← Italian-only policy, forbidden languages
5.  Core/TEXT_ENGINE.md       ← Text generation rules, content.yaml format
6.  Core/DESIGN_LANGUAGE.md   ← 65 design philosophy rules
7.  Core/STYLE_GUIDE.md       ← Colors, typography, grid
8.  Core/COMPONENT_SYSTEM.md  ← C001–C015 specifications
9.  Core/PAGE_SYSTEM.md       ← P001–P010 specifications
10. PromptEngine/{page}.md    ← Page-specific prompt
11. Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml ← Project data
12. Projects/{Model}/{Variant}/ApprovedText/{page}/ ← Existing approved content (if any)
13. Reference images           ← Photography of the physical model
```

---

## Pages (P001–P010)

| ID | Name | Prompt File |
|----|------|-------------|
| P001 | Copertina (Cover) | PromptEngine/Cover.md |
| P002 | Schema Colori (Color Scheme) | PromptEngine/ColorScheme.md |
| P003 | Materiali (Materials) | PromptEngine/Materials.md |
| P004 | Preparazione (Preparation) | PromptEngine/Preparation.md |
| P005 | Verniciatura (Painting) | PromptEngine/Painting.md |
| P006 | Mascheratura (Masking) | PromptEngine/Masking.md |
| P007 | Dettagli (Details) | PromptEngine/Details.md |
| P008 | Decal (Decals) | PromptEngine/Decals.md |
| P009 | Variante Premium (Premium) | PromptEngine/Premium.md |
| P010 | Checklist Finale (Final Checklist) | PromptEngine/FinalChecklist.md |

---

## Components (C001–C015)

| ID | Component | Key Rule |
|----|-----------|----------|
| C001 | Header | Violet panel, Italian title only |
| C002 | Footer | Page ID + model name, never empty |
| C003 | Color Palette | Swatch grid, Tamiya code + Italian name |
| C004 | Step Grid | Numbered, left-to-right, Italian labels |
| C005 | Paint Sequence | Arrow progression, numbered |
| C006 | Callout Box | Informational, violet border |
| C007 | Exploded View | Dot callouts on render |
| C008 | Warning Box | Red accent, Italian text |
| C009 | Tips Box | Star marker, Italian text |
| C010 | Checklist | Checkbox grid, Italian items |
| C011 | Material List | Icon + Italian name + code |
| C012 | Zoom Detail | Magnified area with border |
| C013 | Comparison Panel | Before/after layout |
| C014 | Time Box | Clock icon + Italian duration |
| C015 | Notes Box | Pencil marker, editorial annotation |

Full specifications: `Core/COMPONENT_SYSTEM.md`

---

## content.yaml Structure (Per Page)

Every page's primary source of truth is a `content.yaml` file:

```yaml
page:
  id: "P001"
  name: "Copertina"
  version: "1.0.0"
  language: "it"

title: ""             # Italian — required
subtitle: ""          # Italian — required
footer:
  page_id: "P001"
  model_name: ""      # From PROJECT.yaml

render:
  file: ""            # Render image path
  angle: "3/4 front-left"
  lighting: "studio-neutral"

component_mapping:
  C001: {uses: []}
  C002: {uses: ["footer.page_id", "footer.model_name"]}
```

Full format: `Core/TEXT_ENGINE.md`

---

## Page Lifecycle

```
draft → review → approved → locked → rendered → released → archived
```

- **locked**: content sealed, render can begin, no edits without changelog entry
- **rendered**: visual page generated from locked content.yaml
- **released**: page is in the final published manual

Lifecycle state is stored in `Projects/{Model}/{Variant}/ApprovedText/P00x/metadata.yaml`.

---

## Expected Output

A complete Mini4WD Manual is:
- 10 pages (P001–P010)
- All text in Italian
- All pages generated from validated `content.yaml` files
- All renders matching the physical model without invented details
- All design tokens applied — no hardcoded values
- PDF in three variants: screen, print, archive (see `Templates/PDF_CONFIG.yaml`)
- All pages passing `Core/QA_SYSTEM.md` 110-item checklist

---

## Common AI Errors to Avoid

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Writing text in English or Japanese | QA failure — page rejected | Apply `Config/LANGUAGE_POLICY.yaml` strictly |
| Inventing model colors not in PROJECT.yaml | Incorrect manual | Use only values from PROJECT.yaml; use `TODO:` for unknowns |
| Running Render Engine before Text QA | Invalid render from unvalidated content | Strict pipeline order — Phase 2b/2c before Phase 3 |
| Hardcoding `#4B0082` instead of `{{token.PrimaryViolet}}` | Token system violation | All values from `Assets/DesignSystem/Tokens/tokens.example.yaml` |
| Modifying the physical shape of the model in renders | Inaccurate technical manual | Render exactly what the reference images show |
| Skipping LOAD sequence steps | Incomplete context, rule conflicts | Follow `Docs/LOAD_ORDER.md` exactly |
| Writing content.yaml with incomplete fields | ContentValidation.md failure | All required fields must be populated or marked `TODO:` |
| Using Lorem ipsum as placeholder | Language policy violation | Use `TODO:` as the only permitted placeholder |

---

## Key Document Map

| Need | Read |
|------|------|
| Understand the framework | `SDK_CONTEXT.yaml` + `BOOTSTRAP.md` (this file) |
| Load context in correct order | `Docs/LOAD_ORDER.md` |
| Know all AI behavioral rules | `Core/AI_OPERATING_RULES.md` |
| Know language rules | `Config/LANGUAGE_POLICY.yaml` |
| Generate text for a page | `Core/TEXT_ENGINE.md` + `PromptEngine/{page}.md` |
| Generate a render | `Core/RENDER_GUIDE.md` + `Core/DESIGN_LANGUAGE.md` |
| Validate a page | `Tests/ContentValidation.md` + `Tests/TextValidation.md` |
| Run full QA | `Core/QA_SYSTEM.md` |
| Export PDF | `Core/PDF_MASTER.md` + `Templates/PDF_CONFIG.yaml` |
| Start a new project | `Projects/PROJECT_BOOTSTRAP.md` |
| Get a ready-to-use AI prompt | `Docs/AI_BOOTSTRAP_PROMPT.md` |
| Check SDK status and roadmap | `STATUS.md` |
| Check current release | `ReleaseInfo.yaml` |

---

## Cross References

- `SDK_CONTEXT.yaml` — machine-readable version of this document
- `Docs/LOAD_ORDER.md` — explicit loading order with rationale
- `STATUS.md` — current implementation status and TODO list
- `Core/AI_OPERATING_RULES.md` — 100 rules this document summarizes
- `Core/WORKFLOW.md` — detailed end-to-end workflow
- `Build/Pipeline.md` — full 8-phase pipeline specification
- `README.md` — project overview for human contributors

---

*This document is maintained as part of the Mini4WD Manual SDK. Update it at every minor or major release.*
