# Feature Request Template

**Mini4WD Manual SDK** · Quality Management System · Documento 06

| Campo | Valore |
|-------|--------|
| Scopo | Template per proporre nuove funzionalità del framework |
| Destinatario | Operatore, Contributor, Maintainer |
| Source of Truth | Questo documento (per il formato); le richieste approvate entrano in 11_ROADMAP.md |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Istruzioni

Una Feature Request propone una capacità che il framework oggi non ha. Salva ogni richiesta in `Documentation/QualityManagement/Features/FR-{NNN}.md`. Il Maintainer la valuta e la sposta in `11_ROADMAP.md` (BACKLOG → IN VALUTAZIONE → APPROVATO / RIFIUTATO). Una feature approvata entra nel framework solo tramite Minor o Major Release, previa Change Proposal (`15_CHANGE_PROPOSAL_TEMPLATE.md`).

Una richiesta senza un problema reale documentato (report, UAT, Golden Project non realizzabile) parte con priorità Bassa.

---

```markdown
# FR-___ — {Titolo breve}

## Classificazione

| Campo | Valore |
|-------|--------|
| Feature ID | FR-___ |
| Data | AAAA-MM-GG |
| Proposto da | |
| Priorità proposta | Alta / Media / Bassa |
| Stato | Proposta / In valutazione / Approvata / Rifiutata |

## Motivazione

(Perché serve. Riferisci evidenze concrete: UR-___, UAT-___, Golden Project non realizzabile, cambiamento nei modelli AI.)

## Problema risolto

(Il problema specifico che oggi non si può risolvere, o si risolve male. Un caso reale vale più di dieci ipotetici.)

## Impatto

(Cosa cambia nel framework: quali documenti, quali fasi della pipeline, quali ruoli. Stima: piccolo / medio / grande.)

| Area | Impatto |
|------|---------|
| Prompt Engine | |
| Text Engine | |
| Rendering Engine | |
| Pipeline / Workflow | |
| Documentazione operatore | |

## Alternative

(Come si può ottenere un risultato simile SENZA questa feature. Se un'alternativa ragionevole esiste già, spiegare perché non basta.)

## Compatibilità

- [ ] Retrocompatibile — i progetti esistenti non sono toccati (→ Minor)
- [ ] Richiede migrazione — i progetti esistenti vanno adattati (→ Major)
- [ ] Da valutare

## Priorità

(Giustifica la priorità proposta: quanti utenti/progetti sono toccati, con quale frequenza.)
```
