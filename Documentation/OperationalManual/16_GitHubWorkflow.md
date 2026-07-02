# Capitolo 16 — GitHub Workflow

Questo capitolo descrive come contribuire al repository del Mini4WD Manual SDK: come clonarlo, come proporre modifiche e quali vincoli impone la licenza. Non esiste alcuna pipeline di integrazione continua in questo repository — il flusso descritto qui è interamente manuale.

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| README | `README.md` (§ Quick Start, § Contributing, § License) | Source of Truth |
| Licenza | `LICENSE` | Termini legali vincolanti |
| SDK Context | `SDK_CONTEXT.yaml` (sezione `repository`) | URL e branch di default |

---

## 1. Nessuna pipeline CI/CD

Il repository **non contiene** una cartella `.github/workflows/`. Non esiste automazione GitHub Actions che validi pull request, esegua i test suite di `Tests/`, o blocchi merge. Ogni verifica — QA, coerenza terminologica, `Tests/FrameworkIntegrity.md` — è **eseguita manualmente** dal contributor prima di aprire la PR e dal maintainer prima di accettarla.

> 📝 **Nota:** se in futuro verrà aggiunta automazione CI, questo capitolo va aggiornato per prima cosa — vedi `CHANGE_IMPACT.md` in `Validation/`.

## 2. Clonare il repository

```bash
git clone https://github.com/diegoperu/mini4wdpaintframework.git
cd mini4wdpaintframework
```

Il branch di default è `main` (`SDK_CONTEXT.yaml → repository.default_branch`). Le release sono taggate e pubblicate su `https://github.com/diegoperu/mini4wdpaintframework/releases`.

## 3. Prima di aprire una pull request

`README.md § Contributing` elenca cinque passaggi obbligatori, nell'ordine:

1. Leggere `Core/DOCUMENTATION_STYLE.md` e allineare la voce editoriale del contributo a quella esistente (seconda persona, presente indicativo per le specifiche, RFC 2119 per i requisiti — vedi Capitolo 01 per il richiamo completo)
2. Se la modifica tocca `Core/`, aprire un Architecture Decision Record (ADR) in `STYLE_DECISIONS.md` — `Core/` è la Source of Truth assoluta dello SDK (G09), quindi ogni cambiamento richiede una motivazione tracciata
3. Aggiornare `CHANGELOG.md` sotto la sezione `[Unreleased]`
4. Verificare che la modifica superi le suite in `Tests/` (9 suite — vedi Capitolo 11)
5. Verificare che la modifica soddisfi i criteri di `Core/DEFINITION_OF_DONE.md`

Saltare uno di questi passaggi non blocca tecnicamente l'apertura della PR (nessuna automazione lo impedisce), ma è motivo di rifiuto da parte del maintainer in fase di review manuale.

## 4. Issue e roadmap

Le issue e le richieste di funzionalità sono tracciate su GitHub. Le richieste di funzionalità vanno etichettate con il label `roadmap`. Prima di aprire una richiesta, consultare `ROADMAP.md` (Capitolo 14) per verificare che non sia già pianificata — evita duplicati e dà al maintainer contesto su cosa è già stato deciso.

## 5. Implicazioni della licenza per i contributor

Il progetto è distribuito sotto **Apache License 2.0** (`LICENSE`, Copyright 2024 Mini4WD Manual SDK Contributors). Punti rilevanti per chi contribuisce:

| Clausola | Implicazione pratica |
|----------|------------------------|
| Sezione 2 — Grant of Copyright License | Ogni contributor concede una licenza di copyright perpetua e irrevocabile sul proprio contributo |
| Sezione 3 — Grant of Patent License | Ogni contributor concede anche una licenza di brevetto sui claim necessariamente infranti dal proprio contributo |
| Sezione 4(b) | Se modifichi un file esistente, il file deve riportare una notifica visibile della modifica |
| Sezione 5 — Submission of Contributions | Salvo dichiarazione esplicita contraria, ogni contributo inviato è automaticamente sotto i termini della stessa licenza — non serve firmare un CLA separato |
| Sezione 7 — Disclaimer of Warranty | Il codice/i documenti sono forniti "AS IS", senza garanzie |

> ⚠️ **Warning:** la Sezione 6 (Trademarks) non concede il diritto di usare nomi o marchi del progetto per scopi diversi dalla descrizione dell'origine del lavoro. "Mini 4WD" resta inoltre un marchio registrato di Tamiya Inc. — il progetto dichiara esplicitamente di non essere affiliato (`README.md`, nota finale).

## Vedi anche

- Capitolo 01 — Introduction (per lo stile editoriale richiesto nei contributi)
- Capitolo 11 — QA (per le suite di test da eseguire prima della PR)
- Capitolo 14 — Roadmap (per verificare se una feature è già pianificata)
- Capitolo 15 — Versioning (per `CHANGELOG.md` e ADR)
