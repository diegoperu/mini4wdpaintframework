# [Model Name] — Project Progress Checklist

> **Instructions:** Copy this file to `Projects/{ModelName}/CHECKLIST.md`. Check off items as you complete them.
> See `Core/WORKFLOW.md` for detailed instructions on each phase.

**Model:** [Model Name]
**Scheme:** [Scheme Name]
**Started:** [YYYY-MM-DD]
**SDK Version:** 2.4.1

---

## Phase 0: Project Setup

- [ ] PROJECT.yaml copied from `Templates/PROJECT.yaml` to `Projects/{ModelName}/PROJECT.yaml`
- [ ] All REQUIRED fields filled in PROJECT.yaml
- [ ] COLOR_SCHEME.yaml copied and completed
- [ ] PDF_CONFIG.yaml copied and configured
- [ ] PROJECT.md filled with human-readable summary
- [ ] Project folder structure created:
  - [ ] `Projects/{ModelName}/Images/`
  - [ ] `Projects/{ModelName}/Output/raw/`
  - [ ] `Projects/{ModelName}/Notes/`
- [ ] Reference images gathered in `Projects/{ModelName}/Images/` (single convention, v2.4.1)
- [ ] `qa.status` in PROJECT.yaml set to `draft`

**Phase 0 Complete:** [ ]

---

## Phase 1: Render Generation

### Cover Render (P001)
- [ ] Render generated: 3/4 front-left angle, white background
- [ ] Resolution verified: minimum 2480x3508px
- [ ] Render approved per `Core/RENDER_GUIDE.md §7`
- [ ] File saved: `Projects/{ModelName}/Images/cover_3q.png`

### Color Scheme Renders (P002)
- [ ] Front view render generated (orthographic)
- [ ] Side view render generated (orthographic)
- [ ] Top view render generated (orthographic)
- [ ] All three renders approved per RENDER_GUIDE
- [ ] Files saved: `Images/P002_front.png`, `Images/P002_side.png`, `Images/P002_top.png`

### Detail Renders (P007)
- [ ] Close-up render for each detailAreas[] entry
- [ ] All detail renders approved per RENDER_GUIDE
- [ ] Files saved to `Images/`

**Phase 1 Complete:** [ ]

---

## Phase 2: Manual Page Generation

For each page: run the PromptEngine prompt, review the output, iterate until approved.

### P001 — Cover
- [ ] All tokens substituted in `PromptEngine/Cover.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P001_raw.md`
- [ ] Visual review complete
- [ ] Page QA'd against QA-001 to QA-030
- [ ] P001 approved

### P002 — Color Scheme
- [ ] All tokens substituted in `PromptEngine/ColorScheme.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P002_raw.md`
- [ ] Color legend verified: one row per paintScheme.colors[] entry
- [ ] P002 approved

### P003 — Materials
- [ ] All tokens substituted in `PromptEngine/Materials.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P003_raw.md`
- [ ] Safety warning C008 present
- [ ] P003 approved

### P004 — Preparation
- [ ] All tokens substituted in `PromptEngine/Preparation.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P004_raw.md`
- [ ] All preparationSteps[] rendered
- [ ] P004 approved

### P005 — Painting
- [ ] All tokens substituted in `PromptEngine/Painting.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P005_raw.md`
- [ ] All paintSequence[] steps in correct order
- [ ] Drying time warnings present
- [ ] P005 approved

### P006 — Masking
- [ ] All tokens substituted in `PromptEngine/Masking.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P006_raw.md`
- [ ] All maskingZones[] in sequence table
- [ ] Paint bleed warning present
- [ ] P006 approved

### P007 — Details
- [ ] All tokens substituted in `PromptEngine/Details.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P007_raw.md`
- [ ] All detailAreas[] have zoom panels
- [ ] P007 approved

### P008 — Decals
- [ ] All tokens substituted in `PromptEngine/Decals.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P008_raw.md`
- [ ] All decals[] in reference table
- [ ] Decal softener warning present
- [ ] P008 approved

### P009 — Premium Variant (CONDITIONAL)
- [ ] Check: `premiumVariant.enabled: true` in PROJECT.yaml?
  - If NO: skip P009
  - If YES:
    - [ ] All tokens substituted in `PromptEngine/Premium.md`
    - [ ] Prompt sent to AI model
    - [ ] Raw output saved to `Output/raw/P009_raw.md`
    - [ ] Comparison panel (base vs premium) present
    - [ ] P009 approved

### P010 — Final Checklist
- [ ] All tokens substituted in `PromptEngine/FinalChecklist.md`
- [ ] Prompt sent to AI model
- [ ] Raw output saved to `Output/raw/P010_raw.md`
- [ ] Checkbox for every paintScheme.colors[] entry
- [ ] Completion badge present
- [ ] P010 approved

**Phase 2 Complete:** [ ]

---

## Phase 3: QA

- [ ] Full QA_SYSTEM.md checklist run (see `Core/QA_SYSTEM.md`)
- [ ] All layout items QA-001 to QA-015 passed
- [ ] All rendering items QA-016 to QA-030 passed
- [ ] All typography items QA-031 to QA-045 passed
- [ ] All color/palette items QA-046 to QA-060 passed
- [ ] All component items QA-061 to QA-070 passed
- [ ] All prompt compliance items QA-071 to QA-080 passed
- [ ] All asset items QA-081 to QA-085 passed
- [ ] All workflow items QA-086 to QA-090 passed
- [ ] All naming items QA-091 to QA-095 passed
- [ ] All PDF items QA-096 to QA-100 passed
- [ ] All content items QA-101 to QA-110 passed
- [ ] QA log written to `Notes/qa_log.md`
- [ ] Zero QA failures remaining
- [ ] `qa.status` in PROJECT.yaml set to `approved`

**Phase 3 Complete:** [ ]

---

## Phase 4: Publication

- [ ] All approved page files moved to `Assets/ApprovedManual/{ModelName}/`
- [ ] PDF_CONFIG.yaml reviewed for this project
- [ ] PDF (screen variant) exported — `Assets/ApprovedManual/{ModelName}/manual_screen.pdf`
- [ ] PDF (print variant) exported — `Assets/ApprovedManual/{ModelName}/manual_print.pdf`
- [ ] PDF (archive variant) exported — `Assets/ApprovedManual/{ModelName}/manual_archive.pdf`
- [ ] PDF metadata verified (title, author, keywords, SDK version)
- [ ] PDF bookmarks present and correct
- [ ] Fonts embedded in all PDF variants
- [ ] `notes.md` written in `Assets/ApprovedManual/{ModelName}/`

**Phase 4 Complete:** [ ]

---

## Completion

- [ ] All 4 phases complete
- [ ] Definition of Done satisfied (see `Core/DEFINITION_OF_DONE.md §Manual Level DoD`)
- [ ] CHANGELOG.md updated if this is a new manual version

**MANUAL COMPLETE:** [ ]

---

*Mini4WD Manual SDK v2.5.0 — `Core/WORKFLOW.md` for pipeline details.*
