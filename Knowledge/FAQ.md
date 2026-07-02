# Frequently Asked Questions

**Document ID:** KNW-FAQ-001
**SDK Version:** 2.4.0
**Category:** Reference

---

## General

**Q: Do I need an airbrush to use this SDK?**
A: No. All pages and techniques in the SDK are achievable with spray cans (Tamiya TS/PS series). Airbrush instructions are included as an optional technique where they provide advantage.

**Q: Can I use any paint brand, or must I use Tamiya?**
A: Any paint brand can be used. The SDK uses Tamiya codes as reference but supports any brand — fill `paintBrand` and `paintCode` in `PROJECT.yaml` accordingly. See `Knowledge/Paints.md` for supported brand formats.

**Q: What is the difference between PS and TS paints?**
A: TS paints are for ABS plastic (standard). PS paints are formulated for polycarbonate (Lexan) bodies. Using TS on polycarbonate risks crazing. Verify your body material before selecting paints.

---

## SDK Usage

**Q: Can I use this SDK with any AI model?**
A: Yes. The PromptEngine prompts are designed to be model-agnostic and work with ChatGPT, Claude, Gemini, and any instruction-following LLM. See `PromptEngine/README.md`.

**Q: How do I add a new Mini4WD model?**
A: Copy `Templates/PROJECT.yaml` to `Projects/{NewModelName}/PROJECT.yaml`, fill in all fields, then follow `Build/Pipeline.md` Phase 0 onward.

**Q: What if a required render angle is not achievable with my AI image generator?**
A: Use the closest available angle and document the deviation in `Projects/{ModelName}/Notes/`. Flag in QA log as a known limitation.

**Q: Can I skip pages?**
A: P001, P002, P003, P004, P005, P006, P007, P008, and P010 are required. P009 (Premium Variant) is optional — set `premiumVariant.enabled: false` in PROJECT.yaml.

---

## Quality

**Q: My render has a slightly off-white background. Will it pass QA?**
A: No. QA-021 requires exact #FFFFFF. Regenerate with explicit white background instruction. See `Config/quality.yaml §thresholds.background_white_tolerance_rgb`.

**Q: How many QA failures are allowed?**
A: Zero blocking failures. Maximum 3 non-blocking exceptions (documented in qa_log.md). See `Config/quality.yaml §approval`.

**Q: Who approves a manual?**
A: The project maintainer countersigns the `Assets/ApprovedManual/{ModelName}/README.md`. See `Build/Pipeline.md §Phase 6`.

---

## Versioning

**Q: Which SDK version should I use for my project?**
A: Always use the latest stable version. Record the SDK version in `PROJECT.yaml §sdk_version`.

**Q: Can I update an existing manual to a newer SDK version?**
A: Yes. See `Docs/migration/` for version-specific migration guides.

---

## Related Documents
- `Knowledge/Glossary.md`
- `Knowledge/BestPractices.md`
- `PromptEngine/README.md`
- `Build/Pipeline.md`
