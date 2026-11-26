#!/usr/bin/env python3
"""Funniest Sick-Day Excuse -- make.fun entry.

A sick-day excuse in one line: not a fever, not a migraine -- the cat
has scheduled a mandatory cuddle intervention, and attendance is not
optional.

The program writes that one excuse to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). A command-line
argument may name the directory instead, but the grader passes none.
"""

import os
import sys

from pathlib import Path

EXCUSE = (
    "I can't come in today "
    "-- my cat has scheduled a mandatory cuddle intervention."
)


def main(argv):
    # Gate for this bounty: 1-200 characters of UTF-8 text.
    if not 1 <= len(EXCUSE) <= 200:
        print("excuse must be 1-200 characters, got %d"
              % len(EXCUSE), file=sys.stderr)
        return 1
    out_dir = argv[1] if len(argv) > 1 else (
        os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(Path(out_dir) / "entry.txt", "w",
              encoding="utf-8", newline="\n") as handle:
        handle.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
