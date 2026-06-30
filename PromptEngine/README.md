# PromptEngine

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
6. Save the AI output to `Projects/{ModelName}/Output/raw/P001_raw.md` (or appropriate page ID).
7. Run QA against `Core/QA_SYSTEM.md`.

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

- OpenAI GPT-4 / GPT-4o
- Anthropic Claude (any version)
- Google Gemini
- Meta Llama (via API)
- Mistral / Mixtral
- Any future model

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

*PromptEngine is part of Mini4WD Manual SDK v2.1.0. See `Core/WORKFLOW.md` for the complete generation pipeline.*
