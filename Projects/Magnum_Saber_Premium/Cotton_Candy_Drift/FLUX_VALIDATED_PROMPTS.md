# Prompt FLUX.2 validati — Cotton Candy Drift

> Generato manualmente durante sessione di prompt-engineering iterativo (2026-07-16).
> Non sovrascritto automaticamente da `render_page.py` (a differenza di `MISSING_IMAGES_PROMPT.md`).
> Contiene SOLO i prompt che hanno prodotto un'immagine comparabile (o migliore) rispetto al
> riferimento approvato in `Build/ImageBackups/Cotton_Candy_Drift_pre-flux2_20260716_094508/`.
> Comando: `comfy.sh "<prompt>" -m flux2 -i <reference> -o <output>`

## Problema riscorrente nel batch flux2 iniziale (round 1, tutte 16 immagini)
- Leak testo/loghi: nonostante l'istruzione "nessun testo/logo", il modello riproduceva
  scritte "MAGNUM SABER"/kanji dal box-art reference su viste ad ampio campo (cover, ortogonali).
  Fix: istruzione "REGOLA ASSOLUTA SUL TESTO" ripetuta ed esplicita, con elenco dei testi specifici
  da ignorare dalla foto reference.
- Colore cerchi/telaio incoerente tra generazioni (giallo/verde/rosa/argento a caso) — lo schema
  colori originale menzionava Silver Leaf solo per "telaio e cover motore", non esplicitamente per
  i cerchi nel prompt cover/ortogonali (anche se `PROJECT.yaml` D003/PC005 lo specifica chiaramente:
  cerchi = Silver Leaf #C8C8C8). Fix: riga esplicita "Cerchi ruote: Silver Leaf metallizzato, NON
  rosa NON gialli NON verdi" in ogni prompt.

## P001 — cover (slot: cover)
**File:** `Images/cover_3q.png`
**Reference input:** `Images/ref_3q_front.jpg`
**Esito:** comparabile/migliore della baseline pre-flux — zero testo/loghi, cerchi silver coerenti
col telaio (più fedele allo spec PROJECT.yaml D003 della baseline stessa, che li aveva rosa).

```
Genera SOLO un'illustrazione fotorealistica del modellino Mini4WD -- copertina, vista 3/4 anteriore-sinistra, illuminazione studio neutra, sfondo bianco puro, isolato.

REGOLA ASSOLUTA SUL TESTO: il modellino finito NON ha ALCUNA scritta, lettera, numero, kanji, badge o logo su nessuna superficie -- niente "MAGNUM", niente "SABER", niente kanji, niente numero di gara, niente adesivi/decal di alcun tipo. La foto di riferimento allegata mostra la livrea box-art stock (con scritte e decal) SOLO per la sagoma fisica -- ignora completamente testo, kanji, badge e numero di gara della foto reference. Ripeti: zero testo leggibile in tutta l'immagine.

Forma fisica (sagoma, proporzioni, componenti meccanici, alettone, prese d'aria, cockpit) il piu' fedele possibile alla foto di riferimento. Colori e livrea NON derivano dalla foto di riferimento (e' box-art stock con schema diverso) -- usa SOLO lo schema colori sotto, ripitturando ogni superficie in tinta unita secondo le zone indicate. Non aggiungere fiamme, strisce o grafiche assenti dallo schema.

Schema colori (Cotton Candy Drift), tinta unita per zona, nessuna sfumatura/gradiente tra colori diversi:
- Light Blue (#8FD3E8, lucido) -- colore dominante di carrozzeria/cofano/fiancate/alettone principale.
- Pink (#F4879E, lucido) -- pannelli secondari della cowling, punta dell'alettone.
- Black (#0A0A0A, lucido) -- abitacolo/cockpit, cornice interna, accento su linee di cintura.
- Yellow (#F5D300, lucido) -- SOLO piccoli accenti puntuali (fari), area minima.
- Cerchi ruote: Silver Leaf metallizzato (#C8C8C8), tinta unita, NON rosa NON gialli NON verdi -- coordinati col telaio.
- Telaio/chassis visibile: Silver Leaf metallizzato (#C8C8C8) con dettagli Gun Metal (#4B4E52) scuro su componenti meccanici del motore.

Stile fotografico: product photography, luce studio morbida, ombra leggera sotto il modello, sfondo bianco puro senza elementi di scena. Nessuna cornice, nessun testo overlay, nessuna UI.
```

## P002 — vista ortogonale frontale (slot: front)
**File:** `Images/P002_front.png`
**Reference input:** `.flux_crops/ref_front_crop.jpg` (NON `Images/ref_front.jpg` diretto — vedi sotto)
**Esito:** v2 (istruzione descrittiva/rewrite, come cover/side/top) aveva 2 difetti riscontrati
dall'utente: inquadratura troppo poco zoomata rispetto al reference, e ruote/gomme fuori dalla
sagoma della carrozzeria invece che "tucked in" sotto i parafanghi. v4 con approccio "direct edit"
risolve entrambi.

**Metodo "direct edit" (usare quando l'approccio rewrite-descrittivo droppa geometria/proporzioni):**
1. Pre-crop del reference con imagemagick per matchare lo zoom/framing del target approvato
   (calcolare bbox del soggetto nell'immagine di backup approvata, applicare lo stesso fill-ratio
   al crop del reference) — non fidarsi di un'istruzione testuale di framing, il modello non la
   segue con precisione sui bordi immagine.
2. Prompt minimale "mantieni ESATTAMENTE inquadratura/posa/proporzioni, modifica SOLO i colori" con
   mappatura colore-per-colore esplicita (blu attuale -> hex X, bianco attuale -> hex X, ecc.),
   invece della normale istruzione "ridipingi secondo lo schema colori" generica. Il rewrite
   descrittivo da' al modello troppa liberta' di reinterpretare la geometria (specialmente sulle
   viste ortogonali sintetizzate, dove il modello non ha un "davanti reale" da rispettare come in
   una foto normale).
3. Specificare simmetria esplicita quando la zona è bilaterale (es. "applica il rosa
   simmetricamente su entrambi i lati") — il recolor mirato tende ad applicarsi a una sola istanza
   dominante per chiamata (stesso pattern gia' osservato con qwen, vedi
   `Build/ImageGenTests/P007_D001_local_gen_test.md` Test 13-19).

```
Mantieni ESATTAMENTE l'inquadratura, la posa, la prospettiva, le proporzioni e la posizione di carrozzeria/ruote/telaio di questa foto -- non cambiare geometria, non cambiare zoom, non spostare o ridimensionare le ruote. Modifica SOLO i colori delle superfici, come segue:

- Tutta la carrozzeria blu -> azzurro pastello lucido #8FD3E8.
- Tutte le zone bianche della carrozzeria (muso, cofano, cornice cockpit) -> restano azzurro pastello #8FD3E8 (stesso colore, tinta unita, nessuna zona bianca residua).
- Le fiamme rosse e bianche sulle fiancate/alettone -> rosa lucido pieno #F4879E (tinta unita, elimina completamente il pattern a fiamma, resta un pannello rosa pieno). IMPORTANTE: applica il rosa SIMMETRICAMENTE su ENTRAMBI i lati (sinistro E destro) delle fiancate e di entrambi i supporti dell'alettone -- stessa area, stessa forma speculare su entrambi i lati. Non lasciare un lato blu e l'altro rosa.
- Vetro cockpit (attualmente semi-trasparente/specchiato) -> nero lucido pieno #0A0A0A.
- Rimuovi COMPLETAMENTE ogni scritta: il testo "MAGNUM SABER" sull'alettone e il kanji dorato sul muso devono sparire del tutto, sostituiti dal colore azzurro pastello #8FD3E8 pieno della zona circostante (nessun testo, nessuna scritta residua, nessuna traccia leggibile).
- Fari gialli -> restano gialli lucidi #F5D300, invariati.
- Cerchi ruote (attualmente rossi) -> argento metallizzato lucido #C8C8C8, tinta unita.
- Telaio/bracci sospensione (attualmente neri) -> argento metallizzato #C8C8C8 con dettagli grigio scuro metallizzato #4B4E52.
- Rulli/rollers laterali (attualmente rossi) -> restano come sono ma in argento metallizzato #C8C8C8 anziche' rosso.

Sfondo bianco puro, illuminazione invariata. Nessun testo overlay aggiuntivo, nessuna UI, nessuna cornice.
```

**Crop del reference usato (`.flux_crops/ref_front_crop.jpg`):** `magick ref_front.jpg -crop 2936x2361+930+539 +repage ref_front_crop.jpg` (bbox calcolato per matchare fill-ratio ~0.9 orizzontale/verticale della baseline approvata).

**Nota:** `cover_3q.png` e `P002_top.png` (batch 1, ancora sul metodo rewrite) non hanno mostrato
segnali di questo problema in ispezione visiva — non rifatti, considerati validi cosi' come sono.
Vedi anche nota sull'inconsistenza tra i file reference (`ref_3q_front.jpg` ha livrea bianca/blu
invertita rispetto a `ref_front/side/rear/top.jpg` che sono blu/bianco — foto di due esemplari o
sessioni diverse, non un problema del nostro pipeline; ininfluente perche' i colori non derivano mai
dal reference, solo la sagoma).

## P002 — vista ortogonale laterale (slot: side)
**File:** `Images/P002_side.png`
**Reference input:** `.flux_crops/ref_side_crop.jpg` (NON `Images/ref_side_right.jpg` diretto)
**Esito:** v2/v3 (rewrite descrittivo, stesso approccio di cover/top) avevano problemi di fedelta'
strutturale simili a `P002_front` v2 (cerchi stile auto generica, chassis Mini4WD non riconoscibile).
v4 con metodo direct-edit (vedi ricetta sotto la entry di `P002_front`) ha invertito FRONTE/RETRO
(rosa sul muso, azzurro sullo spoiler — il contrario di quanto richiesto) nonostante l'istruzione
"meta' anteriore/posteriore" fosse esplicita — il modello non associa in modo affidabile
anteriore/posteriore alla geometria visibile. v5 fissa l'errore descrivendo le zone come
SINISTRA/DESTRA dell'immagine con un chiarimento esplicito su quale lato e' il retro (dove si trova
l'alettone) — corretto al primo tentativo. Aggiunta anche istruzione esplicita di preservare forma/
dimensione dei cerchi (stesso numero di razze, stessa dimensione, SOLO colore diverso) per evitare
la deriva verso cerchi in lega generici vista nei tentativi precedenti.

**Lezione riusabile:** per prompt di recolor per-zona su viste laterali, usare SEMPRE
sinistra/destra rispetto all'immagine (con un ancoraggio esplicito tipo "il lato con l'alettone e'
il retro") invece di anteriore/posteriore — l'anteriore/posteriore semantico e' ambiguo per il
modello quando la scena non ha un "davanti" ovvio come una foto di persona.

```
Mantieni ESATTAMENTE l'inquadratura, la posa, la prospettiva, le proporzioni, la posizione e la FORMA/DIMENSIONE dei cerchi ruota di questa foto -- non cambiare geometria, non cambiare zoom, non spostare o ridimensionare le ruote, non cambiare il design/stile dei cerchi (stesso numero di razze, stessa forma, stessa dimensione -- solo colore diverso). Modifica SOLO i colori delle superfici, come segue:

ATTENZIONE ORIENTAMENTO: in questa immagine l'ALETTONE/ALA POSTERIORE (la superficie piatta orizzontale in alto) si trova sul lato SINISTRO dell'immagine -- quello e' il RETRO della vettura. Il MUSO con il parabrezza del cockpit che scende in avanti si trova sul lato DESTRO dell'immagine -- quello e' il FRONTE della vettura.

- Lato DESTRO dell'immagine (muso, parafango con il cockpit, fino al centro della vettura) -- tutte le zone blu E le zone bianche/rosse del pattern a fiamma in questa meta' -> azzurro pastello lucido pieno #8FD3E8, tinta unita, elimina completamente il pattern a fiamma.
- Lato SINISTRO dell'immagine (alettone posteriore con i suoi montanti, fiancata e parafango posteriore, fino al centro della vettura) -- tutte le zone blu E le zone bianche/rosse del pattern a fiamma in questa meta' -> rosa lucido pieno #F4879E, tinta unita, elimina completamente il pattern a fiamma. Deve essere un'area ampia e ben visibile, non solo un accento sulla punta dell'alettone.
- Vetro cockpit (attualmente semi-trasparente scuro) -> nero lucido pieno #0A0A0A.
- Rimuovi COMPLETAMENTE ogni scritta: il testo giallo sull'alettone, il numero di gara "1", il piccolo logo/adesivo vicino al finestrino -> tutti sostituiti dal colore pieno (azzurro o rosa, secondo la zona) circostante, nessuna scritta o numero residuo, nessuna traccia leggibile.
- Cerchi ruote (attualmente verdi, design a razze) -> STESSA FORMA E DIMENSIONE, ricolorati in argento metallizzato lucido pieno #C8C8C8 (colore chiaramente metallico grigio-argento, non bianco).
- Rulli laterali/rollers (attualmente rossi, dischi piatti) -> STESSA FORMA E DIMENSIONE, ricolorati in argento metallizzato pieno #C8C8C8 (non bianco).
- Bracci/telaio neri visibili -> argento metallizzato #C8C8C8 con dettagli grigio scuro metallizzato #4B4E52.

Sfondo bianco puro, illuminazione invariata. Nessun testo overlay aggiuntivo, nessuna UI, nessuna cornice.
```

**Crop del reference usato (`.flux_crops/ref_side_crop.jpg`):** `magick ref_side_right.jpg -crop 4632x2714+52+439 +repage ref_side_crop.jpg`.

## P004 — step 1-5 (slot: step1..step5) — foto di processo PRE-VERNICIATURA

**PROBLEMA CRITICO trovato nel batch flux2 iniziale (round 1):** tutti e 5 gli step P004 erano
stati generati con la scocca GIA' verniciata Cotton Candy Drift E con ruote/telaio montati — SBAGLIATO
su entrambi i punti. Verificato contro i backup pre-flux approvati: a questo stadio del manuale
(prima della verniciatura) e' visibile SOLO la scocca/carrozzeria bianca ABS grezza, SEPARATA dal
telaio — niente ruote, niente rulli, niente chassis, niente colore. Root cause: il prompt originale
(recuperato da git history, generato automaticamente da `render_page.py`) appende ciecamente lo
stesso blocco "schema colori" the-full-car a OGNI slot immagine del progetto, incluse le foto di
processo pre-verniciatura — bug nel generatore di prompt della SDK stessa (`render_page.py`), fuori
scope qui, da segnalare separatamente. Qwen/ChatGPT nel flusso originale evidentemente ignorava
questo blocco irrilevante usando buon senso narrativo sul contesto "Step N — lavaggio/asciugatura/
carteggiatura/ecc."; flux2 lo ha applicato letteralmente.

**Fix:** prompt riscritto da zero per tutti e 5 gli step, con due vincoli espliciti e ripetuti in
ogni prompt:
1. SOLO la scocca (body shell), esplicitamente SENZA telaio/ruote/rulli/meccanica — con istruzione
   di ignorare completamente telaio/ruote anche se presenti nella foto di reference.
2. Plastica ABS bianco crema/avorio NON verniciata (tranne step 5, dove si specifica che il primer
   e' anch'esso bianco, non introduce colore) — nessun accenno allo schema colori Cotton Candy Drift.

Reference input per tutti e 5: `Images/ref_3q_front.jpg` (usato solo per la sagoma della scocca, il
resto — mani, guanti, acqua/carta abrasiva/panno/spray — e' descritto testualmente per azione).

### Step 1 — Lavaggio
```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di PREPARAZIONE PRIMA DELLA VERNICIATURA della sola SCOCCA/CARROZZERIA (body shell) di un modellino Mini4WD -- SENZA telaio, SENZA ruote, SENZA rulli/roller, SENZA meccanica interna. In questa fase la carrozzeria e' stata rimossa dal telaio ed e' maneggiata da sola, come un guscio di plastica cavo (si vede l'interno cavo/vuoto quando visibile). Se nella foto di riferimento il telaio/ruote sono presenti, IGNORALI COMPLETAMENTE -- non includerli nell'immagine, non disegnare ruote, non disegnare telaio nero, non disegnare rulli colorati. Il soggetto e' ESCLUSIVAMENTE la scocca esterna (cofano, fiancate, alettone, cockpit surround) vista come un guscio isolato.

La scocca e' plastica ABS GREZZA NON VERNICIATA, colore bianco crema/avorio uniforme (colore naturale della plastica stampata, superficie lucida di stampo), SENZA alcuna vernice, SENZA schema colori Cotton Candy Drift, SENZA azzurro/rosa/nero applicati -- questi arrivano in step successivi del manuale, non in questo.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Azione mostrata: Step 1 — Lavaggio della carrozzeria. Una mano con guanto in nitrile blu regge uno spazzolino da denti bianco con setole morbide e lo passa delicatamente sulla scocca bianca (senza ruote ne' telaio) immersa in una bacinella/contenitore trasparente con acqua tiepida saponata (leggera schiuma visibile). Inquadratura ravvicinata stile fotografia tutorial/hobby, messa a fuoco sulla scocca e sullo spazzolino, luce studio neutra e morbida, sfondo chiaro semplice e sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica della sola scocca (sagoma, proporzioni, alettone, prese d'aria, cockpit surround) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma della carrozzeria, non il colore, non il telaio, non le ruote.
```

### Step 2 — Asciugatura
```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di PREPARAZIONE PRIMA DELLA VERNICIATURA della sola SCOCCA/CARROZZERIA (body shell) di un modellino Mini4WD -- SENZA telaio, SENZA ruote, SENZA rulli/roller, SENZA meccanica interna. In questa fase la carrozzeria e' stata rimossa dal telaio ed e' maneggiata da sola, come un guscio di plastica cavo (si vede l'interno cavo/vuoto quando visibile, es. dal lato inferiore aperto). Se nella foto di riferimento il telaio/ruote sono presenti, IGNORALI COMPLETAMENTE -- non includerli nell'immagine, non disegnare ruote, non disegnare telaio nero, non disegnare rulli colorati. Il soggetto e' ESCLUSIVAMENTE la scocca esterna (cofano, fiancate, alettone, cockpit surround) vista come un guscio isolato.

La scocca e' plastica ABS GREZZA NON VERNICIATA, colore bianco crema/avorio uniforme (colore naturale della plastica stampata, superficie lucida di stampo), ancora bagnata/con gocce d'acqua visibili sulla superficie, SENZA alcuna vernice, SENZA schema colori Cotton Candy Drift, SENZA azzurro/rosa/nero applicati -- questi arrivano in step successivi del manuale, non in questo.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Azione mostrata: Step 2 — Asciugatura completa. La scocca bianca (senza ruote ne' telaio), ancora con gocce d'acqua sulla superficie lucida, appoggiata capovolta o di lato su un panno pulito bianco/grigio chiaro privo di lanugine, in un ambiente pulito, nessuna mano visibile in questa foto (il pezzo e' lasciato asciugare all'aria da solo). Inquadratura ravvicinata stile fotografia tutorial/hobby, messa a fuoco sulla scocca, luce studio neutra e morbida, sfondo chiaro semplice e sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica della sola scocca (sagoma, proporzioni, alettone, prese d'aria, cockpit surround) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma della carrozzeria, non il colore, non il telaio, non le ruote.
```

### Step 3 — Carteggiatura
```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di PREPARAZIONE PRIMA DELLA VERNICIATURA della sola SCOCCA/CARROZZERIA (body shell) di un modellino Mini4WD -- SENZA telaio, SENZA ruote, SENZA rulli/roller, SENZA meccanica interna. In questa fase la carrozzeria e' stata rimossa dal telaio ed e' maneggiata da sola, come un guscio di plastica cavo (si vede l'interno cavo/vuoto quando visibile, es. dal lato inferiore aperto). Se nella foto di riferimento il telaio/ruote sono presenti, IGNORALI COMPLETAMENTE -- non includerli nell'immagine, non disegnare ruote, non disegnare telaio nero, non disegnare rulli colorati. Il soggetto e' ESCLUSIVAMENTE la scocca esterna (cofano, fiancate, alettone, cockpit surround) vista come un guscio isolato.

La scocca e' plastica ABS GREZZA NON VERNICIATA, colore bianco crema/avorio uniforme (colore naturale della plastica stampata, superficie opacizzata dalla carteggiatura, non piu' lucida), SENZA alcuna vernice, SENZA schema colori Cotton Candy Drift, SENZA azzurro/rosa/nero applicati -- questi arrivano in step successivi del manuale, non in questo.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Azione mostrata: Step 3 — Carteggiatura leggera. La scocca bianca (senza ruote ne' telaio) appoggiata su un piano di lavoro, con un piccolo foglio/pezzo di carta abrasiva (sandpaper) grigio-marrone visibile accanto o a contatto con la superficie del cofano, come se fosse appena stata usata per carteggiare a umido la superficie in un'unica direzione. Superficie leggermente opaca. Nessuna mano necessariamente visibile, o eventualmente una mano con guanto blu che regge la carta abrasiva contro la scocca. Inquadratura ravvicinata stile fotografia tutorial/hobby, messa a fuoco sulla scocca e sulla carta abrasiva, luce studio neutra e morbida, sfondo chiaro semplice e sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica della sola scocca (sagoma, proporzioni, alettone, prese d'aria, cockpit surround) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma della carrozzeria, non il colore, non il telaio, non le ruote.
```

### Step 4 — Rimozione polvere
```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di PREPARAZIONE PRIMA DELLA VERNICIATURA della sola SCOCCA/CARROZZERIA (body shell) di un modellino Mini4WD -- SENZA telaio, SENZA ruote, SENZA rulli/roller, SENZA meccanica interna. In questa fase la carrozzeria e' stata rimossa dal telaio ed e' maneggiata da sola, come un guscio di plastica cavo (si vede l'interno cavo/vuoto quando visibile, es. dal lato inferiore aperto). Se nella foto di riferimento il telaio/ruote sono presenti, IGNORALI COMPLETAMENTE -- non includerli nell'immagine, non disegnare ruote, non disegnare telaio nero, non disegnare rulli colorati. Il soggetto e' ESCLUSIVAMENTE la scocca esterna (cofano, fiancate, alettone, cockpit surround) vista come un guscio isolato.

La scocca e' plastica ABS GREZZA NON VERNICIATA, colore bianco crema/avorio uniforme (colore naturale della plastica stampata, superficie opaca da carteggiatura), SENZA alcuna vernice, SENZA schema colori Cotton Candy Drift, SENZA azzurro/rosa/nero applicati -- questi arrivano in step successivi del manuale, non in questo.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Azione mostrata: Step 4 — Rimozione della polvere. Due mani con guanti in nitrile blu reggono la scocca bianca (senza ruote ne' telaio) e passano su di essa un panno giallo morbido tipo "tack cloth" (panno appiccicoso antipolvere), con leggera polvere bianca visibile sulla superficie e sul panno. Inquadratura ravvicinata stile fotografia tutorial/hobby, messa a fuoco sulla scocca e sul panno, luce studio neutra e morbida, sfondo chiaro semplice e sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica della sola scocca (sagoma, proporzioni, alettone, prese d'aria, cockpit surround) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma della carrozzeria, non il colore, non il telaio, non le ruote.
```

### Step 5 — Primer bianco
```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di PREPARAZIONE PRIMA DELLA VERNICIATURA (applicazione primer) della sola SCOCCA/CARROZZERIA (body shell) di un modellino Mini4WD -- SENZA telaio, SENZA ruote, SENZA rulli/roller, SENZA meccanica interna. In questa fase la carrozzeria e' stata rimossa dal telaio ed e' maneggiata da sola, come un guscio di plastica cavo. Se nella foto di riferimento il telaio/ruote sono presenti, IGNORALI COMPLETAMENTE -- non includerli nell'immagine, non disegnare ruote, non disegnare telaio nero, non disegnare rulli colorati. Il soggetto e' ESCLUSIVAMENTE la scocca esterna (cofano, fiancate, alettone, cockpit surround) vista come un guscio isolato.

La scocca e' ancora plastica ABS bianco crema/avorio uniforme, con una leggera mano di PRIMER BIANCO appena spruzzata (leggerissima variazione di opacita'/texture superficiale rispetto alla plastica grezza, ma il colore resta bianco/avorio chiaro -- il primer e' bianco, non introduce nessun colore Cotton Candy Drift). SENZA azzurro/rosa/nero applicati -- il colore vero e proprio arriva in step successivi del manuale, non in questo.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Azione mostrata: Step 5 — Applicazione del primer bianco. Una mano con guanto in nitrile blu regge la scocca bianca (senza ruote ne' telaio) mentre una bomboletta spray bianca (visibile parzialmente, tenuta dall'altra mano guantata) spruzza una nuvola leggera di primer bianco sulla superficie, a circa 25-30cm di distanza. Nuvola di spray leggermente visibile nell'aria. Inquadratura ravvicinata stile fotografia tutorial/hobby, messa a fuoco sulla scocca, luce studio neutra e morbida, sfondo chiaro semplice e sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica della sola scocca (sagoma, proporzioni, alettone, prese d'aria, cockpit surround) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma della carrozzeria, non il colore, non il telaio, non le ruote.
```

**Nota tecnica:** step1-3 salvati come `.jpg` reali (convertiti con `magick input.png -quality 92
output.jpg`, non semplice rinomina) per coerenza col formato file gia' presente nel progetto —
attenzione a non copiare mai un `.png` sotto un nome `.jpg` con `cp` diretto.

## P006 — M001-3 (slot: zone_M001..M003) — foto di dettaglio MASCHERATURA a meta' lavorazione

**PROBLEMA nel batch flux2 iniziale (round 1):** stesso identico bug di P004 — tutte e 3 le foto
mostravano il modello FINITO, completamente verniciato e assemblato, senza alcun nastro di
mascheratura visibile. Verificato contro i backup: queste sono foto di PROCESSO a meta' lavorazione
(nastro applicato, verniciatura solo parziale), non foto del prodotto finito.

**Fix:** prompt riscritti descrivendo esplicitamente lo stato di avanzamento vernice coerente con
`PROJECT.yaml` → `paintSequence` per ciascuno step, PIU' nastro di mascheratura visibile nella zona
pertinente. Reference `ref_3q_front.jpg` per tutte e 3 (per M003 usato solo come riferimento di stile
generale, il soggetto e' un cerchio isolato quindi la sagoma pesa poco).

### M001 — mascheratura ala posteriore + pannelli laterali (prima di PC002 rosa)
Stato vernice: SOLO azzurro (PC001) fatto, telaio/ruote/rulli ancora neri stock. v2 aveva ruote
verdi/rulli rossi residui dal reference (bug ricorrente) — v3 aggiunge enfasi esplicita
"TUTTI ancora plastica NERA OPACA stock" per telaio+bracci+rulli+cerchi, risolve quasi
completamente (resta un rullo minuscolo rosso, trascurabile, non rifatto).

```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di MASCHERATURA (masking) A META' LAVORAZIONE della carrozzeria di un modellino Mini4WD -- questa NON e' una foto del modello finito, e' una foto di processo con nastro di mascheratura applicato e verniciatura solo parzialmente completata.

STATO ATTUALE DELLA VERNICIATURA IN QUESTA FOTO: la carrozzeria e' gia' interamente verniciata in azzurro pastello lucido #8FD3E8 (prima mano di colore completata) -- NESSUN rosa, NESSUN nero applicato ancora sulla carrozzeria. Il telaio, i bracci di sospensione, i rulli laterali E I CERCHI DELLE RUOTE visibili sono TUTTI ANCORA plastica NERA OPACA stock non verniciata (nessun verde, nessun rosso, nessun colore -- solo nero/plastica scura stock, la verniciatura di telaio e cerchi avviene in una fase separata successiva che non e' questa).

Azione mostrata: applicazione di nastro di mascheratura giallo/senape lungo i bordi dell'ala posteriore (alettone) e dei pannelli laterali della cowling, in preparazione alla verniciatura rosa della zona sottostante (M001). Il nastro segue con precisione i bordi/le linee di piega della carrozzeria, leggermente sollevato ai bordi come nastro vero applicato a mano. In un punto dove il nastro non copre perfettamente, e' visibile un sottile filo di rosa #F4879E gia' applicato come guida/contorno appena sotto il bordo del nastro.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Inquadratura ravvicinata macro sulla zona dell'alettone posteriore e del pannello laterale, stile fotografia tutorial/hobby, luce studio neutra e morbida, sfondo chiaro semplice sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica (sagoma, proporzioni, alettone, prese d'aria, cockpit surround, telaio) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma, il colore segue le istruzioni sopra.
```

### M002 — mascheratura linee di cintura + cornice cockpit (prima di PC003 nero)
Stato vernice: azzurro E rosa gia' fatti, linee/cornice ANCORA colore di base (non ancora nere),
telaio/ruote ancora neri stock. Validato al primo tentativo.

```
Genera SOLO una fotografia fotorealistica ravvicinata di tipo tutorial/how-to, che mostra una fase di MASCHERATURA (masking) A META' LAVORAZIONE della carrozzeria di un modellino Mini4WD -- questa NON e' una foto del modello finito, e' una foto di processo con nastro di mascheratura applicato e verniciatura solo parzialmente completata.

STATO ATTUALE DELLA VERNICIATURA IN QUESTA FOTO: la carrozzeria ha gia' ricevuto sia l'azzurro pastello lucido #8FD3E8 (zone principali) sia il rosa lucido #F4879E (pannelli laterali/alettone) -- entrambi i colori gia' completati e visibili in tinta unita. Le linee di cintura e la cornice del cockpit sono ANCORA DEL COLORE DI BASE (azzurro o rosa, NON ancora nere) -- il nero (PC003) non e' ancora stato applicato, arrivera' DOPO questa mascheratura. Il telaio, i bracci di sospensione, i rulli laterali E I CERCHI DELLE RUOTE visibili sono TUTTI ANCORA plastica NERA OPACA stock non verniciata (nessun colore -- la verniciatura di telaio e cerchi avviene in una fase separata).

Azione mostrata: applicazione di nastro di mascheratura giallo/senape stretto (6mm) che segue con precisione le linee di cintura e il bordo della cornice del cockpit, in preparazione alla verniciatura nera di quelle linee (M002). Una mano con guanto o mano nuda applica/preme il nastro contro la superficie curva. Il nastro segue esattamente il contorno del cockpit e le pieghe del corpo vettura.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Inquadratura ravvicinata macro a 3/4 sulla zona del cockpit e del parafango anteriore, stile fotografia tutorial/hobby, luce studio neutra e morbida, sfondo chiaro semplice sfocato, nessun testo overlay, nessuna UI, nessuna cornice.

Forma fisica (sagoma, proporzioni, alettone, prese d'aria, cockpit surround, telaio) il piu' fedele possibile alla foto di riferimento allegata -- solo la sagoma, il colore segue le istruzioni sopra.
```

### M003 — mascheratura cerchio ruota smontato (prima di PC005 argento)
Soggetto completamente diverso dagli altri due: un SOLO cerchio isolato, smontato dalla gomma,
NON il modello intero. **v2 difetto trovato dall'utente:** nonostante il prompt dicesse "smontato
dalla gomma", il risultato mostrava comunque un anello di gomma nera attorno al cerchio (sotto il
nastro) — descrivere lo STATO ("smontato dalla gomma") non basta, il modello ha comunque disegnato
una gomma perche' visivamente associa "cerchio+nastro" a "ruota completa mascherata". v3 fissa con
un divieto esplicito e ripetuto ("NESSUNA GOMMA, NESSUN PNEUMATICO, NESSUN ANELLO DI GOMMA NERA")
e ridescrive il nastro come applicato DIRETTAMENTE sul bordo rigido di plastica del cerchio, non su
una gomma. Validato.

**Lezione riusabile:** descrivere uno stato risultante ("gia' smontato", "gia' rimosso") non e'
sufficiente per escludere un elemento che il reference/il contesto visivo suggerisce fortemente —
serve un divieto esplicito e ripetuto dell'elemento stesso (stesso principio del "REGOLA ASSOLUTA
SUL TESTO" gia' in uso, generalizzato a qualsiasi elemento fisico da omettere).

```
Genera SOLO una fotografia fotorealistica macro ravvicinata di tipo tutorial/how-to, che mostra la fase di MASCHERATURA di un SINGOLO CERCHIO RUOTA (rim) di un modellino Mini4WD, COMPLETAMENTE SMONTATO DALLA GOMMA/PNEUMATICO.

REGOLA ASSOLUTA: NESSUNA GOMMA, NESSUN PNEUMATICO, NESSUN ANELLO DI GOMMA NERA deve essere visibile nell'immagine. La gomma e' stata rimossa e non e' nell'inquadratura -- si vede SOLO il cerchio rigido di plastica (il rim/mozzo con le razze), completamente nudo, senza alcun anello di gomma attorno. Il bordo esterno del cerchio (dove normalmente sarebbe montata la gomma, ora vuoto/esposto) e' visibile direttamente, e' plastica dura, non gomma morbida nera.

Il cerchio e' plastica GRIGIO CHIARO/BIANCA STOCK NON VERNICIATA (nessun colore Cotton Candy Drift applicato ancora), design a razze sottili stile Mini4WD, forma di un disco rigido con razze e mozzo centrale. Il cerchio e' montato su una bacchetta/asta metallica sottile (attrezzo da banco di lavoro), infilata nel foro centrale del mozzo. Attorno al bordo esterno rigido del cerchio (il labbro di plastica dove la gomma si agganciava, ora esposto) e' applicato un anello di nastro di mascheratura color senape/dorato (tan masking tape) direttamente sulla plastica del cerchio.

REGOLA ASSOLUTA SUL TESTO: nessuna scritta, lettera, numero, kanji, badge o logo leggibile su nessuna superficie.

Sfondo: piano di lavoro chiaro (legno chiaro o superficie neutra sfocata), illuminazione studio neutra e morbida, messa a fuoco macro sul cerchio e sul nastro di mascheratura, nessun testo overlay, nessuna UI, nessuna cornice. Nessun'altra parte del modellino visibile nell'inquadratura (no carrozzeria, no telaio, no altri cerchi, no gomma).
```

### v4 (definitivo) — fix geometria asta + spessore nastro: utente ha segnalato che l'asta metallica
attraversava/trapassava completamente il cerchio (visibile sporgere anche dal lato opposto,
sembrava perforare le razze) e che il nastro era troppo spesso/voluminoso. Self-correction edit
sull'immagine v3 (stesso pattern usato per `P002_top`):
```
Mantieni la stessa inquadratura, sfondo e soggetto generale di questa immagine (cerchio ruota macro, nastro di mascheratura, asta metallica). Correggi SOLO questi 2 difetti:

1. L'asta/bacchetta metallica NON deve attraversare o trapassare il cerchio da parte a parte -- deve essere inserita SOLO nel foro centrale del mozzo e fermarsi li', come se fosse a incastro/pressione in un foro cieco (non passante). Non deve essere visibile alcuna punta dell'asta che sporge dal lato opposto del cerchio o che sembra perforare il disco/le razze. L'asta e' visibile SOLO da un lato (il lato da cui e' inserita), corta, si ferma al centro del mozzo.

2. Il nastro di mascheratura color senape/dorato attorno al bordo del cerchio e' attualmente troppo spesso/voluminoso -- rendilo un nastro SOTTILE e aderente, uno strato piatto ben premuto contro la plastica, non un anello gonfio o arrotolato. Spessore realistico di nastro adesivo da 6-10mm, non un bordo largo e rigonfio.

Tutto il resto (colore cerchio, forma delle razze, sfondo, illuminazione) rimane invariato.
```
Risultato: asta corretta (si ferma al mozzo, non piu' passante). Nastro leggermente migliorato ma
ancora sostanzioso — utente ha accettato cosi' com'e' (priorita' era l'asta, risolta). **Validato
definitivo.**

## P002 — vista ortogonale dall'alto (slot: top)
**File:** `Images/P002_top.png`
**Reference input v2 (scartato per i difetti sotto):** `Images/ref_top.jpg`
**Reference input v3 (valido):** l'immagine v2 stessa (self-correction edit, non il file reference)

**ATTENZIONE — problema noto su `ref_top.jpg`:** questa foto reference NON e' una vera vista
dall'alto a tutta lunghezza -- e' scattata da un angolo frontale-dall'alto che mostra SOLO la meta'
anteriore della vettura (muso, cockpit, ruote anteriori, alettone visibile in cima perche' sporge) —
NON mostra affatto ruote posteriori, parafanghi posteriori o diffusore. Qualsiasi generazione basata
su questa foto deve necessariamente INVENTARE la meta' posteriore, il che spiega la geometria
"strana" riscontrata (blob nero centrale malformato, braccio sospensione e rulli con colori
inconsistenti rispetto a front/side gia' corretti).

**Esito v2 (rewrite method, usando `ref_top.jpg` diretto):** proporzioni generali blu/rosa
accettabili ma difetti: braccio sospensione sinistro rimasto nero (doveva essere argento come negli
altri 3 slot P002 ormai fissati), rulli rimasti bianco/pallido invece di argento, forma del
cockpit/vano centrale malformata (protuberanza a coste bianche innaturale).

**Fix v3 — self-correction edit mirato (NON ripartire dal reference, editare l'output v2 stesso):**
dato che il problema non era la sagoma generale (accettabile) ma 3 difetti puntuali di colore/pulizia,
si è editato **l'immagine v2 gia' generata** con un prompt minimale "mantieni tutto invariato,
correggi solo questi 3 punti" — piu' affidabile che rigenerare da capo da un reference incompleto.
Risultato: braccio e rulli ora argento metallizzato coerente con front/side, cockpit ripulito in
un'unica forma ovale nera liscia. Validato.

```
Mantieni ESATTAMENTE l'inquadratura, la posa, la prospettiva, le proporzioni, la sagoma della carrozzeria e la posizione di ogni elemento di questa immagine -- non cambiare geometria, non cambiare zoom, non aggiungere o rimuovere componenti. Applica SOLO queste correzioni mirate:

1. Il braccio/sospensione sul lato sinistro (attualmente NERO) -> ricolora in argento metallizzato lucido pieno #C8C8C8, identico al colore dei cerchi ruota gia' presenti nell'immagine (stesso argento metallico, non nero, non grigio scuro).
2. I due rulli/rollers circolari alle estremita' (attualmente bianchi/pallidi) -> ricolora in argento metallizzato lucido pieno #C8C8C8, stesso argento metallico dei cerchi ruota. Non bianco.
3. La zona nera al centro della carrozzeria (cockpit/vano motore) -> semplifica in una sagoma pulita e uniforme nero lucido #0A0A0A, una singola forma ovale/allungata liscia (il cockpit tub), senza la protuberanza bianca a coste/nervature attualmente visibile al suo interno -- quella parte deve diventare anch'essa nero lucido pieno, continua con il resto del cockpit.
4. Tutto il resto (colore azzurro, colore rosa, cerchi ruota, fari gialli, sfondo, ombre) rimane ESATTAMENTE invariato, pixel per pixel dove possibile.

Nessun testo, nessun logo, nessuna scritta in nessuna zona dell'immagine.
```

**Lezione riusabile:** quando solo 2-3 difetti puntuali e localizzati vanno corretti (non un
problema di geometria/framing generale), editare l'immagine GIA' generata con un prompt
"mantieni tutto tranne questi punti specifici" e' piu' affidabile e rapido che rigenerare da capo
dal reference originale — specialmente utile quando, come qui, il reference stesso ha dei limiti
(inquadratura incompleta) che rendere una rigenerazione da zero rischiosa quanto la prima volta.

## P007 — D001-4 (slot: area_D001..D004) — foto di dettaglio, modello finito verniciato

**PROBLEMA CRITICO nel batch flux2 iniziale (round 1):** allucinazioni pesanti su piu' immagini.
`P007_D001` mostrava testo/scritte inventate senza senso ("1946MUM 31DER", frammenti di kanji,
lettere gialle) nonostante D001 fosse gia' stato validato in un test precedente nella stessa
sessione — la corsa batch da 16 immagini l'ha sovrascritto con un risultato peggiore, probabilmente
perche' il prompt "one-shot" del batch non aveva il rinforzo "REGOLA ASSOLUTA SUL TESTO" sviluppato
successivamente. `P007_D002` (dovrebbe essere un macro degli ingranaggi/meccanica del motore) e
`P007_D003` (dovrebbe essere un macro dei cerchi ruota) erano COMPLETAMENTE FUORI SOGGETTO — invece
di un macro isolato sulla zona richiesta, il modello ha generato foto ad ampio campo generiche di
parafango/rulli, ignorando la descrizione "Dettaglio specifico per questo slot" nel prompt.

**Fix — approcci diversi per soggetto:**
- **D001** (abitacolo, gia' un macro-crop naturale sulla foto reference): stesso approccio del test
  di inizio sessione, EDIT mode su `ref_3q_front.jpg` con `REGOLA ASSOLUTA SUL TESTO` + cerchi
  esplicitamente silver. Validato.
- **D002** (ingranaggi/motore) e **D003** (cerchi ruota): il soggetto non e' MAI visibile nella foto
  reference (il motore e' coperto dalla scocca, i cerchi non sono mai isolati in nessuna foto) — le
  istruzioni "Dettaglio specifico" venivano quindi ignorate perche' in conflitto con cio' che il
  modello vede nell'immagine di input. Fix: passati a **GENERATE mode (txt2img, nessun `-i`)** con
  descrizione diretta e dettagliata del soggetto isolato — dato che ne' l'ingranaggio ne' il cerchio
  isolato richiedono la geometria specifica della Magnum Saber (sono componenti generici Mini4WD),
  GENERATE mode funziona benissimo qui (a differenza del fallimento GENERATE-mode-senza-reference
  gia' documentato per l'intera vettura in `Build/ImageGenTests/`). Entrambi validati al primo
  tentativo.
- **D004** (piccoli dettagli/prese d'aria): soggetto reale e visibile nel reference (zona
  cockpit-top con sfoghi laterali) — pre-crop del reference sulla zona pertinente + direct-edit
  minimale, stesso pattern di P002. Validato al primo tentativo.

**Lezione riusabile:** se il soggetto richiesto da uno slot NON e' visibile/isolabile nella foto di
reference allegata (es. componenti interni coperti, parti smontate), l'istruzione testuale da sola
non basta a forzare il framing giusto — il modello tende a "vedere" cio' che c'e' nel reference e
ignorare la richiesta in conflitto. In quel caso GENERATE mode (senza `-i`) e' spesso piu'
affidabile dell'EDIT mode, purche' il soggetto non richieda la geometria specifica del modello (va
bene per componenti meccanici generici, NON va bene per l'intera carrozzeria — vedi Test 12 in
`Build/ImageGenTests/P007_D001_local_gen_test.md`).

### D001 — Abitacolo/cornice interna (nero)
**v2** (sotto, prompt descrittivo su `ref_3q_front.jpg` non croppato) fixava il problema testo del
round-1 ma l'utente ha poi notato che l'immagine era "senza dettagli" — confrontata con `P007_D004`
(direct-edit su crop), v2 appariva liscia/sfocata, senza i bordi netti del parabrezza, le prese
d'aria, le linee di giunzione visibili nella foto reference. **v3 fix:** stesso pattern
"direct-edit" gia' consolidato per P002 — crop del reference sulla stessa identica zona cockpit
usata nel primissimo test di sessione (`.flux_crops/ref_d001_crop.jpg`), prompt di color-mapping
diretto invece di descrizione generica, PIU' un'istruzione esplicita anti-oversmoothing ("mantieni
TUTTI i dettagli meccanici/di superficie... non semplificare, non ammorbidire, non sfocare").
Risultato nitido, comparabile a D004. Validato.

**Lezione riusabile:** il prompt descrittivo generico (anche quando geometria/colori sono corretti)
tende a produrre superfici "pulite"/lisce che perdono i dettagli fini della foto originale
(bordi, prese d'aria, linee di giunzione) — per macro di dettaglio dove la texture conta, usare
SEMPRE il metodo direct-edit (crop + color-mapping) con un'istruzione esplicita di preservazione
dettaglio, non il rewrite descrittivo generico.

```
Mantieni ESATTAMENTE l'inquadratura, la posa, la prospettiva, le proporzioni e TUTTI i dettagli meccanici/di superficie di questa immagine (bordi del parabrezza, linee di giunzione, prese d'aria laterali scure, pieghe della carrozzeria, spigoli netti) -- non semplificare, non ammorbidire, non sfocare la superficie, non arrotondare o rimuovere alcun dettaglio in rilievo esistente. Il risultato deve essere NITIDO, a fuoco, con tutti i dettagli della foto originale ancora visibili, non un rendering liscio/plasticoso senza dettagli. Modifica SOLO i colori delle superfici, come segue:

- Tutta la carrozzeria bianca (cofano, cornice cockpit, alettone e i suoi montanti) -> azzurro pastello lucido pieno #8FD3E8, tinta unita, MA mantenendo tutte le ombre/riflessi/dettagli di superficie gia' presenti nella foto originale (non appiattire in un colore piatto senza modellato).
- Le fiamme rosse e la zona blu scura -> rosa lucido pieno #F4879E, tinta unita nella stessa area, mantenendo modellato/ombre.
- Vetro cockpit (attualmente grigio semi-trasparente) -> nero lucido pieno #0A0A0A, mantenendo i riflessi e la lucentezza gia' presenti sul vetro originale.
- Rimuovi COMPLETAMENTE ogni scritta: "MAGNUM" sull'alettone, il piccolo logo bianco "MAGNUM" vicino al finestrino -> sostituiti dal colore pieno della zona circostante (azzurro), nessuna scritta o lettera residua, nessuna traccia leggibile.

Sfondo bianco puro, illuminazione invariata. Nessun testo overlay aggiuntivo, nessuna UI, nessuna cornice.
```
Reference: `.flux_crops/ref_d001_crop.jpg` — `magick ref_3q_front.jpg -crop 1300x1000+2600+550 +repage` (crop diretto sulla zona cockpit, stessa area del test iniziale di sessione).

**v2 (superata, tenuta come riferimento storico del fix testo):**
```
Isolate the car on a pure white background. REGOLA ASSOLUTA SUL TESTO: remove ALL text, ALL letters, ALL numbers, ALL kanji, ALL logos, ALL decals from every surface -- no "MAGNUM", no "SABER", no kanji characters, no race number, no random lettering of any kind, no gibberish text, completely blank painted surfaces. Ignore the reference livery colors entirely. Repaint the cockpit windshield/tub area solid glossy black (#0A0A0A). Repaint the body panels solid light blue (#8FD3E8). Repaint accent panels solid pink (#F4879E). Wheels visible (if any) must be silver metallic (#C8C8C8), not yellow, not green. Tight macro close-up framing on the cockpit area, matching the framing of a product-detail photo. No text anywhere in the final image, no decals, no stickers, no lettering on the spoiler, no lettering on the body panels.
```
Reference: `Images/ref_3q_front.jpg` (EDIT mode, no crop — causa del problema di dettaglio).

### D002 — Ingranaggi e meccanica motore (Gun Metal dry-brush)
```
Macro product photography close-up of ONLY a Mini4WD gearbox/motor cover mechanism, isolated -- NOT the car body, NOT the colored bodywork, NOT the cockpit, NOT a wide car shot. The subject fills the frame: a gun-metal metallic dark gray (#4B4E52) painted gearbox cover with a dry-brush textured finish (subtle brush strokes highlighting raised mechanical ridges, screw heads, panel lines, vent fins), mounted inside a matte black plastic chassis plate. Visible on both sides of the gearbox cover: short exposed metal drive shaft ends with small black rubber bushings/grommets. No colored car body panels visible anywhere in frame -- only the gearbox cover and the black chassis plate around it. Pure white background, soft neutral studio lighting, sharp macro focus. No text, no logos, no lettering anywhere.
```
Reference: nessuno (GENERATE mode, no `-i`).

### D003 — Cerchi ruote (Silver Leaf)
```
Macro product photography of ONLY a single isolated Mini4WD wheel and tire assembly -- NOT the car body, NOT any bodywork, NOT the chassis, just the wheel standing alone. Silver metallic (#C8C8C8) multi-spoke rim (thin spokes, radial pattern, open center hub), with a black rubber slick tire mounted on it (smooth tread, no pattern, low profile). 3/4 view showing both the rim face and the tire tread width. Pure white background, soft neutral studio lighting, sharp macro focus, subtle shadow beneath. No text, no logos, no lettering, no branding on the tire or rim.
```
Reference: nessuno (GENERATE mode, no `-i`). **Nota:** a differenza di `P006_M003` (cerchio SENZA
gomma, in fase di mascheratura pre-verniciatura), qui la gomma DEVE esserci — e' il cerchio finito
gia' montato, dettaglio del modello completo, non una foto di processo.

### D004 — Piccoli dettagli e prese d'aria (Yellow)
```
Mantieni ESATTAMENTE l'inquadratura, la posa, la prospettiva, le proporzioni e la posizione di ogni elemento di questa immagine -- non cambiare geometria, non cambiare zoom. Modifica SOLO i colori delle superfici, come segue:

- Tutta la carrozzeria bianca e blu (cofano, cornice cockpit, alettone e i suoi montanti) -> azzurro pastello lucido pieno #8FD3E8, tinta unita.
- Le fiamme rosse sulle fiancate -> rosa lucido pieno #F4879E, tinta unita, elimina completamente il pattern a fiamma.
- Vetro cockpit (attualmente semi-trasparente grigio) -> nero lucido pieno #0A0A0A.
- Le piccole prese d'aria/sfoghi laterali (attualmente neri/scuri, piccole fessure sulla carrozzeria) -> accento giallo lucido pieno #F5D300 SOLO su queste piccole zone puntuali (prese d'aria), non su aree estese.
- Rimuovi COMPLETAMENTE ogni scritta: "MAGNUM SABER" sull'alettone, "MAGNUM SABER" sulla fiancata, il logo bianco piccolo vicino al finestrino, il numero di gara "1" -> tutti sostituiti dal colore pieno (azzurro o rosa, secondo la zona) circostante, nessuna scritta o numero residuo, nessuna traccia leggibile.

Sfondo bianco puro, illuminazione invariata. Nessun testo overlay aggiuntivo, nessuna UI, nessuna cornice.
```
Reference: `.flux_crops/ref_d004_crop.jpg` — `magick ref_3q_front.jpg -crop 2100x1500+2200+300 +repage ref_d004_crop.jpg`.

## Riepilogo finale — tutte e 16 le immagini validate (2026-07-16)

Tutti e 4 i batch completati: cover+P002 (4), P004 step1-5 (5), P006 M001-3 (3), P007 D001-4 (4) =
16/16. Vedi `CLAUDE.md` per il log completo delle lezioni riusabili emerse durante il processo.
