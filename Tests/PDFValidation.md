# PDF Validation Tests

**Test Suite ID:** TEST-PD
**SDK Version:** 2.4.0
**Layer:** Export
**Reference:** `Core/PDF_MASTER.md`, `Config/pdf.yaml`, `Templates/PDF_CONFIG.yaml`

## Purpose

Verify that exported PDF files meet all technical requirements for screen, print, and archive variants. This test runs after Phase 5 (PDF Generation) and before Phase 6 (Approval).

## When to Run
- After Phase 5 (PDF Generation) completes
- Before moving any PDF to `Assets/ApprovedManual/`
- After any change to `Config/pdf.yaml` or per-project `pdf_config.yaml`

---

## TEST-PD-001: PDF File Presence

**Input:** `Projects/{ModelName}/Output/`

- [ ] `{modelSlug}_manual_screen_v{n}.pdf` exists
- [ ] `{modelSlug}_manual_print_v{n}.pdf` exists
- [ ] `checksums.sha256` exists
- [ ] Both PDFs are non-zero file size

**Output:** ✅ PASS if both PDFs and checksum present | ❌ FAIL (blocking) if any missing

---

## TEST-PD-002: Metadata Completeness

**Input:** PDF properties (open in Acrobat, Preview, or `exiftool`)
**Reference:** `Config/pdf.yaml §required_metadata`

**Screen variant:**
- [ ] `Title` = "{ModelName} Painting Manual"
- [ ] `Subject` = "Mini4WD Painting Manual"
- [ ] `Author` = value from `PROJECT.yaml §project.author`
- [ ] `Creator` = "Mini4WD Manual SDK v2.4.0"
- [ ] `Keywords` includes: model name, "Mini4WD", "painting"

**Print variant:**
- [ ] All above fields present
- [ ] `PDFVersion` ≥ 1.4 (required for PDF/X-4)

**Archive variant (if present):**
- [ ] `PDFVersion` ≥ 1.4 (required for PDF/A-2b)
- [ ] `XMP metadata` present

How to check with CLI:
```bash
exiftool {modelSlug}_manual_screen_v1.pdf | grep -E "Title|Author|Subject|Creator|Keywords"
```

**Output:** ✅ PASS if all metadata fields present and correct | ❌ FAIL (blocking) if Title or Creator missing

---

## TEST-PD-003: Font Embedding

**Input:** Both PDF variants
**Tool:** Adobe Acrobat (File > Properties > Fonts) or `pdffonts` CLI

- [ ] All fonts listed as "Embedded Subset" or "Embedded"
- [ ] No fonts listed as "Not Embedded"
- [ ] `Bebas Neue` (or fallback `Impact`) embedded
- [ ] `Source Sans Pro` (or fallback `Open Sans`) embedded
- [ ] `JetBrains Mono` (or fallback `Courier New`) embedded

How to check with CLI:
```bash
pdffonts {modelSlug}_manual_screen_v1.pdf
```
Look for "yes" in the "emb" column for all entries.

**Output:** ✅ PASS if all fonts embedded | ❌ FAIL (blocking) if any font not embedded

---

## TEST-PD-004: Page Count and Order

**Input:** Both PDF variants

- [ ] Page count = 10 (standard) or 9 (if `premiumVariant.enabled == false`)
- [ ] Page 1 content = P001 Cover (model name visible)
- [ ] Page 2 content = P002 Color Scheme (palette visible)
- [ ] Pages advance in correct order through P010
- [ ] No blank pages between content pages
- [ ] Last page = P010 Final Checklist

**Output:** ✅ PASS if page count and order correct | ❌ FAIL (blocking) if wrong page count

---

## TEST-PD-005: Bookmark Structure

**Input:** Both PDF variants
**Reference:** `Config/pdf.yaml §page_order[].bookmark_title`

- [ ] Top-level bookmarks present for all pages
- [ ] Bookmark titles match `Config/pdf.yaml` exactly:
  - [ ] Page 1: "Cover"
  - [ ] Page 2: "Color Scheme"
  - [ ] Page 3: "Materials & Tools"
  - [ ] Page 4: "Surface Preparation"
  - [ ] Page 5: "Painting Steps"
  - [ ] Page 6: "Masking Guide"
  - [ ] Page 7: "Detail Painting"
  - [ ] Page 8: "Decal Application"
  - [ ] Page 9: "Premium Finish" (if enabled)
  - [ ] Page 10 (or 9): "Final Checklist"
- [ ] Clicking each bookmark navigates to correct page

**Output:** ✅ PASS if all bookmarks present and navigate correctly | ⚠️ WARNING (non-blocking) if bookmarks missing from screen variant only

---

## TEST-PD-006: Bleed Specification

**Input:** Print variant PDF only
**Reference:** `Config/pdf.yaml §variants.print.bleed_mm`

- [ ] Bleed = 3mm on all four sides
- [ ] Bleed marks (crop marks) visible in PDF
- [ ] Page body content does not extend into 3mm bleed zone
- [ ] Exception: P001 Cover may use full-bleed render (render extends to bleed edge)
- [ ] Screen variant: bleed = 0mm (no crop marks)

**Output:** ✅ PASS if bleed correct | ❌ FAIL (blocking) for print variant if bleed is 0mm

---

## TEST-PD-007: Checksum Verification

**Input:** `checksums.sha256` file, both PDF files

Verify checksums match:
```bash
sha256sum -c checksums.sha256
```

Expected output: `{filename}: OK` for each file.

- [ ] Screen PDF checksum matches
- [ ] Print PDF checksum matches
- [ ] No "FAILED" lines in output

**Output:** ✅ PASS if all checksums match | ❌ FAIL (blocking) if any checksum fails

> ⚠️ **Warning:** A checksum failure means the PDF file was modified after the checksum was recorded. Do not approve a manual with a checksum failure — regenerate the PDF and recompute checksums.

---

## TEST-PD-008: Color Profile

**Input:** Both PDF variants
**Tool:** `exiftool` or Acrobat pre-flight

- [ ] Screen variant color profile = sRGB
- [ ] Print variant color profile = CMYK (FOGRA39 or equivalent)
- [ ] No mixed color spaces in print variant (all objects must be CMYK or convertible)

```bash
exiftool {modelSlug}_manual_print_v1.pdf | grep -i "color"
```

**Output:** ✅ PASS if profiles correct | ❌ FAIL (blocking) if print variant is sRGB
