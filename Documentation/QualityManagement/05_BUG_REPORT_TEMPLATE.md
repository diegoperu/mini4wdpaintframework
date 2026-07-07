# Bug Report Template

**Mini4WD Manual SDK** · Quality Management System · Documento 05

| Campo | Valore |
|-------|--------|
| Scopo | Template standard per la segnalazione di bug del framework |
| Destinatario | Operatore, Tester, Reviewer, Maintainer |
| Source of Truth | Questo documento (per il formato); i bug confermati alimentano i Release Criteria |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Istruzioni

Nel Mini4WD Manual SDK un "bug" è quasi sempre un **difetto di documentazione o di specifica**: un'istruzione errata, ambigua, contraddittoria o mancante che produce un risultato sbagliato (Validation FAIL indebito, output non conforme, workflow bloccato). Vale il principio stabilito da UAT-001: *"il problema non è l'utente — è la documentazione"*.

Salva ogni bug in `Documentation/QualityManagement/Bugs/BUG-{NNN}.md`. Un bug diventa **confermato** quando il Maintainer lo riproduce o ne verifica la causa nei documenti. Solo i bug confermati contano per i criteri di rilascio (`02_RELEASE_CRITERIA.md`).

---

```markdown
# BUG-___ — {Titolo breve}

## Classificazione

| Campo | Valore |
|-------|--------|
| Bug ID | BUG-___ |
| Versione | (SDK in cui il bug è stato osservato) |
| Data | AAAA-MM-GG |
| Segnalato da | |
| Priorità | Alta / Media / Bassa (urgenza della correzione) |
| Severità | Blocker / Major / Minor / Trivial (vedi tabella sotto) |
| Riproducibilità | Sempre / Spesso / Raramente / Non riprodotto |
| Documento coinvolto | (path del/dei documenti, es. Tests/TextValidation.md) |
| Stato | Aperto / Confermato / In correzione / Risolto in v___ / Rifiutato |

## Descrizione

(Il difetto in 2-3 frasi: cosa dice o non dice la documentazione, e quale effetto produce.)

## Passi per riprodurre

1. 
2. 
3. 

## Comportamento atteso

(Cosa dovrebbe succedere secondo la documentazione autoritativa — cita il documento.)

## Comportamento reale

(Cosa succede. Errori esatti, output di validazione, testo generato.)

## Workaround

(Come aggirare il problema in attesa della correzione. "Nessuno" se bloccante.)

## Screenshot

- [ ] Sì — percorso/allegato: ______
- [ ] No
```

---

## Scala di severità

| Severità | Definizione | Esempio |
|----------|-------------|---------|
| Blocker | Impedisce di completare un manuale; nessun workaround | Bootstrap impossibile seguendo la documentazione |
| Major | Risultato sbagliato o fase bloccata; esiste un workaround | Validation FAIL su template non generati (UAT-001, Errore 1) |
| Minor | Attrito o ambiguità; il lavoro procede | Convenzione placeholder doppia (UAT-001, Errore 6) |
| Trivial | Refuso o difetto cosmetico senza effetto operativo | Typo in un README |
