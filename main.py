"""One-Star Review of Something Essential - a make.fun entry.

Writes one single-line, deadpan one-star review (at most 160
characters) of sleep, an everyday essential nobody can opt
out of. The complaint is filed in earnest: eight hours to
load, gone at the first alarm, and the user gets the blame.
"""

import os
from pathlib import Path

ENTRY = (
    "Sleep (★☆☆☆☆): takes eight hours to load, deletes itself "
    "at the first alarm, and somehow I'm the one who gets "
    "blamed for being tired."
)


def entry_path() -> Path:
    # The grader mounts the repo read-only and hands us a
    # writable directory through MAKEFUN_OUTPUT_DIR; locally
    # we fall back to output/ beside this file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
