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
| ADR-011 | Separate Configuration from Specification | Accepted | 2.2.0 |
| ADR-012 | Human-Executable Tests as First-Class Citizens | Accepted | 2.2.0 |
| ADR-013 | AI Operating Rules as Mandatory Document | Accepted | 2.2.0 |
| ADR-014 | Knowledge Base Separate from Prompt Templates | Accepted | 2.2.0 |
| ADR-015 | MANIFEST.yaml as Machine-Readable SDK Identity | Accepted | 2.2.0 |

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

## ADR-016

**ID:** ADR-016
**Title:** Text Engine as Independent Editorial Layer
**Version:** 2.3.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
Previous SDK versions treated text as part of the rendering process. AI models would generate visual layouts and text simultaneously, leading to language contamination (Japanese characters, English phrases, Lorem ipsum placeholders) that was difficult to detect before rendering.

### Decision
Introduce a dedicated Text Engine phase that generates all editorial content independently of visual rendering. Text is validated via `Tests/TextValidation.md` and sealed in `ApprovedText/` before the Render Engine begins. The Render Engine receives pre-approved, language-validated text as read-only input.

### Consequences
- Text quality is independently verifiable
- Language violations are caught before any rendering occurs
- AI models can focus on one task at a time (text OR layout — not both)
- ApprovedText files serve as version-controlled editorial record
- Slight increase in production steps (phases 2a/2b/2c added)

---

## ADR-017

**ID:** ADR-017
**Title:** Italian-Only Language Policy with Zero Japanese Tolerance
**Version:** 2.3.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
Mini4WD models are Japanese products. AI models, when generating content about Japanese products, have a tendency to include Japanese text as "aesthetic decoration" — kanji in headers, katakana as design elements, Japanese-inspired pseudo-characters. This is a language contamination problem, not a design problem.

### Decision
Enforce a strict Italian-only language policy via `Config/LANGUAGE_POLICY.yaml`. Zero tolerance for any Japanese scripts (kanji, hiragana, katakana). The visual aesthetic references Japan; the editorial language belongs exclusively to Italy. These are separate layers that never intersect.

### Consequences
- All prompts must load LANGUAGE_POLICY.yaml before generating
- AI Operating Rules expanded with 42 TEXT RENDERING RULES (Rules 059–100)
- Tests/TextValidation.md includes Unicode range checks for CJK scripts
- Approved placeholders defined for uncertain content (never fake text)

---

## ADR-018

**ID:** ADR-018
**Title:** Approved Placeholders Over Invented Content
**Version:** 2.3.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
When PROJECT.yaml data is incomplete, AI models would invent plausible-sounding content (fake paint codes, guessed drying times, fabricated color names). This produced manuals that appeared complete but contained inaccurate technical data.

### Decision
When data is missing, AI models must use approved placeholder strings from `Config/LANGUAGE_POLICY.yaml §approved_placeholders` (`[TITOLO]`, `[TESTO]`, `[VALORE NON SPECIFICATO]`) and add an inline comment pointing to the missing field. Invented content is explicitly forbidden by `Core/AI_OPERATING_RULES.md RULE-063`.

### Consequences
- Incomplete manuals are visually identifiable (placeholders are visible)
- Authors must resolve placeholders before approval
- No silent data fabrication in any approved manual
- Quality is verified by Tests/TextValidation.md TEST-TX-002

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

---

## ADR-011 — Separate Configuration from Specification

**ID:** ADR-011
**Version:** 2.2.0
**Date:** 2024-06-30
**Status:** Accepted

### Context
As the SDK grew beyond documentation, there was a need to distinguish between human-facing specifications (how things SHOULD be) and machine-readable configuration (what values tools USE). Core/ documents mix design philosophy with concrete values, making automation difficult.

### Decision
Introduce `Config/` directory containing YAML files (`sdk.yaml`, `render.yaml`, `pdf.yaml`, `quality.yaml`) that extract concrete parameters from Core/ specs into machine-readable form. Core/ remains authoritative; Config/ implements Core/.

### Consequences
- Tools and scripts read Config/ — not Core/ prose documents
- When Core/ changes, Config/ must be updated in the same commit
- Config/ files are validated against schemas to prevent drift

---

## ADR-012 — Human-Executable Tests as First-Class Citizens

**ID:** ADR-012
**Version:** 2.2.0
**Date:** 2024-06-30
**Status:** Accepted

### Context
The QA_SYSTEM.md checklist covers manual-level quality. There was no validation system for the SDK itself — its internal consistency, document completeness, and cross-reference accuracy.

### Decision
Introduce `Tests/` directory with structured test protocols (`FrameworkIntegrity.md`, `PromptValidation.md`, etc.) as human-executable checklists. These are not automated tests (v3.0.0 goal) but systematic verification guides that can be executed by any contributor.

### Consequences
- SDK contributors must run `Tests/FrameworkIntegrity.md` before releasing new SDK versions
- Test suites are maintained alongside the code they test — each Core/ change may require a Tests/ update
- Automated test conversion planned for v3.0.0

---

## ADR-013 — AI Operating Rules as Mandatory Document

**ID:** ADR-013
**Version:** 2.2.0
**Date:** 2024-06-30
**Status:** Accepted

### Context
PromptEngine/ prompts instruct AI models what to generate, but did not explicitly forbid incorrect behaviors (inventing paint codes, changing body proportions, adding undocumented colors). AI models would occasionally produce plausible but incorrect data.

### Decision
Create `Core/AI_OPERATING_RULES.md` as a mandatory document defining 58+ non-negotiable behavioral rules. All PromptEngine/ prompts should reference this document. QA_SYSTEM.md items verify rule compliance post-generation.

### Consequences
- PromptEngine/ prompts must be updated to reference AI_OPERATING_RULES.md (v2.2.0 update)
- New rules can be added without breaking changes
- Rules are numbered permanently — deprecated rules are marked [DEPRECATED] but not removed

---

## ADR-014 — Knowledge Base Separate from Prompt Templates

**ID:** ADR-014
**Version:** 2.2.0
**Date:** 2024-06-30
**Status:** Accepted

### Context
Technical knowledge about painting techniques (drying times, masking methods, paint compatibility) was scattered across prompt templates and not available as standalone reference material. AI models also needed context injection (RAG) support.

### Decision
Introduce `Knowledge/` as a standalone technical reference library. Knowledge/ contains timeless factual content. PromptEngine/ contains generation instructions. The two are deliberately separate — Knowledge/ can be used independently of any AI model.

### Consequences
- Factual updates (e.g., new paint brand codes) are made in Knowledge/ only
- PromptEngine/ prompts reference Knowledge/ for optional context injection
- Knowledge/ is accessible to non-SDK users as a standalone reference

---

## ADR-015 — MANIFEST.yaml as Machine-Readable SDK Identity

**ID:** ADR-015
**Version:** 2.2.0
**Date:** 2024-06-30
**Status:** Accepted

### Context
There was no single machine-readable file describing the SDK's identity, structure, capabilities, and compatibility requirements. Tools and integrations had to parse prose README files.

### Decision
Introduce `MANIFEST.yaml` at the project root as the authoritative machine-readable SDK descriptor. Contains: name, version, directory map, supported page types, supported component IDs, minimum AI requirements, and compatibility matrix.

### Consequences
- MANIFEST.yaml must be updated with every SDK release
- Version in MANIFEST.yaml must match VERSION file (verified by Tests/FrameworkIntegrity.md TEST-FW-005)
- Future tooling can use MANIFEST.yaml for SDK introspection

---

## ADR-019

**ID:** ADR-019
**Title:** content.yaml as Primary Source of Truth for Page Content
**Version:** 2.4.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
In v2.3.0, the Text Engine output was `ApprovedText/P{NNN}.md` — a Markdown file containing pre-approved Italian content. While this decoupled text from rendering, Markdown has no enforced schema. AI models could generate structurally inconsistent files. Components had no formal mapping to text fields. The Render Engine had to parse unstructured Markdown to extract values.

### Decision
Introduce `content.yaml` as the primary output format for the Text Engine. Each page module in `ApprovedAssets/Text/P{NNN}/` contains a structured YAML file with page-specific fields. Component-to-field mapping is declared in `Core/COMPONENT_SYSTEM.md`. The Render Engine reads `content.yaml` exclusively; `text.md` is a human-readable derivative, auto-generated for editorial review only.

### Consequences
- All text content is schema-validated before approval (Tests/ContentValidation.md CV-001)
- Component-field mapping is machine-verifiable (CV-006)
- text.md is DERIVED, not primary — editing text.md has no effect on rendering
- Render Engine reads `ApprovedAssets/Text/P{NNN}/content.yaml` — never PROJECT.yaml
- Field names: English (structural). Field values: Italian (editorial). Never reversed.
- Incomplete data uses approved placeholders (`[TITOLO]`, `[TESTO]`) — never invented

---

## ADR-020

**ID:** ADR-020
**Title:** Page-as-Module Architecture with Lifecycle States
**Version:** 2.4.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
Pages were previously treated as outputs — files to be generated and approved in one pass. There was no formal lifecycle, no per-page state tracking, no approval history, and no lock mechanism to prevent modification of approved content. In team environments or multi-session AI workflows, approved content could be silently overwritten.

### Decision
Each page is a self-contained module: a directory containing `content.yaml`, `text.md`, `metadata.yaml`, `manifest.yaml`, `changelog.md`, `notes.md`, and `README.md`. Page state is tracked in `metadata.yaml` through a formal lifecycle: `draft → review → approved → locked → rendered → released → archived`. Locked pages cannot be modified without explicit unlock and re-approval. Revision history is recorded per page.

### Consequences
- Each page has an auditable lifecycle (status, approvals, dates, revision counter)
- `locked: true` in metadata.yaml is a hard gate — Render Engine skips locked but unapproved pages
- Per-page `changelog.md` tracks every revision with date and reason
- Pages can be reused across manuals (same permanent ID P001–P010, different content.yaml)
- `notes.md` is editorial scratch space — never rendered, not version-controlled as authoritative

---

## ADR-021

**ID:** ADR-021
**Title:** Render Engine Reads content.yaml Exclusively — Never PROJECT.yaml
**Version:** 2.4.0
**Date:** 2026-07-01
**Status:** Accepted

### Context
Prior to v2.4.0, the Render Engine could access PROJECT.yaml directly to supplement missing content. This created a silent bypass of the Text Engine and language validation pipeline. An AI model could generate a page using PROJECT.yaml data that had never been through language QA, potentially introducing English strings, missing Italian terms, or unformatted values.

### Decision
The Render Engine is contractually prohibited from reading PROJECT.yaml. Its only source of page content is `ApprovedAssets/Text/P{NNN}/content.yaml`. If a field is missing from content.yaml, the Render Engine uses the approved placeholder (`[TESTO]`) and logs a warning — it does not fall back to PROJECT.yaml or any other source.

### Consequences
- Full language QA pipeline is always exercised — no bypass path exists
- Text Engine approval is a hard prerequisite for rendering (enforced by metadata.yaml §approved)
- PROJECT.yaml remains the source of truth for project configuration (metadata, model info, render paths) — not editorial content
- Render Engine errors are caught early: missing content.yaml fields appear as visible placeholders, not silent data substitutions
- AI_OPERATING_RULES.md updated with explicit rule: Render Engine reads ApprovedAssets/Text/P{NNN}/content.yaml ONLY
