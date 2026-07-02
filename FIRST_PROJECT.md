# FIRST_PROJECT.md — Tutorial: dal Clone al Bootstrap OK

**Mini4WD Manual SDK v2.4.1** · Tutorial operatore · Tempo: ~30 minuti

> Tutorial completo con esempi reali: dalla creazione della cartella progetto fino al
> Bootstrap approvato. Esempio usato: **Dash 01 Shadow Emperor**, schema "Shadow Black".
> Prerequisito: aver letto `START_HERE.md`.

---

## PASSO 1 — Clona il repository

```bash
git clone https://github.com/diegoperu/mini4wdpaintframework.git
cd mini4wdpaintframework
```

## PASSO 2 — Crea la cartella progetto

Il nome cartella usa gli **underscore** (mai trattini — vedi `PROJECT_STRUCTURE.md`):

```bash
MODEL="Dash_01_Shadow_Emperor"
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw" "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"
```

Risultato:

```
Projects/Dash_01_Shadow_Emperor/
├── Images/
├── Output/
│   ├── raw/
│   └── pdf/
└── Notes/
```

Non creare nulla sotto `Assets/` o `ApprovedAssets/` — non serve.

## PASSO 3 — Copia e compila PROJECT.yaml

```bash
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
```

Apri `Projects/Dash_01_Shadow_Emperor/PROJECT.yaml` e compila **tutti i campi REQUIRED**
(ogni campo ha un commento che lo spiega). Esempio reale:

```yaml
sdk_version: "2.4.1"

project:
  modelName: "Dash 01 Shadow Emperor"     # nome ufficiale Tamiya, con gli spazi
  modelSlug: "dash-01-shadow-emperor"     # kebab-case: qui SÌ i trattini
  seriesName: "Dash! Yonkuro"
  year: "2026"
  language: "it"
  version: "1.0.0"
  author: "Diego"
  createdAt: "2026-07-02"
  updatedAt: "2026-07-02"

paintScheme:
  name: "Shadow Black"
  colors:
    - id: "PC001"                          # sempre PC001, PC002… (mai C001)
      name: "Base carrozzeria"
      paintBrand: "Tamiya"
      paintCode: "TS-40"
      paintName: "Metallic Black"
      finish: "metallic"                   # valore chiave YAML: inglese, va bene così
    - id: "PC002"
      name: "Dettagli"
      paintBrand: "Tamiya"
      paintCode: "TS-83"
      paintName: "Metallic Silver"
      finish: "metallic"
```

Regole d'oro:

1. **Non inventare codici vernice.** Solo codici reali del produttore.
2. **Dato mancante = `TODO:`** — mai un valore inventato.
3. I valori delle **chiavi YAML** (`finish: metallic`, `technique: spray-can`) sono in
   inglese da schema: è corretto, non è una violazione della language policy.
   Il testo **editoriale** (che finirà sulle pagine) sarà in italiano.
4. I percorsi in `paths:` sono relativi alla cartella progetto (`Images/...`).

## PASSO 4 — Inserisci le immagini

Copia le foto del modello fisico in `Projects/Dash_01_Shadow_Emperor/Images/`:

```
Images/
├── ref_front.jpg          # obbligatoria
├── ref_side_left.jpg      # obbligatoria
├── ref_side_right.jpg     # obbligatoria
├── ref_top.jpg            # obbligatoria
├── ref_3q_front.jpg       # obbligatoria (servirà per la copertina)
└── ref_rear.jpg           # consigliata
```

Requisiti: min 2048px lato lungo, sfondo bianco/neutro, fuoco nitido.

**Questa è l'unica posizione corretta.** Non usare `Assets/ReferenceModels/` (riservata
al Maintainer per i progetti di riferimento SDK).

## PASSO 5 — Verifica pre-bootstrap

- [ ] `Projects/{Modello}/PROJECT.yaml` esiste e non ha campi REQUIRED vuoti (o sono `TODO:` motivati)
- [ ] Almeno 5 foto in `Images/` (front, 2 lati, top, 3/4)
- [ ] Nome cartella con underscore, `modelSlug` in kebab-case
- [ ] Non hai modificato nessun file fuori da `Projects/{Modello}/`

## PASSO 6 — Bootstrap (prima chat AI)

1. Apri una **nuova chat** con il tuo modello AI (ChatGPT / Claude / Gemini).
2. Apri `Docs/AI_BOOTSTRAP_PROMPT.md` → **Fase 1 — Bootstrap**.
3. Allega i file nell'ordine indicato (SDK_CONTEXT.yaml, BOOTSTRAP.md, i Core/ elencati,
   il tuo PROJECT.yaml, le tue foto).
4. Incolla il prompt della Fase 1 e invia.

## PASSO 7 — Leggi e approva il Bootstrap Report

L'AI risponde con un **Bootstrap Report** (formato in `AI_ENTRYPOINT.md`): versione SDK,
documenti caricati, dati del tuo progetto, stato delle pagine, regole attive.

Controlla:

- [ ] Nome modello e schema colori corretti (i TUOI dati, non quelli di Proto Emperor)
- [ ] Tutte le pagine P001–P010 in stato `draft` (normale per un progetto nuovo)
- [ ] Nessun documento mancante segnalato

Se tutto torna, rispondi:

```
Bootstrap approvato. Inizia dalla pagina P001.
```

**→ Bootstrap OK raggiunto.** Da qui in poi segui `WORKFLOW.md` (stato 4: Generazione
Testi) e `OperatorGuide/01_Primo_Manuale.md`.

---

## Se qualcosa va storto

| Sintomo | Causa probabile | Rimedio |
|---|---|---|
| Il report cita "Proto Emperor" invece del tuo modello | PROJECT.yaml sbagliato o non allegato | Riallegare il TUO PROJECT.yaml, rilanciare il prompt |
| L'AI chiede file che non trovi | Percorso citato da doc legacy | I percorsi validi sono quelli di `PROJECT_STRUCTURE.md` |
| Validation FAIL su P001 appena dopo il bootstrap | Stai validando il template vuoto, non un contenuto generato | Prima genera P001 (Fase 2), poi valida (Fase 3). Vedi `OperatorGuide/06_Errori_Comuni.md` |
