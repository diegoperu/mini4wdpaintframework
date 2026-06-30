# Style Decisions — Architecture Decision Records

This document records all significant design and architecture decisions made for the Mini4WD Manual SDK. Each decision is documented as an Architecture Decision Record (ADR).

Before modifying any specification in `Core/`, you must either reference an existing ADR or create a new one here. If a decision is superseded, update the original ADR status and create a new one.

---

## ADR Index

| ID | Title | Status | Version |
|---|---|---|---|
| ADR-001 | Markdown as primary documentation format | Accepted | 1.0.0 |
| ADR-002 | YAML for all structured data | Accepted | 1.0.0 |
| ADR-003 | Permanent page IDs (P001–P010) | Accepted | 2.0.0 |
| ADR-004 | Component-first page assembly | Accepted | 2.0.0 |
| ADR-005 | Design Token system for all visual values | Accepted | 2.1.0 |
| ADR-006 | White background mandatory for all pages | Accepted | 1.0.0 |
| ADR-007 | Violet/purple as primary brand color | Accepted | 1.0.0 |
| ADR-008 | Render-based illustrations only | Accepted | 1.0.0 |
| ADR-009 | AI-model-agnostic prompt design | Accepted | 2.0.0 |
| ADR-010 | Semantic Versioning for all SDK releases | Accepted | 1.0.0 |

---

## ADR-001 — Markdown as Primary Documentation Format

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
The SDK needs a documentation format that is readable as plain text, renderable in web browsers, supported by every major code hosting platform (GitHub, GitLab, Gitea), and editable without special software. XML, HTML, and proprietary formats were considered.

### Decision
All documentation files (README, spec documents, guides) are written in GitHub-Flavored Markdown (GFM). YAML is used for structured data (see ADR-002). PDF and HTML are outputs, never sources.

### Consequences
- Any text editor can open and edit SDK documentation without installation
- Documentation is diff-friendly and PR-reviewable
- Markdown rendering varies slightly across platforms; we target GFM as the baseline
- Complex diagrams are expressed as ASCII art or referenced as images in `Assets/`
- No LaTeX equations; all mathematical notation uses plain text approximations

---

## ADR-002 — YAML for All Structured Data

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
The SDK needs a structured data format for project configuration (PROJECT.yaml), design tokens, PDF configuration, and color schemes. JSON, TOML, and INI were considered. The data must be human-editable without a dedicated tool and must support comments.

### Decision
All structured data files use YAML 1.2. JSON is not used as a primary format (though it may appear in schema validation files). TOML was rejected because it is less familiar to non-developers in the target audience.

### Consequences
- YAML supports inline comments (`#`), which are essential for template files
- YAML indentation sensitivity can cause parse errors; schema validation (tokens.schema.yaml) mitigates this
- All YAML files include a `# yaml-language-server: $schema=` comment where a schema exists
- Tabs are forbidden in YAML files; 2-space indentation is mandatory

---

## ADR-003 — Permanent Page IDs (P001–P010)

**Version:** 2.0.0
**Date:** 2023-09-01
**Status:** Accepted

### Context
In v1, pages were numbered sequentially (01, 02, …) and the numbering implied order. When page 07 (Details) was inserted before what was previously page 07 (Decals), all downstream references broke. File names, prompt references, and approved manual archives all required manual updates.

### Decision
Pages are assigned permanent, immutable identifiers in the format `P###` (three-digit zero-padded). The current set is P001–P010. These identifiers never change regardless of the page's position in the final manual. New pages receive the next available ID (P011, P012, …) even if they are logically inserted between existing pages.

### Consequences
- File names and cross-references based on IDs are stable forever
- The logical order of pages in the PDF is defined by `Templates/PDF_CONFIG.yaml`, not by the IDs
- The identifier P009 (Premium Variant) is not present in all manuals; its absence must be handled gracefully by the PDF pipeline

---

## ADR-004 — Component-First Page Assembly

**Version:** 2.0.0
**Date:** 2023-09-01
**Status:** Accepted

### Context
In v1, page layouts were described holistically in each PromptEngine/ prompt. This led to inconsistency: the header on Cover.md was described differently than the header on Materials.md. When the header specification changed, every prompt required manual updates.

### Decision
Pages are described as assemblies of named, versioned components (C001–C015). The PromptEngine/ prompts reference components by ID. The component specification lives exclusively in `Core/COMPONENT_SYSTEM.md`. Prompts instruct the AI to use `C001 Header` without re-specifying its dimensions, colors, or layout.

### Consequences
- Changing a component specification in COMPONENT_SYSTEM.md propagates to all pages automatically
- AI models must be capable of understanding the component references; this is tested in `Core/QA_SYSTEM.md` §6
- PromptEngine/ prompts are shorter and more focused on page-specific content
- Adding a new component requires only one document change (COMPONENT_SYSTEM.md) plus one CHANGELOG entry

---

## ADR-005 — Design Token System for All Visual Values

**Version:** 2.1.0
**Date:** 2024-01-15
**Status:** Accepted

### Context
Visual values (colors, sizes, fonts) were hardcoded in COMPONENT_SYSTEM.md and STYLE_GUIDE.md as literal hex values and pixel measurements. When a color was adjusted, it required finding and updating all occurrences across multiple documents. There was no single source of truth for visual values.

### Decision
All visual values are defined once in `Assets/DesignSystem/Tokens/tokens.example.yaml`. Every occurrence in Core/ documents, PromptEngine/ prompts, and component specs uses token references in the format `{{token.TokenName}}`. The `tokens.schema.yaml` file defines the allowed token names and their types.

### Consequences
- Changing the primary violet color requires editing one value in one file
- AI models receive token values injected at prompt time (by substituting `{{token.X}}` before submitting the prompt)
- Token names are part of the public SDK API; renaming a token is a breaking change requiring a MAJOR version bump
- Token values must be concrete (hex, pt, mm) — no token may reference another token

---

## ADR-006 — White Background Mandatory for All Pages

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
Early prototypes used light gray (#F0F0F0) or cream (#FFF8F0) backgrounds. Testing showed that slight background tints caused color inaccuracy when printing renders on top of them (the tint shifted perceived paint colors). White also reduces ink cost for print editions.

### Decision
The page background for all manual pages is pure white (#FFFFFF). The violet color is used only in structural elements (header band, side panel, component borders). No page may have a tinted, gradient, or textured background.

### Consequences
- Render images must have white or transparent backgrounds (see `Core/RENDER_GUIDE.md` §4)
- The PDF print variant does not require a background color specification
- Accessibility: white background with dark text always satisfies WCAG 2.1 AA contrast requirements

---

## ADR-007 — Violet/Purple as Primary Brand Color

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
The SDK needed a distinctive primary color that is not associated with any specific Mini4WD brand color, is visually premium, and differentiates the manual system from generic technical documents (which tend to use blue or gray). Red was excluded because it is the standard color for warnings (C008 Warning component). Blue was excluded because it is used for informational callouts.

### Decision
The SDK primary color is VioletPrimary (#5B2D8E), a deep violet. This color is used for the header band (C001), the side panel, component borders, and all brand-identity elements. The full violet palette (VioletDark, VioletLight) is defined in `Core/COLOR_SYSTEM.md`.

### Consequences
- Every manual page immediately signals membership in the Mini4WD Manual SDK through the violet header
- VioletPrimary has sufficient contrast against white (ratio 7.2:1) to satisfy WCAG 2.1 AAA
- White text on VioletPrimary passes WCAG 2.1 AA (ratio 5.1:1)

---

## ADR-008 — Render-Based Illustrations Only

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
Illustration styles considered: hand drawing, vector illustration, flat design, and photorealistic render. Hand drawings depend on artist skill and cannot be replicated consistently. Vector illustrations require manual creation per model. Photography requires physical access to every model in the library.

### Decision
All car body illustrations are photorealistic renders generated by AI image models or 3D rendering software. The rendering standards are specified in `Core/RENDER_GUIDE.md`. No hand-drawn illustrations, flat vector illustrations, or clipart may be used for car body representation.

### Consequences
- Renders can be generated without physical access to the model
- Render quality is constrained by available AI image generation technology at the time
- AI-generated renders require quality review per `Core/RENDER_GUIDE.md` §7
- Vector icons (warning symbols, step numbers, etc.) are permitted and preferred for component decorations

---

## ADR-009 — AI-Model-Agnostic Prompt Design

**Version:** 2.0.0
**Date:** 2023-09-01
**Status:** Accepted

### Context
Early PromptEngine/ prompts contained phrasing like "As a ChatGPT assistant…" and "Use your DALL-E capability to…". This made prompts non-portable. Users reported prompts failing on Claude and Gemini. The SDK cannot be tied to any specific AI provider because providers change capabilities, pricing, and APIs frequently.

### Decision
All PromptEngine/ prompts are written in provider-neutral language. Prompts describe what to produce, not which model should produce it. No prompt may reference a specific AI model name, API, or provider. Prompts use structured token injection (`{{project.X}}`) rather than natural language placeholders.

### Consequences
- Any AI model capable of following structured instructions can use the prompts
- No SDK component can rely on capabilities specific to one AI (e.g., "generate an image inline")
- Image generation and text generation are always separate steps (generate render first, then generate manual page layout description)
- Prompt quality is validated by `Core/QA_SYSTEM.md` §6

---

## ADR-010 — Semantic Versioning for All SDK Releases

**Version:** 1.0.0
**Date:** 2023-03-10
**Status:** Accepted

### Context
An SDK used to generate long-lived documents must have a clear versioning policy. Users need to know when a change in the SDK might affect existing projects. Without versioning, there is no way to pin a project to a stable SDK state.

### Decision
The SDK uses [Semantic Versioning 2.0.0](https://semver.org/): MAJOR.MINOR.PATCH.

- **MAJOR:** Breaking changes — any change to page IDs, component IDs, token names, PROJECT.yaml required fields, or PDF output format
- **MINOR:** Backwards-compatible additions — new pages, new components, new tokens, new documentation
- **PATCH:** Backwards-compatible fixes — typo corrections, clarifications, non-structural changes

The current version is stored in `VERSION` and echoed in `README.md`. Every release is documented in `CHANGELOG.md`. Breaking changes include migration instructions in `Docs/migration/`.

### Consequences
- Projects can reference a specific SDK version in their PROJECT.yaml (`sdkVersion` field)
- Community knows immediately from the version number whether a migration is required
- Pre-1.0 behavior (arbitrary changes) is explicitly prohibited after the 1.0.0 release
