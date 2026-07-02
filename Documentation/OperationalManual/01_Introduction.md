# Introduction

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| README | `README.md` | Panoramica per contributor umani |
| AI Entry Point | `AI_ENTRYPOINT.md` | Contratto di bootstrap per modelli AI |
| SDK Context | `SDK_CONTEXT.yaml` | Identity card machine-readable |
| Manifest | `MANIFEST.yaml` | Descrittore completo (componenti, token, pagine) |
| Repository Manifest | `RepositoryManifest.yaml` | Mappa completa di file e dipendenze |
| Documentation Style | `Core/DOCUMENTATION_STYLE.md` | Regole di scrittura per la documentazione SDK |
| Status | `STATUS.md` | Stato implementazione, roadmap, TODO |
| Config README | `Config/README.md` | Ruolo della cartella `Config/` |

Questo capitolo introduce il Mini4WD Manual SDK, definisce a chi si rivolge questo Manuale Operativo e spiega come orientarsi nei 20 capitoli che seguono.

## 1. Cos'è il Mini4WD Manual SDK

Il Mini4WD Manual SDK è un framework editoriale open-source che permette a qualsiasi modello AI (ChatGPT, Claude, Gemini o futuri modelli) di generare manuali di verniciatura illustrati e professionali per modellini Tamiya Mini4WD, mantenendo standard editoriali e grafici coerenti su centinaia di progetti diversi.

Non è un sistema generativo libero: è **specification-first**. Ogni regola di design, ogni regola editoriale, ogni componente e ogni fase del workflow è già definita nei documenti autoritativi del framework. Il ruolo dell'AI (o del contributor umano) è **eseguire** queste specifiche, non inventarle o reinterpretarle.

La versione corrente è **2.4.0** (codename "CMS"). Per lo stato dettagliato di ogni release, vedi Capitolo 02 — SDKContext.

## 2. A chi si rivolge questo manuale

Questo Manuale Operativo si rivolge a chi deve **mantenere** il framework nel tempo, non a chi genera un singolo manuale di verniciatura. Le due attività sono distinte:

- **Generare un manuale Mini4WD** (un progetto in `Projects/{ModelName}/`) è già documentato in `AI_ENTRYPOINT.md`, `BOOTSTRAP.md` e `Projects/PROJECT_BOOTSTRAP.md`.
- **Mantenere lo SDK stesso** — capire come i 105+ documenti del framework si relazionano tra loro, cosa succede quando uno di essi cambia, come verificare che tutto resti coerente — è lo scopo di questo manuale.

Il lettore previsto è un **manutentore o contributor**, umano o AI, che deve orientarsi nell'intero repository, non solo in una sua parte. Se stai generando un manuale per un modello specifico, leggi invece `AI_ENTRYPOINT.md` prima di qualunque altra cosa: quel documento resta l'entry point ufficiale e non viene sostituito da questo.

## 3. Struttura del repository a colpo d'occhio

`RepositoryManifest.yaml` è la mappa machine-readable completa del repository: elenca ogni file, il suo ruolo, e le sue dipendenze (`depends_on`). Le aree principali sono:

| Cartella | Ruolo | Autorità |
|----------|-------|----------|
| `Core/` | Specifiche autoritative (design, testo, QA, PDF, workflow) | Massima — vince su ogni altra cartella |
| `Config/` | Parametri machine-readable che implementano i valori di `Core/` | Implementa, non ridefinisce |
| `PromptEngine/` | Prompt AI per-pagina, model-agnostic | Esecutivo |
| `Templates/` | File di partenza per nuovi progetti | Punto di partenza, non normativo |
| `Projects/` | Un sottodirectory per ogni modello Mini4WD | Dati di progetto |
| `Assets/` | Design system, fotografia di riferimento, output approvati | Risorse |
| `ApprovedAssets/` | Livello CMS — moduli di contenuto sigillati per pagina | Fonte primaria del contenuto pubblicato |
| `Build/` | Documentazione della pipeline di produzione | Operativo |
| `Tests/` | Suite di validazione QA | Verifica |
| `Knowledge/` | Base di conoscenza tecnica ed editoriale | Supporto |
| `Docs/` | Documentazione supplementare e guide | Derivato da `Core/` |

Per il dettaglio completo file-per-file, non duplicarlo qui: consulta `RepositoryManifest.yaml` direttamente — è la fonte primaria e viene aggiornato a ogni release.

## 4. Gerarchia della Source of Truth

Quando due documenti sembrano dire cose diverse, questa gerarchia — definita in `AI_ENTRYPOINT.md § Source of Truth` e ribadita in `SDK_CONTEXT.yaml § source_of_truth` — risolve il conflitto:

```
Core/  >  content.yaml  >  PROJECT.yaml  >  prompt defaults
```

- **`Core/`** è la specifica assoluta. Nessun documento, nessuna istruzione utente, nessun default del modello AI la sovrascrive.
- **`content.yaml`** (in `ApprovedAssets/Text/P00x/`) è la fonte primaria per il contenuto di ogni singola pagina, una volta generato.
- **`PROJECT.yaml`** sovrascrive i default dei prompt per i valori specifici del progetto (nome modello, colori, ecc.).
- I **default nei prompt** (`PromptEngine/*.md`) si applicano solo quando nessuno dei livelli superiori specifica un valore.

Questa gerarchia vale per ogni domanda del tipo "qual è il valore corretto?" in qualunque punto del framework, inclusa la scrittura di questo stesso Manuale Operativo: se un capitolo qui contraddice `Core/`, `Core/` ha ragione e il capitolo va corretto (vedi `Documentation/OperationalManual/Validation/CONSISTENCY_CHECK.md`).

## 5. Come navigare questo manuale

I 20 capitoli seguono l'ordine con cui un manutentore incontrerebbe le aree del framework, dal bootstrap iniziale fino alla manutenzione a lungo termine:

| # | Capitolo | Cosa copre |
|---|----------|------------|
| 01 | Introduction | Questo capitolo |
| 02 | SDKContext | `SDK_CONTEXT.yaml` come identity card |
| 03 | AIEntryPoint | `AI_ENTRYPOINT.md`, il Bootstrap Contract, le Golden Rules |
| 04 | Bootstrap | Sequenza di avvio, LOAD order, le 100 regole operative AI |
| 05 | Workflow | Il workflow end-to-end e la pipeline a 8 fasi |
| 06 | ProjectYaml | Come configurare un nuovo progetto |
| 07 | TextEngine | Generazione del testo editoriale, `content.yaml` |
| 08 | Assets | Design system, token, componenti, pagine |
| 09 | ApprovedAssets | Il livello CMS e il ciclo di vita delle pagine |
| 10 | RenderEngine | Generazione delle illustrazioni |
| 11 | QA | Le 9 suite di test e la checklist a 110 voci |
| 12 | PDF | Esportazione del manuale finale |
| 13 | GoldenProjects | Il progetto di riferimento Proto Emperor |
| 14 | Roadmap | Funzionalità pianificate e stato TODO |
| 15 | Versioning | SemVer, changelog, ADR |
| 16 | GitHubWorkflow | Come contribuire al repository |
| 17 | BestPractices | Pratiche raccomandate |
| 18 | Troubleshooting | Problemi comuni e soluzioni |
| 19 | FAQ | Domande frequenti |
| 20 | Glossary | Glossario tecnico IT/EN e terminologia approvata |

Ogni capitolo apre con una tabella "Documenti di riferimento" — gli stessi documenti sono catalogati per capitolo in `Documentation/OperationalManual/Validation/DOCUMENT_COVERAGE.md`. Se un documento del framework cambia, `Documentation/OperationalManual/Validation/CHANGE_IMPACT.md` indica esattamente quali capitoli rivedere.

> 📝 **Nota:** questo manuale documenta lo SDK, non un singolo progetto. Non contiene istruzioni di verniciatura — quelle vivono in `Knowledge/` e vengono editorializzate dal Text Engine (Capitolo 07) nei singoli `content.yaml` di progetto.

## Vedi anche

- Capitolo 02 — SDKContext
- Capitolo 03 — AIEntryPoint
- Capitolo 04 — Bootstrap
- Capitolo 15 — Versioning
- `Documentation/OperationalManual/Validation/DOCUMENT_COVERAGE.md`
