# Migration Report — v2.3.0 → v2.4.0

**SDK Version:** 2.4.0
**Migration Date:** 2026-07-01
**Migration Theme:** CMS Layer — Pages as Structured Content Modules
**Breaking Changes:** None
**Previous Version:** 2.3.0
**Authors:** Mini4WD Manual SDK maintainers

---

## Executive Summary

v2.4.0 introduces the ApprovedAssets CMS layer. Pages are no longer flat output files — they are structured content modules with lifecycle state, per-field component mapping, and a formal approval pipeline. The primary content format changes from Markdown (`ApprovedText/P{NNN}.md`) to structured YAML (`ApprovedAssets/Text/P{NNN}/content.yaml`). The Render Engine contract is updated: it reads `content.yaml` exclusively and never accesses PROJECT.yaml directly.

No existing content is removed. No existing IDs change. v2.3.0 projects are fully compatible.

---

## What Changed

### New: ApprovedAssets/ Directory

Central CMS layer. Contains all approved page content modules.

```
ApprovedAssets/
├── README.md                — CMS layer overview
├── index.yaml               — global content/manual/image registry
└── Text/
    ├── README.md            — text module directory guide
    ├── P001/                — Copertina module
    │   ├── content.yaml     ← PRIMARY (schema-validated YAML)
    │   ├── text.md          ← DERIVED (human-readable, auto-generated)
    │   ├── metadata.yaml    — lifecycle state, approvals, QA status
    │   ├── manifest.yaml    — components used, images required, tokens
    │   ├── changelog.md     — per-page revision history
    │   ├── notes.md         — editorial annotations (not rendered)
    │   └── README.md        — page module documentation
    ├── P002/ ... P010/      — same structure × 9 more pages
```

**10 page modules created:** P001–P010 (each × 7 files = 70 files total, plus READMEs and index.yaml).

### New: content.yaml as Primary Text Format

In v2.3.0, Text Engine output was `ApprovedText/P{NNN}.md` (Markdown). In v2.4.0, the primary format is `content.yaml`:

| Aspect | v2.3.0 | v2.4.0 |
|--------|--------|--------|
| Primary format | `ApprovedText/P{NNN}.md` | `ApprovedAssets/Text/P{NNN}/content.yaml` |
| Schema enforcement | None | YAML schema (CV-001) |
| text.md | Primary output | Derived from content.yaml |
| Component mapping | Prose description | Machine-readable field map |
| Lifecycle tracking | None | metadata.yaml states |

**Rule: field names are English (structural keys); field values are Italian (editorial content).**

### New: Page Lifecycle States

Each page module tracks lifecycle state in `metadata.yaml`:

```
draft → review → approved → locked → rendered → released → archived
```

- `locked: true` prevents modification without explicit unlock + re-approval
- `approved: true` is required before Render Engine may read the page
- Revision counter increments on every approved change
- Per-page changelog records all revisions with date and reason

### New: Tests/ContentValidation.md

7 content QA test suites:

| Suite | Scope |
|-------|-------|
| CV-001 | YAML schema validity and required fields |
| CV-002 | Language compliance (Italian values, no Japanese scripts) |
| CV-003 | Data accuracy (values match PROJECT.yaml source) |
| CV-004 | metadata.yaml integrity (states, dates, approvals) |
| CV-005 | manifest.yaml consistency (component IDs, image refs) |
| CV-006 | Component-field mapping (C### fields in content.yaml) |
| CV-007 | Cross-page consistency (P001 title = P010 footer, etc.) |

### Updated: Build Pipeline Phases

| Phase | v2.3.0 | v2.4.0 |
|-------|--------|--------|
| Phase 2a | Text Engine (output: text.md) | Text Engine (output: content.yaml) |
| Phase 2b | Editorial QA | Content QA (Tests/ContentValidation.md) |
| Phase 2c | — | Text QA (Tests/TextValidation.md, was 2b) |
| Phase 2d | — | Approved Assets Sealing (NEW) |
| Phase 3 | Render reads ApprovedText/ | Render reads content.yaml ONLY |

### Updated: Render Engine Contract

**v2.3.0:** Render Engine could supplement from PROJECT.yaml if ApprovedText was incomplete.

**v2.4.0 (ADR-021):** Render Engine reads `ApprovedAssets/Text/P{NNN}/content.yaml` exclusively. No fallback to PROJECT.yaml. Missing fields → approved placeholder, not substitution.

### Updated: LOAD Sequence (9 steps)

v2.3.0 had 8 steps. v2.4.0 adds Step 8:

```
STEP 8: (if updating) LOAD ApprovedAssets/Text/P{NNN}/content.yaml
```

Load existing content.yaml before generating updates. Preserves previously approved content; only modifies declared fields.

### Updated: Core Documents

| Document | Change |
|----------|--------|
| `Core/TEXT_ENGINE.md` | §content.yaml as Primary Output: lifecycle, Render Engine contract |
| `Core/COMPONENT_SYSTEM.md` | §content.yaml Field Mapping: per-component field declarations |
| `Core/PAGE_SYSTEM.md` | §Page-as-Module Architecture: lifecycle states, module structure |
| `PromptEngine/README.md` | §content.yaml Generation Mode: 9-step LOAD, field name/value rule |
| `Build/Pipeline.md` | §CMS Pipeline v2.4.0: phases 2b/2c/2d, Render Engine contract |

### New ADRs

| ADR | Title |
|-----|-------|
| ADR-019 | content.yaml as Primary Source of Truth for Page Content |
| ADR-020 | Page-as-Module Architecture with Lifecycle States |
| ADR-021 | Render Engine Reads content.yaml Exclusively — Never PROJECT.yaml |

---

## File Inventory

### New Files (v2.4.0)

| Path | Type | Description |
|------|------|-------------|
| `ApprovedAssets/README.md` | CMS | Layer overview |
| `ApprovedAssets/index.yaml` | CMS | Global registry |
| `ApprovedAssets/Text/README.md` | CMS | Text module directory guide |
| `ApprovedAssets/Text/P001/content.yaml` | Content | Copertina — primary |
| `ApprovedAssets/Text/P001/text.md` | Content | Copertina — derived |
| `ApprovedAssets/Text/P001/metadata.yaml` | CMS | Lifecycle state |
| `ApprovedAssets/Text/P001/manifest.yaml` | CMS | Component map |
| `ApprovedAssets/Text/P001/changelog.md` | CMS | Revision history |
| `ApprovedAssets/Text/P001/notes.md` | CMS | Editorial notes |
| `ApprovedAssets/Text/P001/README.md` | CMS | Module docs |
| *(P002–P010: same 7 files each = 63 more files)* | Content | Pages 2–10 |
| `Tests/ContentValidation.md` | Tests | 7 content QA suites |
| `MigrationReport_v2.4.md` | Docs | This file |

**Total new files: ~77**

### Modified Files (v2.4.0)

| Path | Change |
|------|--------|
| `Core/TEXT_ENGINE.md` | §content.yaml as Primary Output appended |
| `Core/COMPONENT_SYSTEM.md` | §content.yaml Field Mapping appended |
| `Core/PAGE_SYSTEM.md` | §Page-as-Module Architecture appended |
| `PromptEngine/README.md` | §content.yaml Generation Mode appended |
| `Build/Pipeline.md` | §CMS Pipeline v2.4.0 appended |
| `CHANGELOG.md` | [2.4.0] entry inserted |
| `ROADMAP.md` | v2.4.0 status + v2.5.0 planned appended |
| `STYLE_DECISIONS.md` | ADR-019, ADR-020, ADR-021 appended |
| `VERSION` | 2.3.0 → 2.4.0 |

**No files removed. No IDs changed. No existing content modified.**

---

## Migration Instructions for Existing Projects

v2.4.0 introduces no breaking changes. v2.3.0 projects continue to work without modification.

### Optional Migration Steps

1. **Create ApprovedAssets module directories** for each page:
   ```
   ApprovedAssets/Text/P001/
   ApprovedAssets/Text/P002/
   ... (P003–P010)
   ```

2. **Convert existing ApprovedText Markdown** to content.yaml format.
   - Move content from `Projects/{Model}/ApprovedText/P{NNN}.md`
   - Restructure into YAML per page schema (see existing P001–P010 modules as reference)
   - Generate text.md from content.yaml (derived automatically)

3. **Create metadata.yaml** for each converted page:
   - Set `status: "approved"` if content was previously approved
   - Set `approved_by` and `approved_date`
   - Set `revision: 1` for migrated content

4. **Update prompts** to use 9-step LOAD sequence (add Step 8 for update sessions).

5. **Update Render Engine references** from `ApprovedText/` to `ApprovedAssets/Text/`.

---

## Compatibility Matrix

| SDK Version | Compatible with v2.4.0? | Notes |
|------------|------------------------|-------|
| v2.3.0 projects | ✅ Yes | All content formats compatible |
| v2.2.0 projects | ✅ Yes | Adopt v2.3.0 Text Engine first for full benefit |
| v2.1.0 projects | ✅ Yes | No breaking changes across all versions |

---

## Known Limitations (v2.4.0)

- `ApprovedAssets/index.yaml` requires manual update after each page approval (automated updater planned for v2.5.0)
- content.yaml schema validation is currently human-executed (automated runner planned for v2.5.0)
- No tooling yet for Markdown → content.yaml migration (manual conversion required)

---

## Next: v2.5.0

Planned automation features:
- Python scripts for content.yaml generation and validation
- SVG icon library for components C006, C008
- Automated Tests/ContentValidation.md runner
- `Config/environments/` for dev/staging/production config switching

See `ROADMAP.md §v2.5.0 — Planned` for full scope.
