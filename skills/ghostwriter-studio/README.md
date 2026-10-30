# Ghostwriter Studio

A free Claude skill for professional ghostwriters. It runs **your** process across all your clients and takes the slow work off your plate: mining transcripts, keeping every client's voice straight, prepping calls, first drafts in your structures, repurposing for other platforms, voice checks and monthly reports.

It doesn't replace your judgment or your edit. It learns how you work and works that way.

## What it does

| Say | You get |
|-----|---------|
| "Set up my studio" | A short interview about your process, then your **Studio Playbook**: formats, hook rules, editing rules, banned words, approvals. Everything else follows it. |
| "Onboard a new client" | Interview questions in your style, then a **voice profile** with quoted evidence, a story bank, and 3 test posts. |
| "Prep my call with Sarah" | A one-page call sheet: gaps in her story bank, questions in your style, open items to chase. |
| "Mine this transcript" | Stories, exact phrases and post angles, each linked to the line it came from. |
| "Draft 3 posts for Sarah" | First drafts in your formats and her voice, each with its source and a voice-check score. |
| "Does this sound like Sarah?" | A line-by-line voice check against her profile and your rules. |
| "Repurpose this" | Versions for X, Threads, Instagram, Facebook, Google Business Profile and short video, checked against each platform's limits. |
| "Write Sarah's monthly report" | A one-page report from the numbers you paste in. |

It never invents a story, number or name. Anything missing comes back as `[ASK CLIENT: ...]`.

When you edit its drafts, it can compare your version with its own and turn your changes into rules, so it gets closer to your taste over time.

## Install

**claude.ai:** go to Settings → Capabilities, turn on Code execution, then under Skills choose Upload skill and pick `ghostwriter-studio.zip`. Some help pages place this under Customize → Skills instead. Check your plan, because Anthropic's docs differ on whether the Free plan includes custom skills.

**Claude Code:** copy the `ghostwriter-studio` folder into `~/.claude/skills/`.

Tip for claude.ai: make one Project per client and save their voice profile and story bank in it, plus your playbook in each Project's knowledge.

## Niche packs

`references/niche-packs/` holds domain knowledge for specialist clients. The skill ships with one example (heritage restoration). Ask it to "make a niche pack for <field>" to add your own.
