#!/usr/bin/env python3
"""Snooze Button Roast — one-line roast of an alarm clock that rings at
6 AM on a Saturday. Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback: /output/entry.txt). Python 3 stdlib only, fully deterministic:
same line on every run, no randomness, no time, no network."""

import os

# The roast: a single line, at most 200 characters (118 chars).
ROAST = (
    "My alarm clock screams at 6 AM on Saturday like joy owes it money "
    "— mate, even the sun hits snooze on weekends."
)

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise ValueError("roast must be a single line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
