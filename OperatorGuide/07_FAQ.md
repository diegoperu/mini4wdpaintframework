# 07 — FAQ Operatore

**OperatorGuide · Mini4WD Manual SDK v2.5.0**

> Domande frequenti sull'USO dell'SDK. Per le FAQ tecniche di verniciatura:
> `Knowledge/FAQ.md`.

---

**D: Devo capire come funziona il framework per usarlo?**
R: No. Devi sapere: cosa fare, quando, quali file toccare, quale prompt usare, quando
aprire una nuova chat. È tutto in `START_HERE.md` + `OperatorGuide/`.

**D: Quale modello AI serve?**
R: ChatGPT o Claude, con allegati file e contesto ampio (consigliato 100K+ token).
I prompt sono model-agnostic. Gemini è supportato **solo per la Fase 4** (generazione
di una singola illustrazione) — fallito su UAT-002 per il vecchio scope whole-page,
superato su UAT-004 nel nuovo scope ristretto. Fase 1-3 (testi) non verificate su
Gemini. Vedi `UAT/UAT-002.md`, `UAT/UAT-004.md` e `Docs/RUNTIMES.md`.

**D: Dove metto le foto del modello?**
R: `Projects/{TuoModello}/Images/`. Sempre e solo lì. (v2.4.1 — convenzione unica.)

**D: Perché il validatore non deve bocciare "Chrome Silver" o "TS-37"?**
R: Sono nome commerciale e codice prodotto: language-neutral per
`Config/LANGUAGE_POLICY.yaml §exceptions`. La regola "solo italiano" vale per il testo
editoriale, non per nomi propri, codici e chiavi YAML. Vedi `06_Errori_Comuni.md §E02`.

**D: Ho un FAIL in QA. Modifico il test?**
R: Mai. Si corregge il contenuto (o PROJECT.yaml se il dato di origine è sbagliato) e
si rivalida. I test si modificano solo a livello di release SDK.

**D: Posso generare tutte le 10 pagine con un solo prompt?**
R: No. Una pagina alla volta: genera → QA → seal. È l'unico modo per tenere la qualità
sotto controllo.

**D: Quando apro una nuova chat?**
R: A ogni cambio di motore: testi (chat 1) → rendering (chat 2) → PDF (chat 3). E
quando una chat degenera (Prompt F — Continuità). Tabella in `02_Workflow.md`.

**D: L'AI mi chiede un dato che non ho. Che faccio?**
R: `TODO:`. Mai inventare. Poi recuperi il dato, aggiorni PROJECT.yaml e rigeneri la
pagina interessata.

**D: Posso saltare il rendering di P009?**
R: P009 (Variante Premium) esiste solo se `premiumVariant.enabled: true` in
PROJECT.yaml. Se è false, il manuale va P008 → P010 (9 pagine): non è un errore.

**D: Ho trovato un refuso in una pagina già locked.**
R: La pagina si riapre formalmente: riga in `changelog.md`, correzione via Text Engine,
nuovo QA, nuovo seal, nuovo render. Vedi `LIFECYCLE.md`. Mai editare a mano.

**D: text.md e content.yaml dicono cose diverse. Quale vale?**
R: `content.yaml`, sempre (Golden Rule G02). `text.md` è derivato: se divergono, si
rigenera text.md da content.yaml.

**D: Posso usare Proto_Emperor come base e modificarlo?**
R: Puoi copiarne la struttura e i formati, ma la cartella `Projects/Proto_Emperor/` è
sola lettura: è il riferimento per tutti.

**D: Il Bootstrap Report mostra pagine "locked" che non ho mai generato.**
R: Anomalia: in un progetto nuovo tutte le pagine sono `draft`. Verifica di aver
allegato il TUO PROJECT.yaml e che l'AI stia leggendo
`Projects/{Modello}/{Variante}/ApprovedText/` del TUO progetto, non di un altro (dalla
v2.5.0 ogni progetto ha la propria cartella isolata, quindi questo non dovrebbe più
capitare per contaminazione tra progetti). In dubbio: chiedi al Maintainer.

**D: Chi approva il manuale finale?**
R: Solo il Maintainer (no self-approval). Tu consegni PDF + qa_log; la pubblicazione
in `Assets/ApprovedManual/` non è self-service.
