# Component System

Components are the reusable building blocks of every manual page. A page is not designed from scratch — it is assembled from components. Every visual element that appears on more than one page must be a component.

Components are identified by permanent IDs in the format `C###`. These IDs never change.

See also: `PAGE_SYSTEM.md` for which components each page uses, `Assets/DesignSystem/Tokens/` for token values.

---

## Component Registry

| ID | Name | Required On | Token Refs |
|---|---|---|---|
| C001 | Header | All pages | VioletPrimary, HeaderHeight, TitleFont |
| C002 | Footer | All pages | FooterHeight, Black, LightGray |
| C003 | Palette | P002, P009 | White, LightGray |
| C004 | Shopping List | P003 | OffWhite, LightGray |
| C005 | Paint Sequence | P004, P005 | VioletPrimary, OffWhite |
| C006 | Callout | P004–P008 | BlueInfo, OffWhite |
| C007 | Exploded View | P006 | LightGray, Black |
| C008 | Warning | P003–P008 | RedWarning, White |
| C009 | Tips | P004–P009 | GoldAccent, White |
| C010 | Paint Legend | P002 | White, LightGray |
| C011 | Paint Code Box | P002, P005–P007 | VioletDark, OffWhite, MonoFont |
| C012 | Zoom | P006–P008 | LightGray, Black |
| C013 | Step Number | P004–P008 | VioletPrimary, White, TitleFont |
| C014 | Time Box | P004–P006 | OffWhite, LightGray, MidGray |
| C015 | Notes | P010 | OffWhite, LightGray |

---

## C001 — Header

**Description:** The top band of every page. Contains the brand mark on the left, an optional series name in the center, and a page type label on the right. The violet background is the primary visual signal that this page belongs to the Mini4WD Manual SDK.

**Dimensions:** Full page width × 18mm height (`{{token.HeaderHeight}}`)

**Background:** `{{token.VioletPrimary}}` (#5B2D8E)

**Layout:**
- Left zone (25% width): SDK logo mark (20×18mm, white) + "Mini4WD Manual" wordmark in TitleFont, 14pt, white
- Center zone (50% width): Series name in H3 (22pt), white, centered. Optional — omit if series name is empty.
- Right zone (25% width): Page type label (e.g., "COLOR SCHEME") in Label font (8pt), uppercase, white, right-aligned

**Variants:**
- `standard`: White text on VioletPrimary, right zone shows page type label
- `cover`: Right zone is empty. Center zone may show the series name at larger scale.

**Token References:** `{{token.VioletPrimary}}`, `{{token.HeaderHeight}}`, `{{token.TitleFont}}`, `{{token.BodyFont}}`

**Dependencies:** `tokens.example.yaml`, `Core/COLOR_SYSTEM.md` §2

**Best Practice:** The right-zone label must match the page ID exactly (e.g., the header on P002 reads "COLOR SCHEME", not "Color Scheme" or "Colors"). Use the label names defined in `PAGE_SYSTEM.md`.

**Common Errors:** Using a gradient instead of solid VioletPrimary; wrong font weight for the page label (must be SemiBold 600); reducing header height below 18mm.

**Wireframe:**
```
╔══════════════════════════════════════════════════════════╗
║  [LOGO] Mini4WD Manual    Series Name      COLOR SCHEME ║  18mm
╚══════════════════════════════════════════════════════════╝
```

---

## C002 — Footer

**Description:** The bottom band of every page. Contains the page number and optional copyright or version information. The footer is white with a thin violet rule at the top edge.

**Dimensions:** Full page width × 12mm height (`{{token.FooterHeight}}`)

**Background:** `{{token.White}}`

**Border:** Top edge: 1.5pt solid `{{token.VioletPrimary}}`

**Layout:**
- Left zone: "Mini4WD Manual SDK" in Caption font (9pt), MidGray
- Center zone: Optional project-level subtitle or empty
- Right zone: Page number in format "P001" in Label font (8pt), VioletPrimary, right-aligned

**Variants:**
- `standard`: As described above
- `print`: Adds "Printed: {date}" in MidGray at far right, before page number

**Token References:** `{{token.FooterHeight}}`, `{{token.VioletPrimary}}`, `{{token.MidGray}}`, `{{token.BodyFont}}`

**Common Errors:** Missing the top violet rule; using the manual name instead of "Mini4WD Manual SDK" in the left zone; incorrect page ID format (must be P001, not 1 or 01).

**Wireframe:**
```
──────────────────────────────────────────────────────────  ← 1.5pt violet rule
 Mini4WD Manual SDK                                  P002   12mm
```

---

## C003 — Palette

**Description:** A row of color swatches representing the complete paint scheme for a model. Used on P002 and P009 to give an immediate visual summary of the color scheme.

**Dimensions:** Full main content width × variable height (minimum 24mm per swatch row)

**Background:** `{{token.White}}`

**Layout:**
- Each color is a rectangular swatch: 20mm wide × 20mm tall
- Below each swatch: color name in Caption (9pt), Black
- Below color name: paint code in Mono font (8pt), VioletDark
- Swatches are arranged in a horizontal row, left to right in application order
- If more than 6 colors, wrap to a second row

**Variants:**
- `horizontal`: Single row (default)
- `grid`: 3-column grid for schemes with 7+ colors

**Token References:** `{{token.White}}`, `{{token.LightGray}}`, `{{token.MonoFont}}`, `{{token.BorderRadius}}`

**Common Errors:** Swatch colors that do not match the actual paint; missing paint codes; swatches too small to distinguish similar colors (minimum 20×20mm).

**Wireframe:**
```
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ ████ │ │ ████ │ │ ████ │ │ ████ │
│ ████ │ │ ████ │ │ ████ │ │ ████ │
└──────┘ └──────┘ └──────┘ └──────┘
Metallic   Chrome    Flat    Pearl
 Violet    Silver    Black   White
  TS-83    TS-30     TS-80   TS-55
```

---

## C004 — Shopping List

**Description:** A structured list of all materials required for the project. Each item includes: category, item name, quantity, and optional supplier note.

**Dimensions:** Full main content width × variable height

**Background:** `{{token.OffWhite}}` (table rows alternate White / OffWhite)

**Layout:**
- Table with 4 columns: Category | Item | Qty | Notes
- Header row: VioletPrimary background, white Label text
- Body rows: alternating White and OffWhite backgrounds
- Category rows span all 4 columns with VioletLight background

**Variants:**
- `compact`: 3 columns (no Notes column) for short lists
- `full`: 4 columns (default)

**Token References:** `{{token.OffWhite}}`, `{{token.VioletPrimary}}`, `{{token.VioletLight}}`, `{{token.LightGray}}`

**Common Errors:** Items not categorized (reader cannot scan quickly); missing quantities; using a freeform list instead of the table structure.

---

## C005 — Paint Sequence

**Description:** A numbered sequence diagram showing the order of paint application. Each step is a rectangle with a color swatch, step number, and brief instruction.

**Dimensions:** Full main content width × variable height (approximately 18mm per step)

**Background:** `{{token.White}}`

**Layout:**
- Vertical sequence, top to bottom
- Each step: [C013 Step Number] + [20mm color swatch] + [Step title in H3] + [Instruction in Body]
- Arrow connecting each step to the next (VioletPrimary, 1.5pt)
- Drying time appears as C014 Time Box to the right of the step

**Token References:** `{{token.VioletPrimary}}`, `{{token.OffWhite}}`, `{{token.Black}}`

**Common Errors:** Missing arrows between steps; combining multiple colors in one step; no drying times.

---

## C006 — Callout

**Description:** An informational callout box for supplementary information that is useful but not critical. Distinguished from C008 Warning (critical) and C009 Tips (best practice) by its blue accent.

**Dimensions:** Full main content width or 8 columns × variable height (minimum 2 lines of body text)

**Background:** `{{token.OffWhite}}`

**Border:** Left edge: 4px solid `{{token.BlueInfo}}`

**Layout:**
- Left: BlueInfo icon (information "i", 16×16px) with 8px padding
- Content: Title in H3 (optional), body text in Body font
- Border radius: 4px on right corners only

**Variants:**
- `with-title`: Includes an H3 title above the body text
- `inline`: No title, body text only

**Token References:** `{{token.BlueInfo}}`, `{{token.OffWhite}}`, `{{token.BorderRadius}}`

**Common Errors:** Using C006 for warnings (use C008 instead); using C006 for tips (use C009 instead); omitting the blue icon.

---

## C007 — Exploded View

**Description:** A diagram showing the model body with individual components separated and labeled. Used on P006 Masking to show tape placement zones.

**Dimensions:** 8 columns wide × variable height

**Background:** `{{token.White}}`

**Layout:**
- Main diagram: isometric or top-down view of model with parts separated
- Leader lines: 0.5pt `{{token.LightGray}}` connecting parts to labels
- Labels: Caption (9pt), Black, on white background
- Part numbers: Mono font, VioletDark

**Variants:**
- `masking`: Shows masking tape zones highlighted in GoldAccent at 40% opacity
- `assembly`: Standard exploded view without masking zones

**Common Errors:** Crowded labels that overlap; missing leader lines (reader cannot trace which label belongs to which part).

---

## C008 — Warning

**Description:** A warning box for safety-critical or damage-risk information. Must be used whenever the reader faces a risk of injury, material damage, or irreversible error.

**Dimensions:** Full main content width × variable height (minimum 2 lines)

**Background:** `{{token.White}}`

**Border:** Left edge: 4px solid `{{token.RedWarning}}`

**Layout:**
- Left: RedWarning icon (warning triangle, 16×16px) with 8px padding
- Title: "⚠ WARNING" in Label font (8pt), uppercase, RedWarning color
- Body: Body text in Black, explaining the specific risk

**Variants:**
- `warning`: RedWarning accent (default) — for injury/damage risk
- `caution`: GoldAccent accent — for quality-risk information that is not safety-critical

**Token References:** `{{token.RedWarning}}`, `{{token.White}}`, `{{token.BodyFont}}`

**Common Errors:** Using C008 for tips or general information; omitting the specific consequence of ignoring the warning; using "CAUTION" for a genuine safety risk (use `warning` variant, not `caution`).

---

## C009 — Tips

**Description:** A best-practice tip box. Contains advice that improves quality but is not required. Distinguished from C006 (informational) by its gold accent.

**Dimensions:** Full main content width or 4 columns × variable height

**Background:** `{{token.White}}`

**Border:** Left edge: 4px solid `{{token.GoldAccent}}`

**Layout:**
- Left: GoldAccent icon (star or lightbulb, 16×16px) with 8px padding
- Title: "TIP" in Label font (8pt), uppercase, GoldAccent
- Body: Body text in Black

**Token References:** `{{token.GoldAccent}}`, `{{token.White}}`, `{{token.BodyFont}}`

**Common Errors:** Overusing tips (maximum 2–3 per page); using C009 for required steps (use C005 or the main step sequence); using the warning icon with a tip.

---

## C010 — Paint Legend

**Description:** A reference table mapping colors to their area of application on the model. Appears in the side panel of P002.

**Dimensions:** 4 columns wide (side panel width) × variable height

**Background:** `{{token.White}}`

**Layout:**
- Table: 3 columns — [Swatch 12×12mm] | [Color Name] | [Area Description]
- Header: VioletPrimary background, white Label text ("PAINT LEGEND")
- Rows: White background, 1pt LightGray bottom border per row
- Color names: Caption (9pt), Black
- Area descriptions: Caption (9pt), DarkGray
- No finish badge in this component — finish badges belong to C011 only (see below)
- Row height is variable: it must expand to fit the full Area Description text. Never
  truncate or clip text to force a fixed row height — wrap onto additional lines instead

**Common Errors:** Describing areas too vaguely ("body," "details"); missing colors that appear in the render; swatch colors not matching the paint; adding a finish badge (that's C011's job, not C010's — do not merge the two components into one card); truncating or clipping the Area Description instead of growing the row.

---

## C011 — Paint Code Box

**Description:** A small inline reference showing the code, name, and finish of a specific paint. Appears adjacent to step instructions whenever a paint is referenced.

**Dimensions:** 8 columns wide × 10mm height

**Background:** `{{token.OffWhite}}`

**Border:** 1pt `{{token.LightGray}}` all sides, 4px border-radius

**Layout:**
- Left: Color swatch (10×10mm)
- Center-left: Paint code in MonoFont (9pt), VioletDark (e.g., `TS-29`)
- Center-right: Paint name in Caption (9pt), Black (e.g., "Semi-Gloss Black")
- Right: Finish badge — "GLOSS" / "FLAT" / "METALLIC" in Label (8pt), white on VioletDark background, 2px border-radius

**Token References:** `{{token.OffWhite}}`, `{{token.VioletDark}}`, `{{token.MonoFont}}`, `{{token.LightGray}}`

**Common Errors:** Omitting the finish badge; using a generic color name instead of the official paint name; paint code not in monospace; placing this component inside C010 Paint Legend (they are separate components — C010 is the table on P002, C011 is a standalone inline box next to step instructions on P002/P005–P007).

**Wireframe:**
```
┌──────────────────────────────────────────────────────┐
│ [████] TS-29    Semi-Gloss Black         [FLAT]      │
└──────────────────────────────────────────────────────┘
```

---

## C012 — Zoom

**Description:** A magnified view of a specific small detail, connected to the main render or diagram by a dashed indicator line. Used when an area is too small to be clearly visible at normal render size.

**Dimensions:** 4 columns × variable (typically 4 columns square)

**Background:** `{{token.White}}`

**Border:** 1.5pt `{{token.LightGray}}` all sides, 0px border-radius

**Layout:**
- Magnified image centered in the component area
- Dashed indicator line connects the zoom box to the source area in the main render (1pt, LightGray, dashed: 4px on / 4px off)
- Caption below: "DETAIL: {area name}" in Caption (9pt), MidGray

**Common Errors:** Zoom is not actually larger than the source (defeats the purpose); no indicator line connecting to the source; area description missing.

---

## C013 — Step Number

**Description:** A circular badge containing the step number. The primary navigation element on process pages (P004–P008).

**Dimensions:** 12mm diameter circle

**Background:** `{{token.VioletPrimary}}`

**Layout:**
- Circle shape (border-radius: 50%)
- Number centered: TitleFont, 18pt, white
- If step count > 9: number at 14pt to maintain legibility within circle

**Variants:**
- `standard`: VioletPrimary circle, white number
- `complete`: GreenSuccess circle, white checkmark (used in P010 when reviewing completed steps)

**Token References:** `{{token.VioletPrimary}}`, `{{token.GreenSuccess}}`, `{{token.TitleFont}}`

**Common Errors:** Using square instead of circle; number not centered; using BodyFont instead of TitleFont; steps numbered in a non-sequential order.

---

## C014 — Time Box

**Description:** A small indicator showing the required waiting time for a step (typically a drying or curing time). Appears to the right of a step in C005 Paint Sequence.

**Dimensions:** 18mm wide × 10mm tall

**Background:** `{{token.OffWhite}}`

**Border:** 1pt `{{token.LightGray}}` all sides

**Layout:**
- Top row: Clock icon (8×8px, MidGray) + time value in H3 (22pt), Black (e.g., "30 min")
- Bottom row: "DRYING TIME" label in Label (8pt), MidGray, uppercase

**Variants:**
- `drying`: For paint drying time (default)
- `curing`: For final cure time (topcoat, varnish) — GoldAccent border

**Token References:** `{{token.OffWhite}}`, `{{token.LightGray}}`, `{{token.MidGray}}`

**Common Errors:** Using vague times ("dry completely"); not distinguishing between touch-dry and fully cured; omitting time box for any step that has a mandatory wait.

---

## C015 — Notes

**Description:** A freeform annotation area at the end of a page, typically used at the bottom of P010 Final Checklist. Provides blank lines for handwritten or digital notes by the reader.

**Dimensions:** Full main content width × variable (minimum 30mm)

**Background:** `{{token.OffWhite}}`

**Border:** 1pt `{{token.LightGray}}` all sides, 4px border-radius

**Layout:**
- Header: "NOTES" in Label (8pt), uppercase, VioletPrimary
- Body: Horizontal ruled lines, 1pt `{{token.LightGray}}`, spaced 8mm apart
- Minimum 4 ruled lines, maximum 8 (unless page height permits more)

**Variants:**
- `lined`: Ruled lines (default)
- `blank`: No ruled lines (for digital use where reader types freely)

**Token References:** `{{token.OffWhite}}`, `{{token.LightGray}}`, `{{token.VioletPrimary}}`

**Common Errors:** Too few lines for meaningful notes; no header label (reader doesn't know what this space is for); placing C015 in the middle of a page (it is always at the bottom).

---

## v2.3.0 — Text Source Declaration

*Added in SDK v2.3.0. All components that render text must declare their text source.*

### Text Engine Integration

As of SDK v2.3.0, every component that contains text receives that text exclusively from the Text Engine output (`Projects/{ModelName}/ApprovedText/`). Components do not generate text independently.

**Text-bearing components and their source sections:**

| Component | Text Source in ApprovedText | Text Elements |
|-----------|---------------------------|---------------|
| C001 Header | P{NNN}.md `page_label` field | Page label (right side) |
| C002 Footer | P{NNN}.md frontmatter `model` field | Model name, page number |
| C003 Palette | P002.md `§ Colori` section | Color names, paint codes |
| C004 Shopping List | P003.md `§ Materiali` section | Item names, quantities |
| C005 Paint Sequence | P005.md `§ Sequenza` section | Step labels, color assignments |
| C006 Callout | P{NNN}.md `§ Note` or `§ Informazioni` | Title and body text |
| C007 Exploded View | (no text — visual only) | — |
| C008 Warning | P{NNN}.md `§ Avvertenze` | "ATTENZIONE:" + body |
| C009 Tips | P{NNN}.md `§ Suggerimenti` | "SUGGERIMENTO:" + body |
| C010 Paint Legend | P002.md `§ Legenda` | Code + name pairs |
| C011 Paint Code Box | P002.md `§ Colori` | Code, brand, finish type |
| C012 Zoom | (optional caption from ApprovedText) | Caption only |
| C013 Step Number | P{NNN}.md step frontmatter | "Passo N" label |
| C014 Time Box | P{NNN}.md `duration` fields | "N minuti" / "N ore" |
| C015 Notes | P{NNN}.md `§ Note finali` | Notes body text |

### Render Engine Contract

The Render Engine must:
1. Read ApprovedText/P{NNN}.md before rendering each page
2. Extract text for each component using the mapping table above
3. Place extracted text verbatim — no paraphrase, no translation
4. Log `<!-- RENDER ERROR: missing text for C{NNN} -->` if source is absent
5. Use approved placeholder if source is absent: `[TESTO]`

The Render Engine must NOT:
- Generate any body text
- Translate text
- Abbreviate text without explicit truncation rules (see STYLE_GUIDE §Max Text Lengths)
- Use text from any source other than ApprovedText/

---

## v2.4.0 — content.yaml Field Mapping

*Added in SDK v2.4.0. Each component declares which content.yaml fields it consumes.*

As of v2.4.0, the Render Engine reads component content from `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml` using the field paths declared in each page's `manifest.yaml §components[].content_fields`.

### Component → content.yaml Field Map

| Component | content.yaml Field Path | Notes |
|-----------|------------------------|-------|
| C001 Header | `page.name` (for right-side page label) | Label is Italian per GlossaryIT.md §Page Labels |
| C002 Footer | `footer.page_id`, `footer.model_name` | page_id is fixed; model_name from PROJECT.yaml |
| C003 Palette | `colors[*].name`, `colors[*].hex` | P002 only |
| C004 Shopping List | `paints[*]`, `tools[*]`, `consumables[*]` | P003 only |
| C005 Paint Sequence | `sequence[*].step`, `sequence[*].area`, `sequence[*].color_id` | P005 only |
| C006 Callout | `callouts[*].title`, `callouts[*].body` | Multiple pages |
| C007 Exploded View | (no text — visual only) | — |
| C008 Warning | `warnings[*]` | Must start with "Attenzione:" |
| C009 Tips | `tips[*]` | Must start with "Suggerimento:" |
| C010 Paint Legend | `colors[*].name`, `colors[*].paint_code` | P002 only |
| C011 Paint Code Box | `colors[*].paint_brand`, `colors[*].paint_code`, `colors[*].finish` | P002 only |
| C012 Zoom | Optional caption from `areas[*].zoom_caption` | P006, P007 |
| C013 Step Number | `steps[*].id` or `sequence[*].step` | Label: "Passo N" |
| C014 Time Box | `steps[*].duration` or `sequence[*].drying_time` | Format: "N minuti" |
| C015 Notes | `notes` field or `sections[*].notes` | Multiple pages |

### Render Engine Access Pattern

```python
# Pseudocode — Render Engine field access
content = load_yaml("Projects/{Model}/{Variant}/ApprovedText/P002/content.yaml")
manifest = load_yaml("Projects/{Model}/{Variant}/ApprovedText/P002/manifest.yaml")

for component in manifest.components:
    for field_path in component.content_fields:
        value = deep_get(content, field_path)
        if value is None:
            log_error(f"Missing: {field_path} for {component.id}")
            value = approved_placeholder(field_path)
        render_component(component.id, field_path, value)
```

### Field Access Rules

1. Fields are accessed by dot-path: `colors[0].name`, `steps[2].duration`
2. Missing fields → approved placeholder, never invented content
3. Empty string → treated as missing
4. Arrays → iterate; minimum count per component documented above
5. Nested objects → access sub-fields by dot notation

### Template System Integration

Layout templates (`Templates/`) define component slots as named zones. The Render Engine maps content.yaml fields to template zones using manifest.yaml as the bridge:

```
Template zone "color-list" ← manifest component C003 ← content.yaml colors[]
Template zone "step-1"     ← manifest component C013 ← content.yaml steps[0]
```

Templates contain **no content** — only structural declarations of which zones exist.
