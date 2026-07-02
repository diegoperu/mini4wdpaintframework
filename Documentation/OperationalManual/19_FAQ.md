# Capitolo 19 — FAQ

Domande frequenti su verniciatura, uso dello SDK, qualità e versioning, organizzate per area.

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| FAQ | `Knowledge/FAQ.md` (KNW-FAQ-001) | Source of Truth |

---

## Generale

**D: Serve un aerografo per usare questo SDK?**
R: No. Tutte le pagine e le tecniche dello SDK sono realizzabili con bombolette spray (serie Tamiya TS/PS). Le istruzioni per aerografo sono incluse come tecnica opzionale dove offrono un vantaggio.

**D: Posso usare qualunque marca di vernice, o devo usare Tamiya?**
R: Si può usare qualunque marca di vernice. Lo SDK usa i codici Tamiya come riferimento ma supporta qualunque marca — compilare `paintBrand` e `paintCode` in `PROJECT.yaml` di conseguenza. Vedi `Knowledge/Paints.md` per i formati di marca supportati.

**D: Qual è la differenza tra vernici PS e TS?**
R: Le vernici TS sono per plastica ABS (standard). Le vernici PS sono formulate per carrozzerie in policarbonato (Lexan). Usare TS su policarbonato rischia la screpolatura. Verificare il materiale della carrozzeria prima di scegliere la vernice.

## Uso dello SDK

**D: Posso usare questo SDK con qualunque modello AI?**
R: Sì. I prompt di `PromptEngine/` sono progettati per essere model-agnostic e funzionano con ChatGPT, Claude, Gemini, e qualunque LLM in grado di seguire istruzioni. Vedi `PromptEngine/README.md` (Capitolo 07).

**D: Come aggiungo un nuovo modello Mini4WD?**
R: Copiare `Templates/PROJECT.yaml` in `Projects/{NuovoModello}/PROJECT.yaml`, compilare tutti i campi, poi seguire `Build/Pipeline.md` a partire dalla Fase 0 (Capitolo 05).

**D: Cosa succede se un angolo di render richiesto non è ottenibile con il mio generatore di immagini AI?**
R: Usare l'angolo disponibile più vicino e documentare lo scostamento in `Projects/{ModelName}/Notes/`. Segnalarlo nel log QA come limitazione nota.

**D: Posso saltare delle pagine?**
R: P001, P002, P003, P004, P005, P006, P007, P008 e P010 sono obbligatorie. P009 (Variante Premium) è opzionale — impostare `premiumVariant.enabled: false` in `PROJECT.yaml`.

## Qualità

**D: Il mio render ha uno sfondo leggermente fuori bianco. Passerà la QA?**
R: No. L'item QA-017 richiede esattamente `#FFFFFF`. Rigenerare con istruzione esplicita di sfondo bianco. Vedi `Config/quality.yaml § thresholds.background_white_tolerance_rgb` (Capitolo 11).

**D: Quanti fallimenti QA sono ammessi?**
R: Zero fallimenti bloccanti. Massimo 3 eccezioni non bloccanti (documentate in `qa_log.md`). Vedi `Config/quality.yaml § approval`.

**D: Chi approva un manuale?**
R: Il maintainer del progetto controfirma `Assets/ApprovedManual/{ModelName}/README.md`. Vedi `Build/Pipeline.md § Phase 6` (Capitolo 12).

## Versioning

**D: Quale versione dello SDK devo usare per il mio progetto?**
R: Usare sempre l'ultima versione stabile. Registrare la versione dello SDK in `PROJECT.yaml § sdk_version`.

**D: Posso aggiornare un manuale esistente a una versione più recente dello SDK?**
R: Sì. Vedi `Docs/migration/` per le guide di migrazione specifiche per versione (Capitolo 15).

## Vedi anche

- Capitolo 07 — TextEngine (per il funzionamento di `PromptEngine/`)
- Capitolo 11 — QA (per soglie e approvazione)
- Capitolo 15 — Versioning (per le guide di migrazione)
- Capitolo 20 — Glossary (per i termini tecnici citati qui)
