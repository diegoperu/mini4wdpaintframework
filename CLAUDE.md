# Instructions for Claude Code (engineering assistant on this repo)

This file guides Claude Code when acting as software-engineering assistant on the
Mini4WD Manual SDK repository itself (docs, prompts, framework structure, releases).
It is separate from `AI_ENTRYPOINT.md`/`BOOTSTRAP.md`, which govern the AI persona that
*uses* the SDK to generate manual content — this file is about maintaining the SDK.

## Roadmap discipline

Before implementing a new feature or structural change, check `ROADMAP.md`:

- If the work overlaps a roadmap item, say so explicitly and ask whether to follow the
  roadmap's stated order or bring the item forward now.
- Flag conflicts or precedence: if the requested change depends on something roadmap
  lists as unscheduled or later, or if doing it now would make a planned item harder
  (or easier) to build later, surface that trade-off before implementing.
- If a change is genuinely new (no roadmap overlap), proceed normally, but consider
  whether it should be added to `ROADMAP.md` for future reference.
- Keep `ROADMAP.md` in sync when scope decided in conversation changes it — don't let it
  drift the way it did before the 2026-07-03 rewrite (see the note at the top of that file).
