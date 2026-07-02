# Capitolo 07 — Text Engine

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Specifica principale | `Core/TEXT_ENGINE.md` | Source of truth — architettura, workflow, schema content.yaml |
| Politica linguistica | `Config/LANGUAGE_POLICY.yaml` | Regole di lingua italiana a tolleranza zero |
| Prompt per pagina | `PromptEngine/README.md` + 10 file (Cover.md…FinalChecklist.md) | Esecutori dei prompt per P001–P010 |
| Stile editoriale | `Knowledge/EditorialStyle.md` | Tono, registro, struttura frase |
| Terminologia | `Knowledge/Terminology.md` | Termini tecnici EN→IT con note d'uso |
| Parole vietate | `Knowledge/ForbiddenWords.md` | Script, placeholder, inglese, marketing, informale, auto-riferimento AI |
| Glossario IT/EN | `Knowledge/GlossaryIT.md`, `Knowledge/Glossary.md` | Riferimento terminologico primario |
| Conoscenza tecnica | `Knowledge/Paints.md`, `Masking.md`, `Preparation.md`, `Painting.md`, `Decals.md`, `ClearCoat.md` | Contesto fattuale, non prompt |
| QA contenuto | `Tests/ContentValidation.md` | 7 suite — valida `content.yaml` |
| QA testo | `Tests/TextValidation.md` | 9 test — conformità italiana |
| QA prompt | `Tests/PromptValidation.md` | Valida i file di PromptEngine/ stessi |

## Cos'è e perché esiste

Il Text Engine è il sottosistema editoriale dello SDK: produce ogni contenuto scritto — titoli, descrizioni dei passi, avvertenze, sequenze di verniciatura, liste materiali — indipendentemente dalla resa visiva. Il principio cardine (`Core/TEXT_ENGINE.md §Philosophy`) è che il testo non è decorazione: ha identità editoriale, deve essere validato prima di entrare in qualunque pipeline visiva, e una volta approvato diventa fonte autoritativa unica — il Render Engine (Capitolo 10) non parafrasa, non traduce, non abbrevia.

La separazione Text Engine / Render Engine è netta per design: qualità del testo verificabile indipendentemente, conformità linguistica imposta prima del render, nessun render può contenere testo inventato.

## Evoluzione dello schema di output (v2.3.0 → v2.4.0)

| Versione | Output primario | Percorso |
|----------|------------------|----------|
| v2.3.0 | Markdown (`P{NNN}.md`) | `Projects/{ModelName}/ApprovedText/` |
| v2.4.0 | YAML strutturato (`content.yaml`) — **attuale** | `ApprovedAssets/Text/P{NNN}/content.yaml` |

Dalla v2.4.0, `content.yaml` è la fonte di verità primaria; `text.md` è derivato automaticamente per la sola lettura umana. Se i due file discordano, vince sempre `content.yaml`. La distinzione cruciale nello schema: i **nomi** dei campi in `content.yaml` sono in inglese (chiavi strutturali), i **valori** sono in italiano (contenuto editoriale) — es. `title: "Campione dell'Imperatore"`, mai `titolo: "..."`.

## Workflow operativo

1. **Inizializzazione:** verificare che `PROJECT.yaml` sia completo, caricare `Config/LANGUAGE_POLICY.yaml` e i documenti `Knowledge/` rilevanti.
2. **Generazione (per pagina P001–P010):** aprire `PromptEngine/{PageName}.md`, risolvere tutti i token `{{...}}` da PROJECT.yaml, iniettare la LOAD sequence (v2.4.0, 9 step — vedi `PromptEngine/README.md §v2.4.0`), inviare al modello AI.
3. **QA contenuto:** eseguire `Tests/ContentValidation.md` (schema YAML, compliance linguistica, accuratezza dati, metadata, manifest, mapping componenti, coerenza cross-page).
4. **QA testo:** eseguire `Tests/TextValidation.md` (9 categorie — lingua, testo fittizio, token risolti, frontmatter, terminologia, tono, tipografia, completezza, controlli per-pagina).
5. **Sigillo:** `metadata.yaml → status: approved` (o `locked` per il freeze di produzione), aggiornare `ApprovedAssets/index.yaml`, loggare in `changelog.md`.
6. **Passaggio al Render Engine:** che legge esclusivamente `content.yaml` di pagine `approved` o `locked` — mai `PROJECT.yaml` direttamente (cambio v2.4.0).

## La politica linguistica in sintesi

`Config/LANGUAGE_POLICY.yaml` impone italiano a tolleranza zero: nessun kanji/hiragana/katakana (nemmeno come decorazione — Rule 058 in `Core/DESIGN_LANGUAGE.md`), nessun paragrafo inglese, nessun Lorem ipsum. Eccezioni language-neutral: codici vernice (`TS-57`), ID componenti/pagina, unità di misura, valori numerici. Separatore decimale `,` non `.`; virgolette `«»`. Quando un dato manca, si usa uno dei 10 placeholder approvati (`[TITOLO]`, `[TESTO]`, `[SUGGERIMENTO]`, ecc.) — mai inventare.

`Knowledge/ForbiddenWords.md` cataloga sei categorie di violazioni: script non latini, placeholder generici ("Lorem ipsum", "TBD"), termini inglesi con equivalente italiano obbligatorio (tabella di 25 sostituzioni: "Gloss"→"Lucido", "Step N"→"Passo N", ecc.), linguaggio marketing ("fantastico", "rivoluzionario"), linguaggio informale ("dai una mano", "tipo"), e auto-riferimento AI ("Ecco il testo generato...", "Certamente!").

## Conoscenza tecnica vs prompt: la distinzione critica

`Knowledge/README.md` stabilisce una regola netta: **Knowledge/** contiene riferimento fattuale senza data di scadenza SDK (marche di vernice, tecniche di mascheratura, sequenze di asciugatura), **PromptEngine/** contiene istruzioni di generazione specifiche di versione SDK. Non mettere mai prompt in Knowledge/, non mettere mai riferimento fattuale in PromptEngine/. I file tecnici (`Paints.md`, `Masking.md`, `Preparation.md`, `Painting.md`, `Decals.md`, `ClearCoat.md`) possono essere iniettati come contesto RAG opzionale prima di un prompt, ma non sono essi stessi eseguibili.

## Mappa pagina → contenuto

| Pagina | Prompt | Campi content.yaml chiave |
|--------|--------|---------------------------|
| P001 Cover | `Cover.md` | title, subtitle, footer.page_id, render.file |
| P002 ColorScheme | `ColorScheme.md` | colors[] (min 1) |
| P003 Materials | `Materials.md` | paints[], tools[] |
| P004 Preparation | `Preparation.md` | steps[] (title+description) |
| P005 Painting | `Painting.md` | sequence[] |
| P006 Masking | `Masking.md` | zones[] |
| P007 Details | `Details.md` | areas[] |
| P008 Decals | `Decals.md` | decals[] |
| P009 Premium (condizionale) | `Premium.md` | variant_name — solo se `premiumVariant.enabled: true` |
| P010 FinalChecklist | `FinalChecklist.md` | checklist_sections[] |

Campi richiesti per pagina: `Tests/ContentValidation.md TEST-CV-001`.

## ⚠️ Incoerenza rilevata: i prompt di PromptEngine/ non sono allineati a v2.4.0

Questo è il punto di maggiore attrito trovato analizzando il framework per questo capitolo. `Core/TEXT_ENGINE.md` e `PromptEngine/README.md` dichiarano entrambi che dalla v2.4.0 l'output primario del Text Engine è `content.yaml` in `ApprovedAssets/Text/P{NNN}/`. Ma i 10 file prompt effettivi (`PromptEngine/Cover.md`, `ColorScheme.md`, ecc.) non menzionano mai `content.yaml`: istruiscono a salvare l'output in `Projects/{{project.modelSlug}}/Output/raw/P{NNN}_raw.md` — il pattern v2.3.0 superseduto.

Inoltre i prompt mescolano compiti che l'architettura dichiara separati: specificano font, colori esadecimali, posizioni in millimetri (lavoro da Render Mode) nello stesso file che genera il testo (lavoro da Text Mode). Questo contraddice direttamente `AI_ENTRYPOINT.md §AI Operating Mode`: "Text Mode: Produce only YAML structure. No images. No layout decisions."

Un secondo problema concreto: i prompt scrivono valori colore come letterali esadecimali (`#5B2D8E`) invece di riferimenti token (`{{token.VioletPrimary}}`), in violazione diretta della Golden Rule G06 ("All visual values must reference Design Token names — no hardcoded hex/px/pt") — e della propria suite di test, che in `Tests/PromptValidation.md TEST-PR-005` richiede esplicitamente "All prompts include explicit instruction to use Design Tokens (not hardcoded hex values)".

**Implicazione operativa:** un contributor che segue `PromptEngine/*.md` alla lettera oggi produrrà output nel formato sbagliato per la pipeline v2.4.0 corrente. Fino a quando questi 10 file non vengono riscritti per generare `content.yaml` (separando le istruzioni di layout in prompt di Render Mode), il flusso corretto è: usare `PromptEngine/{page}.md` solo come riferimento dei campi richiesti e del tono, ma dirigere l'output generato verso lo schema `content.yaml` descritto in questo capitolo, non verso `Output/raw/P{NNN}_raw.md`. Segnalato per follow-up in `Validation/CONSISTENCY_CHECK.md` e `Validation/CHANGE_IMPACT.md`.

## Vedi anche

- Capitolo 04 — Bootstrap (LOAD sequence che precede ogni generazione testo)
- Capitolo 06 — ProjectYaml (fonte dati per ogni token)
- Capitolo 09 — ApprovedAssets (ciclo di vita del modulo pagina che ospita content.yaml)
- Capitolo 10 — RenderEngine (consumatore read-only di content.yaml)
- Capitolo 11 — QA (le due suite bloccanti ContentValidation/TextValidation)
- Capitolo 20 — Glossary (terminologia approvata usata dal Text Engine)
