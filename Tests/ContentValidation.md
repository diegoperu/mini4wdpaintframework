# Content Validation Tests

**Test Suite ID:** TEST-CV
**SDK Version:** 2.4.1
**Layer:** Content / CMS
**Reference:** `ApprovedAssets/Text/README.md`, `Core/TEXT_ENGINE.md`, `Config/LANGUAGE_POLICY.yaml`

## Purpose
Verify that `content.yaml` files in `ApprovedAssets/Text/P{NNN}/` are complete, correctly structured, language-compliant, and ready for rendering.

## Validation Scope (v2.4.1) — Template vs Draft vs Approved

This suite validates **generated content only**. The lifecycle position of the file
determines what may be validated:

| State | What it is | Validate? |
|---|---|---|
| **Template** | Page module as shipped by the SDK: `status: draft` AND empty fields / schema comments only. No Text Engine run has populated it. | **NO — never.** A template is not final content. Running this suite on a template produces FAIL by construction and means the pipeline order was skipped (generate first — Phase 2a — then validate). |
| **Draft (generated)** | Text Engine has produced content; `status: draft` or `review`, fields populated (possibly with `TODO:`). | **YES** — this is the normal input of this suite. `TODO:` values are reported as WARNING, not blocking, unless the field is REQUIRED for approval. |
| **Approved / Locked** | `status: approved` or `locked`. | YES for re-validation after a formal revision; otherwise already validated. Placeholders of any kind are BLOCKING here. |

**How to tell a template from generated content:** a template has `status: draft` in
`metadata.yaml` **and** its REQUIRED string fields are empty (`""`). Generated content
has populated fields. If in doubt, check whether `changelog.md` records a Text Engine
generation entry.

Additionally, per `Config/LANGUAGE_POLICY.yaml §exceptions` (v2.4.1), the following are
**never** language violations: manufacturer paint codes (TS-37, XF-1, X-10, X-11…),
commercial product names (Chrome Silver, Gun Metal, Semi Gloss Black, Flat Black,
Primer, Topcoat, Masking Tape…), YAML keys and schema values (`finish: gloss`),
structural/metadata terms (Header, Footer, draft, locked) used as metadata.

## When to Run
- After Text Engine generates content.yaml for any page — **never before**
- Before setting `metadata.yaml §approved: true`
- After any edit to a content.yaml (resets approval)
- Before Render Engine phase begins

## Blocking vs Non-Blocking
- **❌ BLOCKING:** Must fix before approval
- **⚠️ WARNING:** Should fix; may proceed with documented exception

---

## TEST-CV-001: Schema Validity

For each `ApprovedAssets/Text/P{NNN}/content.yaml`:

- [ ] CV-001-A: File is valid YAML (no parse errors) — ❌
- [ ] CV-001-B: `page.id` field present and matches directory name — ❌
- [ ] CV-001-C: `page.id` matches pattern `P[0-9]{3}` — ❌
- [ ] CV-001-D: `page.version` follows SemVer `X.Y.Z` — ⚠️
- [ ] CV-001-E: `page.language` is `"it"` — ❌
- [ ] CV-001-F: All REQUIRED fields are non-empty strings — ❌
- [ ] CV-001-G: No `{{token}}` placeholders remaining unresolved — ❌
- [ ] CV-001-H: No Lorem ipsum in any field — ❌
- [ ] CV-001-I: `footer.page_id` matches `page.id` — ❌

**Required Fields by Page:**

| Page | Required Fields |
|------|----------------|
| P001 | title, subtitle, footer.page_id, footer.model_name, render.file |
| P002 | title, colors (min 1 entry), footer.page_id |
| P003 | title, paints (min 1), tools (min 1), footer.page_id |
| P004 | title, steps (min 1 with title+description), footer.page_id |
| P005 | title, sequence (min 1), footer.page_id |
| P006 | title, zones (min 1), footer.page_id |
| P007 | title, areas (min 1), footer.page_id |
| P008 | title, decals (min 1), footer.page_id |
| P009 | title, variant_name, footer.page_id |
| P010 | title, checklist_sections (min 1), footer.page_id |

---

## TEST-CV-002: Language Compliance

- [ ] CV-002-A: No kanji (U+4E00–U+9FFF) in any field — ❌
- [ ] CV-002-B: No hiragana (U+3040–U+309F) — ❌
- [ ] CV-002-C: No katakana (U+30A0–U+30FF) — ❌
- [ ] CV-002-D: No English headings or section values — ❌
- [ ] CV-002-E: Finish type values in Italian: "lucido"/"opaco"/"satinato"/"metallizzato"/"perlato" — ❌
- [ ] CV-002-F: Step titles in Italian — ❌
- [ ] CV-002-G: Warning text in Italian, starts with "Attenzione:" — ❌
- [ ] CV-002-H: Tip text in Italian, starts with "Suggerimento:" — ❌
- [ ] CV-002-I: No [PLACEHOLDER] values in approved content (approved: true files only) — ❌

---

## TEST-CV-003: Data Accuracy

- [ ] CV-003-A: All `paint_code` values follow brand format (TS-##, C-##, etc.) — ❌
- [ ] CV-003-B: `paint_brand` is one of: Tamiya, Mr.Hobby, Vallejo, or explicitly named — ❌
- [ ] CV-003-C: Colors in P002 match PROJECT.yaml `paintScheme.colors[]` count — ❌
- [ ] CV-003-D: `sequence[].color_id` values reference valid entries in P002 colors — ❌
- [ ] CV-003-E: Step counts in P004/P005 match corresponding PROJECT.yaml arrays — ⚠️
- [ ] CV-003-F: No invented paint codes not in PROJECT.yaml — ❌
- [ ] CV-003-G: Drying time values are specific (not "qualche ora" — must be "N minuti" or "N ore") — ⚠️

---

## TEST-CV-004: Metadata Compliance

For each `ApprovedAssets/Text/P{NNN}/metadata.yaml`:

- [ ] CV-004-A: File is valid YAML — ❌
- [ ] CV-004-B: `page_id` matches parent directory — ❌
- [ ] CV-004-C: `status` is one of: draft/review/approved/locked/rendered/released/archived — ❌
- [ ] CV-004-D: `language` is `"it"` — ❌
- [ ] CV-004-E: `sdk_version` matches current VERSION file — ⚠️
- [ ] CV-004-F: If `approved: true` → `approved_by` and `approved_date` are non-empty — ❌
- [ ] CV-004-G: If `locked: true` → `approved: true` must also be true — ❌
- [ ] CV-004-H: `revision` is an integer ≥ 0 — ❌

---

## TEST-CV-005: Manifest Completeness

For each `ApprovedAssets/Text/P{NNN}/manifest.yaml`:

- [ ] CV-005-A: File is valid YAML — ❌
- [ ] CV-005-B: `components` list includes C001 and C002 — ❌
- [ ] CV-005-C: All component IDs in manifest exist in `Config/sdk.yaml §components.permanent_ids` — ❌
- [ ] CV-005-D: `tokens` list includes at minimum: VioletPrimary, White, DarkGray — ❌
- [ ] CV-005-E: `prompt_file` references an existing file in `PromptEngine/` — ❌
- [ ] CV-005-F: For pages with renders: `images[].role` is non-empty — ⚠️

---

## TEST-CV-006: Component-Field Mapping

Verify content.yaml fields provide data for declared components:

| Component | Required content.yaml field | Check |
|-----------|---------------------------|-------|
| C001 Header | page.name (for label) | [ ] |
| C002 Footer | footer.page_id, footer.model_name | [ ] |
| C003 Palette | colors[] (P002 only) | [ ] |
| C004 Shopping List | paints[], tools[], consumables[] (P003) | [ ] |
| C005 Paint Sequence | sequence[] (P005) | [ ] |
| C006 Callout | callouts[] or inline callout fields | [ ] |
| C008 Warning | warnings[] | [ ] |
| C009 Tips | tips[] | [ ] |
| C010 Paint Legend | colors[] with paint_code (P002) | [ ] |
| C011 Paint Code Box | colors[] with brand+code+finish (P002) | [ ] |
| C013 Step Number | steps[] or sequence[] | [ ] |
| C014 Time Box | steps[].duration or sequence[].drying_time | [ ] |
| C015 Notes | notes field or sections[].notes | [ ] |

---

## TEST-CV-007: Cross-Page Consistency

Run after all 10 pages are generated:

- [ ] CV-007-A: Model name identical across all pages (P001.title = P002.footer.model_name = …) — ❌
- [ ] CV-007-B: Paint scheme name consistent (P001.subtitle = P002.palette_overview name) — ⚠️
- [ ] CV-007-C: Color IDs in P005.sequence[].color_id all defined in P002.colors[].id — ❌
- [ ] CV-007-D: Total page count matches manual type (9 standard, 10 with premium) — ❌
- [ ] CV-007-E: All pages have matching `page.language: "it"` — ❌

---

## Validation Log Format

```yaml
# ContentValidation Log
page_id: "P001"
date: "YYYY-MM-DD"
reviewer: ""
sdk_version: "2.4.0"

results:
  TEST-CV-001:
    status: "PASS"   # PASS | FAIL | WARN
    failures: []
    warnings: []

  # ... repeat per test

summary:
  blocking_failures: 0
  warnings: 0
  status: "PASS"    # PASS | FAIL
  approved_for_render: true
```

## Common Errors

1. **finish field is "gloss" (English)** → use "lucido"
2. **steps[0].title is "Cleaning" (English)** → use "Pulizia"
3. **color_id in sequence not matching colors[]** → ID mismatch, check P002
4. **render.file is empty** → assign approved render path before approval
5. **metadata.yaml approved: true but approved_by empty** → add reviewer name
