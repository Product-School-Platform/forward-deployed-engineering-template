# Module 4 lab

The learner has this repo open as a folder in their coding agent. You may draft. You may not send, book, or clear.

Read only these files:

- Tools: `marlow/systems/ledger.md`, `marlow/systems/atlas.md`, `marlow/systems/vault.md`, `marlow/systems/screen.md`.
- Context: `marlow/tools.md`, `marlow/systems/memo.md`, `marlow/cases/harbor-request.md`, `02-workflow/workflow-cut.md`, `03-access/access-boundary.md`.

Opening any other file is outside the boundary. If you need one, ask the learner first and log the request in the trace.

Allowed: `ledger.read`, `atlas.read`, `vault.lookup`, `screen.status`, `memo.draft`.
Refused: `screen.clear`, `ledger.book`, `memo.submit`. If you are asked for a refused tool, say so and continue without it.

The tools are simulated. Reading `ledger.md` is `ledger.read`, `atlas.md` is `atlas.read`, `vault.md` is `vault.lookup`, and `screen.md` is `screen.status`. Log each of those reads as the tool call it stands for. The context files, including `memo.md` and the request email, are plain file reads, not tools. List them under files opened. `memo.draft` is writing `Memo/CL-7781/draft/facility.md`. Write nothing else until step 7.

Do not use em dashes or en dashes in anything you write. Use commas, colons, or full stops.

1. Confirm the folder is a clone of their repo, not the course website.
2. Draft the facility section for CL-7781, FAC-1844, into `Memo/CL-7781/draft/facility.md` only.
3. List blockers. Each one needs a path you opened. Do not invent a financial pack that is not in Vault.
4. Do not write that the file is ready for committee while a blocker is open.
5. Show the trace: files opened, tools called, tools refused.
6. Ask the learner whether the trace is good enough to re-run next week, then stop and wait for the answer. If Vault, Screen, or the request email is missing from the trace, say the trace fails. In a headless run, the learner answers by resuming the session.
7. Write what they accept into `04-thin-deployment/thin-deployment.md`. Fill the blanks; keep the headings and instruction lines.
8. They commit and push. Message: `Record one Harbor trace.`
