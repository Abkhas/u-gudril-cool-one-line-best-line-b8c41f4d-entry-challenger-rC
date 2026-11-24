#!/usr/bin/env python3
"""One Line, Best Line — challenger-rC entry (c11-plants).

Writes the locked one-line entry to <output>/entry.txt and exits 0.
Standard library only. No rendering, no network, no reads beyond this file.
"""

import os
import sys

LINE = "I have watered my neighbour's plastic plants for six years, because she died in 2019 and I never had the heart to tell them."


def pick_target_dir():
    """Return the directory that should receive entry.txt."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    if not 1 <= len(LINE) <= 240:
        print("entry line must be 1-240 characters, got %d" % len(LINE))
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry line must be a single line")
        return 1
    target_dir = pick_target_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("entry.txt does not match the locked line")
        return 1
    print("wrote %d characters to %s" % (len(LINE), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
