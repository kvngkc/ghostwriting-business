# Automation and Scheduling

```
Monthly interview (recorded) ─► transcript into clients/<slug>/transcripts/
                                      │
Voice profile skill (Claude Code) ────┤  builds/updates voice-profile.md + stories.md
                                      ▼
Weekly: draft_posts.py (cron or n8n) ─► clients/<slug>/drafts/<date>.md
                                      ▼
You edit (human pass) ─► client approves master post
                                      ▼
optimize_posts.py ─► X, Threads, Instagram, Facebook, Google Business Profile, TikTok/Reels/Shorts scripts
                                      ▼
client approves versions ─► schedule in Postiz or Publora
```

The automation does the drafting. Editing and client approval stay manual on purpose, because that's what clients pay for and it keeps false claims out of their posts.

## 1. Server

Use a small Linux VPS (2 vCPU / 4 GB RAM covers Postiz and n8n together), or [Railway's one-click Postiz](https://railway.com/deploy/postiz) if you'd rather not manage a server. Install Docker with the compose plugin.

```bash
cp .env.example .env
```

Then fill in `.env`. Generate the two secrets with:

```bash
openssl rand -hex 32
```

## 2. Drafting script

```bash
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
```

```bash
.venv/bin/python scripts/draft_posts.py example --posts 3
```

`clients/example/` shows the folder layout. Replace it with real client folders. The script uses Claude Opus 5.5 with server-side refusal fallback turned on, and writes drafts only. It never publishes.

Run it every Monday at 07:10 with cron (`crontab -e`):

```
10 7 * * 1 cd /path/to/ghostwriting-business/automation && for c in clients/*/; do .venv/bin/python scripts/draft_posts.py "$(basename "$c")"; done >> drafts.log 2>&1
```

## 2b. Other platforms (social optimiser)

Once the client approves a master post, save it as a file and run:

```bash
.venv/bin/python scripts/optimize_posts.py <client-slug> clients/<client-slug>/approved/<post>.md --platforms x,instagram,facebook,google_business_profile,tiktok
```

This writes `clients/<slug>/social/<post>.json` and a readable `.md` version, then checks every version against the limits in `skills/social-optimizer/references/platforms.json`. If a check fails, Claude gets one chance to fix the failing lines. Send the `.md` to the client for one approval covering all versions. Some limits are marked unverified, so confirm them in each platform's composer.

## 3. Scheduling with Postiz (self-hosted)

1. Create a LinkedIn developer app at linkedin.com/developers and add the "Share on LinkedIn" and "Sign In with LinkedIn using OpenID Connect" products. Set the redirect URL to `<POSTIZ_URL>/integrations/social/linkedin`. Put the client ID and secret in `.env`.
2. Run `./setup-postiz.sh`.
3. Open Postiz, create your account, then turn registration off (the script prints how).
4. For each client, add their LinkedIn as a channel. **The client logs in themselves** (send them the connect link or do it together on a call). You never hold their password.
5. Paste approved posts into Postiz and schedule them.

**Alternative without a server:** Publora is already connected in Claude. It can create drafts and schedule posts, and generate connection links for clients' accounts, so you can schedule straight from a Claude conversation.

## 4. n8n (optional, for more automation)

```bash
cd n8n && docker compose --env-file ../.env up -d
```

Then open http://localhost:5678. Workflows worth building, in order:
1. **Weekly drafts:** Schedule trigger (Mon 07:10) → Execute Command `python3 /data/automation/scripts/draft_posts.py <slug>` → email or Slack yourself "drafts ready". n8n's Docker image doesn't include Python, so the cron line above is simpler to start with.
2. **Transcript intake:** Google Drive trigger on a "transcripts" folder → save into the client's `transcripts/` folder.
3. **Reminders:** 3 days before each client's monthly interview, send the booking link. On invoice day, send yourself a reminder.

## 5. What stays manual

- The monthly interview
- Your edit of every draft
- Client approval
- Anything that sends messages or connection requests on LinkedIn (automating these breaks LinkedIn's terms)
