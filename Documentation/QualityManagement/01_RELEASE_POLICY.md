# Release Policy

**Mini4WD Manual SDK** · Quality Management System · Documento 01

| Campo | Valore |
|-------|--------|
| Scopo | Definire quali modifiche possono entrare in ciascun tipo di release |
| Destinatario | Maintainer, Developer |
| Source of Truth | Questo documento (per la classificazione delle release); `CHANGELOG.md` (per lo storico) |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## 1. Principio

Il framework è **STABLE**. Nessuna modifica entra nel repository "a sentimento": ogni release deve essere giustificata da almeno una delle seguenti evidenze documentate:

- bug confermato (`05_BUG_REPORT_TEMPLATE.md`)
- User Acceptance Test (`04_UAT_TEMPLATE.md`)
- Golden Project non realizzabile (`10_GOLDEN_PROJECTS.md`)
- cambiamenti nei modelli AI (nuove versioni di ChatGPT/Claude/Gemini che alterano il comportamento del framework)
- nuovi requisiti funzionali approvati (`06_FEATURE_REQUEST_TEMPLATE.md` → `11_ROADMAP.md` stato APPROVATO)

Ogni modifica deve nascere da una Change Proposal (`15_CHANGE_PROPOSAL_TEMPLATE.md`) e ogni release deve rispettare i criteri di `02_RELEASE_CRITERIA.md`.

Il versionamento segue [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html): `MAJOR.MINOR.PATCH`.

---

## 2. Patch Release (x.y.Z)

**Cosa può contenere:**

- correzione di bug confermati che NON cambiano il comportamento atteso
- correzioni di documentazione (refusi, riferimenti rotti, incoerenze tra documenti)
- chiarimenti che rendono esplicito un comportamento già esistente
- aggiornamento di esempi errati
- estensione di whitelist/eccezioni già previste (es. nuovi codici colore Tamiya in `Config/LANGUAGE_POLICY.yaml §exceptions`)

**Cosa NON può contenere:**

- nuovi componenti, nuove pagine, nuovi prompt
- modifiche alla pipeline
- modifiche al comportamento del Prompt Engine, Text Engine, Rendering Engine
- rimozione di funzionalità
- modifiche che richiedono migrazione dei progetti esistenti

**Compatibilità:** totale. Un progetto avviato con v2.4.0 deve completarsi identico con v2.4.1.

**Esempi pratici:**

- ✅ v2.4.1: falsi positivi linguistici su "Chrome Silver" → estensione whitelist TX-001-K (UAT-001, Errore 2)
- ✅ Correzione di un path errato in `Docs/LOAD_ORDER.md`
- ❌ Aggiungere un nuovo componente C0xx → è Minor
- ❌ Cambiare l'ordine delle fasi della pipeline → è Minor (o Major se rompe progetti in corso)

---

## 3. Minor Release (x.Y.0)

**Cosa può contenere:**

- nuovi componenti, nuove tipologie di pagina
- nuove funzionalità retrocompatibili
- nuovi prompt o varianti di prompt
- modifiche alla pipeline che NON invalidano i progetti esistenti
- nuovi documenti strutturali (guide, template, sistemi come questo QMS)
- deprecazioni (la funzionalità resta, marcata LEGACY)
- tutto ciò che è ammesso in una Patch

**Cosa NON può contenere:**

- rimozione di funzionalità o documenti su cui i progetti esistenti dipendono
- modifiche incompatibili a `PROJECT.yaml`, `content.yaml` o altri schemi
- cambio della source-of-truth hierarchy

**Compatibilità:** retrocompatibile. I progetti esistenti continuano a funzionare; possono ignorare le novità.

**Esempi pratici:**

- ✅ v2.4.1 → v2.5.0: introduzione di Compiler/ e Prompt Orchestrator (già in roadmap)
- ✅ Nuovo componente "C0xx Icon Legend" richiesto da 3 operatori via Feature Request
- ✅ Marcare `text.approved_text_dir` come LEGACY mantenendo la compatibilità v2.3.0
- ❌ Eliminare `ApprovedText/` → è Major

---

## 4. Major Release (X.0.0)

**Cosa può contenere:**

- breaking changes: rimozione di funzionalità, cambi di schema incompatibili
- ristrutturazione della pipeline
- cambio della source-of-truth hierarchy
- riorganizzazione delle cartelle del repository
- tutto ciò che è ammesso in Minor e Patch

**Obblighi aggiuntivi:**

- Migration Report obbligatorio (es. `MigrationReport_v2.4.md`)
- almeno 1 Golden Project completato con la nuova versione PRIMA del rilascio
- Decision Log aggiornato (`08_DECISION_LOG.md`) per ogni breaking change
- periodo di annuncio: la breaking change deve comparire in `11_ROADMAP.md` (stato APPROVATO) almeno una Minor prima

**Compatibilità:** non garantita. I progetti in corso devono essere migrati seguendo il Migration Report.

**Esempi pratici:**

- ✅ Rimozione definitiva di `ApprovedText/` legacy con migrazione a `content.yaml`
- ✅ Ristrutturazione di `Projects/` con nuovo schema `PROJECT.yaml` v3
- ❌ Un semplice nuovo componente non giustifica mai una Major

---

## 5. Tabella riassuntiva

| Modifica | Patch | Minor | Major |
|----------|:-----:|:-----:|:-----:|
| Fix bug confermato (comportamento invariato) | ✅ | ✅ | ✅ |
| Correzione documentazione | ✅ | ✅ | ✅ |
| Estensione whitelist/eccezioni | ✅ | ✅ | ✅ |
| Nuovo componente / pagina | ❌ | ✅ | ✅ |
| Nuova funzionalità retrocompatibile | ❌ | ✅ | ✅ |
| Modifica pipeline retrocompatibile | ❌ | ✅ | ✅ |
| Deprecazione (LEGACY) | ❌ | ✅ | ✅ |
| Rimozione funzionalità | ❌ | ❌ | ✅ |
| Cambio schema incompatibile | ❌ | ❌ | ✅ |
| Cambio source-of-truth hierarchy | ❌ | ❌ | ✅ |

---

## 6. Documenti collegati

- `02_RELEASE_CRITERIA.md` — quando una release è consentita
- `15_CHANGE_PROPOSAL_TEMPLATE.md` — come proporre una modifica
- `17_VERSION_HISTORY.md` — registro storico delle versioni
- `CHANGELOG.md` (root) — dettaglio delle modifiche per versione
