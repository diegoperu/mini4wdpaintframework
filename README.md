# Mini4WD Manual SDK

**Version 2.1.0** | Apache 2.0 | Open Source

---

## Mission

Mini4WD Manual SDK is an open-source framework that enables any AI model to generate professional illustrated painting manuals for Tamiya Mini4WD models, maintaining consistent editorial and graphic standards across hundreds of projects.

The SDK provides the specification layer, component system, prompt engine, and design tokens required to produce manuals that are visually coherent, technically accurate, and immediately recognizable — regardless of which AI model, tool, or contributor generated them.

---

## Design Philosophy

This framework draws inspiration from Tamiya's technical catalogs and instruction sheets of the 1990s: clean white backgrounds, precise callout boxes, numbered steps, and a sense of craft that communicated both information and enthusiasm. That foundation is reinterpreted with modern graphic design sensibilities — structured grid systems, a systematic color palette anchored in violet, typographic hierarchy, and render-quality illustrations.

The result is a manual system that feels timeless without feeling dated. Every page should look like it was designed by the same studio, whether it was produced in 2024 or 2034.

---

## Quick Start

**Step 1 — Obtain the SDK**
```bash
git clone https://github.com/your-org/mini4wd-manual-sdk.git
cd mini4wd-manual-sdk
```

**Step 2 — Open the project template**
```bash
cp Templates/PROJECT.yaml Projects/MyModel/PROJECT.yaml
```

**Step 3 — Fill in your model data**

Edit `Projects/MyModel/PROJECT.yaml` with your model name, series, paint scheme, and render paths. All required fields are documented inside the file.

**Step 4 — Run the prompts**

For each page P001–P010, open the corresponding file in `PromptEngine/` and inject your PROJECT.yaml data into the `{{token}}` placeholders. Submit the completed prompt to any AI model (ChatGPT, Claude, Gemini, etc.).

**Step 5 — Export PDF**

Once all pages pass the QA checklist (`Core/QA_SYSTEM.md`), export using the configuration in `Templates/PDF_CONFIG.yaml`. See `Core/PDF_MASTER.md` for full export specification.

---

## Directory Structure

```
Mini4WD_Manual_SDK/
│
├── README.md                    ← You are here
├── CHANGELOG.md                 ← Version history
├── VERSION                      ← Current version (2.1.0)
├── LICENSE                      ← Apache 2.0
├── STYLE_DECISIONS.md           ← Architecture Decision Records (ADRs)
├── ROADMAP.md                   ← Planned features and future direction
│
├── Core/                        ← Authoritative specification layer
│   ├── README.md
│   ├── DESIGN_LANGUAGE.md       ← 50+ philosophical rules for the framework
│   ├── STYLE_GUIDE.md           ← Colors, typography, grid, spacing
│   ├── COLOR_SYSTEM.md          ← Full color palette and usage rules
│   ├── MANUAL_SYSTEM.md         ← Architecture overview and lifecycle
│   ├── PAGE_SYSTEM.md           ← P001–P010 specifications
│   ├── COMPONENT_SYSTEM.md      ← C001–C015 specifications
│   ├── RENDER_GUIDE.md          ← Rendering standards and AI prompt templates
│   ├── PDF_MASTER.md            ← Export specification
│   ├── QA_SYSTEM.md             ← 100+ quality checks
│   ├── WORKFLOW.md              ← End-to-end process documentation
│   ├── NAMING_CONVENTION.md     ← File and folder naming rules
│   ├── DOCUMENTATION_STYLE.md   ← How to write SDK documentation
│   └── DEFINITION_OF_DONE.md   ← Completion criteria
│
├── PromptEngine/                ← Page-specific AI prompts
│   ├── README.md
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
├── Templates/                   ← Starter files for new projects
│   ├── README.md
│   ├── PROJECT.yaml             ← Project configuration template
│   ├── PROJECT.md               ← Human-readable project brief template
│   ├── CHECKLIST.md             ← Per-project QA checklist
│   ├── COLOR_SCHEME.yaml        ← Paint scheme definition template
│   └── PDF_CONFIG.yaml          ← PDF export configuration
│
├── Projects/                    ← One subfolder per Mini4WD model
│   ├── README.md
│   └── ExampleModel/            ← Reference project (read-only example)
│       ├── PROJECT.yaml
│       ├── Images/
│       ├── Output/
│       ├── Notes/
│       └── README.md
│
├── Assets/                      ← Design system, references, approved output
│   ├── README.md
│   ├── DesignSystem/
│   │   ├── README.md
│   │   ├── Tokens/              ← Design tokens (YAML)
│   │   ├── Components/          ← Component wireframes and specs
│   │   ├── Palette/             ← Color swatch references
│   │   ├── Typography/          ← Font specimens and specimens
│   │   ├── Icons/               ← Icon library
│   │   └── Layout/              ← Grid and wireframe templates
│   ├── ReferenceModels/         ← Reference photography per model
│   ├── ApprovedManual/          ← Production-approved manual output
│   └── Examples/                ← Example pages for onboarding
│
└── Docs/                        ← Extended documentation and guides
    └── README.md
```

---

## Core Documentation

| Document | Purpose |
|---|---|
| [Core/DESIGN_LANGUAGE.md](Core/DESIGN_LANGUAGE.md) | Philosophical rules governing every design decision |
| [Core/STYLE_GUIDE.md](Core/STYLE_GUIDE.md) | Color, typography, grid, spacing specifications |
| [Core/PAGE_SYSTEM.md](Core/PAGE_SYSTEM.md) | Specification for pages P001–P010 |
| [Core/COMPONENT_SYSTEM.md](Core/COMPONENT_SYSTEM.md) | Specification for components C001–C015 |
| [Core/RENDER_GUIDE.md](Core/RENDER_GUIDE.md) | Illustration standards and AI render prompts |
| [Core/QA_SYSTEM.md](Core/QA_SYSTEM.md) | Quality assurance checklist (100+ items) |
| [Core/WORKFLOW.md](Core/WORKFLOW.md) | End-to-end production workflow |

---

## Versioning Policy

This project follows [Semantic Versioning 2.0.0](https://semver.org/).

- **MAJOR** version: breaking changes to page IDs, component IDs, token names, or PROJECT.yaml schema
- **MINOR** version: new pages, components, or tokens added in a backwards-compatible manner
- **PATCH** version: bug fixes, clarifications, typo corrections

Version is stored in `VERSION`. Every release is documented in `CHANGELOG.md`. Breaking changes include a migration guide in `Docs/migration/`.

---

## Contributing

Contributions are welcome. Before opening a pull request:

1. Read `Core/DOCUMENTATION_STYLE.md` to match the existing documentation voice
2. For any change to `Core/`, file an Architecture Decision Record in `STYLE_DECISIONS.md`
3. Update `CHANGELOG.md` under `[Unreleased]`
4. Ensure your changes pass the conceptual checklist in `Core/DEFINITION_OF_DONE.md` §3

Open issues and feature requests are tracked on GitHub. Tag feature requests with the `roadmap` label. See `ROADMAP.md` for what is already planned.

---

## License

Copyright 2024 Mini4WD Manual SDK Contributors.

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full terms.

---

*Mini4WD Manual SDK is not affiliated with Tamiya Inc. "Mini 4WD" is a trademark of Tamiya Inc. This SDK is an independent open-source project for hobbyist documentation.*
