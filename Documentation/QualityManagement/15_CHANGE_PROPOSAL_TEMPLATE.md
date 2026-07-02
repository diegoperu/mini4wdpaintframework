# Change Proposal Template

**Mini4WD Manual SDK** · Quality Management System · Documento 15

| Campo | Valore |
|-------|--------|
| Scopo | Template obbligatorio per proporre QUALSIASI modifica al framework |
| Destinatario | Chiunque proponga una modifica; Maintainer (decisione) |
| Source of Truth | Questo documento (per il formato) |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Istruzioni

Dal momento in cui il framework è STABLE (DEC-001), **nessuna modifica a documenti autoritativi entra nel repository senza una Change Proposal approvata**. Fanno eccezione solo le correzioni Trivial (refusi senza effetto operativo), che richiedono comunque una riga nel CHANGELOG.

Salva ogni proposta in `Documentation/QualityManagement/Changes/CP-{NNN}.md`. Il Maintainer decide: la proposta approvata entra in `11_ROADMAP.md` (APPROVATO) e viene assegnata a una release secondo `01_RELEASE_POLICY.md`; quella respinta va in RIFIUTATO con motivazione.

Una proposta senza evidenze (nessun UAT, nessun report, nessun bug) viene respinta per definizione: prima si raccolgono i dati, poi si propone.

---

```markdown
# CP-___ — {Titolo breve della modifica}

| Campo | Valore |
|-------|--------|
| ID | CP-___ |
| Data | AAAA-MM-GG |
| Proposto da | |
| Stato | Proposta / Approvata / Rifiutata |
| Release destinazione | Patch / Minor / Major — v___ |

## Problema osservato

(Il problema reale, osservato durante l'uso. Non la soluzione: il problema.)

## Fonte

(Da dove arriva l'evidenza. Elencare i riferimenti esatti.)

| Tipo | Riferimenti |
|------|-------------|
| Bug confermati | BUG-___ |
| UAT | UAT-___ |
| User Report | UR-___ |
| Golden Project non realizzabile | |
| Cambiamento modelli AI | |

## Numero UAT coinvolti

(Quanti UAT distinti hanno evidenziato questo problema.)

## Numero utenti coinvolti

(Quanti operatori distinti lo hanno incontrato.)

## Alternative

(Almeno un'alternativa considerata, inclusa "non fare nulla". Perché la modifica proposta è preferibile.)

1. **Non fare nulla:** 
2. 

## Impatto

(Documenti da modificare, fasi della pipeline toccate, ruoli coinvolti. Elenco esplicito dei file.)

| File | Tipo di modifica |
|------|------------------|
| | |

## Compatibilità

- [ ] Nessun impatto sui progetti esistenti (→ ammissibile in Patch/Minor)
- [ ] Retrocompatibile con deprecazione (→ Minor)
- [ ] Breaking change (→ Major, richiede Migration Report)

## Decisione proposta

(La modifica in forma decisionale, come comparirà nel Decision Log se approvata: "Il framework adotta X perché Y, con conseguenze Z.")
```
