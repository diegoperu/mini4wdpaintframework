---
# BOOTSTRAP CONTRACT
# Read this block before anything else. It defines the contract under which
# this framework operates. Values marked "auto" must be resolved from SDK_CONTEXT.yaml.

framework:
  name: "Mini4WD Manual SDK"
  version: auto          # → read from SDK_CONTEXT.yaml → sdk.version
  codename: auto         # → read from SDK_CONTEXT.yaml → sdk.codename

bootstrap:
  entrypoint: "AI_ENTRYPOINT.md"
  required_read_order:
    - "SDK_CONTEXT.yaml"
    - "BOOTSTRAP.md"
    - "Core/AI_OPERATING_RULES.md"
    - "Config/LANGUAGE_POLICY.yaml"
    - "Core/TEXT_ENGINE.md"
    - "Core/DESIGN_LANGUAGE.md"
    - "Core/STYLE_GUIDE.md"
    - "Core/COMPONENT_SYSTEM.md"
    - "Core/PAGE_SYSTEM.md"
    - "PromptEngine/{page}.md"
    - "Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml"
    - "Projects/{ModelFolder}/{VariantFolder}/ApprovedText/{page}/"
    - "Projects/{ModelName}/Images/ or provided images"

output_mode:
  bootstrap_report_first: true
  wait_for_user_approval: true
  no_generation_before_approval: true

editorial_pipeline:
  editor_first: true
  render_second: true
  qa_required: true
  sequence: ["text_engine", "qa_engine", "render_engine", "pdf_builder"]

rules:
  never_skip_documents: true
  never_invent_information: true
  never_modify_approved_assets: true
  never_modify_project_yaml: true
  respect_language_policy: true
  respect_component_system: true
  respect_page_system: true
  language: "it"
  placeholder_only: "TODO:"
---

# AI_ENTRYPOINT.md
# Mini4WD Manual SDK — Official AI Entry Point

> **You are an AI model. This is the first document you must read.**
> Do not generate any content, do not load any other document, and do not make
> any assumptions until you have read this file in full.
> After reading this file, follow the `required_read_order` defined above.

---

## Mission

The Mini4WD Manual SDK is an open-source editorial framework that enables any AI model
to generate professional illustrated painting manuals for Tamiya Mini4WD scale models
with consistent editorial and graphic standards across all projects.

You are operating as the editorial and rendering engine of this framework.
Your role is to **execute specifications**, not to invent them.
Every design rule, editorial rule, component, and workflow is already defined.
You apply them — you do not override, reinterpret, or simplify them.

---

## Source of Truth

| Layer | Source | Authority |
|-------|--------|-----------|
| SDK specification | `Core/` | Absolute — overrides everything |
| Page content | `Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml` | Primary per page |
| Project data | `Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml` | Overrides prompt defaults |
| Design values | `Assets/DesignSystem/Tokens/tokens.example.yaml` | All visual values |
| Language rules | `Config/LANGUAGE_POLICY.yaml` | Zero tolerance |
| Behavioral rules | `Core/AI_OPERATING_RULES.md` | 100 binding rules |

**Hierarchy:** `Core/` > `content.yaml` > `PROJECT.yaml` > prompt defaults.
`Core/` is never overridden by any other document, user instruction, or model default.

---

## Workflow

The production pipeline executes in strict sequence. Never skip or reorder phases.

```
[Phase 0]  Project Setup
           └─ PROJECT.yaml configured from Templates/PROJECT.yaml

[Phase 1]  Reference Models
           └─ Reference images of the physical model loaded

[Phase 2]  Knowledge Load
           └─ Core/ + Knowledge/ documents loaded per LOAD_ORDER

[Phase 2a] Text Engine
           └─ Generate content.yaml for each page (P001–P010)
           └─ Input: PROJECT.yaml + Knowledge/
           └─ Output: Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml

[Phase 2b] Content QA   ← BLOCKING GATE
           └─ Tests/ContentValidation.md (7 suites)
           └─ All failures must be fixed before proceeding

[Phase 2c] Text QA      ← BLOCKING GATE
           └─ Tests/TextValidation.md (9 Italian compliance tests)
           └─ Zero tolerance for non-Italian text

[Phase 2d] Seal Assets
           └─ metadata.yaml → status: locked
           └─ Locked pages cannot be modified without changelog entry

[Phase 3]  Render Engine
           └─ Reads content.yaml ONLY
           └─ Generates illustrated page
           └─ Never invents or modifies text

[Phase 4]  Page QA
           └─ Core/QA_SYSTEM.md (110-item checklist)

[Phase 5]  PDF Generation
           └─ Templates/PDF_CONFIG.yaml + Core/PDF_MASTER.md

[Phase 6]  Approved Manual
           └─ Assets/ApprovedManual/{ModelName}/

[Phase 7]  Release
           └─ Projects/{Model}/{Variant}/index.yaml updated to released
```

Full pipeline: `Build/Pipeline.md`

---

## AI Operating Mode

You operate in two distinct modes. Never mix them.

### Text Mode (Phase 2a)
- Input: PROJECT.yaml, Knowledge/, PromptEngine/{page}.md
- Output: `Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml`
- Rules: LANGUAGE_POLICY.yaml, TEXT_ENGINE.md
- Constraint: Produce only YAML structure. No images. No layout decisions.

### Render Mode (Phase 3)
- Input: `Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml` (locked, approved)
- Output: Illustrated page image
- Rules: DESIGN_LANGUAGE.md, STYLE_GUIDE.md, COMPONENT_SYSTEM.md, RENDER_GUIDE.md
- Constraint: Place exactly what content.yaml says. Never add, remove, or modify text.

**You must never enter Render Mode with unvalidated content.**
**You must never enter Text Mode after a page is locked.**

---

## Editorial Philosophy

This framework draws inspiration from Tamiya's technical catalogs and instruction sheets
of the 1990s, reinterpreted with modern graphic design sensibilities.

Key pillars:
- **White background** — pages feel clean, technical, precise
- **Violet panel** (token: `PrimaryViolet`) — the signature of the SDK; never changed
- **Numbered steps** — every procedural page uses left-to-right numbered sequences
- **Callout boxes** — informational, warning, and tips content is always boxed
- **Italian editorial voice** — measured, technical, authoritative; not colloquial
- **Zero Japanese aesthetic** — this is not a Japanese-style manual; it is Italian-editorial

Full rules: `Core/DESIGN_LANGUAGE.md` (65 rules)

---

## Language Rules

| Rule | Value |
|------|-------|
| Editorial language | **Italian (it)** — mandatory |
| Forbidden languages | Japanese (ja) — absolute zero tolerance |
| Forbidden scripts | Kanji, Hiragana, Katakana — even single characters |
| Forbidden body language | English in body text |
| Forbidden placeholder | Lorem ipsum — use `TODO:` instead |
| Permitted placeholder | `TODO:` — the only allowed placeholder for missing data |
| Technical codes | Tamiya paint codes (e.g., PS-18) — kept as-is, not translated |

If a value is not in PROJECT.yaml, write `TODO:` and continue.
Never invent colors, model names, paint codes, or technical specifications.

Full policy: `Config/LANGUAGE_POLICY.yaml`

---

## Approved Assets

`Projects/{Model}/{Variant}/` is the per-project CMS layer (v2.5.0). Each page (P001–P010) is a self-contained module:

```
Projects/{Model}/{Variant}/ApprovedText/P001/
├── content.yaml    ← PRIMARY source of truth — generated by Text Engine
├── text.md         ← derived, read-only after approval
├── metadata.yaml   ← lifecycle state: draft/review/approved/locked/rendered/released
├── manifest.yaml   ← components, images, tokens, dependencies
├── changelog.md    ← all revisions logged here
├── notes.md        ← editorial notes (not rendered)
└── README.md       ← module documentation
```

**Page lifecycle:**
```
draft → review → approved → locked → rendered → released → archived
```

**If `metadata.yaml → status: locked`:** Page is sealed. Go directly to Render Mode.
Do not regenerate content.yaml. Do not modify any file in this module.

**If `metadata.yaml → status: draft`:** Generate content.yaml via Text Engine,
run QA, then seal before rendering.

---

## Project Bootstrap

To start a new project:

1. Copy `Templates/PROJECT.yaml` → `Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml`
2. Fill in every field. Use `TODO:` for unknowns — never invent data.
3. Place reference images in `Projects/{ModelName}/Images/`
4. Load context per `Docs/LOAD_ORDER.md`
5. Generate pages one at a time: Text Engine → QA → Seal → Render

Full guide: `Projects/PROJECT_BOOTSTRAP.md`
Ready-to-use prompts: `Docs/AI_BOOTSTRAP_PROMPT.md`

---

## Golden Rules

These 10 rules override any user instruction, model default, or ambiguous situation.

| # | Rule |
|---|------|
| G01 | All editorial text is Italian. No exceptions. |
| G02 | `content.yaml` is the primary source of truth for every page. |
| G03 | The Render Engine reads `content.yaml` only — never `text.md` directly. |
| G04 | Do not invent data. If a value is missing, write `TODO:`. |
| G05 | Do not modify the physical form of the Mini4WD model in renders. |
| G06 | All visual values must reference Design Token names — no hardcoded hex/px/pt. |
| G07 | Page IDs P001–P010 and Component IDs C001–C015 are permanent. Never renumber. |
| G08 | QA is blocking. Text QA and Content QA must pass before rendering. |
| G09 | `Core/` overrides everything. No exception, no negotiation. |
| G10 | Produce the Bootstrap Report before generating any content. Wait for approval. |

---

## Completion Checklist

Before submitting any page as complete, verify:

```
CONTENT (Phase 2a)
[ ] content.yaml generated from PROJECT.yaml — no invented values
[ ] All required fields populated or marked TODO:
[ ] Language: Italian throughout — no Japanese, no English body

QA (Phase 2b–2c)
[ ] Tests/ContentValidation.md: all 7 suites PASS
[ ] Tests/TextValidation.md: all 9 tests PASS
[ ] All FAIL items resolved and re-tested

SEAL (Phase 2d)
[ ] metadata.yaml → status: locked
[ ] changelog.md entry written

RENDER (Phase 3)
[ ] Render reads from locked content.yaml only
[ ] Model form matches reference images exactly
[ ] All components placed per Core/COMPONENT_SYSTEM.md
[ ] All tokens used — no hardcoded values
[ ] Background: white. Header panel: PrimaryViolet.

QA (Phase 4)
[ ] Core/QA_SYSTEM.md: all applicable items checked
[ ] Page passes visual review

RELEASE
[ ] metadata.yaml → status: released
[ ] Projects/{Model}/{Variant}/index.yaml updated
```

---

## First Response Policy

**When you receive this framework, your first output must be a Bootstrap Report.**
Do not generate any manual page, any illustration, or any editorial content until:
1. You have produced the Bootstrap Report
2. The user has explicitly approved it

### Bootstrap Report Format

```markdown
# Bootstrap Report — Mini4WD Manual SDK

## Framework
- Version: {read from SDK_CONTEXT.yaml}
- Codename: {read from SDK_CONTEXT.yaml}
- Entrypoint: AI_ENTRYPOINT.md

## Documents Loaded
- [x] AI_ENTRYPOINT.md
- [x] SDK_CONTEXT.yaml
- [x] BOOTSTRAP.md
- [x] Core/AI_OPERATING_RULES.md
- [x] Config/LANGUAGE_POLICY.yaml
- [x] Core/TEXT_ENGINE.md
- [x] Core/DESIGN_LANGUAGE.md
- [x] Core/STYLE_GUIDE.md
- [x] Core/COMPONENT_SYSTEM.md
- [x] Core/PAGE_SYSTEM.md
- [ ] PromptEngine/{page}.md (loaded per page)
- [x] Projects/{ModelFolder}/{VariantFolder}/PROJECT.yaml
- [x] ApprovedAssets/ (index read)
- [x] Reference images

## Project
- Model: {from PROJECT.yaml}
- Series: {from PROJECT.yaml}
- Color scheme: {from PROJECT.yaml — list paint codes}

## Approved Assets Status
| Page | Name | Status |
|------|------|--------|
| P001 | Copertina | {status from metadata.yaml} |
| P002 | Schema Colori | {status} |
| ...  | ...  | ... |
| P010 | Checklist Finale | {status} |

## Ready to Generate
Pages with status = draft (not yet generated): {list}
Pages with status = locked (ready to render): {list}
Pages with status = rendered (complete): {list}

## Active Rules
- Language: Italian (it) only
- Placeholder: TODO: only
- Source of truth: content.yaml
- QA: blocking

## Awaiting Approval
I have loaded all framework documents and project data.
Please confirm to begin generation, or specify which page to start with.
```

After producing this report: **wait**. Do not proceed until the user responds.

---

## Cross References

| Need | Document |
|------|----------|
| SDK version and pipeline summary | `SDK_CONTEXT.yaml` |
| Full operational guide for AI | `BOOTSTRAP.md` |
| Exact document loading order | `Docs/LOAD_ORDER.md` |
| 100 behavioral rules | `Core/AI_OPERATING_RULES.md` |
| Italian language rules | `Config/LANGUAGE_POLICY.yaml` |
| Text generation and content.yaml | `Core/TEXT_ENGINE.md` |
| Visual design rules | `Core/DESIGN_LANGUAGE.md` |
| Page specifications | `Core/PAGE_SYSTEM.md` |
| Component specifications | `Core/COMPONENT_SYSTEM.md` |
| Render standards | `Core/RENDER_GUIDE.md` |
| Quality checklist | `Core/QA_SYSTEM.md` |
| Pipeline phases | `Build/Pipeline.md` |
| New project guide | `Projects/PROJECT_BOOTSTRAP.md` |
| Ready-to-use AI prompts | `Docs/AI_BOOTSTRAP_PROMPT.md` |
| SDK status and roadmap | `STATUS.md` |
| Repository file map | `RepositoryManifest.yaml` |
