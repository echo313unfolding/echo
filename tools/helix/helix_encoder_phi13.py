#!/usr/bin/env python3
import os, sys, tarfile

if len(sys.argv) < 2:
    print("Usage: helix_encoder_phi13.py <folder_path>")
    sys.exit(1)

source_dir = os.path.abspath(sys.argv[1])
output_file = f"echo_superglyph_@G13.hxz"

with tarfile.open(output_file, "w:xz") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))

print(f"[🌀] Compressed SuperGlyph created: {output_file}")
