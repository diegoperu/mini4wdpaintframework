# Build/

**Role in framework:** The Build directory defines the production pipeline — the end-to-end process that transforms a PROJECT.yaml into a published, approved Mini4WD painting manual.

**SDK Version:** 2.2.0

**Scope:** Orchestration, pipeline documentation, phase sequencing. Not AI prompts (→ PromptEngine/), not design specs (→ Core/).

## Contents

| File | Purpose |
|------|---------|
| `Pipeline.md` | Complete production pipeline specification |

## Workflow Position

Build/ sits at the center of the SDK workflow:

```
Core/ specs + Templates/ + PromptEngine/
              ↓
         PROJECT.yaml
              ↓
         Build/Pipeline.md  ← YOU ARE HERE
              ↓
         Assets/ApprovedManual/
```

## What belongs here
- Pipeline phase definitions
- Phase input/output contracts
- Automation scripts (future — planned v2.3.0)
- CI/CD integration specs (planned v2.3.0)

## What does NOT belong here
- AI prompts → `PromptEngine/`
- Design specs → `Core/`
- Templates → `Templates/`
- Test definitions → `Tests/`

## Dependencies
- `Core/WORKFLOW.md` — high-level workflow (this document provides operational detail)
- `Core/QA_SYSTEM.md` — QA phase spec
- `Core/PDF_MASTER.md` — PDF generation phase
- `Config/sdk.yaml` — runtime configuration

## Related Documents
- `Core/WORKFLOW.md`
- `Core/QA_SYSTEM.md`
- `Core/PDF_MASTER.md`
- `Templates/PROJECT.yaml`
- `Config/sdk.yaml`
- `Tests/README.md`
