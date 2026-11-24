#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to /output/entry.txt.

The audience is whoever is watching the spinner: a stressed
developer on one side of the screen and the AI coding agent on
the other. The humour comes from the unspoken deal between them --
the agent silently rewrites the same function three times while
the human drinks coffee and frames it as supervision.

The entry rules are checked inside this file: a single line of
1-200 characters, UTF-8, more than just whitespace. Validation
happens before anything is written, so a broken line errors out
here instead of reaching the judge.
"""

import os
import sys

# The tip. One line, 124 characters, built on a single reversal:
# the agent does the work in secret, the human takes the credit
# by watching. No setup beyond the spinner, no punchline wasted.
TIP = (
    "Tip: your agent rewrote this function three times and told you "
    "about none of them. Pour coffee. Pretend you are supervising."
)

MAX_CHARS = 200


def main() -> int:
    # Normalise the line first: drop a stray trailing newline so
    # the output file contains the tip and nothing after it.
    line = TIP.rstrip("\n")

    # Check the house rules before writing anything: the tip must
    # have real content, stay on one line, and fit the budget.
    # Better to fail loudly here than to submit a rejected entry.
    if not line.strip():
        print("error: tip is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: tip must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: tip is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    # Output goes where the harness expects it: /output by default,
    # overridable for local runs through MAKEFUN_OUTPUT_DIR.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Plain UTF-8 write, no trailing newline appended: the file
    # should hold exactly the tip, character for character.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)

    print(f"wrote {len(line)}-char tip to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
