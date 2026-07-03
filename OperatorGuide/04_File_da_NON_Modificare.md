# 04 — File da NON Modificare

**OperatorGuide · Mini4WD Manual SDK v2.5.0**

> Tutto ciò che NON devi toccare, e perché. In caso di dubbio: se non è dentro
> `Projects/{TuoModello}/`, non si tocca.

---

## Sola lettura assoluta

| Cartella/File | Cos'è | Perché non si tocca |
|---|---|---|
| `Core/` | La specifica del framework | È la fonte di verità assoluta: una modifica cambia il comportamento di TUTTI i manuali. Solo Developer, con ADR. |
| `PromptEngine/` | I prompt ufficiali per pagina | Sono calibrati sul framework. Si allegano in chat così come sono. |
| `Config/` | Configurazione globale (lingua, QA, render, PDF) | Modificarla altera i validatori per tutti. |
| `Templates/` | I master dei template | Si COPIANO nel progetto; il master resta intatto per i prossimi progetti. |
| `Knowledge/` | Base di conoscenza tecnica/editoriale | Alimenta il Text Engine: modifiche = testi incoerenti. |
| `Tests/` | Le suite di validazione | Se un test fallisce, si corregge il CONTENUTO, mai il test. |
| `Docs/`, `Documentation/`, `OperatorGuide/`, `Build/` | Documentazione | Manutenuta a ogni release. |
| `Assets/DesignSystem/` | Token e design system | I valori visivi sono la firma dell'SDK. |
| `Assets/ReferenceModels/` | Riferimenti dei progetti SDK | Riservata al Maintainer. Le TUE foto vanno in `Projects/{Modello}/Images/`. |
| `Projects/Proto_Emperor/` | Progetto di riferimento | Serve intatto come esempio. Copiane la struttura, non modificarlo. |
| Root: `AI_ENTRYPOINT.md`, `BOOTSTRAP.md`, `SDK_CONTEXT.yaml`, `VERSION`, `CHANGELOG.md`, `MANIFEST.yaml`, ecc. | Identità e stato dell'SDK | Solo Maintainer/Developer a release. |

## Da non modificare A MANO (ci pensa l'AI via prompt)

| Cartella/File | Perché |
|---|---|
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/*` | Ogni modifica deve passare dal Text Engine ed essere tracciata nel changelog di pagina. Un edit a mano rompe la tracciabilità e invalida il QA. |
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/text.md` | È DERIVATO da content.yaml: qualsiasi modifica va fatta su content.yaml (via prompt), mai qui. |
| `Projects/{Modello}/{Variante}/index.yaml` | Registro globale: lo aggiornano Reviewer/Maintainer nelle fasi di seal e release. |
| Pagine con `status: locked` | Sigillate. Riaprire = riga di changelog + ritorno a `review` (vedi `../LIFECYCLE.md`). |

## I 3 errori di modifica più gravi

1. **"Il validatore segnala errore su un termine, lo tolgo dal test"** → No: il test
   è legge. Se il termine è legittimo (codice vernice, nome commerciale) è già
   whitelistato in `Config/LANGUAGE_POLICY.yaml §exceptions`; se il FAIL persiste,
   il problema è nel contenuto o è un bug da segnalare al Maintainer.
2. **"Correggo il refuso direttamente in text.md"** → No: text.md è derivato; al
   prossimo ciclo la correzione sparisce. Si corregge content.yaml via prompt.
3. **"Aggiungo il mio modello in Assets/ReferenceModels/"** → No: quella cartella è
   dell'SDK. Le tue foto stanno in `Projects/{TuoModello}/Images/`.
