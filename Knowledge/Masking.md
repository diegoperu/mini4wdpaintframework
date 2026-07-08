# Masking Techniques

**Document ID:** KNW-MAS-001
**SDK Version:** 2.4.0
**Category:** Technique Reference

---

## Overview

Masking is the process of protecting areas of the model from paint during a spray or brush painting session. Precise masking is critical for clean color separation and professional results.

---

## Masking Materials

### Masking Tape

| Type | Width | Use Case | Notes |
|------|-------|----------|-------|
| Tamiya Masking Tape 6mm | 6mm | Tight curves, fine lines | Standard for Mini4WD |
| Tamiya Masking Tape 10mm | 10mm | Straight edges, large areas | Most versatile |
| Tamiya Masking Tape 18mm | 18mm | Large flat areas | |
| Tamiya Masking Tape 40mm | 40mm | Background protection | |
| Tamiya Curved Masking Tape | Various | Compound curves | Pre-cut curved strips |
| Low-tack tape (general) | Various | Delicate surfaces | Use when primer is fragile |

**Application Temperature:** Room temperature (18–24°C). Cold tape loses adhesion. Hot environments cause bleed-through.

### Masking Fluid / Liquid Mask

Applied with a brush, dries to a rubbery film. Best for irregular shapes that tape cannot follow. Remove by peeling after paint is dry.

**Compatible brands:** Humbrol Maskol, Vallejo Masking Fluid

### Pre-cut Masks

Die-cut masks designed for specific model bodies. Not widely available for Mini4WD. May be custom-cut from masking tape using a cutting mat and craft knife.

---

## Masking Order Principles

1. **Paint light colors before dark.** Mask light areas, apply dark coat over. Fewer masking sessions.
2. **Apply tape to fully cured paint only.** Minimum 24h for spray lacquers. Tape on fresh paint causes lifting.
3. **Press edges firmly.** Run a toothpick along tape edges to eliminate air gaps before spraying.
4. **Remove tape before paint fully cures.** 15–30 min after spraying (for spray lacquers). Removing tape from cured paint risks chipping.
5. **Pull tape at 45° to surface.** Straight-up removal causes edge lifting.

---

## Common Masking Defects

| Defect | Cause | Remedy |
|--------|-------|--------|
| Paint bleed under tape | Tape not pressed firmly / too much paint | Sand, repaint, re-mask with fresh tape |
| Tape pulls up base coat | Applied to uncured paint | Wait full cure time before masking |
| Fuzzy edge | Too much paint, sprayed too close | Thin paint, increase distance |
| Ghost line | Tape residue left on surface | Remove with isopropyl alcohol |
| Torn body during tape removal | Old tape, aggressive adhesive | Use fresh low-tack tape |

---

## Masking Sequence for Two-Color Schemes

```
Step 1: Apply base color (entire body)
Step 2: Wait 24h cure
Step 3: Mask base color zones with tape
Step 4: Apply secondary color
Step 5: Remove tape after 20 min (still tacky)
Step 6: Inspect edges, touch up if needed
Step 7: Clear coat entire body
```

---

## Mascheratura di Cerchi Ruota — NON mascherare la gomma

Le gomme dei Mini4WD sono componenti removibili e intercambiabili (mescole diverse
per aderenza/durata) — si sfilano dal cerchio senza attrezzi. Mascherare il
battistrada per proteggerlo mentre si verniciano i cerchi è superfluo: basta
togliere la gomma.

**Procedura corretta:**
1. Rimuovi la gomma dal cerchio (si sfila a mano, nessun collante da sciogliere).
2. Vernicia il cerchio a gomma smontata — nessuna mascheratura del battistrada
   necessaria.
3. Se la superficie del cerchio dove la gomma fa presa rischia di ricevere
   vernice, mascherala con un dischetto di nastro/carta — la vernice in eccesso
   su quella superficie di contatto impedisce il corretto inserimento/rimozione
   della gomma.
4. Rimonta la gomma solo a vernice completamente asciutta (cura completa, non
   solo flash time).

**Perché non mascherare la gomma:** oltre a essere superfluo (si rimuove), il
nastro sul battistrada scanalato raramente aderisce in modo uniforme — bordi di
vernice imprecisi sul cerchio, rischio di residuo di colla sulla gomma. Vedi
anche `Core/AI_OPERATING_RULES.md §RULE-102`, `Tests/ContentValidation.md §TEST-CV-008`.

---

## Related Documents
- `Knowledge/Painting.md`
- `Knowledge/ClearCoat.md`
- `Knowledge/Troubleshooting.md`
- `PromptEngine/Masking.md`
