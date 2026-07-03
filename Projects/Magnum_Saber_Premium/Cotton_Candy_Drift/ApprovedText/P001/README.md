# Page Module: P001 — Copertina

**Page ID:** P001 (permanent)
**Page Name:** Copertina (Cover)
**SDK Version:** 2.4.0

## Purpose
First page of every Mini4WD manual. Full-bleed visual with model name, paint scheme name, and series identification.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | Cover overlay | Yes |
| `subtitle` | Cover overlay | Yes |
| `series` | Cover overlay (small) | No |
| `footer.page_id` | C002 Footer | Yes |
| `footer.model_name` | C002 Footer | Yes |

## Render Dependencies
- Cover render: `Projects/Magnum_Saber_Premium/Cotton_Candy_Drift/ApprovedImages/P001/cover_3q_v{n}.png`
- Lighting: Studio Neutral
- Layout: Full-bleed

## Related
- `PromptEngine/Cover.md`
- `Core/PAGE_SYSTEM.md §P001`
