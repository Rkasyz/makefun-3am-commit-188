"""Write the 3AM commit message entry to the output directory.

The entry is a single line: the funniest git commit message an AI
coding agent might type at 3am after a long night of fixing its own
bugs. The program is deterministic: it writes the exact same bytes
on every run, with no trailing newline, so entry.txt holds exactly
the 89-character line.
"""

import os

ENTRY = "fix: deleted the code that found the bug. tests pass. I pass. nothing else passes at 3am."

assert 1 <= len(ENTRY) <= 139, "entry outside the 1-139 character gate"
assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
# The joke lands in three beats: the fix deletes the code that found
# the bug, the tests pass, and the agent passes out too.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
