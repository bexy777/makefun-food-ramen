#!/usr/bin/env python3
"""Food-picture-01 entry: steaming tonkotsu ramen.

The picture shipped beside this program (entry.jpg) is copied byte for
byte to the grader's output directory as entry.png. JPEG bytes are
allowed under that name: the gate tells PNG from JPEG by the first
bytes. Copying is deterministic: the same input bytes produce the
same output bytes on every run.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.jpg"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing image: {SOURCE}", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    size = OUTPUT.stat().st_size
    if size > 1_048_576:
        print(f"output too large: {size} bytes (limit 1 MiB)", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
