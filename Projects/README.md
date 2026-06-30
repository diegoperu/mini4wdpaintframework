# Projects

## Purpose

Every Mini4WD model that has a painting manual lives in its own subdirectory here. The `Projects/` directory is the workspace — it contains in-progress and active project files. Approved, published manuals are **moved** (not copied) to `Assets/ApprovedManual/` when QA passes.

---

## Responsibilities

- Contain one subdirectory per Mini4WD model
- Provide a clean, isolated workspace per project
- Track project status from Draft through Approved
- Store raw AI outputs, reference images, QA logs, and notes
- Never contain final approved manuals (those belong in `Assets/ApprovedManual/`)

## What to Put Here

- Project directories, each named after the model
- Project configuration files (`PROJECT.yaml`, `PROJECT.md`, etc.)
- Render images (`Images/`)
- Raw AI-generated page outputs (`Output/raw/`)
- QA logs and notes (`Notes/`)

## What NOT to Put Here

- Final approved PDF files (belong in `Assets/ApprovedManual/`)
- Design system assets (belong in `Assets/DesignSystem/`)
- Reference photography (belongs in `Assets/ReferenceModels/`)
- Template master files (belong in `Templates/`)

---

## Project Naming Convention

The project folder name must follow these rules:

1. Use the **official Tamiya model name**, exactly as it appears in official documentation
2. Replace spaces with underscores: `Proto Emperor` → `Proto_Emperor`
3. Preserve capitalization: `Dash_0_Hawk` not `dash_0_hawk`
4. Never abbreviate: `Proto_Emperor` not `PrtEmpr`
5. The `modelSlug` in `PROJECT.yaml` is the lowercase, hyphenated version: `proto-emperor`

| Model Name | Folder Name | modelSlug |
|-----------|-------------|-----------|
| Proto Emperor | `Proto_Emperor/` | `proto-emperor` |
| Dash 0 Hawk | `Dash_0_Hawk/` | `dash-0-hawk` |
| Avante Mk.III | `Avante_MkIII/` | `avante-mkiii` |
| Wild Mini 4WD | `Wild_Mini_4WD/` | `wild-mini-4wd` |

---

## Project Folder Structure

Every project folder must contain this exact structure:

```
Projects/{ModelName}/
├── PROJECT.yaml          # Main configuration (from Templates/PROJECT.yaml)
├── PROJECT.md            # Human-readable brief (from Templates/PROJECT.md)
├── CHECKLIST.md          # Progress tracker (from Templates/CHECKLIST.md)
├── COLOR_SCHEME.yaml     # Color definitions (from Templates/COLOR_SCHEME.yaml)
├── PDF_CONFIG.yaml       # PDF export config (from Templates/PDF_CONFIG.yaml)
├── README.md             # Project-specific README
├── Images/               # All render images for this project
│   ├── cover_3q.png      # Cover render: 3/4 front-left, min 2480x3508px
│   ├── P002_front.png    # Color scheme: orthographic front view
│   ├── P002_side.png     # Color scheme: orthographic side view
│   ├── P002_top.png      # Color scheme: orthographic top view
│   └── ...               # Additional renders as needed
├── Output/               # All generated outputs
│   ├── raw/              # Raw AI outputs (unprocessed)
│   │   ├── P001_raw.md
│   │   ├── P002_raw.md
│   │   └── ...
│   └── pdf/              # Exported PDFs (before approval)
│       ├── {slug}_manual_screen.pdf
│       ├── {slug}_manual_print.pdf
│       └── {slug}_manual_archive.pdf
└── Notes/                # QA logs, decisions, free notes
    ├── qa_log.md         # QA checklist results
    └── ...               # Any additional notes
```

---

## Project Lifecycle

```
Templates/
    │
    ▼ (copy files)
Projects/{ModelName}/  ◄── ACTIVE WORKSPACE
    │
    ├── Phase 0: Setup (fill PROJECT.yaml)
    │
    ├── Phase 1: Render generation
    │
    ├── Phase 2: Page generation (PromptEngine)
    │
    ├── Phase 3: QA (Core/QA_SYSTEM.md)
    │
    ▼ (move on approval)
Assets/ApprovedManual/{ModelName}/  ◄── APPROVED MANUAL
```

**Status values** (tracked in `PROJECT.yaml` → `qa.status`):

| Status | Meaning |
|--------|---------|
| `draft` | Active development, not yet reviewed |
| `in-review` | Under QA review, changes may be requested |
| `approved` | QA passed, ready for publication |
| `archived` | Published and no longer in active development |

---

## Starting a New Project

```bash
# 1. Create the project folder
MODEL="Your_Model_Name"
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw"
mkdir -p "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"

# 2. Copy all templates
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
cp Templates/PROJECT.md "Projects/${MODEL}/PROJECT.md"
cp Templates/CHECKLIST.md "Projects/${MODEL}/CHECKLIST.md"
cp Templates/COLOR_SCHEME.yaml "Projects/${MODEL}/COLOR_SCHEME.yaml"
cp Templates/PDF_CONFIG.yaml "Projects/${MODEL}/PDF_CONFIG.yaml"

# 3. Create README
cp Projects/Proto_Emperor/README.md "Projects/${MODEL}/README.md"
# Then edit the README for your model

# 4. Fill in PROJECT.yaml — this is the most important step
```

See `Core/WORKFLOW.md` for the complete generation pipeline.

---

## Versioning Rendered Images

Do **not** commit large render images to version control without review. Recommended practice:

- Add `Projects/*/Images/*.png` and `Projects/*/Images/*.jpg` to `.gitignore`
- Track renders in a separate storage system (cloud storage, LFS)
- Only commit image files after QA approval

---

## Archiving Projects

When a manual is complete and published:

1. Move approved files to `Assets/ApprovedManual/{ModelName}/`
2. Set `qa.status: archived` in `PROJECT.yaml`
3. Keep `Projects/{ModelName}/` with raw outputs for reference
4. The project directory is never deleted — it is the record of how the manual was made

---

## Dependencies

| Document | Role |
|----------|------|
| `Templates/` | Source of all configuration templates |
| `PromptEngine/` | Prompts for generating each page |
| `Assets/ApprovedManual/` | Final destination for approved manuals |
| `Core/WORKFLOW.md` | Complete step-by-step pipeline |
| `Core/NAMING_CONVENTION.md` | Folder and file naming rules |
| `Core/QA_SYSTEM.md` | QA checklist used in Phase 3 |

---

## Current Projects

| Model | Status | Scheme | Updated |
|-------|--------|--------|---------|
| [Proto Emperor](Proto_Emperor/) | Example | Violet Phantom | 2024-01-15 |

---

*Projects/ is part of Mini4WD Manual SDK v2.1.0. See `Core/WORKFLOW.md` for the complete pipeline.*
