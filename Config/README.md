# Config/

> **A cosa serve questa cartella:** configurazione globale dell'SDK — language policy, soglie QA, parametri render e PDF.
> **Chi la modifica:** solo Developer.
> **Quando:** solo a release SDK. L'Operatore non la modifica mai: se un validatore sbaglia, si segnala al Maintainer.

**Role in framework:** Runtime configuration for all SDK tools and processes.

**SDK Version:** 2.4.1

Configuration files in this directory drive the behavior of the SDK pipeline, validation tools, and export processes. They are distinct from `Core/` specifications (which are human-facing standards) — Config/ files are machine-readable parameters.

## Contents

| File | Purpose |
|------|---------|
| `sdk.yaml` | Global SDK runtime parameters, page/component registries, naming rules |
| `render.yaml` | Render engine configuration: angles, lighting rigs, resolution thresholds |
| `pdf.yaml` | PDF export global defaults and variant definitions |
| `quality.yaml` | QA validation rules, thresholds, and approval requirements |

## Principles
- All config files are YAML
- Each file is self-documenting (inline comments on every parameter)
- Config files extend Core/ defaults without modifying Core/ documents
- Projects may define local overrides in `Projects/{ModelName}/config/` (future)

## What belongs here
- Global defaults for SDK operations
- Validation thresholds used by `Tests/`
- Tool integration parameters
- Environment-specific overrides (future: `Config/environments/`)

## What does NOT belong here
- Per-project data → `Projects/{ModelName}/PROJECT.yaml`
- Design specifications → `Core/`
- Visual design tokens → `Assets/DesignSystem/Tokens/`
- AI prompts → `PromptEngine/`

## How Config files relate to Core documents

| Config file | Implements parameters from |
|-------------|---------------------------|
| `sdk.yaml` | `Core/MANUAL_SYSTEM.md`, `Core/NAMING_CONVENTION.md` |
| `render.yaml` | `Core/RENDER_GUIDE.md` |
| `pdf.yaml` | `Core/PDF_MASTER.md` |
| `quality.yaml` | `Core/QA_SYSTEM.md`, `Core/DEFINITION_OF_DONE.md` |

## Dependency Chain
```
Core/ specs (human standards)
        ↓
Config/ (machine parameters)
        ↓
Build/Pipeline.md (uses config values)
        ↓
Tests/ (validates against config thresholds)
```

## Related Documents
- `Build/Pipeline.md`
- `Core/WORKFLOW.md`
- `Core/QA_SYSTEM.md`
- `Assets/DesignSystem/Tokens/tokens.example.yaml`
- `Tests/FrameworkIntegrity.md` — verifies version consistency in this directory
