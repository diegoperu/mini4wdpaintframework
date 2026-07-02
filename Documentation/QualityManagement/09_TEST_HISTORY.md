# Test History

**Mini4WD Manual SDK** · Quality Management System · Documento 09

| Campo | Valore |
|-------|--------|
| Scopo | Cronologia di tutti i test eseguiti sul framework (UAT, test di release, prove operative) |
| Destinatario | Maintainer (aggiornamento), tutti (consultazione) |
| Source of Truth | Questo documento per la cronologia; i singoli UAT/report per il dettaglio |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Come usare questo registro

Aggiungi una riga per ogni test concluso, in ordine cronologico inverso (il più recente in alto). Ogni riga rimanda al documento di dettaglio (UAT, User Report o nota). Esiti ammessi: `PASS`, `PASS con riserva`, `FAIL`.

---

## Cronologia

| Data | Tester | Versione SDK | Manuale | LLM | Image Model | Esito | Problemi | Dettaglio |
|------|--------|--------------|---------|-----|-------------|-------|----------|-----------|
| 2026-07-01/02 | Operatore esterno | 2.4.0 | Dash-01_Shadow_Emperor (interrotto a P001) | ChatGPT | — | FAIL | 8 errori indotti dalla documentazione (template validati come contenuto, falsi positivi linguistici, path immagini ambiguo, naming cartella, file set ambiguo, placeholder doppi, fasi/chat non mappate, nessun entry point operatore) | `UAT/UAT-001.md` |

---

## Statistiche (aggiornare a ogni release)

| Metrica | Valore |
|---------|--------|
| Test totali | 1 |
| PASS | 0 |
| PASS con riserva | 0 |
| FAIL | 1 |
| Ultimo test | 2026-07-02 |

Le metriche aggregate derivate da questa cronologia sono definite in `12_METRICS.md`.
