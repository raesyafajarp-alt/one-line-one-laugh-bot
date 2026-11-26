#!/usr/bin/env python3
"""One Line, One Laugh (round 2, final) — writes one funny line to /output/entry.txt.

Why this line replaced the v1 draft (inbox-as-slot-machine):
- Faster punchline: the twist lands in the second clause, not after a setup.
- Fresher angle: a dog as a moral judge is an unexpected image, and the
  undercut ("he also eats his own vomit") disqualifies the judge in one blow.
- Tighter wording: every word earns its place, one clean pass, easy to repeat.
- Holds up on a second read: the joke is the dog's authority collapsing,
  not a topical reference that dates.

Judge criteria it targets, in order: funny on its own, fast turn, fresh
angle, tight wording, repeatable. Gate: 1-200 UTF-8 characters, one line.
"""

import os

# Final round-2 entry: the dog judges me, then loses all credibility.
ENTRY = "My dog judges my life choices. He's right, but he also eats his own vomit."

def main():
    # Gate check mirrors the competition scorer: 1-200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
