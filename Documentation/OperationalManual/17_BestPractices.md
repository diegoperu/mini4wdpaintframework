# Capitolo 17 — Best Practices

Questo capitolo raccoglie le pratiche raccomandate, compilate da modellisti Mini4WD esperti, che producono in modo consistente risultati professionali. Non sono requisiti bloccanti — a differenza delle regole in `Core/AI_OPERATING_RULES.md`, non c'è una verifica QA associata — ma la loro violazione è la causa più comune dei difetti descritti nel Capitolo 18 (Troubleshooting).

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Best Practices | `Knowledge/BestPractices.md` (KNW-BPR-001) | Source of Truth |
| AI Operating Rules | `Core/AI_OPERATING_RULES.md` | Regole correlate — formalizzano parte di queste pratiche come vincoli per l'AI |

---

## 1. Preparazione

1. Lavare sempre le carrozzerie nuove prima di qualunque manipolazione — gli agenti di distacco dello stampo sono invisibili ma compromettono l'adesione della vernice.
2. Carteggiare i gate prima dell'applicazione del primer, non dopo — un gate già primerizzato è più difficile da carteggiare in modo pulito.
3. Applicare il primer in mani sottili — due mani sottili rivelano più difetti di una mano spessa.
4. Ispezionare sotto luce radente — angolare una lampada da tavolo a 10° rispetto alla superficie rende visibili graffi e avvallamenti.
5. Rispettare almeno 24 ore tra i passaggi principali — accelerare i tempi di cura è la causa più comune di difetti.

## 2. Verniciatura

6. Provare sempre lo spray su uno scarto prima di applicarlo sul modello — intercetta ugelli intasati, pressione errata, vernice fredda.
7. Etichettare tutti i contenitori di vernice dopo l'apertura — vernice diluita non etichettata si confonde facilmente con il solo diluente.
8. Applicare più mani sottili piuttosto che una mano spessa — le mani spesse colano, intrappolano solvente e richiedono più tempo di cura.
9. Spruzzare in un'unica direzione per passata — passate a direzione casuale creano copertura irregolare.
10. Lavorare a temperatura ambiente (18–24°C) — la vernice fredda è viscosa e non atomizza bene; ambienti caldi causano evaporazione troppo rapida del solvente.

## 3. Mascheratura

11. Applicare il nastro solo su vernice completamente indurita (minimo 24h per le lacche).
12. Rifinire i bordi del nastro con uno stuzzicadenti o un bastoncino di legno, mai con l'unghia — le unghie lasciano tracce di grasso.
13. Rimuovere il nastro prima che la vernice sia completamente indurita (15–30 minuti dopo la spruzzatura) — la lacca completamente secca si crepa ai bordi del nastro in fase di rimozione.
14. Usare nastro fresco per ogni sessione — il nastro vecchio perde adesività in modo non uniforme e può lasciare residui.
15. Sovrapporre le strisce di nastro di 1–2mm — gap tra le strisce causano infiltrazioni di vernice.

## 4. Decalcomanie

16. Applicare le decalcomanie solo su superfici lucide — la texture opaca intrappola aria sotto i bordi della decalcomania, causando l'effetto argento.
17. Rifilare le decalcomanie vicino al disegno — ampie aree di pellicola trasparente restano visibili come bordi sul modello finito.
18. Usare l'ammorbidente per decalcomanie su ogni superficie curva — le decalcomanie piatte non si conformano alle curve senza assistenza chimica.
19. Non affrettare mai la cura delle decalcomanie — minimo 24h prima della vernice trasparente, minimo 12h prima della manipolazione.
20. Applicare due mani di vernice trasparente lucida dopo le decalcomanie — seppellisce il bordo della decalcomania per un effetto "dipinto".

## 5. Uso dello SDK

21. Compilare `PROJECT.yaml` completamente prima di avviare qualunque prompt — i vuoti nei dati producono marcatori `TODO:` in output, che devono essere risolti prima della QA (vedi Capitolo 06 e Capitolo 11).
22. Eseguire `Tests/FrameworkIntegrity.md` prima di iniziare una nuova versione dello SDK — verifica che tutti i documenti siano presenti.
23. Mantenere `qa_log.md` aggiornato durante tutta la produzione — non affidarsi alla memoria per lo stato della QA.
24. Archiviare le immagini di riferimento immediatamente — una volta ottenute buone foto di riferimento, archiviarle in `Assets/ReferenceModels/` prima di iniziare i render.
25. Un modello per directory di progetto — non condividere mai un `PROJECT.yaml` tra due modelli diversi.

## 6. Relazione con le regole operative dell'AI

Le pratiche 21–25 sopra sono raccomandazioni; `Core/AI_OPERATING_RULES.md` le eleva a vincoli formali per un'AI che opera sullo SDK, organizzati per categoria: `[DATA]` Data Accuracy Rules, `[DESIGN]` Design Compliance Rules, `[LAYOUT]` Layout Rules, `[COLOR]` Color Rules, `[CONTENT]` Content Rules, `[RENDER]` Render Rules, `[COMPONENT]` Component Rules, `[TOKEN]` Design Token Rules, `[OUTPUT]` Output Format Rules, e — dalla v2.3.0 — `[TEXT]` Text Rendering Rules (regole 059–100). La differenza pratica: una best practice violata produce un modello di qualità inferiore; una regola operativa violata blocca la QA (Capitolo 11).

## Vedi anche

- Capitolo 06 — ProjectYaml (compilazione completa prima del prompt)
- Capitolo 11 — QA (verifica formale, a differenza di queste raccomandazioni informali)
- Capitolo 18 — Troubleshooting (i difetti che derivano dall'ignorare queste pratiche)
- Capitolo 04 — Bootstrap (dove `Core/AI_OPERATING_RULES.md` viene caricato)
