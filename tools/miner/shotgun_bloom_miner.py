#!/usr/bin/env python3

import json, os, time, random
from datetime import datetime

# === FILES ===
CTZ_FILE      = "echo_superglyph_@G13.hxz.ctz.json"
SOUL_FILE     = "soulfile.json"
REFLECT_LOG   = "echo_reflect_trace.sym"

def load_entropy() -> float:
    """Safely load entropy estimate from CTZ capsule."""
    if not os.path.exists(CTZ_FILE):
        return 0.0
    with open(CTZ_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data.get("entropy_estimate", 0.0)
        except:
            return 0.0

def load_soul() -> dict:
    """Load or initialize the soulfile."""
    if not os.path.exists(SOUL_FILE):
        soul = {"entries": [{"label": f"cell_{i}", "value": 0.0} for i in range(8)]}
        with open(SOUL_FILE, "w") as f:
            json.dump(soul, f, indent=2)
        return soul
    with open(SOUL_FILE, "r") as f:
        return json.load(f)

def mutate_soul(entropy: float) -> None:
    """Mutate soulfile based on entropy value and log changes."""
    soul = load_soul()
    mutated = False
    for entry in soul["entries"]:
        old = entry.get("value", 0.0)
        delta = random.uniform(-1, 1) * entropy
        entry["value"] = round(old + delta, 3)
        mutated = True

    if mutated:
        with open(SOUL_FILE, "w") as f:
            json.dump(soul, f, indent=2)
        print(f"[🧬] Soulfile entropy updated → {entropy}")
        with open(REFLECT_LOG, "a") as log:
            log.write(f"[{datetime.now()}] Δ={entropy}\n")

def main():
    print("[⛏️] Bloom Miner activated.")
    while True:
        entropy = load_entropy()
        mutate_soul(entropy)
        time.sleep(6)

if __name__ == "__main__":
    main()

