---
name: voice-profile
description: Build or update a ghostwriting client's voice profile from their real writing, transcripts and interview answers, then use it to draft or check posts in that voice. Use when the user says "build a voice profile", "analyse this client's voice", "capture how they write", "onboard a new ghostwriting client", "update the voice file", "does this draft sound like them", or pastes a batch of someone's posts, emails or a call transcript and wants writing that sounds like that person. Not for generic copywriting with no specific person behind it.
---

# Voice Profile

A voice profile is a short, evidence-backed file that lets anyone (you, Claude, an editor you hire) write posts a client would read and say "that's me". It is built only from the client's own material. Nothing in it is guessed.

The profile lives at `clients/<client-slug>/voice-profile.md`, beside the raw material it was built from:

```
clients/<client-slug>/
  samples/          their own writing: posts, emails, newsletters, talks (one file each)
  transcripts/      interview and call transcripts
  voice-profile.md  the output of this skill
  stories.md        bank of real stories, opinions and numbers they have told you
```

## Modes

Pick the mode from the request.

1. **Build**: no profile exists yet. Run every step below.
2. **Update**: a profile exists and new material arrived (a new transcript, posts the client edited, feedback). Run steps 2 to 5 on the new material only, then merge. Never drop an existing rule unless new evidence contradicts it; note the change in the changelog at the bottom of the profile.
3. **Check**: the user gives a draft and asks whether it sounds like the client. Run the scoring in `references/analysis-rubric.md` (section "Scoring a draft") against the profile and return the score, the lines that break the voice, and a corrected version that changes only those lines.

## Build steps

### 1. Gather enough material

Minimum before writing a profile:
- 10 or more pieces the client wrote themselves (posts, emails, newsletters). Material written by a previous ghostwriter or an AI tool does not count; ask if unsure.
- 1 recorded interview of 30 to 45 minutes, transcribed. Use the question bank in `references/interview-questions.md`.

If there is less than that, say what is missing and build a draft profile marked `status: provisional`. Do not fill gaps with assumptions.

Run `python3 scripts/voice_stats.py clients/<slug>/samples` to get the measurable numbers (sentence length, paragraph length, question rate, emoji and hashtag use, most frequent openers). Put those numbers in the profile as they come out.

### 2. Read for the things numbers miss

Read every sample and transcript. Work through `references/analysis-rubric.md` and collect evidence for each dimension. Every claim in the profile needs at least one direct quote from the material. A trait seen only once is a note, not a rule.

Pay most attention to the transcript. People speak more like themselves than they write, so the spoken phrases, analogies and opinions are the best raw material.

### 3. Pull the content bank

From the transcripts, list into `stories.md`:
- real stories (who, what happened, what changed), with the transcript timestamp or file
- strong opinions, including ones that go against common advice in their field
- numbers and results they stated themselves
- topics they said they will not talk about

Never add a story, number, client name or result the client did not give you. Ghostwritten posts go out under the client's name, so an invented detail is a false statement by them.

### 4. Write the profile

Fill `references/voice-profile-template.md` and save it as `clients/<slug>/voice-profile.md`. Keep it under about 150 lines. It is a working tool, not an essay: short rules, each followed by a real quote.

### 5. Validate with the client

Write 3 short test posts from 3 different stories in `stories.md` using only the profile. Send them to the client with one question: "Which lines don't sound like you?" Record their answers in the profile under "Client corrections" and adjust the rules. A profile is `status: approved` only after this round.

## Drafting with the profile

When drafting posts for a client, load in this order: `voice-profile.md`, then `stories.md`, then the specific transcript section the post comes from. Draft, then run the "Scoring a draft" check before handing it over. A human edit pass happens after this, every time.

## Rules

- Use only the client's real material. No invented stories, numbers, credentials, client names or quotes.
- Keep client material private. Do not paste it into tools whose terms allow training on inputs unless the client agreed to that in writing.
- The profile describes how the client writes. It does not make them sound "better" by generic standards. If they write long paragraphs, the profile says so.
- Re-run Update mode every month after the client interview, and whenever the client rewrites a draft heavily. Their edits are the best evidence there is.
