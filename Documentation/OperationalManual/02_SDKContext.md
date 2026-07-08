# SDKContext

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| SDK Context | `SDK_CONTEXT.yaml` | Identity card machine-readable — Source of Truth di questo capitolo |
| Release Info | `ReleaseInfo.yaml` | Metadata di release machine-readable |
| SDK Config | `Config/sdk.yaml` | Parametri runtime globali |
| Version | `VERSION` | Numero di versione corrente in testo semplice |

## 1. Perché SDK_CONTEXT.yaml esiste

`SDK_CONTEXT.yaml` è il primo file che qualunque modello AI deve leggere (`bootstrap.official_entrypoint` punta a `AI_ENTRYPOINT.md`, ma `load_order.sequence` colloca `SDK_CONTEXT.yaml` al passo 1, subito dopo). È la carta d'identità dello SDK in formato interrogabile a macchina: conferma quale versione stai usando, qual è la pipeline, qual è la gerarchia di source of truth e in quale ordine caricare il resto del framework.

A differenza di `README.md` o `BOOTSTRAP.md`, che sono scritti per essere letti da un umano, `SDK_CONTEXT.yaml` è pensato per essere interrogato in modo affidabile: ogni chiave ha un solo valore atteso, senza prosa da interpretare.

## 2. Sezione per sezione

### `sdk`
Nome, versione (`2.4.0`), codename (`CMS`), maturità (`beta`), stato (`active`), lingua editoriale (`it`), licenza (Apache 2.0). Un manutentore verifica qui la versione corrente prima di qualunque altra operazione.

### `repository`
URL del repository, branch di default, release corrente. Usato dal Capitolo 16 (GitHubWorkflow) per i link di contribuzione.

### `compatibility`
Dichiara compatibilità con ChatGPT, Claude e modelli futuri per l'intera pipeline; Gemini è compatibile solo per la Fase 4 (generazione di una singola illustrazione — vedi `UAT/UAT-002.md`, `UAT/UAT-004.md`), non verificato per Fase 1-3. Nota esplicita: "All PromptEngine/ prompts are model-agnostic. No model-specific syntax is used." Se in futuro un prompt introducesse sintassi specifica di un modello, questa sezione andrebbe aggiornata e la nota rimossa o corretta.

### `pipeline`
La sequenza `text_engine → qa_engine → render_engine → pdf_builder`, con input, output e documento spec per ciascuna fase. Questa è la versione compatta della pipeline; il dettaglio completo a 8 fasi è in `Build/Pipeline.md` (vedi Capitolo 05).

### `architecture`
Principi strutturali: modulare, versionato, editor-first, model-agnostic, additive-only. La chiave `principles` elenca in prosa i vincoli non negoziabili, incluso "Page IDs P001–P010 and Component IDs C001–C015 are permanent and never change" — lo stesso vincolo espresso come Golden Rule G07 in `AI_ENTRYPOINT.md` (Capitolo 03).

### `source_of_truth`
La stessa gerarchia `Core/ > content.yaml > PROJECT.yaml > prompt defaults` descritta nel Capitolo 01 § 4, qui in forma machine-readable.

### `load_order`
La sequenza a 13 passi che ogni modello AI deve seguire prima di generare contenuto. Riassunta qui, dettagliata in `Docs/LOAD_ORDER.md` con motivazione per ciascun passo (Capitolo 04).

### `roadmap`
`current_version`, `next_version`, e `next_planned` — l'elenco di funzionalità pianificate per la prossima release (`Compiler/`, Prompt Orchestrator, Icon Library, tutorial, automazione release). Ogni voce qui deve restare marcata come pianificata finché non compare in `CHANGELOG.md` come rilasciata (vedi `Documentation/OperationalManual/Validation/CONSISTENCY_CHECK.md`, controlli C2–C4).

### `golden_project`
Punta a `Projects/Proto_Emperor/` come riferimento strutturale ufficiale. Vedi Capitolo 13 — GoldenProjects.

### `documentation`
Percentuale di completamento stimata per area (`core_specs: complete`, `tutorials: planned_v2.5.0`, ecc.). Utile come termometro rapido, ma non sostituisce `Documentation/OperationalManual/Validation/DOCUMENTATION_STATUS.yaml`, che è la fonte più granulare per lo stato di *questo* manuale specifico.

### `bootstrap`
Elenco dei documenti di bootstrap con il loro percorso (`official_entrypoint`, `entry_point`, `context_file`, `manifest`, `status`, `load_order`, `ai_prompt`, `project_guide`, `release_info`), con la nota esplicita: *"AI models must read AI_ENTRYPOINT.md FIRST — it contains the Bootstrap Contract"*.

## 3. Come restano sincronizzati VERSION, ReleaseInfo.yaml e Config/sdk.yaml

Quattro file portano il numero di versione dello SDK e devono sempre concordare:

| File | Cosa contiene oltre al numero di versione |
|------|--------------------------------------------|
| `VERSION` | Solo il numero, in testo semplice (`2.4.0`) — usato da tooling che non vuole fare parsing YAML |
| `SDK_CONTEXT.yaml` | Versione + tutto il contesto operativo (sezioni sopra) |
| `ReleaseInfo.yaml` | Versione + `release_date`, `release_type`, `codename`, `breaking_changes`, `migration_notes`, `new_in_this_version`, `compatibility`, `previous_releases`, `next_release` |
| `Config/sdk.yaml` | Versione + parametri runtime (schema di `PROJECT.yaml`, registro pagine/componenti, pattern di naming) |

`ReleaseInfo.yaml` è il più dettagliato sul **cosa è cambiato**: ogni release elenca `new_in_this_version` e, se applicabile, `breaking_changes` con `migration_notes` che puntano a un file in `Docs/migration/`. `Config/sdk.yaml`, al contrario, non descrive la release — descrive lo stato *corrente* delle regole (es. `next_available_component_id: "C016"`) e non deve mai contraddire `Core/COMPONENT_SYSTEM.md` o `Core/PAGE_SYSTEM.md`, di cui è l'implementazione machine-readable (vedi `Config/README.md § How Config files relate to Core documents`).

> ⚠️ **Warning:** se aggiorni la versione in uno di questi quattro file senza aggiornare gli altri tre, il framework entra in uno stato inconsistente rilevabile solo manualmente (non esiste ancora un test automatico — `Tests/FrameworkIntegrity.md` è eseguito a mano). Aggiornali sempre insieme, nello stesso commit.

## 4. Uso pratico per il manutentore

Quando devi rispondere a "che versione dello SDK sto guardando, e cosa posso fare con essa", `SDK_CONTEXT.yaml` è il primo file da aprire, non `README.md`: è progettato per essere corretto anche quando la prosa di `README.md` non è stata ancora aggiornata dopo una release (anche se, nella pratica, i due dovrebbero sempre concordare — verificalo con `Documentation/OperationalManual/Validation/CONSISTENCY_CHECK.md` controllo C1).

Quando invece devi rispondere a "cosa è cambiato tra due versioni", usa `ReleaseInfo.yaml § previous_releases` insieme a `CHANGELOG.md` (Capitolo 15 — Versioning tratta questo in dettaglio).

## Vedi anche

- Capitolo 01 — Introduction (gerarchia Source of Truth)
- Capitolo 03 — AIEntryPoint
- Capitolo 04 — Bootstrap (load_order dettagliato)
- Capitolo 13 — GoldenProjects
- Capitolo 14 — Roadmap
- Capitolo 15 — Versioning
