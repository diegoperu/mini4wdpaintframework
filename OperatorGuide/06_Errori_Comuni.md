# 06 — Errori Comuni

**OperatorGuide · Mini4WD Manual SDK v2.4.1**

> Errori realmente osservati durante il primo test con un operatore esterno
> (report completo: `../UAT/UAT-001.md`), più gli errori classici delle sessioni AI.
> Formato: sintomo → causa → soluzione.

---

## E01 — Validation FAIL su P001 subito dopo il bootstrap

**Sintomo:** bootstrap OK, lanci la validazione su P001 e piove di FAIL (campi vuoti,
placeholder, "contenuto mancante").
**Causa:** hai validato il **template** di `ApprovedAssets/Text/P001/` — che nasce con
campi vuoti e `status: draft` — invece del contenuto generato. Un template non è
contenuto finale.
**Soluzione:** prima **Fase 2** (genera content.yaml), poi **Fase 3** (valida). Il QA
si applica solo a contenuto generato (status `review` in poi) — vedi
`Tests/ContentValidation.md §Validation Scope`.

## E02 — Il validatore segnala come "inglese vietato" nomi di vernici e codici

**Sintomo:** FAIL su "Chrome Silver", "Gun Metal", "Semi Gloss Black", "Primer",
"TS-37", "X-10", oppure su chiavi come "Header", "Footer", "draft".
**Causa:** confusione tra **contenuto editoriale** (deve essere italiano) e
**metadati/termini tecnici** (language-neutral): nomi commerciali delle vernici,
codici prodotto, chiavi YAML, stati del lifecycle.
**Soluzione:** questi termini sono legittimi e whitelistati in
`Config/LANGUAGE_POLICY.yaml §exceptions` (v2.4.1). Se l'AI li segnala lo stesso,
rispondile: «Applica LANGUAGE_POLICY §exceptions: nomi commerciali, codici vernice e
chiavi YAML sono language-neutral». Il testo che descrive («Applica il primer…») resta
italiano; il nome del prodotto («Tamiya Surface Primer») resta com'è.

## E03 — Foto nel posto sbagliato

**Sintomo:** l'AI non trova le immagini, o documenti diversi indicano cartelle diverse.
**Causa:** documentazione pre-2.4.1 ambigua tra `Projects/{Modello}/Images/` e
`Assets/ReferenceModels/{Modello}/`.
**Soluzione:** convenzione unica v2.4.1 — **tutte le tue immagini in
`Projects/{Modello}/Images/`**. `Assets/ReferenceModels/` è solo del Maintainer.

## E04 — Nome cartella con trattini

**Sintomo:** `Projects/Dash-01_Shadow_Emperor/` — QA naming FAIL o slug incoerenti.
**Causa:** il trattino appartiene al `modelSlug` (kebab-case), non alla cartella.
**Soluzione:** cartella con **underscore** (`Dash_01_Shadow_Emperor/`), slug con
trattini (`dash-01-shadow-emperor`). Rinomina la cartella e aggiorna PROJECT.yaml.

## E05 — "Devo creare anche PROJECT.md, CHECKLIST.md…?"

**Sintomo:** documenti diversi elencano set di file diversi per il progetto.
**Causa:** ambiguità documentale pre-2.4.1.
**Soluzione:** set **minimo** per il bootstrap: `PROJECT.yaml` + `Images/` + `Output/`
+ `Notes/`. Gli altri template sono opzionali (utili, non bloccanti). Vedi
`PROJECT_STRUCTURE.md`.

## E06 — Placeholder sbagliato

**Sintomo:** FAIL per "[TEXT HERE]", "Lorem ipsum", o dubbio tra `TODO:` e `[TITOLO]`.
**Causa:** due famiglie di placeholder con usi diversi.
**Soluzione:** **tu e l'AI usate solo `TODO:`** per i dati mancanti. I placeholder
`[TITOLO]`-style sono marcatori interni dei template SDK: se ne vedi uno in un
contenuto generato, la generazione è incompleta — rigenera. Lorem ipsum: mai.

## E07 — L'AI riscrive il testo durante il rendering

**Sintomo:** la pagina illustrata ha frasi diverse dal content.yaml.
**Causa:** l'AI è uscita dal Render Mode.
**Soluzione:** rilancia il prompt Fase 4 sottolineando: «Leggi ESCLUSIVAMENTE da
content.yaml. Non generare testo nuovo». Se persiste, nuova chat, ri-bootstrap render.

## E08 — Tutto il manuale in un colpo solo

**Sintomo:** «Generami P001–P010» → output lunghissimo, qualità in caduta, QA impossibile.
**Causa:** salto del loop per-pagina.
**Soluzione:** una pagina alla volta: genera → valida → sigilla → prossima.

## E09 — Chat degenerata

**Sintomo:** l'AI dimentica le regole, mescola le fasi, cita dati di altri modelli.
**Causa:** contesto saturo o contaminato.
**Soluzione:** nuova chat con **Prompt F — Continuità** (`Docs/AI_BOOTSTRAP_PROMPT.md`),
indicando pagine completate e pagina corrente.

## E10 — Dati inventati dall'AI

**Sintomo:** nel content.yaml compaiono codici vernice o tempi di essiccazione che non
hai mai fornito.
**Causa:** l'AI ha riempito i buchi.
**Soluzione:** REJECT in QA (CV-003-F). Fai sostituire ogni dato inventato con il
valore vero da PROJECT.yaml o con `TODO:`. Poi, se serve, completa PROJECT.yaml e
rigenera.
