# 05 — Checklist Operative

**OperatorGuide · Mini4WD Manual SDK v2.5.0**

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

## Per OGNI pagina — rendering (chat #2)

```
[ ] Nuova chat (la prima volta)
[ ] status: locked verificato PRIMA di renderizzare
[ ] File di design + content.yaml + foto allegati (lista Fase 4)
[ ] Prompt Fase 4 inviato
[ ] Testo sulla pagina IDENTICO a content.yaml
[ ] Sfondo bianco, header viola, footer presente
[ ] QA visivo eseguito (QA_SYSTEM.md)
[ ] Immagine salvata col naming corretto in Projects/{Modello}/{Variante}/ApprovedImages/P00x/
[ ] metadata.yaml → rendered
[ ] Esito annotato in Notes/qa_log.md
```

## PDF (chat #3)

```
[ ] Tutte le pagine in status: rendered
[ ] PDF_CONFIG.yaml copiato nel progetto e compilato
[ ] Nuova chat con Core/PDF_MASTER.md + config allegati
[ ] Variante screen esportata
[ ] Variante print esportata (CMYK, bleed 3mm)
[ ] Variante archive esportata
[ ] Ordine pagine, segnalibri, metadati, font verificati
[ ] checksums.sha256 generato
[ ] Consegna al Maintainer (PDF + qa_log + PROJECT.yaml)
```
