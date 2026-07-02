# FILE_MATRIX.md — Matrice dei File

**Mini4WD Manual SDK v2.4.1** · Documento operatore

> Per ogni file/cartella del repository: si può modificare? Quando? Chi? In quale fase?
> Ruoli: **Operatore** (usa l'SDK), **Reviewer** (approva), **Maintainer** (governa il repo),
> **Developer** (sviluppa il framework), **AI** (genera contenuti in chat).
> Definizioni: `OPERATOR_PROFILE.md`. Fasi: `WORKFLOW.md`.

---

## Root

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `START_HERE.md` | NO | Solo release | Developer | — |
| `README.md` | NO | Solo release | Developer | — |
| `AI_ENTRYPOINT.md` | NO | Solo release | Developer | — |
| `BOOTSTRAP.md` | NO | Solo release | Developer | — |
| `SDK_CONTEXT.yaml` | NO | Solo release | Developer | — |
| `WORKFLOW.md`, `LIFECYCLE.md`, `FILE_MATRIX.md`, `PROJECT_STRUCTURE.md`, `WHO_MODIFIES_WHAT.md`, `OPERATOR_PROFILE.md` | NO | Solo release | Developer | — |
| `FIRST_PROJECT.md`, `FIRST_RENDER.md`, `FIRST_PDF.md` | NO | Solo release | Developer | — |
| `CHANGELOG.md`, `VERSION`, `ReleaseInfo.yaml`, `MANIFEST.yaml`, `RepositoryManifest.yaml` | NO | Release | Maintainer | Release |
| `STATUS.md`, `ROADMAP.md`, `STYLE_DECISIONS.md` | NO | Release | Maintainer/Developer | — |
| `GPT.md`, `LICENSE` | NO | — | Maintainer | — |

## Core/ — specifica del framework

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Core/*` (tutti) | **NO — mai** | Solo con ADR in STYLE_DECISIONS.md | Developer | — |

## Config/

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Config/LANGUAGE_POLICY.yaml` | NO | Release | Developer | — |
| `Config/sdk.yaml`, `render.yaml`, `pdf.yaml`, `quality.yaml` | NO | Release | Developer | — |

## PromptEngine/

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `PromptEngine/*.md` | **NO — mai** | Solo release | Developer | — |

L'Operatore li **usa** (li allega in chat), non li modifica.

## Templates/ — master, si copiano

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Templates/*` (i master) | NO | Solo release | Developer | — |
| Le **copie** in `Projects/{Modello}/` | SÌ | Setup progetto | Operatore | NUOVO PROGETTO |

## Projects/ — il TUO spazio di lavoro

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Projects/{TuoModello}/PROJECT.yaml` | **SÌ** | Setup e correzioni QA | **Operatore** | NUOVO PROGETTO |
| `Projects/{TuoModello}/Images/*` | **SÌ** | Setup; render in fase 7 | **Operatore** | NUOVO PROGETTO / RENDERING |
| `Projects/{TuoModello}/Output/*` | SÌ | Generazione | Operatore + AI | TESTI / PDF |
| `Projects/{TuoModello}/Notes/*` | SÌ | Sempre | Operatore | Tutte |
| `Projects/PROJECT_BOOTSTRAP.md` | NO | Release | Developer | — |
| `Projects/Proto_Emperor/*` | **NO — riferimento sola lettura** | — | Maintainer | — |

## ApprovedAssets/ — CMS, scrive l'AI

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `ApprovedAssets/Text/P00x/content.yaml` | SÌ (via AI) | Generazione testi | **AI** (mai a mano dopo `locked`) | GENERAZIONE TESTI |
| `ApprovedAssets/Text/P00x/metadata.yaml` | SÌ (via AI) | Avanzamento lifecycle | AI / Reviewer | QA / SEAL |
| `ApprovedAssets/Text/P00x/changelog.md` | SÌ (via AI) | Ogni revisione | AI | Tutte |
| `ApprovedAssets/Text/P00x/text.md` | **NO — derivato** | — | AI (auto) | — |
| `ApprovedAssets/Text/P00x/manifest.yaml`, `notes.md`, `README.md` | SÌ (via AI) | Generazione | AI | TESTI |
| `ApprovedAssets/Images/*` | SÌ (via AI) | Rendering | AI | RENDERING |
| `ApprovedAssets/index.yaml` | SÌ | Approvazioni e release | Reviewer/Maintainer | SEAL / RELEASE |

**Regola:** l'Operatore non edita mai a mano i file di `ApprovedAssets/` — le modifiche
passano per i prompt e restano tracciate nei changelog di pagina.

## Assets/

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Assets/DesignSystem/*` | NO | Release | Developer | — |
| `Assets/ReferenceModels/*` | NO (per l'Operatore) | — | Maintainer | — |
| `Assets/ApprovedManual/{Modello}/` | SÌ | Pubblicazione | Maintainer | GOLDEN PROJECT |
| `Assets/Examples/*` | NO | Release | Developer | — |

## Knowledge/ · Tests/ · Docs/ · Build/ · Documentation/

| File | Modificabile? | Quando | Da chi | Fase |
|---|---|---|---|---|
| `Knowledge/*` | NO | Release | Developer | — |
| `Tests/*` | NO | Release | Developer | — |
| `Docs/*` | NO | Release | Developer | — |
| `Build/*` | NO | Release | Developer | — |
| `Documentation/*` | NO | Release | Developer | — |
| `OperatorGuide/*` | NO | Release | Developer | — |
| `UAT/*` | SÌ | Dopo ogni test utente | Maintainer | — |

---

## Riassunto per l'Operatore

**Modifichi solo:** `Projects/{TuoModello}/` (PROJECT.yaml, Images/, Output/, Notes/ e
le copie dei template). **Tutto il resto è sola lettura.** L'AI scrive in
`ApprovedAssets/` tramite i prompt; tu non ci metti mano direttamente.
