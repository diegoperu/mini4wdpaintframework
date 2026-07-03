# RUNTIMES.md — Runtime Supportati

**Mini4WD Manual SDK v2.5.0** · Documento operatore

> Un **Runtime** è l'ambiente in cui l'Operatore interagisce con l'AI.
> Ambienti diversi = procedure di caricamento diverse.
> Leggi questa pagina prima di iniziare: scegli il tuo runtime, poi vai alla guida dedicata.

---

## Cos'è un Runtime

Il Mini4WD Manual SDK funziona con qualsiasi AI che supporti l'elaborazione di documenti. Tuttavia, il modo in cui i file vengono forniti all'AI dipende dall'ambiente di esecuzione:

- **ChatGPT Web** — l'AI non ha accesso diretto al repository. I file del framework vengono caricati come un unico archivio ZIP; PROJECT.yaml e le immagini vengono allegati separatamente.
- **Claude Code** — l'AI ha accesso diretto al repository clonato localmente. Nessun allegato necessario: legge e scrive i file direttamente.

Lo stesso framework, le stesse regole, la stessa pipeline — procedure di avvio diverse.

---

## Tabella comparativa

| Caratteristica | ChatGPT Web | Claude Code |
|---|---|---|
| Repository locale richiesto | NO | **SÌ** |
| Framework allegato come ZIP | **SÌ** | NO |
| PROJECT.yaml | Allegato separatamente | File nel repo locale |
| Immagini di riferimento | Allegate separatamente | File nel repo locale |
| Nuova chat consigliata per ogni fase | **SÌ** (obbligatorio) | Solo al cambio di motore |
| L'AI accede ai file del framework | Via ZIP caricato | Direttamente nel repo |
| L'AI scrive i file generati | NO — output in chat | **SÌ** — scrive nel repo |
| Usabile senza Git | **SÌ** | NO |
| Adatto a operatori non tecnici | **SÌ** | Richiede familiarità con CLI |

---

## Quale runtime scegliere

| Se... | Usa |
|---|---|
| Non hai Git installato | ChatGPT Web |
| Non vuoi clonare il repository | ChatGPT Web |
| Vuoi iniziare in meno di 5 minuti | ChatGPT Web |
| Hai già il repository clonato | Claude Code |
| Vuoi che l'AI scriva i file direttamente nel repo | Claude Code |
| Sei uno sviluppatore che lavora sul framework | Claude Code |

---

## Guide per runtime

| Runtime | Guida | Stato |
|---|---|---|
| ChatGPT Web | `OperatorGuide/Runtimes/ChatGPT_Web.md` | ✅ Disponibile |
| Claude Code | `OperatorGuide/Runtimes/Claude_Code.md` | ✅ Disponibile |

---

## Runtime futuri

L'architettura del framework è progettata per supportare altri runtime senza modifiche alla pipeline o al Prompt Engine. Per aggiungere un runtime: creare `OperatorGuide/Runtimes/{NomeRuntime}.md` seguendo lo stesso formato delle guide esistenti, poi aggiornare questa tabella.

| Runtime | Stato | Note |
|---|---|---|
| ChatGPT Web | ✅ Supportato | Procedura via ZIP + allegati |
| Claude Code | ✅ Supportato | Accesso diretto al repository |
| Claude Web | 🔜 Pianificato | Analogo a ChatGPT Web |
| Gemini | 🔜 Pianificato | Via Google Drive o allegati |
| Ollama | 🔜 Pianificato | Locale, richiede context window ≥ 100K token |
| Open WebUI | 🔜 Pianificato | Dipende dal modello backend |
| vLLM | 🔜 Pianificato | Deployment locale/cloud |

---

## Riferimenti

- `OperatorGuide/Runtimes/ChatGPT_Web.md` — guida completa ChatGPT Web
- `OperatorGuide/Runtimes/Claude_Code.md` — guida completa Claude Code
- `START_HERE.md` — punto di partenza assoluto
- `Docs/AI_BOOTSTRAP_PROMPT.md` — prompt separati per runtime
