# PDF Master

This document specifies all requirements for the PDF export of Mini4WD manuals. A manual PDF is the final deliverable. The specifications here define two variants: one optimized for screen viewing and one ready for professional offset printing.

Configuration for the export is set in `Templates/PDF_CONFIG.yaml`.

---

## 1. PDF Variants

Every approved manual must be exported in both variants before it can be published.

| Variant | File Suffix | Standard | Use Case |
|---|---|---|---|
| Screen | `_screen` | PDF/A-2b | Digital distribution, web download |
| Print | `_print` | PDF/X-4 | Professional offset printing |

Example file names:
```
proto-emperor_manual_screen_v1.pdf
proto-emperor_manual_print_v1.pdf
```

---

## 2. PDF Standards

### Screen Variant: PDF/A-2b
- **Purpose:** Archival — guarantees the file will render correctly in any PDF viewer indefinitely
- **Color space:** sRGB
- **Fonts:** All fonts embedded as subsets
- **Images:** Maximum compression that preserves visual quality (JPEG quality 90 for photographs, lossless PNG for vector-based elements)
- **Encryption:** None (PDF/A prohibits encryption)
- **PDF version:** 1.7

### Print Variant: PDF/X-4
- **Purpose:** Print-ready — guarantees correct output on commercial offset presses
- **Color space:** CMYK FOGRA39 (ISO Coated v2 300%)
- **Fonts:** All fonts embedded as subsets
- **Images:** Minimum 300 dpi at final printed size, no downsampling
- **Encryption:** None
- **PDF version:** 1.6 minimum
- **Output intent:** ISO Coated v2 300% (FOGRA39)

---

## 3. Color Profiles

| Variant | RGB Profile | CMYK Profile |
|---|---|---|
| Screen | sRGB IEC61966-2.1 | n/a |
| Print | n/a | ISO Coated v2 300% (FOGRA39) |

> ⚠️ **Warning:** Converting RGB violet (#5B2D8E) to CMYK FOGRA39 produces approximately C:64 M:84 Y:0 K:12. The CMYK equivalent is slightly less saturated than the sRGB original. Always request a print proof before mass printing. The Pantone reference (2627 C) may be used as a spot color specification for the violet if the printer supports it.

---

## 4. Bleed

Print variant only. Screen variant has no bleed.

| Edge | Bleed |
|---|---|
| All sides | 3mm |

Elements that extend to the page edge (header band, footer band, side panel on pages that use it) must extend 3mm beyond the trim mark. Interior elements must remain within the safe area (8mm inside the trim mark).

```
┌─────────────────────────────────────────────────┐  ← Bleed edge
│ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅  ← Trim mark
│ ⋅ ┌──────────────────────────────────────┐ ⋅  ← Safe area (8mm in)
│ ⋅ │                                      │ ⋅
│ ⋅ │         CONTENT AREA                 │ ⋅
│ ⋅ │                                      │ ⋅
│ ⋅ └──────────────────────────────────────┘ ⋅
│ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅
└─────────────────────────────────────────────────┘  ← Bleed edge
```

---

## 5. Page Order

The page order in the PDF is defined by `Templates/PDF_CONFIG.yaml`. The default order is:

```yaml
pageOrder:
  - P001  # Cover (required)
  - P002  # Color Scheme (required)
  - P003  # Materials (required)
  - P004  # Preparation (required)
  - P005  # Painting (required)
  - P006  # Masking (required)
  - P007  # Details (required)
  - P008  # Decals (required)
  # P009 is optional — include only if the project has a premium variant
  - P010  # Final Checklist (required)
```

If P009 is included:
```yaml
pageOrder:
  - P001
  - P002
  - P003
  - P004
  - P005
  - P006
  - P007
  - P008
  - P009  # Premium Variant (optional)
  - P010
```

The page count must be 10 (standard) or 11 (with premium variant). Deviations require a project-level note in `Projects/{ModelName}/Notes/decisions.md`.

---

## 6. PDF Metadata

All metadata fields are required. Missing metadata is a QA failure (QA-096 through QA-100).

| Field | Value Template | Example |
|---|---|---|
| Title | `{{project.modelName}} — {{project.paintScheme.name}} — Mini4WD Manual` | "Proto Emperor — Midnight Violet — Mini4WD Manual" |
| Author | `{{project.author}}` | "Studio Tamiya Fans" |
| Subject | `Mini4WD painting manual — {{project.series}} chassis` | "Mini4WD painting manual — Super-II chassis" |
| Keywords | `mini4wd, tamiya, painting, {{project.modelName}}, {{project.paintScheme.name}}` | "mini4wd, tamiya, painting, proto emperor, midnight violet" |
| Creator | `Mini4WD Manual SDK v{{sdkVersion}}` | "Mini4WD Manual SDK v2.1.0" |
| Producer | Set by export tool | Set automatically |
| Creation Date | `{{project.createdDate}}` | "2024-01-20" |

---

## 7. Bookmark Structure

The PDF must include a bookmark tree for navigation. Screen variant only (print variant does not require bookmarks).

```
Manual Root
├── Cover
├── Color Scheme
├── Materials
├── Preparation
├── Painting
├── Masking
├── Details
├── Decals
[├── Premium Variant]  (optional)
└── Final Checklist
```

Bookmarks must link to the exact page, not to the top of the PDF.

---

## 8. Font Embedding Requirements

All fonts used in the manual must be embedded as subsets in the PDF. A PDF that references system fonts without embedding them is a QA failure.

Required fonts to embed:
- `Bebas Neue` (Title Font) — or confirmed substitute
- `Source Sans Pro` (Body Font) — Regular, SemiBold, Bold weights
- `JetBrains Mono` (Mono Font) — Regular weight minimum

> 📝 **Note:** Bebas Neue and Source Sans Pro are available under the SIL Open Font License and can be embedded freely. JetBrains Mono is available under the Apache License 2.0. Always verify font license compatibility before embedding in a distributed PDF.

---

## 9. Export Tools

The following tools are validated for producing SDK-compliant PDFs. Other tools may work but are not tested.

### Affinity Publisher 2
**Recommended.** Full PDF/X-4 and PDF/A-2b support, CMYK color management, bleed/trim mark generation.
- Export via: `File → Export → PDF (Print)` for print variant
- Export via: `File → Export → PDF (Digital - High Quality)` for screen variant
- Apply FOGRA39 ICC profile at export time

### Adobe InDesign
Full PDF/X-4 support. Requires licensed subscription.
- Export via: `File → Export → Adobe PDF (Print)` → Preset: `[PDF/X-4:2008]`
- For PDF/A: use `Acrobat Distiller` post-export conversion

### Scribus (Open Source)
Free and open source. PDF/X-3 support (not X-4). Acceptable for print variant when PDF/X-4 is not required.
- Export via: `File → Export → Save as PDF` → PDF 1.4, PDF/X-3

### pandoc + LaTeX (pdflatex / xelatex)
Suitable for screen variant / PDF/A. Not recommended for print due to CMYK limitations.
- Requires custom LaTeX template
- Use `xelatex` for custom font support
- PDF/A output via `pdfx` LaTeX package

Full configuration examples are provided in `Docs/guides/pdf-export.md`.

---

## 10. Print-Ready vs Screen-Optimized Differences

| Property | Screen | Print |
|---|---|---|
| Color space | sRGB | CMYK FOGRA39 |
| Standard | PDF/A-2b | PDF/X-4 |
| Bleed | None | 3mm all sides |
| Trim marks | None | Included |
| Image resolution | 96–150 dpi (downsampled) | 300 dpi minimum (no downsample) |
| File size | ~5–15 MB typical | ~30–80 MB typical |
| Encryption | Not applicable | Prohibited |
| Bookmarks | Required | Optional |
| Hyperlinks | Active (if included) | Inactive (print ignores) |
| Black text rendering | sRGB composite | 100K black (no rich black for text) |

> ⚠️ **Warning:** Rich black (#1A1A1A body text) in the screen variant converts to approximately C:0 M:0 Y:0 K:90 in CMYK. This is correct for body text. Do NOT use rich black (e.g., C:60 M:40 Y:40 K:100) for body text — it causes misregistration and text fringing in offset printing.
