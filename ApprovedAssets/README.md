# ApprovedAssets/

> **A cosa serve questa cartella:** il CMS dell'SDK — contenuti editoriali e visivi approvati, un modulo per pagina.
> **Chi la modifica:** l'**AI via prompt** (contenuti), Reviewer/Maintainer (approvazioni e `index.yaml`). **Mai l'Operatore a mano.**
> **Quando:** Fasi 2–4 del workflow (testi, QA, render). I moduli nascono come TEMPLATE in stato `draft`: campi vuoti = normale, non è contenuto difettoso (vedi `Tests/ContentValidation.md §Validation Scope`).

**Role in framework:** The single source of truth for all approved editorial and visual content in the Mini4WD Manual SDK.

**SDK Version:** 2.4.1
**Supersedes:** `Projects/{ModelName}/ApprovedText/` (v2.3.0) — retained for backward compatibility

---

## Architecture

ApprovedAssets/ is the CMS layer of the SDK. Unlike `Projects/`, which is a working directory, ApprovedAssets/ contains only **sealed, approved content** ready for rendering and publication.

```
ApprovedAssets/
├── Text/          ← Structured content: content.yaml + text.md per page
│   ├── P001/      ← One directory per page (permanent IDs)
│   ├── P002/
│   └── ...P010/
├── Images/        ← Approved renders organized by page and model
├── Components/    ← Approved component instances
├── Templates/     ← Layout templates (no content — structure only)
├── References/    ← Reference images and source material
└── index.yaml     ← Global content registry
```

## The Content Philosophy

**content.yaml is the source of truth.** It contains structured editorial data in machine-readable YAML. Every other representation derives from it:
- `text.md` is generated from `content.yaml` for human readability
- Render prompts read `content.yaml` to populate visual components
- QA tools validate against `content.yaml` schema

**text.md is derived, not primary.** If content.yaml and text.md disagree, content.yaml wins. Never edit text.md without also updating content.yaml.

## Page Lifecycle

Every page in `Text/P{NNN}/` follows this lifecycle:

```
draft → review → approved → locked → rendered → released → archived
```

Status is tracked in `Text/P{NNN}/metadata.yaml §status`.

## What belongs here
- Approved, validated content ready for rendering
- Sealed page modules (locked pages are read-only)
- Approved render images
- Published component instances

## What does NOT belong here
- Work-in-progress content → Projects/{ModelName}/
- Unapproved text → Projects/{ModelName}/ApprovedText/raw/
- Reference source photos → Assets/ReferenceModels/
- SDK specifications → Core/

## Dependencies
- `Core/PAGE_SYSTEM.md` — page ID registry
- `Core/TEXT_ENGINE.md` — content generation specification
- `Config/LANGUAGE_POLICY.yaml` — language enforcement
- `Tests/ContentValidation.md` — QA protocol
- `MANIFEST.yaml` — SDK-level registry

## Related Documents
- `Core/TEXT_ENGINE.md`
- `Build/Pipeline.md`
- `Tests/ContentValidation.md`
- `ApprovedAssets/index.yaml`
