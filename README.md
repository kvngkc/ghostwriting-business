# Ghostwriting Business Kit

Everything needed to start and run a LinkedIn ghostwriting business that uses AI for drafting, with a human doing the interviews and the editing.

| Folder | What's in it |
|--------|--------------|
| `niche/` | Chosen niche (UK heritage restoration contractors): research, scoring, offer, validation plan, heritage primer, one-page leaflet (A/B, source in `niche/leaflet/`) and its test plan |
| `skills/ghostwriter-studio/` | **Product:** free Claude skill for ghostwriters that runs their own process (playbook, transcript mining, voice profiles, call prep, drafts, voice check, repurposing, reports). Upload zip: `dist/ghostwriter-studio.zip` |
| `skills/social-optimizer/` | Claude skill + length checker that adapts one approved post for X, Threads, Instagram, Facebook, Google Business Profile and short-video scripts |
| `skills/voice-profile/` | Claude skill that builds a client's voice profile from their own writing and interviews, then drafts and checks posts against it. Install by copying it to `~/.claude/skills/voice-profile/`. |
| `sales/outreach-sequences.md` | Cold email, LinkedIn (manual) and warm-network sequences, reply templates, sending setup |
| `sales/sales-pipeline-playbook.md` | Full sales cycle: targeting, outreach, discovery call script, objections, proposal, close, retention, metrics |
| `automation/` | Weekly drafting script and multi-platform optimiser (Claude API), Postiz scheduler setup, n8n, cron |
| `business/business-setup.md` | Registration, tax, payments, contracts, data protection, outreach rules, tools, risks |
| `business/client-agreement-template.md` | Services agreement template (have a lawyer review it) |
| `business/client-onboarding-checklist.md` | Day-by-day onboarding for each new client |
| `tracker/ghostwriting-hq.html` | Source of the Ghostwriting HQ tracker (launch plan, pipeline, clients) |

Tracker: https://claude.ai/artifact/Hroey4NmEcGgZH1B4MK4rz (private to you)

## Order of work

1. Read `niche/niche-research.md` and run its validation plan (talk to 10 heritage firms) before investing further.
2. Work through the Launch tab in the tracker, top to bottom.
3. Run the process on yourself first, so you have a portfolio.
4. Start outreach and log every prospect in the Pipeline tab.
5. When a deal is won, it appears in Clients. Onboard it with the checklist.
6. Every week: drafts → your edit → client approval → social optimiser → schedule. Every month: interview, voice profile update, report, invoice.

## Ground rules

- Every story, number and claim in a post comes from the client. Nothing invented.
- A human edits every post and the client approves it before it's published.
- No bots for LinkedIn connections, messages or engagement. Clients connect their own accounts to the scheduler, so you never hold their passwords.
- Keep client material out of AI tools that train on inputs.
