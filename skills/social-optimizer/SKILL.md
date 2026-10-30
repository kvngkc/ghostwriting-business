---
name: social-optimizer
description: Adapt one approved ghostwritten post (usually LinkedIn) into platform-ready versions for X, Threads, Instagram (caption, carousel outline, alt text), Facebook, Google Business Profile, and short-video scripts for Reels, TikTok and YouTube Shorts, in the client's voice and within each platform's limits. Use when the user says "optimise this for other socials", "repurpose this post", "make Instagram/X/Facebook/TikTok versions", "adapt for Google Business Profile", "turn this into a reel script", or "cross-post this". Not for writing a first draft from scratch (use voice-profile) or for paid ad copy.
---

# Social Optimizer

Turns one approved master post into versions built for each platform. The facts stay fixed; only the form changes.

## Inputs

1. **The approved master post.** It must already be client-approved. Adapting an unapproved draft doubles the editing work.
2. **The client's voice profile:** `clients/<slug>/voice-profile.md`.
3. **Target platforms.** Default: the platforms listed in the client's profile, or ask.
4. **Photos available** (file names or descriptions), if any.

## Steps

1. Read `references/platform-guide.md` for each target platform, and `references/platforms.json` for its hard limits.
2. List the facts in the master post (who, what, where, numbers, techniques). Every version may use only these facts plus anything in the client's `stories.md`. If a platform version seems to need a fact that isn't there, leave a `[CHECK: ...]` note instead of inventing it.
3. Write each version following the platform guide. Keep the client's own words and phrases from the voice profile, and change only length, order and register.
4. Save the versions as JSON in the shape below. Then run:
   `python3 scripts/check_lengths.py <file.json>`
   Fix every line it reports (over the limit, too many hashtags) and run it again until it passes.
5. Present each version under a platform heading, with the checker result. All versions go back to the client for one approval, together.

## Output shape (JSON, for the checker)

```json
{
  "client": "slug",
  "source": "drafts/2026-11-02.md#post-1",
  "versions": [
    {"platform": "x", "text": "...", "thread": ["optional", "extra posts"]},
    {"platform": "instagram", "caption": "...", "carousel": ["slide 1 text", "..."], "alt_text": ["..."], "first_photo": "..."},
    {"platform": "facebook", "text": "..."},
    {"platform": "google_business_profile", "text": "...", "button": "Call | Learn more"},
    {"platform": "tiktok", "caption": "...", "script": "...", "shots": ["..."]},
    {"platform": "youtube_shorts", "title": "...", "description": "...", "script": "...", "shots": ["..."]},
    {"platform": "threads", "text": "..."},
    {"platform": "linkedin", "text": "..."}
  ]
}
```

The field names must match `platforms.json` (`text`, `caption`, `title`, `description`, `script`).

## Rules

- No new facts, numbers, names, places or claims. Adapt only what is already there.
- No copy-paste across platforms. Each version should be built for its platform.
- Keep the client's voice. The voice profile's "never use" list applies on every platform.
- Avoid AI tells everywhere: "it's not X, it's Y", self-answered questions, stacked em dashes, "unlock", "game-changer".
- Name a location or a building's owner only if the client confirmed the owner agreed.
- Several limits in `platforms.json` are marked `"verified": false`. When a platform's composer shows a different limit, update the file.

## Automation

`automation/scripts/optimize_posts.py` runs this skill's rules through the Claude API for an approved post, writes the JSON, and runs the checker. Use the skill interactively when you want to steer the versions, and the script for weekly batches.
