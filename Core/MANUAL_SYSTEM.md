# Manual System

This document describes the architecture of a Mini4WD Manual — how all parts of the SDK combine to produce a finished document — and the lifecycle of a manual from initial setup to final approved PDF.

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Mini4WD Manual SDK                       │
├──────────────┬──────────────────┬────────────┬─────────────┤
│   Core/      │  PromptEngine/   │ Templates/ │   Assets/   │
│  (specs)     │   (prompts)      │(templates) │(design sys) │
└──────┬───────┴────────┬─────────┴─────┬──────┴──────┬──────┘
       │                │               │             │
       │   ┌────────────┘               │             │
       │   │  ┌─────────────────────────┘             │
       │   │  │  ┌────────────────────────────────────┘
       │   │  │  │
       ▼   ▼  ▼  ▼
  ┌─────────────────────────┐
  │     Projects/MyModel/   │
  │      PROJECT.yaml       │  ← Data source for all pages
  └──────────┬──────────────┘
             │
             │  Token injection
             ▼
  ┌─────────────────────────┐
  │    PromptEngine/        │
  │  Filled prompts (×10)   │  ← AI-ready prompt per page
  └──────────┬──────────────┘
             │
             │  AI generation
             ▼
  ┌─────────────────────────┐
  │   Projects/MyModel/     │
  │    Output/raw/ (×10)    │  ← Raw AI output
  └──────────┬──────────────┘
             │
             │  QA review
             ▼
  ┌─────────────────────────┐
  │    Core/QA_SYSTEM.md    │
  │   (110-item checklist)  │
  └──────────┬──────────────┘
             │
             │  Pass all checks
             ▼
  ┌─────────────────────────┐
  │ Assets/ApprovedManual/  │
  │   MyModel/P001–P010     │  ← Approved page files
  └──────────┬──────────────┘
             │
             │  PDF export
             ▼
  ┌─────────────────────────┐
  │ Assets/ApprovedManual/  │
  │   MyModel/manual.pdf    │  ← Final deliverable
  └─────────────────────────┘
```

---

## 2. Manual Lifecycle

A manual passes through four states. State transitions require explicit action.

### State 1: Draft

- `Projects/{ModelName}/PROJECT.yaml` has been created and populated
- Reference images are present in `Assets/ReferenceModels/{ModelName}/`
- At least one page has been generated but QA is not complete
- Files live in `Projects/{ModelName}/Output/raw/`

**Who can create a Draft:** Any contributor.

### State 2: Review

- All 10 pages (P001–P010) have been generated
- The contributor has performed a self-review against `Core/QA_SYSTEM.md`
- Failures have been documented in `Projects/{ModelName}/Notes/qa_log.md`
- Corrected pages replace raw outputs; the qa_log records what changed

**Who can advance to Review:** The original contributor, by completing self-QA.

### State 3: QA Pass

- All 110 QA items in `Core/QA_SYSTEM.md` return PASS
- The `qa_log.md` is complete and shows no open failures
- PDF has been exported in both screen and print variants

**Who verifies QA Pass:** A second contributor or the project maintainer (not the original contributor).

### State 4: Approved

- Manual files have been moved to `Assets/ApprovedManual/{ModelName}/`
- The PDF is present at `Assets/ApprovedManual/{ModelName}/manual.pdf`
- An entry has been added to `Assets/ApprovedManual/README.md`

**Who approves:** Project maintainer only.

---

## 3. File Naming Convention for Outputs

All output files follow the pattern defined in `Core/NAMING_CONVENTION.md`. Summary:

```
{model-slug}_{page-id}_{descriptor}_{version}.{ext}
```

Examples:
```
proto-emperor_P001_cover_v1.png
proto-emperor_P002_colorscheme_v2.png
proto-emperor_manual_v1.pdf
proto-emperor_manual_print_v1.pdf
```

The `model-slug` is the model name in kebab-case (lowercase, hyphens, no special characters). See `Core/NAMING_CONVENTION.md` for the full derivation rule.

---

## 4. Folder Structure per Project

```
Projects/
└── Proto_Emperor/                    ← PascalCase, matches official Tamiya name
    ├── PROJECT.yaml                  ← Project configuration (required)
    ├── README.md                     ← Project brief for human readers
    ├── Images/                       ← Approved renders for this project
    │   ├── cover_v1.png
    │   ├── colorscheme_front_v1.png
    │   ├── colorscheme_side_v1.png
    │   └── ...
    ├── Output/                       ← Generated page files
    │   ├── raw/                      ← AI output before QA
    │   │   ├── P001_raw.png
    │   │   └── ...
    │   └── approved/                 ← Pages that have passed individual QA
    │       ├── P001.png
    │       └── ...
    └── Notes/                        ← Free-form notes and QA log
        ├── qa_log.md                 ← Required: documents every QA session
        └── decisions.md              ← Optional: design choices for this project
```

---

## 5. How PROJECT.yaml Drives the Manual

`PROJECT.yaml` is the single source of truth for all project-specific data. It provides the values injected into `{{project.X}}` tokens in `PromptEngine/` prompts.

A minimal PROJECT.yaml includes:

```yaml
sdkVersion: "2.1.0"
modelName: "Proto Emperor"
modelSlug: "proto-emperor"
series: "Super-II Chassis"
manufacturer: "Tamiya"

paintScheme:
  name: "Midnight Violet"
  style: "metallic"
  primaryColor: "Metallic Violet"
  secondaryColor: "Chrome Silver"
  accentColor: "Flat Black"

renders:
  cover: "Images/cover_v1.png"
  colorFront: "Images/colorscheme_front_v1.png"
  colorSide: "Images/colorscheme_side_v1.png"
  colorTop: "Images/colorscheme_top_v1.png"

author: "Contributor Name"
createdDate: "2024-01-20"
manualVersion: "1.0.0"
```

The full schema is documented in `Templates/PROJECT.yaml`. All fields marked `required: true` in the schema must be present and non-empty for a manual to pass QA.

---

## 6. Template Inheritance

All projects start from `Templates/PROJECT.yaml`. This template defines the schema and provides documentation for every field via inline comments. Projects do not "inherit" from the template at runtime — they copy it and fill it in.

The SDK does not support template inheritance at the project level (e.g., defining a "base" project that other projects extend). Each project is a complete, self-contained `PROJECT.yaml`. This design decision was made to keep project files simple, auditable, and independent.

If a future version introduces a common field (e.g., `photographerCredit`), it will be added to the template with a migration guide in `CHANGELOG.md`.

---

## 7. Version Management per Manual

Each manual has its own `manualVersion` field in `PROJECT.yaml`, independent of the SDK version. Manual versioning follows SemVer:

- **MAJOR:** Complete repaint scheme change (different colors, different style)
- **MINOR:** Additional pages added, or significant render updates
- **PATCH:** Typo corrections, color code fixes, layout adjustments

The SDK version at the time of creation is recorded in `sdkVersion`. This allows future maintainers to understand which SDK capabilities were available when the manual was created.

When an SDK MAJOR version changes, existing manuals are not automatically invalidated. They continue to reference the SDK version under which they were created. Migration to a new SDK MAJOR is optional and documented in `Docs/migration/`.

---

## 8. Archive and Publication Policy

### Archive (Assets/ApprovedManual/)
All approved manuals live in `Assets/ApprovedManual/`. This directory is the permanent record of the SDK's output. Approved manuals are never deleted — only superseded by a new manual version.

When a new version of a manual is approved:
1. The old version moves to `Assets/ApprovedManual/{ModelName}/archive/v{N}/`
2. The new version replaces the top-level files
3. The `Assets/ApprovedManual/README.md` is updated with the new version number

### Publication
Publication means making the PDF available to the public (community website, README link, GitHub release). Publication requires Approved status. A Draft or Review-state manual must never be published.

Publication is not managed by the SDK — it is managed by the project that uses the SDK. The SDK's role ends at the Approved state.
