#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The program is deterministic: every run writes the same single line,
with no trailing newline, so the output file is byte-identical to the
line itself. It uses only the Python standard library.
"""

import os

LINE = "Out of office. I've trained my inbox to answer 'noted' to everything, so honestly, nothing has changed."


def main():
    """Write LINE to /output/entry.txt, creating /output if needed."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
