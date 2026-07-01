# Proto Emperor — Violet Phantom

> **Status:** Example Reference Project
> This project is included with the Mini4WD Manual SDK as a demonstration and reference. All data is realistic but intended as an example — not an official Tamiya document.

---

**Model:** Proto Emperor
**Scheme:** Violet Phantom
**SDK Version:** 2.4.0
**Language:** Italian (it)
**Manual Version:** 1.0.0
**QA Status:** Example (not production QA'd)
**Created:** 2024-01-15
**Author:** Mini4WD Manual SDK Team

---

## About This Project

The Proto Emperor is a legendary Mini4WD chassis known for its forward-motor layout and aggressive aerodynamic styling. The "Violet Phantom" scheme uses a deep violet base coat with metallic silver accents on aerodynamic appendages, and matte black chassis detailing. A pearl topcoat variant ("Violet Phantom Pearl Edition") is included as the P009 premium variant.

This project demonstrates:
- A multi-color scheme with 4 paint colors
- Use of all 10 manual pages (P001-P010)
- Premium variant (P009) enabled
- Complete PROJECT.yaml with all fields filled
- A realistic preparation and painting workflow

---

## Paint Scheme: Violet Phantom

| ID | Role | Brand | Code | Color Name | Finish | Hex |
|----|------|-------|------|-----------|--------|-----|
| C001 | Body Base | Tamiya | TS-57 | Blue Violet | Gloss | #4B3A8C |
| C002 | Aerodynamic Accents | Tamiya | TS-40 | Metal Black | Metallic | #2C2C2C |
| C003 | Trim & Wing Highlights | Tamiya | TS-30 | Silver | Metallic | #C0C0C0 |
| C004 | Chassis & Interior | Tamiya | TS-38 | Gun Metal | Metallic | #5C6370 |

**Top Coat:** Tamiya TS-79 Semi Gloss Clear

---

## Project Structure

```
Projects/Proto_Emperor/
├── PROJECT.yaml          ✓ Filled — example configuration
├── PROJECT.md            ✓ Human-readable brief
├── CHECKLIST.md          ✓ Progress tracker
├── COLOR_SCHEME.yaml     ✓ Full color definitions
├── PDF_CONFIG.yaml       ✓ Export configuration
├── README.md             ✓ This file
├── Images/               → Place render images here
│   ├── cover_3q.png      [PLACEHOLDER — cover render not included]
│   ├── P002_front.png    [PLACEHOLDER]
│   ├── P002_side.png     [PLACEHOLDER]
│   └── P002_top.png      [PLACEHOLDER]
├── Output/               → AI-generated page outputs
│   ├── raw/              → Raw outputs from PromptEngine prompts
│   └── pdf/              → Exported PDFs
└── Notes/                → QA logs and notes
```

---

## How to Use This as a Reference

1. **Study the PROJECT.yaml** to understand how to fill in your own project's configuration.
2. **Compare it to the Templates/PROJECT.yaml** to see which fields are required vs optional.
3. **Run the PromptEngine prompts** against this PROJECT.yaml to generate example pages.
4. **Use the generated pages** as visual reference for what a correctly-generated manual looks like.

---

## Generating Pages from This Example

```bash
# Read the PROJECT.yaml data
cat Projects/Proto_Emperor/PROJECT.yaml

# For each page, substitute tokens and run the prompt:
# 1. Open PromptEngine/Cover.md
# 2. Replace {{project.modelName}} with "Proto Emperor"
# 3. Replace {{project.seriesName}} with "Championship Series"
# 4. Replace {{paintScheme.name}} with "Violet Phantom"
# 5. Replace {{paths.coverRenderPath}} with "Images/cover_3q.png"
# 6. Replace {{project.year}} with "2024"
# 7. Paste the substituted prompt into your AI model
```

---

## QA Status

This is an example project. Production QA has not been run. Use it as a structural reference only.

To run QA on your own project, see `Core/QA_SYSTEM.md`.

---

*Part of Mini4WD Manual SDK v2.4.0 — Example Project. See `Projects/README.md` for project conventions.*
