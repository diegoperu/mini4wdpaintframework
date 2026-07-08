# Bootstrap

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Bootstrap | `BOOTSTRAP.md` | Source of Truth diretta — guida operativa AI |
| AI Entry Point | `AI_ENTRYPOINT.md` | Contratto di bootstrap (Capitolo 03) |
| SDK Context | `SDK_CONTEXT.yaml` | Identity card (Capitolo 02) |
| Load Order | `Docs/LOAD_ORDER.md` | Sequenza di caricamento con motivazione |
| AI Bootstrap Prompt | `Docs/AI_BOOTSTRAP_PROMPT.md` | Prompt pronti all'uso (A–F) |
| Docs README | `Docs/README.md` | Ruolo della cartella `Docs/` |
| AI Operating Rules | `Core/AI_OPERATING_RULES.md` | 100 regole comportamentali |
| Language Policy | `Config/LANGUAGE_POLICY.yaml` | Politica italiano-only |
| Project Bootstrap | `Projects/PROJECT_BOOTSTRAP.md` | Guida nuovo progetto |

## 1. Rapporto tra AI_ENTRYPOINT.md e BOOTSTRAP.md

I due documenti non sono ridondanti. `AI_ENTRYPOINT.md` (Capitolo 03) è il **contratto**: breve, normativo, contiene il Bootstrap Contract YAML e le Golden Rules. `BOOTSTRAP.md` è la **guida operativa** che espande quel contratto in dettaglio pratico — apre esplicitamente con l'avviso *"AI models: read AI_ENTRYPOINT.md before this document"*.

`BOOTSTRAP.md` aggiunge cose che `AI_ENTRYPOINT.md` non contiene:

- Una tabella "What this SDK is NOT" che disambigua il framework da sistemi simili (non è un plugin Stable Diffusion, non è un tool di modellazione 3D, non è una pipeline automatica)
- I 10 "Core Rules (Non-Negotiable)" — una riformulazione operativa delle Golden Rules, orientata all'azione immediata
- Tre percorsi di avvio (Path A: da GitHub, Path B: da ZIP, Path C: ricevendo solo `BOOTSTRAP.md` + `SDK_CONTEXT.yaml`)
- Tabelle complete di pagine (P001–P010) e componenti (C001–C015) con la regola chiave di ciascuno
- Una tabella "Common AI Errors to Avoid" con 8 errori tipici, la loro conseguenza e come prevenirli

## 2. La sequenza di caricamento (LOAD sequence)

`Docs/LOAD_ORDER.md` è il documento normativo per l'ordine di lettura — non improvvisare l'ordine, ogni passo dipende da quello precedente. La sequenza completa, 14 passi (Step 0, `AI_ENTRYPOINT.md`, seguito dai 13 passi di `SDK_CONTEXT.yaml → load_order.sequence`):

| # | Documento | Perché in questa posizione |
|---|-----------|------------------------------|
| 0 | `AI_ENTRYPOINT.md` | Stabilisce il Bootstrap Contract che governa l'interpretazione di tutto il resto |
| 1 | `SDK_CONTEXT.yaml` | Identità e contesto operativo dello SDK |
| 2 | `BOOTSTRAP.md` | Guida operativa dettagliata |
| 3 | `Core/AI_OPERATING_RULES.md` | Vincoli comportamentali che governano come interpretare i documenti successivi |
| 4 | `Config/LANGUAGE_POLICY.yaml` | Deve essere attivo prima che venga generato qualsiasi testo |
| 5 | `Core/TEXT_ENGINE.md` | Definisce il formato di output — necessario prima di generare `content.yaml` |
| 6 | `Core/DESIGN_LANGUAGE.md` | Grammatica visiva — necessaria prima del rendering |
| 7 | `Core/STYLE_GUIDE.md` | Palette, tipografia, griglia |
| 8 | `Core/COMPONENT_SYSTEM.md` | Deve precedere `PAGE_SYSTEM.md` (le pagine referenziano i componenti) |
| 9 | `Core/PAGE_SYSTEM.md` | Specifiche per pagina |
| 10 | `PromptEngine/{page}.md` | Solo il prompt della pagina corrente — non precaricare tutti e 10 |
| 11 | `Projects/{ModelName}/PROJECT.yaml` | Caricato per ultimo tra le specifiche: sovrascrive i default di tutti i documenti precedenti |
| 12 | `ApprovedAssets/Text/{page}/` | Contenuto già sigillato per la pagina corrente, se esiste |
| 13 | Immagini di riferimento | Fotografia del modello fisico |

Se il contesto disponibile è limitato, `Docs/LOAD_ORDER.md § Abbreviated LOAD` definisce un ordine minimo vitale: passi 0–5 più il prompt della pagina corrente e `PROJECT.yaml` — i passi 6–9 (linguaggio visivo) possono essere rimandati se il compito corrente è solo generazione testuale.

## 3. Le 100 AI Operating Rules

`Core/AI_OPERATING_RULES.md` (Document ID `CORE-AIR-001`) è il documento che rende operative le Golden Rules del Capitolo 03. La sua apertura è categorica: *"These rules are constraints, not suggestions. An AI-generated output that violates any rule in this document is considered non-compliant and must be regenerated."*

Le regole sono organizzate in 9 categorie (Regole 001–058, aggiunte in v2.2.0):

| Categoria | Intervallo | Esempio concreto |
|-----------|------------|-------------------|
| `[DATA]` | RULE-001–010 | RULE-001: mai inventare codici vernice — solo da `PROJECT.yaml § paintScheme.colors[].paintCode` |
| `[DESIGN]` | RULE-011–020 | RULE-016: nessun gradiente come sfondo — solo colori solidi |
| `[LAYOUT]` | RULE-021–028 | RULE-022: mai riordinare le pagine — P001–P010 è fisso |
| `[COLOR]` | RULE-029–035 | RULE-030: `VioletPrimary` deve essere esattamente `#5B2D8E`, mai approssimato |
| `[CONTENT]` | RULE-036–044 | RULE-040: nessun testo placeholder ("Lorem ipsum", "[TEXT HERE]") nell'output finale |
| `[RENDER]` | RULE-045–050 | RULE-045: sfondo dei render sempre bianco puro, nessuna eccezione |
| `[COMPONENT]` | RULE-051–053 | RULE-053: ogni pagina deve avere C001 e C002 |
| `[TOKEN]` | RULE-054–055 | RULE-054: nessun valore hardcoded — sempre riferimento a Design Token |
| `[OUTPUT]` | RULE-056–058 | RULE-057: tutti i marcatori `TODO:` devono essere risolti prima della QA |

A queste si aggiunge, dalla v2.3.0, la categoria `[TEXT]` (RULE-059–100), interamente dedicata al rendering testuale in italiano: divieto assoluto di script giapponesi anche come decorazione (RULE-060–061), formattazione italiana dei numeri — separatore decimale, interi/percentuali/dimensioni (RULE-070, RULE-085), uso delle virgolette basse «…» (RULE-071), e il principio cardine RULE-072: *"The Render Engine never generates text — it only places text."*

Dalla v2.5.5 si aggiunge la categoria `[SAFETY]` (RULE-101–102), sulla sicurezza meccanica dei contenuti generati: RULE-101 vieta di istruire la verniciatura di parti mobili/funzionali (ingranaggi, meccanica interna del motore), RULE-102 impone di mascherare la superficie di contatto del cerchio, mai la gomma stessa (removibile/intercambiabile). Vedi `Knowledge/MechanicalSafety.md`.

Ogni categoria bloccante è indicata nella tabella "Compliance Summary" del documento — per `[DATA]`, `[DESIGN]`, `[LAYOUT]`, `[COLOR]` tutte le regole sono bloccanti; per le altre categorie solo un sottoinsieme lo è esplicitamente.

## 4. Le 102 rules riassunte non sostituiscono la lettura completa

Questo capitolo riassume categorie ed esempi, non riproduce le 102 regole verbatim: farlo violerebbe lo stesso principio di `Core/DOCUMENTATION_STYLE.md § 12` ("Do not pad" — ogni frase deve guadagnarsi il proprio posto) applicato a un documento che già esiste ed è già la fonte primaria. Per la lista completa e vincolante, apri `Core/AI_OPERATING_RULES.md` direttamente.

## 5. Come un nuovo progetto fa bootstrap

`Docs/AI_BOOTSTRAP_PROMPT.md` fornisce sei prompt pronti all'uso (Prompt A–F), tutti scritti in italiano (poiché l'output atteso è editoriale in italiano) e senza sintassi specifica di alcun modello:

| Prompt | Uso |
|--------|-----|
| A — Full Session Bootstrap | Avvio di una sessione completa da zero; allega 11 file/risorse in ordine |
| B — Single Page Generation | Genera una pagina specifica, assumendo che il contesto framework sia già caricato |
| C — QA Validation | Esegue Content QA e Text QA su un `content.yaml` |
| D — Render Engine | Genera l'illustrazione da un `content.yaml` bloccato |
| E — Minimal Bootstrap | Per quando il modello riceve solo lo ZIP dello SDK e deve auto-orientarsi |
| F — Session Continuity | Riprende una sessione già avviata, riportando lo stato pagine completate/rimanenti |

`Projects/PROJECT_BOOTSTRAP.md` guida invece l'**autore umano** attraverso l'intero processo di creazione di un nuovo progetto, dai prerequisiti (nome ufficiale Tamiya, codici vernice, fotografia di riferimento) fino al Passo 8 (Release), passando per la creazione della cartella progetto, la compilazione di `PROJECT.yaml`, e il ciclo per-pagina Text Engine → QA → Seal → Render descritto in dettaglio nel Capitolo 05.

## Vedi anche

- Capitolo 01 — Introduction
- Capitolo 02 — SDKContext
- Capitolo 03 — AIEntryPoint (Bootstrap Contract, Golden Rules)
- Capitolo 05 — Workflow (pipeline completa)
- Capitolo 06 — ProjectYaml
- Capitolo 07 — TextEngine (regole `[TEXT]` in dettaglio)
