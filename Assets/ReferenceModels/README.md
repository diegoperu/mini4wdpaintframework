# Assets/ReferenceModels/

**Version:** 2.1.0
**Used by:** PromptEngine/ prompts during render generation
**Spec:** Core/RENDER_GUIDE.md §6

---

## Purpose

`ReferenceModels/` contains source photography and reference artwork for each Mini4WD model in the SDK. These images are the **raw input** for generating manual illustrations — they feed into the AI render generation prompts described in `Core/RENDER_GUIDE.md §6`.

Reference images are **not** manual illustrations. They are never placed directly into a manual page. They are input material that guides the AI model during render creation.

---

## Directory Structure

One subfolder per Mini4WD model:

```
ReferenceModels/
└── {ModelName}/             # Named exactly as PROJECT.yaml modelName (spaces → underscores)
    ├── README.md            # Model-specific notes and image status
    ├── reference_front.jpg  # REQUIRED — front orthographic view
    ├── reference_side.jpg   # REQUIRED — right-side view
    ├── reference_top.jpg    # REQUIRED — top-down view
    ├── box_art.jpg          # OPTIONAL — official Tamiya box artwork
    ├── official_render.jpg  # OPTIONAL — official Tamiya promotional render
    ├── chassis_bottom.jpg   # OPTIONAL — chassis underside (for detail pages)
    └── detail_{area}.jpg    # OPTIONAL — close-up of specific area (e.g., detail_cockpit.jpg)
```

---

## Required Files

Every model subfolder must contain these three files before the render generation phase begins:

| File | Description | Minimum Size |
|------|-------------|-------------|
| `reference_front.jpg` | Front orthographic view — camera level with front face, no perspective | 800×600px |
| `reference_side.jpg` | Right-side orthographic view — camera level with right side | 800×600px |
| `reference_top.jpg` | Top-down view — camera directly above, looking down | 800×600px |

If these files are not present, do not begin render generation. Document the missing files in the project's `Notes/` directory.

---

## Optional Files

| File Pattern | Description | When to Include |
|-------------|-------------|----------------|
| `box_art.jpg` | Official Tamiya box artwork scan | Include when available — shows intended color scheme and livery |
| `official_render.jpg` | Official Tamiya promotional render | Include when available — shows desired finish quality |
| `chassis_bottom.jpg` | Chassis underside photograph | Include for P004 Preparation if chassis painting is documented |
| `detail_{area}.jpg` | Close-up of a specific area | Include when a detail is too small to see in the orthographic views |

---

## Image Requirements

| Property | Requirement |
|----------|-------------|
| Minimum resolution | 800×600px (required files), 400×400px (optional detail shots) |
| Color space | sRGB |
| Format | JPG (for photos), PNG (for renders with transparent background) |
| Watermarks | Not permitted — use only unencumbered images |
| Background | Any (reference images are not placed directly in manuals) |
| White balance | Neutral preferred — avoid heavy color casts |

---

## How to Use Reference Images

Reference images feed into the AI render generation prompts defined in `Core/RENDER_GUIDE.md §6`.

### Step 1: Gather Reference
Photograph or source images for all three required angles. Natural daylight or a light box produce the best results for photography.

### Step 2: Prepare the Prompt
Use the render prompt template from `Core/RENDER_GUIDE.md §6`, substituting the reference image path:

```
[RENDER PROMPT — cover page]
Reference: Assets/ReferenceModels/{ModelName}/reference_front.jpg
           Assets/ReferenceModels/{ModelName}/reference_side.jpg
Subject: {MODEL NAME} Mini4WD scale model car
Finish: {paint scheme from PROJECT.yaml}
Angle: 3/4 front-left, elevated 15°
Lighting: studio-neutral (3-point: key 45° top-left, fill 45° bottom-right, rim back-right)
Background: pure white (#FFFFFF)
Style: photorealistic, product photography, clean
Output: 2480×3508px minimum (A4 @300dpi)
```

### Step 3: Review the Render
Compare the generated render against the reference images using `Core/RENDER_GUIDE.md §7` (quality checklist). If the body shape, proportions, or key details are incorrect, re-run with tighter reference instructions.

---

## Copyright and Licensing

> ⚠️ **Important:** Only include images you have the legal right to use.

| Source | Notes |
|--------|-------|
| Your own photographs | Always permitted |
| CC0 or public domain images | Permitted — document the source in the model README.md |
| Creative Commons Attribution images | Permitted with credit — document in README.md |
| Official Tamiya box art scans | Contact Tamiya for commercial use rights; for personal use, proceed with caution |
| Downloaded promotional renders | Generally not permitted for redistribution — check source terms |

If a reference image cannot be included due to copyright, document this in the model's `README.md` and describe the model appearance in text instead. The AI render prompt can use text description in place of reference images.

---

## Naming Convention

Model subfolder names must match `PROJECT.yaml` `modelName` field with spaces replaced by underscores:

| modelName in PROJECT.yaml | Folder Name |
|--------------------------|-------------|
| `Proto Emperor` | `Proto_Emperor/` |
| `Astute` | `Astute/` |
| `Avante Mk III` | `Avante_Mk_III/` |

Detail image naming: `detail_{area_slug}.jpg`
- `detail_cockpit.jpg`
- `detail_rear-wing.jpg`
- `detail_front-bumper.jpg`

---

## Model Subfolders

| Model | Status | Required Images |
|-------|--------|----------------|
| `Proto_Emperor/` | Example (placeholders) | See README.md |

Add a row to this table when adding a new model subfolder.
