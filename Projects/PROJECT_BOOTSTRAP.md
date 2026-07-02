# PROJECT_BOOTSTRAP.md
# Mini4WD Manual SDK — New Project Guide

**Version:** 2.4.0
**Entry point:** `BOOTSTRAP.md`

> This document guides you through creating a new Mini4WD manual project
> from scratch. Read `BOOTSTRAP.md` and `SDK_CONTEXT.yaml` before this document.

---

## Prerequisites

Before starting, ensure you have:

- [ ] The Mini4WD Manual SDK (this repository)
- [ ] The official Tamiya model name (exact spelling)
- [ ] Tamiya paint codes for the intended color scheme
- [ ] Reference photography of the physical model (multiple angles)
- [ ] An AI model with sufficient context window (recommended: 100K+ tokens)

---

## Step 1 — Create the Project Folder

```bash
mkdir -p Projects/{ModelName}/Images
mkdir -p Projects/{ModelName}/Output
mkdir -p Projects/{ModelName}/Notes
```

Replace `{ModelName}` with the model name using underscores (e.g., `Proto_Emperor`).

**Naming rules (`Core/NAMING_CONVENTION.md`):**
- Use the official Tamiya model name
- Replace spaces with underscores
- No special characters, no lowercase-only names
- Examples: `Proto_Emperor`, `Avante_Mk3`, `Dash_001_Shadow`

---

## Step 2 — Create PROJECT.yaml

Copy the template and fill in your model data:

```bash
cp Templates/PROJECT.yaml Projects/{ModelName}/PROJECT.yaml
```

Open `Projects/{ModelName}/PROJECT.yaml` and fill in every field:

```yaml
project:
  modelName: "Proto Emperor"          # Official Tamiya name, exactly as printed
  modelSlug: "proto-emperor"          # kebab-case, used for file naming
  seriesName: "Super II"              # Chassis series
  year: "2024"                        # Production year of this manual (string, not integer)
  language: "it"
  version: "1.0.0"

paintScheme:
  name: "Midnight Violet"
  colors:
    - id: "PC001"                     # Paint-color ID — never reuse the C00N pattern (that's the Component ID registry, see COMPONENT_SYSTEM.md)
      paintBrand: "Tamiya"
      paintCode: "PS-18"
      paintName: "Metallic Purple"
      finish: "metallic"
    - id: "PC002"
      paintBrand: "Tamiya"
      paintCode: "PS-1"
      paintName: "White"
      finish: "gloss"
  # Add all colors in the scheme

paths:
  coverRenderPath: "Images/cover_3q_front.jpg"
  colorSchemeRenderFront: "Images/P002_front.png"
  colorSchemeRenderSide: "Images/P002_side.png"
  colorSchemeRenderTop: "Images/P002_top.png"
```

Reference images live in `Assets/ReferenceModels/{ModelName}/`, not in `PROJECT.yaml` (see `Build/Pipeline.md` Phase 1).

**Rules:**
- Every color must have a Tamiya/manufacturer `paintCode` — no invented codes
- All file paths are relative to the project folder
- Use `TODO:` for any unknown values — never invent data
- Every field in `Templates/PROJECT.yaml` has a comment explaining it

Reference: `Projects/Proto_Emperor/PROJECT.yaml`

---

## Step 3 — Prepare Reference Images

Place your reference photography in `Projects/{ModelName}/Images/`:

| File | Content | Required |
|------|---------|----------|
| `ref_front.jpg` | Front view, white background | Yes |
| `ref_side_left.jpg` | Left side view | Yes |
| `ref_side_right.jpg` | Right side view | Yes |
| `ref_top.jpg` | Top-down view | Yes |
| `ref_rear.jpg` | Rear view | Recommended |
| `ref_3q_front.jpg` | 3/4 front-left view | Yes (for cover) |
| `ref_detail_*.jpg` | Close-ups of key details | As needed |

**Image requirements (`Config/render.yaml`):**
- Minimum resolution: 2048px on the long edge
- White or neutral background preferred
- Sharp focus, no motion blur
- Multiple lighting conditions if available

---

## Step 4 — Initialize ApprovedAssets

The CMS layer for your project is at `ApprovedAssets/Text/`. Each page module
is pre-created by the SDK. Check the current state:

```bash
cat ApprovedAssets/index.yaml
```

All pages start in `draft` status. You will advance each page through the
lifecycle as you generate and validate content.

---

## Step 5 — Load the SDK Context (AI Session)

Open your AI session and use the prompt from `Docs/AI_BOOTSTRAP_PROMPT.md`.

**Recommended: Prompt A (Full Session Bootstrap)**

Attach files in this order:
1. `SDK_CONTEXT.yaml`
2. `BOOTSTRAP.md`
3. `Core/AI_OPERATING_RULES.md`
4. `Config/LANGUAGE_POLICY.yaml`
5. `Core/TEXT_ENGINE.md`
6. `Core/DESIGN_LANGUAGE.md`
7. `Core/STYLE_GUIDE.md`
8. `Core/COMPONENT_SYSTEM.md`
9. `Core/PAGE_SYSTEM.md`
10. `Projects/{ModelName}/PROJECT.yaml`
11. Reference images

---

## Step 6 — Generate Pages (P001–P010)

Generate one page at a time. For each page:

### 6a — Text Engine (Phase 2a)
Attach `PromptEngine/{page}.md` and use Prompt B from `Docs/AI_BOOTSTRAP_PROMPT.md`.

Output: `ApprovedAssets/Text/P00x/content.yaml`

### 6b — Content QA (Phase 2b)
Attach `Tests/ContentValidation.md` and validate the content.yaml.
Fix all FAIL results before proceeding.

### 6c — Text QA (Phase 2c)
Attach `Tests/TextValidation.md` and validate Italian compliance.
Zero tolerance for non-Italian text or Lorem ipsum.

### 6d — Seal the Page (Phase 2d)
Update `ApprovedAssets/Text/P00x/metadata.yaml`:
```yaml
lifecycle:
  status: "locked"
  locked_at: "2026-07-01"
  locked_by: "AI model name + session"
```

### 6e — Render (Phase 3)
Use Prompt D from `Docs/AI_BOOTSTRAP_PROMPT.md`.
Input: locked `content.yaml` + reference images.
Output: illustrated page image.

### 6f — Visual QA (Phase 4)
Validate the render against `Core/QA_SYSTEM.md`.
Check all relevant items in the 110-item checklist.

---

## Step 7 — Assemble PDF (Phase 5)

Once all 10 pages pass QA:

1. Verify all pages are in `rendered` lifecycle status
2. Use `Templates/PDF_CONFIG.yaml` for export settings
3. Follow `Core/PDF_MASTER.md` for the full export specification
4. Generate three variants: screen, print, archive

Output: `Assets/ApprovedManual/{ModelName}/{ModelName}_Manual.pdf`

---

## Step 8 — Release (Phase 7)

1. Move all pages to `released` status in `metadata.yaml`
2. Update `ApprovedAssets/index.yaml` with final states
3. Archive source files per `Core/PDF_MASTER.md` §Archive

---

## Project Checklist

Use this checklist to track progress:

```
PROJECT SETUP
[ ] Project folder created: Projects/{ModelName}/
[ ] PROJECT.yaml filled — no TODO: fields (or all TODOs documented)
[ ] Reference images loaded (minimum 4 angles)
[ ] AI session bootstrapped with full LOAD sequence

PAGE GENERATION (repeat for each page)
[ ] P001 Copertina — content.yaml generated
[ ] P001 — ContentValidation: PASS
[ ] P001 — TextValidation: PASS
[ ] P001 — metadata: locked
[ ] P001 — render generated
[ ] P001 — QA_SYSTEM: PASS
[ ] P002 ... (repeat)
[ ] P003 ...
[ ] P004 ...
[ ] P005 ...
[ ] P006 ...
[ ] P007 ...
[ ] P008 ...
[ ] P009 ...
[ ] P010 ...

ASSEMBLY
[ ] All 10 pages in rendered status
[ ] PDF screen variant generated
[ ] PDF print variant generated
[ ] PDF archive variant generated
[ ] ApprovedAssets/index.yaml updated to released
```

---

## Reference Project

The `Projects/Proto_Emperor/` folder is the reference project for this SDK.
Use it as a structural guide for folder layout and PROJECT.yaml format.

Do not modify the Proto_Emperor project — it is a read-only reference.

---

## Cross References

- `BOOTSTRAP.md` → non-negotiable rules and pipeline overview
- `SDK_CONTEXT.yaml` → SDK identity and pipeline summary
- `Docs/LOAD_ORDER.md` → exact context loading order
- `Docs/AI_BOOTSTRAP_PROMPT.md` → ready-to-use prompts for ChatGPT, Claude, Gemini
- `Templates/PROJECT.yaml` → project configuration template
- `Core/WORKFLOW.md` → detailed workflow documentation
- `Build/Pipeline.md` → full 8-phase pipeline specification
- `Core/QA_SYSTEM.md` → 110-item quality checklist
