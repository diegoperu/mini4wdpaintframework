# Post-Mortem Template

**Mini4WD Manual SDK** · Quality Management System · Documento 13

| Campo | Valore |
|-------|--------|
| Scopo | Template da compilare quando un manuale NON viene completato |
| Destinatario | Operatore (compilazione), Maintainer (analisi) |
| Source of Truth | Questo documento (per il formato) |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Istruzioni

Compila un Post-Mortem ogni volta che un manuale viene abbandonato o non arriva al PDF finale. Salva in `Documentation/QualityManagement/PostMortems/PM-{NNN}.md`. Un Post-Mortem è senza colpe: per il framework vale il principio di UAT-001 — *se un operatore che segue la documentazione fallisce, il difetto è nella documentazione*. Ogni Post-Mortem deve produrre almeno un'azione concreta (bug report, change proposal, o motivazione esplicita del perché non serve).

---

```markdown
# PM-___ — {Nome progetto non completato}

| Campo | Valore |
|-------|--------|
| ID | PM-___ |
| Data | AAAA-MM-GG |
| Operatore | |
| Versione SDK | |
| Progetto | Projects/______ |
| Fase raggiunta | Bootstrap / Testi / QA / Rendering / PDF |

## Obiettivo

(Cosa si voleva produrre: modello, numero pagine previsto, scadenze.)

## Problema

(Cosa ha impedito il completamento. Fatti, non interpretazioni: errori esatti, output, punti di blocco.)

## Causa

(Causa radice. Distingui: difetto di documentazione / limite del modello AI / dati di progetto insufficienti / errore operativo indotto / causa esterna.)

## Documentazione coinvolta

(Documenti del framework che hanno contribuito al problema o che avrebbero dovuto prevenirlo.)

| Documento | Ruolo nel problema |
|-----------|--------------------|
| | |

## Correzione

(Cosa è stato fatto o proposto: Bug ID aperti, Change Proposal, workaround adottati. Se nessuna correzione è necessaria, spiegare perché.)

## Lezione appresa

(Cosa questo fallimento insegna sul framework. Una frase che un futuro operatore o Maintainer dovrebbe leggere PRIMA di trovarsi nello stesso punto.)
```
