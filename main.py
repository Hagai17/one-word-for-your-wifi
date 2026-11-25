"""One Word for Your Wi-Fi — entry program.

The entry is a single word: "Narcoleptic".

Home Wi-Fi does many annoying things, but the one everyone recognises is the
connection that falls asleep without warning — mid-call, mid-download,
mid-sentence — and wakes up later acting like nothing happened. The word was
picked by duelling twelve candidates against the judge's published criteria
(funniest at once, truest to how Wi-Fi behaves, and an angle the crowd won't
reach for); see candidates.md for the full bracket.

The program prints the word and writes it to /output/entry.txt, which is what
the competition's sealed gate scorer reads (UTF-8, 1-20 characters).
"""

import os

ENTRY = "Narcoleptic"
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the entry word to the file the gate scorer reads."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def check_gate(word):
    """The gate: one word, 1-20 characters, not only whitespace."""
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.strip() == word and " " not in word, "entry must be one word"
    return True


def main():
    check_gate(ENTRY)
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
