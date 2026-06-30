# Assets/DesignSystem/Typography/

**Version:** 2.1.0
**Token source:** Assets/DesignSystem/Tokens/tokens.example.yaml `typography.*`
**Spec:** Core/STYLE_GUIDE.md §2–3

---

## Purpose

This document defines the typography system of the Mini4WD Manual SDK: font families, type scale specimens, licensing, and usage rules. All values are also available as design tokens — reference `{{token.TitleFont}}`, `{{token.BodySize}}`, etc. in prompts.

---

## Font Families

### TitleFont — Bebas Neue

**Token:** `{{token.TitleFont}}`
**Stack:** `"Bebas Neue, Impact, Arial Black, sans-serif"`
**Download:** [Google Fonts — Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue)
**License:** SIL Open Font License 1.1 (free for commercial use)
**Designer:** Ryoichi Tsunekawa

**Characteristics:**
- Condensed, all-caps display typeface
- High x-height, strong vertical rhythm
- Excellent legibility at large sizes (24pt+)
- Zero kerning required at display sizes

**Usage:**
- Display level (48pt): model name on cover page
- H1 level (36pt): main page title
- C013 Step Number badge: 22pt
- C001 Header wordmark: 14pt
- C002 Footer label: 8pt uppercase

**Fallback rationale:**
- `Impact`: closest system font in weight and condensation — widely available on Windows/macOS
- `Arial Black`: heavy weight, broader letterforms — fallback for systems without Impact
- `sans-serif`: generic category fallback

---

### BodyFont — Source Sans Pro

**Token:** `{{token.BodyFont}}`
**Stack:** `"Source Sans Pro, Open Sans, Helvetica Neue, sans-serif"`
**Download:** [Google Fonts — Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+3)
**License:** SIL Open Font License 1.1 (free for commercial use)
**Designer:** Paul D. Hunt (Adobe)

**Characteristics:**
- Humanist sans-serif optimized for UI and long-form reading
- High readability at 9pt–14pt
- Available in 6 weights (ExtraLight through Black)
- Excellent Latin diacritics support for Italian text

**Usage:**
- Body text (11pt Regular): all paragraph text, list items, component descriptions
- H4 headings (16pt SemiBold): callout titles, step headers
- Caption (9pt Regular): image captions, footnotes, metadata
- Label (8pt SemiBold Uppercase): component tags, page type labels

**Weight usage:**
| Weight | Usage |
|--------|-------|
| Regular (400) | Body text, captions |
| SemiBold (600) | H3, H4, callout titles |
| Bold (700) | H2, critical warnings |
| ExtraLight (200) | Large display subheadings (optional) |

**Fallback rationale:**
- `Open Sans`: very similar humanist sans, widely preloaded in browsers
- `Helvetica Neue`: classic neutral fallback, macOS default
- `sans-serif`: generic category

---

### MonoFont — JetBrains Mono

**Token:** `{{token.MonoFont}}`
**Stack:** `"JetBrains Mono, Courier New, monospace"`
**Download:** [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
**License:** SIL Open Font License 1.1 (free for commercial use)
**Designer:** Philipp Nurullin, Konstantin Bulenkov

**Characteristics:**
- Monospaced font with increased x-height
- Excellent character disambiguation (0/O, 1/l/I)
- Designed for code — ideal for paint codes and part numbers

**Usage:**
- C011 Paint Code Box: product codes (e.g., `TS-57`, `Mr.Color C-5`)
- Any part number reference in body text: `inline code style`
- Technical identifiers in Notes (C015)

---

## Type Scale Specimens

### Display — 48pt TitleFont

```
PROTO EMPEROR
```
*Bebas Neue 48pt — cover model name (P001)*

---

### H1 — 36pt TitleFont

```
COLOR SCHEME
```
*Bebas Neue 36pt — page main title*

---

### H2 — 28pt TitleFont

```
Base Coat Application
```
*Bebas Neue 28pt — section heading*

---

### H3 — 22pt BodyFont SemiBold

```
Preparation Steps
```
*Source Sans Pro SemiBold 22pt — subsection heading*

---

### H4 — 16pt BodyFont SemiBold

```
Pro Tip: Thinning the Paint
```
*Source Sans Pro SemiBold 16pt — callout/step title*

---

### Body — 11pt BodyFont Regular

```
Apply the base coat in thin, even layers. Hold the spray can
25–30cm from the surface and use sweeping side-to-side motion.
Allow each coat to dry for 30 minutes before applying the next.
```
*Source Sans Pro Regular 11pt, line-height 1.6*

---

### Caption — 9pt BodyFont Regular

```
Fig. 1 — Three-quarter front view showing completed base coat
```
*Source Sans Pro Regular 9pt, line-height 1.5*

---

### Label — 8pt BodyFont SemiBold Uppercase

```
COLOR SCHEME  ·  P002
```
*Source Sans Pro SemiBold 8pt Uppercase — page type and page number*

---

### Code — 11pt MonoFont Regular

```
TS-57  |  Mr.Color C-5  |  AK-11006
```
*JetBrains Mono Regular 11pt — paint codes in C011 Paint Code Box*

---

## Typography Rules

### Allowed Combinations

| Context | Font | Weight | Size | Case |
|---------|------|--------|------|------|
| Page title | TitleFont | — | 36–48pt | Uppercase (inherent) |
| Section heading | TitleFont | — | 22–28pt | Uppercase |
| Callout title | BodyFont | SemiBold | 16pt | Title Case |
| Step title | BodyFont | SemiBold | 14pt | Title Case |
| Body paragraph | BodyFont | Regular | 11pt | Sentence case |
| Caption | BodyFont | Regular | 9pt | Sentence case |
| Label/badge | BodyFont | SemiBold | 8pt | UPPERCASE |
| Paint code | MonoFont | Regular | 11pt | As printed |

### Forbidden Combinations

| Forbidden | Reason |
|-----------|--------|
| Italic in TitleFont | Bebas Neue has no true italic — synthetic slant is unacceptable |
| Bold in Caption (9pt) | Too heavy at small size, reduces readability |
| TitleFont for body text | Condensed all-caps text is not readable at paragraph length |
| BodyFont at Display size (48pt) | Proportions are wrong for display; TitleFont serves this role |
| Mixed font families in a single heading | Creates visual noise |
| Underline for anything other than hyperlinks | Confuses links with emphasis |
| ALL CAPS in BodyFont body text | Reduces reading speed for paragraphs |

---

## Font Installation

For print and PDF export tools (Affinity Publisher, InDesign, Scribus), install fonts system-wide:

1. Download Bebas Neue and Source Sans Pro from Google Fonts
2. Download JetBrains Mono from the JetBrains website
3. Install per your OS:
   - **macOS:** Double-click `.ttf`/`.otf` → Install Font
   - **Windows:** Right-click `.ttf`/`.otf` → Install for all users
   - **Linux:** Copy to `~/.fonts/` and run `fc-cache -f -v`
4. Restart your layout application after installation

---

## Font Licensing Summary

| Font | License | Commercial Use | Modification |
|------|---------|----------------|--------------|
| Bebas Neue | OFL 1.1 | ✅ Free | ✅ Allowed |
| Source Sans Pro | OFL 1.1 | ✅ Free | ✅ Allowed |
| JetBrains Mono | OFL 1.1 | ✅ Free | ✅ Allowed |

All fallback fonts (Impact, Arial Black, Open Sans, Helvetica Neue, Courier New) are either system fonts or Google Fonts with compatible licensing. Do not substitute proprietary fonts (e.g., Futura, Helvetica purchased) without verifying license compatibility for your distribution method.
