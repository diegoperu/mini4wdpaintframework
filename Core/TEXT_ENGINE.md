# Text Engine

**Document ID:** CORE-TXT-001
**SDK Version:** 2.3.0
**Status:** Stable — Mandatory
**Replaces:** (none — new document)
**Referenced by:** Build/Pipeline.md, Core/WORKFLOW.md, PromptEngine/README.md, Core/COMPONENT_SYSTEM.md

---

## Overview

The Text Engine is the editorial subsystem of the Mini4WD Manual SDK. It is responsible for producing all written content — page titles, step descriptions, callout text, warnings, paint sequence labels, material lists, notes — independently of any visual rendering process.

**Core principle:** Text is not decoration. Text is editorial content with identity, language, tone, and authorship. It must be validated before it enters any visual pipeline.

**Architecture position:**

```
PROJECT.yaml + Knowledge/
        ↓
   TEXT ENGINE          ← THIS DOCUMENT
        ↓
  Editorial QA (Tests/TextValidation.md)
        ↓
  ApprovedText/ (P001.md → P010.md)
        ↓
   RENDER ENGINE
        ↓
    Page QA
```

The Render Engine never generates text. It only places pre-approved text into visual layouts.

---

## Philosophy

### Text has identity

Every piece of text in a Mini4WD manual belongs to a specific editorial context: an Italian technical manual for a hobbyist painter. It is not a translation exercise. It is not a placeholder. It is not a simulation of another language.

### Separation of concerns

Text generation and visual rendering are fundamentally different tasks requiring different validation criteria. By separating them, the SDK ensures that:

- Text quality is independently verifiable
- Language compliance is enforced before rendering
- Renders cannot contain invented or incorrect text
- AI models can focus on one task at a time

### Validated text as single source of truth

Once text passes Editorial QA, it becomes the sole authoritative source for all visual pages. The Render Engine treats approved text as read-only input — it does not paraphrase, translate, or abbreviate.

---

## Responsibilities

The Text Engine is responsible for:

1. Receiving all data from `PROJECT.yaml`
2. Querying `Knowledge/` documents for technical terminology
3. Generating all text content for pages P001–P010
4. Enforcing language policy per `Config/LANGUAGE_POLICY.yaml`
5. Producing structured Markdown files (P001.md–P010.md)
6. Submitting output to Editorial QA (`Tests/TextValidation.md`)
7. Storing approved text in `Projects/{ModelName}/ApprovedText/`

The Text Engine is NOT responsible for:

- Visual layout
- Color choices
- Render angles
- Component dimensions
- PDF export

---

## Inputs

| Source | Field / Document | Usage |
|--------|-----------------|-------|
| `PROJECT.yaml` | `project.modelName` | Page titles, cover, footer |
| `PROJECT.yaml` | `project.language` | Language enforcement |
| `PROJECT.yaml` | `paintScheme.colors[]` | Color name labels, paint sequence |
| `PROJECT.yaml` | `preparationSteps[]` | Step descriptions P004 |
| `PROJECT.yaml` | `paintSequence[]` | Step descriptions P005 |
| `PROJECT.yaml` | `maskingZones[]` | Zone descriptions P006 |
| `PROJECT.yaml` | `detailAreas[]` | Detail descriptions P007 |
| `PROJECT.yaml` | `decals[]` | Decal placement descriptions P008 |
| `PROJECT.yaml` | `premiumVariant` | Premium page content P009 |
| `Knowledge/Glossary.md` | All entries | Terminology consistency |
| `Knowledge/GlossaryIT.md` | All entries | Italian terminology |
| `Knowledge/Terminology.md` | All entries | Technical term standardization |
| `Config/LANGUAGE_POLICY.yaml` | All fields | Language enforcement |

---

## Outputs

The Text Engine produces one Markdown file per page, stored in `Projects/{ModelName}/ApprovedText/`:

| File | Page | Contents |
|------|------|---------|
| `P001.md` | Cover | Title, subtitle, scheme name, series |
| `P002.md` | Color Scheme | Color names, paint codes, finish labels, notes |
| `P003.md` | Materials | Paint list, tool list, consumables, safety notes |
| `P004.md` | Preparation | Step titles, step descriptions, tips, warnings |
| `P005.md` | Painting | Step sequence, color assignments, drying time notes |
| `P006.md` | Masking | Zone descriptions, masking order, technique notes |
| `P007.md` | Details | Detail area descriptions, color assignments, technique |
| `P008.md` | Decals | Decal names, placement instructions, softener notes |
| `P009.md` | Premium Variant | Premium scheme name, additional technique descriptions |
| `P010.md` | Final Checklist | Checklist items, care instructions, completion note |

### Output File Format

Each ApprovedText file uses structured Markdown with YAML frontmatter:

```
---
page_id: P001
model: Proto Emperor
language: it
version: 1.0.0
approved: false
approved_by: ""
approved_date: ""
sdk_version: 2.3.0
---
```

The `approved` field is set to `true` only after passing `Tests/TextValidation.md`.

---

## Workflow

### Step 1 — Initialize

1. Verify `PROJECT.yaml` is complete (all required fields non-empty)
2. Load `Config/LANGUAGE_POLICY.yaml`
3. Load relevant `Knowledge/` documents
4. Copy `Templates/APPROVED_TEXT.md` template to `Projects/{ModelName}/ApprovedText/`

### Step 2 — Generate Text (via PromptEngine)

For each page P001–P010:

1. Open `PromptEngine/{PageName}.md`
2. Resolve all `{{token}}` values from PROJECT.yaml
3. Inject the LOAD sequence (see `PromptEngine/README.md §Load Sequence`)
4. Submit to AI model — text-only generation, no visual description
5. Save raw text output to `Projects/{ModelName}/ApprovedText/raw/P{NNN}_raw.md`

### Step 3 — Editorial QA

Run `Tests/TextValidation.md` checklist against each raw text file.

### Step 4 — Approval

For each page that passes all TextValidation checks:

1. Set `approved: true` in YAML frontmatter
2. Set `approved_by` and `approved_date`
3. Save final file to `Projects/{ModelName}/ApprovedText/P{NNN}.md`

### Step 5 — Hand-off to Render Engine

Render Engine reads only from `ApprovedText/` — never from raw output.

---

## Integration with Prompt Engine

Prompts in `PromptEngine/` use the LOAD sequence as their first instruction block:

```
LOAD Core/DESIGN_LANGUAGE.md
LOAD Core/COMPONENT_SYSTEM.md
LOAD Assets/DesignSystem/Tokens/tokens.example.yaml
LOAD Core/TEXT_ENGINE.md          ← NEW in v2.3.0
LOAD Config/LANGUAGE_POLICY.yaml  ← NEW in v2.3.0
LOAD Core/AI_OPERATING_RULES.md
LOAD Projects/{ModelName}/PROJECT.yaml
GENERATE: [page-specific instruction]
```

Text-mode prompts (Text Engine phase) instruct the AI to produce only written content, in Italian, following the Typography Rules in `Core/STYLE_GUIDE.md §Typography Rules`.

---

## Integration with Render Engine

The Render Engine receives ApprovedText files as read-only input:

1. It reads `ApprovedText/P{NNN}.md`
2. It extracts text sections using the structured Markdown format
3. It places text into the correct visual components (C001–C015)
4. It does NOT generate, paraphrase, or translate any text

If a text section is missing from ApprovedText, the Render Engine uses these approved placeholders:

- `[TITOLO]` for missing titles
- `[SOTTOTITOLO]` for missing subtitles
- `[TESTO]` for missing body text

It never invents text.

---

## QA

Text quality is verified in `Tests/TextValidation.md` with these primary checks:

1. **Language:** all text is Italian (zero tolerance for other languages)
2. **Completeness:** no `{{token}}` placeholders remaining
3. **No fake text:** no lorem ipsum, kanji, hiragana, katakana, random characters
4. **Terminology consistency:** terms match `Knowledge/GlossaryIT.md`
5. **Tone compliance:** text follows `Knowledge/EditorialStyle.md`
6. **Approved flag:** YAML frontmatter `approved: true` set before hand-off

---

## Examples

### Correct — P004 step text (Italian, technical, imperative)

```markdown
## Passo 1 — Pulizia

Rimuovi la carrozzeria dallo sprue utilizzando le tronchesi. Elimina i gate
con un coltello da modellismo. Lava la superficie con acqua tiepida e sapone
neutro. Asciuga con aria compressa.

**Durata stimata:** 15 minuti
**Attenzione:** Non toccare la superficie con le mani dopo il lavaggio.
```

### Incorrect — language violation

```
## Step 1 — Cleaning           ← INGLESE — RIFIUTATO
Wash the body with soapy water. ← INGLESE — RIFIUTATO
```

### Incorrect — fake text

```
## Fase 1
Lorem ipsum dolor sit amet.    ← LOREM — RIFIUTATO
```

### Correct — placeholder when data missing

```markdown
## [TITOLO]
[TESTO]
<!-- MISSING: project.preparationSteps[0].title — aggiungere in PROJECT.yaml -->
```

---

## Dependencies

| Document | Dependency Type |
|----------|----------------|
| `Config/LANGUAGE_POLICY.yaml` | Runtime constraint |
| `Core/AI_OPERATING_RULES.md §TEXT RENDERING RULES` | Behavioral constraint |
| `Core/STYLE_GUIDE.md §Typography Rules` | Style constraint |
| `Knowledge/GlossaryIT.md` | Terminology reference |
| `Knowledge/EditorialStyle.md` | Tone and register |
| `Knowledge/Terminology.md` | Technical terms |
| `Knowledge/ForbiddenWords.md` | Forbidden vocabulary |
| `Tests/TextValidation.md` | QA protocol |
| `PromptEngine/README.md` | Prompt integration |
| `Templates/APPROVED_TEXT.md` | Output template |

---

## Related Documents

- `Build/Pipeline.md` — full pipeline context
- `Core/WORKFLOW.md` — workflow overview
- `Core/COMPONENT_SYSTEM.md` — text placement in components
- `PromptEngine/README.md` — LOAD sequence
- `Config/LANGUAGE_POLICY.yaml` — language rules
- `Tests/TextValidation.md` — QA checklist
