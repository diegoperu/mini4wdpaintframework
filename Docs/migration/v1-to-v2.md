# Migration Guide: SDK v1.x → v2.x

**Applies to:** Mini4WD Manual SDK v1.x users upgrading to v2.0.0 or later
**Written for:** v2.0.0
**Updated for:** v2.1.0

---

## Overview

SDK v2.0.0 introduced three breaking changes that affect all existing projects:

1. **Component IDs renamed** — `COMP_` prefix replaced with `C###` format
2. **PROJECT.yaml field renamed** — `car_name` renamed to `modelName`
3. **Page IDs changed** — numeric format (`001`) replaced with prefixed format (`P001`)

Additionally, v2.1.0 introduced the Design Token system. This is not a breaking change for existing content, but adopting tokens is strongly recommended for forward compatibility.

This guide walks through each change with before/after examples and a step-by-step migration procedure.

---

## Breaking Changes Summary

| Change | v1.x | v2.x |
|--------|------|------|
| Component ID format | `COMP_HEADER` | `C001` |
| PROJECT.yaml model field | `car_name` | `modelName` |
| Page ID format | `001`, `002` | `P001`, `P002` |
| Component count | 12 | 15 (C013, C014, C015 added) |

---

## Step 1: Audit Your Projects

Before beginning migration, identify all files that need updating:

```bash
# Find all files referencing old component IDs
grep -r "COMP_" Projects/ PromptEngine/ --include="*.md" --include="*.yaml"

# Find all files referencing old car_name field
grep -r "car_name:" Projects/ --include="*.yaml"

# Find all files referencing old page ID format (bare numbers)
grep -rE '"00[0-9]"' Projects/ --include="*.yaml"
```

Save the output — you will work through each hit in the steps below.

---

## Step 2: Rename Component IDs

### Old Format → New Format

| v1 ID | v2 ID | Component Name |
|-------|-------|----------------|
| `COMP_HEADER` | `C001` | Header |
| `COMP_FOOTER` | `C002` | Footer |
| `COMP_PALETTE` | `C003` | Palette |
| `COMP_SHOPPING` | `C004` | Shopping List |
| `COMP_SEQUENCE` | `C005` | Paint Sequence |
| `COMP_CALLOUT` | `C006` | Callout |
| `COMP_EXPLODED` | `C007` | Exploded View |
| `COMP_WARNING` | `C008` | Warning |
| `COMP_TIPS` | `C009` | Tips |
| `COMP_LEGEND` | `C010` | Paint Legend |
| `COMP_PAINTBOX` | `C011` | Paint Code Box |
| `COMP_ZOOM` | `C012` | Zoom |

### New in v2 (no migration needed — these are additions)

| v2 ID | Component Name |
|-------|----------------|
| `C013` | Step Number |
| `C014` | Time Box |
| `C015` | Notes |

### How to Update

In every prompt file and PROJECT.yaml where component IDs appear, perform a find-and-replace:

```bash
# Example using sed (run from repository root)
sed -i 's/COMP_HEADER/C001/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_FOOTER/C002/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_PALETTE/C003/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_SHOPPING/C004/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_SEQUENCE/C005/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_CALLOUT/C006/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_EXPLODED/C007/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_WARNING/C008/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_TIPS/C009/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_LEGEND/C010/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_PAINTBOX/C011/g' PromptEngine/*.md Projects/**/*.yaml
sed -i 's/COMP_ZOOM/C012/g' PromptEngine/*.md Projects/**/*.yaml
```

### Before / After Example

**v1.x (old):**
```yaml
# PROJECT.yaml
pages:
  - id: "001"
    components: [COMP_HEADER, COMP_FOOTER]
```

**v2.x (new):**
```yaml
# PROJECT.yaml
pages:
  - id: "P001"
    components: [C001, C002]
```

---

## Step 3: Update PROJECT.yaml Fields

### Renamed Field: `car_name` → `modelName`

**v1.x (old):**
```yaml
project:
  car_name: "Proto Emperor"
  series: "Championship Series"
  year: 2024
```

**v2.x (new):**
```yaml
project:
  modelName: "Proto Emperor"
  modelSlug: "proto-emperor"      # NEW REQUIRED FIELD in v2
  seriesName: "Championship Series"
  year: "2024"                     # Now a string, not integer
  language: "it"                   # NEW REQUIRED FIELD in v2
  version: "1.0.0"                 # NEW REQUIRED FIELD in v2
  createdAt: "2024-01-15"          # NEW REQUIRED FIELD in v2
  updatedAt: "2024-01-15"          # NEW REQUIRED FIELD in v2
```

### New Required Fields in v2

| Field | Type | Description |
|-------|------|-------------|
| `modelSlug` | string | kebab-case version of modelName (e.g., `"proto-emperor"`) |
| `language` | string | ISO language code (e.g., `"it"`, `"en"`) |
| `version` | string | Manual version in SemVer format |
| `createdAt` | string | ISO date string (YYYY-MM-DD) |
| `updatedAt` | string | ISO date string (YYYY-MM-DD) |
| `sdk_version` | string | SDK version used to generate this manual |

### How to Update

1. Open each `Projects/{ModelName}/PROJECT.yaml`
2. Rename `car_name:` to `modelName:`
3. Rename `series:` to `seriesName:`
4. Add all new required fields (see template at `Templates/PROJECT.yaml`)
5. Change `year:` from integer to quoted string: `year: 2024` → `year: "2024"`

---

## Step 4: Update Page IDs

### Old Format → New Format

| v1 ID | v2 ID |
|-------|-------|
| `"001"` | `"P001"` |
| `"002"` | `"P002"` |
| `"003"` | `"P003"` |
| `"004"` | `"P004"` |
| `"005"` | `"P005"` |
| `"006"` | `"P006"` |
| `"007"` | `"P007"` |
| `"008"` | `"P008"` |
| `"009"` | `"P009"` |
| `"010"` | `"P010"` |

Page IDs appear in:
- `PROJECT.yaml` (page list, dependency references)
- Output file names (e.g., rename `001.png` → `P001.png`)
- Prompt file names in `PromptEngine/` (already updated in v2 SDK files)

### How to Update

```bash
# Rename output files
cd Projects/{ModelName}/Output/
for i in 001 002 003 004 005 006 007 008 009 010; do
  [ -f "${i}.png" ] && mv "${i}.png" "P${i}.png"
done

# Update YAML references
sed -i 's/id: "001"/id: "P001"/g' Projects/**/*.yaml
# Repeat for 002-010
```

---

## Step 5: Adopt Design Tokens (v2.1.0 — Recommended)

This step is not a breaking change — it does not affect rendering of existing pages. However, it is strongly recommended for all new prompt work and future-proofs your content against SDK color or sizing changes.

### What to Do

1. Copy `Assets/DesignSystem/Tokens/tokens.example.yaml` to your project directory as `tokens.override.yaml`
2. Customize any values that differ from the SDK defaults
3. In your prompt files, replace hardcoded values with token references:

**Before (hardcoded):**
```
Header background: #5B2D8E
Header height: 18mm
Body font: Source Sans Pro, 11pt
```

**After (tokens):**
```
Header background: {{token.VioletPrimary}}
Header height: {{token.HeaderHeight}}
Body font: {{token.BodyFont}}, {{token.BodySize}}
```

4. Before submitting prompts to an AI model, substitute token references using the values from your token file.

See `Assets/DesignSystem/Tokens/README.md` for the full token reference.

---

## Step 6: Validate Migration

After completing steps 1–5, run these validation checks:

```bash
# Check no old component IDs remain
grep -r "COMP_" Projects/ PromptEngine/ && echo "FOUND — fix before continuing" || echo "OK"

# Check no old car_name field remains
grep -r "car_name:" Projects/ && echo "FOUND — fix before continuing" || echo "OK"

# Check no old bare page IDs remain
grep -rE '"00[0-9]"' Projects/ && echo "FOUND — fix before continuing" || echo "OK"
```

All three checks must return "OK" before the migration is complete.

---

## Rollback Procedure

If migration causes issues and you need to revert to v1.x:

1. Restore from your backup (you did make a backup, right?)
2. Re-install SDK v1.x by checking out the `v1.x` git tag:
   ```bash
   git checkout v1.0.0 -- Core/ PromptEngine/ Templates/
   ```
3. Your `Projects/` directory files (PROJECT.yaml, etc.) are not tracked in the SDK repo — restore from your own backup

---

## Frequently Asked Questions

**Q: Do I need to regenerate all my manual pages after migration?**
A: Not necessarily. The migration only changes identifiers and field names — it does not change the visual output. Existing approved pages in `Assets/ApprovedManual/` are still valid. You only need to regenerate pages if you want to take advantage of new v2 features (new components C013–C015, design tokens).

**Q: Can I migrate only some projects now and others later?**
A: Yes. The migration is per-project. v2 SDK files (Core/, PromptEngine/, Templates/) are backwards-compatible for generating new pages as long as your PROJECT.yaml uses v2 field names. Old PROJECT.yaml files will produce warnings until migrated.

**Q: My PROJECT.yaml has custom fields not in the migration guide. What do I do?**
A: Custom fields are preserved as-is. The migration only requires the specific field renames documented above. Add new required fields; rename the fields listed; custom fields are unaffected.

**Q: Where can I get help if the migration goes wrong?**
A: Open an issue on the project repository. Include your SDK version before migration, the error you encountered, and the relevant snippet from your PROJECT.yaml.
