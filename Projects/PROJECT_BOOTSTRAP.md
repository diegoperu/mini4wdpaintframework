# PROJECT_BOOTSTRAP.md — Creazione Nuovo Progetto

**Mini4WD Manual SDK v2.4.1** · Guida operativa
**Prerequisito:** `START_HERE.md` (root del repository)

> Guida operativa, non descrittiva: esegui i PASSI in ordine, uno alla volta.
> Al termine avrai un progetto pronto e il Bootstrap approvato.
> Versione estesa con esempi reali: `FIRST_PROJECT.md`.

---

## Prima di iniziare — cosa ti serve

- [ ] Nome ufficiale Tamiya del modello (grafia esatta)
- [ ] Codici vernice del produttore (es. TS-57, PS-1)
- [ ] Foto del modello fisico: minimo front, 2 lati, top, 3/4 frontale
- [ ] Un modello AI con contesto ampio (100K+ token consigliati)

---

## PASSO 1 — Crea la cartella progetto

```bash
MODEL="Nome_Modello"        # spazi → underscore. MAI trattini nel nome cartella.
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw" "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"
```

Regole nome (da `Core/NAMING_CONVENTION.md`):

- `Proto Emperor` → `Proto_Emperor` ✓
- `Dash 01 Shadow Emperor` → `Dash_01_Shadow_Emperor` ✓ (non `Dash-01_...` ✗)
- Maiuscole conservate, niente abbreviazioni, niente caratteri speciali

**Non creare altre cartelle**, in particolare niente sotto `Assets/` o `ApprovedAssets/`.

## PASSO 2 — Copia e compila PROJECT.yaml

```bash
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
```

Apri la copia (MAI il master in `Templates/`) e compila ogni campo REQUIRED seguendo i
commenti nel file. Regole:

1. Codici vernice reali del produttore — mai inventati
2. Dato mancante → `TODO:` — mai un valore inventato
3. `modelSlug` in kebab-case: `dash-01-shadow-emperor`
4. Percorsi in `paths:` relativi alla cartella progetto (`Images/...`)
5. I valori-chiave dello schema (`finish: gloss`, `technique: spray-can`) restano in
   inglese: sono chiavi tecniche, non testo editoriale. L'italiano è per i contenuti
   che finiranno sulle pagine.

Esempio compilato di riferimento: `Projects/Proto_Emperor/PROJECT.yaml` (sola lettura).

## PASSO 3 — Inserisci le foto di riferimento

Copia le foto in `Projects/{Modello}/Images/` — **unica posizione valida** (v2.4.1;
`Assets/ReferenceModels/` è riservata al Maintainer):

| File | Vista | Obbligatoria |
|---|---|---|
| `ref_front.jpg` | Frontale | Sì |
| `ref_side_left.jpg` | Lato sinistro | Sì |
| `ref_side_right.jpg` | Lato destro | Sì |
| `ref_top.jpg` | Dall'alto | Sì |
| `ref_3q_front.jpg` | 3/4 frontale-sinistra | Sì (copertina) |
| `ref_rear.jpg` | Posteriore | Consigliata |
| `ref_detail_*.jpg` | Dettagli | Se servono |

Qualità: min 2048px lato lungo, sfondo bianco/neutro, fuoco nitido (`Config/render.yaml`).

## PASSO 4 — Verifica pre-bootstrap

```
[ ] PROJECT.yaml senza campi REQUIRED vuoti (o TODO: motivati)
[ ] Foto presenti (min 5)
[ ] Nome cartella con underscore, modelSlug in kebab-case
[ ] Nessun file toccato fuori da Projects/{Modello}/
```

Non serve inizializzare `ApprovedAssets/`: i moduli pagina P001–P010 esistono già in
stato `draft` (sono template — verranno riempiti dall'AI in Fase 2).

## PASSO 5 — Bootstrap della sessione AI

1. Apri una **nuova chat**.
2. Vai a `Docs/AI_BOOTSTRAP_PROMPT.md → Fase 1 — Bootstrap`.
3. Allega i file nell'ordine elencato (framework + il TUO PROJECT.yaml + le TUE foto).
4. Incolla il prompt Fase 1 e invia.

## PASSO 6 — Approva il Bootstrap Report

L'AI produce un Bootstrap Report (formato: `AI_ENTRYPOINT.md`). Verifica che citi il
TUO modello, i TUOI colori, e le pagine P001–P010 in `draft`. Poi scrivi in chat:

```
Bootstrap approvato. Inizia dalla pagina P001.
```

**Il progetto è avviato.** Da qui:

- Percorso completo: `OperatorGuide/01_Primo_Manuale.md`
- State machine: `WORKFLOW.md` (root)
- Prompt per le fasi successive: `Docs/AI_BOOTSTRAP_PROMPT.md` (Fasi 2–5)

## PASSO 7 — Loop di generazione (sintesi)

Per ogni pagina P001 → P010, nella stessa chat del bootstrap:

```
PASSO 7a  Genera   → Prompt Fase 2 + PromptEngine/{pagina}.md → content.yaml
PASSO 7b  Valida   → Prompt Fase 3 + Tests/ContentValidation.md + Tests/TextValidation.md
PASSO 7c  Correggi → se REJECTED: applica le correzioni, torna a 7b
PASSO 7d  Sigilla  → metadata.yaml → status: locked + riga di changelog
```

⚠️ Mai validare una pagina non ancora generata: i template `draft` falliscono il QA
per costruzione (`Tests/ContentValidation.md §Validation Scope`).

## PASSO 8 — Fasi successive

| Fase | Guida | Chat |
|---|---|---|
| Rendering | `FIRST_RENDER.md` | Nuova (chat #2) |
| PDF | `FIRST_PDF.md` | Nuova (chat #3) |
| Pubblicazione | `LIFECYCLE.md` — la esegue il Maintainer | — |

---

## Riferimenti

- `START_HERE.md` — punto di partenza assoluto
- `PROJECT_STRUCTURE.md` — struttura cartelle e convenzione immagini
- `FILE_MATRIX.md` — cosa puoi modificare
- `OperatorGuide/06_Errori_Comuni.md` — se qualcosa fallisce
- `Projects/Proto_Emperor/` — progetto di riferimento (sola lettura)
