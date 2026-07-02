# UAT Template — User Acceptance Test

**Mini4WD Manual SDK** · Quality Management System · Documento 04

| Campo | Valore |
|-------|--------|
| Scopo | Template ufficiale per gli User Acceptance Test del framework |
| Destinatario | Tester, Reviewer, Maintainer |
| Source of Truth | Questo documento (per il formato); gli UAT compilati sono evidenze |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Istruzioni

Un UAT è un test formale del framework eseguito da un utente reale su uno scenario definito. Salva ogni UAT compilato in `UAT/UAT-{NNN}.md` (numerazione progressiva; UAT-001 già esistente). Un UAT con esito FAIL deve aprire almeno un Bug Report (`05_BUG_REPORT_TEMPLATE.md`) e va registrato in `09_TEST_HISTORY.md`.

Riferimento reale: `UAT/UAT-001.md` (primo test con operatore esterno, v2.4.0 → correzioni in v2.4.1).

---

```markdown
# UAT-___ — {Titolo breve dello scenario}

## Identificazione

| Campo | Valore |
|-------|--------|
| ID | UAT-___ |
| Versione SDK | |
| Tester | (nome + ruolo: Operatore / Reviewer / esterno) |
| Data | AAAA-MM-GG |

## Scenario

(Cosa si vuole verificare, in una frase. Es: "Un operatore che non ha mai usato il framework crea un progetto e completa il Bootstrap seguendo solo la documentazione.")

## Prerequisiti

(Stato iniziale richiesto: repository pulito, modello AI, immagini disponibili, conoscenze pregresse del tester.)

- 
- 

## Passaggi eseguiti

(Sequenza reale, numerata. Registra cosa il tester ha FATTO, non cosa avrebbe dovuto fare.)

1. 
2. 
3. 

## Risultato atteso

(Cosa la documentazione promette che accada.)

## Risultato ottenuto

(Cosa è accaduto davvero. Includi messaggi di errore esatti, output di validazione, comportamenti anomali.)

## Esito

- [ ] **PASS** — risultato ottenuto = risultato atteso
- [ ] **PASS con riserva** — obiettivo raggiunto, ma con attriti o workaround
- [ ] **FAIL** — obiettivo non raggiunto seguendo la documentazione

## Bug aperti

| Bug ID | Descrizione breve |
|--------|-------------------|
| | |

## Note

(Osservazioni non classificabili come bug: impressioni del tester, suggerimenti, tempi.)
```
