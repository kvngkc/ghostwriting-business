# Run 2 notes

## Setup
- The instructions said to create `claude/skill-test-run-2` from main. The branch already existed locally and on origin, one commit ahead of main (6899492, "Fix issues found in skill test run 1", which changes SKILL.md, the platform guide and both scripts). I didn't reset it, because that would have thrown that commit away. All tests ran against the skill as it is on this branch, and the results are committed on top of 6899492.
- Only the allowed inputs under `launch/` were read. Nothing under `test-results/` existed before this run.

## Ambiguous, contradictory or hard-to-follow parts of SKILL.md

1. **Length: is it a client "habit" (rule 2) or a playbook rule (rule 3)?** The playbook says 60–150 words; Maya's samples are 46–70. The conflict order puts "the client's own verified words and habits" above the playbook, but it doesn't say whether post length counts as a habit. I wrote to the overlap (60–80) and flagged it. Test 9 later settled it (40–80).
2. **Catchphrase flag when the writer doesn't decide.** Rule 2 says "Flag it to the writer once, record their decision… and don't raise it again." It doesn't say what to do while no decision has been made: use it or hold it back? I used it (rule 2 allows it) and recorded "pending".
3. **Rule 2 vs. the rubric's "Patterns that do not belong in any profile".** Rule 2 says a phrase the client "really says or wrote" can be used even if its shape is banned. The rubric says that if a *sample* contains such a pattern, it "was probably written by a tool or a previous writer; confirm with the client". Maya's post-3 has "Good bookkeeping isn't neat spreadsheets. It's someone who…". Is a sample "the client's own verified words" or suspect? I treated it as suspect and asked the client.
4. **Test posts and real drafts from the same stories.** Test posts "don't use up a story", but the skill doesn't say whether real drafts should wait for the client's reactions to the test posts, or should avoid near-duplicates of them. With only six stories, test 4 and test 9 had to reuse test-post stories. I took different angles and said so.
5. **Contrarian format with no stated "common belief".** Several stories only work as contrarian posts if the belief is the client's own old view, or something someone said to her ("just the bookkeepers"). The skill's "can't be filled honestly → switch format" rule doesn't say whether that counts. I used it and said so in "Format used".
6. **No guidance for the writer's own editing rules in a voice check.** Mode 6 says to score the rubric rows "plus the writer's own editing rules", but there's no row or scale for them. I reported them as pass/fail lines.
7. **Mark as published:**
   - (a) Nothing says what to do if the post was never `approved` (D1 went straight from draft to published).
   - (b) "With the date": the writer said "this month" with no day, so I used today's date and noted it.
8. **Monthly report vs. `used.md`.** Mode 9 says the report reads from `used.md`, but the writer gave "Posts published: 8" while `used.md` had 1. There's no guidance on which wins, or on whether to ask for the missing posts. I used the writer's figure and flagged the gap.
9. **Onboarding with a monthly-call transcript.** Mode 2 assumes an onboarding interview. The only transcript was a monthly call, and the skill doesn't say whether that counts as "an onboarding interview". I treated it as not one (profile provisional).
10. **The "concrete" hook rule vs. a catchphrase opener.** It's unclear whether a client's catchphrase as a first line meets "concrete". I scored Opening 4.
11. **claude.ai "give the updated file in full".** For one-line changes (used.md rows, one stories.md line), giving the whole file every time is heavy. I gave whole files after big changes and the changed line after small ones. The skill could say whether that's acceptable.
12. **Playbook "LinkedIn only" vs. a repurpose request.** Handled by rule 1 ("do it their way and offer to update the playbook"), but mode 7 itself doesn't mention checking the playbook's platform list.
13. **Relative dates in drafts** ("in September") go stale between drafting and posting. There's no guidance; I flagged it on D2.

## Script output (no errors)

`voice_stats.py` ran without error. Note: it reported 0 British / 0 American spelling signals for these samples, so spelling had to be inferred by reading (£, café).

```
$ python3 skills/ghostwriter-studio/scripts/voice_stats.py test-results/run-2/workspace/clients/maya-lindqvist/samples
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

`check_lengths.py` ran without error (exit 0 both times; the second run is after fixing colon reveals and the alt text, which the script doesn't check):

```
$ python3 skills/ghostwriter-studio/scripts/check_lengths.py repurposed/d1-versions.json
x.text: 242/280 ok
instagram.caption: 336/2200 ok
instagram: limits not officially verified, check in the composer
instagram_reels.caption: 39/2200 ok
instagram_reels.script: 334/1200 ok
instagram_reels: limits not officially verified, check in the composer

PASS
(exit 0)
```

**Limitation found:** `check_lengths.py` only scans the fields listed in platforms.json (text / caption / script / title / description, plus thread). The skill also asks for a photo note, an alt text and a shot list, and those had nowhere to go but extra JSON keys (`photo_note`, `alt_text`, `shot_list`, `carousel_fallback`). Those keys contain `[ASK CLIENT]` / `[ASK WRITER]` notes, but they aren't scanned, so the script printed PASS instead of NOT READY. The JSON format in SKILL.md (`{"versions":[{"platform":"x","text":"..."}]}`) doesn't define fields for these.
