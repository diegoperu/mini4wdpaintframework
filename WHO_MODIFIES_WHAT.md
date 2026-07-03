# WHO_MODIFIES_WHAT.md — Chi Modifica Cosa

**Mini4WD Manual SDK v2.5.0** · Documento operatore
**Ruoli:** definiti in `OPERATOR_PROFILE.md` · **Dettaglio per file:** `FILE_MATRIX.md`

---

## Tabella principale

| Artefatto | Chi lo modifica | Come | Quando |
|---|---|---|---|
| `PROJECT.yaml` (nel tuo progetto) | **Operatore** | Editor di testo | Setup progetto; correzioni dopo QA FAIL |
| `Projects/{Modello}/{Variante}/Images/` | **Operatore** | Copia file | Setup progetto |
| `Projects/{Modello}/{Variante}/Notes/qa_log.md` | **Operatore** | Editor di testo | Durante QA |
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/content.yaml` | **AI** | Prompt Fase 2 (Text Engine) | Generazione testi |
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml` | **AI / Reviewer** | Prompt QA + conferma | Approvazione e seal |
| `Projects/{Modello}/{Variante}/ApprovedImages/` | **AI** | Prompt Fase 4 (Render) | Rendering |
| `Projects/{Modello}/{Variante}/index.yaml` | **Reviewer / Maintainer** | Editor / prompt | Seal e release |
| `Assets/ApprovedManual/{Modello}/` | **Maintainer** | Copia file + firma | Pubblicazione |
| `Templates/` (master) | **Developer** | Pull request | Release SDK |
| `PromptEngine/` | **Developer** | Pull request + ADR | Release SDK |
| `Core/` | **Developer** | Pull request + ADR obbligatorio | Release SDK |
| `Config/` (incl. LANGUAGE_POLICY) | **Developer** | Pull request | Release SDK |
| `Knowledge/`, `Tests/`, `Docs/` | **Developer** | Pull request | Release SDK |
| `CHANGELOG.md`, `VERSION`, `ReleaseInfo.yaml` | **Maintainer** | Commit di release | Release SDK |
| `UAT/` | **Maintainer** | Nuovo report UAT | Dopo ogni test utente |

---

## Vista per ruolo

### Operatore
Modifica **solo** `Projects/{SuoModello}/`. Non tocca mai framework, template master,
ApprovedText/ApprovedImages (ci pensa l'AI via prompt), Assets.

### AI (in chat)
Scrive `content.yaml`, `text.md` (derivato), `metadata.yaml`, `manifest.yaml`,
`changelog.md`, `notes.md` dei moduli pagina e i render. Non modifica mai `Core/`,
`PROJECT.yaml`, né gli asset già `locked` (Bootstrap Contract, regole
`never_modify_approved_assets` e `never_modify_project_yaml`).

### Reviewer
Approva: imposta `approved/locked` nei `metadata.yaml`, firma i QA log, aggiorna
`Projects/{Modello}/{Variante}/index.yaml`. Non genera contenuti.

### Maintainer
Pubblica: `Assets/ApprovedManual/`, tag di release, CHANGELOG, VERSION, UAT.
Unico che può concedere lo status Approved finale (niente self-approval).

### Developer
Evolve il framework: `Core/`, `Config/`, `PromptEngine/`, `Templates/`, `Tests/`,
`Knowledge/`, `Docs/`. Ogni modifica a `Core/` richiede un ADR in `STYLE_DECISIONS.md`.
