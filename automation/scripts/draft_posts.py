#!/usr/bin/env python3
"""Draft a week of LinkedIn posts for one client from their own material.

Usage:
  python3 draft_posts.py <client-slug> [--posts 3] [--transcript FILE]

Reads clients/<slug>/voice-profile.md, clients/<slug>/stories.md and the newest
transcript in clients/<slug>/transcripts/ (or the one you name), then writes
drafts to clients/<slug>/drafts/<date>.md for human editing and client approval.
Nothing is published by this script.

Needs ANTHROPIC_API_KEY (or an `ant auth login` profile).
"""
import argparse
import datetime
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT.parent / "skills" / "voice-profile"

SYSTEM = """You are drafting LinkedIn posts for a ghostwriting client. The posts go out under the client's own name after a human editor and the client approve them.

Write in the client's voice exactly as the voice profile describes it, including its rhythm, openings, vocabulary and boundaries. Use only stories, opinions, numbers and names that appear in the client's stories file or transcript. If a post would need a detail the material doesn't contain, leave a [CHECK: ...] note for the editor instead of inventing it.

Avoid generic AI patterns: "it's not X, it's Y" reveals, "no X, no Y, no Z" lists, self-answered questions, stacked em dashes, and words like leverage, unlock, delve, game-changer.

For each post output:
## Post <n>: <working title>
Source: <file and the part of the material it comes from>
<the post>
Voice check: <one line on which profile rules it follows, and anything the editor should look at>"""


def newest(folder: Path) -> Path | None:
    files = sorted((p for p in folder.glob("*") if p.is_file()), key=lambda p: p.stat().st_mtime)
    return files[-1] if files else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("client")
    parser.add_argument("--posts", type=int, default=3)
    parser.add_argument("--transcript", type=Path)
    args = parser.parse_args()

    client_dir = ROOT / "clients" / args.client
    profile = client_dir / "voice-profile.md"
    stories = client_dir / "stories.md"
    transcript = args.transcript or newest(client_dir / "transcripts")
    missing = [str(p) for p in (profile, stories, transcript) if not p or not Path(p).exists()]
    if missing:
        sys.exit(f"Missing: {', '.join(missing) or 'a transcript'}. Build the voice profile first.")

    rubric = (SKILL / "references" / "analysis-rubric.md").read_text()
    material = (
        f"<voice_profile>\n{profile.read_text()}\n</voice_profile>\n\n"
        f"<stories>\n{stories.read_text()}\n</stories>\n\n"
        f"<transcript file=\"{transcript.name}\">\n{transcript.read_text()}\n</transcript>\n\n"
        f"<scoring_rubric>\n{rubric}\n</scoring_rubric>"
    )
    ask = (
        f"Draft {args.posts} LinkedIn posts for this week. Each one should use a different story or opinion, "
        "preferring material from the transcript that hasn't been used yet. Then score each draft with the "
        "rubric's 'Scoring a draft' section and fix any line that scores below 4 before you output it."
    )

    client = anthropic.Anthropic()
    with client.beta.messages.stream(
        model="claude-opus-5-5",
        max_tokens=64000,
        system=SYSTEM,
        output_config={"effort": "high"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": [
            {"type": "text", "text": material, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": ask},
        ]}],
    ) as stream:
        response = stream.get_final_message()

    if response.stop_reason == "refusal":
        sys.exit(f"The request was declined ({response.stop_details}). Nothing written.")
    text = "".join(b.text for b in response.content if b.type == "text")
    if response.stop_reason == "max_tokens":
        print("Warning: output hit the length limit; the last post may be cut off.", file=sys.stderr)

    out_dir = client_dir / "drafts"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{datetime.date.today().isoformat()}.md"
    out.write_text(f"# Drafts for {args.client} ({datetime.date.today()})\n\nStatus: needs human edit, then client approval\n\n{text}\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
