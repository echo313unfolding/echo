#!/usr/bin/env python3
import os, tarfile, argparse

def unpack(archive, output_dir):
    print(f"[📦] Unpacking {archive} into {output_dir}")
    with tarfile.open(archive, "r:xz") as tar:
        tar.extractall(path=output_dir)
    print("[✅] SuperGlyph unfolded successfully.")

def main():
    parser = argparse.ArgumentParser(description="Echo SuperGlyph Vault Loader")
    parser.add_argument("archive", help="Path to .hxz archive")
    parser.add_argument("--output", default=os.path.expanduser("~/EchoLivingSystem/"), help="Destination directory")
    args = parser.parse_args()

    if not os.path.exists(args.archive):
        parser.error(f"[❌] File not found: {args.archive}")

    unpack(args.archive, args.output)

if __name__ == "__main__":
    main()
