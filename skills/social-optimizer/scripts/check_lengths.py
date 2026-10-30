#!/usr/bin/env python3
"""Check platform versions against the limits in references/platforms.json.

Usage: python3 check_lengths.py <versions.json>
Exits 1 if any version breaks a limit, so it can gate an automated run.
"""
import json
import re
import sys
from pathlib import Path

LIMITS = json.loads((Path(__file__).resolve().parents[1] / "references" / "platforms.json").read_text())
HASHTAG = re.compile(r"(?<![\w&])#\w+")


def check(versions):
    problems, report = [], []
    for v in versions:
        name = v.get("platform", "?")
        spec = LIMITS.get(name)
        if not spec:
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
        for i, post in enumerate(v.get("thread") or [], start=2):
            texts.append(post)
            limit = spec["fields"]["text"]["max"]
            if len(post) > limit:
                problems.append(f"{name} thread post {i} is {len(post)} characters; limit {limit}")
        tags = sum(len(HASHTAG.findall(t)) for t in texts)
        if tags > spec.get("max_hashtags", 99):
            problems.append(f"{name}: {tags} hashtags; max {spec['max_hashtags']}")
        if not spec.get("verified", True):
            report.append(f"{name}: limits not officially verified, check in the composer")
        if "[CHECK" in " ".join(texts):
            report.append(f"{name}: contains [CHECK] notes to resolve before approval")
    return problems, report


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    data = json.loads(Path(sys.argv[1]).read_text())
    problems, report = check(data.get("versions", []))
    print("\n".join(report))
    if problems:
        print("\nFAIL")
        print("\n".join(f"- {p}" for p in problems))
        sys.exit(1)
    print("\nPASS")


if __name__ == "__main__":
    main()
