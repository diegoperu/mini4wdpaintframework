# OPERATOR_PROFILE.md — Ruoli e Responsabilità

**Mini4WD Manual SDK v2.5.0**

> L'SDK distingue quattro ruoli umani (più l'AI come esecutore). Una stessa persona può
> coprire più ruoli, ma le responsabilità restano separate: sapere "con quale cappello"
> stai agendo evita modifiche nel posto sbagliato.

---

## Operatore

**Chi è:** chiunque voglia produrre un manuale. Non ha partecipato allo sviluppo
dell'SDK e non deve conoscerne gli inner working.

| Aspetto | Dettaglio |
|---|---|
| **Responsabilità** | Creare il progetto, compilare PROJECT.yaml, fornire le foto, eseguire i prompt fase per fase, far girare i QA, tenere aggiornato qa_log.md |
| **File modificabili** | Solo `Projects/{SuoModello}/` — PROJECT.yaml, Images/, Output/, Notes/ e copie dei template |
| **File vietati** | `Core/`, `Config/`, `PromptEngine/`, `Templates/` (master), `Knowledge/`, `Tests/`, `Assets/`, `ApprovedAssets/` (a mano), progetto `Proto_Emperor/` |
| **Competenze richieste** | Uso base di git (clone), editor di testo, saper compilare uno YAML seguendo i commenti, uso di una chat AI con allegati. **Nessuna competenza di sviluppo.** |
| **Documenti di riferimento** | `START_HERE.md`, `OperatorGuide/`, `WORKFLOW.md`, `FIRST_PROJECT.md` |

## Reviewer

**Chi è:** chi approva contenuti e render. Deve essere diverso da chi ha generato
il contenuto (regola no-self-approval).

| Aspetto | Dettaglio |
|---|---|
| **Responsabilità** | Verificare gli esiti QA, approvare i content.yaml (status `approved`/`locked`), firmare `approved_by`/`approved_date`, validare i render contro QA_SYSTEM.md, aggiornare `Projects/{Modello}/{Variante}/index.yaml` |
| **File modificabili** | `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml` (campi approvazione), `Projects/{Modello}/{Variante}/index.yaml`, qa_log.md |
| **Competenze richieste** | Italiano editoriale, conoscenza di `Tests/ContentValidation.md`, `Tests/TextValidation.md`, `Core/QA_SYSTEM.md` |

## Maintainer

**Chi è:** chi governa il repository e le pubblicazioni.

| Aspetto | Dettaglio |
|---|---|
| **Responsabilità** | Approvazione finale dei manuali (`Assets/ApprovedManual/`), release SDK (VERSION, CHANGELOG, tag), gestione `Assets/ReferenceModels/`, report UAT, revisione pull request |
| **File modificabili** | `CHANGELOG.md`, `VERSION`, `ReleaseInfo.yaml`, `MANIFEST.yaml`, `STATUS.md`, `Assets/ApprovedManual/`, `Assets/ReferenceModels/`, `UAT/` |
| **Competenze richieste** | Git avanzato (tag, release), SemVer, conoscenza completa del workflow |

## Developer

**Chi è:** chi sviluppa il framework stesso.

| Aspetto | Dettaglio |
|---|---|
| **Responsabilità** | Evoluzione di Core/, Config/, PromptEngine/, Templates/, Tests/, Knowledge/, Docs/; ADR in `STYLE_DECISIONS.md` per ogni modifica a Core/; retro-compatibilità (ID P001–P010 e C001–C015 permanenti) |
| **File modificabili** | Tutto il framework, via pull request |
| **Competenze richieste** | Architettura dell'SDK completa, prompt engineering, sistemi di design, processi QA |

## AI (esecutore, non ruolo umano)

Genera testi e render **solo attraverso i prompt ufficiali** ed entro il Bootstrap
Contract (`AI_ENTRYPOINT.md`): mai modificare PROJECT.yaml, mai inventare dati, mai
toccare asset `locked`, tutto il testo editoriale in italiano.

---

## Matrice rapida

| Azione | Operatore | Reviewer | Maintainer | Developer |
|---|:-:|:-:|:-:|:-:|
| Compilare PROJECT.yaml | ✅ | — | — | — |
| Eseguire prompt di generazione | ✅ | — | — | — |
| Approvare/lock di una pagina | — | ✅ | ✅ | — |
| Pubblicare un manuale | — | — | ✅ | — |
| Modificare Core/ o PromptEngine/ | — | — | — | ✅ |
| Rilasciare una versione SDK | — | — | ✅ | ✅ (PR) |
