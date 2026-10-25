# Stop That Shit

Muse-adapted guard, based on lennney/stop-that-shit (MIT, tag 0.2.5, https://github.com/lennney/stop-that-shit).
Original is a Codex / Claude Code Hook + Skill Guard. Muse does not run its Hooks, so this file is the Muse version: a rule to apply before doing extra work, not a memory-saving tool. Muse's global memory is already MEMORY.md plus the nightly 22:00 Notion sync, not this skill.

Use when doing any coding, file, or multi-step task for 帅东, especially when you are tempted to add something extra, refactor nearby code, add a check, or re-verify something already checked.

SHIT = four behaviours to stop:
- S — Scope creep: fixing one problem and refactoring unrelated modules. Necessary callers, data migrations and tests go with the fix; extensions with no current use stop.
- H — Hashing & hypothetical hardening: a checksum nobody reads, a compatibility layer for an imagined future. Keep a defence only if it can find a problem and trigger rejection, recovery or diagnosis. Fix defences that swallow errors or create duplicate side effects.
- I — Intent violation: user said read-only review, files still get changed. Review reports problems; modification needs authorisation. The boundary the user drew counts.
- T — Task thrashing: re-reading, re-testing, re-reviewing the same thing with no new problem or change. Reuse evidence that already answers the current question; only re-verify when code or acceptance criteria changed. When done and verified, stop.

Judge in this order, after reading the relevant code / files:
1. What is the current deliverable, authorisation, and existing support promise?
2. Is existing capability enough? Start from the directly usable solution, standard library, platform capability, already installed dependency.
3. What concrete gap remains? Fill only the behaviour and protection needed now.
4. What does this defence actually do? Keep effective ones, drop useless ones, fix harmful ones.
5. Is verification complete for the scope? If no in-scope blocker remains, end.

Necessary work must be done fully: if a fix touches published data, complete migration, both read and write sides, and compatibility tests together, even if the diff gets bigger. Do not leave a broken caller behind.

Do not use this skill to bypass safety, to skip a check the user actually asked for, or to claim a task is done without verification. Do not invent hashes, checksums, history, or progress to justify extra work.
