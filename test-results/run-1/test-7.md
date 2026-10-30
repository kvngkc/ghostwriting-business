# Test 7

**Prompt:** "Repurpose this for X, Instagram and a short video script." (using the strongest post from Test 4)

---

## Output

**Post used: Test 4, Draft A (the bakery bin, "Nobody at one of our bakeries counted the bin.").** It's the strongest of the three: the only one with no `[ASK CLIENT]` gaps in the text, a real before-and-after number (18% → 9% in six weeks), a physical scene (the clipboard) and Maya's own catchphrase to end on. Drafts B and C are mostly gaps.

**Before you use these:**
- The skill repurposes *approved* posts. Draft A isn't approved yet: Maya hasn't OK'd publishing 18% / 9%, and you haven't confirmed the catchphrase "That's not accounting, that's counting." (it has the "not X, Y" shape on the skill's AI-tell list). If either changes, these versions change with it.
- Your playbook says you deliver **LinkedIn only**. I've done these because you asked; tell me if you're adding platforms for Maya and I'll update the playbook.
- **Hashtags:** your playbook says no hashtags, and Maya uses none. The platform guide suggests up to 5 specific ones on Instagram and 3–5 on video captions. I've followed your rule (none). Optional, if you want them: #bakery #foodwaste #smallbusiness [ASK WRITER].
- **No call to action:** the guide suggests a soft CTA on Instagram, but Maya never ends with one (4 of 4 samples). Left out.

Same facts in every version, all from transcript [02:44]–[04:00]. Nothing added.

---

### X (single post, 197/280)

```
One of our bakeries was binning about 18% of what they baked. Nobody counted the bin.

We put a clipboard by the back door. Six weeks later they were at 9%.

That's not accounting, that's counting.
```

Single post, not a thread: the story fits in one and each extra post would be thin.

---

### Instagram feed post

**Photo first:** [ASK CLIENT: is there a photo of the clipboard by the back door? Don't show the bakery's name, signage or anything that identifies it unless the bakery agrees.] Without a photo, this works as the text carousel below.

**Caption (316/2200; first line is the hook, 46 characters):**

```
Nobody at one of our bakeries counted the bin.

They were binning about 18% of what they baked, and didn't know.

We set them up with a sheet. Literally a clipboard by the back door.

Six weeks later they were at 9%.

The thing with bakeries is the margins live in the waste.

That's not accounting, that's counting.
```

**Carousel outline (5 slides):**
1. Photo of the clipboard [ASK CLIENT] + text: "Nobody counted the bin."
2. "About 18% of what they baked went in it."
3. "So we put a clipboard by the back door."
4. "Six weeks later: 9%."
5. "That's not accounting, that's counting." (Maya's name, no CTA)

**Alt text:** [depends on the photo Maya supplies; describe what's in it, e.g. "A clipboard with a handwritten waste sheet hanging by a back door." only if that's what the photo shows]

---

### Short video script (Instagram Reels; also works for TikTok / YouTube Shorts)

For Maya to read to camera. About 15–20 seconds spoken, which is under the guide's 20–60 seconds; that's fine for one story, or she can add a line in her own words.

| Time | Maya says | Shot |
|------|-----------|------|
| 0–3s (hook) | "One of our bakeries was binning about 18% of what they baked." | Close-up of a full bin, or of Maya [ASK CLIENT: what footage exists / can be filmed] |
| 3–10s | "They didn't know. Nobody counted the bin. So we put a sheet by the back door. Literally a clipboard." | Close-up of the clipboard and a hand writing on it |
| 10–14s (result) | "Six weeks later, they were at 9%." | Maya to camera |
| 14–17s (close) | "That's not accounting, that's counting." | Maya to camera |

**Caption (73/2200):** `Nobody counted the bin. Six weeks with a clipboard: 18% waste down to 9%.`
**Hashtags:** none (your rule). If adding: #bakery #foodwaste #smallbusiness [ASK WRITER]
**If posting to YouTube Shorts:** title (under 100 chars): `The clipboard that halved a bakery's waste` [CHECK: "halved" is 18% → 9%, which is Maya's numbers; confirm she's happy with the word]

**Filming note:** shooting at the bakery would identify it. [ASK CLIENT: does the bakery agree to appear, or film the clipboard bit somewhere neutral?]

---

### Length check

Versions saved to `workspace/clients/maya-lindqvist/repurposed/2026-10-30-bakery-bin.json`. Ran `python3 scripts/check_lengths.py`:

```
x.text: 197/280 ok
instagram.caption: 316/2200 ok
instagram: limits not officially verified, check in the composer
instagram_reels.caption: 73/2200 ok
instagram_reels.script: 236/1200 ok
instagram_reels: limits not officially verified, check in the composer

PASS
```

All pass. Instagram limits aren't officially verified (per `platforms.json`); check in the composer before posting.
