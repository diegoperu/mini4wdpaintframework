# User Report Template

**Mini4WD Manual SDK** · Quality Management System · Documento 03

| Campo | Valore |
|-------|--------|
| Scopo | Template compilabile per il report di utilizzo di un operatore |
| Destinatario | Operatore |
| Source of Truth | Questo documento (per il formato); i report compilati sono evidenze |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## Istruzioni

Compila un report per **ogni sessione di lavoro significativa** (un manuale completato, un tentativo interrotto, un test). Copia il template qui sotto in un nuovo file `Documentation/QualityManagement/Reports/UR-{NNN}.md` (numerazione progressiva). Non serve essere esaustivi: un report breve e onesto vale più di uno lungo e vago. Vedi `16_OPERATOR_FEEDBACK.md` per quando e come consegnarlo.

---

```markdown
# User Report UR-___

## Identificazione

| Campo | Valore |
|-------|--------|
| Data | AAAA-MM-GG |
| Operatore | |
| Versione SDK | (da `VERSION`, es. 2.4.1) |
| Versione ChatGPT | (es. GPT-5.x / non usato) |
| Versione Claude | (es. Claude Fable 5 / non usato) |
| Modello AI utilizzato | (modello principale della sessione) |
| Image Model utilizzato | (se applicabile) |

## Sessione

| Campo | Valore |
|-------|--------|
| Tempo impiegato | (totale, es. 3h 30m) |
| Manuale prodotto | (nome progetto, es. Projects/DashOtto/; "non completato" se interrotto) |
| Fase raggiunta | (Bootstrap / Testi / QA / Rendering / PDF / Golden Project) |

## Difficoltà incontrate

(Descrivi ogni difficoltà: cosa stavi facendo, cosa ti aspettavi, cosa è successo.)

1.
2.

## Documenti poco chiari

(Elenca i documenti che hanno generato dubbi e perché.)

| Documento | Cosa non era chiaro |
|-----------|---------------------|
| | |

## Errori

(Errori concreti: Validation FAIL, prompt rifiutati, output sbagliati. Se un errore è riproducibile, apri anche un Bug Report con 05_BUG_REPORT_TEMPLATE.md e indica qui il Bug ID.)

| Errore | Fase | Bug ID (se aperto) |
|--------|------|--------------------|
| | | |

## Screenshot disponibili

- [ ] Sì — percorso/allegato: ______
- [ ] No

## Suggerimenti

(Facoltativo. Cosa avrebbe reso la sessione più semplice?)

## Valutazione generale

Esperienza complessiva con il framework in questa sessione: **___ / 5**

| Voto | Significato |
|:----:|-------------|
| 1 | Impossibile lavorare senza aiuto esterno |
| 2 | Completato solo con molti tentativi ed errori |
| 3 | Completato, ma con difficoltà evitabili |
| 4 | Fluido, con attriti minori |
| 5 | Fluido dall'inizio alla fine |
```
