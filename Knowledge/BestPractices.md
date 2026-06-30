# Best Practices

**Document ID:** KNW-BPR-001
**SDK Version:** 2.2.0
**Category:** Expert Guidance

---

Compiled from experienced Mini4WD painters. These practices are not requirements — they are recommendations that consistently produce professional results.

---

## Preparation

1. **Always wash new bodies before any handling.** Mold release agents are invisible but catastrophic to adhesion.
2. **Sand gates before priming, not after.** Primed gates are harder to sand cleanly.
3. **Prime in thin coats.** Two thin coats of primer reveal more defects than one thick coat.
4. **Inspect under raking light.** Angle a desk lamp at 10° to the surface — scratches and low spots become clearly visible.
5. **Keep 24h between major steps.** Rushing cure times is the single most common cause of defects.

## Painting

6. **Always test spray on scrap before applying to model.** This catches clogs, wrong pressure, and cold paint.
7. **Label all paint containers after opening.** Unlabeled thinned paint is easy to confuse with thinner alone.
8. **Apply multiple thin coats rather than one thick coat.** Thick coats run, trap solvent, and take longer to cure.
9. **Spray in a single direction per pass.** Random direction spraying creates uneven coverage.
10. **Work at room temperature (18–24°C).** Cold paint is viscous and doesn't atomize well. Hot environments cause rapid solvent evaporation.

## Masking

11. **Always apply masking tape to fully cured paint (24h minimum for lacquer).**
12. **Burnish tape edges with a toothpick or wooden stick, not your fingernail.** Fingernails leave oil traces.
13. **Remove masking tape before paint is fully cured (15–30 min after spraying).** Dried lacquer cracks at tape edges during removal.
14. **Use fresh tape for every session.** Old tape loses tack uniformly and may leave adhesive residue.
15. **Overlap tape strips by 1–2mm.** Gaps between strips cause paint bleed.

## Decals

16. **Apply decals only to gloss surfaces.** Matte texture traps air under decal edges, causing silvering.
17. **Trim decals close to artwork.** Large areas of clear film show as visible film edges on the finished model.
18. **Use decal softener on any curved surface.** Flat decals do not conform to curves without chemical assistance.
19. **Never rush decal curing.** 24h minimum before clear coat. 12h minimum before handling.
20. **Apply two gloss clear coats after decals.** This buries the decal edge for a painted-on look.

## SDK Usage

21. **Fill PROJECT.yaml completely before starting any prompt.** Gaps in data lead to TODO markers in output, which must be resolved before QA.
22. **Run Tests/FrameworkIntegrity.md before starting a new SDK version.** Verify all documents are present.
23. **Keep qa_log.md updated throughout production.** Don't rely on memory for QA status.
24. **Archive reference images immediately.** Once you have good reference photos, archive them in `Assets/ReferenceModels/` before starting renders.
25. **One model per project directory.** Never share a PROJECT.yaml across two models.

---

## Related Documents
- `Knowledge/Preparation.md`
- `Knowledge/Painting.md`
- `Knowledge/Masking.md`
- `Knowledge/Decals.md`
- `Knowledge/Troubleshooting.md`
