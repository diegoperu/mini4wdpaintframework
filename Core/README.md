# Core

> **A cosa serve questa cartella:** specifica autoritativa del framework — design, componenti, pagine, regole AI, QA. Tutto il resto dell'SDK dipende da qui.
> **Chi la modifica:** solo Developer, con ADR in `STYLE_DECISIONS.md`.
> **Quando:** solo a release SDK. **Mai durante un progetto.** L'Operatore la legge/allega, non la tocca.

The `Core/` directory is the authoritative specification layer of the Mini4WD Manual SDK. Every other directory in this SDK depends on Core. No component, prompt, template, or asset may contradict a Core specification.

---

## Responsibility

Core documents define **what** the SDK is and **how** it behaves. They do not contain project-specific content, model data, AI prompts, or finished output. They are technical specifications in the same tradition as a software API reference or an industrial design standard.

If a decision about visual design, editorial style, page structure, or workflow cannot be answered by reading `Core/`, then `Core/` is incomplete and must be extended before work continues.

---

## Governance

Changes to `Core/` require an Architecture Decision Record (ADR) filed in `STYLE_DECISIONS.md` at the root of the SDK. You must not modify a Core document without either:
- Referencing an existing ADR that covers your change, or
- Creating a new ADR that records the decision, its context, and its consequences.

This requirement exists because Core specifications propagate to every manual ever produced by the SDK. A change to `COMPONENT_SYSTEM.md` affects every existing and future prompt in `PromptEngine/`. A change to `COLOR_SYSTEM.md` potentially invalidates approved manuals in `Assets/ApprovedManual/`. Changes must be deliberate and documented.

---

## Files in This Directory

| File | Description |
|---|---|
| `DESIGN_LANGUAGE.md` | The philosophical DNA of the framework — 50+ rules governing every design decision |
| `STYLE_GUIDE.md` | Technical specification for colors, typography, grid, spacing, and component styling |
| `COLOR_SYSTEM.md` | Full color palette with hex, RGB, CMYK, and Pantone values; color roles and accessibility rules |
| `MANUAL_SYSTEM.md` | Architecture overview, manual lifecycle, template inheritance, and publication policy |
| `PAGE_SYSTEM.md` | Specification for permanent pages P001–P010; input/output, dependencies, checklists |
| `COMPONENT_SYSTEM.md` | Specification for reusable components C001–C015; dimensions, variants, token references |
| `RENDER_GUIDE.md` | Standards for all illustrations: required angles, lighting rigs, resolution, AI prompt templates |
| `PDF_MASTER.md` | Full specification for PDF export: color profiles, bleed, metadata, font embedding |
| `QA_SYSTEM.md` | 110-item quality assurance checklist organized by category |
| `WORKFLOW.md` | End-to-end production workflow from PROJECT.yaml to final PDF |
| `NAMING_CONVENTION.md` | File, folder, and image naming rules for the entire SDK |
| `DOCUMENTATION_STYLE.md` | Style guide for writing SDK documentation (voice, tense, headings, formatting) |
| `DEFINITION_OF_DONE.md` | Completion criteria at manual, page, and framework levels |

---

## Dependency Order

Core documents have a natural dependency chain. When reading for the first time, follow this order:

```
DESIGN_LANGUAGE
      │
      ▼
 STYLE_GUIDE ──────────────────────┐
      │                            │
      ▼                            ▼
COLOR_SYSTEM              NAMING_CONVENTION
      │
      ▼
PAGE_SYSTEM ───────────── COMPONENT_SYSTEM
      │                            │
      └──────────────┬─────────────┘
                     │
                     ▼
               RENDER_GUIDE
                     │
                     ▼
               PDF_MASTER
                     │
                     ▼
              QA_SYSTEM ────── DEFINITION_OF_DONE
                     │
                     ▼
                WORKFLOW
```

`MANUAL_SYSTEM.md` and `DOCUMENTATION_STYLE.md` are standalone reference documents that can be read at any point.

---

## What Belongs Here

- Definitions: what a "page", "component", "token", or "render" is in this SDK
- Rules: what must, should, or must not appear in any manual
- Specifications: exact values for dimensions, colors, type sizes, render resolutions
- Checklists: QA criteria applied to every deliverable
- Workflow: the sequence of operations that produces a finished manual

## What Does Not Belong Here

- Project-specific data (model names, paint schemes, render paths) → belongs in `Projects/`
- AI prompt text → belongs in `PromptEngine/`
- Design files, images, or fonts → belongs in `Assets/`
- Starter templates → belongs in `Templates/`
- Example or sample output → belongs in `Assets/Examples/` or `Assets/ApprovedManual/`

---

## Relationship to Other Directories

| Directory | How It Uses Core |
|---|---|
| `PromptEngine/` | Every prompt references page IDs from PAGE_SYSTEM.md and component IDs from COMPONENT_SYSTEM.md |
| `Templates/` | PROJECT.yaml schema is derived from MANUAL_SYSTEM.md; PDF_CONFIG.yaml implements PDF_MASTER.md |
| `Assets/DesignSystem/` | Design tokens implement the values specified in COLOR_SYSTEM.md and STYLE_GUIDE.md |
| `Assets/ApprovedManual/` | An approved manual has passed all checks in QA_SYSTEM.md and DEFINITION_OF_DONE.md |
| `Projects/` | Each project produces output that must satisfy Core specifications to be approved |
| `Docs/` | Extended guides reference Core documents and must not contradict them |

---

## Common Errors

**Modifying visual values without updating tokens.** If you change a hex value in COLOR_SYSTEM.md, the corresponding token in `Assets/DesignSystem/Tokens/tokens.example.yaml` must also be updated. Values exist in exactly one place; COLOR_SYSTEM.md describes the color system, and the token file is the machine-readable source. Do not let them diverge.

**Adding content to Core that belongs in PromptEngine.** Core describes structure, not prompt text. If you find yourself writing "Tell the AI to…" in a Core document, that content belongs in PromptEngine/.

**Skipping the ADR.** It is tempting to make a "small" change to a component dimension or a font size without filing an ADR. Resist this. Even small changes to Core propagate to all existing prompts and potentially invalidate approved manuals. The ADR is not bureaucracy — it is the record that explains to a contributor in 2030 why a specific value was chosen.
