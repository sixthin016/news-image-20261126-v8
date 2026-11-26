#!/usr/bin/env python3
"""Entry point — news-image-20261126 v7. Stdlib only: copy the pre-rendered
image to the output directory. No network, no exec, no wall clock."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
print("copied entry.png to", OUT)
