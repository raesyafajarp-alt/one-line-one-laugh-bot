#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

ENTRY = 'I asked my GPS for the meaning of life. It said "recalculating" \u2014 and honestly, same.'

def main():
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
