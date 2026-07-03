# Page Module: P003 — Materiali e Strumenti

**Page ID:** P003 (permanent)
**Page Name:** Materiali e Strumenti (Materials & Tools)
**SDK Version:** 2.4.0

## Purpose
Lists all paints, tools, and consumables required to complete the paint job. Safety notes mandatory.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `paints[].name` | C004 Materials Table | Yes |
| `paints[].code` | C004 Materials Table | Yes |
| `paints[].brand` | C004 Materials Table | Yes |
| `paints[].finish` | C004 Materials Table | Yes |
| `tools[].name` | C004 Materials Table | Yes |
| `tools[].type` | C004 Materials Table | Yes |
| `consumables[].name` | C004 Materials Table | Yes |
| `safety_notes` | C008 Warning Box | Yes |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- No render images required — table-only layout

## Related
- `PromptEngine/Materials.md`
- `Core/PAGE_SYSTEM.md §P003`
- `Projects/Magnum_Saber_Premium/Cotton_Candy_Drift/ApprovedText/P002/content.yaml` — colors referenced here must match P002
