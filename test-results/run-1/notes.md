# Run 1: notes on SKILL.md and scripts

## Ambiguous, contradictory or hard to follow

1. **Banned "not X, Y" pattern vs the client's own catchphrase.** SKILL.md's style rules ban "it's not X, it's Y" reveals in every output, and the rubric says such patterns in samples were "probably written by a tool". But Maya's signature line, spoken on the call, is "That's not accounting, that's counting." and post-3 has "Good bookkeeping isn't neat spreadsheets. It's someone who...". "Match the client, not a house style" and "their process wins" pull the other way. No guidance on which wins when the pattern is verifiably the client's own speech. I kept the catchphrase as a quoted line and flagged it to the writer every time.

2. **Onboarding assumes an onboarding interview; the test supplied a monthly call.** Mode 2 step 2 builds the profile "once the writer has the transcript", implying the onboarding transcript. With only a monthly call, audience, 6-month goal, hated words, emoji/humour and disclosure answers are missing. Unclear whether to build a provisional profile or stop. I built a provisional one with [ASK CLIENT] markers.

3. **Mode 2 step 3 and mode 4 overlap.** Onboarding already fills `stories.md` "as in mode 4", so "Mine Maya's transcript" straight after has nothing new to do. Unclear whether onboarding should also output the "5 strongest angles" list. I put the full entries in onboarding and the summary + angles in Test 3.

4. **Do onboarding test posts count as "used"?** `used.md` is "which stories became which posts, so nothing repeats", and mode 5 says pick unused stories. Test posts are for client reaction, not publication. With one transcript (6 stories), counting them as used leaves only thin stories for "Draft 3 posts". I counted them as used (status "test post"), which forced two of the three Test 4 drafts to be mostly [ASK CLIENT] gaps.

5. **Sample count.** Rubric/mode 1 talk about 5–10 posts; only 4 samples given. Rules "seen once go under Notes", but there's no minimum for a Rule when the sample set is this small (most rules are "3 of 4" or "4 of 4").

6. **Writer's format vs available material.** The "list of three" format needs three items; the transcript never gives three. Nothing in SKILL.md says what to do when a requested format can't be filled honestly (skip it? skeleton with gaps?). I drafted a skeleton and flagged it.

7. **Writer's length minimum vs client's natural length.** Playbook says 60–150 words; Maya's own posts are 46–70 words, and several honest drafts fall below 60 once unsourced lines are removed. "Their process wins" vs "match the client" is unresolved. Not padded; flagged lengths instead.

8. **Repurposing beyond the playbook's platforms / rules.** Playbook: "LinkedIn only", "No hashtags". Platform guide recommends hashtags (Instagram up to 5, video 3–5) and a soft CTA; the client never uses CTAs. Unclear whether the writer's "no hashtags" is LinkedIn-only or global. I used none and offered optional ones.

9. **Mode 7 says "an approved post".** The test asked to repurpose a first draft. No guidance for unapproved input; I proceeded and flagged the pending approvals.

10. **"Short video script" platform.** `platforms.json` has tiktok, youtube_shorts and instagram_reels with different fields (Shorts needs a title). The checker needs one platform name. I picked instagram_reels (matches the Instagram ask) and gave a Shorts title separately (not length-checked by the script).

11. **Platform guide is heritage-flavoured.** Audience lines, examples ("This wall was killed by cement", #limemortar), "script for the owner to read on site" are written for the heritage niche, in a generic reference file. Had to translate for a bookkeeper.

12. **Monthly report: "best comment or conversation" vs writer's format.** The skill's report includes it; the writer's reporting format (playbook) doesn't, and no comment was supplied. Rule 1 says the playbook wins, but the skill lists it as a required section. Left as [ASK WRITER].

13. **Report needs data the studio doesn't track.** "What went out" needs the list of published posts, but `used.md` has no clear "published" step in any mode, so after drafting the studio can't know which 8 posts went out. A "mark as published" step is missing.

14. **Voice check scoring.** "Score 1 to 5 on each line, then average": unclear if "line" means each check row or each line of the draft. "Fix lines scoring below 4" (mode 5) reads like draft lines. I scored per check row and listed failing draft lines separately.

15. **Setup mode: "ask for real examples".** The writer gave descriptions but no example posts/hooks. The skill says write the playbook "from their answers and examples only" but doesn't say whether to block until examples arrive. I wrote it with gaps marked.

16. **Where things live in Claude Code.** "Each client gets a folder" but no layout is given for the playbook vs client folders, nor where call sheets, reports or repurposed versions go. I used `workspace/playbook.md` and `workspace/clients/maya-lindqvist/{calls,reports,repurposed}/`.

## Script output and issues

### voice_stats.py (ran without error)
```
Samples: 4
Sentence length: average 8.0 words, typical range 1-16
Paragraph length: average 1.8 sentences; one-line paragraphs 59%
Per post: questions 0.2, exclamation marks 0.0, emoji 0.0, hashtags 0.0
Spelling signals: British-style 0, American-style 0 (rough; check by reading)
Most common sentence openers: they (2), it's (2), every (1), almost (1), they're (1), last (1), not (1), enough. (1), know (1), then (1), i (1), one (1)
```
Issues (no crash):
- Numbered list markers ("1.", "2.", "3." in post-4) are split off as one-word sentences, dragging the sentence-length floor to 1 and the average down.
- Openers aren't stripped of full stops: "enough." is counted as an opener token.
- The spelling detector found nothing despite clearly British text (£, "café"); signals are limited to a fixed word list. Fine as documented ("rough"), but it returned no useful signal here.
- It doesn't report words per post, though the playbook's length rule needs it (I used `wc -w`: 46, 59, 64, 70).

### check_lengths.py (ran without error)
```
x.text: 197/280 ok
instagram.caption: 316/2200 ok
instagram: limits not officially verified, check in the composer
instagram_reels.caption: 73/2200 ok
instagram_reels.script: 236/1200 ok
instagram_reels: limits not officially verified, check in the composer

PASS
```
Issues (no crash):
- The `[CHECK` scan only flags `[CHECK`, not `[ASK CLIENT` markers, so a version with unresolved client questions would PASS silently.
- Thread posts are checked against `fields.text.max`; a platform without a `text` field (e.g. instagram) would KeyError if a `thread` key were supplied. Not hit in this run.
