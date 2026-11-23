#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original one-line roast of a gadget used every day
(a smartwatch and its hourly stand-up congratulations) to
/output/entry.txt, UTF-8, exactly one line of at most 200 characters.

Standard library only. No input, no network, no randomness:
the output is deterministic.
"""

import os

ROAST = (
    "My smartwatch congratulates me for standing up once an hour, "
    "like a fitness coach who thinks my job is sitting professionally."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ROAST.strip()
    if not line or len(line) > 200:
        raise ValueError("roast must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
