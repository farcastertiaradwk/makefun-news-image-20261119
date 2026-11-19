#!/usr/bin/env python3
"""news-image-20261119 entry: write the day's news image to /output/entry.png.

The image is held in this repository as entry.png; this program copies it to
the output directory. No network, fully deterministic: the same bytes every run.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "dff279d972aa916c5d088aa5431f5d95cea9eb756a482c14a37f73753a6bcc83"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        print(f"missing entry image: {src}", file=sys.stderr)
        return 1
    if os.path.getsize(src) > 1048576:
        print("entry image exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: got {digest}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
