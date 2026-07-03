# FILE_MATRIX.md — Matrice dei File

**Mini4WD Manual SDK v2.4.1** · Documento operatore

> Per ogni file/cartella del repository: si può modificare? Quando? Chi? In quale fase?
> Ruoli: **Operatore** (usa l'SDK), **Reviewer** (approva), **Maintainer** (governa il repo),
> **Developer** (sviluppa il framework), **AI** (genera contenuti in chat).
> Definizioni: `OPERATOR_PROFILE.md`. Fasi: `WORKFLOW.md`.
>
> Colonna **Runtime**: come il file viene fornito all'AI per runtime.
> `ChatGPT Web: ZIP` = incluso nell'archivio ZIP del framework.
> `ChatGPT Web: Allegato` = caricato separatamente (non dentro il ZIP).
> `ChatGPT Web: In chat` = prodotto dall'AI come testo in chat (da copiare in locale).
> `Claude Code: Diretto` = l'AI accede al file nel repository locale.
> `Claude Code: Nel repo` = l'AI scrive il file direttamente nel repository.

---

## Root

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `START_HERE.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `README.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `AI_ENTRYPOINT.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `BOOTSTRAP.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `SDK_CONTEXT.yaml` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `WORKFLOW.md`, `LIFECYCLE.md`, `FILE_MATRIX.md`, `PROJECT_STRUCTURE.md`, `WHO_MODIFIES_WHAT.md`, `OPERATOR_PROFILE.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `FIRST_PROJECT.md`, `FIRST_RENDER.md`, `FIRST_PDF.md` | NO | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `CHANGELOG.md`, `VERSION`, `ReleaseInfo.yaml`, `MANIFEST.yaml`, `RepositoryManifest.yaml` | NO | Release | Maintainer | Release | ChatGPT: ZIP · Claude: Diretto |
| `STATUS.md`, `ROADMAP.md`, `STYLE_DECISIONS.md` | NO | Release | Maintainer/Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `GPT.md`, `LICENSE` | NO | — | Maintainer | — | ChatGPT: ZIP · Claude: Diretto |

## Core/ — specifica del framework

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Core/*` (tutti) | **NO — mai** | Solo con ADR in STYLE_DECISIONS.md | Developer | — | ChatGPT: ZIP · Claude: Diretto |

## Config/

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Config/LANGUAGE_POLICY.yaml` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Config/sdk.yaml`, `render.yaml`, `pdf.yaml`, `quality.yaml` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |

## PromptEngine/

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `PromptEngine/*.md` | **NO — mai** | Solo release | Developer | — | ChatGPT: ZIP · Claude: Diretto |

L'Operatore li **usa** (li allega in chat o l'AI li legge dal repo), non li modifica.

## Templates/ — master, si copiano

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Templates/*` (i master) | NO | Solo release | Developer | — | ChatGPT: ZIP (estrai solo PROJECT.yaml) · Claude: Diretto |
| Le **copie** in `Projects/{Modello}/` | SÌ | Setup progetto | Operatore | NUOVO PROGETTO | ChatGPT: Allegato · Claude: Diretto |

## Projects/ — il TUO spazio di lavoro

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Projects/{TuoModello}/PROJECT.yaml` | **SÌ** | Setup e correzioni QA | **Operatore** | NUOVO PROGETTO | ChatGPT: **Allegato** · Claude: Diretto |
| `Projects/{TuoModello}/Images/*` | **SÌ** | Setup; render in fase 7 | **Operatore** | NUOVO PROGETTO / RENDERING | ChatGPT: **Allegato** · Claude: Diretto |
| `Projects/{TuoModello}/Output/*` | SÌ | Generazione | Operatore + AI | TESTI / PDF | ChatGPT: In chat · Claude: Nel repo |
| `Projects/{TuoModello}/Notes/*` | SÌ | Sempre | Operatore | Tutte | ChatGPT: Locale (non caricato) · Claude: Diretto |
| `Projects/PROJECT_BOOTSTRAP.md` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Projects/Proto_Emperor/*` | **NO — riferimento sola lettura** | — | Maintainer | — | ChatGPT: ZIP · Claude: Diretto |

## ApprovedAssets/ — CMS, scrive l'AI

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `ApprovedAssets/Text/P00x/content.yaml` | SÌ (via AI) | Generazione testi | **AI** (mai a mano dopo `locked`) | GENERAZIONE TESTI | ChatGPT: **In chat** (copia manuale) · Claude: Nel repo |
| `ApprovedAssets/Text/P00x/metadata.yaml` | SÌ (via AI) | Avanzamento lifecycle | AI / Reviewer | QA / SEAL | ChatGPT: In chat · Claude: Nel repo |
| `ApprovedAssets/Text/P00x/changelog.md` | SÌ (via AI) | Ogni revisione | AI | Tutte | ChatGPT: In chat · Claude: Nel repo |
| `ApprovedAssets/Text/P00x/text.md` | **NO — derivato** | — | AI (auto) | — | ChatGPT: In chat · Claude: Nel repo |
| `ApprovedAssets/Text/P00x/manifest.yaml`, `notes.md`, `README.md` | SÌ (via AI) | Generazione | AI | TESTI | ChatGPT: In chat · Claude: Nel repo |
| `ApprovedAssets/Images/*` | SÌ (via AI) | Rendering | AI | RENDERING | ChatGPT: In chat · Claude: Nel repo |
| `ApprovedAssets/index.yaml` | SÌ | Approvazioni e release | Reviewer/Maintainer | SEAL / RELEASE | ChatGPT: ZIP · Claude: Diretto |

**Regola:** l'Operatore non edita mai a mano i file di `ApprovedAssets/` — le modifiche
passano per i prompt e restano tracciate nei changelog di pagina.

## Assets/

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Assets/DesignSystem/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Assets/ReferenceModels/*` | NO (per l'Operatore) | — | Maintainer | — | ChatGPT: ZIP · Claude: Diretto |
| `Assets/ApprovedManual/{Modello}/` | SÌ | Pubblicazione | Maintainer | GOLDEN PROJECT | ChatGPT: ZIP · Claude: Diretto |
| `Assets/Examples/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |

## Knowledge/ · Tests/ · Docs/ · Build/ · Documentation/

| File | Modificabile? | Quando | Da chi | Fase | Runtime |
|---|---|---|---|---|---|
| `Knowledge/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Tests/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Docs/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Build/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `Documentation/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `OperatorGuide/*` | NO | Release | Developer | — | ChatGPT: ZIP · Claude: Diretto |
| `UAT/*` | SÌ | Dopo ogni test utente | Maintainer | — | ChatGPT: ZIP · Claude: Diretto |

---

## Riassunto per l'Operatore

**Modifichi solo:** `Projects/{TuoModello}/` (PROJECT.yaml, Images/, Output/, Notes/ e
le copie dei template). **Tutto il resto è sola lettura.** L'AI scrive in
`ApprovedAssets/` tramite i prompt; tu non ci metti mano direttamente.

**Con ChatGPT Web:** carica il repository come ZIP + allega separatamente PROJECT.yaml e immagini.
L'AI produce i file in chat — sei tu a salvarli localmente se vuoi conservarli.

**Con Claude Code:** l'AI legge e scrive i file direttamente nel repository locale.
Nessun allegato necessario.
