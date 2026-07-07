# Decision Log

**Mini4WD Manual SDK** · Quality Management System · Documento 08

| Campo | Valore |
|-------|--------|
| Scopo | Registro delle decisioni architetturali e di processo del framework |
| Destinatario | Maintainer, Developer, futuri contributor |
| Source of Truth | Questo documento per le decisioni QMS/processo; `STYLE_DECISIONS.md` per le decisioni di design editoriale |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Formato

Ogni decisione è immutabile una volta registrata: se viene ribaltata, si aggiunge una NUOVA decisione che la sostituisce (con riferimento), non si modifica la vecchia.

```markdown
### DEC-___ 

| Campo | Valore |
|-------|--------|
| ID | DEC-___ |
| Data | AAAA-MM-GG |
| Stato | Attiva / Sostituita da DEC-___ |

**Problema:** 
**Decisione:** 
**Motivazione:** 
**Conseguenze:** 
**Documenti coinvolti:** 
```

---

## Decisioni registrate

### DEC-001 — Il framework è STABLE: evoluzione solo evidence-based

| Campo | Valore |
|-------|--------|
| ID | DEC-001 |
| Data | 2026-07-02 |
| Stato | Attiva |

**Problema:** dopo v2.4.1 il framework è funzionalmente completo per il ciclo Bootstrap → PDF. Modifiche continue "a sentimento" rischiano di degradare coerenza e tracciabilità.

**Decisione:** il framework è dichiarato STABLE. Ogni modifica futura richiede un'evidenza documentata (bug confermato, UAT, Golden Project non realizzabile, cambiamento nei modelli AI, requisito funzionale approvato) e passa per una Change Proposal.

**Motivazione:** UAT-001 ha dimostrato che il valore del framework sta nella coerenza della documentazione; modifiche non tracciate creano le stesse ambiguità che v2.4.1 ha corretto.

**Conseguenze:** ritmo di rilascio più lento; ogni release documentata; il QMS diventa vincolante per Maintainer e contributor.

**Documenti coinvolti:** intera cartella `Documentation/QualityManagement/`, `CHANGELOG.md`.

---

### DEC-002 — Il QMS vive in Documentation/QualityManagement/ e non tocca il framework

| Campo | Valore |
|-------|--------|
| ID | DEC-002 |
| Data | 2026-07-02 |
| Stato | Attiva |

**Problema:** dove collocare i processi di qualità senza interferire con Prompt Engine, Text Engine, Rendering Engine e pipeline.

**Decisione:** il QMS è un layer documentale separato in `Documentation/QualityManagement/`, accanto a `Documentation/OperationalManual/`. Non modifica alcun documento autoritativo del framework; i registri operativi (bug, report, feature) vivono in sottocartelle `Bugs/`, `Reports/`, `Features/`.

**Motivazione:** separazione tra "cosa fa il framework" (Core, Config, PromptEngine…) e "come lo si governa" (QMS). L'AI che genera manuali non deve caricare il QMS nel proprio contesto.

**Conseguenze:** il QMS non compare nel load order di bootstrap; gli UAT restano in `UAT/` (posizione preesistente) e il QMS li referenzia.

**Documenti coinvolti:** `Documentation/QualityManagement/*`, `UAT/`.

---

### DEC-003 — Gli UAT restano in UAT/ (root), il QMS li indicizza

| Campo | Valore |
|-------|--------|
| ID | DEC-003 |
| Data | 2026-07-02 |
| Stato | Attiva |

**Problema:** `UAT/UAT-001.md` esiste già in root; il QMS introduce il template UAT. Due possibili sedi per gli UAT futuri.

**Decisione:** gli UAT compilati continuano a vivere in `UAT/` (root). Il QMS fornisce il template (`04_UAT_TEMPLATE.md`) e la cronologia (`09_TEST_HISTORY.md`), che li referenzia.

**Motivazione:** evitare lo spostamento di file esistenti (nessuna modifica al framework) e mantenere un solo posto dove cercare gli UAT.

**Conseguenze:** chi compila un UAT salva in `UAT/`, poi registra l'esito in `09_TEST_HISTORY.md`.

**Documenti coinvolti:** `UAT/`, `04_UAT_TEMPLATE.md`, `09_TEST_HISTORY.md`.
