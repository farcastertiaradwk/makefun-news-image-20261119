#!/usr/bin/env python3
"""Entrypoint for the news-image-20261119 v2 entry.

Copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png.
Python standard library only, no network access, deterministic.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
EXPECTED_SHA256 = "9b75629c9447260913e748aa379b4dd07b36f730aa61e7b73b9abf407a5c495c"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SOURCE):
        print("missing entry.png next to main.py", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) == 0:
        print("entry.png is empty", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    digest = hashlib.sha256(open(dest, "rb").read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print("sha256 mismatch for copied entry.png", file=sys.stderr)
        return 1
    print("wrote", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
