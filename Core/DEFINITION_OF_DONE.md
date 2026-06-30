# Definition of Done

This document defines what "complete" means at every level of the Mini4WD Manual SDK. Work is not done until it satisfies the applicable criteria. Partial completion is not completion.

There are three levels: **Manual**, **Page**, and **Framework** (for SDK contributions).

---

## 1. Manual Level — Definition of Done

A manual is DONE when all of the following are true:

**Content completeness:**
1. All 10 required pages (P001–P010, excluding optional P009) have been generated and saved to `Projects/{ModelName}/Output/approved/`
2. If the project includes a premium variant, P009 has also been generated and approved
3. `Projects/{ModelName}/PROJECT.yaml` is complete — no empty required fields, no `{{project.X}}` placeholders remaining

**Quality:**
4. All 110 items in `Core/QA_SYSTEM.md` have been reviewed and all return PASS
5. QA was performed by a reviewer different from the contributor who generated the manual
6. `Projects/{ModelName}/Notes/qa_log.md` documents the QA session with date, reviewer name, and the result of every checklist item

**Renders:**
7. All renders meet the resolution minimums in `Core/RENDER_GUIDE.md` §5
8. All renders are present in `Projects/{ModelName}/Images/` and referenced in PROJECT.yaml

**PDF:**
9. PDF has been exported in both screen and print variants per `Core/PDF_MASTER.md`
10. Both PDF files are present in `Assets/ApprovedManual/{ModelName}/`
11. PDF metadata is complete per `Core/PDF_MASTER.md` §6
12. PDF fonts are embedded as subsets (QA-099)

**Filing:**
13. All approved pages are present in `Assets/ApprovedManual/{ModelName}/`
14. An entry for this manual has been added to `Assets/ApprovedManual/README.md`
15. A project maintainer has granted Approved status

**A manual that satisfies criteria 1–14 but has not received maintainer approval (criterion 15) is in QA Pass state, not Approved state.**

---

## 2. Page Level — Definition of Done

A single page (P001–P010) is DONE when all of the following are true:

**Components:**
1. All components listed in the "Components Used" section of the page's specification in `Core/PAGE_SYSTEM.md` are present
2. No component appears that is not listed in the page specification (without documented justification in `Projects/{ModelName}/Notes/decisions.md`)

**Tokens:**
3. No unresolved `{{token.X}}` placeholders visible in the page output
4. No unresolved `{{project.X}}` placeholders visible in the page output
5. All token values match `Assets/DesignSystem/Tokens/tokens.example.yaml`

**Typography:**
6. All text uses fonts from the approved stack (per `Core/STYLE_GUIDE.md` §2.1)
7. All text is at the correct size for its level (per `Core/STYLE_GUIDE.md` §2.2)

**Color:**
8. All structural colors (header, footer, component borders, backgrounds) are from the approved palette in `Core/COLOR_SYSTEM.md`
9. No color combination fails WCAG 2.1 AA contrast

**Renders:**
10. All renders on the page meet resolution minimums for their use case
11. All renders have pure white or transparent backgrounds
12. All renders are from the approved renders in `Projects/{ModelName}/Images/`

**Layout:**
13. Page uses the 12-column grid with correct column assignments
14. Margins match `Core/STYLE_GUIDE.md` §3.2
15. Header (C001) and footer (C002) are present at correct dimensions

**A page that passes individual page QA but has not been saved to `Output/approved/` is not done — it is reviewed.**

---

## 3. Framework Level — Definition of Done (SDK Contributions)

A change to the Mini4WD Manual SDK (a contribution to `Core/`, `PromptEngine/`, `Templates/`, or `Assets/DesignSystem/`) is DONE when all of the following are true:

**Decision record:**
1. If the change modifies any specification in `Core/`: an Architecture Decision Record (ADR) has been filed in `STYLE_DECISIONS.md`
2. If the change is an addition (new page, new component, new token): the ADR records why the addition was necessary and which existing documents it affects

**Documentation:**
3. All documents affected by the change have been updated to reflect it
4. No document references a version of the changed specification that no longer exists
5. Cross-references between documents are accurate

**Versioning:**
6. `CHANGELOG.md` has been updated under `[Unreleased]` with an accurate description of the change
7. If the change is a breaking change (MAJOR): `VERSION` has been bumped and a migration guide has been drafted in `Docs/migration/`
8. If the change is a non-breaking addition (MINOR): `VERSION` has been bumped appropriately
9. If the change is a fix or clarification (PATCH): `VERSION` has been bumped appropriately

**Validation:**
10. At least one example in the documentation demonstrates the change
11. If a new QA item is required: it has been added to `Core/QA_SYSTEM.md` with a unique QA-NNN identifier
12. If the change affects the Definition of Done itself: this document has been updated

**Review:**
13. A second contributor has reviewed the change for accuracy and completeness
14. The change does not introduce any contradiction with other Core documents

---

## 4. Relationship Between Levels

A framework-level change is done (level 3) before any new pages or components it introduces can be used. A page is done (level 2) before the manual that contains it can be marked done (level 1). The hierarchy is:

```
Framework DoD (SDK contributions)
    ↓
Page DoD (individual pages)
    ↓
Manual DoD (complete manual)
```

Work at a lower level cannot make work at a higher level done if the lower level's DoD is not met. A manual cannot be Approved if any of its pages fail the Page DoD, even if the other 9 pages are perfect.
