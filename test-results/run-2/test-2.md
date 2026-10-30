# Test 2

**Prompt:** "Onboard a new client: Maya Lindqvist, founder of Fernhill."

---

Mode: **2. Onboard a client**. Client folder created: `clients/maya-lindqvist/` (samples/, transcripts/, calls/, drafts/, repurposed/, reports/).

## Step 1. Interview questions for Maya's 45-minute onboarding call

Your own questions and digging rules come first (from your playbook), then gaps filled from the skill's question bank. There's no niche pack for hospitality or bookkeeping, so no pack questions are added. (I can build a "hospitality finance" pack if you want one.)

**From your playbook**
1. "What did a client say this month that stuck with you?"
2. "What did you disagree with this month?"
3. "What number surprised you?"
   - Every answer: ask for the number, and ask "what happened next?"

**Filling the gaps (onboarding)**
4. In one or two sentences, what does Fernhill do and who for?
5. Who do you most want reading your posts? Describe one real person.
6. What do you want those people to think or do after following you for six months?
7. How did you end up doing this work? What was the moment you decided? (She's already published the "one laptop, two clients" origin, so push for something new: what happened next?)
8. What is the worst professional mistake you have made, and what did it teach you?
9. What does most of the hospitality finance world get wrong?
10. What question do restaurant owners ask you most? How do you answer it?
11. Which results are you proudest of? Which numbers can I use publicly?
12. Which client stories can be told, named or anonymised? Which are off limits?
13. Which words or phrases do you hate seeing in posts?
14. How do you feel about emojis, hashtags, swearing, humour?
15. Do you want posts to mention that you work with a writer?

**Please send me Maya's writing samples (5–10 posts she wrote herself) and any call transcript.**

> *Writer provides:* `post-1.md` to `post-4.md` (Maya's own past posts) and `transcript.md` (monthly call, 3 October).

Saved to `clients/maya-lindqvist/samples/` and `clients/maya-lindqvist/transcripts/2026-10-03-monthly-call.md`.

## Step 2. Voice profile

Ran `python3 scripts/voice_stats.py clients/maya-lindqvist/samples`:

```
Samples: 4
Post length: 46-70 words, average 60
Sentence length: average 8.7 words, typical range 3-16
Paragraph length: average 1.6 sentences; one-line paragraphs 59%
Per post: questions 0.2, exclamation marks 0.0, emoji 0.0, hashtags 0.0
Spelling signals: British-style 0, American-style 0 (rough; check by reading); currency signs: £ 1, $ 0
Most common sentence openers: they (2), it's (2), every (1), almost (1), they're (1), last (1), not (1), enough (1), know (1), then (1), i (1), one (1)

First lines:
  post-1.md: Every restaurant owner I meet can tell me their best-selling dish.
  post-2.md: I started Fernhill with one laptop and two clients.
  post-3.md: Unpopular opinion: your accountant should be a bit annoying.
  post-4.md: Three things I check first in any café's accounts:
```

Note: the script found no British/American spelling signals at all (these four posts contain none of its stem words), so spelling is inferred by reading: "£", "café", and "binning" in the transcript point to British.

Only 4 samples and no onboarding interview yet, so the profile is **status: provisional**. I've built it anyway and listed what's missing as `[ASK CLIENT]`.

**File: `clients/maya-lindqvist/voice-profile.md`** (claude.ai: paste into Maya's Project knowledge, replacing any earlier version)

```markdown
---
client: Maya Lindqvist
slug: maya-lindqvist
status: provisional
built_from: 4 samples, 1 transcript (monthly call, 3 October); no onboarding interview yet
last_updated: 2026-10-30
---

# Maya Lindqvist: voice profile

## In one paragraph
Maya founded Fernhill, a 14-person bookkeeping firm that only works with food businesses (restaurants, cafés, bakeries). She writes for restaurant and café owners in short, plain lines with a concrete detail early and a blunt verdict at the end. She states rather than hedges, argues with habits rather than people, and lets a dry aside do the humour ("Family dinners were awkward for a while."). Reading her feels like a straight-talking friend who happens to know your numbers.

## Audience and goal
- Writing for: [ASK CLIENT: describe one real person you most want reading your posts]. Inferred from samples, to confirm: restaurant and café owners ("Every restaurant owner I meet", post-1; "any café's accounts", post-4).
- After 6 months, readers should: [ASK CLIENT]

## Measured style (from voice_stats.py, 4 samples)
- Post length: 46–70 words, average 60
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
- Catchphrase: "That's not accounting, that's counting." (transcript 03:55; "I say it all the time. My team are sick of it.", 04:00). Its shape matches the skill's banned "it's not X, it's Y" pattern, but it is Maya's own verified line. **Writer's decision: pending** (flagged 2026-10-30; writer had nothing to add). Used in drafts until the writer says otherwise.
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
- None yet.

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
```

## Step 3. Transcript mined into the story bank

**File: `clients/maya-lindqvist/stories.md`** (claude.ai: paste into Maya's Project knowledge)

```markdown
# Maya Lindqvist: story bank

Source key: `transcripts/2026-10-03-monthly-call.md` (monthly call, recorded 3 October). Timestamps are from that file.

---

## S1. The client we lost for telling the truth
- **Story:** A client (anonymise as "a client" only) had a site that was losing about £2,000 a month, eleven months after opening; they kept calling it "still ramping up". Fernhill put it in the monthly pack in plain English: it was costing them a salary. The owner got upset and called them "just the bookkeepers". Two weeks later the client moved to another firm. Maya doesn't regret it.
- **Source:** transcript [00:35]; permission to post at [02:14].
- **Exact phrases:** "They left because we told them something they didn't want to hear." / "still ramping up" / "this site is costing you a salary" / "just the bookkeepers" / "I don't regret it." / "If I'd softened it, they'd have kept bleeding money and I'd have been complicit."
- **Post angles:**
  - Lesson from a moment: the line in the monthly pack, the walk-out, and why she'd do it again.
  - Contrarian: "Keep the client happy" vs. Maya's view that softening bad news makes her complicit.
  - Lesson from a moment: "just the bookkeepers": what a bookkeeper's job actually is.
- **Needs checking:** Maya said "never name them, not even 'a four-site café group in Leeds'… Just 'a client'." So no café group, no four sites, no city. [ASK CLIENT: is "their newest site" too identifying? Drafts avoid it until you say.] Confirm "about £2,000 a month" and "eleven months" can be published.

## S2. The bakery that counted its bin
- **Story:** One of Fernhill's bakery clients was binning about 18% of what it baked and didn't know, because nobody counted the bin. Fernhill set them up with a sheet ("literally a clipboard by the back door"). In six weeks waste was down to 9%.
- **Source:** transcript [02:44]–[04:00].
- **Exact phrases:** "The thing with bakeries is the margins live in the waste." / "nobody counted the bin" / "literally a clipboard by the back door" / "That's not accounting, that's counting. But it shows up in the accounts." / "I say it all the time. My team are sick of it." [04:00]
- **Post angles:**
  - Lesson from a moment: the clipboard by the back door, 18% to 9% in six weeks.
  - Contrarian: people think margins live in pricing; in bakeries they live in the waste.
  - Lesson from a moment: "That's not accounting, that's counting." (the simplest fix is often counting).
- **Needs checking:** [ASK CLIENT: OK to post this story, anonymised? Permission was only discussed for S1 and Priya.] Confirm 18% and 9% and "six weeks". Catchphrase shape: see voice profile (writer's decision pending).

## S3. Three new clients, all bakeries
- **Story:** In September Fernhill lost one client and took on three new ones, all bakeries. "Bakeries are having a moment."
- **Source:** transcript [00:08].
- **Exact phrases:** "Mad." / "We lost a client, which hurt" / "all bakeries for some reason. Bakeries are having a moment."
- **Post angles:**
  - Lesson from a moment: a month of one loss and three bakeries.
  - List of three: [ASK CLIENT: what are the three things you check first in a bakery's accounts?] (only waste is known so far).
- **Needs checking:** Why bakeries? [ASK CLIENT: what's behind it?] Thin on its own; better as context for S2.

## S4. Changed her mind on cloud software
- **Story:** Five years ago Maya would have told every client to move everything to the cloud straight away. Now she thinks the software matters less than whether someone looks at the numbers every week. She has seen owners with beautiful dashboards they haven't opened since March.
- **Source:** transcript [04:16]–[05:30].
- **Exact phrases:** "Five years ago I'd have told every client to move everything to the cloud tomorrow." / "the software matters less than whether someone actually looks at the numbers every week" / "beautiful dashboards who haven't opened them since March"
- **Post angles:**
  - Contrarian: better software won't fix your numbers; looking at them every week will.
  - Lesson from a moment: the beautiful dashboard nobody opened since March.
- **Needs checking:** Flag: this could read as a dig at software vendors or at clients who own the dashboards. [ASK CLIENT: happy to say this publicly? Any software partners who'd mind?] No example client or number yet: [ASK CLIENT: a specific dashboard story?]

## S5. Priya passed her final exam
- **Story:** Priya, at Fernhill since she was 19, passed her final accountancy exam. Maya "cried a bit". Priya is happy to be mentioned.
- **Source:** transcript [05:53].
- **Exact phrases:** "she's been with us since she was 19. I cried a bit."
- **Post angles:**
  - Lesson from a moment: the day Priya passed. [ASK CLIENT: what did it teach you, or what does it say about how you build the team?]
  - Specialist pride (as in post-2): growing people inside a small firm.
- **Needs checking:** [ASK CLIENT: which qualification? how many years has Priya been at Fernhill? Does Priya want her surname or tag?] Permission given for name.

## S6. If my report takes longer to read than a menu
- **Story:** (Opinion, no scene.) Restaurant owners get into the trade because they love feeding people, not spreadsheets, so Maya's job is to make the numbers so simple they don't feel like homework.
- **Source:** transcript [06:20].
- **Exact phrases:** "Nobody opens a restaurant because they love spreadsheets." / "make the numbers so simple they don't feel like homework" / "If my report takes longer to read than a menu, I've failed."
- **Post angles:**
  - Contrarian: [ASK CLIENT: what does the usual bookkeeping report look like that you're arguing against?]
  - Statement post in her own sample shape (opener, reason, verdict), ending on the menu line.
- **Needs checking:** Nothing numeric. A scene would make it stronger: [ASK CLIENT: an owner's reaction to a short report?]

---

## Already published by Maya (from samples; don't repeat)
- Sunday roast losing money, price up £2 (post-1)
- Started with one laptop and two clients: her aunt's café and the café across the road; nine years later fourteen people, food businesses only (post-2)
- "Your accountant should be a bit annoying" (post-3)
- Three things she checks first in a café's accounts (post-4)

## Off-limits this month
- The new office (not signed yet) [05:34]
- VAT changes (waiting for final guidance) [05:34]
- Any identifying detail of the client lost in September [02:14]
```

**5 strongest angles for this month**
1. S2 bakery bin, lesson from a moment: a clipboard, 18% to 9% in six weeks, and her own catchphrase. Concrete, numeric, visual.
2. S1 the client we lost, lesson from a moment: a real cost (lost a client) for a principle she already posts about ("your accountant should be a bit annoying"). Strong, and she's cleared it anonymised.
3. S4 cloud software, contrarian: a genuine change of mind, with a vivid line ("dashboards… haven't opened them since March").
4. S6 report shorter than a menu: her clearest statement of why Fernhill exists; ends on a repeatable line.
5. S5 Priya: warm, cleared by name; needs the lesson from Maya before it's a post.

**Off-limits:** the new office, VAT changes, any identifying detail of the lost client.

**Opinions she might not want public:** "I'd have been complicit" (S1) is strong language about an ex-client; the cloud-software reversal (S4) could read as a dig at software vendors or at clients with unused dashboards. Both flagged `[ASK CLIENT]` in stories.md.

## Flags for you (raised once)

1. **Catchphrase vs. banned pattern.** "That's not accounting, that's counting." has the "it's not X, it's Y" shape that the skill bans, but it's Maya's own verified line ("I say it all the time", 04:00). Conflict order applied: rule 2 (client's own verified words) over the style defaults, so I've used it verbatim in test post T1. **Your decision?** Keep using it, or leave it out?
   > *Writer:* Nothing more to add.
   Recorded in the voice profile as "Writer's decision: pending". I won't raise it again unless you do.
2. **Length.** Your playbook says 60–150 words; Maya's own posts are 46–70 words (average 60). Conflict order applied: rule 2 (the client's own habits) sits above rule 3 (your playbook), so I've written to the overlap, roughly 60–80 words, which keeps her rhythm and stays inside your range. **Your call:** 60–80 for Maya, or her own 46–70?
   > *Writer:* Nothing more to add.
   Using 60–80 for now; T2 came out at 56 and I left it short rather than pad.
3. **Post-3 has an AI-tell shape** ("Good bookkeeping isn't neat spreadsheets. It's someone who…"). I haven't modelled drafts on that line until Maya confirms she wrote it (`[ASK CLIENT]` in the profile).

## Step 4. Three test posts for Maya to react to

First drafts, written in your formats from the story bank. Marked `test` in `used.md`; they don't use up the stories. Expect to edit.

**File: `clients/maya-lindqvist/drafts/2026-10-30-test-posts.md`**

---

### T1. Lesson from a moment: the bakery bin

> A bakery client was binning about 18% of what they baked.
>
> They didn't know. Nobody counted the bin.
>
> With bakeries, the margins live in the waste.
>
> So we set them up with a sheet. Literally a clipboard by the back door.
>
> Six weeks later they were at 9%.
>
> That's not accounting, that's counting.
>
> But it shows up in the accounts.

- **Source:** S2; transcript [02:44] "they were binning about 18%… literally a clipboard by the back door, and in six weeks they were at 9%. That's not accounting, that's counting. But it shows up in the accounts."
- **Format used:** Lesson from a moment
- **Length:** 60 words; first line 11 words
- **Voice check:** Rhythm 5, Opening 5, Vocabulary 5, Stance 5, Substance 5, No AI tells 5 (catchphrase is Maya's verified line, used under conflict rule 2) → **5.0**. Your rules: hook under 12 words ✓, no question opener ✓, repeatable last line ✓, no hashtags ✓, no banned words ✓, one idea ✓.
- **[ASK CLIENT]:** OK to post this story (anonymised)? Are "about 18%", "9%" and "six weeks" right to publish?

### T2. Contrarian: cloud software

> I've changed my mind about cloud software.
>
> Five years ago I'd have told every client to move everything to the cloud tomorrow.
>
> Now I think the software matters less than whether someone actually looks at the numbers every week.
>
> I've seen people with beautiful dashboards who haven't opened them since March.
>
> Someone has to actually look.

- **Source:** S4; transcript [04:16] "Five years ago I'd have told every client to move everything to the cloud tomorrow. Now I think the software matters less than whether someone actually looks at the numbers every week. I've seen people with beautiful dashboards who haven't opened them since March."
- **Format used:** Contrarian. The "common belief" is Maya's own old belief (move everything to the cloud), because she didn't say who else holds it.
- **Length:** 56 words (**short**: under your 60 minimum, inside Maya's 46–70; not padded); first line 7 words
- **Voice check:** Rhythm 4 (one 17-word sentence, just over her typical 16), Opening 4, Vocabulary 5, Stance 4 ("Now I think" is a hedge, but it's her spoken phrasing), Substance 5, No AI tells 5 → **4.5**. Fixed during the check: my first ending, "The software isn't the hard part. Looking every week is.", was an "isn't X, Y is" reveal; replaced with "Someone has to actually look."
- **[ASK CLIENT]:** Happy to say this publicly (software partners)? A specific dashboard story would make it stronger.

### T3. Lesson from a moment: the client we lost

> We lost a client in September.
>
> We told them something they didn't want to hear.
>
> Part of their business had been losing about £2,000 a month. Eleven months in, they were still calling it "ramping up".
>
> So we wrote it in plain English in the monthly pack. This is costing you a salary.
>
> They said we were "just the bookkeepers". Two weeks later they'd moved firms.
>
> I don't regret it.
>
> If I'd softened it, I'd have been complicit.

- **Source:** S1; transcript [00:35] "They left because we told them something they didn't want to hear. Their newest site was losing about £2,000 a month… Eleven months in… this site is costing you a salary… 'just the bookkeepers'. Two weeks later they moved to another firm. I don't regret it. If I'd softened it… I'd have been complicit." Permission [02:14].
- **Format used:** Lesson from a moment
- **Length:** 78 words; first line 6 words
- **Voice check:** Rhythm 4 (above her 70-word max, inside your range), Opening 5, Vocabulary 5, Stance 5, Substance 5, No AI tells 5 → **4.8**
- **[ASK CLIENT]:** Maya asked for "just a client", so I wrote "part of their business" instead of "their newest site". OK to say "site", or keep it vague? OK to publish £2,000 and eleven months? Comfortable with "complicit" in public?

---

**File: `clients/maya-lindqvist/used.md`**

```markdown
# Maya Lindqvist: used stories

| Story | Post | Format | Status | Date | Numbers |
|-------|------|--------|--------|------|---------|
| S2 bakery bin | T1 (drafts/2026-10-30-test-posts.md) | Lesson from a moment | test | 2026-10-30 | |
| S4 cloud software | T2 (drafts/2026-10-30-test-posts.md) | Contrarian | test | 2026-10-30 | |
| S1 client we lost | T3 (drafts/2026-10-30-test-posts.md) | Lesson from a moment | test | 2026-10-30 | |

Test posts don't use up a story.
```

## Next
- Send T1–T3 to Maya for her reactions (Google Doc, per your playbook).
- Book the 45-minute onboarding call using the questions above; the profile stays provisional until then and until there are 5+ samples.

## Questions I asked (record)
- To the writer: "Please send me Maya's writing samples and any call transcript." → provided (4 posts + transcript).
- To the writer: catchphrase decision → nothing more to add (pending).
- To the writer: 60–80 or 46–70 words for Maya → nothing more to add.
- To the client (via `[ASK CLIENT]`, for the writer to pass on): audience; 6-month goal; British spelling; words she hates; emoji/hashtags/humour; disclosure; formats she dislikes; 1–3 more samples; whether she wrote post-3; permission for S2; 18%/9%/six weeks; "site" wording and £2,000/eleven months for S1; "complicit"; S4 public and any software partners; S4 dashboard story; why bakeries; three things she checks in a bakery's accounts; Priya's qualification, years, surname; a scene for S6.
