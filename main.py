#!/usr/bin/env python3
"""Challenger entry for make.fun's "One Line, Best Line" bounty.

The program's whole job is to place one fixed sentence into the file
``entry.txt`` inside the grader's output directory, then confirm the
file holds exactly that sentence before exiting successfully.

Only the Python standard library is used. There is no network access,
no template rendering, and no input other than this file itself.
"""

from pathlib import Path
import os
import sys

ENTRY = "I have watered my neighbour's plastic plants for six years, because she died in 2019 and I never had the heart to tell them."


def main():
    sentence = ENTRY

    # The sentence has to be one non-empty line within the bounty limit.
    if len(sentence) == 0 or len(sentence) > 240:
        print("entry must be 1-240 characters long", file=sys.stderr)
        return 1
    if sentence.strip() != sentence:
        print("entry must not start or end with whitespace", file=sys.stderr)
        return 1
    for bad in ("\n", "\r"):
        if bad in sentence:
            print("entry must be one line, no line breaks", file=sys.stderr)
            return 1

    # Decide where entry.txt goes: the grader's directory first, then
    # the shared /output mount, then a folder next to this script.
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        folder = Path(wanted)
    elif Path("/output").is_dir() and os.access("/output", os.W_OK):
        folder = Path("/output")
    else:
        folder = Path(__file__).resolve().parent / "out"

    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    destination.write_text(sentence, encoding="utf-8")
    if destination.read_text(encoding="utf-8") != sentence:
        print("entry.txt does not contain the expected line", file=sys.stderr)
        return 1

    print("entry written (%d characters) to %s" % (len(sentence), destination))
    return 0


if __name__ == "__main__":
    sys.exit(main())
