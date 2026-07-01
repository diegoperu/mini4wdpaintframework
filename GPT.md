# GPT.md --- Mini4WD Manual SDK

## Scopo

Questo documento riassume lo stato del progetto e deve essere allegato o
usato come riferimento quando si apre una nuova chat.

## Stato del progetto

Il framework **Mini4WD Manual SDK** è stato progettato come un SDK
editoriale per produrre manuali illustrati di verniciatura per Mini4WD.

Valutazione attuale: **9.7/10**.

## Obiettivo

Generare manuali coerenti, modulari e ripetibili partendo da: - SDK
ZIP - PROJECT.yaml - immagini del modello - Prompt Engine

## Architettura

-   Core
-   PromptEngine
-   Templates
-   Projects
-   Assets
-   Build
-   Config
-   Tests
-   Knowledge
-   Docs

## Documenti principali

-   AI_OPERATING_RULES.md
-   DESIGN_LANGUAGE.md
-   STYLE_GUIDE.md
-   PAGE_SYSTEM.md
-   COMPONENT_SYSTEM.md
-   QA_SYSTEM.md
-   DEFINITION_OF_DONE.md
-   WORKFLOW.md
-   MANIFEST.yaml
-   ROADMAP.md
-   CHANGELOG.md

## Workflow

1.  Allegare lo ZIP dello SDK.
2.  Allegare PROJECT.yaml.
3.  Allegare le immagini del modello.
4.  Generare una pagina alla volta:
    -   P001 Cover
    -   P002 Color Scheme
    -   P003 Materials
    -   P004 Preparation
    -   P005 Painting
    -   P006 Masking
    -   P007 Details
    -   P008 Decals
    -   P009 Premium Variant
    -   P010 Final Checklist
5.  Verifica QA.
6.  Assemblaggio PDF.

## Regole fondamentali

-   Non modificare la forma della Mini4WD.
-   Non inventare dettagli.
-   Usare esclusivamente i colori definiti nel PROJECT.yaml.
-   Rispettare il Design Language.
-   Utilizzare Design Tokens e Component System.
-   Manuali in stile Tamiya anni '90 reinterpretato con grafica moderna.

## Stato raggiunto

Lo SDK è sufficientemente maturo per iniziare la produzione di manuali
reali e validarlo con modelli differenti.

## Evoluzioni pianificate

-   Compiler/
    -   Project Loader
    -   Context Builder
    -   Page Generator
    -   QA Engine
    -   PDF Assembler
-   Prompt Orchestrator
-   Component Catalog avanzato
-   Release System
-   Reference Validation

## Istruzioni per una nuova chat

1.  Leggere prima lo SDK.
2.  Leggere PROJECT.yaml.
3.  Analizzare le immagini del modello.
4.  Applicare il framework senza reinventare regole.
5.  Se manca un'informazione, chiedere chiarimenti oppure usare TODO:
    mai inventare dati.
