"""One Word From Your Ex: writes the entry text to /output/entry.txt.

Why this word: the one word an ex reaches for when they describe you —
painfully honest, and you know it the second you hear it.
"""

import os

# The entry itself: one word, the word my ex would use to describe me.
ENTRY = 'Overthinker'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
