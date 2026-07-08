# Capitolo 08 — Assets e Design System

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Filosofia di design | `Core/DESIGN_LANGUAGE.md` | Source of truth — 65 regole, principi non negoziabili |
| Specifica visiva | `Core/STYLE_GUIDE.md` | Valori esatti: colori, tipografia, griglia, spaziatura |
| Sistema colore | `Core/COLOR_SYSTEM.md` | Riferimento autoritativo per ogni colore ammesso |
| Sistema componenti | `Core/COMPONENT_SYSTEM.md` | Registro C001–C015, specifiche complete |
| Sistema pagine | `Core/PAGE_SYSTEM.md` | Registro P001–P010, dipendenze per pagina |
| Convenzione naming | `Core/NAMING_CONVENTION.md` | Regole di nome per file, cartelle, identificatori |
| Design Tokens (esempio) | `Assets/DesignSystem/Tokens/tokens.example.yaml` | Unico sorgente di valori visivi machine-readable |
| Schema token | `Assets/DesignSystem/Tokens/tokens.schema.yaml` | Validazione struttura token |
| README Assets | `Assets/README.md`, `Assets/DesignSystem/README.md` + 6 README di sottocartella | Ruolo di ogni sottodirectory |
| Modelli di riferimento | `Assets/ReferenceModels/README.md` | Foto fisiche usate come base per i render |
| Test correlati | `Tests/LayoutValidation.md`, `ColorValidation.md`, `NamingValidation.md`, `AssetsValidation.md` | QA per griglia, colore, naming, integrità asset |

## Cos'è e perché esiste

`Core/DESIGN_LANGUAGE.md` è il fondamento filosofico: non descrive colori o dimensioni (quello è compito di `STYLE_GUIDE.md`/`COLOR_SYSTEM.md`) ma le convinzioni che informano ogni decisione — Rule 1: "questo framework esiste per servire l'hobbista"; Rule 5: "documentation is code", nessun linguaggio vago nelle affermazioni normative; Rule 9: "ogni pagina deve sembrare disegnata dalla stessa mano". Se una domanda di design non trova risposta in STYLE_GUIDE o COMPONENT_SYSTEM, la risposta è qui.

## Identità visiva in sintesi

Bianco è il colore dominante su ogni pagina; il colore primario TamiyaPrimary è l'accento che marca il framework; oro evidenzia l'eccellenza; rosso è esclusivo per gli avvisi (Rule 13). La banda header TamiyaPrimary è la firma dello SDK — deve comparire su ogni pagina (Rule 14). Nessun elemento decorativo è ammesso a meno che non serva uno scopo informativo (Rule 18).

### Rules 55–65 — Identità editoriale (v2.3.0)

Sezione unica di questo SDK: separa esplicitamente l'estetica visiva (ispirata all'artigianato tecnico giapponese Tamiya) dalla lingua editoriale (italiana). Rule 058: "un lettore che non capisce il giapponese deve capire ogni parola del manuale — zero caratteri giapponesi in qualunque elemento testuale." Rule 061: "il design non deve mai sembrare una traduzione automatica — deve sembrare scritto da un editore italiano che ama i Mini4WD." Questa distinzione è operativamente rilevante: un'AI che genera testo non deve mai confondere il riferimento estetico (visivo) con la lingua (editoriale) — vedi Capitolo 07.

## Design Tokens: l'unica fonte di valori visivi

Regola d'oro G06 (`AI_ENTRYPOINT.md`): tutti i valori visivi devono referenziare nomi di Design Token — mai hex/px/pt hardcoded. `Assets/DesignSystem/Tokens/tokens.example.yaml` è il file machine-readable che ogni componente e ogni pagina consulta. Se un colore non è in `Core/COLOR_SYSTEM.md` e in questo file token, non può comparire in una pagina del manuale (eccezione: gli swatch di vernice reale nel componente C003, che rappresentano dati del mondo reale, non colori strutturali).

Palette chiusa — colori strutturali e funzionali:

| Ruolo | Colori | Uso |
|-------|--------|-----|
| Strutturale | TamiyaPrimary `#114B69`, TamiyaDark, TamiyaLight, White, OffWhite, LightGray | Identità, layout, background |
| Funzionale | Black `#1A1A1A` (mai #000000 puro), DarkGray, MidGray | Testo |
| Funzionale — segnale | RedWarning (solo avvisi), GoldAccent (max 3 per pagina), GreenSuccess, BlueInfo | Comunicazione a colore fisso |

Regola assoluta (`Core/COLOR_SYSTEM.md §7`): testo su sfondo scuro (TamiyaPrimary) è sempre bianco, nessuna eccezione.

## Component System: C001–C015

I componenti sono i blocchi riutilizzabili — una pagina non si disegna da zero, si assembla. Gli ID sono permanenti in formato `C###` e non cambiano mai (`next_available_component_id` attuale: `C016`).

| ID | Nome | Obbligatorio su |
|----|------|------------------|
| C001 | Header | Tutte le pagine |
| C002 | Footer | Tutte le pagine |
| C003 | Palette | P002, P009 |
| C004 | Shopping List | P003 |
| C005 | Paint Sequence | P004, P005 |
| C006 | Callout | P004–P008 |
| C007 | Exploded View | P006 |
| C008 | Warning | P003–P008 |
| C009 | Tips | P004–P009 |
| C010 | Paint Legend | P002 |
| C011 | Paint Code Box | P002, P005–P007 |
| C012 | Zoom | P006–P008 |
| C013 | Step Number | P004–P008 |
| C014 | Time Box | P004–P006 |
| C015 | Notes | P010 |

Dalla v2.4.0 ogni componente dichiara anche il proprio campo `content.yaml` sorgente (`Core/COMPONENT_SYSTEM.md §v2.4.0 — content.yaml Field Mapping`) — es. C008 Warning legge `warnings[*]` e deve iniziare con "Attenzione:"; C009 Tips legge `tips[*]` e deve iniziare con "Suggerimento:".

## Page System: P001–P010

Registro permanente delle pagine — vedi Capitolo 07 per la mappa pagina→content.yaml. Ogni pagina dichiara i propri componenti richiesti, i propri campi PROJECT.yaml di input, una checklist e gli errori comuni. P009 (Premium Variant) è l'unica pagina non obbligatoria; ometterla è valido, un manuale che ne omette un'altra fallisce `QA-086`.

## Naming Convention in sintesi

Pattern per le immagini: `{model-slug}_{pageId}_{descriptor}_{version}.{ext}` — es. `proto-emperor_P001_cover_v1.png`. Cartelle SDK: PascalCase (`Core/`, `PromptEngine/`). Cartelle progetto: PascalCase con underscore (`Proto_Emperor`), lo slug derivato è lowercase-hyphen (`proto-emperor`). Caratteri vietati ovunque: spazi e 17 simboli con significato shell/URL/filesystem (`Core/NAMING_CONVENTION.md §6`).

> 📝 **Nota:** `Core/NAMING_CONVENTION.md §2.1` specifica che i file guida in `Docs/` usano `kebab-case.md` (esempio citato: `automated-pdf.md`) — ma i file reali in `Docs/` sono `AI_BOOTSTRAP_PROMPT.md`, `LOAD_ORDER.md`, `README.md`, tutti in SCREAMING_SNAKE_CASE o convenzione fissa; solo `Docs/migration/v1-to-v2.md` segue davvero il kebab-case dichiarato. L'esempio `automated-pdf.md` non esiste nel repository. Incoerenza minore, non bloccante — segnalata in `Validation/CONSISTENCY_CHECK.md`.

## Errori comuni

| Errore | Rilevamento | Fix |
|--------|-------------|-----|
| Colore hex hardcoded invece del token | Grep di pattern `#[0-9A-Fa-f]{6}` fuori da tokens.example.yaml | Sostituire con `{{token.NomeColore}}` |
| Render con sfondo grigio/gradiente | Ispezione visiva | Rigenerare — solo bianco puro o trasparente |
| Header con gradiente invece di TamiyaPrimary solido | Ispezione visiva | Sostituire con `#114B69` piatto (via token) |
| Componente C008/C009 usato per lo scopo sbagliato | Confronto contenuto vs ruolo (avviso vs consiglio) | C008 solo per rischio, C009 solo per best practice |
| Più di 3 elementi oro per pagina | Conteggio visivo | Ridurre — l'oro perde significato se sovrautilizzato |

## Vedi anche

- Capitolo 07 — TextEngine (i componenti C001–C015 ricevono testo da content.yaml, mai lo generano)
- Capitolo 10 — RenderEngine (applica Design Language e Style Guide in fase di rendering)
- Capitolo 11 — QA (le 4 suite di test collegate a questo capitolo)
