# Page Module: P002 — Schema Colori

**Page ID:** P002 (permanent)
**Page Name:** Schema Colori (Color Scheme)
**SDK Version:** 2.4.0

## Purpose
Documents the complete paint scheme: all colors, paint codes, finish types, and 3-view orthographic renders of the model.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header, page title | Yes |
| `intro` | Body text | No |
| `colors[].name` | C003 Palette, C010, C011 | Yes |
| `colors[].paint_code` | C011 Paint Code Box | Yes |
| `colors[].paint_brand` | C011 Paint Code Box | Yes |
| `colors[].finish` | C011, C010 | Yes |
| `colors[].hex` | C003 Palette swatch | No |
| `colors[].notes` | C015 Notes | No |
| `color_notes` | C006 Callout | No |
| `palette_overview` | C003 intro | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P002_front.png` — orthographic front
- `P002_side.png` — orthographic right
- `P002_top.png` — orthographic top

## Related
- `PromptEngine/ColorScheme.md`
- `Core/PAGE_SYSTEM.md §P002`
