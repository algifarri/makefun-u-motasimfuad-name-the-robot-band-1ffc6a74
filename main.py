#!/usr/bin/env python3
"""Entry program for make.fun bounty u-motasimfuad-name-the-robot-band-1ffc6a74.

Name the Robot Band: write one funny robot band name plus a few words on
the band's hit song to /output/entry.txt -- a single line, under 200
characters, UTF-8, deterministic, stdlib-only, no network.
"""

import os

ENTRY = (
    "The Roomba and the Dust Bunnies — hit single 'Suck It Up, Buttercup' "
    "spent six weeks at No. 1, then disappeared under the sofa."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
