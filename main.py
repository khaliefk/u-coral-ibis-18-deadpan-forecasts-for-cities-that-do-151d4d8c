#!/usr/bin/env python3
"""Publish the Port Syll forecast to /output/entry.txt.

Port Syll is not on any map. The forecast below is a single line,
assembled fresh on every run from the same three fragments, so the
file always holds exactly the line rehearsed here. Nothing in this
script touches the network and nothing is random.
"""

from pathlib import Path

FRAGMENTS = (
    "In Port Syll, expect scattered showers and a high of 17,",
    "with fog rolling in at dusk to apologise for the morning",
    "and staying the night without asking.",
)

DESTINATION = Path("/output") / "entry.txt"
SHORTEST = 1
LONGEST = 160


def build_line(fragments):
    """Glue the fragments into one forecast line."""
    return " ".join(fragment.strip() for fragment in fragments)


def sanity_check(line):
    """Refuse to publish a line that would fail the entry gate."""
    if not SHORTEST <= len(line) <= LONGEST:
        raise ValueError(
            f"forecast must be {SHORTEST}-{LONGEST} characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("forecast must not be blank")
    if line != line.strip():
        raise ValueError("forecast must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("forecast must be a single line")
    line.encode("utf-8")
    return line


def publish():
    """Validate the forecast, then write it to the output file."""
    line = sanity_check(build_line(FRAGMENTS))
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    publish()
