#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one line of plain text (an alien tourist's review of planet Earth)
to entry.txt in the output directory. Pure standard library only.
"""

import os
import sys

LINE = (
    "Two days in, I still cannot tell who serves whom: the tall ones follow "
    "small furry creatures everywhere, bagging their droppings like tribute. "
    "Five stars. I would serve them too."
)


def candidate_dirs():
    """Output directories in order of preference, de-duplicated."""
    seen = []
    for d in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
        "/tmp",
    ):
        if d and d not in seen:
            seen.append(d)
    return seen


def main() -> int:
    # Self-check against the sealed gate: UTF-8 text, 1-200 chars, not blank.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line fails the gate"
    payload = LINE.encode("utf-8")

    last_err = None
    for out_dir in candidate_dirs():
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "wb") as fh:
                fh.write(payload)
            # Read back and verify byte-exact before declaring success.
            with open(path, "rb") as fh:
                if fh.read() != payload:
                    raise OSError("read-back mismatch in %s" % path)
            return 0
        except OSError as err:  # try the next candidate directory
            last_err = err
    print("could not write entry.txt anywhere: %s" % last_err, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
