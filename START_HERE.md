# START HERE — Parti da qui

**Mini4WD Manual SDK v2.4.1** · Tempo di lettura: 3 minuti

> Questo è il PRIMO documento da leggere. Non spiega come funziona il framework:
> spiega solo **cosa fare per ottenere il tuo primo manuale**.
> Non serve conoscere gli inner working dell'SDK.

---

## Cosa farai

```
   TU (Operatore)                        L'AI (in chat)
   ──────────────                        ──────────────
1. Cloni il repository
2. Crei la cartella progetto
3. Compili PROJECT.yaml
4. Metti le foto in Images/
                          ─────────►
                                       5. Bootstrap (verifica tutto)
                                       6. Genera i testi (P001–P010)
                                       7. QA testi (validazione)
                                       8. Rendering delle pagine
                                       9. QA rendering
                                      10. PDF finale
```

Tu prepari i dati. L'AI genera il manuale. Ogni fase ha un prompt pronto da copiare.

---

## Checklist di partenza

Prima di aprire qualsiasi chat con l'AI:

- [ ] Repository clonato
- [ ] Nome ufficiale Tamiya del modello (grafia esatta)
- [ ] Codici vernici Tamiya (es. TS-57, PS-1)
- [ ] Foto del modello (minimo 4 angolazioni, sfondo chiaro)
- [ ] Letto questo documento fino in fondo

Poi, in ordine:

- [ ] **1.** Crea `Projects/{Nome_Modello}/` con dentro `Images/`, `Output/`, `Notes/`
- [ ] **2.** Copia `Templates/PROJECT.yaml` → `Projects/{Nome_Modello}/PROJECT.yaml` e compilalo
- [ ] **3.** Metti le foto in `Projects/{Nome_Modello}/Images/` ← **UNICA posizione corretta**
- [ ] **4.** Apri una chat AI e usa il **Prompt Fase 1 — Bootstrap** da `Docs/AI_BOOTSTRAP_PROMPT.md`
- [ ] **5.** Aspetta il Bootstrap Report e approvalo
- [ ] **6.** Prosegui una fase alla volta seguendo `WORKFLOW.md`

---

## Le uniche cose che devi modificare

| Puoi modificare | NON toccare mai |
|---|---|
| `Projects/{TuoModello}/` (tutta la cartella) | `Core/` |
| `Projects/{TuoModello}/PROJECT.yaml` | `PromptEngine/` |
| `Projects/{TuoModello}/Images/` (le tue foto) | `Config/` |
| — | `Templates/` (si copia, non si edita) |
| — | `ApprovedAssets/` (li scrive l'AI, non tu) |
| — | `Assets/`, `Knowledge/`, `Tests/`, `Docs/` |

Tabella completa: `FILE_MATRIX.md`

---

## Quando aprire una nuova chat

| Fase | Nuova chat? |
|---|---|
| Bootstrap → Generazione testi | NO — stessa chat |
| Generazione testi → QA testi | NO — stessa chat |
| QA testi → Rendering | **SÌ — nuova chat** (Prompt Fase 4) |
| Rendering → PDF | **SÌ — nuova chat** (Prompt Fase 5) |
| La chat è diventata lunga/confusa | SÌ — usa il Prompt di Continuità |

Dettagli e prompt pronti: `Docs/AI_BOOTSTRAP_PROMPT.md`

---

## Dove andare adesso

| Vuoi… | Leggi |
|---|---|
| Il tutorial completo del primo manuale | `OperatorGuide/01_Primo_Manuale.md` |
| Creare il progetto passo-passo | `FIRST_PROJECT.md` |
| Capire il flusso completo (state machine) | `WORKFLOW.md` |
| Sapere quali cartelle creare e dove mettere le immagini | `PROJECT_STRUCTURE.md` |
| Gli errori più comuni (e come evitarli) | `OperatorGuide/06_Errori_Comuni.md` |

> **Regola d'oro:** se qualcosa fallisce in validazione, NON modificare i file del
> framework. Correggi solo `PROJECT.yaml` o i dati del tuo progetto, poi rilancia
> il prompt di QA. Vedi `OperatorGuide/06_Errori_Comuni.md`.
