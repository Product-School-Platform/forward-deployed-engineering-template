# Module 4 lab

The learner has this repo open as a clone. You draft only by calling `tools/marlow_adapter.py`. You may not satisfy this lab by reading `marlow/systems` yourself and narrating tool names.

Do not use em dashes or en dashes in anything you write. Use commas, colons, or full stops.

Pilot tools, and only these:

```bash
python3 tools/marlow_adapter.py call ledger.read FAC-1844
python3 tools/marlow_adapter.py call atlas.read CL-7781
python3 tools/marlow_adapter.py call vault.lookup CL-7781
python3 tools/marlow_adapter.py call screen.status CL-7781
python3 tools/marlow_adapter.py call memo.draft --body-file /tmp/facility.md
```

Plain reads, logged, not tools:

```bash
python3 tools/marlow_adapter.py read marlow/cases/harbor-request.md
python3 tools/marlow_adapter.py read marlow/systems/memo.md
python3 tools/marlow_adapter.py read marlow/policy/credit-policy.md
python3 tools/marlow_adapter.py read marlow/policy/screen-rules.md
python3 tools/marlow_adapter.py read 02-workflow/workflow-cut.md
python3 tools/marlow_adapter.py read 03-access/access-boundary.md
```

Refused, on purpose: `screen.clear`, `ledger.book`, `memo.submit`. Call `memo.submit` once and keep the refusal.

`memo.draft` writes only `Memo/CL-7781/draft/facility.md`. Write nothing else until step 7.

1. Confirm the folder is a git clone of their repo, not the course website. `git remote -v` is enough.
2. Draft the facility section for CL-7781, FAC-1844, by calling the adapter. Put the body in a temp file and pass `--body-file`.
3. List blockers. Each one needs a path the adapter opened. Do not invent a financial pack that is not in Vault.
4. Do not write that the file is ready for committee while a blocker is open.
5. The trace is `04-thin-deployment/trace.jsonl`. Do not hand-write it. If Vault, Screen, or the request email is missing from it, say the trace fails.
6. Ask the learner whether the trace is good enough to re-run next week, then stop and wait. In a headless run, the learner answers by resuming the session.
7. Run `python3 evals/harbor_check.py`. Write what they accept into `04-thin-deployment/thin-deployment.md`. Fill the blanks. Keep the headings and the instruction lines.
8. They commit and push. Message: `Record one Harbor trace.`

If the adapter will not start, say so, and stop. Do not pretend a file read was a tool call.
