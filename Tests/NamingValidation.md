# Naming Convention Validation Tests

**Test Suite ID:** TEST-NM
**SDK Version:** 2.2.0
**Layer:** Filesystem
**Reference:** `Core/NAMING_CONVENTION.md`, `Config/sdk.yaml §naming`

## Purpose

Verify that all files, directories, and configuration values follow the SDK naming conventions defined in `Core/NAMING_CONVENTION.md`. Correct naming is required for automated tools, cross-references, and long-term maintainability.

## When to Run
- When a new project directory is created
- Before Phase 2 (to catch bad image names from Phase 1)
- When contributing new files to the SDK itself

---

## TEST-NM-001: Project Directory Name

**Input:** `Projects/` directory listing
**Reference:** `Core/NAMING_CONVENTION.md §Project Directories`
**Rule:** Directory name must use official model name with underscores for spaces, each word capitalized

Verify for each project directory:
- [ ] No spaces in directory name
- [ ] Uses underscores `_` for word separation (NOT hyphens)
- [ ] Each word starts with a capital letter
- [ ] Matches official Tamiya product name exactly (check against `PROJECT.yaml §project.modelName`)

| Valid | Invalid |
|-------|---------|
| `Proto_Emperor` | `proto-emperor` |
| `Dash_Yonkuro` | `dash_yonkuro` |
| `Ray_Stinger` | `Ray Stinger` |
| `Thunder_Shot` | `thundershot` |

**Output:** ✅ PASS if all project directories comply | ❌ FAIL (blocking) if spaces in directory names

---

## TEST-NM-002: PROJECT.yaml modelSlug Field

**Input:** `Projects/{ModelName}/PROJECT.yaml §project.modelSlug`
**Reference:** `Config/sdk.yaml §project_schema.model_slug_pattern`
**Rule:** `project.modelSlug` must be kebab-case, all lowercase

Verify:
- [ ] All characters are lowercase
- [ ] Only `a-z`, `0-9`, and `-` characters
- [ ] Does not start with `-` or end with `-`
- [ ] Matches pattern `^[a-z0-9][a-z0-9-]*[a-z0-9]$`
- [ ] modelSlug is a kebab-case version of the directory name

| Valid | Invalid |
|-------|---------|
| `proto-emperor` | `Proto_Emperor` |
| `dash-yonkuro` | `dash_yonkuro` |
| `ray-stinger` | `RAY-STINGER` |

**Output:** ✅ PASS if slug is valid | ❌ FAIL (blocking) if pattern fails

---

## TEST-NM-003: Output Image File Names

**Input:** `Projects/{ModelName}/Images/`, `Projects/{ModelName}/Output/`
**Reference:** `Config/sdk.yaml §naming.page_output_pattern`
**Rule:** `{modelSlug}_{pageId}_{variant}_v{n}.png`

Verify each output image:
- [ ] Starts with `{modelSlug}` in kebab-case (matches `project.modelSlug`)
- [ ] Contains valid page ID `P001`–`P010`
- [ ] Contains variant descriptor (e.g., `colorscheme`, `cover`, `masking-zone-1`)
- [ ] Ends with version suffix `_v{n}` where n is a positive integer
- [ ] Extension is `.png` (lowercase)

| Valid | Invalid |
|-------|---------|
| `proto-emperor_P002_colorscheme_v1.png` | `ProtoEmperor_page2.PNG` |
| `proto-emperor_P001_cover_v2.png` | `cover.png` |
| `proto-emperor_P007_detail-wheel_v1.png` | `P007-detail.png` |

**Output:** ✅ PASS if all images follow pattern | ⚠️ WARNING (non-blocking) for minor deviations

---

## TEST-NM-004: Core Document Names

**Input:** `Core/` directory listing
**Reference:** `Core/NAMING_CONVENTION.md §Core Documents`
**Rule:** All Core/ documents must be SCREAMING_SNAKE_CASE with `.md` extension

Verify:
- [ ] All characters before `.md` are uppercase or `_`
- [ ] Words separated by `_` only
- [ ] Extension is `.md` (lowercase)
- [ ] No spaces or hyphens in filename

| Valid | Invalid |
|-------|---------|
| `DESIGN_LANGUAGE.md` | `DesignLanguage.md` |
| `QA_SYSTEM.md` | `qa-system.md` |
| `PAGE_SYSTEM.md` | `Page System.md` |

**Output:** ✅ PASS if all Core/ docs comply | ❌ FAIL (blocking) if any Core doc uses wrong case

---

## TEST-NM-005: Config File Names

**Input:** `Config/` directory listing
**Reference:** `Core/NAMING_CONVENTION.md §Config Files`
**Rule:** Config files must be lowercase snake_case with `.yaml` extension (not `.yml`)

Verify:
- [ ] All characters are lowercase or `_`
- [ ] Extension is `.yaml` — `.yml` is not accepted
- [ ] No uppercase, hyphens, or spaces

| Valid | Invalid |
|-------|---------|
| `sdk.yaml` | `SDK.yaml` |
| `render.yaml` | `render.yml` |
| `pdf.yaml` | `PDF-Config.yaml` |
| `quality.yaml` | `Quality.yaml` |

**Output:** ✅ PASS if all Config/ files comply | ❌ FAIL (blocking) if `.yml` extension used

---

## TEST-NM-006: PDF Output File Names

**Input:** `Projects/{ModelName}/Output/` PDF files
**Reference:** `Config/sdk.yaml §naming.pdf_screen_pattern`, `§pdf_print_pattern`

- [ ] Screen PDF: `{modelSlug}_manual_screen_v{n}.pdf`
- [ ] Print PDF: `{modelSlug}_manual_print_v{n}.pdf`
- [ ] Archive PDF (if present): `{modelSlug}_manual_archive_v{n}.pdf`
- [ ] Checksum file: `checksums.sha256`
- [ ] All extensions lowercase

**Output:** ✅ PASS if all PDF names comply | ⚠️ WARNING (non-blocking) for archive PDF if missing
