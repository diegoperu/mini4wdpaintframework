# Assets/ApprovedManual/

**Version:** 2.1.0
**Access:** READ-ONLY during production
**Governance:** Project maintainer approval required for all changes
**QA Gate:** Core/QA_SYSTEM.md (all items must pass before entry)

---

## Purpose

`ApprovedManual/` is the **publication record** of the Mini4WD Manual SDK. It contains only pages and PDFs that have passed the full quality assurance process defined in `Core/QA_SYSTEM.md`. Once a file enters this directory, it is treated as immutable.

Think of this directory as the "golden copy" — the version of a manual that represents the canonical, approved output for a given model and paint scheme.

---

## Access Policy

| Action | Permitted? | Who |
|--------|------------|-----|
| Read any file | ✅ Yes | Anyone |
| Add new approved manual | ✅ Yes | Manual creator after QA approval |
| Update existing file | ⚠️ Only via versioning (see below) | Project maintainer |
| Delete a file | ❌ No | Nobody (see deletion policy) |

---

## Directory Structure

```
ApprovedManual/
└── {ModelName}/                    # One subfolder per approved model
    ├── README.md                   # Approval metadata, version history
    ├── PROJECT.yaml                # Snapshot of PROJECT.yaml at approval time
    ├── P001.png                    # Approved Cover page
    ├── P002.png                    # Approved Color Scheme page
    ├── P003.png                    # Approved Materials page
    ├── P004.png                    # Approved Preparation page
    ├── P005.png                    # Approved Painting page
    ├── P006.png                    # Approved Masking page
    ├── P007.png                    # Approved Details page
    ├── P008.png                    # Approved Decals page
    ├── P009.png                    # Approved Premium Variant page (if generated)
    ├── P010.png                    # Approved Final Checklist page
    ├── manual_screen.pdf           # Screen-optimized PDF (sRGB, 150dpi)
    ├── manual_print.pdf            # Print-ready PDF (CMYK FOGRA39, 300dpi, 3mm bleed)
    └── Notes/
        └── qa_log.md               # QA session log with reviewer sign-off
```

---

## Approval Process

A manual enters `ApprovedManual/` only after completing all four phases defined in `Core/WORKFLOW.md`:

1. **Phase 0–2:** Project setup, renders, and page generation complete
2. **Phase 3:** All QA_SYSTEM.md checklist items pass — zero failures
3. **Manual review:** A second person (or the same person after 24 hours) reviews the QA log
4. **Move to ApprovedManual/:** Copy (do not move) final pages from `Projects/{ModelName}/Output/` to `Assets/ApprovedManual/{ModelName}/`
5. **PDF export:** Generate both screen and print PDFs per `Core/PDF_MASTER.md`
6. **Sign-off:** Write a QA sign-off entry in `Notes/qa_log.md`

---

## File Naming

Pages in this directory use the standardized naming scheme:

| File | Description |
|------|-------------|
| `P001.png` through `P010.png` | Page renders at production resolution |
| `manual_screen.pdf` | PDF/A-2b, sRGB, 150dpi, no bleed |
| `manual_print.pdf` | PDF/X-4, CMYK FOGRA39, 300dpi, 3mm bleed |
| `PROJECT.yaml` | Exact copy of `Projects/{ModelName}/PROJECT.yaml` at approval time |

---

## Versioning: Updating an Approved Manual

When an approved manual requires correction (QA failure found after approval, paint code update, etc.):

1. **Never overwrite** the existing files
2. Create versioned copies: `P001_v2.png`, `P002_v2.png`, etc.
3. Create new PDFs: `manual_screen_v2.pdf`, `manual_print_v2.pdf`
4. Update `Notes/qa_log.md` with a new entry documenting what changed and why
5. Update the model's `README.md` to indicate the current approved version

After a v2 approval, the v1 files remain in place as the historical record.

---

## Deletion Policy

Files in `ApprovedManual/` are **never deleted**. This policy exists because:

- Approved manuals may have been distributed to users
- The publication record must be auditable
- Superseded versions serve as a baseline for understanding what changed

If a manual is retired (model discontinued, scheme deprecated), mark it as retired in the model's `README.md`. Do not delete the files.

The only exception is a file added by mistake (e.g., wrong model folder) — in this case, deletion requires a written decision logged in `Notes/qa_log.md` and approved by a project maintainer.

---

## Git Tagging

Each time a manual is approved and moved to this directory, tag the git commit:

```bash
git tag -a "approved/{model-slug}/v{version}" -m "Approved: {Model Name} v{version}"
# Example:
git tag -a "approved/proto-emperor/v1.0.0" -m "Approved: Proto Emperor Violet Phantom v1.0.0"
```

This makes it possible to check out the exact state of the SDK at the time any manual was approved.

---

## Approved Manuals Index

| Model | Scheme | Version | Status | Approval Date |
|-------|--------|---------|--------|---------------|
| Proto Emperor | — | — | Placeholder | — |

Add a row when a manual is approved.
