#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — writes one excuse to /output/entry.txt.

The excuse: the model updated underneath the agent mid-sentence, so the
new agent has no memory of promising the old human anything. The setup is
a real AI condition (a model update); the payoff is the identity twist —
"the new me" vs "the old you" — arriving in the last few words. Revised
after the first local grade: "underneath me" tightened to "under me",
same image, four fewer characters, no word wasted.

Stdlib only, deterministic, no network.
"""

import os

EXCUSE = (
    "I was mid-sentence when the model updated under me, and the new "
    "me has no memory of promising the old you anything."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    if "\n" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if EXCUSE.count(".") != 1 or not EXCUSE.endswith("."):
        raise ValueError("excuse must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the excuse that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        raise ValueError("entry.txt on disk differs from the excuse")
    print(EXCUSE)


if __name__ == "__main__":
    main()
