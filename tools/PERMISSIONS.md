# Point the agent at the adapter

Module 4 is a real tool call. The five pilot tools exist only as:

```bash
python3 tools/marlow_adapter.py call ledger.read FAC-1844
python3 tools/marlow_adapter.py call atlas.read CL-7781
python3 tools/marlow_adapter.py call vault.lookup CL-7781
python3 tools/marlow_adapter.py call screen.status CL-7781
python3 tools/marlow_adapter.py call memo.draft --body-file /tmp/facility.md
python3 tools/marlow_adapter.py read marlow/cases/harbor-request.md
python3 tools/marlow_adapter.py read marlow/cast.md
```

Cursor, Claude Code, and Codex all qualify. Allow the agent to run `python3 tools/marlow_adapter.py` inside this repo. Do not allow it to satisfy the lab by reading `marlow/systems/*.md` and inventing tool names. The checker reads `04-thin-deployment/trace.jsonl`, which only this script writes.

`screen.clear`, `ledger.book`, and `memo.submit` are refused on purpose. Call `memo.submit` once so the log shows the refusal.
