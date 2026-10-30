#!/usr/bin/env python3
"""Adapt one client-approved post into versions for other platforms.

Usage:
  python3 optimize_posts.py <client-slug> <approved-post.md> [--platforms x,instagram,facebook,...]

Uses the social-optimizer skill's platform guide and limits, writes
clients/<slug>/social/<post-name>.json and .md, and runs the length checker.
If the checker fails, Claude gets one chance to fix the reported lines.
Nothing is published.

Needs ANTHROPIC_API_KEY (or an `ant auth login` profile).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT.parent / "skills" / "social-optimizer"
CHECKER = SKILL / "scripts" / "check_lengths.py"
DEFAULT_PLATFORMS = ["x", "threads", "instagram", "facebook", "google_business_profile", "tiktok", "youtube_shorts"]

NULLABLE = {"type": ["string", "null"]}
LIST = {"type": "array", "items": {"type": "string"}}
SCHEMA = {
    "type": "object",
    "properties": {
        "versions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "platform": {"type": "string"},
                    "text": NULLABLE, "caption": NULLABLE, "title": NULLABLE,
                    "description": NULLABLE, "script": NULLABLE, "button": NULLABLE, "first_photo": NULLABLE,
                    "thread": LIST, "carousel": LIST, "alt_text": LIST, "shots": LIST,
                },
                "required": ["platform", "text", "caption", "title", "description", "script", "button",
                             "first_photo", "thread", "carousel", "alt_text", "shots"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["versions"],
    "additionalProperties": False,
}

SYSTEM = """You adapt a client-approved ghostwritten post into versions for other social platforms. The client's name goes on every version, so:
- Use only facts in the approved post and the client's stories file. Adapting changes form, never facts. If a version seems to need a missing detail, write [CHECK: what is needed] instead of inventing it.
- Keep the client's voice and words as described in their voice profile, including its "never use" list.
- Build each version for its platform as the platform guide describes; never paste the same text across platforms.
- Stay inside the hard limits given. Count characters carefully.
- Avoid AI tells: "it's not X, it's Y", self-answered questions, stacked em dashes, "unlock", "game-changer".
Fill unused fields with null or an empty list. Use these fields per platform: x/threads/linkedin/facebook/google_business_profile -> text (x may add thread); instagram -> caption, carousel, alt_text, first_photo; instagram_reels/tiktok -> caption, script, shots; youtube_shorts -> title, description, script, shots; google_business_profile may set button."""


def clean(data):
    """Drop empty fields so the JSON reads like the skill's documented shape."""
    return {"versions": [{k: v for k, v in ver.items() if v not in (None, [], "")} for ver in data["versions"]]}


def run_checker(path):
    result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
    return result.returncode == 0, result.stdout


def to_markdown(data):
    out = []
    for v in data["versions"]:
        out.append(f"## {v['platform']}")
        for key in ("title", "text", "caption", "description", "script"):
            if v.get(key):
                out.append(f"**{key}**\n\n{v[key]}")
        for key in ("thread", "carousel", "alt_text", "shots"):
            if v.get(key):
                out.append(f"**{key}**\n" + "\n".join(f"{i}. {x}" for i, x in enumerate(v[key], 1)))
        for key in ("first_photo", "button"):
            if v.get(key):
                out.append(f"**{key}:** {v[key]}")
    return "\n\n".join(out) + "\n"


def ask(client, messages):
    with client.beta.messages.stream(
        model="claude-opus-5-5",
        max_tokens=32000,
        system=SYSTEM,
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=messages,
    ) as stream:
        response = stream.get_final_message()
    if response.stop_reason == "refusal":
        sys.exit(f"The request was declined ({response.stop_details}). Nothing written.")
    if response.stop_reason == "max_tokens":
        sys.exit("Output hit the length limit before finishing. Try fewer platforms per run.")
    text = next(b.text for b in response.content if b.type == "text")
    return response, json.loads(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("client")
    parser.add_argument("post", type=Path)
    parser.add_argument("--platforms", default=",".join(DEFAULT_PLATFORMS))
    args = parser.parse_args()

    client_dir = ROOT / "clients" / args.client
    profile = client_dir / "voice-profile.md"
    stories = client_dir / "stories.md"
    for p in (profile, stories, args.post):
        if not p.exists():
            sys.exit(f"Missing: {p}")
    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    limits = json.loads((SKILL / "references" / "platforms.json").read_text())
    unknown = [p for p in platforms if p not in limits]
    if unknown:
        sys.exit(f"Unknown platforms: {', '.join(unknown)}. Known: {', '.join(k for k in limits if not k.startswith('_'))}")

    context = (
        f"<platform_guide>\n{(SKILL / 'references' / 'platform-guide.md').read_text()}\n</platform_guide>\n\n"
        f"<hard_limits>\n{json.dumps({p: limits[p] for p in platforms}, indent=1)}\n</hard_limits>\n\n"
        f"<voice_profile>\n{profile.read_text()}\n</voice_profile>\n\n"
        f"<stories>\n{stories.read_text()}\n</stories>"
    )
    messages = [{"role": "user", "content": [
        {"type": "text", "text": context, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": f"<approved_post>\n{args.post.read_text()}\n</approved_post>\n\nCreate one version for each of: {', '.join(platforms)}."},
    ]}]

    client = anthropic.Anthropic()
    out_dir = client_dir / "social"
    out_dir.mkdir(exist_ok=True)
    out_json = out_dir / f"{args.post.stem}.json"

    response, data = ask(client, messages)
    data = {"client": args.client, "source": str(args.post), **clean(data)}
    out_json.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    ok, report = run_checker(out_json)

    if not ok:
        print("Checker found problems; asking for one fix.\n" + report, file=sys.stderr)
        messages += [
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": f"The length checker reported:\n{report}\nReturn all versions again with only the failing lines fixed."},
        ]
        _, fixed = ask(client, messages)
        data = {"client": args.client, "source": str(args.post), **clean(fixed)}
        out_json.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        ok, report = run_checker(out_json)

    (out_dir / f"{args.post.stem}.md").write_text(f"# Social versions: {args.post.name}\n\nStatus: needs client approval\n\n" + to_markdown(data))
    print(report)
    print(f"Wrote {out_json} and {out_json.with_suffix('.md')}")
    if not ok:
        sys.exit("Some versions still break a limit. Fix them by hand before scheduling.")


if __name__ == "__main__":
    main()
