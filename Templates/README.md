# Templates

## Purpose

Templates are the entry point for every new Mini4WD manual project. This directory contains blank, fully commented master copies of all configuration files needed to start a project from scratch.

Templates are **never edited in place**. They are **copied** to `Projects/{ModelName}/` before filling in project-specific data.

---

## Responsibilities

- Provide a single source of truth for all project configuration schemas
- Ensure every new project starts from a known, validated structure
- Document every field with inline comments
- Serve as living documentation of the PROJECT.yaml schema

## What to Put Here

- Master template files in YAML and Markdown formats
- Schema documentation embedded as YAML comments
- Example values (clearly marked as examples)

## What NOT to Put Here

- Filled-in project data (belongs in `Projects/{ModelName}/`)
- Design assets (belong in `Assets/`)
- Prompt files (belong in `PromptEngine/`)
- Generated output (belongs in `Projects/{ModelName}/Output/`)

---

## File List

| File | Purpose | Copy to |
|------|---------|---------|
| `PROJECT.yaml` | Main project configuration | `Projects/{ModelName}/PROJECT.yaml` |
| `PROJECT.md` | Human-readable project brief | `Projects/{ModelName}/PROJECT.md` |
| `CHECKLIST.md` | Progress tracking checklist | `Projects/{ModelName}/CHECKLIST.md` |
| `COLOR_SCHEME.yaml` | Color scheme definition | `Projects/{ModelName}/COLOR_SCHEME.yaml` |
| `PDF_CONFIG.yaml` | PDF export configuration | `Projects/{ModelName}/PDF_CONFIG.yaml` |

---

## How to Start a New Project

1. **Create the project folder:**
   ```
   mkdir -p Projects/YourModelName/Images
   mkdir -p Projects/YourModelName/Output/raw
   mkdir -p Projects/YourModelName/Notes
   ```

2. **Copy all templates:**
   ```
   cp Templates/PROJECT.yaml Projects/YourModelName/PROJECT.yaml
   cp Templates/PROJECT.md Projects/YourModelName/PROJECT.md
   cp Templates/CHECKLIST.md Projects/YourModelName/CHECKLIST.md
   cp Templates/COLOR_SCHEME.yaml Projects/YourModelName/COLOR_SCHEME.yaml
   cp Templates/PDF_CONFIG.yaml Projects/YourModelName/PDF_CONFIG.yaml
   ```

3. **Fill in `PROJECT.yaml` first** — it is the data source for all prompt tokens.

4. **Fill in `PROJECT.md`** — use it as a human-readable brief to share with collaborators.

5. **Open `CHECKLIST.md`** — use it to track progress through the workflow.

6. **See `Core/WORKFLOW.md`** for the complete step-by-step generation pipeline.

---

## Required vs Optional Fields

Every field in `PROJECT.yaml` is annotated with `# REQUIRED` or `# OPTIONAL`.

- **REQUIRED** fields: the PromptEngine cannot generate correct output without them. Leaving a required field empty will produce prompts with unresolved `{{token}}` placeholders.
- **OPTIONAL** fields: the PromptEngine handles their absence gracefully. Some optional fields enable additional content (e.g., `premiumVariant.enabled: true` enables P009).

---

## Schema Versioning

Templates are versioned together with the SDK. The `sdk_version` field at the top of `PROJECT.yaml` must match the SDK version used to generate the manual.

If you upgrade the SDK:
1. Check `CHANGELOG.md` for breaking changes in the PROJECT.yaml schema.
2. Update your project's `PROJECT.yaml` accordingly.
3. See `Docs/migration/` for migration guides between major versions.

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Editing the template instead of the copy | All future projects start with wrong values | Only ever copy — never fill the original |
| Leaving required fields empty | Unresolved tokens in generated pages | Check all REQUIRED fields before running prompts |
| Using wrong `sdk_version` | Schema mismatch, token errors | Match sdk_version to the SDK version in `VERSION` file |
| Wrong `modelSlug` format | File naming errors | Must be lowercase kebab-case: `proto-emperor` not `Proto Emperor` |
| `premiumVariant.enabled: true` without filling premium fields | Empty P009 | Always fill `premiumVariant.name` and `specialTechniques` when enabling |

---

## Dependencies

| Document | Role |
|----------|------|
| `Core/PAGE_SYSTEM.md` | Defines which PROJECT.yaml fields each page uses |
| `PromptEngine/README.md` | Master token reference table |
| `Core/WORKFLOW.md` | Complete generation pipeline |
| `Core/NAMING_CONVENTION.md` | Naming rules for modelSlug and file paths |

---

*Templates are part of Mini4WD Manual SDK v2.1.0. See `Core/WORKFLOW.md` for the complete generation pipeline.*
