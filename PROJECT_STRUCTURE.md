# PROJECT_STRUCTURE.md — Struttura del Progetto

**Mini4WD Manual SDK v2.4.1** · Documento operatore

> Questo documento elimina ogni ambiguità su: quali cartelle creare, quali NON creare,
> dove mettere le immagini, dove NON metterle.

---

## Convenzione UNICA per le immagini (v2.4.1)

**Tutte le immagini del tuo progetto vanno in `Projects/{Nome_Modello}/Images/`.**

Questo vale sia per le **foto di riferimento** del modello fisico sia per i **render
approvati**. Non devi creare nulla sotto `Assets/`.

| Posizione | Chi la usa | Cosa contiene |
|---|---|---|
| `Projects/{Modello}/Images/` | **Operatore (TU)** | Foto di riferimento + render del tuo progetto |
| `Assets/ReferenceModels/` | Solo Maintainer | Fotografia dei progetti di riferimento dell'SDK (es. Proto_Emperor). **Non crearci cartelle.** |
| `ApprovedAssets/Images/` | Solo AI (fase Rendering) | Render approvati delle pagine. **Non caricarci foto.** |

> Nota storica: versioni precedenti della documentazione indicavano
> `Assets/ReferenceModels/{Modello}/` come destinazione delle foto di riferimento.
> Da v2.4.1 quella cartella è riservata ai progetti di riferimento mantenuti dall'SDK.
> Per i tuoi progetti usa **sempre e solo** `Projects/{Modello}/Images/`.

---

## Cartelle da creare

Per un nuovo progetto crei **solo questo** (niente altro, in nessun'altra posizione):

```
Projects/{Nome_Modello}/
├── PROJECT.yaml     ← copiato da Templates/PROJECT.yaml e compilato
├── Images/          ← le tue foto di riferimento (+ render quando arrivano)
├── Output/          ← output generati (l'AI/tu salvate qui)
│   ├── raw/         ← output grezzi delle pagine
│   └── pdf/         ← PDF esportati
└── Notes/           ← qa_log.md e appunti
```

Comandi:

```bash
MODEL="Nome_Modello"           # es. "Dash_01_Shadow_Emperor" — underscore, NON trattini
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw" "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
```

**File opzionali** (utili ma non necessari per il bootstrap): `PROJECT.md`,
`CHECKLIST.md`, `COLOR_SCHEME.yaml`, `PDF_CONFIG.yaml`, `README.md` — tutti copiati
da `Templates/`. Il set minimo per partire è: `PROJECT.yaml` + `Images/` + `Output/` + `Notes/`.

---

## Nome della cartella progetto

Regole (`Core/NAMING_CONVENTION.md`):

1. Nome ufficiale Tamiya, grafia esatta
2. Spazi → underscore: `Proto Emperor` → `Proto_Emperor`
3. **Niente trattini nel nome cartella** (`Dash-01_...` ✗ → `Dash_01_...` ✓)
4. Maiuscole conservate, niente abbreviazioni
5. Il trattino si usa solo nel `modelSlug` dentro PROJECT.yaml: `proto-emperor`

| Nome modello | Cartella ✓ | Cartella ✗ |
|---|---|---|
| Proto Emperor | `Proto_Emperor/` | `proto-emperor/`, `ProtoEmperor/` |
| Dash 01 Shadow Emperor | `Dash_01_Shadow_Emperor/` | `Dash-01_Shadow_Emperor/` |

---

## Cartelle da NON creare / NON toccare

| Cartella | Perché non toccarla |
|---|---|
| `Assets/ReferenceModels/{TuoModello}/` | NON crearla: riservata ai riferimenti SDK |
| `ApprovedAssets/Text/P00x/` | Esistono già: l'AI ci scrive i content.yaml |
| `ApprovedAssets/Images/` | Ci scrive l'AI in fase rendering |
| `Core/`, `Config/`, `PromptEngine/`, `Knowledge/`, `Tests/` | Framework — sola lettura |
| `Templates/` | Master: si copia, non si modifica |
| `Assets/ApprovedManual/{TuoModello}/` | La crea il Maintainer alla pubblicazione |

---

## Immagini: requisiti minimi

In `Projects/{Modello}/Images/` servono almeno:

| File | Contenuto | Obbligatoria |
|---|---|---|
| `ref_front.jpg` | Vista frontale | Sì |
| `ref_side_left.jpg` | Lato sinistro | Sì |
| `ref_side_right.jpg` | Lato destro | Sì |
| `ref_top.jpg` | Vista dall'alto | Sì |
| `ref_3q_front.jpg` | 3/4 frontale-sinistra (per la copertina) | Sì |
| `ref_rear.jpg` | Vista posteriore | Consigliata |
| `ref_detail_*.jpg` | Dettagli | Se servono |

Requisiti qualità (`Config/render.yaml`): min 2048px sul lato lungo, sfondo bianco
o neutro, fuoco nitido.

I percorsi in `PROJECT.yaml → paths:` sono **relativi alla cartella progetto**
(quindi `Images/ref_front.jpg`, non `Projects/.../Images/ref_front.jpg`).

---

## Riferimenti

- Tutorial primo progetto: `FIRST_PROJECT.md`
- Chi modifica cosa: `WHO_MODIFIES_WHAT.md` e `FILE_MATRIX.md`
- Progetto di esempio (sola lettura): `Projects/Proto_Emperor/`
