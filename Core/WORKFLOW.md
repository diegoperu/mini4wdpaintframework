# Workflow

This document describes the complete end-to-end process for producing a Mini4WD painting manual using the SDK. Every manual follows this workflow. Skipping phases is not permitted — each phase's output is the input to the next.

**AI models:** Read `AI_ENTRYPOINT.md` first (contains Bootstrap Contract and First Response Policy), then `SDK_CONTEXT.yaml` and `BOOTSTRAP.md`. Load context in the full order defined in `Docs/LOAD_ORDER.md`.

See also: `MANUAL_SYSTEM.md` for architecture context, `QA_SYSTEM.md` for the QA checklist.

---

## Overview

```
Phase 0: Project Setup
       │
       ▼
Phase 1: Render Generation
       │
       ▼
Phase 2: Manual Generation
       │
       ▼
Phase 3: QA
       │
       ├── FAIL → Return to Phase 2 (or Phase 1 if render failure)
       │
       ▼
Phase 4: Approval & Publication
```

---

## Phase 0: Project Setup

**Goal:** Create the complete data foundation for the manual before any generation begins. A manual started with incomplete data will require multiple iterations to fix.

### Steps

**0.1** Create the project directory:
```
Projects/{ModelName}/
```
The folder name must match the official Tamiya model name with underscores replacing spaces (e.g., `Proto_Emperor`). See `Core/NAMING_CONVENTION.md`.

**0.2** Copy the project template:
```bash
cp Templates/PROJECT.yaml Projects/{ModelName}/PROJECT.yaml
```

**0.3** Fill in all required fields in `Projects/{ModelName}/PROJECT.yaml`.

Open the file and complete every field that has a `required: true` comment. Do not submit the prompt for any page until all required fields are complete. Required fields that are missing will produce unfilled `{{project.X}}` tokens in page output.

**0.4** Gather reference images:
```
Assets/ReferenceModels/{ModelName}/
├── reference_front.jpg
├── reference_side.jpg
├── reference_top.jpg
├── box_art.jpg          (optional but recommended)
└── official_render.jpg  (optional)
```

Reference images are not used in the manual — they guide render generation and design decisions. See `Assets/ReferenceModels/README.md` for source and usage guidelines.

**0.5** Define the color scheme:
```bash
cp Templates/COLOR_SCHEME.yaml Projects/{ModelName}/color_scheme.yaml
```

Fill in all paint colors, their codes, finish types, and swatch hex values. This file is the source for the `paintScheme.colors` array in PROJECT.yaml and for C003, C010, and C011 component data.

**Decision point:**

```
Is PROJECT.yaml complete?
├── YES → Proceed to Phase 1
└── NO  → Return to 0.3 and complete all required fields
```

---

## Phase 1: Render Generation

**Goal:** Produce all render images required by the page specifications. Renders must be approved before any manual page is generated.

### Steps

**1.1** Identify required renders from PAGE_SYSTEM.md.

For a standard 10-page manual, the required renders are:
- Cover render (P001): 1 image
- Three-view renders (P002): 3 images (front, side, top)
- Optional in-progress renders (P005): 0–3 images
- Masking diagram render (P006): 1–2 images
- Detail renders (P007): 1 per detail element
- Decal placement renders (P008): 1–2 images

**1.2** Generate each render using the AI prompt templates in `Core/RENDER_GUIDE.md` §6.

Before submitting a render prompt:
- Insert the values from PROJECT.yaml into the template tokens
- Specify the correct angle per `RENDER_GUIDE.md` §2
- Specify the correct lighting rig (choose one rig for the entire manual)
- Specify the minimum resolution from `RENDER_GUIDE.md` §5

**1.3** Review each render against the quality checklist in `Core/RENDER_GUIDE.md` §7.

**Decision point per render:**
```
Does render pass RENDER_GUIDE.md §7 checklist?
├── YES → Save to Projects/{ModelName}/Images/ with correct name
└── NO  → Identify the failure, adjust prompt, regenerate
```

> ⚠️ **Warning:** Do not accept a render that fails the quality checklist with the intention of "fixing it later." Approved renders are the foundation of every page. A defective render causes multiple QA failures downstream.

**1.4** Update PROJECT.yaml render paths:
```yaml
renders:
  cover: "Images/cover_v1.png"
  colorFront: "Images/colorscheme_front_v1.png"
  colorSide: "Images/colorscheme_side_v1.png"
  colorTop: "Images/colorscheme_top_v1.png"
```

**Decision point:**
```
Are all required renders in Images/ and referenced in PROJECT.yaml?
├── YES → Proceed to Phase 2
└── NO  → Return to 1.2
```

---

## Phase 2: Manual Generation

**Goal:** Generate all 10 manual pages using the PromptEngine/ prompts and the PROJECT.yaml data.

### Steps

**2.1** For each page P001–P010, open the corresponding prompt file:
```
PromptEngine/Cover.md         (for P001)
PromptEngine/ColorScheme.md   (for P002)
PromptEngine/Materials.md     (for P003)
PromptEngine/Preparation.md   (for P004)
PromptEngine/Painting.md      (for P005)
PromptEngine/Masking.md       (for P006)
PromptEngine/Details.md       (for P007)
PromptEngine/Decals.md        (for P008)
PromptEngine/FinalChecklist.md (for P010)
```
If P009 is included: `PromptEngine/Premium.md`

**2.2** Inject PROJECT.yaml data into `{{project.X}}` tokens.

Replace each `{{project.X}}` token with the corresponding value from PROJECT.yaml. Replace each `{{token.X}}` with the corresponding value from `Assets/DesignSystem/Tokens/tokens.example.yaml`.

> 📝 **Note:** Manual token injection is the current process. A future CLI tool (see ROADMAP.md) will automate this. For now, search and replace each `{{token.X}}` and `{{project.X}}` in the prompt text before submitting to the AI.

**2.3** Submit the filled prompt to your chosen AI model.

The SDK is AI-model-agnostic. Any capable text-generation AI may be used. The prompt has been designed to produce consistent output regardless of which model processes it.

**2.4** Review the raw output.

Does the output match the page specification in PAGE_SYSTEM.md?
- If the AI produced a textual description of the page, use it as a specification for layout in your design tool (Affinity Publisher, InDesign, Scribus)
- If the AI produced image output directly, review against the QA_SYSTEM.md checklist for that page

**2.5** Save raw output:
```
Projects/{ModelName}/Output/raw/P001_raw.{ext}
Projects/{ModelName}/Output/raw/P002_raw.{ext}
...
```

**2.6** Produce the final page file.

Using the AI output as content and the component specs as layout guidelines, produce the final page file (PNG, PDF, or source file). Save to:
```
Projects/{ModelName}/Output/approved/P001.png
```

Wait to move to `approved/` until individual page QA passes.

**Decision point per page:**
```
Does page output satisfy the page-level Definition of Done (DEFINITION_OF_DONE.md §2)?
├── YES → Save to Output/approved/
└── NO  → Identify failure, revise, regenerate
```

---

## Phase 3: QA

**Goal:** Verify that all 10 pages, combined as a manual, satisfy the full QA_SYSTEM.md checklist.

### Steps

**3.1** Open a new `Projects/{ModelName}/Notes/qa_log.md` file:
```markdown
# QA Log — {ModelName}

Date: {date}
Reviewer: {name} (must be different from the contributor who generated the manual)
SDK Version: 2.4.0
Manual Version: {{project.manualVersion}}

## Results

QA-001: PASS
QA-002: PASS
...
```

**3.2** Work through all 110 QA items in `Core/QA_SYSTEM.md`. Record each result.

**3.3** For every FAIL:
- Document the specific failure in qa_log.md (what is wrong, where it appears)
- Return to the appropriate phase:
  - Render failure → Return to Phase 1, step 1.2
  - Page content failure → Return to Phase 2, step 2.2
  - Layout failure → Return to Phase 2, step 2.6 (layout revision)
  - PDF metadata failure → Correct in PDF_CONFIG.yaml and re-export

**Decision point:**
```
All 110 QA items PASS?
├── YES → Proceed to Phase 4
└── NO  → Fix failures and re-run affected QA items (re-run entire QA if 5+ items fail)
```

> 📝 **Note:** If 5 or more QA items fail, re-run the entire checklist after fixing them. Fixes sometimes introduce new failures.

---

## Phase 4: Approval and Publication

**Goal:** Move the manual to Approved status and produce the final PDF deliverable.

### Steps

**4.1** Move approved pages to the canonical location:
```bash
mkdir -p Assets/ApprovedManual/{ModelName}
cp Projects/{ModelName}/Output/approved/*.png Assets/ApprovedManual/{ModelName}/
```

**4.2** Configure PDF export:
```bash
cp Templates/PDF_CONFIG.yaml Assets/ApprovedManual/{ModelName}/pdf_config.yaml
```

Edit `pdf_config.yaml` with the project-specific metadata from PROJECT.yaml.

**4.3** Export PDF — screen variant:
Using the export tool of your choice (see PDF_MASTER.md §9):
```
Output: Assets/ApprovedManual/{ModelName}/{model-slug}_manual_screen_v1.pdf
Standard: PDF/A-2b
Color space: sRGB
```

**4.4** Export PDF — print variant:
```
Output: Assets/ApprovedManual/{ModelName}/{model-slug}_manual_print_v1.pdf
Standard: PDF/X-4
Color space: CMYK FOGRA39
Bleed: 3mm
```

**4.5** Run final PDF QA (QA-096 to QA-100).

**4.6** Update `Assets/ApprovedManual/README.md`:
Add an entry for the new manual:
```markdown
| {ModelName} | {PaintSchemeName} | {manualVersion} | {date} |
```

**4.7** Notify the project maintainer for final approval.

Only a project maintainer can grant Approved status. Self-approval is not permitted.

---

## Quick Reference Decision Flowchart

```
START
  │
  ▼
PROJECT.yaml complete? ── NO ──→ Complete all required fields
  │ YES
  ▼
All renders approved? ──── NO ──→ Regenerate failing renders
  │ YES
  ▼
All 10 pages generated? ── NO ──→ Generate missing pages
  │ YES
  ▼
All 110 QA items PASS? ─── NO ──→ Fix failures, re-QA
  │ YES
  ▼
PDF exported (both variants)? ─ NO ──→ Export PDFs
  │ YES
  ▼
Files in ApprovedManual/? ─── NO ──→ Move files
  │ YES
  ▼
Maintainer approved? ────── NO ──→ Request review
  │ YES
  ▼
DONE — Manual is Published
```
