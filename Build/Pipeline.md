# Production Pipeline

**SDK Version:** 2.2.0
**Document ID:** BUILD-001
**Status:** Stable
**Dependencies:** `Core/WORKFLOW.md`, `Core/QA_SYSTEM.md`, `Core/PDF_MASTER.md`, `Config/sdk.yaml`

---

## Overview

The Mini4WD Manual SDK production pipeline transforms a `PROJECT.yaml` configuration into a published, QA-approved PDF manual. The pipeline has 8 sequential phases. Each phase has defined inputs, outputs, validation criteria, and a responsible actor.

```
┌─────────────────────────────────────────────────────────────┐
│           Mini4WD Manual SDK — Production Pipeline          │
├─────────┬───────────────────────────────────────────────────┤
│ Phase 0 │  Project Setup        PROJECT.yaml + references   │
│ Phase 1 │  Reference Models     Photography & source art    │
│ Phase 2 │  Prompt Engine        AI prompt execution         │
│ Phase 3 │  Render Engine        AI illustration generation  │
│ Phase 4 │  QA                   110-item checklist          │
│ Phase 5 │  PDF Generation       Screen + print export       │
│ Phase 6 │  Approved Manual      Archive & publication       │
│ Phase 7 │  Release              Version tag + changelog     │
└─────────┴───────────────────────────────────────────────────┘
```

---

## Phase 0 — Project Setup

**Purpose:** Initialize all project data before any generation begins.

**Actor:** Manual author

**Input:**
- `Templates/PROJECT.yaml` (source template)
- Official Tamiya model name and product code
- Paint scheme concept

**Process:**
1. Copy `Templates/PROJECT.yaml` → `Projects/{ModelName}/PROJECT.yaml`
2. Fill all REQUIRED fields (see schema comments in template)
3. Copy `Templates/COLOR_SCHEME.yaml` → `Projects/{ModelName}/COLOR_SCHEME.yaml`
4. Fill color scheme fields including real Tamiya/Mr.Hobby paint codes
5. Copy `Templates/CHECKLIST.md` → `Projects/{ModelName}/Notes/CHECKLIST.md`
6. Validate PROJECT.yaml against `Config/sdk.yaml` schema rules

**Output:**
- `Projects/{ModelName}/PROJECT.yaml` (complete)
- `Projects/{ModelName}/Notes/CHECKLIST.md` (initialized)

**Validation:**
- All REQUIRED fields present and non-empty
- `modelSlug` matches kebab-case pattern `^[a-z0-9-]+$`
- `year` is a valid 4-digit year
- `paintScheme.colors` array has at least 1 entry
- `paths.coverRenderPath` value is a valid relative path

**Exit Criteria:** PROJECT.yaml passes `Config/quality.yaml` schema validation.

**Common Errors:**
- Leaving placeholder text in required fields
- Using spaces in `modelSlug` instead of hyphens
- Specifying paint codes that don't exist — see `Knowledge/Paints.md`

---

## Phase 1 — Reference Models

**Purpose:** Gather all visual source material needed to generate renders and illustrations.

**Actor:** Manual author

**Input:**
- Physical model or official photography
- Tamiya box art (if available and licensed)
- Official render references

**Process:**
1. Create `Assets/ReferenceModels/{ModelName}/` directory
2. Photograph model from all required angles (see `Assets/ReferenceModels/README.md` §Required Angles)
3. Name files per `Core/NAMING_CONVENTION.md`
4. Validate images meet minimum resolution (800×600px)
5. Add reference listing to `Assets/ReferenceModels/{ModelName}/README.md`

**Output:**
- `Assets/ReferenceModels/{ModelName}/reference_front.jpg`
- `Assets/ReferenceModels/{ModelName}/reference_side.jpg`
- `Assets/ReferenceModels/{ModelName}/reference_top.jpg`
- `Assets/ReferenceModels/{ModelName}/README.md`

**Validation:**
- Minimum 3 reference images present (front, side, top)
- All images ≥ 800×600px
- Pure white or neutral gray background (no cluttered environments)
- No watermarks

**Exit Criteria:** All required reference images approved and filed.

---

## Phase 2 — Prompt Engine

**Purpose:** Execute page generation prompts against the AI model of choice.

**Actor:** Manual author + AI model

**Input:**
- `Projects/{ModelName}/PROJECT.yaml` (Phase 0 output)
- `PromptEngine/{PageName}.md` (one per page)
- `Assets/DesignSystem/Tokens/tokens.example.yaml` (design token values)

**Process:**

For each page P001–P010:
1. Open `PromptEngine/{PageName}.md`
2. Substitute all `{{token}}` placeholders with values from PROJECT.yaml
3. Verify no `{{placeholder}}` remains before submitting
4. Submit resolved prompt to AI model
5. Review output against page spec in `Core/PAGE_SYSTEM.md`
6. Save raw output to `Projects/{ModelName}/Output/raw/P{NNN}_raw.md`

**Token Substitution Reference:** See `PromptEngine/README.md §Token Reference Table`

**AI Model Compatibility:** Prompts are model-agnostic. Compatible with ChatGPT, Claude, Gemini, and any instruction-following LLM. See `Core/AI_OPERATING_RULES.md` for AI behavior constraints.

**Output:**
- `Projects/{ModelName}/Output/raw/P001_raw.md` through `P010_raw.md`

**Validation:**
- No unresolved `{{token}}` strings in output
- All required components present per `Core/PAGE_SYSTEM.md`
- AI has not invented paint codes not in PROJECT.yaml — see `Core/AI_OPERATING_RULES.md §Rule 1`

**Exit Criteria:** All 10 raw pages generated and spot-checked.

---

## Phase 3 — Render Engine

**Purpose:** Generate all visual illustrations for the manual.

**Actor:** Manual author + AI image generation model

**Input:**
- `Assets/ReferenceModels/{ModelName}/` (Phase 1 output)
- `Core/RENDER_GUIDE.md` (angle, lighting, resolution specs)
- `Projects/{ModelName}/PROJECT.yaml` (paint scheme)

**Process:**

For each required render:
1. Select lighting rig from `Core/RENDER_GUIDE.md §3`
2. Select camera angle from `Core/RENDER_GUIDE.md §2`
3. Build render prompt using `Core/RENDER_GUIDE.md §6` template
4. Generate render with AI image model
5. Validate render against `Core/RENDER_GUIDE.md §7` checklist
6. Place approved render in `Projects/{ModelName}/Images/`

**Required Renders Per Manual:**

| Page | File | Angle | Lighting |
|------|------|-------|----------|
| P001 | `cover_3q.png` | 3/4 front-left, 15° elevation | Studio Neutral |
| P002 | `P002_front.png` | Orthographic front | Studio Neutral |
| P002 | `P002_side.png` | Orthographic right | Studio Neutral |
| P002 | `P002_top.png` | Orthographic top | Studio Neutral |
| P005 | `P005_step_{n}.png` | 3/4 front-left | Detail rig |
| P006 | `P006_masking_{n}.png` | Area-specific close-up | Detail rig |
| P007 | `P007_detail_{n}.png` | Close-up 45° | Detail rig |

**Output:**
- `Projects/{ModelName}/Images/` (all approved renders)

**Validation:**
- Background pure white (#FFFFFF) — no exceptions
- Resolution meets minimums per `Core/RENDER_GUIDE.md §5`
- No motion blur, artifacts, or background remnants
- Paint finish matches `paintScheme.colors[].finish`

**Exit Criteria:** All required renders in Images/ and individually validated.

---

## Phase 4 — QA

**Purpose:** Systematic quality verification across all generated pages and renders.

**Actor:** Manual author (QA reviewer)

**Input:**
- `Projects/{ModelName}/Output/raw/` (Phase 2 output)
- `Projects/{ModelName}/Images/` (Phase 3 output)
- `Core/QA_SYSTEM.md` (110-item checklist)

**Process:**
1. Open `Core/QA_SYSTEM.md`
2. For each QA item, verify against generated output
3. Document results in `Projects/{ModelName}/Notes/qa_log.md`
4. For failed items: return to responsible phase, fix, re-verify
5. Iterate until all items pass

**QA Log Format:**
```
# QA Log — {ModelName} v{version}
Date: YYYY-MM-DD
Reviewer: {name}

## Pass
- QA-001: ✅
- QA-002: ✅

## Fail (Iteration 1)
- QA-047: ❌ — Background not pure white in P002_side.png → return to Phase 3

## Final Status: PASSED / FAILED
```

**Output:**
- `Projects/{ModelName}/Notes/qa_log.md` (completed)

**Exit Criteria:** Zero failures in `qa_log.md`. Reviewer signs off.

**Blocking Failures (must fix before proceeding):**
- Any render with non-white background (`QA-017`)
- Any page missing C001 Header (`QA-061`)
- Any unresolved `{{token}}` in output (`QA-071`)
- Resolution below minimums (`QA-018`)

---

## Phase 5 — PDF Generation

**Purpose:** Export final paginated PDF in screen and print variants.

**Actor:** Manual author

**Input:**
- Approved pages from Phase 4
- `Templates/PDF_CONFIG.yaml` (export settings)
- `Core/PDF_MASTER.md` (export specification)

**Process:**
1. Copy `Templates/PDF_CONFIG.yaml` → `Projects/{ModelName}/pdf_config.yaml`
2. Fill metadata fields (title, author, keywords)
3. Arrange pages in order: P001–P010
4. Export screen variant (sRGB, 150dpi, no bleed) → `Output/manual_screen.pdf`
5. Export print variant (CMYK FOGRA39, 300dpi, 3mm bleed) → `Output/manual_print.pdf`
6. Verify PDF metadata, bookmarks, font embedding per `Core/PDF_MASTER.md`
7. Generate SHA-256 checksum for each PDF

**Supported Export Tools:** Affinity Publisher, Adobe InDesign, Scribus, pandoc+LaTeX. See `Core/PDF_MASTER.md §Export Tools`.

**Output:**
- `Projects/{ModelName}/Output/manual_screen.pdf`
- `Projects/{ModelName}/Output/manual_print.pdf`
- `Projects/{ModelName}/Output/checksums.sha256`

**Validation:**
- PDF metadata complete (title, author, keywords, creator)
- All bookmarks present (P001–P010)
- All fonts embedded
- Bleed correct per variant (0mm screen, 3mm print)

**Exit Criteria:** Both PDF variants generated, validated, and checksummed.

---

## Phase 6 — Approved Manual

**Purpose:** Archive the approved, publication-ready manual.

**Actor:** Manual author + project maintainer

**Input:**
- Phase 4 approved pages
- Phase 5 PDFs and checksums

**Process:**
1. Create `Assets/ApprovedManual/{ModelName}/` directory
2. Copy approved pages P001.png–P010.png
3. Copy `manual_screen.pdf`, `manual_print.pdf`, `checksums.sha256`
4. Copy `Projects/{ModelName}/PROJECT.yaml` as snapshot
5. Copy `Projects/{ModelName}/Notes/qa_log.md`
6. Create `Assets/ApprovedManual/{ModelName}/README.md` with approval metadata
7. Maintainer reviews and countersigns README

**Output:**
- `Assets/ApprovedManual/{ModelName}/` (complete approved package)

**Approval Record (`README.md`):**
```markdown
# Approved Manual: {ModelName}
**Manual Version:** {version}
**SDK Version:** 2.2.0
**Approved:** YYYY-MM-DD
**Reviewer:** {name}
**QA Log:** qa_log.md
**Status:** APPROVED
```

**Exit Criteria:** Maintainer has reviewed and README contains approval signature.

---

## Phase 7 — Release

**Purpose:** Version the approved manual and publish the release record.

**Actor:** Project maintainer

**Input:**
- Phase 6 approved package
- `CHANGELOG.md`

**Process:**
1. Tag release in version control: `git tag v{manualVersion}-{modelSlug}`
2. Update `CHANGELOG.md` with new manual entry
3. If SDK changes were made: bump SDK `VERSION`, update `CHANGELOG.md`
4. Push tag and changelog to remote

**Output:**
- Git tag
- Updated `CHANGELOG.md`

**Exit Criteria:** Tag pushed, CHANGELOG updated.

---

## Pipeline Decision Points

```
Phase 0 → Setup complete?
  NO  → Fix PROJECT.yaml → retry Phase 0
  YES → Phase 1

Phase 1 → References approved?
  NO  → Reshoot / relicense → retry Phase 1
  YES → Phase 2 + Phase 3 (can run in parallel)

Phase 2+3 → Pages and renders ready?
  NO  → Fix and regenerate failing items
  YES → Phase 4

Phase 4 → QA passed?
  NO  → Identify failing phases → return to Phase 2 or 3
  YES → Phase 5

Phase 5 → PDF valid?
  NO  → Fix export config → retry Phase 5
  YES → Phase 6

Phase 6 → Maintainer approved?
  NO  → Return to failing phase
  YES → Phase 7
```

---

## Related Documents
- `Core/WORKFLOW.md` — high-level workflow overview
- `Core/QA_SYSTEM.md` — Phase 4 detail
- `Core/PDF_MASTER.md` — Phase 5 detail
- `Core/RENDER_GUIDE.md` — Phase 3 detail
- `Core/AI_OPERATING_RULES.md` — Phase 2 constraints
- `Config/sdk.yaml` — runtime configuration
- `Config/quality.yaml` — validation rules and thresholds
- `PromptEngine/README.md` — Phase 2 prompt usage guide
- `Assets/ApprovedManual/README.md` — Phase 6 governance
- `Tests/README.md` — validation protocols per phase

---

## v2.3.0 — Extended Pipeline with Text Engine

As of SDK v2.3.0, the pipeline includes dedicated Text Engine phases between Project Setup and Render Engine. The updated sequence:

```
┌─────────────────────────────────────────────────────────────────┐
│         Mini4WD Manual SDK — Full Pipeline v2.3.0              │
├─────────┬───────────────────────────────────────────────────────┤
│ Phase 0 │ Project Setup        PROJECT.yaml + references        │
│ Phase 1 │ Reference Models     Photography & source art         │
│ Phase 2 │ Knowledge Load       Terminology, style, glossary     │
│ Phase 2a│ Text Engine          Italian editorial content        │
│ Phase 2b│ Editorial QA         Tests/TextValidation.md          │
│ Phase 2c│ Approved Text        ApprovedText/ P001–P010           │
│ Phase 3 │ Render Engine        AI illustration generation        │
│ Phase 4 │ Page QA              QA_SYSTEM.md 110-item checklist  │
│ Phase 5 │ PDF Generation       Screen + print + archive         │
│ Phase 6 │ Approved Manual      Archive & publication            │
│ Phase 7 │ Release              Version tag + changelog          │
└─────────┴───────────────────────────────────────────────────────┘
```

### Phase 2 — Knowledge Load (NEW in v2.3.0)

**Purpose:** Load all editorial reference material before text generation.

**Input:**
- `Knowledge/GlossaryIT.md`
- `Knowledge/EditorialStyle.md`
- `Knowledge/Terminology.md`
- `Knowledge/ForbiddenWords.md`
- `Config/LANGUAGE_POLICY.yaml`

**Process:** Inject relevant Knowledge/ sections as context into the Text Engine prompts. This ensures terminology consistency and language compliance without relying on the AI's internal knowledge.

**Output:** Knowledge context ready for Text Engine prompts.

### Phase 2a — Text Engine (NEW in v2.3.0)

**Purpose:** Generate all Italian editorial content for P001–P010, decoupled from visual rendering.

**Actor:** Manual author + AI model (text-only mode)

**Input:**
- `Projects/{ModelName}/PROJECT.yaml`
- `PromptEngine/{PageName}.md` (LOAD sequence preamble)
- Knowledge context from Phase 2

**Process:**
1. For each page P001–P010, run text-mode prompt from PromptEngine/
2. The prompt uses the full LOAD sequence (see `PromptEngine/README.md §Load Sequence`)
3. Generate Italian text content only — no visual layout descriptions
4. Save raw output to `Projects/{ModelName}/ApprovedText/raw/P{NNN}_raw.md`

**Output:** Raw Italian text files in ApprovedText/raw/

### Phase 2b — Editorial QA (NEW in v2.3.0)

**Purpose:** Validate text quality before it enters the Render Engine.

**Actor:** Manual author (editor role)

**Input:** `ApprovedText/raw/P{NNN}_raw.md` files
**Reference:** `Tests/TextValidation.md`

**Process:**
1. Run all TEST-TX checks against each raw text file
2. Fix any blocking failures (language violations, fake text, unresolved tokens)
3. Document non-blocking warnings in qa_log.md
4. Iterate until all blocking checks pass

**Output:** Verified text ready for approval.

### Phase 2c — Approved Text (NEW in v2.3.0)

**Purpose:** Seal approved text as the authoritative source for rendering.

**Actor:** Manual author

**Process:**
1. Set `approved: true` in YAML frontmatter
2. Set `approved_by` and `approved_date`
3. Save to `Projects/{ModelName}/ApprovedText/P{NNN}.md`

**Exit Criteria:** All 10 ApprovedText files present with `approved: true`.

**Critical:** The Render Engine (Phase 3) must not begin until all required ApprovedText files are sealed.

---

## Related Documents (updated v2.3.0)
- `Core/TEXT_ENGINE.md` — Text Engine specification
- `Config/LANGUAGE_POLICY.yaml` — Language enforcement
- `Tests/TextValidation.md` — Phase 2b QA protocol
- `Knowledge/GlossaryIT.md` — Phase 2 terminology reference
- `Knowledge/EditorialStyle.md` — Phase 2a editorial style
