# Test 7

**Prompt:** "Repurpose this for X, Instagram and a short video script." (using the strongest test-4 post)

---

Mode: **7. Repurpose**.

> **Not approved yet.** D1 is still a draft and Maya hasn't seen it. Its open questions (permission to post the bakery story, the 18% / 9% / six-weeks figures) apply to every version below. If D1 changes, these need redoing.

**Which post:** D1, "That's not accounting, that's counting" (bakery bin). I judge it the strongest of the three: it's the most concrete (a clipboard, 18% to 9%, six weeks), it's visual, which Instagram and video need, and it ends on Maya's own line. D2 scored as high on voice but is more sensitive (a lost client, "complicit"), and D3 is short and has no scene to film.

**Playbook note:** your playbook says "Platforms I deliver: LinkedIn only". You've asked for X, Instagram and video, so I've done it your way. **Want me to update the playbook** to add these platforms (for Maya only, or for all clients)?
> *Writer:* Nothing more to add.
Playbook left as is.

Rules carried over to every platform: **no hashtags** (your playbook), no emoji or exclamation marks (Maya, 4 of 4 samples), your banned words, same facts only. "Short video" = Instagram Reels (you didn't name TikTok or Shorts).

---

## X (242 / 280 characters)

> One of our bakery clients was binning about 18% of what they baked. They didn't know, because nobody counted the bin.
>
> We set them up with a clipboard by the back door. Six weeks later they were at 9%.
>
> That's not accounting, that's counting.

Single post, no thread: the story fits in one.

## Instagram (feed post)

**Photo first:** `[ASK CLIENT: a photo of the actual clipboard by the back door, if the bakery agrees. No signage, faces or anything that identifies the bakery.]`

**If there's no photo, 5-slide text carousel:**
1. A bakery was binning 18% of what they baked.
2. They didn't know. Nobody counted the bin.
3. With bakeries, the margins live in the waste.
4. So we set them up with a clipboard by the back door.
5. Six weeks later they were at 9%. That's not accounting, that's counting.

**Caption (336 / 2,200 characters; first line 72 characters, inside the ~125 shown before "more"):**

> Nobody counted the bin. So nobody knew 18% of the baking was going in it.
>
> It was one of our new bakery clients. We set them up with a sheet. Literally a clipboard by the back door.
>
> With bakeries, the margins live in the waste.
>
> Six weeks later they were at 9%.
>
> That's not accounting, that's counting. But it shows up in the accounts.

No call to action (Maya doesn't use them). No hashtags.

**Alt text:** `[ASK WRITER: write once the photo is chosen; describe only what is in it]`

## Short video: Instagram Reels script (about 25 seconds, Maya to camera)

| Time | Maya says |
|------|-----------|
| 0–3s (hook) | "One of our bakery clients was binning about 18% of what they baked." |
| 3–15s | "They didn't know. Nobody counted the bin. With bakeries, the margins live in the waste. So we set them up with a sheet. Literally a clipboard by the back door." |
| 15–20s (result) | "Six weeks later, they were at 9%." |
| 20–25s (close) | "That's not accounting, that's counting." |

**Shot list**
1. Maya to camera, close, for the hook.
2. `[ASK CLIENT: if the bakery agrees]` the clipboard by the back door, no signage or faces. Otherwise stay on Maya.
3. Maya to camera for the 9% and the closing line.
- Don't film anywhere that shows or hints at the new office (off-limits until signed).

**Caption:** "That's not accounting, that's counting." (no hashtags)

---

## Length check

Versions written to `clients/maya-lindqvist/repurposed/d1-versions.json`. Ran `python3 scripts/check_lengths.py repurposed/d1-versions.json`:

```
x.text: 242/280 ok
instagram.caption: 336/2200 ok
instagram: limits not officially verified, check in the composer
instagram_reels.caption: 39/2200 ok
instagram_reels.script: 334/1200 ok
instagram_reels: limits not officially verified, check in the composer

PASS
```

PASS on limits. Before posting, though, three things are still open and the checker doesn't see them (they sit in the photo note, shot list and alt text, not in the post text): the photo, the bakery's permission to film, and the alt text. Plus D1's own open questions. Treat these versions as **not ready** until those are answered.

Two edits I made while checking (before the run above): carousel slides 4 and 5 originally had colon reveals ("So: a clipboard…", "Six weeks later: 9%."), which are on the AI-tell list; and my first alt text described a photo that doesn't exist yet.

## Questions I asked (record)
- To the writer: update the playbook to add X / Instagram / Reels? → nothing more to add.
- To the client via `[ASK CLIENT]`: photo of the clipboard; bakery's permission to film/photograph.
- To the writer via `[ASK WRITER]`: alt text once the photo is chosen.
