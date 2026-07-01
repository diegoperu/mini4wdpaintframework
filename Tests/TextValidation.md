# Text Validation Tests

**Test Suite ID:** TEST-TX
**SDK Version:** 2.3.0
**Layer:** Editorial / Text Engine
**Reference:** `Core/TEXT_ENGINE.md`, `Config/LANGUAGE_POLICY.yaml`, `Core/AI_OPERATING_RULES.md §TEXT RENDERING RULES`, `Knowledge/GlossaryIT.md`

## Purpose

Verify that all text content in `ApprovedText/` files is linguistically correct, editorially consistent, and compliant with the language policy before it enters the Render Engine.

## When to Run

- After Text Engine generates raw text (before approval)
- Before setting `approved: true` in ApprovedText frontmatter
- After any text edit to an ApprovedText file
- Before running any PromptEngine/ render prompts

## Blocking vs Non-Blocking

**Blocking (❌):** Must fix before setting `approved: true`. Render Engine must not receive unapproved text.
**Warning (⚠️):** Should fix; does not block approval if documented in qa_log.md.

---

## TEST-TX-001: Language Compliance (BLOCKING)

Verify all text is Italian. Run for each ApprovedText file.

### Japanese Scripts — Zero Tolerance
- [ ] TX-001-A: No kanji characters (Unicode U+4E00–U+9FFF) — ❌ BLOCKING
- [ ] TX-001-B: No hiragana characters (U+3040–U+309F) — ❌ BLOCKING
- [ ] TX-001-C: No katakana characters (U+30A0–U+30FF) — ❌ BLOCKING
- [ ] TX-001-D: No CJK punctuation (U+3000–U+303F) — ❌ BLOCKING
- [ ] TX-001-E: No half-width katakana (U+FF65–U+FF9F) — ❌ BLOCKING

### Other Forbidden Scripts
- [ ] TX-001-F: No Chinese simplified/traditional characters — ❌ BLOCKING
- [ ] TX-001-G: No Korean hangul — ❌ BLOCKING
- [ ] TX-001-H: No Arabic script — ❌ BLOCKING
- [ ] TX-001-I: No Cyrillic (Russian) characters — ❌ BLOCKING

### English
- [ ] TX-001-J: No English sentences or paragraphs — ❌ BLOCKING
- [ ] TX-001-K: Accepted English technical terms only: "spray", "airbrush", "primer", "clear coat" — ⚠️ verify per `Config/LANGUAGE_POLICY.yaml §exceptions`
- [ ] TX-001-L: No English headings or section titles — ❌ BLOCKING

### Other Latin Languages
- [ ] TX-001-M: No French, German, Spanish, or Portuguese paragraphs — ❌ BLOCKING

---

## TEST-TX-002: Fake Text Prohibition (BLOCKING)

- [ ] TX-002-A: No "Lorem ipsum" or any variant ("Lorem ipsum dolor…") — ❌ BLOCKING
- [ ] TX-002-B: No random character strings ("asdfjkl", "xyzxyz", "aaaaaaa") — ❌ BLOCKING
- [ ] TX-002-C: No pseudo-Japanese text (Latin chars arranged to mimic kana) — ❌ BLOCKING
- [ ] TX-002-D: No generic template placeholders left unresolved ("[TEXT HERE]", "PLACEHOLDER") — ❌ BLOCKING
  - **Exception:** Approved placeholders from `Config/LANGUAGE_POLICY.yaml §approved_placeholders` are permitted ONLY when `approved: false` in frontmatter. All must be resolved before `approved: true`.

---

## TEST-TX-003: Token Resolution (BLOCKING)

- [ ] TX-003-A: No unresolved `{{token}}` strings visible in output — ❌ BLOCKING
- [ ] TX-003-B: `{{project.modelName}}` literal does not appear in body text — ❌ BLOCKING
- [ ] TX-003-C: Model name is present as the actual name (e.g., "Proto Emperor") — ❌ BLOCKING if wrong
- [ ] TX-003-D: Paint codes are actual codes ("TS-57") not token syntax — ❌ BLOCKING

---

## TEST-TX-004: YAML Frontmatter Validity

- [ ] TX-004-A: Every ApprovedText file has a valid YAML frontmatter block (`---` delimited) — ❌ BLOCKING
- [ ] TX-004-B: `page_id` present and matches filename (`P001.md` → `page_id: P001`) — ❌ BLOCKING
- [ ] TX-004-C: `language: it` present — ❌ BLOCKING
- [ ] TX-004-D: `sdk_version` matches current `VERSION` file — ⚠️ WARNING
- [ ] TX-004-E: `approved` field is boolean `true` or `false` — ❌ BLOCKING
- [ ] TX-004-F: When `approved: true`, both `approved_by` and `approved_date` must be non-empty — ❌ BLOCKING

---

## TEST-TX-005: Terminology Consistency

- [ ] TX-005-A: Terms consistent with `Knowledge/GlossaryIT.md` — ⚠️ WARNING if inconsistent
- [ ] TX-005-B: "Carrozzeria" used consistently (not alternating with "corpo" or "scocca") — ⚠️
- [ ] TX-005-C: "Verniciatura" used consistently (not "pittura" or "colorazione") — ⚠️
- [ ] TX-005-D: "Mascheratura" used consistently (not "nastro" used as a verb) — ⚠️
- [ ] TX-005-E: "Primer" used consistently (not "fondo" or "apprêt") — ⚠️
- [ ] TX-005-F: No terms from `Knowledge/ForbiddenWords.md` — ❌ BLOCKING

---

## TEST-TX-006: Tone and Register

- [ ] TX-006-A: Instructions use second person singular imperative ("Applica", not "Si applica" or "Applicare") — ⚠️
- [ ] TX-006-B: No informal or slang terms — ⚠️
- [ ] TX-006-C: No marketing language ("fantastico", "incredibile", "rivoluzionario") — ⚠️
- [ ] TX-006-D: Quantities are specified numerically, not vaguely ("2 mani" not "alcune mani") — ⚠️
- [ ] TX-006-E: Tone matches `Knowledge/EditorialStyle.md §Registro` — ⚠️

---

## TEST-TX-007: Typography Rules Compliance

- [ ] TX-007-A: Decimal separator is "," not "." (Italian convention: 1,5 not 1.5) — ⚠️
- [ ] TX-007-B: Thousand separator is "." for numbers ≥ 1.000 — ⚠️
- [ ] TX-007-C: Quotes use «guillemets» not "straight quotes" — ⚠️
- [ ] TX-007-D: No ALL CAPS in body text (component IDs and labels excepted) — ⚠️
- [ ] TX-007-E: Section headings use sentence case (first word capitalized only) — ⚠️
- [ ] TX-007-F: No trailing whitespace lines at end of sections — ⚠️

---

## TEST-TX-008: Completeness

- [ ] TX-008-A: All required ApprovedText files present (P001–P008, P010; P009 if `premiumVariant.enabled: true`) — ❌ BLOCKING
- [ ] TX-008-B: No empty sections (heading present, body absent) — ❌ BLOCKING
- [ ] TX-008-C: P002 lists all colors from `PROJECT.yaml §paintScheme.colors[]` — ❌ BLOCKING
- [ ] TX-008-D: P003 lists all materials from `PROJECT.yaml §materials` — ❌ BLOCKING
- [ ] TX-008-E: P005 step sequence matches `paintSequence[]` order from PROJECT.yaml — ❌ BLOCKING
- [ ] TX-008-F: `<!-- TEXT_ENGINE_MARKER: end -->` comment present at end of file — ⚠️

---

## TEST-TX-009: Page-Specific Checks

### P001 — Copertina
- [ ] Model name present and correctly spelled — ❌
- [ ] Paint scheme name present — ❌
- [ ] Series name present (if in PROJECT.yaml) — ⚠️
- [ ] Year present — ⚠️

### P002 — Schema Colori
- [ ] All colors from `paintScheme.colors[]` listed — ❌
- [ ] All paint codes exact-match PROJECT.yaml (case-sensitive) — ❌
- [ ] Each finish type stated in Italian ("Lucido", "Opaco", "Metallizzato", "Perlato") — ❌

### P003 — Materiali
- [ ] Every paint from `paintScheme.colors[]` appears in the paint list — ❌
- [ ] Safety notes present (at minimum one warning regarding solvents) — ⚠️

### P004 — Preparazione
- [ ] Step count matches `preparationSteps[]` count in PROJECT.yaml — ❌
- [ ] Each step has both title and description — ❌

### P005 — Verniciatura
- [ ] Step count matches `paintSequence[]` count in PROJECT.yaml — ❌
- [ ] Each step references a valid `colorId` from `paintScheme.colors[]` — ❌
- [ ] Drying times present for each step — ⚠️

### P006 — Mascheratura
- [ ] Zone count matches `maskingZones[]` count in PROJECT.yaml — ❌
- [ ] Masking sequence order matches `maskingOrder` values — ❌

### P008 — Decalcomanie
- [ ] Decal count matches `decals[]` count in PROJECT.yaml — ❌
- [ ] Clear coat note present after decal application — ⚠️

### P010 — Lista di Controllo Finale
- [ ] At least 10 checklist items present — ⚠️
- [ ] Storage and care section present — ⚠️

---

## Pass/Fail Record Template

```
# TextValidation Log — {ModelName} {PageID}
Data: YYYY-MM-DD
Revisore: {nome}

Blocchi ❌: {conteggio}
Avvertenze ⚠️: {conteggio}
Superati ✅: {conteggio}

Stato: SUPERATO / FALLITO
Note: {eccezioni documentate}

Approvato per Render Engine: SÌ / NO
```

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Section titles in English | Missing LANGUAGE_POLICY in LOAD sequence | Add `LOAD Config/LANGUAGE_POLICY.yaml` to prompt |
| "Code: TS-57" instead of "Codice: TS-57" | AI defaulted to English labels | Regenerate with LANGUAGE_POLICY loaded |
| "30 minutes" instead of "30 minuti" | Same as above | Regenerate |
| Lorem ipsum in step body | AI placeholder not replaced | Remove and regenerate that step |
| Unresolved `{{project.modelName}}` | Token substitution skipped | Resolve all tokens before generating |
| `approved: true` with empty `approved_by` | Approval form incomplete | Fill reviewer field before setting approved |

---

## Related Documents

- `Core/TEXT_ENGINE.md`
- `Config/LANGUAGE_POLICY.yaml`
- `Core/AI_OPERATING_RULES.md §TEXT RENDERING RULES`
- `Knowledge/GlossaryIT.md`
- `Knowledge/EditorialStyle.md`
- `Knowledge/ForbiddenWords.md`
- `Build/Pipeline.md §Phase 2 (Text Engine)`
