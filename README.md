# Ghostwriter Studio

A free Claude skill for solo ghostwriters. It learns your process, then runs it for every client: mining transcripts, voice profiles, call prep, first drafts in your formats, voice checks, repurposing for other platforms and monthly client reports. You stay the writer, and it takes the slow parts.

| Path | What's in it |
|------|--------------|
| `skills/ghostwriter-studio/` | The skill. Start with its `README.md` (what it does, how to install). |
| `dist/ghostwriter-studio.zip` | The file people upload to claude.ai (Settings → Capabilities → Skills). Rebuild after changing the skill (command below). |
| `launch/test-kit/` | Fictional client (posts + call transcript) and an 8-test checklist for trying the skill on claude.ai |
| `launch/launch-plan.md` | How to get the first solo ghostwriters using it and giving feedback |
| `launch/launch-post.md` | LinkedIn launch post, plus `launch/slides/` (3 images) |
| `tracker/ghostwriting-hq.html` | Source of the Studio HQ tracker: launch tasks, outreach, users |

Tracker: https://claude.ai/artifact/Hroey4NmEcGgZH1B4MK4rz (private to you)
Post images: https://claude.ai/artifact/EqTLEKaLPAoAifjjqSUv2n (private to you)

## Rebuild the zip

```bash
cd skills && rm -f ../dist/ghostwriter-studio.zip && zip -qr ../dist/ghostwriter-studio.zip ghostwriter-studio -x '*/__pycache__/*'
```

## Principles

- **The writer's process wins.** The skill follows each writer's playbook over its own defaults.
- **Nothing invented.** Every story, number and name traces back to the client's own material. Anything missing becomes `[ASK CLIENT]`.
- **Free for now.** The goal at this stage is real ghostwriters using it and telling us what's missing.

Earlier versions of this repo (the done-for-you service plan, heritage niche research, outreach and automation) are in the git history, if ever needed.
