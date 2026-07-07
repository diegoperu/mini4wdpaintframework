# Metrics

**Mini4WD Manual SDK** · Quality Management System · Documento 12

| Campo | Valore |
|-------|--------|
| Scopo | Definire le metriche qualitative del framework e come raccoglierle |
| Destinatario | Maintainer (analisi), Operatore (raccolta via User Report) |
| Source of Truth | Questo documento per le definizioni; `09_TEST_HISTORY.md` e i report per i dati grezzi |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## 1. Principio

Le metriche misurano il framework, non gli operatori. Servono a rispondere a una sola domanda: *il framework sta diventando più facile e più affidabile da usare, versione dopo versione?* I dati grezzi arrivano da User Report (`03`), UAT (`04`) e Test History (`09`). Il Maintainer aggiorna la tabella §3 a ogni release.

---

## 2. Definizione delle metriche

| # | Metrica | Definizione | Fonte | Direzione buona |
|---|---------|-------------|-------|-----------------|
| M01 | Tempo medio Bootstrap | Tempo dal primo prompt al Bootstrap Report OK | User Report §Sessione | ↓ |
| M02 | Tempo medio P001 | Tempo dal Bootstrap OK alla prima pagina (P001) con testo approvato | User Report §Sessione | ↓ |
| M03 | Numero medio di rigenerazioni | Rigenerazioni (testo o immagine) per pagina prima dell'approvazione | User Report §Errori | ↓ |
| M04 | Numero FAIL Validation | Validation FAIL per manuale (Tests/ContentValidation, TextValidation) | User Report §Errori | ↓ |
| M05 | Numero FAIL Rendering | Render scartati al QA immagini, per manuale | User Report §Errori | ↓ |
| M06 | Numero Prompt ripetuti | Prompt reinviati identici o quasi per ottenere l'output atteso | User Report §Difficoltà | ↓ |
| M07 | Numero manuali completati | Manuali arrivati a PDF finale, per versione SDK | Test History | ↑ |
| M08 | Golden Projects | Golden Projects certificati, per versione SDK | 10_GOLDEN_PROJECTS.md | ↑ |
| M09 | Tasso PASS UAT | UAT con esito PASS / UAT totali della versione | Test History | ↑ |
| M10 | Valutazione media operatore | Media del voto 1-5 dei User Report della versione | User Report §Valutazione | ↑ |
| M11 | Bug confermati per versione | Bug con stato Confermato aperti contro la versione | Bugs/ | ↓ |
| M12 | Documenti segnalati poco chiari | Documenti distinti citati in §Documenti poco chiari | User Report | ↓ |

---

## 3. Rilevazioni per versione

Aggiornare a ogni release. "—" = dato non ancora disponibile.

| Metrica | v2.4.0 | v2.4.1 | v2.5.0 |
|---------|:------:|:------:|:------:|
| M01 Tempo medio Bootstrap | — | — | |
| M02 Tempo medio P001 | non raggiunto (UAT-001) | — | |
| M03 Rigenerazioni medie | — | — | |
| M04 FAIL Validation | 1+ indebito (UAT-001) | — | |
| M05 FAIL Rendering | — | — | |
| M06 Prompt ripetuti | — | — | |
| M07 Manuali completati | 0 | 0 | |
| M08 Golden Projects | 0 | 0 | |
| M09 Tasso PASS UAT | 0/1 | — | |
| M10 Valutazione media | — | — | |
| M11 Bug confermati | 8 (UAT-001) | 0 | |
| M12 Documenti poco chiari | 6+ (UAT-001) | — | |

---

## 4. Soglie di attenzione

Superata una soglia, il Maintainer apre una valutazione (non necessariamente una release):

- M04 > 2 FAIL Validation indebiti per manuale → probabile difetto di scoping nei test
- M06 > 3 prompt ripetuti per fase → probabile ambiguità nel Prompt Engine o nella guida
- M09 < 50% PASS → blocco delle Minor finché la causa non è capita
- M10 < 3/5 su 2+ report → retrospettiva obbligatoria sull'onboarding
