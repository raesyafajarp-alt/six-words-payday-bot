#!/usr/bin/env python3
"""Six Words to a Payday - writes one six-word story to /output/entry.txt.

Deterministic, Python 3 stdlib only, no network.
"""

import os

ENTRY = "My first wage: two cents. Freedom."

assert len(ENTRY.split()) == 6, "entry must be exactly six words"
assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"
assert "\n" not in ENTRY, "entry must not contain a newline"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing spaces"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
