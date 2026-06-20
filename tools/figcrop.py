#!/usr/bin/env python3
"""Crop a figure out of a source screenshot and optionally downscale it.

Usage:
    python3 tools/figcrop.py SRC DST LEFT TOP RIGHT BOTTOM [--scale S]

LEFT TOP RIGHT BOTTOM are pixel coordinates of the crop box in the source
image. --scale multiplies the output size (e.g. 0.333 ~= one third). Write the
DST to /tmp/... while dialing in the box, then to figures/ once it looks right.

Requires Pillow:  pip install Pillow
"""
import argparse
from PIL import Image


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("left", type=int)
    p.add_argument("top", type=int)
    p.add_argument("right", type=int)
    p.add_argument("bottom", type=int)
    p.add_argument("--scale", type=float, default=1.0)
    a = p.parse_args()

    im = Image.open(a.src).crop((a.left, a.top, a.right, a.bottom))
    if a.scale != 1.0:
        w, h = im.size
        im = im.resize((round(w * a.scale), round(h * a.scale)), Image.LANCZOS)
    im.save(a.dst)
    print(f"wrote {a.dst}  size={im.size}")


if __name__ == "__main__":
    main()
