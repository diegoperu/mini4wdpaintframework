# Forbidden Words and Phrases

**Document ID:** KNW-FBD-001
**SDK Version:** 2.4.0
**Category:** Editorial Reference
**Reference:** `Config/LANGUAGE_POLICY.yaml`, `Core/AI_OPERATING_RULES.md §TEXT RENDERING RULES`

---

## Purpose

This document lists words, phrases, and scripts that must NEVER appear in generated manual text. Compliance is verified by `Tests/TextValidation.md TEST-TX-005-E` and `TEST-TX-001` through `TEST-TX-002`.

---

## Category 1: Forbidden Languages and Scripts

### Japanese Scripts — Zero Tolerance

The following Unicode ranges must never appear in any generated text output:

| Script | Unicode Range | Example Characters | Status |
|--------|-------------|-------------------|--------|
| Kanji | U+4E00–U+9FFF | 漢字, 日本語 | ❌ FORBIDDEN |
| Hiragana | U+3040–U+309F | あいうえお | ❌ FORBIDDEN |
| Katakana | U+30A0–U+30FF | アイウエオ | ❌ FORBIDDEN |
| CJK Punctuation | U+3000–U+303F | 「」、。 | ❌ FORBIDDEN |
| Half-width Katakana | U+FF65–U+FF9F | ｱｲｳｴｵ | ❌ FORBIDDEN |
| Full-width Latin | U+FF01–U+FF60 | Ａ，Ｂ | ❌ FORBIDDEN |

### Other Forbidden Scripts

| Script | Example | Status |
|--------|---------|--------|
| Chinese (Simplified) | 简体中文 | ❌ FORBIDDEN |
| Chinese (Traditional) | 繁體中文 | ❌ FORBIDDEN |
| Korean (Hangul) | 한국어 | ❌ FORBIDDEN |
| Arabic | العربية | ❌ FORBIDDEN |
| Cyrillic (Russian) | Русский | ❌ FORBIDDEN |
| Devanagari | हिन्दी | ❌ FORBIDDEN |

**Rationale:** Manuals are Italian editorial products. No non-Latin script has any role in the text layer of this SDK. The Japanese aesthetic inspiration applies only to visual design, not to text.

---

## Category 2: Forbidden Placeholder Text

| Forbidden String | Why | Approved Replacement |
|----------------|-----|---------------------|
| "Lorem ipsum" | Generic Latin filler | [TESTO] |
| "Lorem ipsum dolor sit amet" | Classic filler | [TESTO] |
| "Consectetur adipiscing elit" | Lorem variant | [TESTO] |
| "Foo", "Bar", "Baz" | Developer shorthand | [VALORE NON SPECIFICATO] |
| "Test text" | Test artifact | [TESTO] |
| "Testo di prova" | Italian test artifact | [TESTO] |
| "TODO" (in editorial output) | Development marker | Approved placeholder or resolved value |
| "[INSERT TEXT HERE]" | Template artifact | [TESTO] |
| "[YOUR TEXT HERE]" | Template artifact | [TESTO] |
| "Sample text" | Generic filler | [TESTO] |
| "Placeholder" | Template artifact | [TESTO] |
| "N/A" (in editorial body) | Not applicable — specify why | [VALORE NON SPECIFICATO] |
| "TBD" | To be determined | [VALORE NON SPECIFICATO] |

---

## Category 3: Forbidden English Terms in Body Text

These English terms have Italian equivalents per `Knowledge/GlossaryIT.md` and must use them:

| Forbidden (English) | Required (Italian) |
|--------------------|-------------------|
| "Gloss" (adjective in text) | "Lucido" |
| "Matte" / "Matt" | "Opaco" |
| "Metallic" | "Metallizzato" |
| "Pearl" | "Perlato" |
| "Satin" | "Satinato" |
| "Step N" | "Passo N" |
| "Warning" (label) | "Attenzione" |
| "Tip" / "Pro tip" | "Suggerimento" |
| "Note" (body text label) | "Nota" |
| "Color scheme" | "Schema colori" |
| "Materials" | "Materiali" |
| "Preparation" | "Preparazione" |
| "Painting" | "Verniciatura" |
| "Masking" | "Mascheratura" |
| "Details" | "Dettagli" |
| "Decals" | "Decalcomanie" |
| "Final checklist" | "Checklist finale" |
| "Cover" (page label) | "Copertina" |
| "Brush" | "Pennello" |
| "Sandpaper" | "Carta vetrata" |
| "Drying time" | "Tempo di asciugatura" |
| "Coat" (noun) | "Mano" |
| "Surface" | "Superficie" |
| "Body" (of model) | "Carrozzeria" |
| "Paint" (noun, general) | "Vernice" |

**Exception:** Technical terms with no Italian equivalent are accepted in *italic* at first use only: *airbrush*, *spray*, *primer*.

---

## Category 4: Forbidden Marketing Language

| Forbidden Phrase | Why |
|----------------|-----|
| "fantastico", "incredibile" | Hyperbole — not technical |
| "perfetto", "ideale per tutti" | Unsubstantiated claim |
| "il migliore sul mercato" | Comparative without basis |
| "rivoluzionario", "innovativo" | Marketing fluff |
| "facile e veloce" | Vague — specify actual time/steps |
| "risultati professionali garantiti" | Unverifiable claim |
| "adatto a tutti i livelli" | Overgeneralization |
| "senza sforzo" | Misleading for a technical process |

---

## Category 5: Forbidden Informal Language

| Forbidden | Correct Alternative |
|-----------|-------------------|
| "dai una mano" (colloquial) | "Applica una mano" |
| "metti su il primer" | "Applica il primer" |
| "fai asciugare" | "Lascia asciugare" |
| "tipo" (as "sort of") | Rephrase specifically |
| "roba" (for materials) | "materiale" / specific name |
| "un bel po'" | Specific quantity |
| "alla fine" (vague) | "Al termine del passo N" |
| "dai!" (encouragement) | Remove entirely |
| "occhio!" (informal warning) | "Attenzione:" |

---

## Category 6: Forbidden AI Self-Reference

Text that reveals AI generation process must never appear in output:

| Forbidden String | Type |
|----------------|------|
| "Ecco il testo generato..." | AI meta-commentary |
| "Come richiesto..." | AI acknowledgement |
| "Ho generato il seguente..." | AI self-reference |
| "Nota: questo testo è stato..." | AI disclaimer |
| "Posso aiutarti con..." | AI offer |
| "Certamente!" / "Certo!" | AI pleasantry |

---

## Related Documents
- `Knowledge/EditorialStyle.md`
- `Knowledge/GlossaryIT.md`
- `Config/LANGUAGE_POLICY.yaml`
- `Tests/TextValidation.md`
- `Core/AI_OPERATING_RULES.md §TEXT RENDERING RULES`
