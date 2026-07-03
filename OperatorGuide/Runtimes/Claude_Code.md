# Guida Claude Code — Il Tuo Primo Manuale

**OperatorGuide · Mini4WD Manual SDK v2.4.1 · Runtime: Claude Code**

> Questa guida è autonoma: contiene tutto ciò che ti serve per produrre il tuo primo manuale
> usando Claude Code. Non è necessario leggere altri documenti prima di questa guida.
> Segui i passi nell'ordine esatto.

---

## Cosa è diverso da ChatGPT Web

Con Claude Code l'AI ha accesso diretto al repository clonato localmente:
- Non devi caricare alcun ZIP
- Non devi allegare file manualmente
- L'AI legge direttamente tutti i file del framework
- L'AI **scrive** i file generati (content.yaml, metadata.yaml, ecc.) direttamente nel repository
- Non serve riaprire una nuova sessione per ogni fase: Claude Code mantiene il contesto del repository

---

## Cosa ti serve

- [ ] Claude Code installato (`npm install -g @anthropic-ai/claude-code` o pacchetto equivalente)
- [ ] Git installato
- [ ] Repository Mini4WD Manual SDK clonato localmente
- [ ] Nome ufficiale Tamiya del tuo modello (grafia esatta)
- [ ] Codici vernice Tamiya (es. TS-57, PS-1, XF-1)
- [ ] Foto del modello: minimo 5 angolazioni (front, lati, top, 3/4 frontale)

---

## PASSO 1 — Clona il repository

```bash
git clone https://github.com/diegoperu/mini4wdpaintframework.git
cd mini4wdpaintframework
```

Il repository è ora disponibile localmente. Claude Code può leggere e scrivere tutti i file.

---

## PASSO 2 — Crea la cartella progetto

```bash
MODEL="Nome_Modello"        # spazi → underscore, MAI trattini nel nome cartella
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw" "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"
```

Regole nome cartella (da `Core/NAMING_CONVENTION.md`):

| Modello | Nome cartella corretto |
|---|---|
| Proto Emperor | `Proto_Emperor` |
| Dash 01 Shadow Emperor | `Dash_01_Shadow_Emperor` |

Maiuscole conservate, underscore tra le parole, niente trattini nel nome cartella.

**Non creare altre cartelle**, in particolare niente sotto `Assets/` o `ApprovedAssets/`.

---

## PASSO 3 — Copia e compila PROJECT.yaml

```bash
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
```

Apri la **copia** (MAI il master in `Templates/`) con qualsiasi editor e compila ogni campo marcato `# REQUIRED`. Regole:

1. **Nomi vernici reali** — usa i codici Tamiya reali (TS-57, X-10, PS-1…), mai inventati
2. **Dato mancante** → scrivi `TODO:` — mai un valore inventato
3. **`modelSlug`** in kebab-case: `dash-01-shadow-emperor`
4. I percorsi in `paths:` sono relativi alla cartella progetto: `Images/ref_front.jpg`
5. I valori tecnici (`finish: gloss`, `technique: spray-can`) restano in inglese

Esempio di riferimento già compilato: `Projects/Proto_Emperor/PROJECT.yaml` (sola lettura).

---

## PASSO 4 — Inserisci le immagini di riferimento

Copia le tue foto in `Projects/{Modello}/Images/` — **unica posizione valida**.

| Nome file | Vista | Obbligatoria |
|---|---|---|
| `ref_front.jpg` | Frontale | **SÌ** |
| `ref_side_left.jpg` | Lato sinistro | **SÌ** |
| `ref_side_right.jpg` | Lato destro | **SÌ** |
| `ref_top.jpg` | Dall'alto | **SÌ** |
| `ref_3q_front.jpg` | 3/4 frontale-sinistra | **SÌ** (per la copertina) |
| `ref_rear.jpg` | Posteriore | Consigliata |
| `ref_detail_*.jpg` | Dettagli particolari | Se disponibili |

Requisiti: minimo 2048px sul lato lungo, sfondo bianco o neutro, fuoco nitido.

---

## PASSO 5 — Verifica pre-bootstrap

```
[ ] Projects/{Modello}/ creata con Images/, Output/, Notes/
[ ] PROJECT.yaml compilato, nessun campo REQUIRED vuoto (o TODO: motivato)
[ ] Minimo 5 foto in Projects/{Modello}/Images/
[ ] Nome cartella con underscore, modelSlug in kebab-case
[ ] Nessun file toccato fuori da Projects/{Modello}/
```

---

## PASSO 6 — Avvia Claude Code nel repository

```bash
claude
```

Claude Code si avvia nel contesto del repository. L'AI può leggere tutti i file del framework direttamente — non serve allegare nulla.

---

## PASSO 7 — Usa il Prompt Bootstrap

Incolla il **Prompt Fase 1 — Bootstrap** da `Docs/AI_BOOTSTRAP_PROMPT.md §FASE 1 · Claude Code`.

```
Stai operando come motore editoriale del Mini4WD Manual SDK v2.4.1.

Leggi i seguenti file del repository nell'ordine indicato:
1. AI_ENTRYPOINT.md
2. SDK_CONTEXT.yaml
3. BOOTSTRAP.md
4. Core/AI_OPERATING_RULES.md
5. Config/LANGUAGE_POLICY.yaml
6. Core/TEXT_ENGINE.md
7. Core/DESIGN_LANGUAGE.md
8. Core/STYLE_GUIDE.md
9. Core/COMPONENT_SYSTEM.md
10. Core/PAGE_SYSTEM.md
11. Projects/{Modello}/PROJECT.yaml
12. Projects/{Modello}/Images/ (immagini di riferimento)

Regole fondamentali:
- Tutto il testo editoriale deve essere in italiano.
- content.yaml è la source of truth per ogni pagina.
- Non inventare dati. Se un valore non è in PROJECT.yaml, usa TODO: come placeholder.
- Nomi commerciali delle vernici, codici prodotto (TS-xx, X-xx, PS-xx) e chiavi YAML
  sono language-neutral: non vanno tradotti né segnalati come violazioni.
- Non modificare la forma fisica del modello nei render.
- Segui Core/AI_OPERATING_RULES.md per ogni operazione.

Produci ora il Bootstrap Report nel formato definito da AI_ENTRYPOINT.md,
poi fermati e attendi la mia approvazione esplicita.
```

Sostituisci `{Modello}` con il nome reale della cartella progetto.

---

## PASSO 8 — Approva il Bootstrap Report

L'AI produce un Bootstrap Report. Verifica che contenga:

- [ ] Il nome del TUO modello (non un modello di esempio)
- [ ] I TUOI codici vernice
- [ ] Le 10 pagine P001–P010 in stato `draft`
- [ ] Conferma versione SDK 2.4.1

Se corretto, scrivi:

```
Bootstrap approvato. Inizia dalla pagina P001.
```

Se il report cita dati sbagliati: correggi `Projects/{Modello}/PROJECT.yaml` e rilancia il prompt.

---

## PASSO 9 — Generazione testi (stessa sessione)

Nella stessa sessione Claude Code, usa il **Prompt Fase 2** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

Con Claude Code, l'AI scrive `content.yaml` direttamente in `ApprovedAssets/Text/P00x/`.
Non serve copiare output dalla chat: i file sono già nel repository.

Per ogni pagina P001 → P010:
1. **Genera** — Prompt Fase 2
2. **Valida** — Prompt Fase 3 (QA)
3. **Correggi** se REJECTED, poi rivalida
4. **Sigilla** — l'AI aggiorna `metadata.yaml → status: locked`

---

## PASSO 10 — Rendering (nuova sessione con contesto diverso)

Il rendering usa un contesto AI diverso dai testi. Avvia una nuova sessione Claude Code
(oppure usa il **Prompt Fase 4** nella sessione corrente se il contesto è ancora pulito).

Usa il **Prompt Fase 4** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

L'AI legge direttamente `ApprovedAssets/Text/P00x/content.yaml` (già locked) e
`Projects/{Modello}/Images/` — nessun allegato necessario.

---

## PASSO 11 — PDF

Usa il **Prompt Fase 5** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

Prerequisito: copia compilata di `Templates/PDF_CONFIG.yaml` in `Projects/{Modello}/PDF_CONFIG.yaml`.

---

## Riepilogo fasi

| Fase | Nuova sessione | Cosa fa l'AI |
|---|---|---|
| Bootstrap + Testi + QA | SÌ (inizio) | Legge dal repo, scrive content.yaml |
| Rendering | Consigliata (contesto diverso) | Legge content.yaml, scrive immagini in ApprovedAssets/ |
| PDF | Consigliata | Guida assemblaggio PDF |

---

## Sessione degenerata o contesto saturo?

Usa il **Prompt F — Continuità** da `Docs/AI_BOOTSTRAP_PROMPT.md §Prompt di servizio`.
Con Claude Code non serve ricaricare i file — l'AI accede di nuovo direttamente al repository.

---

## Errori frequenti

| Errore | Causa | Soluzione |
|---|---|---|
| L'AI valida template vuoti e dà FAIL | Hai saltato la generazione (Fase 2) | Genera prima, poi valida |
| content.yaml contiene dati inventati | PROJECT.yaml aveva campi vuoti | Correggi PROJECT.yaml, rigenera |
| L'AI modifica file fuori da Projects/ | Istruzioni errate nel prompt | Usa i prompt ufficiali, controlla le modifiche |
| Contesto saturo | Chat troppo lunga | Prompt F — Continuità |

Guida errori completa: `OperatorGuide/06_Errori_Comuni.md`

---

## Riferimenti

- `Docs/RUNTIMES.md` — confronto tra tutti i runtime
- `Docs/AI_BOOTSTRAP_PROMPT.md` — tutti i prompt pronti per fase
- `OperatorGuide/01_Primo_Manuale.md` — panoramica delle 6 tappe
- `Projects/PROJECT_BOOTSTRAP.md` — guida rapida creazione progetto
- `OperatorGuide/06_Errori_Comuni.md` — diagnosi degli errori comuni
- `Knowledge/FAQ.md` — domande frequenti
