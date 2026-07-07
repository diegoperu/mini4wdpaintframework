# 05 — Checklist Operative

**OperatorGuide · Mini4WD Manual SDK v2.5.5**

> Una checklist per ogni fase. Stampale o tienile aperte di fianco alla chat.

---

## Setup (prima di qualsiasi chat)

```
[ ] Repository clonato
[ ] Nome ufficiale Tamiya verificato (grafia esatta)
[ ] Codici vernice reali raccolti (TS-xx, PS-xx, ...)
[ ] Cartella creata: Projects/{Modello}/ con Images/, Output/raw, Output/pdf, Notes/
[ ] Nome cartella con underscore (niente trattini)
[ ] PROJECT.yaml copiato da Templates/ e compilato
[ ] Nessun campo REQUIRED vuoto (o TODO: motivato)
[ ] modelSlug in kebab-case
[ ] Foto in Projects/{Modello}/Images/ — min 5 angolazioni, min 2048px
[ ] NIENTE creato/modificato fuori da Projects/{Modello}/
```

## Bootstrap (chat #1)

```
[ ] Nuova chat aperta
[ ] File allegati nell'ordine della Fase 1 (Docs/AI_BOOTSTRAP_PROMPT.md)
[ ] Il MIO PROJECT.yaml allegato (non quello di Proto_Emperor)
[ ] Foto allegate
[ ] Prompt Fase 1 incollato e inviato
[ ] Bootstrap Report ricevuto
[ ] Report cita il MIO modello e i MIEI colori
[ ] Nessun documento mancante segnalato
[ ] Approvazione scritta in chat («Bootstrap approvato, inizia da P001»)
```

## Per OGNI pagina — testi (chat #1)

```
[ ] PromptEngine/{pagina}.md allegato
[ ] Prompt Fase 2 inviato (con ID e nome pagina giusti)
[ ] content.yaml ricevuto — tutto in italiano, TODO: dove mancano dati
[ ] Prompt Fase 3 (QA) inviato con i 2 file di test allegati
[ ] Verdetto APPROVED (se REJECTED: correzioni applicate e rivalidato)
[ ] Seal confermato: metadata.yaml → locked
[ ] content.yaml salvato in Projects/{Modello}/{Variante}/ApprovedText/P00x/
```

## Rendering — tutte le pagine (script locale, nessuna chat)

```
[ ] pip install -r Scripts/requirements.txt (una tantum)
[ ] playwright install chromium (una tantum)
[ ] Tutte le pagine in status: locked verificato PRIMA di lanciare lo script
[ ] Scripts/render_page.py {Modello} {Variante} eseguito
[ ] Build/Preview/*.png generato per ogni pagina
[ ] Projects/{Modello}/{Variante}/MISSING_IMAGES.md controllato
[ ] Se vuoto → salta alla checklist PDF
[ ] Se non vuoto → continua con la checklist "Illustrazione mancante" sotto
```

## Per OGNI illustrazione mancante (chat nuova)

```
[ ] Scripts/package_handoff.sh {Modello} {Variante} eseguito (una volta per progetto)
[ ] Nuova chat aperta (MAI la stessa di un'illustrazione precedente)
[ ] ZIP + foto di riferimento allegati come immagini dirette
[ ] Blocco prompt copiato da MISSING_IMAGES_PROMPT.md per lo slot giusto
[ ] Immagine ricevuta: nessun testo/tabella/logo, solo il soggetto isolato
[ ] Colori dell'immagine corrispondono a PROJECT.yaml → colors[], non al box-art delle foto
[ ] Immagine salvata ESATTAMENTE al path indicato nel blocco prompt
[ ] Scripts/render_page.py {Modello} {Variante} rilanciato — slot sparito da MISSING_IMAGES.md
[ ] metadata.yaml della pagina → rendered (quando tutti i suoi slot sono completi)
[ ] Esito annotato in Notes/qa_log.md
```

## PDF anteprima (script locale, nessuna chat)

```
[ ] Tutte le pagine in status: rendered
[ ] Scripts/render_page.py {Modello} {Variante} pdf eseguito
[ ] Projects/{Modello}/{Variante}/{Modello}_{Variante}.pdf generato (tutte le pagine unite)
[ ] Controllo visivo rapido: ordine pagine, nessuna riga bianca, nessuna pagina doppia
```

## PDF produzione (chat nuova)

```
[ ] PDF_CONFIG.yaml copiato nel progetto e compilato
[ ] Nuova chat con Core/PDF_MASTER.md + config allegati
[ ] Variante screen esportata
[ ] Variante print esportata (CMYK, bleed 3mm)
[ ] Variante archive esportata
[ ] Ordine pagine, segnalibri, metadati, font verificati
[ ] checksums.sha256 generato
[ ] Consegna al Maintainer (PDF + qa_log + PROJECT.yaml)
```
