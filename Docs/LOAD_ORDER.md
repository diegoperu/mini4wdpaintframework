# LOAD_ORDER.md
# Mini4WD Manual SDK — Context Loading Order

**Version:** 2.4.1

> This document defines the exact order in which an AI model must load SDK documents
> before generating any page. Skipping steps or loading out of order produces incomplete
> context and rule conflicts. Follow this sequence exactly.

---

## Why Order Matters

Each document in the LOAD sequence builds on the previous ones:

- `AI_ENTRYPOINT.md` establishes the Bootstrap Contract — the binding agreement that governs everything
- `AI_OPERATING_RULES.md` establishes behavioral constraints that govern how all other documents are interpreted
- `LANGUAGE_POLICY.yaml` must be active before any text is generated
- `TEXT_ENGINE.md` defines the output format — must be loaded before generating `content.yaml`
- `DESIGN_LANGUAGE.md` and `STYLE_GUIDE.md` define the visual grammar — must be loaded before rendering
- `COMPONENT_SYSTEM.md` must be loaded before `PAGE_SYSTEM.md` (pages reference components)
- `PROJECT.yaml` is loaded last among specifications because it overrides defaults set by all previous documents
- `ApprovedAssets/` are loaded after `PROJECT.yaml` to provide existing sealed content for the current project

---

## Full LOAD Sequence

### Step 0 — AI_ENTRYPOINT.md
**Type:** Markdown | **Path:** `AI_ENTRYPOINT.md`

The official SDK entry point. Contains the Bootstrap Contract (YAML block), mission, source-of-truth hierarchy, workflow overview, AI operating mode, editorial philosophy, language rules, Golden Rules, completion checklist, and First Response Policy.

**Why first:** The Bootstrap Contract at the top of this file defines the binding rules for everything that follows. No other document can be correctly interpreted without first accepting this contract. After reading this file, produce the Bootstrap Report and wait for user approval before generating any content.

**What you learn:** The 10 Golden Rules, the complete pipeline, the First Response Policy (Bootstrap Report + wait for approval), and the exact read order for all subsequent documents.

---

### Step 1 — SDK_CONTEXT.yaml
**Type:** YAML | **Path:** `SDK_CONTEXT.yaml`

SDK identity card. Provides version, pipeline overview, architecture principles, and source-of-truth hierarchy. Establishes the operating context for all subsequent documents.

**What you learn:** What version of the SDK you are using, what the pipeline is, what the source of truth is, what the load order should be.

---

### Step 2 — BOOTSTRAP.md
**Type:** Markdown | **Path:** `BOOTSTRAP.md`

Operational guide — expands on the rules and workflow introduced in AI_ENTRYPOINT.md. Covers pipeline detail, page and component index, common errors to avoid, and the document map.

**What you learn:** Detailed pipeline steps, pages P001–P010 with prompt files, components C001–C015 with roles, content.yaml structure, expected output format, complete error table.

---

### Step 3 — AI_OPERATING_RULES.md
**Type:** Markdown | **Path:** `Core/AI_OPERATING_RULES.md`

100 behavioral rules governing AI model behavior during all phases of production. Rules 001–058 cover design and rendering. Rules 059–100 cover text rendering. All rules are binding.

**What you learn:** Exactly what an AI model may and may not do, in detail. These rules are the behavioral contract for the entire framework.

---

### Step 4 — LANGUAGE_POLICY.yaml
**Type:** YAML | **Path:** `Config/LANGUAGE_POLICY.yaml`

Italian-only language policy. Defines the permitted language (it), forbidden languages (ja, en in body text), forbidden scripts (kanji, hiragana, katakana), and approved placeholders (`TODO:`).

**What you learn:** Language is Italian only. Zero tolerance for Japanese. The only permitted non-Italian string is `TODO:` as placeholder.

**Load before:** Any text generation step.

---

### Step 5 — TEXT_ENGINE.md
**Type:** Markdown | **Path:** `Core/TEXT_ENGINE.md`

Text Engine specification. Defines how editorial text is generated, the `content.yaml` schema (primary output), the `text.md` derivation rules, and the relationship between the Text Engine and the Render Engine.

**What you learn:** `content.yaml` is the primary output of text generation. The Render Engine reads `content.yaml` only. `text.md` is derived and read-only after approval.

**Load before:** Any text generation or content.yaml production.

---

### Step 6 — DESIGN_LANGUAGE.md
**Type:** Markdown | **Path:** `Core/DESIGN_LANGUAGE.md`

65 rules defining the visual philosophy of the SDK. Rules 1–54 cover aesthetic identity (Tamiya 1990s reinterpreted with modern sensibility, violet as signature color). Rules 55–65 cover editorial identity (Italian editorial voice vs. Japanese aesthetic).

**What you learn:** The visual DNA of every page — violet panel, white background, clean callouts, numbered steps, technical precision.

---

### Step 7 — STYLE_GUIDE.md
**Type:** Markdown | **Path:** `Core/STYLE_GUIDE.md`

Color palette, typography, grid, and spacing specifications. Includes Typography Rules for Italian editorial text.

**What you learn:** Exact palette, font families (TitleFont / BodyFont), grid structure, spacing system.

---

### Step 8 — COMPONENT_SYSTEM.md
**Type:** Markdown | **Path:** `Core/COMPONENT_SYSTEM.md`

Specifications for all 15 components (C001–C015), including dimensions, content.yaml field mapping, and layout rules.

**What you learn:** Exactly how each component is structured, what content.yaml fields it consumes, and how it must be rendered.

---

### Step 9 — PAGE_SYSTEM.md
**Type:** Markdown | **Path:** `Core/PAGE_SYSTEM.md`

Specifications for all 10 pages (P001–P010), including required components, layout zones, and content requirements.

**What you learn:** Which components appear on each page, in which zones, with what constraints.

---

### Step 10 — PromptEngine/{page}.md
**Type:** Markdown | **Path:** `PromptEngine/Cover.md` (or the page being generated)

Page-specific prompt for the current page. Contains the generation instructions, required fields, and page-specific rules.

**What you learn:** The specific instructions for generating the current page.

**Note:** Load only the prompt for the page you are currently generating. Do not pre-load all 10 prompts.

---

### Step 11 — Projects/{ModelName}/PROJECT.yaml
**Type:** YAML | **Path:** `Projects/{ModelName}/PROJECT.yaml`

Project configuration for the current model. Contains model name, series, paint scheme, render paths, and all project-specific data. Overrides prompt defaults for any field it specifies.

**What you learn:** The actual model name, paint colors (Tamiya codes + Italian names), render file paths, and all project-specific data that populates content.yaml.

**Critical:** Do not use default values when PROJECT.yaml provides explicit values. PROJECT.yaml always wins over defaults.

---

### Step 12 — ApprovedAssets/Text/{page}/
**Type:** Directory | **Path:** `Projects/{ModelFolder}/{VariantFolder}/ApprovedText/P00x/`

Existing sealed content for the current page, if any. Contains `content.yaml` (primary source of truth), `metadata.yaml` (lifecycle state), `manifest.yaml` (dependencies), and `changelog.md` (revision history).

**What you learn:** Whether this page already has approved content. If `metadata.yaml → status: locked`, do not regenerate — render from the existing `content.yaml`.

**If the page is locked:** Go directly to Phase 3 (Render Engine). Do not modify content.yaml.

---

### Step 13 — Reference Images
**Type:** Image files | **Path:** `Projects/{ModelName}/Images/` or provided by user

Photography of the physical Mini4WD model. Used by the Render Engine to ensure renders match the real product exactly.

**What you learn:** The actual form, color areas, and surface details of the model.

**Critical:** Renders must match the reference images. Never modify the model's shape, proportions, or structure.

---

## Abbreviated LOAD (Minimum Viable)

If context window is limited and you must prioritize, load in this minimum-viable order:

```
0. AI_ENTRYPOINT.md           ← Cannot be skipped — contains Bootstrap Contract
1. SDK_CONTEXT.yaml           ← Cannot be skipped
2. BOOTSTRAP.md               ← Cannot be skipped
3. Core/AI_OPERATING_RULES.md ← Cannot be skipped
4. Config/LANGUAGE_POLICY.yaml ← Cannot be skipped before text generation
5. Core/TEXT_ENGINE.md        ← Cannot be skipped before content.yaml generation
6. PromptEngine/{page}.md     ← Page-specific — always required
7. Projects/{Model}/PROJECT.yaml ← Always required
```

Steps 6–9 (Design Language, Style Guide, Component System, Page System) are required before rendering. They may be deferred if the current task is text-only generation.

---

## Phase-Specific Load Requirements

| Phase | Minimum Required Documents |
|-------|---------------------------|
| Phase 0 — Bootstrap | Step 0 (AI_ENTRYPOINT.md) + Step 1 (SDK_CONTEXT.yaml) |
| Phase 2a — Text Engine | Steps 0–7 + 10–11 |
| Phase 2b/2c — QA | Steps 0–4 + Tests/ContentValidation.md + Tests/TextValidation.md |
| Phase 3 — Render Engine | Steps 0–13 (full load) |
| Phase 4 — Page QA | Steps 0–4 + Core/QA_SYSTEM.md |
| Phase 5 — PDF | Steps 0–4 + Core/PDF_MASTER.md + Templates/PDF_CONFIG.yaml |

---

## Cross References

- `AI_ENTRYPOINT.md` → Bootstrap Contract and First Response Policy
- `SDK_CONTEXT.yaml` → `load_order` field summarizes this document
- `BOOTSTRAP.md` → operational guide — detailed pipeline and error table
- `Core/WORKFLOW.md` → detailed workflow using this load order
- `Build/Pipeline.md` → phase-by-phase pipeline with load requirements
- `PromptEngine/README.md` → LOAD sequence for prompt execution
