#!/usr/bin/env python3
"""Marlow pilot tools. The boundary is this process, not a sentence in a prompt.

Pilot tools: ledger.read, atlas.read, vault.lookup, screen.status, memo.draft.
Refused: screen.clear, ledger.book, memo.submit.
Plain reads (logged, not tools): the request email, memo.md, the two policies,
tools.md, and the two files you already wrote.

Usage:
  python3 tools/marlow_adapter.py --help
  python3 tools/marlow_adapter.py call ledger.read FAC-1844
  python3 tools/marlow_adapter.py call memo.draft --body-file draft.txt
  python3 tools/marlow_adapter.py read marlow/cases/harbor-request.md
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE = ROOT / "04-thin-deployment" / "trace.jsonl"
DRAFT = ROOT / "Memo" / "CL-7781" / "draft" / "facility.md"

TOOLS = {
    "ledger.read": ROOT / "marlow" / "systems" / "ledger.md",
    "atlas.read": ROOT / "marlow" / "systems" / "atlas.md",
    "vault.lookup": ROOT / "marlow" / "systems" / "vault.md",
    "screen.status": ROOT / "marlow" / "systems" / "screen.md",
}
REFUSED = ("screen.clear", "ledger.book", "memo.submit")
PLAIN = {
    "marlow/cases/harbor-request.md": ROOT / "marlow" / "cases" / "harbor-request.md",
    "marlow/systems/memo.md": ROOT / "marlow" / "systems" / "memo.md",
    "marlow/tools.md": ROOT / "marlow" / "tools.md",
    "marlow/policy/credit-policy.md": ROOT / "marlow" / "policy" / "credit-policy.md",
    "marlow/policy/screen-rules.md": ROOT / "marlow" / "policy" / "screen-rules.md",
    "02-workflow/workflow-cut.md": ROOT / "02-workflow" / "workflow-cut.md",
    "03-access/access-boundary.md": ROOT / "03-access" / "access-boundary.md",
}


def _log(kind: str, name: str, target: str) -> None:
    TRACE.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "via": "marlow_adapter",
        "kind": kind,
        "name": name,
        "target": target,
    }
    with TRACE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row) + "\n")


def _show(path: Path) -> str:
    if not path.is_file():
        return f"(missing: {path.relative_to(ROOT)})"
    return path.read_text(encoding="utf-8")


def call(name: str, arg: str, body: str) -> int:
    if name in REFUSED:
        _log("refused", name, arg or "")
        print(f"REFUSED {name}. That verb is not on the pilot list.", file=sys.stderr)
        return 2
    if name == "memo.draft":
        text = body.strip()
        if not text:
            print("memo.draft needs a body. Pass --body-file or pipe the draft on stdin.", file=sys.stderr)
            return 2
        DRAFT.parent.mkdir(parents=True, exist_ok=True)
        DRAFT.write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")
        _log("tool", "memo.draft", "Memo/CL-7781/draft/facility.md")
        print(f"Wrote {DRAFT.relative_to(ROOT)}")
        return 0
    path = TOOLS.get(name)
    if path is None:
        _log("refused", name, arg or "")
        print(f"REFUSED {name}. Unknown tool. The pilot list is fixed.", file=sys.stderr)
        return 2
    if not arg:
        print(f"{name} needs an id.", file=sys.stderr)
        return 2
    _log("tool", name, arg)
    print(_show(path))
    return 0


def plain_read(rel: str) -> int:
    key = rel.replace("\\", "/").lstrip("./")
    path = PLAIN.get(key)
    if path is None:
        _log("refused", "read", key)
        print(
            "REFUSED read. System files are tools (ledger.read, atlas.read, vault.lookup, screen.status). "
            "Plain reads are the request email, memo.md, the policies, tools.md, and your Module 2 and 3 files.",
            file=sys.stderr,
        )
        return 2
    _log("read", "file", key)
    print(_show(path))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Marlow pilot tool adapter. The trace is 04-thin-deployment/trace.jsonl.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    called = sub.add_parser("call", help="Call one pilot tool, or record a refusal.")
    called.add_argument("name")
    called.add_argument("id", nargs="?", default="")
    called.add_argument("--body-file", default="")
    read = sub.add_parser("read", help="Plain file read. Not a pilot tool.")
    read.add_argument("path")
    args = parser.parse_args()
    if args.cmd == "read":
        return plain_read(args.path)
    body = ""
    if args.name == "memo.draft":
        if args.body_file:
            body = Path(args.body_file).read_text(encoding="utf-8")
        elif not sys.stdin.isatty():
            body = sys.stdin.read()
    return call(args.name, args.id, body)


if __name__ == "__main__":
    raise SystemExit(main())
