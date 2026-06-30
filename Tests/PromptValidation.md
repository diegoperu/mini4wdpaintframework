# Prompt Validation Tests

**Test Suite ID:** TEST-PR
**SDK Version:** 2.2.0
**Layer:** PromptEngine
**Reference:** `PromptEngine/README.md`, `Core/PAGE_SYSTEM.md`, `Core/AI_OPERATING_RULES.md`, `Config/sdk.yaml §project_schema`

## Purpose

Verify that all prompt templates in `PromptEngine/` are syntactically correct, use valid token syntax, reference only existing component IDs, and comply with AI Operating Rules before being executed against any AI model.

## When to Run
- Before executing any prompt against an AI model (Build/Pipeline.md Phase 2)
- After modifying any `PromptEngine/` file
- After adding new fields to `Templates/PROJECT.yaml`
- After adding new tokens to `Assets/DesignSystem/Tokens/`

---

## TEST-PR-001: Token Syntax Validity

**Input:** All `.md` files in `PromptEngine/`
**Success Criteria:** Every `{{token}}` reference uses correct double-brace syntax with valid namespace

For each prompt file, check:

- [ ] All tokens use double-brace syntax: `{{project.fieldName}}`
- [ ] No single-brace syntax: `{token}` — **FAIL (blocking)**
- [ ] No bare field names without namespace: `modelName` used as token — WARN
- [ ] No spaces inside braces: `{{ project.modelName }}` — WARN
- [ ] Token paths reference fields that exist in `Templates/PROJECT.yaml`

**Valid syntax:**
```
{{project.modelName}}
{{project.seriesName}}
{{project.paintScheme.name}}
{{project.paintScheme.colors[0].paintCode}}
{{project.preparationSteps[0].title}}
{{project.year}}
```

**Invalid syntax:**
```
{project.modelName}           ← single brace — FAIL
{{modelName}}                 ← missing namespace — FAIL
{{ project.modelName }}       ← spaces inside braces — WARN
project.modelName             ← bare path in text — WARN
```

**Output:** ✅ PASS if no FAIL items found | ❌ FAIL (blocking) if any single-brace tokens exist

---

## TEST-PR-002: Token Coverage Per Page

**Input:** Each prompt file, `Config/sdk.yaml §project_schema.required_fields`
**Success Criteria:** Each prompt uses only tokens that exist in PROJECT.yaml schema

For each prompt file, extract all `{{token}}` references and verify:

| Prompt File | Tokens Used | All Exist in PROJECT.yaml | Check |
|-------------|-------------|--------------------------|-------|
| Cover.md | project.modelName, project.seriesName, project.paintScheme.name, paths.coverRenderPath, project.year | [ ] | [ ] |
| ColorScheme.md | project.modelName, project.paintScheme.*, project.paintScheme.colors[] | [ ] | [ ] |
| Materials.md | project.modelName, project.materials.*, project.paintScheme.colors[] | [ ] | [ ] |
| Preparation.md | project.modelName, project.preparationSteps[] | [ ] | [ ] |
| Painting.md | project.modelName, project.paintSequence[], project.paintScheme.colors[] | [ ] | [ ] |
| Masking.md | project.modelName, project.maskingZones[] | [ ] | [ ] |
| Details.md | project.modelName, project.detailAreas[] | [ ] | [ ] |
| Decals.md | project.modelName, project.decals[] | [ ] | [ ] |
| Premium.md | project.modelName, project.premiumVariant.* | [ ] | [ ] |
| FinalChecklist.md | project.modelName, project.paintScheme.name | [ ] | [ ] |

**Output:** ✅ PASS if all tokens map to valid PROJECT.yaml fields

---

## TEST-PR-003: Component References Valid

**Input:** All files in `PromptEngine/`
**Reference:** `Config/sdk.yaml §components.permanent_ids`
**Success Criteria:** All component IDs referenced in prompts are registered

For each prompt file:
- [ ] All referenced component IDs match pattern `C[0-9]{3}`
- [ ] All referenced IDs exist in `Config/sdk.yaml §components.permanent_ids`
- [ ] No deprecated names used (e.g., `COMP_HEADER`, `HEADER_COMPONENT`)
- [ ] No references to C016+ unless those IDs have been registered

**Output:** ✅ PASS if all references valid | ❌ FAIL (blocking) if unknown component IDs found

---

## TEST-PR-004: Page Coverage

**Input:** `PromptEngine/` directory listing, `Config/sdk.yaml §pages`
**Success Criteria:** One prompt file exists per page in the registry

| Page ID | Required | Prompt File | Exists |
|---------|----------|-------------|--------|
| P001 | Yes | `Cover.md` | [ ] |
| P002 | Yes | `ColorScheme.md` | [ ] |
| P003 | Yes | `Materials.md` | [ ] |
| P004 | Yes | `Preparation.md` | [ ] |
| P005 | Yes | `Painting.md` | [ ] |
| P006 | Yes | `Masking.md` | [ ] |
| P007 | Yes | `Details.md` | [ ] |
| P008 | Yes | `Decals.md` | [ ] |
| P009 | No | `Premium.md` | [ ] |
| P010 | Yes | `FinalChecklist.md` | [ ] |

**Output:** ✅ PASS if all required pages have prompt files | ❌ FAIL (blocking) if any required prompt missing

---

## TEST-PR-005: AI Operating Rule Compliance

**Input:** All `PromptEngine/` files
**Reference:** `Core/AI_OPERATING_RULES.md`
**Success Criteria:** No prompt instructs the AI to violate operating rules

- [ ] No prompt asks AI to invent or guess paint codes — AI must use only PROJECT.yaml data
- [ ] No prompt asks AI to modify body shape or proportions of the model
- [ ] No prompt allows AI to add colors not in `paintScheme.colors`
- [ ] No prompt asks AI to create decals not listed in `project.decals[]`
- [ ] All prompts include explicit instruction to use Design Tokens (not hardcoded hex values)
- [ ] All prompts identify which page they are generating ("You are generating P003")
- [ ] All prompts include a validation checklist section

**Output:** ✅ PASS if all checks clear | ❌ FAIL (blocking) if any rule violation found

---

## TEST-PR-006: Required Sections Present

**Input:** Each prompt file
**Success Criteria:** Consistent structure across all prompt files

For each file, verify these sections exist:
- [ ] `## Purpose` — states which page this prompt generates
- [ ] `## Required Inputs` — table of `{{tokens}}` with source and example
- [ ] `## Prompt Template` — fenced block containing the full prompt text
- [ ] `## Validation` — post-generation checklist the author must run

**Output:** ✅ PASS if all sections present in all files | ⚠️ WARNING if sections missing in optional-page prompts

**Common Errors:**
- Missing `## Validation` section — AI output bypasses verification
- Token table references fields not in `Templates/PROJECT.yaml`
- Prompt Template block not fenced — AI model may misread formatting
