# Assets/

> **A cosa serve questa cartella:** design system (token, componenti, palette), riferimenti dei progetti SDK e manuali pubblicati.
> **Chi la modifica:** Developer (DesignSystem), Maintainer (ReferenceModels, ApprovedManual).
> **Quando:** release SDK e pubblicazione manuali. **L'Operatore non ci crea nulla:** le sue immagini vanno in `Projects/{Modello}/Images/`.

**Version:** 2.1.0
**Maintainer:** Mini4WD Manual SDK Core Team
**Depends on:** Core/STYLE_GUIDE.md, Core/NAMING_CONVENTION.md, Core/RENDER_GUIDE.md

---

## Purpose

`Assets/` is the concrete layer of the SDK. While `Core/` defines abstract specifications, `Assets/` contains the actual implementations: design token files, component wireframes, reference photography, and approved manual outputs.

Everything a practitioner needs to produce a manual — that is not a written specification — lives here.

---

## Directory Structure

```
Assets/
├── DesignSystem/          # Concrete design system implementation
│   ├── Tokens/            # Design token YAML files (single source of visual truth)
│   ├── Components/        # Wireframe specs and dimension tables for C001–C015
│   ├── Palette/           # Color swatch documentation and usage rules
│   ├── Typography/        # Font specimens, fallback stacks, licensing
│   ├── Icons/             # SVG icon library (v2.2.0+)
│   └── Layout/            # Grid diagrams and layout pattern reference
├── ReferenceModels/       # Source photography per Mini4WD model
│   └── {ModelName}/       # One subfolder per model
├── ApprovedManual/        # QA-approved final page outputs (READ-ONLY in production)
│   └── {ModelName}/       # One subfolder per approved model
└── Examples/              # SDK-maintained page output samples for visual reference
```

---

## What Belongs Here vs Core/

| Question | Core/ | Assets/ |
|----------|-------|---------|
| What color should the header be? | Yes — STYLE_GUIDE.md defines it | No |
| What hex value does TamiyaPrimary resolve to? | No | Yes — tokens.example.yaml |
| What size should the footer be? | Yes — COMPONENT_SYSTEM.md | No |
| What does a completed P002 page look like? | No | Yes — Examples/ |
| Where is the reference photo for Proto Emperor? | No | Yes — ReferenceModels/ |
| What is the render resolution for covers? | Yes — RENDER_GUIDE.md §5 | Repeated in tokens for tooling |

**Rule:** If a value can change between projects (a color shade, a font size override), it is in `Assets/`. If it is a permanent architectural decision, it is in `Core/`.

---

## File Size Guidelines

| Asset Type | Maximum Size | Format |
|------------|-------------|--------|
| Cover render | 10 MB | PNG, sRGB |
| Body page render | 5 MB | PNG, sRGB |
| Detail render | 2 MB | PNG, sRGB |
| Icon | 100 KB | SVG |
| Reference photo | 8 MB | JPG, sRGB |
| Design token file | 100 KB | YAML |
| PDF (screen) | 30 MB | PDF/A-2b |
| PDF (print) | 80 MB | PDF/X-4 |

If a file exceeds these limits, optimize before committing. Use [Squoosh](https://squoosh.app/) for images or `svgo` for SVG files.

---

## Naming Conventions

All file names follow `Core/NAMING_CONVENTION.md`. Summary:

- Render images: `{modelSlug}_{pageId}_{variant}_{version}.png`
  - Example: `proto-emperor_P002_colorscheme-front_v1.png`
- Reference photos: `reference_{angle}.jpg` (within model subfolder)
  - Example: `reference_front.jpg`
- Token files: `tokens.{variant}.yaml`
  - Example: `tokens.example.yaml`, `tokens.dark-theme.yaml`

---

## Asset Versioning

When iterating on an asset without replacing it:

1. Keep the original file: `proto-emperor_P002_v1.png`
2. Create the new version: `proto-emperor_P002_v2.png`
3. Update `PROJECT.yaml` to reference the new version
4. Do not delete v1 until the manual is in `ApprovedManual/` state

---

## Git LFS

This repository recommends [Git Large File Storage](https://git-lfs.com/) for binary assets. Configure your `.gitattributes` with:

```
*.png filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
```

YAML, Markdown, and SVG files do NOT require LFS and must be tracked normally.

---

## Deletion Policy

- **ReferenceModels/**: Files may be updated or replaced freely during the production phase.
- **DesignSystem/**: Changes must be synchronized with `Core/STYLE_GUIDE.md`. Never change a token value without a corresponding ADR in `STYLE_DECISIONS.md`.
- **ApprovedManual/**: Files here are **never deleted**. Superseded versions get a `_v2`, `_v3` suffix. Deletion requires a written decision by a project maintainer, logged in the project's `Notes/` directory.
- **Examples/**: Managed by SDK maintainers only. Do not modify.

---

## Dependencies

- `Core/STYLE_GUIDE.md` — authoritative specification that `Assets/DesignSystem/` implements
- `Core/NAMING_CONVENTION.md` — all file names in `Assets/` must comply
- `Core/RENDER_GUIDE.md` — specifies what goes in `ReferenceModels/` and what quality standards apply
- `Core/QA_SYSTEM.md` — defines when assets may enter `ApprovedManual/`
- `Templates/PROJECT.yaml` — references asset paths from `Projects/{ModelName}/Images/`

---

## Related Directories

- `Core/` — abstract specifications this directory implements
- `Projects/` — working directory; assets migrate here when approved
- `Templates/` — structured data files that reference asset paths
