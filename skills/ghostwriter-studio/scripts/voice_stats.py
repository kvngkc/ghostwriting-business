#!/usr/bin/env python3
"""Measure the countable parts of a client's writing style.

Usage: python3 voice_stats.py <samples-folder>

Reads every .txt and .md file in the folder (one piece of writing per file)
and prints the numbers the voice profile's "Measured style" section needs.
"""
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF]")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
# Word stems that differ between British and American spelling. A generic
# "-or"/"-our" pattern miscounts words like "for" and "door".
_STEMS = ["colo", "favo", "behavio", "labo", "hono", "neighbo", "flavo", "humo", "rumo", "harbo", "endeavo"]
_IZE = ["organi", "reali", "recogni", "priori", "speciali", "summari", "maximi", "minimi", "optimi", "apologi", "emphasi", "standardi", "categori", "customi", "utili"]
BRITISH = re.compile(r"\b(?:(?:%s)urs?|(?:%s)s(?:e|es|ed|ing|ation)|analys(?:e|ed|ing)|centre|metre|theatre|cheque|programme|travell(?:ed|ing|er))\b" % ("|".join(_STEMS), "|".join(_IZE)), re.I)
AMERICAN = re.compile(r"\b(?:(?:%s)rs?|(?:%s)z(?:e|es|ed|ing|ation)|analyz(?:e|ed|ing)|center|meter|theater|check(?=ing account)|program(?!m)|travel(?:ed|ing|er))\b" % ("|".join(_STEMS), "|".join(_IZE)), re.I)


def sentences(text):
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            parts.extend(s for s in SENTENCE_END.split(line) if s.strip())
    return parts


def main(folder):
    files = sorted(p for p in Path(folder).iterdir() if p.suffix in {".txt", ".md"})
    if not files:
        sys.exit(f"No .txt or .md files in {folder}")

    sent_lengths, para_lengths, openers = [], [], Counter()
    questions = exclaims = emojis = hashtags = 0
    one_line_paras = total_paras = 0
    british = american = 0
    first_lines = []

    for f in files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
        if paras:
            first_lines.append((f.name, paras[0].strip().splitlines()[0][:120]))
        for p in paras:
            n = len(sentences(p))
            para_lengths.append(n)
            total_paras += 1
            one_line_paras += n == 1
        for s in sentences(text):
            words = s.split()
            sent_lengths.append(len(words))
            if words:
                openers[words[0].lower().strip("\"'“”‘’,:")] += 1
        questions += text.count("?")
        exclaims += text.count("!")
        emojis += len(EMOJI.findall(text))
        hashtags += len(re.findall(r"(?<!\w)#\w+", text))
        british += len(BRITISH.findall(text))
        american += len(AMERICAN.findall(text))

    n = len(files)
    q = statistics.quantiles(sent_lengths, n=10) if len(sent_lengths) >= 10 else [min(sent_lengths), max(sent_lengths)]
    print(f"Samples: {n}")
    print(f"Sentence length: average {statistics.mean(sent_lengths):.1f} words, typical range {q[0]:.0f}-{q[-1]:.0f}")
    print(f"Paragraph length: average {statistics.mean(para_lengths):.1f} sentences; one-line paragraphs {100 * one_line_paras / total_paras:.0f}%")
    print(f"Per post: questions {questions / n:.1f}, exclamation marks {exclaims / n:.1f}, emoji {emojis / n:.1f}, hashtags {hashtags / n:.1f}")
    print(f"Spelling signals: British-style {british}, American-style {american} (rough; check by reading)")
    print("Most common sentence openers:", ", ".join(f"{w} ({c})" for w, c in openers.most_common(12)))
    print("\nFirst lines:")
    for name, line in first_lines:
        print(f"  {name}: {line}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
