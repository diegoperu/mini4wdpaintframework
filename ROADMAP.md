# Roadmap

This document describes the planned direction for Mini4WD Manual SDK. It is a living document and reflects current intentions, not binding commitments.

To propose a feature, open a GitHub Issue and apply the `roadmap` label. See **How to Propose a Feature** at the bottom of this document.

> **2026-07-03 — Full revision.** Previous versions of this file had drifted badly from
> reality: duplicated v2.3.0/v3.0.0 sections with conflicting scopes, "Planned" entries
> for versions that had already shipped with completely different content, and no entry
> at all for the current next release. This revision reconciles the roadmap against
> `ReleaseInfo.yaml`, `SDK_CONTEXT.yaml`, and `CHANGELOG.md`, which are the actual sources
> of truth for what shipped. Going forward, keep this file in sync at every release —
> see `Documentation/QualityManagement/01_RELEASE_POLICY.md`.

---

## Vision

Mini4WD Manual SDK aims to become the canonical open framework for producing professional, archival-quality painting manuals for scale model hobby projects. The goal is a library of approved manuals, a community of contributors across multiple countries, and tooling that makes manual production as fast and consistent as a software build pipeline.

The SDK must remain model-agnostic at the AI layer. No feature will be added that requires a specific AI provider. See `Docs/RUNTIMES.md` for supported runtimes; `UAT/UAT-002.md` and `UAT/UAT-004.md` for the Gemini compatibility history (degraded, then restored for Fase 4 only after the rendering architecture split text/layout out of the AI's job).

---

## Released

| Version | Codename | Date | Theme |
|---|---|---|---|
| 2.1.0 | Foundation | 2026-06-30 | Initial release — Core framework, PromptEngine, Design Tokens, Component System |
| 2.2.0 | Pipeline | 2026-06-30 | Build pipeline, Config layer, Test suites, Knowledge base, AI Operating Rules |
| 2.3.0 | Editorial | 2026-07-01 | Text Engine, Italian-only language policy, LOAD sequence, editorial knowledge base |
| 2.4.0 | CMS | 2026-07-01 | CMS layer (`ApprovedAssets/`), content.yaml as source of truth, page lifecycle |
| 2.4.1 | Operator | 2026-07-02 | UX & Operator Workflow — START_HERE, OperatorGuide/, runtime-aware docs, UAT-001 fixes |
| 2.5.0 | MultiProject | 2026-07-03 | Multi-Project Content Isolation — per-variant `Projects/{Model}/{Variant}/` structure |
| 2.5.5 | MultiProject | 2026-07-07 | Deterministic Rendering — `Scripts/render_page.py` template replaces whole-page AI rendering, custom fonts embedded, PDF merge, Gemini restored for Fase 4 (UAT-004) |

Full detail for each release: `CHANGELOG.md`. Machine-readable metadata for the current and prior releases: `ReleaseInfo.yaml`. Pre-2.1.0 history (1.0.0–2.0.0) exists only in `CHANGELOG.md` as early scaffolding and predates the current release process.

Governance note (2026-07-03): Gemini was degraded from "planned runtime" to "not supported" following 3 failed render attempts on UAT-002 (hallucinated output, leaked metadata, off-prompt responses). See `Docs/RUNTIMES.md` and `UAT/UAT-002.md`. This roadmap does not list unsupported runtimes as a target.

Governance note (2026-07-06): Gemini restored to "supported", limited to Fase 4
(single-illustration generation) after UAT-004 retest under the new render
architecture (`Scripts/render_page.py` produces page text/layout; the AI's job
shrank to generating one isolated illustration, no longer the failure mode
UAT-002 found). Fase 1-3 (text/bootstrap) remain unverified on Gemini.

---

## Build Order (2026-07-03)

`v2.6.0` in `ReleaseInfo.yaml`/`SDK_CONTEXT.yaml` bundles items with a real dependency
order between them — building them in the listed order (rather than as one flat bucket)
avoids rework. This section is the authoritative sequencing; version numbers below are
provisional and may be re-cut once scope per release is decided (v2.6.0 may end up
covering only steps 1–4, with the rest sliding to v2.7.0+).

1. **Validate the Fase 4 prompt fix** (in progress) — reference-image scope + C010/C011
   split, see commit `3096aef`. Confirms colors and text-box overflow are actually fixed
   before building anything on top of the render pipeline.
2. **Theme/collana mechanism** (schema only, not the full style catalog) — `PROJECT.yaml`/
   `COLLECTION.yaml` shape and token resolution order (project → collana → SDK default).
   Must land before Compiler/ and before Token Inheritance, see **Multi-Style / Theme
   System** below — both of those would otherwise encode or duplicate this mechanism.
3. **P002 compact orthogonal-view layout** — cheap, bundle with step 1's render testing
   since it touches the same page/components already under test.
4. **`Documentation/OperationalManual/` path cleanup** — independent debt paydown, no
   dependency either way, do it whenever convenient.
5. **`Compiler/` + Prompt Orchestrator** — now reads theme/collana config from step 2
   instead of hardcoding it. Absorbs the automated QA runner, index updater, and PDF
   pipeline from **Automation & Tooling** below rather than duplicating that scope in a
   second system.
6. **Icon Library** (15 SVG icons) — build against token references, not fixed hex, so
   new themes from step 2 apply automatically. Can run in parallel with step 5.
7. **`Docs/tutorial/` + release system automation** — written once the operator workflow
   (manual prompting vs. Compiler-assisted) is settled by step 5, to avoid rewriting them.
8. **Multi-language support** — blocked, not just unscheduled: needs the RULE-058
   locale-scoping decision below before any implementation starts.
9. **Extended Page Set (P011–P015) / Component Extensions (C016–C020)** — built on the
   settled theme + Compiler architecture rather than against a foundation still moving.
10. **Platform Features** (Web Prompt Runner, Plugin system) — last, major/breaking.
    Token Inheritance specifically is folded into step 2's design, not built separately.

**Parallel track (no dependency on steps above):** Claude Code Text-Phase Autopilot —
touches only Fase 2/3 (text generation + QA), never Fase 4 (render/theme/chrome), so it
does not need to wait for step 2. See **Planned — Unscheduled** below.

---

## Next Release — v2.6.0 (Planned)

**Target:** Q3 2026. Scope = Build Order steps 1–4 above, pending re-cut once step 2 is scoped in detail.

- `Compiler/` — automated pipeline executor (Project Loader, Context Builder, Page Generator, QA Engine, PDF Assembler) — see Build Order step 5, likely slides to v2.7.0
- Prompt Orchestrator — manages the LOAD sequence automatically instead of manual per-phase prompting — step 5
- `Documentation/OperationalManual/` — update all path references to v2.5.0 two-level project structure — step 4
- Icon Library — 15 SVG icons, replacing current Unicode fallbacks (see `Assets/DesignSystem/Icons/README.md`) — step 6
- Multi-language support: Italian, Japanese, English as selectable whole-document locales — step 8, blocked
- `Docs/tutorial/` — end-to-end tutorial documents — step 7
- Release system automation — step 7

> ⚠️ **Known drift:** `ReleaseInfo.yaml → next_release` and `SDK_CONTEXT.yaml → roadmap.next_planned`
> list slightly different feature sets for v2.6.0 (the list above is their union). Reconcile
> both files to a single authoritative list before v2.6.0 planning locks — and reconsider
> whether all of this still belongs in one release given the Build Order above.
>
> ⚠️ **Open question — multi-language vs. RULE-058:** `Core/DESIGN_LANGUAGE.md` RULE-058
> mandates zero Japanese characters in any text element of an Italian manual. Multi-language
> support must mean a **whole document rendered in one selected locale** (a Japanese-locale
> manual has zero Italian text, and vice versa) — never mixed scripts within a single document.
> `Config/LANGUAGE_POLICY.yaml` is currently Italian-only by design (v2.3.0 architecture
> change) and will need explicit per-locale policy files before this feature can start.

---

## Planned — Unscheduled

Features with committed scope but no assigned version yet. Build Order step numbers
reference the sequencing section above where applicable.

### Claude Code Text-Phase Autopilot — Parallel track, independent of Build Order
Originated 2026-07-03. Today the Claude Code text workflow (`OperatorGuide/Runtimes/
Claude_Code.md` steps 9a→9b→9c→9d) requires a human to manually trigger each phase per
page — generate, QA, seal — across up to 10 pages. Goal: a Claude Code Skill that runs
this loop autonomously across all applicable pages (P001–P010, conditional pages per
`PROJECT.yaml`), to speed up human review — the human reviews finished/locked text, not
each round-trip.

**Scope:** Fase 2/3 (text generation + QA + seal) only. Never touches Fase 4 (render) —
no dependency on the Theme/collana mechanism (step 2) or on `Compiler/` (step 5). Can be
built now, in parallel with the numbered Build Order.

**Failure handling (the actual design problem):**
- REJECTED on first QA pass → auto-correct and re-run QA (already the manual 9c pattern),
  capped at 2–3 attempts per page. Not blocking.
- REJECTED past the retry cap, or a structural failure (a REQUIRED `PROJECT.yaml` field
  is genuinely absent, a `colorId` reference resolves to nothing) → blocking. Log page,
  reason, and attempt count; continue to the next page rather than halting the run.
- If the first 2–3 pages all hit blocking failures for the same underlying reason, stop
  early and report "likely malformed PROJECT.yaml" instead of grinding through all pages
  identically.
- Final output: a per-page report (page, status LOCKED/BLOCKED, attempts, reason if
  blocked) — same idea as the `qa_log.md` already described under the Long-Term CLI Tool,
  just realized now instead of waiting for that tool.
- Recommended safety gate: run only P001 first, pause for human confirmation, then run
  the rest unattended. Removing the per-page human checkpoint means a systemic
  misunderstanding (e.g. a misread paint scheme) could repeat identically across many
  pages before anyone looks, unlike today's manual loop where an operator tends to notice
  by page 1–2. This does not make the self-QA problem worse than it already is (Fase 3 QA
  is already the same model grading its own Fase 2 output, today, manually) — it just
  removes the human's early chance to catch a systemic issue before it repeats.

**Downsides of the Skill approach, for the record:**
- Claude Code only — ChatGPT Web and future local-model runtimes get no benefit from this
  specific implementation; state that limitation in the Skill's own docs.
- Batch autonomy trades real-time human observability for a post-hoc report.
- Still a functional change under STABLE governance — needs the same documented
  justification as any other roadmap item, not a casual addition.

**Does this prejudice the eventual Compiler/Prompt Orchestrator (step 5), given the
long-term goal of supporting local AI models?** No — different mechanism, not a
prototype of the same code. The Skill is agentic instructions executed by Claude Code's
own harness (no API keys, no provider SDK — still "prompt text", just executed in a loop
instead of by hand). The eventual Compiler, to be genuinely model-agnostic including
local models, will need to be real software calling whichever provider's API directly.

Note: an earlier draft of this section flagged a conflict with a "no direct AI calls, SDK
is prompt text not software" constraint that used to live under `What Will Not Be Added`.
That constraint has been removed (2026-07-03) — direct provider API calls are the intended
long-term direction for `Compiler/`, not something to avoid. No conflict remains.

### Multi-Style / Theme System — Build Order step 2
Currently `Core/DESIGN_LANGUAGE.md` defines one fixed visual identity applied to every
project regardless of paint scheme mood (Rule 1/11/12: Tamiya-catalog aesthetic, white
background, function over fashion). Add a `paintScheme.style` or `project.theme` field in
`PROJECT.yaml` allowing a project to select among multiple sanctioned visual themes, each
with its own token set in `Assets/DesignSystem/Tokens/`.

Originated from a 2026-07-03 UX review of two designer mockups (`Brocken Gigant` cover +
P002) that proposed a dark/high-contrast/action-poster style incompatible with the current
default skin. Two new components are candidates to ship alongside this system, not before it
(they only make sense once a manual can opt into a non-neutral tone):
- **Painting Highlight** — 3-photo glamour grid with title + caption, tone-dependent
- **CTA footer banner** — motivational closing strip, tone-dependent

Each new theme must still pass Rule 1 (function over decoration) for whatever tone it targets.

**Manual frame chrome must become config-driven, not prompt-hardcoded.** Today the page
frame itself (background, header/footer color) is literal text in the Fase 4 prompt —
e.g. `Docs/AI_BOOTSTRAP_PROMPT.md`: *"Sfondo bianco puro. Pannello header viola
(token.PrimaryViolet)"*, duplicated in `OperatorGuide/Runtimes/Claude_Code.md` 10c. There
is no config layer resolving which token applies; the prompt names `PrimaryViolet`
directly. This must move to a per-project (or per-series) config value that the prompt
*resolves* instead of hardcodes.

**New hierarchy level: series/collection ("collana").** A theme should be settable once
for a whole series of models and inherited by every project under it, not just per single
project. This requires a config layer above `PROJECT.yaml` that does not exist today —
the SDK only has `Projects/{Model}/{Variant}/`, no collection/series grouping. Candidate
shape: a `Collections/{CollanaName}/COLLECTION.yaml` (or similar) declaring the default
theme, with `PROJECT.yaml` gaining an optional `collana` reference and an optional
override if a single project needs to deviate from its series' theme.

### P002 Layout — Compact Orthogonal View Row — Build Order step 3
Independent of the theme system. Current P002 shows front/side/top renders as three large
vertical panels. Alternate layout: same `renders.front/side/top` data from `content.yaml`,
displayed as a compact thumbnail row alongside the color legend. Pure layout variant, no new
content.yaml fields, no theme dependency — can ship whenever.

### Extended Page Set (P011–P015) — Build Order step 9
- P011: Tools & Equipment reference page
- P012: Common Mistakes & Troubleshooting
- P013: Advanced Techniques (airbrushing, candy coat, metallics)
- P014: Custom Part Painting (chassis, rollers, motor cover)
- P015: Photography & Display guide

### Component Extensions (C016–C020) — Build Order step 9
- C016: Comparison Table (before/after paint stages)
- C017: Difficulty Rating badge
- C018: Compatibility Matrix (paint brands)
- C019: QR Code block (links to video companion)
- C020: Author/Contributor credit block

### Automation & Tooling — absorbed into Build Order step 5
Not a separate system from `Compiler/` — building these independently would produce two
automation stacks that don't compose. Scope folds into the Compiler/'s QA Engine and PDF
Assembler:
- Automated PDF pipeline (pandoc + LaTeX, or headless Chromium/Puppeteer) → Compiler PDF Assembler
- Automated `Tests/ContentValidation.md` and `Tests/TextValidation.md` runners (script-based, not manual AI checklist) → Compiler QA Engine
- Automated `ApprovedAssets/index.yaml` / project index updater → Compiler Context Builder

Still independent of Compiler, no folding needed:
- `Build/CI.md` — CI/CD integration guide
- `Config/environments/` — local dev/staging/production overrides

### Platform Features (Breaking — would require a MAJOR version bump) — Build Order step 10
- Web-based Prompt Runner — browser tool that fills `PromptEngine/` templates from `PROJECT.yaml`, no server required
- Plugin system for custom component/page types via `plugins/` directory (`plugin.yaml` manifest; `COMPONENT_SYSTEM.md` schema gains a `source` field)
- ~~Token Inheritance~~ — folded into Build Order step 2 (Multi-Style/Theme System). It was
  the same token-resolution-order mechanism proposed twice under two different names; do
  not design separately.

### Local AI Render Node — Independent of Build Order, long-term ChatGPT replacement
Originated 2026-07-06, after handoff testing on Cotton Candy Drift exposed structural
limits in ChatGPT Web as the Fase 4 (Render Engine) runtime: outright refusals when
asked to certify pixel-exact conformity, and — once that was fixed — content
hallucination (wrong page layout, invented color codes/hex, cross-page context
contamination within one chat). These are not prompt bugs; they are inherent to asking
a single generalist diffusion-backed chat to produce exact text/tables/hex inside one
generated image.

Goal: a local node (available VM: NVIDIA A100 48GiB, 128GiB RAM, 24-core EPYC 7302 —
hardware is not the bottleneck for this) that splits the work instead of asking one
model to do it all: diffusion model (SDXL/Flux.1-dev + ControlNet/IP-Adapter) generates
only the physical-model illustration, shape-conditioned on reference photos and
color-conditioned on `content.yaml → colors[]`; a deterministic template/compositing
layer (HTML+Playwright or PIL) renders all text, tables, badges, and callouts directly
from `content.yaml`/`PROJECT.yaml`/`manifest.yaml` — no model ever generates text, so
hex/codes/names cannot be hallucinated.

**Confirmed by a full 8-page test (2026-07-06, ChatGPT "Thinking", single continuous
chat):** a single chat fixes cross-page visual consistency (same car/palette every
page) and nails P002's color hex/codes exactly, but consistency turns out to be
anchored to the model's own earlier invention, not to content.yaml — an area-mapping
error made on P002 (e.g. Silver Leaf mislabeled as "Headlight Surround" instead of
chassis/motor cover) then repeats faithfully on every later page that reuses that
color. Prose-heavy pages (P003 Materials, P004 Preparation, P006 Masking, P010
Checklist) get reconstructed from genre knowledge almost entirely disconnected from
their actual content.yaml, and every page came back in English despite the
Italian-only zero-tolerance rule. Full findings: `Docs/LOCAL_RENDER_NODE.md`. This
confirms the fidelity ceiling is structural (asking one model to generate long
text/data as pixels), not a chat-management problem — reinforces the case for this
node regardless of single- vs multi-chat handoff practice.

Full estimate and reasoning: `Docs/LOCAL_RENDER_NODE.md`. Rough sizing: 4-7 weeks
part-time / 2-3 weeks full-time; main open risk is R&D time on shape+color conditioning
quality, not hardware or the compositing engine (mechanical, predictable work). No SDK
version assigned yet — stays here until scoped into a real Build Order step. Compatible
with the Vision constraint that the SDK stay model-agnostic at the AI layer (this is an
additional runtime, see `Docs/RUNTIMES.md`, not a replacement requirement).

**Update 2026-07-06 — compositing half shipped, in production use.** The deterministic
half of the split (`Scripts/render_page.py` + Jinja2/HTML/CSS templates) is built and
now the primary path in `OperatorGuide/Runtimes/Claude_Code.md` § PASSO 10 and
`OperatorGuide/Runtimes/ChatGPT_Web.md` § PASSO 12 (not just this roadmap doc) — covers
all 9 pages that exist in the test project (P001-P008, P010; P009 has no populated
content.yaml to build/validate against yet). AI generation scope is now narrowed to
individual illustration slots only (cover render, 3 orthographic views, per-step/zone/area
detail photos — image path convention documented in `Docs/LOCAL_RENDER_NODE.md` §
Contratto), never a whole page. `Scripts/package_handoff.sh` and
`Docs/RENDER_HANDOFF_CONTEXT.md` were slimmed accordingly (no more `ApprovedText/`,
`COMPONENT_SYSTEM.md`, `QA_SYSTEM.md` in the ChatGPT handoff — an image generator no
longer touches page text/layout at all). Remaining scope for this roadmap item is
narrower than originally estimated: only the R&D + compositing-engine phases from the
table above are actually still open; the "Pipeline glue" step is effectively the
image-slot contract, already defined.

---

## Long-Term Vision

By full maturity, the SDK should support:
- A large library of approved model manuals across multiple contributors and countries
- Multiple languages as first-class, non-mixed locales (see multi-language open question above)
- An automated end-to-end pipeline: `PROJECT.yaml` → published PDF in one command
- A community governance model for reviewing and merging contributed manuals
- Extensibility beyond Mini4WD to any Tamiya kit family

### Community Model Library
Public repository of approved manuals contributed by the community. Submission via PR to an approved-manuals directory with completed `PROJECT.yaml` and QA log; community review before merge; web index of available manuals.

### Video Manual Support
Page specifications for video companion guides, not just static PDF: storyboard template, script template, frame-by-frame annotation system.

### Tactile/Print-Optimized Variant
High-contrast print variant for accessibility; spiral-bound single-page print format; lamination-safe PDF variant (no dark backgrounds on the back of a page).

### CLI Tool
Command-line interface (`mini4wd-sdk init`, `mini4wd-sdk qa`, `mini4wd-sdk export`) that reads `PROJECT.yaml`, validates against schema, and outputs a QA report.

---

## What Will Not Be Added

- **Model-specific content** — The SDK contains no Mini4WD model data. Models live in `Projects/`.
- **Paint brand recommendations** — The SDK describes how to represent colors; it does not endorse brands.
- **Racing or performance content** — This SDK covers painting manuals only. Motor tuning, gear ratios, and track setups are out of scope.

---

## How to Propose a Feature

1. Open a GitHub Issue with the title format: `[Feature] Short description`
2. Apply the `roadmap` label
3. In the issue body, describe:
   - **Problem:** What cannot be done today?
   - **Proposed solution:** What should the SDK support?
   - **Affected components:** Which `Core/` documents, pages, or components are involved?
   - **Fits the philosophy?** How does it align with `Core/DESIGN_LANGUAGE.md`?
   - **Breaking?** Would this require a MAJOR version bump?
4. Reference any relevant ADRs in `STYLE_DECISIONS.md`.
5. Maintainers will triage and assign to a version milestone, or mark `wontfix` with a reason.
