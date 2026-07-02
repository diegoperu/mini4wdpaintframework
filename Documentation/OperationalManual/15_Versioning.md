# Capitolo 15 — Versioning

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Version | `VERSION` | Source of Truth — numero di versione corrente in testo semplice |
| Changelog | `CHANGELOG.md` | Storico completo di tutte le versioni |
| Release Info | `ReleaseInfo.yaml` | Metadata di release machine-readable |
| Style Decisions | `STYLE_DECISIONS.md` | Architecture Decision Records (ADR) |
| Migration Report v2.4 | `MigrationReport_v2.4.md` | Guida di migrazione v2.3.0 → v2.4.0 |
| Migration v1→v2 | `Docs/migration/v1-to-v2.md` | Guida di migrazione v1.x → v2.x |
| Manual System | `Core/MANUAL_SYSTEM.md` (§7) | Versionamento indipendente per manuale |

---

## 1. Versionamento dell'SDK

L'SDK usa Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH), formalizzato in `ADR-010`:

- **MAJOR** — breaking change: qualsiasi modifica a Page ID, Component ID, nomi dei token, campi obbligatori di `PROJECT.yaml`, o formato di output PDF
- **MINOR** — aggiunte retrocompatibili: nuove pagine, nuovi componenti, nuovi token, nuova documentazione
- **PATCH** — correzioni retrocompatibili: correzioni di typo, chiarimenti, modifiche non strutturali

La versione corrente è in `VERSION` (testo semplice, oggi `2.4.0`) ed è riecheggiata in `README.md`. Ogni release è documentata in `CHANGELOG.md`. Le breaking change includono sempre istruzioni di migrazione in `Docs/migration/`.

---

## 2. Storico versioni (da CHANGELOG.md)

| Versione | Data | Codename | Tema |
|----------|------|----------|------|
| 1.0.0 | 2023-03-10 | — | Rilascio iniziale — template pagine base, style guide, licenza Apache 2.0 |
| 1.1.0 | 2023-06-20 | — | Pagine P07/P08, correzione margini US-Letter |
| 2.0.0 | 2023-09-01 | — | **Breaking:** Component ID `COMP_` → `C###`, `car_name` → `modelName`, Page ID `001` → `P001` |
| 2.1.0 | 2024-01-15 / 2026-06-30* | Foundation | Design Token system, `Core/QA_SYSTEM.md` (110 item), `Core/DEFINITION_OF_DONE.md`, pagina P009 |
| 2.2.0 | 2024-06-30 / 2026-06-30* | Pipeline | `Build/Pipeline.md`, `Config/`, `Tests/` (7→9 suite), `Core/AI_OPERATING_RULES.md` (58 regole iniziali), `Knowledge/`, `MANIFEST.yaml` |
| 2.3.0 | 2026-07-01 | Editorial | `Core/TEXT_ENGINE.md`, `Config/LANGUAGE_POLICY.yaml`, knowledge base editoriale italiana, regole 059–100 |
| 2.4.0 | 2026-07-01 | CMS | `ApprovedAssets/` (CMS layer), `content.yaml` come primary source of truth, ciclo di vita pagina |
| 2.5.0 | pianificata | — | Vedi Capitolo 14 — contenuto non ancora concordato tra le fonti SDK |

> ⚠️ **Warning — date incoerenti:** `CHANGELOG.md` riporta `[2.1.0] - 2024-01-15` e `[2.2.0] - 2024-06-30`, mentre `ReleaseInfo.yaml → previous_releases` riporta le stesse due versioni con data `2026-06-30` per entrambe. `2.3.0` e `2.4.0` sono coerenti fra le due fonti (`2026-07-01`). Le date 2024 in `CHANGELOG.md` per 2.1.0/2.2.0 sembrano essere le date "storiche" originali non aggiornate quando il progetto è stato ribattezzato con la cronologia 2026 usata da `ReleaseInfo.yaml` e `STATUS.md`. Usare `ReleaseInfo.yaml` come fonte primaria per le date recenti.

---

## 3. Versione SDK vs versione del manuale

Sono due numeri **indipendenti**, e la distinzione è facile da confondere per un nuovo contributor:

- `VERSION` (root del repository) — la versione dell'SDK stesso
- `manualVersion` (campo in `PROJECT.yaml`, per progetto) — la versione del singolo manuale prodotto

`Core/MANUAL_SYSTEM.md` §7 definisce il SemVer per `manualVersion`:

- **MAJOR** — cambio completo di schema colore (colori diversi, stile diverso)
- **MINOR** — pagine aggiuntive, aggiornamenti significativi ai render
- **PATCH** — correzioni di typo, fix di codici colore, aggiustamenti di layout

`sdkVersion` (altro campo di `PROJECT.yaml`) registra quale versione dell'SDK era disponibile al momento della creazione del manuale — non cambia quando l'SDK viene aggiornato. Quando l'SDK cambia versione MAJOR, i manuali esistenti **non vengono invalidati automaticamente**: continuano a riferire alla versione SDK sotto cui sono stati creati. La migrazione a un nuovo MAJOR dell'SDK è opzionale e documentata in `Docs/migration/`.

---

## 4. Architecture Decision Records (ADR)

Un ADR (Architecture Decision Record) documenta una decisione di design significativa: contesto, decisione, conseguenze. `STYLE_DECISIONS.md` è il registro completo — **prima di modificare qualsiasi specifica in `Core/`, occorre referenziare un ADR esistente o crearne uno nuovo**.

ADR notevoli per capire l'architettura attuale:

| ADR | Titolo | Versione | Perché conta |
|-----|--------|----------|----------------|
| ADR-003 | Page ID permanenti (P001–P010) | 2.0.0 | Gli ID non cambiano mai, anche se una pagina viene inserita logicamente "in mezzo" — l'ordine reale è deciso da `Templates/PDF_CONFIG.yaml`, non dagli ID |
| ADR-005 | Design Token per tutti i valori visivi | 2.1.0 | Nessun colore/dimensione va mai hardcoded — rinominare un token è un breaking change MAJOR |
| ADR-009 | Prompt AI-agnostici | 2.0.0 | Nessun prompt può nominare un modello AI specifico |
| ADR-015 | `MANIFEST.yaml` come identità SDK machine-readable | 2.2.0 | La versione in `MANIFEST.yaml` deve combaciare con `VERSION` (verificato da `Tests/FrameworkIntegrity.md` TEST-FW-005) |
| ADR-019 | `content.yaml` come primary source of truth | 2.4.0 | Sostituisce `text.md` come output primario del Text Engine |
| ADR-021 | Render Engine legge solo `content.yaml`, mai `PROJECT.yaml` | 2.4.0 | Chiude un bypass silenzioso della pipeline di validazione linguistica |

Un ADR "superato" non viene cancellato: il suo stato viene aggiornato e un nuovo ADR viene creato a riferirlo.

---

## 5. Guide di migrazione

| Guida | Copre | Breaking? |
|-------|-------|-----------|
| `Docs/migration/v1-to-v2.md` | v1.x → v2.0.0/v2.1.0: rinomina Component ID, campo `car_name`→`modelName`, formato Page ID | Sì — 3 breaking change |
| `MigrationReport_v2.4.md` | v2.3.0 → v2.4.0: introduzione `ApprovedAssets/`, `content.yaml` come formato primario | No — puramente additivo |

La migrazione v2.3.0→v2.4.0 è interamente opzionale: "No existing content is removed. No existing IDs change. v2.3.0 projects are fully compatible." I progetti v2.3.0 restano funzionanti senza modifiche; `Projects/{model}/ApprovedText/` resta supportato per retrocompatibilità.

Per la migrazione v1→v2 (breaking), la procedura prevede un audit con `grep` dei riferimenti agli ID vecchi, un find-and-replace guidato passo-passo, e una validazione finale che conferma zero occorrenze residue di `COMP_`, `car_name:`, o Page ID a 3 cifre senza prefisso `P`.

---

## Vedi anche

- Capitolo 02 — SDKContext (versione corrente e file di identità)
- Capitolo 14 — Roadmap (versione successiva pianificata)
- Capitolo 06 — ProjectYaml (campi `sdkVersion` e `manualVersion`)
- Capitolo 05 — Workflow (`Core/MANUAL_SYSTEM.md` come Source of Truth condivisa con questo capitolo)
