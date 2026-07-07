# Golden Projects

**Mini4WD Manual SDK** · Quality Management System · Documento 10

| Campo | Valore |
|-------|--------|
| Scopo | Registro dei Golden Projects — manuali completi che certificano una versione del framework |
| Destinatario | Maintainer (aggiornamento), tutti (consultazione) |
| Source of Truth | Questo documento |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Cos'è un Golden Project

Un Golden Project è un manuale completato end-to-end (Bootstrap → Testi → QA → Rendering → QA → PDF) che rispetta tutte le specifiche del framework e viene conservato come **riferimento certificato** di cosa una versione dell'SDK sa produrre. Vedi `Documentation/OperationalManual/13_GoldenProjects.md` per i criteri di qualità.

Ruolo nel QMS:

- una **Major Release** richiede almeno 1 Golden Project completato con la versione candidata (`02_RELEASE_CRITERIA.md §4`)
- un **Golden Project non realizzabile** è una delle cinque evidenze che giustificano una modifica al framework (`01_RELEASE_POLICY.md §1`)
- ogni Golden Project completato chiude con una Retrospettiva (`14_RETROSPECTIVE_TEMPLATE.md`); ogni tentativo fallito apre un Post-Mortem (`13_POST_MORTEM_TEMPLATE.md`)

Stati ammessi: `In corso` / `Completato` / `Fallito (→ Post-Mortem)` / `Superato` (resta valido come archivio ma non certifica più la versione corrente).

---

## Registro

| Nome | Versione SDK | Versione AI | Numero pagine | Data | Stato | Note |
|------|--------------|-------------|---------------|------|-------|------|
| — | — | — | — | — | — | Nessun Golden Project ancora completato. Primo candidato: completamento di un manuale con v2.4.1 dopo le correzioni UAT-001. |

---

## Storico tentativi

| Nome | Versione SDK | Data | Esito | Riferimento |
|------|--------------|------|-------|-------------|
| Dash-01_Shadow_Emperor | 2.4.0 | 2026-07-01/02 | Interrotto a P001 (non era un tentativo Golden formale; test operatore) | `UAT/UAT-001.md` |
