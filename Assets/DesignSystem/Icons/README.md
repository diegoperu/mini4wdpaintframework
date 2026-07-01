# Assets/DesignSystem/Icons/

**Version:** 2.4.0
**Status:** Planned for v2.5.0 — not yet included
**Interim solution:** Unicode symbols (documented below)

---

## Status

The icon library for Mini4WD Manual SDK is planned for release in **v2.5.0**. This directory currently contains no SVG files.

Until v2.5.0, all components use Unicode symbols as interim icon representations. These symbols are specified in `Core/COMPONENT_SYSTEM.md` for each component that requires an icon.

See `ROADMAP.md` for the v2.5.0 release timeline.

---

## Interim Unicode Symbols

The following Unicode symbols are the currently approved interim icons for each component:

| Symbol | Unicode | Component | Role |
|--------|---------|-----------|------|
| ℹ | U+2139 | C006 Callout | Informational callout marker |
| ⚠ | U+26A0 | C008 Warning | Warning marker |
| ★ | U+2605 | C009 Tips | Pro tip marker |
| ✓ | U+2713 | C010, P010 | Checklist check |
| ⏱ | U+23F1 | C014 Time Box | Time estimate |
| ✎ | U+270E | C015 Notes | Notes marker |
| ▶ | U+25B6 | C005 Paint Sequence | Step progression arrow |
| ⊕ | U+2295 | C007 Exploded View | Callout dot |
| 🔍 | U+1F50D | C012 Zoom | Zoom indicator |

Use these symbols in the TitleFont or BodyFont SemiBold weight at the component's specified size. Do not style them with custom colors other than those specified in `Core/COMPONENT_SYSTEM.md`.

---

## v2.5.0 Icon Specification

When the icon library is created, every icon must conform to these standards:

### Format
- **Format:** SVG only — no PNG, no WebP, no raster formats
- **Artboard:** 24×24px
- **Viewbox:** `viewBox="0 0 24 24"`
- **Stroke width:** 2px (for outline icons)
- **Fill icons:** flat, single color using `currentColor`
- **No hardcoded colors:** use `currentColor` so icons inherit text color

### Naming Convention
```
icon-{name}.svg
```
Examples:
- `icon-warning.svg`
- `icon-tip.svg`
- `icon-brush.svg`
- `icon-airbrush.svg`

### Required Icons for v2.5.0

| File Name | Used In | Description |
|-----------|---------|-------------|
| `icon-warning.svg` | C008 Warning | Triangle with exclamation mark |
| `icon-tip.svg` | C009 Tips | Star or lightbulb |
| `icon-info.svg` | C006 Callout | Lowercase 'i' in circle |
| `icon-check.svg` | P010 Checklist | Simple checkmark |
| `icon-brush.svg` | P005 Painting | Paintbrush |
| `icon-airbrush.svg` | P005 Painting | Airbrush nozzle |
| `icon-sandpaper.svg` | P004 Preparation | Sanding block |
| `icon-decal.svg` | P008 Decals | Sheet with peel corner |
| `icon-clock.svg` | C014 Time Box | Clock face |
| `icon-star.svg` | C009 Tips | Filled star |
| `icon-zoom.svg` | C012 Zoom | Magnifying glass |
| `icon-notes.svg` | C015 Notes | Pencil |
| `icon-palette.svg` | C003 Palette | Paint palette |
| `icon-arrow-right.svg` | C005 Paint Sequence | Right-pointing arrow |
| `icon-explode.svg` | C007 Exploded View | Four-way explode arrows |

### SVG Template

```svg
<!-- icon-{name}.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"
     aria-hidden="true">
  <!-- icon paths here -->
</svg>
```

---

## Contribution Process

To contribute an icon for the v2.5.0 library:

1. Create the SVG following the specification above
2. Test at 16px, 24px, and 32px to verify legibility at all sizes
3. Validate SVG with `svgo --pretty icon-name.svg` (should reduce size without changing appearance)
4. Open a Pull Request with the file in this directory
5. Include a visual preview in the PR description (inline SVG or screenshot)
6. Reference the component that will use the icon in the PR description

Icons are reviewed for visual consistency with the existing set before merging. The goal is a cohesive family, not a collection of styles.

---

## Using Icons in Prompts

Once icons are available, reference them in prompts as:

```
[ICON: icon-warning.svg, size: 20px, color: {{token.WarningColor}}]
```

Until icons exist, continue using the Unicode symbol equivalents from the interim table above.
