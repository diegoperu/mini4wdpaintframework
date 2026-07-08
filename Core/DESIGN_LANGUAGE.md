# Design Language

The Design Language is the philosophical foundation of the Mini4WD Manual SDK. It does not describe colors or dimensions — those live in `STYLE_GUIDE.md` and `COLOR_SYSTEM.md`. It describes the beliefs, principles, and aesthetic convictions that inform every design decision.

Before working on any SDK component, read this document. If a design question is not answered by `STYLE_GUIDE.md` or `COMPONENT_SYSTEM.md`, the answer is found here.

---

## 1. Philosophy

**Rule 1.** This framework exists to serve the hobbyist. Every decision — visual, editorial, structural — must make the manual easier to read, understand, and follow. Aesthetic choices that serve only aesthetics are not permitted.

**Rule 2.** The SDK is not a collection of prompts. It is a design system. The prompts are one artifact of the system. The system also includes specifications, tokens, components, a QA checklist, and a workflow. All parts are equally important.

**Rule 3.** Consistency is the primary quality of this framework. A manual produced by a contributor in Tokyo must be visually indistinguishable from one produced by a contributor in Milan, using the same SDK version.

**Rule 4.** The framework is not tied to any technology. Any AI model, any rendering software, any PDF tool, any text editor can participate in the pipeline. Decisions that would create a dependency on a specific tool are prohibited unless they are isolated in a clearly marked optional layer.

**Rule 5.** Documentation is code. Every specification must be unambiguous. Vague language ("approximately," "roughly," "as needed") is not permitted in normative statements. If the value is not known, the document must state that it is not specified and explain when it will be.

**Rule 6.** This framework is designed to last. Decisions are made with the assumption that the SDK will still be in active use in ten years. Trendy choices that will read as dated are avoided. The aesthetic anchor is not 2024 — it is "timeless technical."

**Rule 7.** The manual must be usable by a hobbyist who has never painted a model before. No step may assume prior knowledge unless it is explicitly stated on an earlier page of the same manual.

**Rule 8.** The SDK does not contain model-specific data. The SDK is the scaffolding; the project files are the building. Keeping these separate allows the SDK to be versioned independently of any individual manual.

**Rule 9.** Every page must feel like it was designed by the same hand. This is the test. If a page could have been produced without reading this document, it probably violates a rule.

**Rule 10.** The framework respects the craft. Mini4WD painting is a skilled hobby. The manual must communicate the precision and care that the craft demands. Clipart, stock icons, and generic layouts are inadequate. Every visual element must be deliberate.

---

## 2. Visual Identity

**Rule 11.** The visual identity is inspired by Tamiya's technical catalogs and instruction sheets of the 1990s: white background, precise callout boxes, numbered steps, clean typography, and technical diagrams. This is the cultural reference, not a template to copy.

**Rule 12.** The identity is reinterpreted with modern graphic design: structured grid, systematic color palette, typographic hierarchy, and render-quality illustrations. The result must feel contemporary without feeling fashionable.

**Rule 13.** White is the dominant color on every page. TamiyaPrimary is the accent that marks the framework. Gold is used to highlight excellence and important information. Red is used exclusively for warnings. These roles are fixed and non-negotiable.

**Rule 14.** The TamiyaPrimary header band is the SDK's signature. It must appear on every page. Its presence immediately communicates: "This page was produced by the Mini4WD Manual SDK." A page without this header is not an SDK page.

**Rule 15.** The side panel (four columns, TamiyaPrimary background) is the secondary structural element. On pages where it appears, it contains supplementary information: callouts, tips, the palette legend. It must never contain the primary narrative.

**Rule 16.** White space is not empty space — it is structure. Margins, gutters, and padding are not defaults to be filled. They define the visual weight and reading rhythm of each page. Crowded pages are failures, not thoroughness.

**Rule 17.** Every page has a clear visual hierarchy: one primary element, one secondary element, supporting information. The reader's eye must never be confused about where to look first.

**Rule 18.** No decorative element is permitted unless it serves an informational purpose. No rules, borders, or dividers may be added because they "look good." Every graphic element must either organize, highlight, or explain.

**Rule 19.** The manual must be visually impressive at first glance and completely legible at sustained reading. These are not competing goals. Design that achieves only one has failed.

**Rule 20.** Shadows, gradients, and visual effects are permitted only when they describe a real-world property (e.g., the shadow cast by a rendered car, the gradient of a metallic paint finish). Decorative shadows and gradients are prohibited.

---

## 3. Typography

**Rule 21.** Typography is not decoration. Every font choice has a function. The title font conveys authority. The body font conveys precision. The monospace font conveys exactness. Using a decorative typeface because it "looks cool" violates this rule.

**Rule 22.** The type scale is fixed. There are exactly seven type sizes: Display (48pt), H1 (36pt), H2 (28pt), H3 (22pt), Body (11pt), Caption (9pt), Label (8pt). No other sizes may be introduced without a corresponding ADR.

**Rule 23.** Type is set in the language of the manual. If a manual is in Italian, all labels, callouts, and instructions are in Italian. Mixed-language typography is not permitted unless a specific technical term has no translation.

**Rule 24.** Line length must not exceed 75 characters for body text. Long lines reduce reading speed and comprehension. The 12-column grid and defined page margins enforce this at the layout level.

**Rule 25.** Orphans and widows are editorial failures. A single word on the last line of a paragraph is an orphan. A single line of a paragraph at the top of a column is a widow. Both must be corrected by rewriting or reflowing — never by altering spacing.

**Rule 26.** All caps is used only in component labels (e.g., "COLOR SCHEME" in the header right section) and never in body text. Small caps are permitted for part codes and technical identifiers.

**Rule 27.** Bold is used to mark genuinely critical information — warnings, required materials, mandatory steps. It is not used for emphasis of interest or variety. If everything is bold, nothing is bold.

**Rule 28.** Italic is used for product names, first use of technical terms, and quotations. It is not used for casual emphasis or stylistic variety.

---

## 4. Layout

**Rule 29.** Every page is built on a 12-column grid with 4mm gutters. No element may span columns partially. Elements must align to the grid at every edge.

**Rule 30.** The page margin is not a minimum — it is the specification. Content that bleeds into the margin (except the header band, which extends full-width) is a QA failure.

**Rule 31.** The header band and footer band are fixed elements. Their height, color, and position are defined by C001 and C002 respectively. No page may adjust these dimensions.

**Rule 32.** Information flows top-to-bottom, left-to-right within the main content area. The side panel flows independently of the main content. The reader must never need to jump back up the page to resolve a reference.

**Rule 33.** Step numbers (C013) are the primary navigation element within process pages. They must be large, clearly visible, and never interrupted by other elements.

**Rule 34.** Images and renders are placed before the text that describes them. A reader following a step must see the illustration before reading the instruction that references it.

**Rule 35.** No layout element may overlap another without a functional reason. Overlapping elements create visual confusion and printing artifacts. Overlaps in renders (e.g., a rendered car overlapping a subtle background grid) are forbidden.

**Rule 36.** The layout of each page type is fixed by its page specification (PAGE_SYSTEM.md). Variation within a page is achieved by the content of components, not by repositioning them.

---

## 5. Rendering

**Rule 37.** Renders replace what would otherwise require studio photography. They must be treated with the same discipline: correct lighting, correct angle, correct finish. A render that does not accurately represent the painted model is worse than no render.

**Rule 38.** A render must show the model as its owner will see it: under controlled light, sharp focus, with the care and pride of a craftsperson presenting their work. Low-effort renders are an insult to the craft.

**Rule 39.** The background of every render is pure white (#FFFFFF). This is not negotiable. Environmental backgrounds, bokeh, or textured surfaces introduce visual noise that competes with the model.

**Rule 40.** Render angles are specified per page in `RENDER_GUIDE.md`. No page may use an angle not listed in that document unless the page spec explicitly permits it.

**Rule 41.** Lighting must be consistent within a single manual. If the cover render uses Studio Neutral lighting, all renders in that manual use Studio Neutral. Mixing lighting styles within a manual creates a disjointed visual experience.

**Rule 42.** Detail renders (C012 Zoom) must show the specific detail at sufficient scale to be instructive. A zoom that does not reveal useful information should not be included.

**Rule 43.** No render may be altered with decorative filters, color grading, or artistic effects. The render represents the physical model. Altering it misrepresents the outcome of following the manual.

**Rule 44.** Resolution is not optional. Renders that do not meet the minimum resolution specified in `RENDER_GUIDE.md` §5 are QA failures. A low-resolution render that "looks fine on screen" will fail in print.

---

## 6. Color

**Rule 45.** Color has meaning in this system. Every color role is fixed and documented in `COLOR_SYSTEM.md`. Using red for visual interest violates its role as a warning signal. Using TamiyaPrimary for something other than structural elements dilutes the brand signal.

**Rule 46.** The SDK palette is closed. Colors not defined in `COLOR_SYSTEM.md` and `Assets/DesignSystem/Tokens/` may not appear in manual pages. The only exception is paint swatch representations in the C003 Palette component, which must accurately represent real paint colors.

**Rule 47.** No gradient may replace a solid color unless it describes a real-world surface (e.g., a metallic finish transitioning between light and shadow on a curved panel). Gradients used for "visual effect" in structural elements are prohibited.

**Rule 48.** Color contrast must meet WCAG 2.1 AA at minimum for all text-on-background combinations. TamiyaPrimary on White exceeds this standard. White on TamiyaPrimary exceeds this standard. Any new color combination introduced in a derivative work must be tested before use.

**Rule 49.** Print colors must be validated against CMYK equivalents before approval. Screen color (sRGB) and print color (CMYK FOGRA39) can differ significantly, especially for saturated blues. The CMYK values in `COLOR_SYSTEM.md` are the authoritative print reference.

**Rule 50.** The primary color (#114B69) is derived from the blue star of the Tamiya "Star Mark" logo, darkened and desaturated so it does not conflict with any of the four reserved functional colors (red, green, blue, gold) — see `STYLE_DECISIONS.md` ADR-023. This is the reason it is a deep, unusual shade of blue rather than Tamiya's bright logo blue. Do not substitute a more saturated or lighter blue.

**Rule 51.** Black in this system is #1A1A1A, not #000000. Pure black causes visual harshness and appears as a registration mark in some print workflows. The near-black #1A1A1A is softer in print and visually indistinguishable from pure black at reading distance.

**Rule 52.** Gold (#C8A838) is used exclusively to highlight premium information, important tips, and excellence markers. It is not a decorative color. Its scarcity on a page gives it meaning. A page with more than three gold elements has overused gold.

**Rule 53.** The palette components (C003 Palette, C010 Paint Legend, C011 Paint Code Box) use exact swatch representations of real paint colors. These swatches are calibrated in `COLOR_SYSTEM.md` §7. They are the only elements on a page that may introduce colors outside the SDK palette.

**Rule 54.** When in doubt, use white. The default background is always white. The default text is always Black (#1A1A1A). Color is added only when it serves communication, not composition.

---

## v2.3.0 — Editorial Identity Principles (Rules 55–65)

*Added in SDK v2.3.0. These rules govern the relationship between visual Japanese aesthetic and Italian editorial identity.*

**RULE-055** The visual language is inspired by Japanese technical craftsmanship. The editorial language belongs to an Italian publisher. These are two distinct, coexisting layers that never interfere.

**RULE-056** The manual aesthetically references Tamiya's catalog tradition: clean layout, technical callouts, precise diagrams. It does NOT imitate the original Japanese manual — it reinterprets it through an Italian editorial lens.

**RULE-057** Japanese visual elements (clean lines, precision, the concept of *monozukuri* — the art of making things) inform the design philosophy, not the content. Content is always Italian.

**RULE-058** A reader who does not understand Japanese must understand every word in this manual. There are zero Japanese characters in any text element.

**RULE-059** The typography conveys Italian technical authority. Not a translation. Not an approximation. Native Italian technical communication.

**RULE-060** Visual references to Japanese aesthetics are expressed through layout, proportion, and use of white space — never through script imitation or decorative pseudo-characters.

**RULE-061** The design must never look like a machine translation. It must look like it was designed and written by an Italian publisher who loves Mini4WD.

**RULE-062** The Tamiya aesthetic is the visual starting point. Italian technical publishing is the editorial destination.

**RULE-063** Any visual element that could be mistaken for Japanese text is forbidden. This includes: simulated kana shapes, decorative elements resembling kanji, brushstroke-style type treatments intended to evoke Japanese writing.

**RULE-064** The manual is not a Japanese product adapted for Italy. It is an Italian product inspired by Japanese product culture.

**RULE-065** When in doubt: would an Italian technical editor approve this? If yes — publish. If no — redesign.
