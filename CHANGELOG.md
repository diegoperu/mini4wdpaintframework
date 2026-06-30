# Changelog

All notable changes to Mini4WD Manual SDK are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Multi-language support (Italian, Japanese, English)
- SVG icon library for C006 Callout and C008 Warning components
- Automated PDF pipeline via pandoc + LaTeX

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
