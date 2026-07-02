# Capitolo 18 — Troubleshooting

Questo capitolo raccoglie i difetti di produzione più comuni nella verniciatura di modelli Mini4WD, la loro causa e il rimedio. Riguarda problemi di **produzione fisica del modello** (vernice, mascheratura, decalcomanie) — non problemi dello SDK stesso. Per lo stato dei problemi noti dello SDK, vedi § 4 più sotto.

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Troubleshooting | `Knowledge/Troubleshooting.md` (KNW-TRB-001) | Source of Truth |
| Status | `STATUS.md` (§ Known Issues) | Stato dei problemi noti dello SDK (non della verniciatura) |

---

## 1. Difetti superficiali

### Buccia d'arancia (Orange Peel)
**Descrizione:** texture a fossette simile alla buccia d'arancia.
**Causa:** vernice applicata troppo spessa, bomboletta tenuta troppo vicina, vernice fredda.
**Rimedio:** lasciar indurire completamente (24h). Carteggiare a umido 1000→1500→2000. Applicare mani finali più sottili.

### Occhio di pesce (Fish Eye)
**Descrizione:** crateri circolari sulla superficie della vernice.
**Causa:** contaminazione da oli o silicone sulla superficie (impronte, agenti di distacco, lubrificanti al silicone).
**Rimedio:** rimuovere completamente e ricominciare. Sgrassare a fondo con alcol isopropilico. Assicurarsi che non ci siano prodotti al silicone nelle vicinanze durante la verniciatura.

### Colature
**Descrizione:** la vernice scorre verso il basso prima di asciugare.
**Causa:** vernice applicata in eccesso, bomboletta troppo vicina, o passate troppo lente.
**Rimedio:** lasciar indurire completamente. Carteggiare con grana 800. Riapplicare mani più sottili.

### Verniciatura a secco / texture granulosa
**Descrizione:** superficie ruvida, sabbiosa.
**Causa:** bomboletta tenuta troppo lontana, vernice asciugata prima di raggiungere la superficie, umidità bassa.
**Rimedio:** lucidare con composto fine. Per casi gravi: carteggiare a umido 800→1000→1500.

### Screpolatura
**Descrizione:** rete di crepe sulla superficie della vernice.
**Causa:** vernici incompatibili (solitamente solvente della lacca che attacca una base acrilica).
**Rimedio:** non riparabile — deve essere rimossa completamente. Usare sempre sistemi di vernice compatibili tra loro.

### Distacco della vernice durante la rimozione del nastro
**Causa:** nastro applicato su vernice non completamente indurita, o nastro troppo aggressivo su superfici fragili.
**Rimedio:** ritoccare con pennello. Per aree estese: riverniciare e attendere la cura completa prima della mascheratura successiva.

## 2. Difetti delle decalcomanie

### Effetto argento (Silvering)
**Causa:** aria intrappolata sotto la decalcomania su superficie non lucida.
**Rimedio:** applicare ammorbidente per decalcomanie, premere con decisione, lasciare riasciugare.

### Dissoluzione della decalcomania
**Causa:** vernice trasparente a lacca applicata su decalcomanie fresche/umide.
**Rimedio:** non reversibile. Rimuovere, riverniciare, riapplicare le decalcomanie, lasciare indurire completamente prima della vernice trasparente.

## 3. Checklist di prevenzione

Prima di ogni sessione di verniciatura:

- [ ] Temperatura dell'area di lavoro 18–24°C
- [ ] Umidità 40–60% (verificare con igrometro)
- [ ] Nessun prodotto al silicone entro 2 metri
- [ ] Mani lavate; maneggiare il modello con guanti dopo lo sgrassaggio
- [ ] Vernice agitata/mescolata a fondo
- [ ] Prova spray su scarto prima dell'applicazione sul modello

## 4. Problemi noti dello SDK (distinti dai difetti di verniciatura sopra)

`STATUS.md § Known Issues` riporta, alla data dell'ultima verifica di questo capitolo, **nessun problema noto documentato** per lo SDK stesso. Se questo capitolo viene consultato aspettandosi un problema con la pipeline, i prompt, o la generazione — non lo si troverà qui: consultare invece `STATUS.md § TODO` (Capitolo 14) per gli elementi ancora da completare, che non sono bug ma lavoro pianificato.

> 📝 **Nota:** non confondere le due categorie. Questo capitolo tratta difetti fisici di verniciatura (causa: chimica, tecnica, ambiente); `STATUS.md § Known Issues` tratterebbe difetti dello SDK stesso (causa: specifica incompleta, bug di generazione, inconsistenza tra documenti).

## Vedi anche

- Capitolo 17 — BestPractices (le pratiche che prevengono la maggior parte di questi difetti)
- Capitolo 14 — Roadmap (per TODO e problemi pianificati dello SDK)
- Capitolo 19 — FAQ (per domande più generali su verniciatura e SDK)
