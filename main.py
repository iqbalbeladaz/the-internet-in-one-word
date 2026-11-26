"""the-internet-in-one-word: the whole internet in a single word.

The word is "feral". The internet was supposed to be a library and it
went feral: nobody is in charge, nothing is house-trained, and memes,
scams, knowledge, rage and cat videos all breed unchecked in the same
wild. It is funny by itself, true of the internet as a whole rather
than one app or mood, surprising (nobody's first reach is "feral"),
and it lands in one beat at five letters.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "feral"

MAX_CHARS = 30


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty word")
    if len(ENTRY.split()) != 1:
        raise ValueError("entry must be a single word")
    if not ENTRY.isalpha():
        raise ValueError("entry must be letters only: no digits or punctuation")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
