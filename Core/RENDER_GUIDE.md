# Render Guide

This document specifies the standards for all rendered illustrations used in Mini4WD manuals. "Render" refers to any photorealistic computer-generated image of a Mini4WD model. All illustrations of model car bodies in SDK-compliant manuals are renders — not hand drawings, not flat vectors, not stock photography.

---

## 1. Render Philosophy

Photography of physical models is inconsistent, requires physical access to the model, and cannot be easily reproduced. Renders solve all three problems: they can be generated at any time, they are perfectly consistent within a defined lighting rig, and they can be re-generated at any resolution.

Renders must be treated with the same discipline as studio photography. A lazy render is worse than a good photograph. The render represents the finished paint job — it is the reader's primary expectation-setting tool. If the render looks poor, the reader assumes the manual is poor. If the render is accurate and beautiful, the reader is motivated to follow the manual carefully.

Renders are generated outside the SDK's text pipeline. The SDK does not generate images — it specifies what images must look like and provides AI prompt templates to produce them. The actual generation uses a separate AI image model or 3D rendering software.

### Reference Image Scope

Reference photos in `Projects/{Model}/{Variant}/Images/` are almost always stock box-art
or stock product photography — they carry the **original manufacturer livery**, not the
paint scheme being documented. Their authority is strictly limited:

**Reference images ARE authoritative for:** body shape, panel lines, proportions,
silhouette, mechanical components (chassis, wing geometry, cockpit shape, wheel/tire
placement), and component presence (spoilers, air intakes, cowling shape).

**Reference images are NEVER authoritative for:** body color, livery, flames, stripes,
or any painted graphic; decal placement, decal artwork, or printed logos/numbers;
wheel/rim color (unless `paintScheme` explicitly specifies it).

Paint colors, hex values, and area-of-application come **exclusively** from
`content.yaml → colors[]`. When the reference photo's livery conflicts with the paint
scheme — the normal case, since the reference is stock and the paint scheme is a repaint
— the paint scheme always wins. Do not blend, tint, or "recolor" the reference livery:
discard it entirely and repaint per `colors[]`. Do not invent graphics (flames, stripes,
patterns) that are not described in the paint scheme, even if present in the reference
photo.

---

## 2. Required Render Angles

Each page type requires specific render angles. No other angle may be used unless explicitly permitted by the page specification.

### Cover (P001)
- **Primary:** 3/4 front-left view, elevated 15° above horizontal
- The model faces the viewer at approximately 45° from center-left
- Camera elevation shows the top surface of the body
- The rear of the model is partially visible but not the primary focus

### Color Scheme (P002)
- **Front view:** True orthographic projection, 0° elevation, 0° rotation from front
- **Side view:** True orthographic projection, 0° elevation, exactly 90° from front
- **Top view:** True orthographic projection, 90° elevation (directly above)
- All three views are on the same page; consistent lighting across all three

> ⚠️ **Warning:** Orthographic projections have NO perspective distortion. Use orthographic camera mode, not perspective camera mode. Perspective renders look "wrong" in a three-view layout even when the angle appears similar.

### Preparation (P004)
- Any angle that clearly shows the area being prepared (body panel, bottom, wheel arch)
- Typically 3/4 front-left or side view at 0° elevation

### Painting (P005)
- **In-progress renders (optional):** 3/4 front-left at 15° elevation, showing partially painted model
- **Final state render:** Same as cover angle

### Masking (P006)
- **Top view:** True orthographic, 90° elevation — shows masking tape placement
- **Detail views:** 45° elevation, front-left — shows critical masking edges

### Details (P007)
- **Close-up renders:** 45° elevation, angle depends on the detail being shown
- The detail must fill at least 40% of the image frame

### Decals (P008)
- **Side view:** Orthographic or near-orthographic to show decal placement
- **Top view:** For top-surface decals

### Premium Variant (P009)
- **Comparison render:** Two models side-by-side — standard variant (left) and premium (right)
- Same angle for both (3/4 front-left at 15°)

---

## 3. Lighting Rigs

All renders within a single manual must use the same primary lighting rig. Mixing lighting rigs within a manual creates a disjointed visual experience and is a QA failure (QA-041).

### Studio Neutral

The default lighting rig. Clean, balanced, showcases all surfaces equally.

```
       [Key Light]
      /  Top-left
     /   45° horizontal
    /    60° from vertical (above horizon)
[Model] ── → ── → ──
    \
     \   [Fill Light]
      \  Bottom-right
       \ 45° horizontal (opposite side from key)
        \ 30° from vertical (lower than key)

        [Rim Light]
        Back-right
        near-horizontal (10° above)
        low intensity (30% of key)
```

- Key-to-fill ratio: 3:1
- Rim intensity: 30% of key
- Color temperature: neutral white (6500K equivalent)
- Soft shadows: key light shadow softness 40%

**Use when:** The paint scheme is highly detailed and all surfaces should be visible. Best for metallic and multi-color schemes.

### Drama

High-contrast rig for visually striking cover renders. Emphasizes the form of the body.

```
        [Key Light]
       / Top-right
      /  75° horizontal
     /   45° from vertical

[Model]

        (no fill — or very minimal at 10% key)
        
        [Rim Light]
        Back-left
        20° above horizontal
        50% of key intensity
```

- Key-to-fill ratio: 10:1 (near-dark fill)
- Rim intensity: 50% of key
- Color temperature: slightly warm (5000K equivalent)
- Hard shadows: key light shadow softness 10%

**Use when:** The cover render requires maximum visual impact. Not suitable for three-view technical pages — shadows obscure surface detail.

### Detail

Soft, even lighting designed to minimize shadows and reveal surface texture for close-up detail renders.

```
        [Soft Box — Front]
        0° horizontal (directly in front)
        10° above horizontal
        Large source (wraps around model)

        [Key Light]
        90° horizontal (side)
        30° from vertical
        50% intensity
```

- Key-to-fill ratio: 2:1
- No rim light
- Color temperature: neutral white (6500K)
- Very soft shadows: 80% softness

**Use when:** Generating close-up detail renders (C012 Zoom) or technical diagram renders. Maximizes legibility of surface detail.

---

## 4. Background Standards

The render background must be one of:

1. **Pure white (#FFFFFF)** — for all standard renders
2. **Transparent (alpha channel)** — for PNG renders that will be composited onto the page

**Never use:**
- Gray or off-white backgrounds — they alter perceived paint color
- Gradient backgrounds — they add visual noise
- Environmental backgrounds (floors, surfaces, scenery) — inconsistent with the catalog aesthetic
- Bokeh or depth-of-field backgrounds — obscure the model's clean profile
- Drop shadows baked into the render — shadows are added by the layout using CSS/InDesign effects

---

## 5. Resolution Requirements

Minimum resolution is specified per use case. Images that do not meet the minimum are a QA failure (QA-016 through QA-020).

| Use Case | Minimum Resolution | DPI | Token |
|---|---|---|---|
| Cover render (P001) | 2480 × 3508 px | 300 dpi (A4) | `{{token.RenderResolutionCover}}` |
| Full-page body renders | 1240 × 1754 px | 150 dpi (A4) | — |
| Three-view renders (each) | 1000 × 800 px minimum | 150 dpi minimum | — |
| Detail/zoom renders (C012) | 800 × 800 px | 150 dpi | — |
| Comparison renders (P009) | 1240 × 620 px per side | 150 dpi | — |

> 📝 **Note:** For US Letter format, multiply dimensions by 0.942 (216/229.5). The difference is small enough that A4-size renders can be used on Letter pages without loss.

---

## 6. AI Prompt Templates for Renders

These templates are model-agnostic. Substitute the values from `PROJECT.yaml` before submitting to any AI image generation tool.

### Template: Cover Render

```
[RENDER PROMPT]
Subject: {{project.modelName}} Tamiya Mini 4WD scale model car
Body finish: {{project.paintScheme.primaryColor}}, {{project.paintScheme.style}} finish
Secondary color: {{project.paintScheme.secondaryColor}} (if applicable)
Angle: 3/4 front-left view, camera elevated 15 degrees above the horizontal
Lighting: 3-point studio lighting, key light from top-left at 45 degrees, 
          fill light from bottom-right at 30% intensity, rim light from rear-right
Background: pure white (#FFFFFF), no shadow on background
Style: photorealistic product photography, clean, sharp focus throughout
Output: 2480 x 3508 pixels, sRGB color space
No watermarks, no text overlays, no environmental elements
```

### Template: Three-View Render (P002)

```
[RENDER PROMPT — FRONT VIEW]
Subject: {{project.modelName}} Tamiya Mini 4WD scale model car
Body finish: {{project.paintScheme.primaryColor}}, {{project.paintScheme.style}} finish
Angle: true orthographic front view — NO perspective distortion — camera at exact 0 degrees 
       elevation, 0 degrees horizontal rotation from front
Lighting: soft diffuse lighting, flat and even, minimal shadows
Background: pure white (#FFFFFF)
Style: technical illustration, clean product render, sharp
Output: 800 x 600 pixels minimum, sRGB

[RENDER PROMPT — SIDE VIEW]
(same parameters, angle: orthographic, exactly 90 degrees from front)

[RENDER PROMPT — TOP VIEW]  
(same parameters, angle: orthographic, 90 degrees elevation — directly above)
```

### Template: Detail/Zoom Render

```
[RENDER PROMPT — DETAIL]
Subject: {{project.modelName}} Tamiya Mini 4WD — closeup of {{detail.areaName}}
Body finish: {{project.paintScheme.primaryColor}}, {{project.paintScheme.style}} finish
Angle: 45 degrees elevation, positioned to show {{detail.areaName}} clearly
Lighting: Detail rig — large soft box from front, side key at 50% intensity
Background: pure white (#FFFFFF)
Style: macro photography, sharp detail, clean
Output: 800 x 800 pixels minimum, sRGB
The detail area must fill at least 40% of the image frame
```

---

## 7. Quality Checklist for Renders

Before accepting a render for use in a manual page, verify all of the following:

- [ ] Background is pure white or transparent (no gray tones, no gradients)
- [ ] Angle matches the required angle for this page per §2
- [ ] Lighting rig matches the rig selected for this manual per §3
- [ ] Resolution meets the minimum for this use case per §5
- [ ] No motion blur, noise, or AI generation artifacts visible
- [ ] Model body shape is recognizable as the correct Mini4WD model
- [ ] Paint finish accurately represents the specified `paintScheme.style`
- [ ] All paint colors present in the render match the scheme definition — verify each
      `colors[].hex` against the rendered pixels individually, not by overall impression
- [ ] No colors, graphics, or decals were carried over from the reference photo's livery
      (see §1 Reference Image Scope) unless also specified in `colors[]`
- [ ] Decals (if present) are legible at the render's intended display size
- [ ] No elements from outside the model are visible (no hands, no background props)
- [ ] White balance is neutral (no warm or cool color cast on white background)
- [ ] Shadow direction is consistent with the lighting rig description

A render that fails any of these checks must be regenerated before use.
