#!/usr/bin/env python3
import sys, os, hashlib, json

if len(sys.argv) < 2:
    print("Usage: shotgun_entropy_writer.py <.hxz file>")
    sys.exit(1)

path = sys.argv[1]
with open(path, "rb") as f:
    data = f.read()

entropy = len(set(data)) / 256
sha256 = hashlib.sha256(data).hexdigest()

out = {
    "file": os.path.basename(path),
    "sha256": sha256,
    "entropy_estimate": round(entropy * 8, 3)
}

outpath = f"{path}.ctz.json"
with open(outpath, "w") as f:
    json.dump(out, f, indent=2)

print(f"[✅] Entropy written → {outpath}")
