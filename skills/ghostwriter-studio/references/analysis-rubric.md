# Voice Analysis Rubric

Collect evidence for each dimension below. Each finding needs a quote and a count ("seen in 7 of 12 samples"). Findings seen once go under Notes, not Rules.

How many samples a Rule needs:
- 5 or more samples: seen in at least half of them.
- Fewer than 5 samples: seen in at least 3, or stated by the client in an interview (cite the timestamp). Mark the profile `status: provisional` and ask the writer for more samples.

## Dimensions

| # | Dimension | What to look for |
|---|-----------|------------------|
| 1 | Rhythm | Average and range of sentence length (from `voice_stats.py`). Do they mix very short lines with long ones? One-line paragraphs or blocks? |
| 2 | Openings | How posts start: a story, a claim, a number, a question, dialogue. Copy their 5 best first lines verbatim. |
| 3 | Endings | How posts end: question to readers, lesson, call to action, no ending at all. |
| 4 | Vocabulary | Words and phrases they repeat, jargon they use and jargon they avoid, local or industry slang, British or American spelling. |
| 5 | Stance | How sure they sound. Do they hedge ("I think", "maybe") or state? Do they argue with ideas, or with people? |
| 6 | Warmth and humour | Self-deprecating, dry, none. How they talk about clients and competitors. |
| 7 | Structure | Lists or prose, use of numbered points, headings, line breaks, bold text. |
| 8 | Persuasion | What they use as proof: stories, data, client results, credentials, analogies. |
| 9 | Signature moves | Recurring analogies, catchphrases, framings, sign-offs. |
| 10 | Mechanics | Emoji, hashtag, exclamation mark and question rates; capitalisation habits; contractions. |
| 11 | Boundaries | Topics, words and formats they refuse (from the interview). |

## Patterns that do not belong in any profile

These are generic AI tells. Even if a sample contains them, they were probably written by a tool or a previous writer; confirm with the client before keeping one.

The exception is a phrase the client *said* (it's in a transcript, verbatim) or confirmed they wrote. That's their voice, not a tell: record it under "Signature moves" with its source and the writer's OK, and drafts may quote it. Don't generalise it into a rule that lets new lines use the pattern.
- "It's not X, it's Y" reveals and "no X, no Y, no Z" lists
- Self-answered questions ("The result? 40% growth.")
- Stock openers: "Here's the thing", "Let's dive in", "In today's fast-paced world"
- Stacked em dashes and colon reveals
- Words such as "leverage", "unlock", "game-changer", "delve", "elevate"

## Scoring a draft

Score the draft 1 to 5 on each check below (one score per row, not per line of the draft), then average the six scores.

| Check | 5 means |
|-------|---------|
| Rhythm | Sentence and paragraph lengths sit inside the profile's ranges |
| Opening | Uses one of their opening types and would fit beside their real first lines |
| Vocabulary | Uses their words; contains nothing from their "never" list |
| Stance | Same level of certainty and the same kind of target |
| Substance | Every story, number and claim traces back to `stories.md` or a transcript |
| No AI tells | None of the patterns above |

Substance is a hard gate: any claim that does not trace back to the client's material fails the draft, whatever the other scores. Report the six scores and the average, then list each failing line of the draft with the rule it breaks, and give a corrected draft that changes only those lines. Also check the writer's own editing rules (length, hooks, endings, banned words) and list breaks the same way.

A client's verbatim phrase recorded under "Signature moves" doesn't count against "No AI tells".
