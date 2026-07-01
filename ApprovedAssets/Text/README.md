# ApprovedAssets/Text/

**Role:** Structured editorial content store. One subdirectory per page (P001–P010).

**SDK Version:** 2.4.0

Each page directory is a self-contained content module with full lifecycle tracking, versioning, and editorial metadata.

## Structure

```
Text/
├── P001/   Copertina (Cover)
├── P002/   Schema Colori (Color Scheme)
├── P003/   Materiali (Materials)
├── P004/   Preparazione (Preparation)
├── P005/   Verniciatura (Painting)
├── P006/   Mascheratura (Masking)
├── P007/   Dettagli (Details)
├── P008/   Decalcomanie (Decals)
├── P009/   Variante Premium (conditional)
├── P010/   Checklist Finale
└── README.md  (this file)
```

## Files Per Page Directory

| File | Format | Purpose | Primary author |
|------|--------|---------|----------------|
| `content.yaml` | YAML | **Source of truth** — structured editorial data | Text Engine |
| `text.md` | Markdown | Human-readable view of content.yaml (derived) | Text Engine |
| `metadata.yaml` | YAML | Lifecycle status, approvals, QA tracking | Author |
| `manifest.yaml` | YAML | Components, images, tokens, dependencies | Author |
| `changelog.md` | Markdown | Per-page revision history | Author |
| `notes.md` | Markdown | Editorial annotations, TODOs — NOT rendered | Author |
| `README.md` | Markdown | Page module documentation | Author |

## Content Priority

```
content.yaml  ←  PRIMARY (Render Engine reads this)
    ↓ derived
text.md       ←  SECONDARY (human review only)
```

If content.yaml and text.md disagree: **content.yaml wins always**.

## Lifecycle States

| State | content.yaml editable | Render Engine reads |
|-------|-----------------------|---------------------|
| draft | Yes | No |
| review | Yes (tracked) | No |
| approved | No (requires reset) | Yes |
| locked | No | Yes |
| rendered | No | Read-only |
| released | No | Read-only |
| archived | No | No |

## Related Documents
- `Core/TEXT_ENGINE.md`
- `Tests/ContentValidation.md`
- `Config/LANGUAGE_POLICY.yaml`
- `ApprovedAssets/README.md`
