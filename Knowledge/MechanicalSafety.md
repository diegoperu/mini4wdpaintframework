# Mechanical Safety — Componenti da NON Verniciare

**Document ID:** KNW-SAF-001
**SDK Version:** 2.5.5
**Category:** Technique Reference

---

## Perché questo documento esiste

Un Mini4WD è un modello **funzionante**, non statico: dopo la verniciatura deve
continuare a correre su pista con motore, ingranaggi e ruote che si muovono
liberamente. Vernice applicata su una parte mobile o su un contatto elettrico
non è solo un difetto estetico — impedisce il funzionamento del modello (attrito
aggiunto agli ingranaggi, spessore che disallinea gli accoppiamenti, isolamento
di un contatto elettrico che deve condurre corrente).

Questo documento è la fonte di verità per **quali componenti non vanno mai
inclusi** in `detailAreas[]` (P007), `maskingZones[]` (P006) o negli step di
`PROJECT.yaml`/`content.yaml` come target di verniciatura — usato da
`Tests/ContentValidation.md §TEST-CV-008` e da `Core/AI_OPERATING_RULES.md §RULE-101`.

---

## Componenti da NON verniciare mai (parti mobili/funzionali)

| Componente | Motivo |
|---|---|
| Ingranaggi (gear) | La vernice altera lo spessore dei denti — ingranamento compromesso, usura accelerata |
| Motore — interno (spazzole, commutatore, avvolgimenti) | Vernice sui contatti elettrici impedisce la conduzione — motore non parte |
| Cuscinetti / boccole (superfici di rotolamento) | Vernice aumenta l'attrito — asse non gira liberamente |
| Albero motore e alberi di trasmissione | Parte rotante a contatto diretto con ingranaggi — stesso problema degli ingranaggi |
| Contatti elettrici (terminali batteria, interruttore) | Vernice = isolante — nessuna conduzione elettrica |
| Superficie di rotolamento pneumatici (battistrada) | Vernice altera aderenza e bilanciamento ruota |
| Assi ruota (punto di contatto con il cerchio) | Interferenza meccanica con il montaggio |

## Componenti sicuri da verniciare (cosmetici, nessuna parte mobile)

| Componente | Note |
|---|---|
| Carrozzeria (body shell) | Componente cosmetico per definizione — nessun vincolo meccanico |
| Cover motore esterna (guscio plastico, non il motore) | Puramente cosmetica, non a contatto con parti in movimento |
| Cerchi ruota — superficie esterna (non il foro/asse) | Verniciabile finché la vernice non finisce sul punto di contatto con l'asse |
| Telaio — superfici non a contatto con parti mobili | Es. piastra superiore del telaio, alettoni, supporti statici |
| Ali/spoiler, prese d'aria decorative, dettagli abitacolo | Componenti statici, nessun vincolo funzionale |

**Regola pratica:** se un componente ruota, scorre, o conduce elettricità durante
il normale funzionamento del modello, non va verniciato. Se in dubbio, verniciare
solo la cover/guscio esterno cosmetico del componente, mai il meccanismo interno.

---

## Related Documents
- `Core/AI_OPERATING_RULES.md §RULE-101`
- `Tests/ContentValidation.md §TEST-CV-008`
- `Knowledge/Painting.md`
- `Knowledge/Masking.md`
