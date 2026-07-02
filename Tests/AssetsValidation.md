# Assets Validation Tests

**Test Suite ID:** TEST-AS
**SDK Version:** 2.4.0
**Layer:** Assets
**Reference:** `Assets/README.md`, `Core/RENDER_GUIDE.md §5`, `Core/NAMING_CONVENTION.md`, `Config/render.yaml §resolution`

## Purpose

Verify that all required asset files are present, correctly named, meet format specifications, and that no orphaned or stale files exist in the asset directories.

## When to Run
- After Phase 1 (Reference Models) — verify reference images
- After Phase 3 (Render Engine) — verify output renders
- Before Phase 6 (Approval) — full asset inventory
- Periodically to detect orphaned files

---

## TEST-AS-001: Design System Token Files

**Input:** `Assets/DesignSystem/Tokens/`

- [ ] `tokens.example.yaml` exists and is non-empty
- [ ] `tokens.schema.yaml` exists and is non-empty
- [ ] Both files are valid YAML (no parse errors)
- [ ] `tokens.example.yaml` validates against `tokens.schema.yaml`
- [ ] `tokens.example.yaml §tokens.colors.neutral.White` = `#FFFFFF`

How to check YAML validity:
```bash
python3 -c "import yaml; yaml.safe_load(open('Assets/DesignSystem/Tokens/tokens.example.yaml'))" && echo "VALID"
```

**Output:** ✅ PASS if both files valid | ❌ FAIL (blocking) if either file invalid or missing

---

## TEST-AS-002: Project Reference Images

**Input:** `Projects/{ModelName}/Images/` (operator projects — single convention v2.4.1; `Assets/ReferenceModels/{ModelName}/` for SDK reference projects only)
**Reference:** `Assets/ReferenceModels/README.md §Required Angles`

For each project being validated:
- [ ] `reference_front.jpg` exists
- [ ] `reference_side.jpg` exists
- [ ] `reference_top.jpg` exists
- [ ] `README.md` exists in directory
- [ ] All images ≥ 800×600px
- [ ] All images are JPG format (reference photography — JPG is OK)
- [ ] No visible watermarks

Optional files (warn if missing, not blocking):
- [ ] `box_art.jpg`
- [ ] `official_render.jpg`

**Output:** ✅ PASS if 3 required images and README present | ❌ FAIL (blocking) if any required image missing

---

## TEST-AS-003: Project Output Render Images

**Input:** `Projects/{ModelName}/Images/`
**Reference:** `Config/render.yaml §resolution`

**Required renders (minimum):**
- [ ] `cover_3q.png` — width ≥ 2480px, height ≥ 3508px
- [ ] `P002_front.png` — width ≥ 1000px, height ≥ 800px
- [ ] `P002_side.png` — width ≥ 1000px, height ≥ 800px
- [ ] `P002_top.png` — width ≥ 1000px, height ≥ 800px

For all render images:
- [ ] Format is PNG
- [ ] Background is white (#FFFFFF ±5 per channel)
- [ ] No motion blur or compression artifacts
- [ ] File size is reasonable (cover: 2–15MB, body renders: 0.5–5MB)

How to check dimensions:
```bash
identify -format "%f: %wx%h\n" Projects/{ModelName}/Images/*.png
# requires ImageMagick
```

**Output:** ✅ PASS if all required renders present and valid | ❌ FAIL (blocking) if cover render missing or undersized

---

## TEST-AS-004: Approved Manual Package

**Input:** `Assets/ApprovedManual/{ModelName}/`
**Note:** Run this test ONLY after Phase 6 (Approval) is declared complete

Required files:
- [ ] `P001.png` through `P010.png` all present (or P009.png present if premium enabled)
- [ ] All page PNGs ≥ minimum body page resolution (1240×1754px)
- [ ] `{modelSlug}_manual_screen_v{n}.pdf` present
- [ ] `{modelSlug}_manual_print_v{n}.pdf` present
- [ ] `checksums.sha256` present
- [ ] `PROJECT.yaml` snapshot present (copy from project, not symlink)
- [ ] `qa_log.md` present and shows Final Status: PASSED
- [ ] `README.md` present with approval date, reviewer name, and SDK version

**Output:** ✅ PASS if all required files present and QA log shows PASSED | ❌ FAIL (blocking) if any file missing

---

## TEST-AS-005: No Orphaned or Stale Files

**Input:** Entire `Assets/` directory tree

- [ ] No `.DS_Store` files anywhere in Assets/
- [ ] No `Thumbs.db` files anywhere in Assets/
- [ ] No `*_backup.*` files in `Assets/ApprovedManual/`
- [ ] No `*.tmp` files
- [ ] No image files in directory roots (all images must be inside named subdirectories)
- [ ] Every subdirectory in `Assets/ReferenceModels/` has a `README.md`
- [ ] Every subdirectory in `Assets/ApprovedManual/` has a `README.md`

How to check for .DS_Store:
```bash
find Assets/ -name ".DS_Store" -o -name "Thumbs.db" | wc -l
# Should be 0
```

**Output:** ✅ PASS if no stale files found | ⚠️ WARNING (non-blocking) if `.DS_Store` found (delete and continue)

---

## TEST-AS-006: DesignSystem Directory READMEs

**Input:** `Assets/DesignSystem/` and all subdirectories

- [ ] `Assets/DesignSystem/README.md` exists
- [ ] `Assets/DesignSystem/Tokens/README.md` exists
- [ ] `Assets/DesignSystem/Components/README.md` exists
- [ ] `Assets/DesignSystem/Palette/README.md` exists
- [ ] `Assets/DesignSystem/Typography/README.md` exists
- [ ] `Assets/DesignSystem/Icons/README.md` exists
- [ ] `Assets/DesignSystem/Layout/README.md` exists

**Output:** ✅ PASS if all READMEs present | ⚠️ WARNING (non-blocking) if any missing

**Common Errors:**
- Renders left in project root (`/`) instead of `Projects/{ModelName}/Images/`
- Approved pages not moved from `Output/` to `Assets/ApprovedManual/` before closing phase
- Reference images incorrectly placed in `Assets/ApprovedManual/` instead of `Assets/ReferenceModels/`
