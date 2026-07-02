# Capitolo 20 — Glossary

Appendice terminologica. Poiché l'italiano è l'unica lingua editoriale ammessa nello SDK (`Config/LANGUAGE_POLICY.yaml`, G01), il **Glossario Italiano è il riferimento primario**: ogni termine qui elencato deve essere usato esattamente come specificato, senza sinonimi né varianti, in qualunque manuale generato. Il glossario inglese (`Knowledge/Glossary.md`) esiste come riferimento tecnico/internazionale per i contributor, non come fonte di termini da usare in output.

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Glossario Italiano | `Knowledge/GlossaryIT.md` (KNW-GIT-001) | Source of Truth per l'output editoriale |
| Terminologia Tecnica | `Knowledge/Terminology.md` (KNW-TRM-001) | Contesto ed equivalenze EN→IT per termini meno comuni |
| Glossario (EN) | `Knowledge/Glossary.md` (KNW-GLS-001) | Riferimento tecnico internazionale — non normativo per l'output |
| Parole Vietate | `Knowledge/ForbiddenWords.md` (KNW-FBD-001) | Lista di esclusione — vedi § 4 |

---

## 1. Termini tecnici principali (italiano ufficiale)

| Termine ufficiale | Termini vietati | Descrizione |
|--------------------|-------------------|-------------|
| Carrozzeria | corpo, scocca, bodywork | La scocca in policarbonato o ABS del modello |
| Verniciatura | colorazione, pittura | Il processo di applicazione del colore |
| Mascheratura | nastro, taping | Protezione delle aree con nastro o fluido |
| Primer | fondo, sottofondo, base coat | Strato preparatorio prima del colore |
| Smalto | paint (in italiano) | Vernice in senso generico |
| Diluente | thinner (quando non specificato) | Solvente per diluire la vernice |
| Stucco | filler | Materiale per correggere imperfezioni superficiali |
| Grana | grit | Grado di abrasività della carta vetrata |
| Mano | coat, strato | Un'applicazione di vernice |
| Vernice trasparente | clear coat | Strato protettivo finale trasparente |
| Decalcomania | decal | Decorazione adesiva o a risciacquo |

## 2. Finiture

| Termine ufficiale | Inglese (solo riferimento) | Vietato in output |
|---------------------|-------------------------------|----------------------|
| Lucido | Gloss | "Gloss", "brillante" |
| Opaco | Matte / Flat | "Matte", "mat", "piatto" |
| Satinato | Satin | "Satin", "semi-lucido" |
| Metallizzato | Metallic | "Metallic", "metal" |
| Perlato | Pearl | "Pearl", "perla" |
| Cromato | Chrome | "Chrome", "specchio" |

## 3. Strumenti, componenti visuali, pagine

Strumenti (estratto): Aerografo (*airbrush* accettato in corsivo al primo uso), Bomboletta spray, Pennello, Tronchesi, Coltello da modellismo, Carta vetrata, Nastro da mascheratura, Aria compressa.

Etichette dei componenti visuali (usate in intestazioni e titoli): `C006 Callout` → NOTA / INFORMAZIONE / NOTA TECNICA; `C008 Warning` → ATTENZIONE; `C009 Tips` → SUGGERIMENTO; `C015 Notes` → NOTE.

Etichette pagina (sezione destra `C001 Header`):

| Pagina | Etichetta italiana |
|--------|----------------------|
| P001 | COPERTINA |
| P002 | SCHEMA COLORI |
| P003 | MATERIALI |
| P004 | PREPARAZIONE |
| P005 | VERNICIATURA |
| P006 | MASCHERATURA |
| P007 | DETTAGLI |
| P008 | DECALCOMANIE |
| P009 | VARIANTE PREMIUM |
| P010 | CHECKLIST FINALE |

Elenco completo di tutte le categorie (chimica delle vernici, superfici, processo, aerografo, difetti) in `Knowledge/Terminology.md` — non riprodotto qui per intero; consultare il documento sorgente per l'equivalenza EN→IT di ogni termine tecnico meno comune.

## 4. Parole ed espressioni da NON usare mai

> ⚠️ **Warning:** questa sezione elenca esclusioni, non alternative valide da cui scegliere. Ogni voce qui presente è vietata in qualunque testo editoriale generato dallo SDK, verificato da `Tests/TextValidation.md`.

**Script non latini — tolleranza zero.** Kanji, Hiragana, Katakana, punteggiatura CJK, Katakana a larghezza dimezzata, Latino a larghezza intera, cinese (semplificato/tradizionale), coreano, arabo, cirillico, devanagari: nessuno di questi script ha alcun ruolo nel livello testuale dello SDK. L'ispirazione estetica giapponese riguarda solo il design visivo, mai il testo (`Knowledge/ForbiddenWords.md § Rationale`).

**Testo segnaposto vietato:** "Lorem ipsum" e varianti, "Foo/Bar/Baz", "Test text", "Testo di prova", `TODO` in output editoriale, "[INSERT TEXT HERE]", "Sample text", "Placeholder", "N/A" nel corpo editoriale, "TBD". Sostituto approvato: `[TESTO]` oppure `[VALORE NON SPECIFICATO]` — mai `TODO:` nel testo finale (il placeholder `TODO:` è ammesso solo nelle fasi intermedie, vedi Capitolo 07).

**Termini inglesi con equivalente italiano obbligatorio:** "Gloss"→Lucido, "Matte/Matt"→Opaco, "Metallic"→Metallizzato, "Pearl"→Perlato, "Satin"→Satinato, "Step N"→Passo N, "Warning"→Attenzione, "Tip/Pro tip"→Suggerimento, "Note"→Nota, e le etichette di pagina della tabella in § 3. Eccezione: termini tecnici privi di equivalente italiano sono ammessi in *corsivo* alla prima occorrenza soltanto — *airbrush*, *spray*, *primer*.

**Linguaggio marketing vietato:** "fantastico", "incredibile", "perfetto", "ideale per tutti", "il migliore sul mercato", "rivoluzionario", "innovativo", "facile e veloce", "risultati professionali garantiti", "adatto a tutti i livelli", "senza sforzo".

**Linguaggio informale vietato:** "dai una mano" (colloquiale) → "Applica una mano"; "metti su il primer" → "Applica il primer"; "fai asciugare" → "Lascia asciugare"; "tipo"/"roba"/"un bel po'"/"alla fine" (vaghi) → riformulare in modo specifico; "dai!", "occhio!" → rimuovere o sostituire con "Attenzione:".

**Auto-riferimento dell'AI vietato:** "Ecco il testo generato...", "Come richiesto...", "Ho generato il seguente...", "Nota: questo testo è stato...", "Posso aiutarti con...", "Certamente!/Certo!" — qualunque testo che riveli il processo di generazione AI non deve mai comparire nell'output.

## Vedi anche

- Capitolo 07 — TextEngine (dove questi glossari vengono caricati come input)
- Capitolo 11 — QA (`Tests/TextValidation.md` verifica il rispetto di questa terminologia)
- Capitolo 04 — Bootstrap (`Config/LANGUAGE_POLICY.yaml` nel `required_read_order`)
