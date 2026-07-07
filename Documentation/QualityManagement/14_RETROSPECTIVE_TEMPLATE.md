# Retrospective Template

**Mini4WD Manual SDK** · Quality Management System · Documento 14

| Campo | Valore |
|-------|--------|
| Scopo | Template da compilare dopo ogni manuale COMPLETATO |
| Destinatario | Operatore (compilazione), Maintainer (analisi) |
| Source of Truth | Questo documento (per il formato) |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Istruzioni

Compila una Retrospettiva entro pochi giorni dal completamento di un manuale (PDF finale prodotto), finché i dettagli sono freschi. Salva in `Documentation/QualityManagement/Retrospectives/RETRO-{NNN}.md`. La Retrospettiva è complementare al User Report: il report registra i dati della sessione, la retrospettiva ragiona sul processo. Ogni azione elencata deve avere un responsabile e un riferimento QMS (bug, feature request, change proposal) oppure la dicitura "nessuna azione".

---

```markdown
# RETRO-___ — {Nome manuale completato}

| Campo | Valore |
|-------|--------|
| ID | RETRO-___ |
| Data | AAAA-MM-GG |
| Operatore | |
| Versione SDK | |
| Progetto | Projects/______ |
| User Report collegato | UR-___ |

## Cosa ha funzionato

(Parti del framework che hanno fatto il loro lavoro senza attriti. Essere specifici aiuta a NON toccarle nelle prossime release.)

- 
- 

## Cosa non ha funzionato

(Attriti, ambiguità, passaggi ripetuti. Anche ciò che alla fine si è risolto da solo.)

- 
- 

## Cosa migliorare

(Proposte concrete, in ordine di impatto percepito. Non tutte diventeranno modifiche: verranno filtrate dai Release Criteria.)

- 
- 

## Azioni

| Azione | Responsabile | Riferimento QMS |
|--------|--------------|-----------------|
| | | BUG-___ / FR-___ / CP-___ / nessuna azione |
```
