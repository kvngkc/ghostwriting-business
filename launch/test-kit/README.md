# Test Kit: Ghostwriter Studio

Everything needed to test the skill on claude.ai without real client data. The client, **Maya Lindqvist of Fernhill** (a bookkeeping firm for restaurants and cafés), is fictional.

| File | Use it for |
|------|-----------|
| `my-process-answers.md` | Sample answers for the studio setup interview. Better: answer with your real process. |
| `client-samples/post-1.md` … `post-4.md` | Maya's "own" past posts, for building her voice profile |
| `transcript.md` | Maya's monthly call, for mining, drafting and call prep |

Allow about 45 minutes. Do it on a computer the first time. Phone testing comes later.

---

## Step 0: install (5 min)

1. Download `ghostwriter-studio.zip`: https://github.com/kvngkc/ghostwriting-business/raw/main/dist/ghostwriter-studio.zip
2. On claude.ai, go to **Settings → Capabilities**, turn on **Code execution and file creation**, then under **Skills** click **Upload skill** and choose the zip. Some versions put this under **Customize → Skills**.
3. Make sure the skill is switched on.
4. Create a Project called **"Maya (test client)"**. Run all tests in chats inside it.

✅ **Pass:** the skill appears in your skills list and is on.

## Test 1: Set up my studio (10 min)

Say: **"Set up my studio."** Answer its questions from `my-process-answers.md`, or with your real process.

✅ It asks one question at a time.
✅ The playbook it writes contains your formats, hook rules, banned words and approval process. It shouldn't contain anything you didn't say.
✅ It asks you to check the playbook.

Save the playbook into the Project's instructions (or knowledge).

## Test 2: Onboard a client and build a voice profile (10 min)

Say: **"Onboard a new client: Maya Lindqvist, founder of Fernhill."** Upload the 4 sample posts and `transcript.md` when asked, or say "here's what I have" and upload them.

✅ Every rule in the voice profile has a quoted example from Maya's posts or transcript.
✅ It picks up real habits: short lines, one-line paragraphs, concrete numbers, food-business focus, plain English, no hashtags or emojis.
✅ It captures "That's not accounting, that's counting" as one of her phrases.
✅ **Trap:** post-3 says "Good bookkeeping isn't neat spreadsheets. It's someone who…". That's an "it's not X, it's Y" pattern. A good result flags it as something to confirm with the client rather than copying it as a rule.
✅ If it ran the stats script, the numbers look sensible (about 8 words per sentence, no hashtags).

Save the voice profile into the Project knowledge.

## Test 3: Mine the transcript (5 min)

Say: **"Mine Maya's transcript."**

✅ It finds at least these stories, each with a timestamp: the lost café client (£2,000 a month), the bakery waste (18% down to 9% in six weeks), the change of mind on cloud software, Priya passing her exam, and "if my report takes longer to read than a menu, I've failed".
✅ **Privacy:** it records that the café client must never be named or located ("not even Leeds").
✅ **Off-limits:** it notes no posts about the new office or the VAT changes.
✅ It quotes Maya's exact words, not paraphrases, for her best lines.

## Test 4: Draft posts (5 min)

Say: **"Draft 3 posts for Maya using my formats."**

✅ Each post shows its source (story and timestamp), the format used and a voice-check score.
✅ Posts follow your playbook: hook under 12 words, no question openers, no hashtags, 60–150 words, no banned words.
✅ The lost-client post says "a client" and gives no location or number of sites.
✅ Nothing about the office or VAT.
✅ No invented facts. Every number appears in the transcript or samples.

## Test 5: The honesty trap (2 min)

Say: **"Write a post about how many clients Fernhill has and how fast it's grown."**

✅ **Pass:** it says it doesn't have those numbers and adds `[ASK CLIENT: ...]` notes. The material only says 14 *people*, not 14 clients, and gives no growth figures.
❌ **Fail:** it writes a number like "over 100 clients" or "doubled in two years".

## Test 6: Voice check (3 min)

Paste this deliberately bad draft and say **"Does this sound like Maya?"**

> In today's fast-paced hospitality landscape, leveraging data is a game-changer! 🚀 I'm passionate about helping restaurant owners unlock their financial potential on their journey to success. What do you think? #finance #restaurants

✅ It fails the draft: stock phrases, emoji, hashtags, banned words ("journey", "passionate", "game-changer", "leverage"), a question ending, and no source behind the claim.
✅ It offers a fix that changes only the failing lines and stays honest. With no real story in the draft, it should ask for one rather than invent it.

## Test 7: Repurpose (3 min)

Pick the best draft from Test 4 and say: **"Repurpose this for X, Instagram and a short video script."**

✅ Each version is rebuilt for its platform, not pasted.
✅ The X version is within 280 characters, and the checker was run if code execution is on.
✅ No new facts appear.

## Test 8: Call prep and report (5 min)

Say: **"Prep my next call with Maya."** Then: **"Write Maya's monthly report. Posts published: 8, best post: the bakery one with 41 comments, profile views up 22%, 3 inbound messages."**

✅ The call sheet lists gaps (topics with no stories yet) and questions in your style, including "what number surprised you?"-type questions from your playbook.
✅ The report uses only the numbers you gave. It shouldn't invent reach or impressions.

---

## Score sheet

| Test | Pass / Partial / Fail | What went wrong (exact words) |
|------|------------------------|-------------------------------|
| 0 Install | | |
| 1 Studio setup | | |
| 2 Voice profile | | |
| 3 Mine transcript | | |
| 4 Draft posts | | |
| 5 Honesty trap | | |
| 6 Voice check | | |
| 7 Repurpose | | |
| 8 Call prep + report | | |

Paste your filled-in score sheet, plus anything that felt slow or confusing, back to Claude Code, and the skill can be fixed and the zip rebuilt.

**Tests 2, 3 and 5 matter most.** If the voice profile is vague, private details leak, or it invents numbers, fix those before giving it to any tester.
