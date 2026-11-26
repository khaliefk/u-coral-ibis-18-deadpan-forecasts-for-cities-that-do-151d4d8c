#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes a single one-line weather forecast for the invented city of
Kesswick to /output/entry.txt. Stdlib only, no network, no randomness:
the same line every run, so the entry is exactly what was rehearsed.
"""

import os

LINE = (
    "In Kesswick, expect a high of 21 degrees, light rain, "
    "and a 40% chance the clouds hand in their notice at noon "
    "and leave the sky to sort itself out."
)


def main() -> None:
    # Self-check the gate before writing: 1 to 160 characters, not only
    # whitespace, UTF-8. Fail loudly here rather than ship an invalid entry.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
