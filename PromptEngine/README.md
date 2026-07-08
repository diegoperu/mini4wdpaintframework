# PromptEngine

> **A cosa serve questa cartella:** i prompt ufficiali per generare ogni pagina (P001–P010). L'Operatore li ALLEGA in chat, uno per pagina, in Fase 2.
> **Chi la modifica:** solo Developer.
> **Quando:** solo a release SDK. Mai adattarli a un singolo progetto: i dati di progetto stanno in PROJECT.yaml.

## Purpose

PromptEngine is the bridge between the Core specification layer and AI-driven page generation. Each file in this directory contains a fully specified, model-agnostic prompt for generating one page of a Mini4WD painting manual.

PromptEngine does not contain design decisions. It references them. Every visual rule, every component spec, every color token — all defined in `Core/`. The prompts here are *executors*, not *definers*.

---

## Responsibilities

- Translate `PROJECT.yaml` data into page-specific generation instructions
- Encode the layout, component, and style requirements for each page
- Remain compatible with any AI model (ChatGPT, Claude, Gemini, Mistral, etc.)
- Never duplicate Core specifications — always reference by document and section

## What to Put Here

- One `.md` file per page ID (Cover.md → P001, ColorScheme.md → P002, etc.)
- Prompt templates using `{{token}}` syntax for PROJECT.yaml fields
- Token reference tables per prompt
- Validation checklists linking to QA_SYSTEM.md and DEFINITION_OF_DONE.md

## What NOT to Put Here

- Design decisions (belong in `Core/STYLE_GUIDE.md`, `Core/DESIGN_LANGUAGE.md`)
- Color definitions (belong in `Core/COLOR_SYSTEM.md`)
- Component specifications (belong in `Core/COMPONENT_SYSTEM.md`)
- Model-specific data (belongs in `Projects/{ModelName}/PROJECT.yaml`)
- AI-model-specific syntax (e.g., no `[INST]` tags, no system prompt wrappers)

---

## File List

| File | Page ID | Description |
|------|---------|-------------|
| `Cover.md` | P001 | Cover page prompt |
| `ColorScheme.md` | P002 | Color scheme overview prompt |
| `Materials.md` | P003 | Materials and shopping list prompt |
| `Preparation.md` | P004 | Surface preparation steps prompt |
| `Painting.md` | P005 | Paint application sequence prompt |
| `Masking.md` | P006 | Masking technique guide prompt |
| `Details.md` | P007 | Fine detail painting prompt |
| `Decals.md` | P008 | Decal placement guide prompt |
| `Premium.md` | P009 | Premium variant prompt |
| `FinalChecklist.md` | P010 | Final quality checklist prompt |

---

## Token Substitution

All prompts use `{{token.path}}` syntax, mirroring the structure of `PROJECT.yaml`. Tokens must be substituted **before** sending the prompt to an AI model.

### How to Run a Prompt

1. Open `Projects/{ModelName}/PROJECT.yaml` and verify all required fields are filled.
2. Open the desired prompt file (e.g., `PromptEngine/Cover.md`).
3. Copy the **Prompt Template** section.
4. Replace every `{{token}}` with the corresponding value from `PROJECT.yaml`.
5. Paste the substituted prompt into your AI model of choice.
6. Save the AI output to `Projects/{Modello}/{Variante}/ApprovedText/P001/content.yaml` (or appropriate page ID).
7. Run `Tests/ContentValidation.md` and `Tests/TextValidation.md` — both must pass before sealing (`metadata.yaml → status: locked`), then run `Core/QA_SYSTEM.md` at render stage.

### Automation

Token substitution can be automated with any scripting language. Example (Python pseudocode):

```python
import yaml, re

with open("Projects/Proto_Emperor/PROJECT.yaml") as f:
    data = yaml.safe_load(f)

with open("PromptEngine/Cover.md") as f:
    prompt = f.read()

# Flatten nested keys: project.modelName → data["project"]["modelName"]
def resolve(token, data):
    keys = token.split(".")
    val = data
    for k in keys:
        val = val[k]
    return str(val)

tokens = re.findall(r"\{\{([\w.]+)\}\}", prompt)
for t in tokens:
    prompt = prompt.replace("{{" + t + "}}", resolve(t, data))

print(prompt)
```

---

## Master Token Reference

All tokens used across all prompts in this directory:

| Token | Source Field | Used In |
|-------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | All pages |
| `{{project.modelSlug}}` | `project.modelSlug` | All pages (file naming) |
| `{{project.seriesName}}` | `project.seriesName` | P001, P002 |
| `{{project.year}}` | `project.year` | P001 |
| `{{project.language}}` | `project.language` | All pages |
| `{{project.version}}` | `project.version` | P010 |
| `{{project.author}}` | `project.author` | P001, P010 |
| `{{paintScheme.name}}` | `paintScheme.name` | P001, P002, P010 |
| `{{paintScheme.description}}` | `paintScheme.description` | P002 |
| `{{paintScheme.colorNotes}}` | `paintScheme.colorNotes` | P002 |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | P002, P003, P005 |
| `{{materials.tools}}` | `materials.tools[]` | P003 |
| `{{materials.consumables}}` | `materials.consumables[]` | P003 |
| `{{preparationSteps}}` | `preparationSteps[]` | P004 |
| `{{paintSequence}}` | `paintSequence[]` | P005 |
| `{{maskingZones}}` | `maskingZones[]` | P006 |
| `{{detailAreas}}` | `detailAreas[]` | P007 |
| `{{decals}}` | `decals[]` | P008 |
| `{{premiumVariant.name}}` | `premiumVariant.name` | P009 |
| `{{premiumVariant.additionalMaterials}}` | `premiumVariant.additionalMaterials[]` | P009 |
| `{{premiumVariant.specialTechniques}}` | `premiumVariant.specialTechniques[]` | P009 |
| `{{paths.coverRenderPath}}` | `paths.coverRenderPath` | P001 |
| `{{paths.colorSchemeRenderFront}}` | `paths.colorSchemeRenderFront` | P002 |
| `{{paths.colorSchemeRenderSide}}` | `paths.colorSchemeRenderSide` | P002 |
| `{{paths.colorSchemeRenderTop}}` | `paths.colorSchemeRenderTop` | P002 |

---

## Model Compatibility

Prompts are written in plain instructional English. They must work without modification on:

- OpenAI GPT-4 / GPT-4o ✓ (verified)
- Anthropic Claude (any version) ✓ (verified)
- Google Gemini ⚠️ (Phase 4 only, single-illustration generation ✓ — see `UAT/UAT-004.md`; failed UAT-002 for old whole-page Phase 3/4 scope, and Phase 1-3 text/bootstrap remain unverified)
- Meta Llama (via API) — untested
- Mistral / Mixtral — untested
- Any future model — untested

**Never** include model-specific syntax inside prompt templates:
- No `[INST]...[/INST]` (Llama format)
- No `<|im_start|>` (ChatML format)
- No system/user JSON wrappers
- No model-specific parameters or flags

The AI model's interface (system prompt, temperature, etc.) is configured by the user at runtime, not by the SDK.

---

## Extending the Prompt Engine

To add a new page prompt (e.g., P011 for a new page type):

1. Define the page in `Core/PAGE_SYSTEM.md` with its permanent ID (P011).
2. Create `PromptEngine/NewPageName.md` following the exact structure of existing prompt files.
3. Add the file to the table in this README.
4. Add all new tokens to the Master Token Reference table above.
5. Update `Core/CHANGELOG.md` with a minor version bump.

**Never modify existing prompt files in ways that break backward compatibility.** If a structural change is needed, create a versioned variant (e.g., `Cover_v2.md`) and document the migration in `Core/WORKFLOW.md`.

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Forgetting to substitute `{{tokens}}` before sending | AI generates with literal placeholder text | Always substitute all tokens before use |
| Substituting partial tokens | Broken output with `{{project.` fragments | Use regex to catch all `{{...}}` patterns |
| Using model-specific syntax in templates | Prompt breaks on other AI models | Write plain English only in templates |
| Editing prompt files instead of copying | Upstream changes are lost | Always copy to a scratch file for editing |
| Adding design rules to prompts | Specs duplicate Core/ and diverge | Reference Core/ documents by section |

---

## Dependencies

| Document | Role |
|----------|------|
| `Core/PAGE_SYSTEM.md` | Defines page IDs, inputs, outputs, and component requirements |
| `Core/COMPONENT_SYSTEM.md` | Defines C001–C015 component specs referenced in prompts |
| `Core/STYLE_GUIDE.md` | Defines palette, typography, spacing used in layouts |
| `Core/RENDER_GUIDE.md` | Defines render angles, lighting, and resolution requirements |
| `Core/QA_SYSTEM.md` | Defines validation checklists referenced at end of each prompt |
| `Templates/PROJECT.yaml` | Source of all `{{token}}` values |

---

*PromptEngine is part of Mini4WD Manual SDK v2.4.0. See `Core/WORKFLOW.md` for the complete generation pipeline.*

---

## v2.3.0 — LOAD Sequence (Mandatory)

As of SDK v2.3.0, every prompt must begin with a LOAD sequence that injects the full framework context. This replaces ad-hoc context injection and ensures consistent AI behavior across all models.

### LOAD Sequence Definition

```
╔══════════════════════════════════════════════════════╗
║         MINI4WD MANUAL SDK — LOAD SEQUENCE          ║
╠══════════════════════════════════════════════════════╣
║  STEP 1  │  LOAD Core/DESIGN_LANGUAGE.md            ║
║  STEP 2  │  LOAD Core/COMPONENT_SYSTEM.md           ║
║  STEP 3  │  LOAD Assets/DesignSystem/Tokens/        ║
║          │        tokens.example.yaml               ║
║  STEP 4  │  LOAD Core/TEXT_ENGINE.md                ║
║  STEP 5  │  LOAD Config/LANGUAGE_POLICY.yaml        ║
║  STEP 6  │  LOAD Core/AI_OPERATING_RULES.md         ║
║  STEP 7  │  LOAD Projects/{ModelName}/PROJECT.yaml  ║
║  STEP 8  │  GENERATE: [page-specific instruction]   ║
╚══════════════════════════════════════════════════════╝
```

### Why This Order Matters

1. **DESIGN_LANGUAGE** first — establishes editorial philosophy before any specifics
2. **COMPONENT_SYSTEM** second — defines the visual vocabulary available
3. **TOKENS** third — provides concrete visual values
4. **TEXT_ENGINE** fourth — establishes text authorship rules before language policy
5. **LANGUAGE_POLICY** fifth — enforces Italian-only AFTER text rules are loaded
6. **AI_OPERATING_RULES** sixth — applies all 102 rules as hard constraints
7. **PROJECT.yaml** seventh — injects project-specific data
8. **GENERATE** last — only after all context is loaded

### How to Use in Practice

**For ChatGPT / Claude / Gemini (conversational injection):**

Paste this preamble before each page prompt:

```
[CONTEXT LOAD — Mini4WD Manual SDK v2.4.0]

You are an AI model operating within the Mini4WD Manual SDK editorial pipeline.
Before generating any content, internalize the following constraints:

1. DESIGN PHILOSOPHY: The manual aesthetically references Tamiya technical catalogs.
   The visual style is Japanese-influenced. The editorial content is entirely Italian.
   Never confuse visual aesthetic with language. No Japanese text — ever.

2. LANGUAGE POLICY (Config/LANGUAGE_POLICY.yaml):
   - Primary language: Italian (it) — all body text, headings, labels, warnings, tips
   - Forbidden: Japanese (kanji, hiragana, katakana), English paragraphs, Lorem ipsum
   - Accepted exceptions: paint codes (TS-57), airbrush, spray, primer (in italic)
   - Approved placeholders when data missing: [TITOLO], [TESTO], [SOTTOTITOLO]

3. TEXT ENGINE RULES (Core/AI_OPERATING_RULES.md — RULES 059–100):
   - Text is editorial content, not decoration
   - Never invent paint codes, colors, or materials not in PROJECT.yaml
   - Never generate fake text, random characters, or pseudo-Japanese
   - Instructions use second-person singular imperative in Italian

4. COMPONENT SYSTEM: Use only approved components C001–C015.
   C001 Header and C002 Footer mandatory on every page.

5. DESIGN TOKENS: All visual values from tokens.example.yaml.
   TamiyaPrimary #114B69, White #FFFFFF, DarkGray #4A4A4A.

[PROJECT DATA]
Model: {{project.modelName}}
Language: {{project.language}}
Paint Scheme: {{project.paintScheme.name}}
[...remaining PROJECT.yaml fields...]

[GENERATE]
```

### Text-Mode vs Render-Mode Prompts

**Text-mode prompts (Phase 2a — Text Engine):**
- Generate ONLY Italian editorial text
- Output structured Markdown per `Templates/APPROVED_TEXT.md` format
- No visual layout descriptions
- No color hex values
- No component dimensions

**Render-mode prompts (Phase 3 — Render Engine):**
- Load ApprovedText/P{NNN}.md as source
- Generate visual layout description using text from ApprovedText/
- All text content from ApprovedText/ — verbatim, no rewrite
- Describe component placement, sizes, visual relationships

### Updated Token Reference Table

| Token | Source | Page(s) |
|-------|--------|---------|
| `{{project.modelName}}` | PROJECT.yaml | All |
| `{{project.language}}` | PROJECT.yaml | All (must be "it") |
| `{{project.paintScheme.name}}` | PROJECT.yaml | P001, P002 |
| `{{project.paintScheme.colors[N].paintCode}}` | PROJECT.yaml | P002, P003 |
| `{{project.paintScheme.colors[N].name}}` | PROJECT.yaml | P002 |
| `{{project.paintScheme.colors[N].finish}}` | PROJECT.yaml | P002 |
| `{{project.preparationSteps[N].title}}` | PROJECT.yaml | P004 |
| `{{project.preparationSteps[N].description}}` | PROJECT.yaml | P004 |
| `{{project.preparationSteps[N].duration}}` | PROJECT.yaml | P004 |
| `{{project.paintSequence[N].area}}` | PROJECT.yaml | P005 |
| `{{project.paintSequence[N].colorId}}` | PROJECT.yaml | P005 |
| `{{project.maskingZones[N].area}}` | PROJECT.yaml | P006 |
| `{{project.decals[N].name}}` | PROJECT.yaml | P008 |
| `{{project.decals[N].position}}` | PROJECT.yaml | P008 |
| `{{project.premiumVariant.name}}` | PROJECT.yaml | P009 |
| `{{token.TamiyaPrimary}}` | tokens.example.yaml | All (render) |
| `{{token.HeaderHeight}}` | tokens.example.yaml | C001 (render) |

---

## v2.4.0 — content.yaml Generation Mode

*Added SDK v2.4.0. Text Engine now outputs structured YAML instead of Markdown.*

### Updated LOAD Sequence (v2.4.0)

```
╔══════════════════════════════════════════════════════╗
║         MINI4WD MANUAL SDK — LOAD SEQUENCE v2.4.0   ║
╠══════════════════════════════════════════════════════╣
║  STEP 1  │  LOAD Core/DESIGN_LANGUAGE.md            ║
║  STEP 2  │  LOAD Core/COMPONENT_SYSTEM.md           ║
║  STEP 3  │  LOAD Assets/DesignSystem/Tokens/        ║
║          │        tokens.example.yaml               ║
║  STEP 4  │  LOAD Core/TEXT_ENGINE.md                ║
║  STEP 5  │  LOAD Config/LANGUAGE_POLICY.yaml        ║
║  STEP 6  │  LOAD Core/AI_OPERATING_RULES.md         ║
║  STEP 7  │  LOAD Projects/{ModelName}/PROJECT.yaml  ║
║  STEP 8  │  (if updating) LOAD content.yaml         ║
║  STEP 9  │  GENERATE                                ║
╚══════════════════════════════════════════════════════╝
```

**Step 8 is new in v2.4.0.** Load the existing `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml` when updating (not generating fresh). Preserves prior approved content; only modifies declared fields.

### Text-Mode vs Render-Mode (v2.4.0 update)

**Text-mode prompts (Phase 2a — content.yaml output):**
- Generate structured YAML conforming to page content.yaml schema
- Output saved to `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml` ← PRIMARY
- text.md auto-derived from content.yaml — do not generate separately
- Field names: English. Field values: Italian
- No visual layout. No hex values. No component dimensions.

**Render-mode prompts (Phase 3 — Render Engine):**
- Load `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml` as source (not text.md)
- Read approved field values verbatim — no rewrite, no paraphrase
- Generate visual layout description using those values
- Render Engine never reads PROJECT.yaml directly (v2.4.0 change)

### Field Name vs Field Value Distinction

Critical rule: content.yaml field **names** are English (structural keys). Field **values** are Italian (editorial content).

```yaml
# CORRECT
title: "Campione dell'Imperatore"
subtitle: "Manuale di verniciatura"
footer:
  model_name: "Emperor Emperor Special"

# WRONG — Italian field names
titolo: "Campione dell'Imperatore"
```

### content.yaml Schema (per page)

Each page has a defined schema. Prompt files for individual pages (Cover.md, ColorScheme.md, etc.) specify required and optional fields. All text values: Italian. All placeholder values: use `[TITOLO]`, `[TESTO]`, `[SOTTOTITOLO]` — never invent data.

### Approved Assets Sealing (Phase 2d)

After text generation and QA:
1. Set `metadata.yaml §status: "approved"`
2. Set `metadata.yaml §approved_by` and `§approved_date`
3. Optional: set `metadata.yaml §locked: true` for production freeze
4. Update `Projects/{Modello}/{Variante}/index.yaml`
5. Log in `changelog.md`

Render Engine may only begin after sealing.
