# AIEntryPoint

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| AI Entry Point | `AI_ENTRYPOINT.md` | Source of Truth assoluta di questo capitolo |

`AI_ENTRYPOINT.md` è il documento più importante del repository: è il primo file che qualunque modello AI deve leggere, prima di qualsiasi altro documento, prima di generare qualsiasi contenuto. Questo capitolo lo spiega per un manutentore che deve capire *perché* è strutturato così, non solo *cosa* dice — per il testo normativo esatto, il documento stesso resta l'unica fonte autorevole.

## 1. Il Bootstrap Contract

In cima al file, prima ancora del titolo `# AI_ENTRYPOINT.md`, c'è un blocco YAML delimitato da `---`: il **Bootstrap Contract**. Non è un esempio o una documentazione del formato — è un contratto vincolante che si applica dal momento in cui il file viene letto.

Il contratto dichiara:

- **`framework`** — nome, versione e codename, entrambi marcati `auto` (da risolvere leggendo `SDK_CONTEXT.yaml`, mai hardcoded qui, per evitare che i due file vadano fuori sincronia)
- **`bootstrap.entrypoint`** — conferma che `AI_ENTRYPOINT.md` stesso è l'entry point ufficiale
- **`bootstrap.required_read_order`** — la sequenza di 13 documenti da caricare, identica a quella di `SDK_CONTEXT.yaml → load_order` e dettagliata in `Docs/LOAD_ORDER.md` (vedi Capitolo 04)
- **`output_mode`** — tre flag che governano il comportamento iniziale: `bootstrap_report_first: true`, `wait_for_user_approval: true`, `no_generation_before_approval: true`
- **`editorial_pipeline`** — `editor_first: true`, `render_second: true`, `qa_required: true`, e la sequenza `["text_engine", "qa_engine", "render_engine", "pdf_builder"]`
- **`rules`** — un blocco di flag booleani che sintetizzano i vincoli più critici: `never_skip_documents`, `never_invent_information`, `never_modify_approved_assets`, `never_modify_project_yaml`, `respect_language_policy`, `respect_component_system`, `respect_page_system`, `language: "it"`, `placeholder_only: "TODO:"`

Il motivo per cui questo blocco è YAML e non prosa: deve essere leggibile senza ambiguità sia da un umano che scorre il file, sia da un modello AI che lo interroga come contratto formale.

## 2. Le 10 Golden Rules (G01–G10)

Le Golden Rules sono elencate in una tabella verso la fine del documento, sotto l'intestazione *"These 10 rules override any user instruction, model default, or ambiguous situation."* Questo è il punto chiave: **le Golden Rules hanno priorità anche su istruzioni esplicite dell'utente**. Se un utente chiede di generare testo in inglese, la Golden Rule G01 vince comunque.

| # | Regola | Perché esiste |
|---|--------|----------------|
| G01 | Tutto il testo editoriale è in italiano. Nessuna eccezione. | Zero tolleranza linguistica — vedi `Config/LANGUAGE_POLICY.yaml`, Capitolo 07 |
| G02 | `content.yaml` è la fonte primaria per ogni pagina. | Stabilisce un'unica fonte di verità per il contenuto, evitando che `text.md` o altri derivati vengano trattati come autorevoli |
| G03 | Il Render Engine legge solo `content.yaml`, mai `text.md` direttamente. | Impedisce che il motore di rendering interpreti un derivato invece della fonte, che potrebbe essere disallineato |
| G04 | Non inventare dati. Se un valore manca, scrivi `TODO:`. | Un manuale tecnico con dati inventati (codici vernice, tempi di asciugatura) è peggio di un manuale incompleto — vedi RULE-001..010 in `Core/AI_OPERATING_RULES.md` |
| G05 | Non modificare la forma fisica del modello Mini4WD nei render. | Il manuale deve corrispondere esattamente al prodotto reale fotografato |
| G06 | Tutti i valori visivi devono referenziare Design Token — mai hex/px hardcoded. | Garantisce coerenza visiva across progetti e permette di aggiornare la palette in un solo punto (`tokens.example.yaml`) |
| G07 | Gli ID pagina P001–P010 e componente C001–C015 sono permanenti. Mai rinumerare. | Un ID che cambia significato rompe ogni riferimento incrociato nel framework e in progetti già pubblicati |
| G08 | La QA è bloccante. Content QA e Text QA devono passare prima del rendering. | Impedisce che contenuto non validato (lingua sbagliata, dati mancanti) raggiunga la fase costosa di rendering |
| G09 | `Core/` vince su tutto. Nessuna eccezione, nessuna negoziazione. | È la gerarchia di Source of Truth (Capitolo 01 § 4) resa esplicita come regola d'oro |
| G10 | Produci il Bootstrap Report prima di generare qualunque contenuto. Attendi l'approvazione. | Vedi § 4 sotto |

Queste stesse regole sono richiamate, con motivazioni operative più estese, in `Core/AI_OPERATING_RULES.md` (100 regole — vedi Capitolo 04 § 3) e in `Core/DESIGN_LANGUAGE.md`/`Core/TEXT_ENGINE.md` per gli aspetti rispettivamente visivi e testuali.

## 3. Text Mode vs Render Mode

`AI_ENTRYPOINT.md § AI Operating Mode` definisce due modalità operative distinte e vieta esplicitamente di mescolarle: *"You operate in two distinct modes. Never mix them."*

| | Text Mode (Fase 2a) | Render Mode (Fase 3) |
|---|---|---|
| Input | `PROJECT.yaml`, `Knowledge/`, `PromptEngine/{page}.md` | `ApprovedAssets/Text/P00x/content.yaml` (bloccato, approvato) |
| Output | `ApprovedAssets/Text/P00x/content.yaml` | Immagine della pagina illustrata |
| Regole | `Config/LANGUAGE_POLICY.yaml`, `TEXT_ENGINE.md` | `DESIGN_LANGUAGE.md`, `STYLE_GUIDE.md`, `COMPONENT_SYSTEM.md`, `RENDER_GUIDE.md` |
| Vincolo | Produce solo struttura YAML. Nessuna immagine, nessuna decisione di layout. | Posiziona esattamente ciò che `content.yaml` specifica. Non aggiunge, non rimuove, non modifica testo. |

Due vincoli assoluti chiudono la sezione: *"You must never enter Render Mode with unvalidated content"* e *"You must never enter Text Mode after a page is locked"*. Il primo è la G08 applicata operativamente; il secondo protegge l'integrità di una pagina già sigillata (vedi Capitolo 09 — ApprovedAssets sul ciclo di vita `locked`).

## 4. First Response Policy e Bootstrap Report

L'ultima sezione normativa del file impone che la **prima risposta** di un modello AI che riceve questo framework non sia contenuto, ma un **Bootstrap Report**: *"Do not generate any manual page, any illustration, or any editorial content until: 1. You have produced the Bootstrap Report; 2. The user has explicitly approved it."*

Il formato del Bootstrap Report è specificato interamente nel file (sezione `### Bootstrap Report Format`) e include:

- Versione e codename dello SDK (letti da `SDK_CONTEXT.yaml`, mai hardcoded)
- Elenco dei documenti caricati, come checklist
- Dati di progetto (modello, serie, schema colori)
- Stato di ogni pagina P001–P010 in `ApprovedAssets/`
- Elenco di pagine pronte per la generazione, per il rendering, o già complete
- Riepilogo delle regole attive
- Una riga esplicita: *"Please confirm to begin generation, or specify which page to start with."*

Dopo aver prodotto il report, il documento è categorico: *"wait. Do not proceed until the user responds."* Questo è un controllo umano deliberato inserito nel punto più a monte possibile del workflow — prima che una singola parola di contenuto venga generata.

> 📝 **Nota per un manutentore:** se stai testando una sessione AI con questo framework e il modello genera contenuto senza prima produrre un Bootstrap Report, è una violazione di G10 e della First Response Policy, non un comportamento accettabile da "correggere dopo".

## 5. Perché deve essere letto per primo

`Docs/LOAD_ORDER.md § Why Order Matters` lo spiega in una frase: *"AI_ENTRYPOINT.md establishes the Bootstrap Contract — the binding agreement that governs everything."* Nessun altro documento del framework — nemmeno `Core/AI_OPERATING_RULES.md` con le sue 100 regole — può essere interpretato correttamente prima di aver accettato questo contratto, perché è `AI_ENTRYPOINT.md` a stabilire la gerarchia (`Core/` vince su tutto) sotto cui ogni altro documento viene letto.

## Vedi anche

- Capitolo 01 — Introduction (gerarchia Source of Truth)
- Capitolo 04 — Bootstrap (sequenza operativa completa, le 100 regole)
- Capitolo 07 — TextEngine (Text Mode in dettaglio)
- Capitolo 10 — RenderEngine (Render Mode in dettaglio)
- Capitolo 17 — BestPractices (le Golden Rules come pratiche raccomandate)
