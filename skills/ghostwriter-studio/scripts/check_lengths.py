#!/usr/bin/env python3
"""Check platform versions against the limits in references/platforms.json.

Usage: python3 check_lengths.py <versions.json>
Prints FAIL and exits 1 if any version breaks a limit. Prints NOT READY and
exits 2 if everything fits but some versions still contain [ASK ...] or
[CHECK ...] notes. Prints PASS and exits 0 otherwise.
"""
import json
import re
import sys
from pathlib import Path

LIMITS = json.loads((Path(__file__).resolve().parents[1] / "references" / "platforms.json").read_text())
HASHTAG = re.compile(r"(?<![\w&])#\w+")
OPEN_NOTE = re.compile(r"\[(ASK CLIENT|ASK WRITER|CHECK)\b[^\]]*\]?", re.I)
# Field used for each post in a thread; platforms without a text field use their first field.
THREAD_FIELD = "text"


def check(versions):
    problems, pending, report = [], [], []
    for v in versions:
        name = v.get("platform", "?")
        spec = LIMITS.get(name)
        if not spec or name.startswith("_"):
            problems.append(f"{name}: unknown platform (add it to platforms.json)")
            continue
        texts = []
        for field, rule in spec["fields"].items():
            value = v.get(field)
            if value is None:
                continue
            texts.append(value)
            n = len(value)
            status = "ok" if n <= rule["max"] else "TOO LONG"
            report.append(f"{name}.{field}: {n}/{rule['max']} {status}")
            if n > rule["max"]:
                problems.append(f"{name}.{field} is {n} characters; limit {rule['max']}")
        thread = v.get("thread") or []
        if thread:
            if not spec.get("thread_allowed"):
                problems.append(f"{name}: threads aren't supported for this platform")
            else:
                limit = spec["fields"].get(THREAD_FIELD, next(iter(spec["fields"].values())))["max"]
                for i, post in enumerate(thread, start=2):
                    texts.append(post)
                    report.append(f"{name} thread post {i}: {len(post)}/{limit} {'ok' if len(post) <= limit else 'TOO LONG'}")
                    if len(post) > limit:
                        problems.append(f"{name} thread post {i} is {len(post)} characters; limit {limit}")
        tags = sum(len(HASHTAG.findall(t)) for t in texts)
        if tags > spec.get("max_hashtags", 99):
            problems.append(f"{name}: {tags} hashtags; max {spec['max_hashtags']}")
        if not spec.get("verified", True):
            report.append(f"{name}: limits not officially verified, check in the composer")
        # Scan every string in the version (alt text, shot lists, photo notes...), not just limited fields.
        extras = [x for k, val in v.items() if k != "platform" for x in (val if isinstance(val, list) else [val]) if isinstance(x, str)]
        notes = OPEN_NOTE.findall(" ".join(extras))
        if notes:
            pending.append(f"{name}: {len(notes)} unresolved [ASK/CHECK] note(s) in the text")
    return problems, pending, report


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    data = json.loads(Path(sys.argv[1]).read_text())
    problems, pending, report = check(data.get("versions", []))
    print("\n".join(report))
    if problems:
        print("\nFAIL")
        print("\n".join(f"- {p}" for p in problems + pending))
        sys.exit(1)
    if pending:
        print("\nNOT READY (fits the limits, but resolve these before posting)")
        print("\n".join(f"- {p}" for p in pending))
        sys.exit(2)
    print("\nPASS")


if __name__ == "__main__":
    main()
