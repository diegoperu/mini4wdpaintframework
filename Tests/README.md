# Tests/

> **A cosa serve questa cartella:** le suite di validazione QA. L'Operatore le ALLEGA in chat in Fase 3 (QA); non le esegue a mano né le modifica.
> **Chi la modifica:** solo Developer, a release SDK.
> **Quando:** se un test fallisce si corregge il CONTENUTO, mai il test. I template `draft` non si validano (`ContentValidation.md §Validation Scope`).

**Role in framework:** Defines validation protocols for every layer of the SDK.

**SDK Version:** 2.4.1

Tests/ contains human-executable validation protocols — structured checklists and test procedures that verify the SDK itself is internally consistent and that each generated manual meets quality standards. These are not automated test suites (automation planned for v3.0.0) but systematic, repeatable verification guides.

## Contents

| File | Test Suite ID | Tests | Layer |
|------|---------------|-------|-------|
| `FrameworkIntegrity.md` | TEST-FW | SDK internal consistency, file presence, registry consistency | Framework |
| `PromptValidation.md` | TEST-PR | Prompt template correctness, token syntax, AI rule compliance | PromptEngine |
| `LayoutValidation.md` | TEST-LY | Page dimensions, component placement, margin integrity | Visual |
| `NamingValidation.md` | TEST-NM | File and directory naming conventions | Filesystem |
| `ColorValidation.md` | TEST-CL | Color accuracy, token usage, paint code validity | Color |
| `PDFValidation.md` | TEST-PD | PDF metadata, font embedding, bookmarks, checksums | Export |
| `AssetsValidation.md` | TEST-AS | Asset presence, format compliance, no orphaned files | Assets |
| `ContentValidation.md` | TEST-CV | content.yaml schema, language, data, metadata, manifest, component mapping, cross-page consistency, mechanical safety (8 suites) | Content / CMS |
| `TextValidation.md` | TEST-TX | Italian language compliance, forbidden words, terminology, editorial style (9 tests) | Editorial |

## Test Execution Order

Run tests in this order when validating a full manual production run:

```
1. FrameworkIntegrity   → Verify SDK itself is internally valid
2. NamingValidation     → Verify all files are correctly named
3. ColorValidation      → Verify colors match approved palette
4. LayoutValidation     → Verify pages meet layout spec
5. PromptValidation     → Verify no unresolved tokens remain
6. AssetsValidation     → Verify all assets are present and valid
7. PDFValidation        → Verify PDF exports meet technical spec
```

## Pass/Fail Criteria

- **✅ PASS** — all checklist items for that test return positive
- **❌ FAIL (blocking)** — any item marked BLOCKING fails; pipeline cannot advance
- **⚠️ WARNING (non-blocking)** — item fails but is documented; pipeline may continue with exception

Blocking/non-blocking classification is defined in `Config/quality.yaml §blocking_qa_ids`.

## When to Run Tests

| Trigger | Tests to Run |
|---------|-------------|
| Starting new project | TEST-FW |
| Before Phase 2 (prompts) | TEST-FW, TEST-PR |
| After Phase 3 (renders) | TEST-CL, TEST-AS |
| Before Phase 4 (QA) | All tests |
| Before Phase 6 (approval) | All tests + full Core/QA_SYSTEM.md |
| After SDK version bump | TEST-FW |

## Relationship to Core/QA_SYSTEM.md

`Tests/` and `Core/QA_SYSTEM.md` serve different purposes:

| | Tests/ | Core/QA_SYSTEM.md |
|-|--------|-------------------|
| **Scope** | SDK validity + manual quality | Manual quality only |
| **When** | Per-phase checkpoints | Before approval |
| **Depth** | Layer-by-layer (9 suites) | Single flat checklist (110 items) |
| **Runs on** | SDK + project files | Generated manual pages |

Both must pass before a manual can be moved to `Assets/ApprovedManual/`.

## Related Documents
- `Core/QA_SYSTEM.md` — 110-item manual quality checklist
- `Config/quality.yaml` — numeric thresholds used by these tests
- `Build/Pipeline.md` — where tests fit in the production pipeline
- `Core/DEFINITION_OF_DONE.md` — exit criteria per phase
