# Page Module: P007 — Verniciatura dei Dettagli

**Page ID:** P007 (permanent)
**Page Name:** Verniciatura dei Dettagli (Detail Painting)
**SDK Version:** 2.4.0

## Purpose
Fine detail painting guide for interior panels, edges, and decorative elements. Each area references a color from P002 via color_id.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `areas[].id` | C013 Step Badge | Yes |
| `areas[].name` | Body text | Yes |
| `areas[].color_id` | C011 Paint Code Box (via P002) | Yes |
| `areas[].technique` | Body text | Yes |
| `areas[].description` | Body text | Yes |
| `areas[].notes` | C015 Notes Panel | No |
| `warnings` | C008 Warning Box | No |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P007_detail_zoom.png` — close-up detail area (optional, C012)

## Related
- `PromptEngine/Details.md`
- `Core/PAGE_SYSTEM.md §P007`
- `ApprovedAssets/Text/P002/content.yaml` — color_id must resolve here
