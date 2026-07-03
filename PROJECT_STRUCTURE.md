# PROJECT_STRUCTURE.md — Struttura del Progetto

**Mini4WD Manual SDK v2.5.0** · Documento operatore

> Questo documento elimina ogni ambiguità su: quali cartelle creare, quali NON creare,
> dove mettere le immagini, dove NON metterle.

---

## Struttura progetto v2.5.0

Ogni progetto ha **due livelli**: modello e variante colore.

```
Projects/{Nome_Modello}/{Nome_Variante}/
```

Esempi:
```
Projects/Dash_01_Shadow_Emperor/Shadow_Black/
Projects/Magnum_Saber_Premium/Cotton_Candy_Drift/
Projects/Proto_Emperor/Violet_Phantom/
Projects/Proto_Emperor/Midnight_Blue/        ← stessa auto, variante diversa
```

Il `{Nome_Variante}` deriva da `paintScheme.slug` in PROJECT.yaml (kebab-case → PascalCase_Underscore):
`cotton-candy-drift` → cartella `Cotton_Candy_Drift`.

---

## Convenzione UNICA per le immagini (v2.5.0)

**Tutte le immagini del tuo progetto vanno in `Projects/{Nome_Modello}/{Nome_Variante}/Images/`.**

| Posizione | Chi la usa | Cosa contiene |
|---|---|---|
| `Projects/{Modello}/{Variante}/Images/` | **Operatore (TU)** | Foto di riferimento del modello fisico |
| `Projects/{Modello}/{Variante}/ApprovedImages/` | Solo AI (Rendering) | Render delle pagine generati dall'AI |
| `Assets/ReferenceModels/` | Solo Maintainer | Fotografia dei progetti di riferimento SDK. **Non crearci cartelle.** |

---

## Cartelle da creare

Per un nuovo progetto crei **solo questo** (niente altro, in nessun'altra posizione):

```
Projects/{Nome_Modello}/{Nome_Variante}/
├── PROJECT.yaml       ← copiato da Templates/PROJECT.yaml e compilato
├── Images/            ← le tue foto di riferimento
├── Output/            ← output generati
│   ├── raw/
│   └── pdf/
├── Notes/             ← qa_log.md e appunti
├── ApprovedText/      ← creata dall'AI (generazione testi)
│   ├── P001/ … P010/
│   │   ├── content.yaml
│   │   ├── metadata.yaml
│   │   ├── changelog.md
│   │   └── ...
└── ApprovedImages/    ← creata dall'AI (rendering)
    ├── P001/ … P010/
```

Comandi:

```bash
MODEL="Dash_01_Shadow_Emperor"   # underscore, NON trattini
VARIANT="Shadow_Black"           # da paintScheme.slug convertito
mkdir -p "Projects/${MODEL}/${VARIANT}/Images"
mkdir -p "Projects/${MODEL}/${VARIANT}/Output/raw" "Projects/${MODEL}/${VARIANT}/Output/pdf"
mkdir -p "Projects/${MODEL}/${VARIANT}/Notes"
mkdir -p "Projects/${MODEL}/${VARIANT}/ApprovedText"
mkdir -p "Projects/${MODEL}/${VARIANT}/ApprovedImages"
cp Templates/PROJECT.yaml "Projects/${MODEL}/${VARIANT}/PROJECT.yaml"
```

`ApprovedText/` e `ApprovedImages/` vengono riempite dall'AI — le cartelle esistono
già se le hai create, oppure l'AI le crea in automatico (Claude Code).

**Set minimo per il bootstrap:** `PROJECT.yaml` + `Images/` + `Output/` + `Notes/`.

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
| `Core/`, `Config/`, `PromptEngine/`, `Knowledge/`, `Tests/` | Framework — sola lettura |
| `Templates/` | Master: si copia, non si modifica |
| `Assets/ApprovedManual/` | La gestisce il Maintainer alla pubblicazione |
| `ApprovedAssets/` | Deprecata in v2.5.0 — non usare |

---

## Immagini: requisiti minimi

In `Projects/{Modello}/{Variante}/Images/` servono almeno:

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
- Progetto di esempio (sola lettura): `Projects/Proto_Emperor/Violet_Phantom/`
