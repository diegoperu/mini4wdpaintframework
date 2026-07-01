# Page Module: P008 — Applicazione Decalcomanie

**Page ID:** P008 (permanent)
**Page Name:** Applicazione Decalcomanie (Decal Application)
**SDK Version:** 2.4.0

## Purpose
Decal inventory and numbered application sequence. Placement zoom panels for precision. Clear coat warning is mandatory.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `decals[].id` | Body table | Yes |
| `decals[].name` | Body table | Yes |
| `decals[].position` | Body table | Yes |
| `decals[].size` | Body table | No |
| `decals[].notes` | C015 Notes Panel | No |
| `application_steps[].step` | C013 Step Badge | Yes |
| `application_steps[].description` | Body text | Yes |
| `warnings` | C008 Warning Box | Yes |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P008_decal_placement.png` — annotated placement view (optional)
- `P008_decal_zoom.png` — close-up application detail (optional, C012)

## Related
- `PromptEngine/Decals.md`
- `Core/PAGE_SYSTEM.md §P008`
