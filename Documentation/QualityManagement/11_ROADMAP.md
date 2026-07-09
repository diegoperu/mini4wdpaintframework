# QMS Roadmap

**Mini4WD Manual SDK** · Quality Management System · Documento 11

| Campo | Valore |
|-------|--------|
| Scopo | Registro governato delle evoluzioni del framework, per stato di approvazione |
| Destinatario | Maintainer (aggiornamento), Contributor (consultazione e proposte) |
| Source of Truth | Questo documento per lo STATO delle proposte; `ROADMAP.md` (root) per la visione di lungo periodo |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Regole

- Ogni elemento entra dal BACKLOG e si muove solo in avanti: BACKLOG → IN VALUTAZIONE → APPROVATO → IN SVILUPPO → COMPLETATO, oppure → RIFIUTATO in qualsiasi momento.
- **Ogni elemento riporta una motivazione** e, dove esiste, il riferimento all'evidenza (FR-, BUG-, UAT-, UR-).
- Il passaggio a APPROVATO richiede una Change Proposal (`15_CHANGE_PROPOSAL_TEMPLATE.md`) valutata dal Maintainer.
- Gli elementi RIFIUTATI restano nel registro con motivazione: evitano di ridiscutere le stesse idee.

---

## BACKLOG

| Elemento | Motivazione | Evidenza |
|----------|-------------|----------|
| Libreria icone SVG per C006 Callout e C008 Warning | Già pianificata in `CHANGELOG.md §Unreleased`; nessuna richiesta operatore ancora registrata | — |
| Pipeline PDF automatizzata (pandoc + LaTeX) | Ridurre il lavoro manuale della fase PDF; oggi interamente a carico dell'operatore | KI-002 |

## IN VALUTAZIONE

| Elemento | Motivazione | Evidenza |
|----------|-------------|----------|
| Supporto multi-lingua (Italiano, Giapponese, Inglese) | Pianificato in `CHANGELOG.md §Unreleased`; da valutare impatto su LANGUAGE_POLICY e Text Engine | — |

## APPROVATO

| Elemento | Motivazione | Evidenza |
|----------|-------------|----------|
| Compiler/ e Prompt Orchestrator (v2.5.0) | Già annunciato in `CHANGELOG.md §Unreleased` e `SDK_CONTEXT.yaml`; riduce i prompt ripetuti manualmente | Roadmap pre-QMS |
| Theme/Collana mechanism — schema di risoluzione (v2.6.0, Build Order step 2) | Nessun modo di applicare/aggiornare un tema a un'intera serie di manuali da un solo punto; oggi solo override CLI manuale per-render | CP-001 |

## IN SVILUPPO

| Elemento | Motivazione | Evidenza |
|----------|-------------|----------|
| — | | |

## COMPLETATO

| Elemento | Release | Motivazione | Evidenza |
|----------|---------|-------------|----------|
| Operator Layer (START_HERE, OperatorGuide, WORKFLOW, FILE_MATRIX…) | v2.4.1 | Onboarding operatore assente; 8 errori indotti dalla documentazione | UAT-001 |
| Validation Scoping (Template/Draft/Approved) | v2.4.1 | Validation FAIL su template non generati | UAT-001 Errore 1 |
| Language Policy §exceptions (5 categorie) | v2.4.1 | Falsi positivi su codici colore e nomi commerciali | UAT-001 Errore 2 |
| Quality Management System (questa cartella) | post-v2.4.1 | Governare l'evoluzione del framework con dati invece che opinioni | DEC-001 |

## RIFIUTATO

| Elemento | Motivazione del rifiuto | Evidenza |
|----------|-------------------------|----------|
| — | | |
