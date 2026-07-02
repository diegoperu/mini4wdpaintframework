# Version History

**Mini4WD Manual SDK** · Quality Management System · Documento 17

| Campo | Valore |
|-------|--------|
| Scopo | Registro storico sintetico delle versioni del framework: motivazione, ambito, compatibilità |
| Destinatario | Maintainer (aggiornamento), tutti (consultazione) |
| Source of Truth | `CHANGELOG.md` (root) per il dettaglio delle modifiche; questo documento per motivazione e compatibilità |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Come usare questo registro

Una riga per versione, la più recente in alto. Questo registro risponde a tre domande che il CHANGELOG non struttura: **perché** la versione esiste (quale evidenza l'ha giustificata), **cosa** ha toccato in sintesi, e **se** un progetto in corso può adottarla senza rischi. Il Maintainer la compila come parte della checklist di rilascio (`02_RELEASE_CRITERIA.md §5`).

---

## Registro

### v2.4.1 — 2026-07-02

| Campo | Valore |
|-------|--------|
| Tipo | Patch (UX & Operator Workflow) |
| Motivazione | UAT-001: primo test con operatore esterno, esito FAIL con 8 errori indotti dalla documentazione |
| Documenti modificati | Operator Layer nuovo (`START_HERE.md`, `OperatorGuide/` ×8, `WORKFLOW.md`, `FILE_MATRIX.md`, `PROJECT_STRUCTURE.md`, `FIRST_PROJECT/RENDER/PDF.md`, `WHO_MODIFIES_WHAT.md`, `LIFECYCLE.md`, `OPERATOR_PROFILE.md`, `UAT/UAT-001.md`); riscritti `Projects/PROJECT_BOOTSTRAP.md`, `Docs/AI_BOOTSTRAP_PROMPT.md`; scoping validazione in `Config/LANGUAGE_POLICY.yaml`, `Tests/ContentValidation.md`, `Tests/TextValidation.md`; metadati release |
| Compatibilità | Totale — nessuna modifica a comportamento, architettura, engine o ApprovedAssets |

### v2.4.0 — codename "CMS"

| Campo | Valore |
|-------|--------|
| Tipo | Minor |
| Motivazione | Bootstrap System v2: entry point ufficiale per modelli AI e contratto di bootstrap |
| Documenti modificati | Nuovi `AI_ENTRYPOINT.md`, `BOOTSTRAP.md`, `SDK_CONTEXT.yaml`, `STATUS.md`, `ReleaseInfo.yaml`, `RepositoryManifest.yaml`, `Docs/LOAD_ORDER.md`, `Docs/AI_BOOTSTRAP_PROMPT.md`, `Projects/PROJECT_BOOTSTRAP.md`; aggiornati README e cross-reference Core |
| Compatibilità | Retrocompatibile; `ApprovedText/` marcato legacy (percorso v2.3.0 ancora supportato) |

### Versioni precedenti (≤ 2.3.0)

Precedenti all'introduzione del QMS: il dettaglio è in `CHANGELOG.md`. Da questo punto in poi, ogni nuova versione DEVE avere la propria voce in questo registro.

---

## Regola per le voci future

Ogni nuova voce deve riportare: **Data**, **Tipo** (Patch/Minor/Major), **Motivazione** (con riferimenti alle evidenze: BUG-, UAT-, UR-, FR-, CP-), **Documenti modificati** (sintesi; dettaglio nel CHANGELOG), **Compatibilità** (Totale / Retrocompatibile / Breaking + Migration Report).
