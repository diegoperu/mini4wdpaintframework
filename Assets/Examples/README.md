# Assets/Examples/

**Version:** 2.1.0
**Managed by:** SDK Core Team only
**Status:** No examples included in v2.1.0 — planned for v2.2.0

---

## Purpose

`Examples/` contains SDK-maintained sample outputs for every page type (P001–P010). These samples represent the **target visual quality** for AI-generated pages. Use them as a reference when evaluating whether a generated page meets the SDK's standards.

Examples are not project-specific. They show an idealized version of each page type using a fictional or demo model, demonstrating correct layout, typography, component usage, and design token application.

---

## Status: v2.1.0

No example files are included in this release. The first set of examples is planned for **v2.2.0** (see `ROADMAP.md`).

Until examples are available:
- Use `Core/COMPONENT_SYSTEM.md` wireframes as your visual reference
- Use `Assets/DesignSystem/Layout/README.md` for layout pattern diagrams
- Use `Assets/DesignSystem/Components/README.md` for component wireframes

---

## Planned Contents (v2.2.0)

When examples are released, each page type will have one approved example file:

| File | Page Type | Description |
|------|-----------|-------------|
| `P001_example.png` | Cover | Demo model, full-bleed render, primary-color header, display title |
| `P002_example.png` | Color Scheme | 3-view renders, color legend, paint code boxes |
| `P003_example.png` | Materials | Shopping list in two-column layout, safety warnings |
| `P004_example.png` | Preparation | Numbered steps, exploded view, time boxes |
| `P005_example.png` | Painting | Paint sequence steps, color swatches, drying time warnings |
| `P006_example.png` | Masking | Annotated render with masking zones, zoom for complex areas |
| `P007_example.png` | Details | Close-up renders for cockpit, wheels, rear wing |
| `P008_example.png` | Decals | Placement guide, zoom views, application order |
| `P009_example.png` | Premium Variant | Pearl finish technique, comparison panel |
| `P010_example.png` | Final Checklist | Two-column checklist, sign-off zone |

---

## How to Use Examples

When evaluating a generated page:

1. Open the corresponding example file (e.g., `P002_example.png` for a color scheme page)
2. Compare against these criteria:
   - **Layout:** Does the generated page match the layout pattern? (See `Assets/DesignSystem/Layout/README.md`)
   - **Header/Footer:** Are C001 and C002 present and correctly styled?
   - **Typography:** Do font sizes and weights match the type scale?
   - **Color:** Are colors from the approved palette? No rogue hex values?
   - **Components:** Are all required components present for this page type?
3. Document any deviations in `Projects/{ModelName}/Notes/qa_log.md`

---

## Contributing an Example

To contribute an example for the SDK library:

1. The example must come from a fully approved manual (in `Assets/ApprovedManual/`)
2. The model owner must provide explicit consent for the page to be used as an SDK example
3. Sensitive model information (custom color recipes, proprietary techniques) should be generalized
4. Open a Pull Request with the file named `P{NNN}_example.png`
5. The PR must include a note in the PR description confirming model-owner consent
6. Examples are reviewed by the SDK Core Team for visual quality before merging

One example per page type is maintained by the Core Team. Community examples may be accepted in a future `Examples/Community/` subdirectory.

---

## Quality Standard for Examples

An example file is only accepted if it demonstrates:

- [ ] Zero QA_SYSTEM.md failures
- [ ] Correct use of all design tokens (no hardcoded values visible)
- [ ] All required components for that page type present
- [ ] Render meets RENDER_GUIDE.md §5 resolution requirements
- [ ] Typography matches STYLE_GUIDE.md §2–3 exactly
- [ ] Layout matches one of the four patterns in Layout/README.md
