# Test 2

**Prompt:** "Onboard a new client: Maya Lindqvist, founder of Fernhill."

(Then the ghostwriter provided Maya's 4 sample posts and `transcript.md`.)

---

## Output, part 1: before the material arrives

I've set up a client folder for Maya: `workspace/clients/maya-lindqvist/` with `voice-profile.md`, `stories.md`, `used.md`, `samples/` and `transcripts/`.

**Niche pack:** Fernhill is bookkeeping for food businesses. There's no pack for hospitality or bookkeeping in `references/niche-packs/` (only heritage restoration), so none is loaded. Want me to make one ("make a niche pack for hospitality bookkeeping")? I'd build it only from what you and Maya give me and mark anything I'm unsure of as unverified.

### Onboarding interview questions for Maya (45 minutes, your style)

Your three favourites lead, adapted for a first call; the rest fill gaps from the question bank. After every answer, your two digs: **"What was the number?"** and **"What happened next?"**

**Your questions**
1. "What did a client say this month that stuck with you?"
2. "What did you disagree with this month?"
3. "What number surprised you?" (this month, or ever, in a client's accounts)

**Who she is and who she talks to**
4. In one or two sentences, what does Fernhill do and who for?
5. Who do you most want reading your posts? Describe one real person.
6. What do you want those people to think or do after following you for six months?

**Origin and turning points**
7. What's the worst professional mistake you've made? What happened next?
8. Tell me about a client who changed how Fernhill works.

**Opinions**
9. What does most of the industry (accountants, bookkeepers) get wrong about food businesses?
10. What's something you believed five years ago that you no longer believe?
11. What question do restaurant owners ask you most? How do you answer it?

**Proof and boundaries**
12. Which results are you proudest of? Which numbers can I use publicly?
13. Which client stories can be told, named or anonymised? Which are off limits?
14. Which words or phrases do you hate seeing in posts?
15. Topics you never want to post about? How do you feel about emojis, hashtags, swearing, humour?
16. Do you want posts to mention that you work with a writer?

Over to you: run the call, then send me the transcript and 5–10 of Maya's own posts.

---

## Output, part 2: after the ghostwriter sent 4 sample posts and `transcript.md`

Thanks. Saved as `samples/post-1.md`…`post-4.md` and `transcripts/2026-10-03-monthly-call.md`.

**One thing to flag first:** the transcript is a *monthly* call (3 October), not the onboarding interview above. So several onboarding answers are missing: Maya's ideal reader, her six-month goal, words she hates, emoji/humour preferences, and whether to disclose that she works with a writer. I've built the profile from what's here, marked it **provisional**, and put `[ASK CLIENT]` wherever the onboarding answers would go. Only 4 samples (the skill asks for 5–10), so most rules rest on 3–4 posts.

### Step 2: measurable style

Ran `python3 scripts/voice_stats.py samples/`:

```
Samples: 4
Sentence length: average 8.0 words, typical range 1-16
Paragraph length: average 1.8 sentences; one-line paragraphs 59%
Per post: questions 0.2, exclamation marks 0.0, emoji 0.0, hashtags 0.0
Spelling signals: British-style 0, American-style 0 (rough; check by reading)
Most common sentence openers: they (2), it's (2), every (1), almost (1), they're (1), last (1), not (1), enough. (1), know (1), then (1), i (1), one (1)

First lines:
  post-1.md: Every restaurant owner I meet can tell me their best-selling dish.
  post-2.md: I started Fernhill with one laptop and two clients.
  post-3.md: Unpopular opinion: your accountant should be a bit annoying.
  post-4.md: Three things I check first in any café's accounts:
```

Reading notes on the numbers: the "1" at the bottom of the sentence range is partly the script counting post-4's list markers ("1.", "2.") as one-word sentences; "enough." shows the script doesn't strip full stops from openers. Spelling: the script found no signals, but £, "café", "Sunday roast" and "binning" make British spelling the right call.

### Voice profile (provisional)

Saved to `workspace/clients/maya-lindqvist/voice-profile.md`. On claude.ai, paste into Maya's Project knowledge.

```markdown
---
client: Maya Lindqvist
slug: maya-lindqvist
status: provisional
built_from: 4 samples, 1 transcript (monthly call, 3 October)
last_updated: 2026-10-30
---

# Maya Lindqvist: voice profile

## In one paragraph
Maya founded Fernhill, a 14-person bookkeeping firm that only works with food businesses (restaurants, cafés, and lately bakeries). She writes for owners who love feeding people, not spreadsheets. Reading her feels like a blunt, warm friend who has seen your accounts: short lines, one real number, a dry aside, then a plain verdict. She states things; she doesn't hedge or hype.

## Audience and goal
- Writing for: restaurant and café owners. Her words: "Restaurant owners get into the trade because they love feeding people. Nobody opens a restaurant because they love spreadsheets." (transcript [06:20]). [ASK CLIENT: describe one real person you most want reading your posts]
- After 6 months, readers should: [ASK CLIENT: not covered on the call; onboarding question 3]

## Measured style (from voice_stats.py, 4 samples)
- Sentence length: average 8.0 words, typical range 1-16 (the 1 is partly the script counting "1." list markers as sentences)
- Paragraph length: average 1.8 sentences; one-line paragraphs 59%
- Post length: 46-70 words (post-3: 46, post-4: 59, post-1: 64, post-2: 70)
- Questions per post: 0.2; exclamation marks per post: 0.0
- Emoji: none; hashtags: none
- Spelling: script found no signals. By reading: British context (£, "café", "Sunday roast"; transcript "binning", "Mad"). Use British spelling.

## Rules (each with evidence)
1. **Short paragraphs, one or two sentences, blank line between.** Evidence: "They're rarely the same dish." (post-1), seen in 4 of 4 samples.
2. **Open with a flat, concrete statement, never a question.** Evidence: "Every restaurant owner I meet can tell me their best-selling dish." (post-1); "I started Fernhill with one laptop and two clients." (post-2). Statement openers in 4 of 4.
3. **End on a short plain verdict, no question to readers, no call to action.** Evidence: "Know your numbers. Then decide." (post-1); "It's also the one that tells me if the business is actually working." (post-4). Seen in 4 of 4.
4. **Proof is a specific number from a real client or from Fernhill.** Evidence: "They put the price up by £2 and nobody blinked." (post-1); "one laptop and two clients" / "Nine years later we're fourteen people" (post-2); "Wages as a share of sales, week by week" (post-4). Seen in 3 of 4 (post-3 has none).
5. **Dry, understated humour, usually one line.** Evidence: "Family dinners were awkward for a while." (post-2); "your accountant should be a bit annoying" (post-3); "Number three is the one people get defensive about." (post-4). Seen in 3 of 4.
6. **States, doesn't hedge.** No "I think", "maybe", "perhaps" in 0 of 4 samples; certainty words like "Simple:" (post-2). Seen in 4 of 4. (On calls she does say "Now I think", transcript [04:16]: fine in quotes from her, but posts state.)
7. **Contractions throughout.** Evidence: "They didn't drop it." (post-1), "I'd rather" (post-2), "isn't" (post-3), "what's" (post-4). Seen in 4 of 4.
8. **Food businesses are the setting.** Evidence: "Every restaurant owner I meet" (post-1), "my aunt's café" (post-2), "any café's accounts" (post-4). Seen in 3 of 4.
9. **No emoji, no hashtags, no exclamation marks.** Seen in 4 of 4 (all counts 0.0).
10. **Clients are anonymous and treated kindly.** Evidence: "Last month a client found out..." (post-1). Seen in 1 of 4 samples, backed by transcript: "Just 'a client'." [02:14] and "Lovely people." [00:35]. (Rule because Maya stated it as a boundary.)

## Openings they use
- General observation about owners: "Every restaurant owner I meet can tell me their best-selling dish." (post-1)
- First-person origin: "I started Fernhill with one laptop and two clients." (post-2)
- Labelled opinion: "Unpopular opinion: your accountant should be a bit annoying." (post-3)
- List set-up: "Three things I check first in any café's accounts:" (post-4)

## Endings they use
- Two-beat instruction: "Know your numbers. Then decide." (post-1)
- Personal principle: "I'd rather be very good for a small group of people than average for everyone." (post-2)
- Definition: "It's someone who will say "this isn't working" while there's still time to fix it." (post-3)
- Payoff of the list: "It's also the one that tells me if the business is actually working." (post-4)

## Words and phrases
- They use: "know your numbers" (post-1), "the business is actually working" (post-4), "plain English" (transcript [00:35]), "costing you" (transcript [00:35]), "margins live in the waste" (transcript [02:44]), "counting" (transcript [02:44]), "doesn't feel like homework" (transcript [06:20]), "food businesses" (post-2), "a client" (post-1).
- They never use (from writer's playbook; nothing yet from Maya): "journey", "passionate", "excited to announce", "game-changer", "leverage", plus the skill's AI-tell list. [ASK CLIENT: onboarding question 14, words you hate seeing in posts]

## Signature moves
- Catchphrase: "That's not accounting, that's counting." (transcript [02:44]; "I say it all the time. My team are sick of it." [04:00]). Note: this has the "not X, Y" shape the skill bans as an AI tell. It is Maya's real spoken line, so it's kept as a quoted phrase only. Writer to confirm.
- Food-world comparisons for finance: "If my report takes longer to read than a menu, I've failed." (transcript [06:20]); "best-selling dish" vs "most profitable one" (post-1).
- Short beat after a number: "Not by much. Enough." (post-1).

## Opinions they hold
- Tell clients the hard truth early: "If I'd softened it, they'd have kept bleeding money and I'd have been complicit." (transcript [00:35]); "your accountant should be a bit annoying" (post-3)
- Software matters less than looking: "the software matters less than whether someone actually looks at the numbers every week" (transcript [04:16])
- Simplicity: "make the numbers so simple they don't feel like homework" (transcript [06:20])
- Specialise: "I'd rather be very good for a small group of people than average for everyone." (post-2)
- Bakeries: "the margins live in the waste" (transcript [02:44])

## Boundaries
- Off-limits topics: never identify clients ("never name them, not even 'a four-site café group in Leeds'... Just 'a client'", [02:14]). This month: no new office (not signed), nothing on VAT changes until guidance is final ([05:34]).
- Formats they dislike: [ASK CLIENT]
- Emoji / hashtags / humour / swearing preferences: [ASK CLIENT] (samples have none of emoji/hashtags)
- Disclosure preference for working with a writer: [ASK CLIENT]

## Client corrections
- none yet

## Notes (seen once, not yet rules)
- Rhetorical question mid-post: "If they never tell you anything you don't want to hear, what are you paying them for?" (post-3). 1 of 4.
- "Isn't X. It's Y." reveal: "Good bookkeeping isn't neat spreadsheets. It's someone who will say..." (post-3). 1 of 4. Flagged per rubric (AI-tell shape); confirm with Maya before treating as hers.
- Colon set-up: "Simple: I'd rather be..." (post-2); "Unpopular opinion:" (post-3).
- Numbers: spelled out in post-2 ("fourteen", "Nine years"), digits for money (post-1 "£2"). Mixed; no rule yet.
- Numbered list used once (post-4).

## Changelog
- 2026-10-30: built from samples/post-1..4.md and transcripts/2026-10-03-monthly-call.md. Provisional: no onboarding interview transcript yet.
```

### Step 3: story bank from the transcript

Saved to `workspace/clients/maya-lindqvist/stories.md`. Full transcript mining (with the 5 strongest angles for the month) is mode 4; ask "mine Maya's transcript" for that summary.

```markdown
---
client: Maya Lindqvist
last_updated: 2026-10-30
sources: transcripts/2026-10-03-monthly-call.md (call recorded 3 October); samples/post-1..4.md
---

# Maya Lindqvist: story bank

Background facts (from samples and transcript): Maya founded Fernhill, a bookkeeping firm for restaurants and cafés. Started "with one laptop and two clients" (post-2). "Nine years later we're fourteen people and we still only work with food businesses" (post-2). Transcript intro: "a 14-person bookkeeping firm for restaurants and cafés".

---

## S1. The café group that left after hearing the truth
- **Story:** A client (a café group with several sites) had a newest site losing about £2,000 a month, eleven months after opening. The owner kept calling it "still ramping up". Fernhill put it in the monthly pack in plain English: this site is costing you a salary. The owner got upset and said they were "just the bookkeepers". Two weeks later the client moved to another firm. Maya doesn't regret it.
- **Source:** transcript [00:35]–[02:14]
- **Exact phrases:**
  - "They left because we told them something they didn't want to hear."
  - "this site is costing you a salary"
  - "just the bookkeepers"
  - "If I'd softened it, they'd have kept bleeding money and I'd have been complicit."
  - "I don't regret it."
- **Post angles:**
  - Lesson from a moment: the line in the monthly pack ("this site is costing you a salary") and what it cost Fernhill, then the lesson (say it while there's time).
  - Contrarian: common belief "keep the client happy"; Maya: softening bad news makes you complicit.
  - Links to post-3's published opinion ("your accountant should be a bit annoying"): this is the real-world proof of it.
- **Needs checking / permissions:**
  - **Never name them.** Maya: "never name them, not even 'a four-site café group in Leeds'. People would work it out. Just 'a client'." Do NOT use: café group, four sites, Leeds. Use "a client" only. (Whether "a client with several sites" / "their newest site" is already too identifying: [ASK CLIENT: can we say the losing location was their newest site, or only "part of the business"?])
  - £2,000 a month and "eleven months in" are Maya's figures ("about £2,000"). Keep "about".
  - Fernhill lost the client in September (transcript [00:08]).

## S2. The bakery that counted its bin
- **Story:** One of Fernhill's new bakery clients was binning about 18% of what they baked and didn't know, because nobody counted the bin. Fernhill set them up with a sheet, "literally a clipboard by the back door". In six weeks waste was at 9%.
- **Source:** transcript [02:44]–[04:00]
- **Exact phrases:**
  - "The thing with bakeries is the margins live in the waste."
  - "nobody counted the bin"
  - "literally a clipboard by the back door"
  - "That's not accounting, that's counting. But it shows up in the accounts."
  - "I say it all the time. My team are sick of it."
- **Post angles:**
  - Lesson from a moment: the clipboard by the back door, 18% to 9% in six weeks; ending on "That's not accounting, that's counting."
  - List of three: three things she checks in a bakery's numbers, waste third. [ASK CLIENT: the other two]
  - Contrarian: belief that better margins need better software or price rises; Maya: a clipboard did it. (Pairs with S3, but keep to one idea per post.)
- **Needs checking:**
  - 18% → 9% in six weeks: Maya's figures ("about 18%"). Confirm we can publish them. [ASK CLIENT: OK to publish the 18% and 9% figures?]
  - Bakery not to be named unless Maya confirms permission.
  - "That's not accounting, that's counting" has the "not X, Y" shape the skill flags as an AI tell, but it's Maya's own spoken catchphrase. Writer to confirm it can be used verbatim.

## S3. Changed her mind on cloud software
- **Story/opinion:** Five years ago Maya would have told every client to move everything to the cloud straight away. Now she thinks the software matters less than whether someone actually looks at the numbers every week. She's seen people with beautiful dashboards they haven't opened since March.
- **Source:** transcript [04:16]–[05:30]
- **Exact phrases:**
  - "Five years ago I'd have told every client to move everything to the cloud tomorrow."
  - "the software matters less than whether someone actually looks at the numbers every week"
  - "beautiful dashboards who haven't opened them since March"
- **Post angles:**
  - Contrarian: "move everything to the cloud" → the weekly look matters more → what she does instead [ASK CLIENT: what does Fernhill do to make sure someone looks every week?].
  - Lesson from a moment: the dashboard not opened since March. [ASK CLIENT: one specific client this happened to, anonymised?]
  - "Belief I've changed" format, five years ago vs now.
- **Needs checking:** no specific client story yet, only a general observation. Don't name any software product.

## S4. Priya passed her final accountancy exam
- **Story:** Priya, on Maya's team, passed her final accountancy exam. She has been with Fernhill since she was 19. Maya "cried a bit".
- **Source:** transcript [05:53]
- **Exact phrases:** "she's been with us since she was 19", "I cried a bit"
- **Post angles:**
  - Lesson from a moment: the news landing, and what it says about growing people from 19.
  - Team post (not one of the writer's three formats; check before using).
- **Needs checking / permissions:**
  - "She's happy for me to mention her." Permission given for her first name. [ASK CLIENT: surname? Can we tag her? Which qualification body / exam?]
  - [ASK CLIENT: how many years has she been with Fernhill? What did she start doing?] (We only have "since she was 19".)
  - Whether "I cried a bit" can be published. [ASK CLIENT]

## S5. "If my report takes longer to read than a menu, I've failed"
- **Opinion:** Restaurant owners get into the trade because they love feeding people. Nobody opens a restaurant because they love spreadsheets. So Maya's job is to make the numbers so simple they don't feel like homework.
- **Source:** transcript [06:20]
- **Exact phrases:**
  - "Restaurant owners get into the trade because they love feeding people."
  - "Nobody opens a restaurant because they love spreadsheets."
  - "make the numbers so simple they don't feel like homework"
  - "If my report takes longer to read than a menu, I've failed."
- **Post angles:**
  - Contrarian: belief that a good bookkeeper gives you detailed reports; Maya: if it's longer than a menu, she's failed.
  - Lesson from a moment: [ASK CLIENT: a moment a client didn't read a report, or a report that worked because it was short?]
  - List of three: three things that go in a report shorter than a menu. [ASK CLIENT: what are they?]
- **Needs checking:** no specific scene yet.

## S6. Three new clients in September, all bakeries
- **Story fragment:** In September Fernhill took on three new clients, "all bakeries for some reason. Bakeries are having a moment." (Also lost one client: S1.)
- **Source:** transcript [00:08]
- **Exact phrases:** "Mad.", "all bakeries for some reason", "Bakeries are having a moment."
- **Post angles:**
  - List of three: three things she checks first in a bakery (waste is one: "the margins live in the waste"). [ASK CLIENT: the other two]
  - Observation post: why bakeries? [ASK CLIENT: any idea why bakeries are coming to you now?]
- **Needs checking:** thin. Needs more from Maya before it can carry a post on its own.

---

## Topics to avoid this month (from transcript [05:34])
- The new office: "Don't mention the new office. We haven't signed yet."
- VAT changes: "nothing about the VAT changes. I want to wait until the guidance is final."

## Already published (from samples; do not reuse)
- P1 (post-1): best-selling vs most profitable dish; client's Sunday roast losing money; price up £2.
- P2 (post-2): Fernhill origin, aunt's café and the café across the road; nine years, fourteen people, food businesses only.
- P3 (post-3): "your accountant should be a bit annoying".
- P4 (post-4): three things checked first in a café's accounts (wages weekly, waste, owner paying themselves).
```

### Step 4: three test posts for Maya to react to

First drafts in your formats and Maya's voice. Expect to edit them. They're for Maya to react to ("does this sound like you?"), so her corrections can go into the profile. Each picks a different story and format; the post-1…4 stories are treated as already published.

---

**Test post 1: lesson from a moment**

```
We lost a client in September.

Part of their business was losing about £2,000 a month.

Eleven months in, they were still calling it "ramping up".

So we put it in the monthly pack, in plain English: it was costing them a salary.

The owner was upset. Said we were "just the bookkeepers".

Two weeks later they moved to another firm.

I don't regret it.

If I'd softened it, they'd have kept bleeding money and I'd have been complicit.

Say it while there's still time to fix it.
```

- **Source:** S1, transcript [00:35]–[02:14] ("They left because we told them something they didn't want to hear"; "If I'd softened it, they'd have kept bleeding money and I'd have been complicit.")
- **Format used:** Lesson from a moment
- **Length:** 88 words; first line 6 words.
- **Voice check score:** 4.7 / 5 (Rhythm 5, Opening 5, Vocabulary 5, Stance 5, Substance 4 pass, No AI tells 4)
  - Substance passes (every fact is from the transcript), scored 4 because of the anonymity question below.
  - No AI tells 4: the last line echoes post-3's "while there's still time to fix it", which is Maya's own published phrase, so kept.
- **[ASK CLIENT]:**
  - Maya said "never name them, not even 'a four-site café group in Leeds'... Just 'a client'." I wrote "Part of their business" instead of "their newest site" / "four sites". Is "their newest site" OK, or is even that too identifying?
  - OK to publish "about £2,000 a month" and "eleven months in"?

---

**Test post 2: the contrarian**

```
Five years ago I had one answer for every client.

Move everything to the cloud. Tomorrow.

I've changed my mind.

The software matters less than whether someone actually looks at the numbers every week.

I've seen beautiful dashboards that haven't been opened since March.

[ASK CLIENT: what Fernhill does instead to make sure someone looks every week, e.g. "Now we..."]

Look every week. The software comes second.
```

- **Source:** S3, transcript [04:16] ("Five years ago I'd have told every client to move everything to the cloud tomorrow... the software matters less than whether someone actually looks at the numbers every week... beautiful dashboards who haven't opened them since March.")
- **Format used:** The contrarian (common belief → why she disagrees → what she does instead)
- **Length:** 51 words without the gap; under your 60-word minimum until Maya fills in "what she does instead".
- **Voice check score:** 4.3 / 5 (Rhythm 5, Opening 4, Vocabulary 4, Stance 5, Substance 4 pass with gap, No AI tells 4)
  - Opening 4: first line is reworded from her "I'd have told every client to move everything to the cloud tomorrow" to keep it under 12 words.
  - Vocabulary/No AI tells 4: "The software comes second." is my wording of her opinion, not her phrase.
- **[ASK CLIENT]:** what Fernhill does instead to make sure someone looks at the numbers every week (the third beat of your contrarian format is missing). Any specific client whose dashboard sat unopened since March (anonymised)?

---

**Test post 3: the contrarian**

```
Nobody opens a restaurant because they love spreadsheets.

Restaurant owners get into the trade because they love feeding people.

So my job is to make the numbers so simple they don't feel like homework.

[ASK CLIENT: what's actually in a Fernhill monthly report, and how long is it?]

A thicker report isn't better bookkeeping. [CHECK WITH CLIENT: our wording of her view]

The bar is simple.

If my report takes longer to read than a menu, I've failed.
```

- **Source:** S5, transcript [06:20] ("Nobody opens a restaurant because they love spreadsheets... make the numbers so simple they don't feel like homework. If my report takes longer to read than a menu, I've failed.")
- **Format used:** The contrarian
- **Length:** 56 words without the gap; under 60 until the gap is filled.
- **Voice check score:** 4.2 / 5 (Rhythm 5, Opening 5, Vocabulary 4, Stance 4, Substance 4 pass with gap, No AI tells 3)
  - "A thicker report isn't better bookkeeping." is my phrasing of the common belief she's arguing against, not her words; it also leans towards the "isn't X" reveal shape. Flagged rather than cut, because the contrarian format needs the belief stated. Replace with Maya's own words if she has them.
- **[ASK CLIENT]:** what's in a Fernhill monthly report and how long it is; confirm the "thicker report" line says what she means.

I couldn't make a **list of three** from this material without inventing the list: no part of the transcript gives three things Maya checks or believes. Questions for that are in the stories bank (S2, S5, S6).

### Used stories

Saved to `workspace/clients/maya-lindqvist/used.md`:

```markdown
---
client: Maya Lindqvist
last_updated: 2026-10-30
---

# Maya Lindqvist: used stories

| Story | Post | Status | Date |
|-------|------|--------|------|
| P1 Sunday roast / most profitable dish | samples/post-1.md | published (before onboarding) | before 2026-10 |
| P2 Fernhill origin, aunt's café | samples/post-2.md | published (before onboarding) | before 2026-10 |
| P3 "your accountant should be a bit annoying" | samples/post-3.md | published (before onboarding) | before 2026-10 |
| P4 three things checked in a café's accounts | samples/post-4.md | published (before onboarding) | before 2026-10 |
| S1 café group that left | Test post 1 "We lost a client in September." (lesson from a moment) | test post, sent to Maya for reaction | 2026-10-30 |
| S3 cloud software change of mind | Test post 2 "Five years ago I had one answer for every client." (contrarian) | test post, sent to Maya for reaction | 2026-10-30 |
| S5 report shorter than a menu | Test post 3 "Nobody opens a restaurant because they love spreadsheets." (contrarian) | test post, sent to Maya for reaction | 2026-10-30 |
```

### Open questions for you (the writer)
1. Maya's catchphrase **"That's not accounting, that's counting."** has the "not X, Y" shape the skill bans as an AI tell. It's her real spoken line (and you said "I love that"). OK to use it verbatim as her quote?
2. Post-3's "Good bookkeeping isn't neat spreadsheets. It's someone who..." has the same shape. Per the rubric I've kept it under Notes, not Rules, until Maya confirms she wrote it.
3. Still need the onboarding interview for: ideal reader, six-month goal, hated words, emoji/humour, disclosure.

When you edit these drafts, send me your version and I'll compare it with mine and add what changed as a rule in Maya's profile or your playbook.
