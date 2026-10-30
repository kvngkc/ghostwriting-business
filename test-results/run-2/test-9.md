# Test 9

## 9a

**Prompt:** "Maya says 'That's not accounting, that's counting' is fine to use, it's her line. Also she'd rather the posts be 40 to 80 words like her own. Update what you need to."

---

Recorded both as client corrections. Conflict order applied: rule 2 (the client's own verified words and habits) over rule 3 (your playbook) and the skill's style defaults.

**What changed**
1. **Catchphrase:** approved for use verbatim. It's settled and I won't flag it again. The exception is for that exact line only; the "it's not X, it's Y" shape is still banned everywhere else in Maya's drafts.
2. **Length:** Maya's target is now **40–80 words**. This overrides your playbook's 60–150 for Maya only. Your playbook is unchanged and still applies to other clients. Want a line in the playbook noting that client profiles can set their own length? (Not needed for this to work.)
   > *Writer:* Nothing more to add.
3. **Knock-on effects:** D3 (46 words) and T2 (56) are no longer "short"; nothing needs padding or trimming. All current drafts sit inside 40–80 (D2 60, D3 46, T3 78).

**Updated `clients/maya-lindqvist/voice-profile.md`** (claude.ai: replace the Project's copy with this full file)

```markdown
---
client: Maya Lindqvist
slug: maya-lindqvist
status: provisional
built_from: 4 samples, 1 transcript (monthly call, 3 October); no onboarding interview yet
last_updated: 2026-10-30 (client corrections added)
---

# Maya Lindqvist: voice profile

## In one paragraph
Maya founded Fernhill, a 14-person bookkeeping firm that only works with food businesses (restaurants, cafés, bakeries). She writes for restaurant and café owners in short, plain lines with a concrete detail early and a blunt verdict at the end. She states rather than hedges, argues with habits rather than people, and lets a dry aside do the humour ("Family dinners were awkward for a while."). Reading her feels like a straight-talking friend who happens to know your numbers.

## Audience and goal
- Writing for: [ASK CLIENT: describe one real person you most want reading your posts]. Inferred from samples, to confirm: restaurant and café owners ("Every restaurant owner I meet", post-1; "any café's accounts", post-4).
- After 6 months, readers should: [ASK CLIENT]

## Measured style (from voice_stats.py, 4 samples)
- Post length: 46–70 words, average 60
- **Target length for drafts: 40–80 words** (Maya's stated preference, 2026-10-30; overrides the playbook's 60–150 for Maya only, under conflict rule 2)
- Sentence length: average 8.7 words, typical range 3–16
- Paragraph length: average 1.6 sentences; one-line paragraphs 59%
- Questions per post: 0.2; exclamation marks per post: 0
- Emoji: none; hashtags: none
- Spelling: British, inferred by reading (script found 0 spelling signals either way). Evidence: "£2" (post-1), "café" (post-2, post-4); in the transcript "binning", "Mad". [ASK CLIENT: confirm British spelling]

## Rules (each with evidence)
1. Short lines, mostly one sentence per paragraph. Evidence: "They're rarely the same dish." / "Not by much. Enough." (post-1); 59% one-line paragraphs. Seen in 4 of 4 samples.
2. The first line is a plain statement with a concrete noun, never a question. Evidence: "I started Fernhill with one laptop and two clients." (post-2). Seen in 4 of 4 samples (0 question openers).
3. Ends on a short verdict or instruction, never a question to readers. Evidence: "Know your numbers. Then decide." (post-1); "It's also the one that tells me if the business is actually working." (post-4). Seen in 4 of 4 samples.
4. A specific, real detail carries each post (a dish, a price, a person, a count). Evidence: "their famous Sunday roast was losing money on every plate" and "put the price up by £2" (post-1); "my aunt's café" (post-2); "Wages as a share of sales, week by week" (post-4). Seen in 4 of 4 samples.
5. States rather than hedges in posts: no "I think", "maybe", "perhaps". Evidence: "your accountant should be a bit annoying." (post-3). Seen in 4 of 4 samples. (She does say "Now I think..." when speaking, transcript 04:16, so a single "I think" in a changed-my-mind post is in character.)
6. Contractions throughout. Evidence: "They're", "didn't" (post-1); "we're", "don't", "I'd" (post-2); "isn't", "It's" (post-3); "What's", "It's" (post-4). Seen in 4 of 4 samples.
7. No emoji, no hashtags, no exclamation marks. Seen in 4 of 4 samples (counts all 0).
8. Clients appear anonymised as "a client" or by type. Evidence: "Last month a client found out..." (post-1); "any café's accounts" (post-4). Seen in 2 of 4 samples; matches her stated boundary (transcript 02:14).
9. Dry, understated humour, often a short aside. Evidence: "Family dinners were awkward for a while." (post-2); "your accountant should be a bit annoying." (post-3); "Number three is the one people get defensive about." (post-4). Seen in 3 of 4 samples.

## Openings they use
- Observation about owners: "Every restaurant owner I meet can tell me their best-selling dish." (post-1)
- Origin fact: "I started Fernhill with one laptop and two clients." (post-2)
- Labelled opinion: "Unpopular opinion: your accountant should be a bit annoying." (post-3)
- List set-up: "Three things I check first in any café's accounts:" (post-4)

## Endings they use
- Instruction: "Know your numbers. Then decide." (post-1)
- Personal principle: "I'd rather be very good for a small group of people than average for everyone." (post-2)
- Definition: "It's someone who will say "this isn't working" while there's still time to fix it." (post-3)
- Twist on the list: "It's also the one that tells me if the business is actually working." (post-4)

## Words and phrases
- They use: "numbers" ("Know your numbers", post-1; "looks at the numbers every week", "make the numbers so simple", transcript 04:16, 06:20); "food businesses" (post-2); "restaurant owner(s)" (post-1, transcript 06:20); "plain English" (transcript 00:35); "bleeding money" (transcript 00:35).
- They never use: [ASK CLIENT: words you hate seeing in posts]. Not seen in any sample: corporate jargon, "leverage", "journey", "passionate", "unlock" (all also banned by the writer's playbook).

## Signature moves
- Catchphrase: "That's not accounting, that's counting." (transcript 03:55; "I say it all the time. My team are sick of it.", 04:00). Its shape matches the skill's banned "it's not X, it's Y" pattern, but it is Maya's own verified line. **Decision (2026-10-30): approved for use verbatim.** Maya confirmed it's her line and fine to use. Settled; don't flag again. The exception covers this exact line only, not the "it's not X, it's Y" shape in general.
- Simple-over-clever framing: "If my report takes longer to read than a menu, I've failed." (transcript 06:20)
- Specialist pride: "I'd rather be very good for a small group of people than average for everyone." (post-2)

## Opinions they hold
- Tell clients the hard truth even if you lose them: "If I'd softened it, they'd have kept bleeding money and I'd have been complicit." (transcript, 00:35)
- Software matters less than looking: "Now I think the software matters less than whether someone actually looks at the numbers every week." (transcript, 04:16)
- In bakeries, waste is the margin: "The thing with bakeries is the margins live in the waste." (transcript, 02:44)
- Numbers should be simple: "Nobody opens a restaurant because they love spreadsheets." (transcript, 06:20)
- Your accountant should challenge you: "your accountant should be a bit annoying." (post-3)
- Specialise: "we still only work with food businesses." (post-2)

## Boundaries
- Off-limits topics:
  - Never name the client Fernhill lost in September, or give identifying detail: "never name them, not even 'a four-site café group in Leeds'. People would work it out. Just 'a client'." (transcript, 02:14)
  - The new office: "Don't mention the new office. We haven't signed yet." (transcript, 05:34) Check monthly.
  - VAT changes: "nothing about the VAT changes. I want to wait until the guidance is final." (transcript, 05:34) Check monthly.
- Cleared to mention: Priya, by name, passing her final accountancy exam (transcript, 05:53).
- Formats they dislike: [ASK CLIENT]
- Emoji, hashtags, swearing, humour: [ASK CLIENT] (samples use no emoji or hashtags)
- Disclosure preference for working with a writer: [ASK CLIENT]

## Client corrections
- 2026-10-30: "That's not accounting, that's counting." -> Maya: fine to use, it's her line. Approved verbatim (see Signature moves).
- 2026-10-30: draft length -> Maya would rather posts be 40 to 80 words, like her own. Target for Maya is now 40–80 words.

## Notes (seen once, not yet rules)
- "Unpopular opinion:" label as an opener (post-3).
- Numbered list (post-4).
- One mid-post rhetorical question: "If they never tell you anything you don't want to hear, what are you paying them for?" (post-3). Never as an opener or ending.
- Post-3 contains an "isn't X. It's Y" reveal: "Good bookkeeping isn't neat spreadsheets. It's someone who will say..." This is on the generic-AI-tell list. [ASK CLIENT: did you write post-3 yourself? If yes, this shape can stay as yours; until then, not used as a model.]

## Missing before this profile can be approved
- Fewer than 5 samples (have 4): [ASK CLIENT: 1–3 more posts you wrote yourself]
- No onboarding interview yet: audience, goal, words to avoid, emoji/hashtag/humour preferences, disclosure, results that can be used publicly.

## Changelog
- 2026-10-30: built from 4 samples (post-1 to post-4) and the 3 October monthly call transcript. Status provisional.
- 2026-10-30: client corrections: catchphrase approved; target length 40–80 words. Still provisional (onboarding interview and a 5th sample outstanding).
```

**`stories.md`**, one line in S2 updated (claude.ai: replace S2's "Needs checking" line):

```
- **Needs checking:** [ASK CLIENT: OK to post this story, anonymised? Permission was only discussed for S1 and Priya.] Confirm 18% and 9% and "six weeks". Catchphrase approved by Maya 2026-10-30 (see voice profile).
```

Playbook not changed.

## Questions I asked (record)
- To the writer: add a line to the playbook about per-client length? → nothing more to add.

---

## 9b

**Prompt:** "Draft 1 more post for Maya."

---

Mode: **5. Draft posts**.

**Story pick** (from `used.md`): S1, S6 are drafts, S3 is held by the D4 skeleton, S2 is published. That leaves **S4 (cloud software)**, which only has a test post, and **S5 (Priya)**. Priya's post needs the lesson from Maya (`[ASK CLIENT]`) and I won't invent one, so this is S4.

Maya still hasn't reacted to T2 (the S4 test post), so D5 builds on it: the dashboard image now comes before the verdict, and it ends on a short line instead of a second statement. First draft; expect to edit.

### D5. Contrarian: cloud software

> I've changed my mind about cloud software.
>
> Five years ago I'd have told every client to move everything to the cloud tomorrow.
>
> Now I've seen people with beautiful dashboards who haven't opened them since March.
>
> The software matters less than whether someone actually looks at the numbers.
>
> Every week.

- **Source:** S4; transcript [04:16] "Five years ago I'd have told every client to move everything to the cloud tomorrow. Now I think the software matters less than whether someone actually looks at the numbers every week. I've seen people with beautiful dashboards who haven't opened them since March."
- **Format used:** Contrarian. The common belief is her own old one (move everything to the cloud); why she changed (dashboards nobody opens); what she does instead (looking at the numbers every week).
- **Length:** 49 words (inside Maya's 40–80); first line 7 words
- **Voice check:** Rhythm 5, Opening 4 (a stance line rather than a scene, but concrete and under 12 words), Vocabulary 5, Stance 5 (her spoken "Now I think" dropped; her posts state rather than hedge, rule 5), Substance 5, No AI tells 5 → **4.8**. Your rules: no question opener ✓, repeatable last line ✓, no hashtags ✓, no banned words ✓, one idea ✓.
- **[ASK CLIENT]:** Happy to say this publicly? Any software partners who'd mind? A specific dashboard story would make it stronger (already on the November call sheet).

**`used.md`** (claude.ai: replace the Project's copy)

```markdown
# Maya Lindqvist: used stories

| Story | Post | Format | Status | Date | Numbers |
|-------|------|--------|--------|------|---------|
| S2 bakery bin | T1 (drafts/2026-10-30-test-posts.md) | Lesson from a moment | test | 2026-10-30 | |
| S4 cloud software | T2 (drafts/2026-10-30-test-posts.md) | Contrarian | test | 2026-10-30 | |
| S1 client we lost | T3 (drafts/2026-10-30-test-posts.md) | Lesson from a moment | test | 2026-10-30 | |
| S2 bakery bin | D1 (drafts/2026-10-30-drafts.md) | Lesson from a moment | published | 2026-10-30 (marked; went out this month, exact date not given) | 41 comments (best post of October) |
| S1 client we lost | D2 (drafts/2026-10-30-drafts.md) | Contrarian | draft | 2026-10-30 | |
| S6 report vs. menu | D3 (drafts/2026-10-30-drafts.md) | Statement (switched from list of three) | draft | 2026-10-30 | |
| S3 three new bakeries (+ growth numbers to come) | D4 skeleton (drafts/2026-10-30-drafts.md) | Lesson from a moment (planned) | draft (skeleton, waiting on numbers) | 2026-10-30 | |
| S4 cloud software | D5 (drafts/2026-10-30-drafts.md) | Contrarian | draft | 2026-10-30 | |

Test posts don't use up a story.
```

## Questions I asked (record)
- None to the writer. `[ASK CLIENT]` items listed under the draft.
