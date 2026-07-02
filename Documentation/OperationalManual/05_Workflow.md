# Workflow

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Workflow | `Core/WORKFLOW.md` | Panoramica di alto livello del processo end-to-end |
| Pipeline | `Build/Pipeline.md` | Source of Truth diretta — pipeline a 8 fasi, aggiornata a v2.4.0 |
| Build README | `Build/README.md` | Ruolo della cartella `Build/` |
| Manual System | `Core/MANUAL_SYSTEM.md` | Architettura e ciclo di vita del manuale (4 stati) |

## 1. Due documenti, due livelli di dettaglio

`Core/WORKFLOW.md` e `Build/Pipeline.md` descrivono lo stesso processo a granularità diversa. `Core/WORKFLOW.md` apre con: *"This document describes the complete end-to-end process for producing a Mini4WD painting manual using the SDK. Every manual follows this workflow. Skipping phases is not permitted."* Definisce 5 fasi (Phase 0–4): Project Setup, Render Generation, Manual Generation, QA, Approval & Publication.

`Build/Pipeline.md` è più granulare: 8 fasi (Phase 0–7), con input/output/attore/validazione per ciascuna, e — punto rilevante per questo capitolo — include tre blocchi di aggiornamento versione (v2.3.0, v2.4.0) che ridisegnano la Fase 2 in sotto-fasi (2a–2d) per riflettere l'introduzione del Text Engine e del livello CMS.

> ⚠️ **Nota di coerenza (per il manutentore):** `Core/WORKFLOW.md` non è stato aggiornato agli stessi livelli di dettaglio versionato di `Build/Pipeline.md`. Il suo Phase 2 ("Manual Generation") descrive ancora un flusso `Output/raw/` → `Output/approved/` con `qa_log.md` in stile `QA-001: PASS`, senza menzionare `content.yaml`, `ApprovedAssets/`, o il ciclo di vita `draft → review → approved → locked → rendered → released → archived` introdotto in v2.4.0. Questo non è necessariamente un errore — `Core/WORKFLOW.md` potrebbe descrivere il flusso generico indipendente da CMS — ma è una divergenza che vale la pena segnalare: se pianifichi di aggiornare `Core/WORKFLOW.md` a v2.4.0, verifica prima con il maintainer se il vecchio flusso `Output/raw/` resta valido come percorso legacy o va rimosso. Registrato anche in `Documentation/OperationalManual/Validation/CONSISTENCY_CHECK.md`.

Per il flusso operativo corrente (v2.4.0), questo capitolo segue `Build/Pipeline.md § v2.4.0 — CMS Pipeline` come riferimento primario.

## 2. La pipeline a 8 fasi (v2.4.0)

```
Phase 0  Project Setup        PROJECT.yaml + references
Phase 1  Reference Models     Photography & source art
Phase 2  Knowledge Load       GlossaryIT, EditorialStyle, Policy
Phase 2a Text Engine          AI genera content.yaml
Phase 2b Content QA           Tests/ContentValidation.md
Phase 2c Text QA              Tests/TextValidation.md
Phase 2d Approved Assets      ApprovedAssets/Text/P{NNN}/ sigillato
Phase 3  Render Engine        Legge content.yaml → genera render
Phase 4  Image QA             Tests/AssetsValidation.md
Phase 4a Page QA              Tests/LayoutValidation.md
Phase 5  PDF Generation       Screen + print + archive
Phase 6  Approved Manual      Assets/ApprovedManual/
Phase 7  Release              Tag + CHANGELOG + index.yaml
```

Ogni fase ha un attore responsabile, input, output e criteri di uscita definiti in `Build/Pipeline.md`. Punti operativi chiave per un manutentore:

- **Fase 0 (Project Setup):** criterio di uscita = `PROJECT.yaml` passa la validazione schema di `Config/quality.yaml`. Errori comuni: placeholder lasciati nei campi obbligatori, `modelSlug` con spazi invece di trattini, codici vernice inesistenti (verificare contro `Knowledge/Paints.md`).
- **Fase 2a (Text Engine, v2.4.0):** cambio rispetto a v2.3.0 — l'output primario è ora `content.yaml`, non `text.md`. `text.md` viene generato automaticamente come copia derivata per revisione umana.
- **Fase 2b/2c (QA testuale, bloccanti):** una pagina non può avanzare alla Fase 3 finché entrambe le suite non passano. Questo è G08 (Capitolo 03) applicato operativamente.
- **Fase 2d (Approved Assets Sealing, v2.4.0):** imposta `metadata.yaml → approved: true` e opzionalmente `locked: true`, aggiorna `ApprovedAssets/index.yaml`, incrementa `metadata.yaml → revision`, registra la modifica in `changelog.md`.
- **Fase 3 (Render Engine, v2.4.0):** cambio critico rispetto a v2.3.0 — il Render Engine legge `content.yaml` come fonte primaria, `text.md` solo come fallback con log di errore, e **mai** `PROJECT.yaml` direttamente. Questo è G03 applicato: *"The Render Engine reads content.yaml only — never text.md directly"* diventa, nel dettaglio operativo, una gerarchia a tre livelli con `PROJECT.yaml` esplicitamente escluso.
- **Fase 7 (Release):** oltre al tag Git e all'aggiornamento di `CHANGELOG.md`, la v2.4.0 aggiunge l'aggiornamento di `ApprovedAssets/index.yaml → manuals` e il cambio di stato di ogni pagina a `released` in `metadata.yaml`.

## 3. Come la pipeline si allinea al ciclo di vita del manuale

`Core/MANUAL_SYSTEM.md § 2` definisce 4 stati per un manuale nel suo complesso, distinti dalle 8 fasi della pipeline (che operano a grana più fine, spesso per-pagina):

| Stato | Condizione | Chi può avanzare |
|-------|------------|---------------------|
| **Draft** | `PROJECT.yaml` creato, almeno una pagina generata, QA non completa | Qualunque contributor |
| **Review** | Tutte le 10 pagine generate, self-review contro `Core/QA_SYSTEM.md` completata, fallimenti documentati in `Notes/qa_log.md` | Il contributor originale, completando la self-QA |
| **QA Pass** | Tutti i 110 item QA restituiscono PASS, `qa_log.md` completo, PDF esportato in entrambe le varianti | Un secondo contributor o il maintainer del progetto — **non** il contributor originale |
| **Approved** | File spostati in `Assets/ApprovedManual/{ModelName}/`, PDF presente, entry aggiunta a `Assets/ApprovedManual/README.md` | Solo il maintainer del progetto |

Il vincolo "QA Pass" richiede un revisore diverso dal contributor originale — è lo stesso principio del punto 4.7 in `Core/WORKFLOW.md § Phase 4`: *"Only a project maintainer can grant Approved status. Self-approval is not permitted."*

## 4. Mappatura fase pipeline → stato manuale

```
Phase 0–2d (Text Engine + QA testuale)  ──┐
Phase 3 (Render)                          ├──→  Draft
Phase 4–4a (Image/Page QA)                │
                                           ▼
Self-review completa, qa_log.md scritto  ──→  Review
                                           │
Tutti i 110 item QA_SYSTEM.md PASS        ▼
(verificato da un secondo contributor)   ──→  QA Pass
                                           │
Phase 5 (PDF) + Phase 6 (Approved Manual) ▼
Maintainer countersigna                  ──→  Approved
                                           │
Phase 7 (Release)                         ▼
                                          Pubblicato (fuori perimetro SDK)
```

`Core/MANUAL_SYSTEM.md § 8` chiarisce che la pubblicazione (rendere il PDF disponibile pubblicamente) non è gestita dallo SDK: *"Publication is not managed by the SDK — it is managed by the project that uses the SDK. The SDK's role ends at the Approved state."*

## 5. Decision flowchart operativo

`Core/WORKFLOW.md § Quick Reference Decision Flowchart` fornisce una sequenza di controlli binari utile come checklist rapida:

```
PROJECT.yaml completo? ── NO ──→ completa i campi obbligatori
  │ SÌ
Tutti i render approvati? ── NO ──→ rigenera i render falliti
  │ SÌ
Tutte le 10 pagine generate? ── NO ──→ genera le pagine mancanti
  │ SÌ
Tutti i 110 item QA passano? ── NO ──→ correggi, ri-esegui QA
  │ SÌ
PDF esportato (entrambe le varianti)? ── NO ──→ esporta i PDF
  │ SÌ
File in ApprovedManual/? ── NO ──→ sposta i file
  │ SÌ
Maintainer ha approvato? ── NO ──→ richiedi revisione
  │ SÌ
FINE — Manuale pubblicato
```

Se 5 o più item QA falliscono in un'iterazione, `Core/WORKFLOW.md § Phase 3` raccomanda di ri-eseguire l'intera checklist dopo le correzioni, non solo gli item falliti: le correzioni introducono a volte nuovi fallimenti.

## Vedi anche

- Capitolo 04 — Bootstrap (LOAD sequence che precede la Fase 0)
- Capitolo 06 — ProjectYaml (Fase 0 in dettaglio)
- Capitolo 07 — TextEngine (Fasi 2, 2a)
- Capitolo 09 — ApprovedAssets (Fase 2d, ciclo di vita pagina)
- Capitolo 10 — RenderEngine (Fase 3)
- Capitolo 11 — QA (Fasi 2b, 2c, 4, 4a)
- Capitolo 12 — PDF (Fase 5)
- Capitolo 15 — Versioning (Fase 7)
