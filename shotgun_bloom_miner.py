#!/usr/bin/env python3
"""Auto-mutate soulfile.json based on entropy.

Reads entropy info from echo_superglyph_@G13.hxz.ctz.json, mutates
entries in soulfile.json, and logs the changes to echo_reflect_trace.sym.
"""

from __future__ import annotations

import json
import os
import random
import time
from typing import Any, Dict, List

ENTROPY_FILE = "echo_superglyph_@G13.hxz.ctz.json"
SOUL_FILE = "soulfile.json"
TRACE_FILE = "echo_reflect_trace.sym"


def load_entropy() -> float:
    """Load the entropy estimate from ENTROPY_FILE."""
    with open(ENTROPY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return float(data.get("entropy_estimate", 0.0))


def load_soul() -> Dict[str, Any]:
    """Load soul data from SOUL_FILE or return a default structure."""
    if os.path.exists(SOUL_FILE):
        with open(SOUL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"entries": [{"name": "alpha", "value": 0.0}]}


def mutate_entries(soul: Dict[str, Any], entropy: float) -> List[str]:
    """Mutate entries in the soul data using the entropy value.

    Returns a list of log strings describing the changes.
    """
    random.seed(entropy)
    logs: List[str] = []
    for entry in soul.get("entries", []):
        old_value = float(entry.get("value", 0.0))
        delta = random.uniform(-1, 1) * entropy
        entry["value"] = old_value + delta
        logs.append(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} {entry.get('name', '?')}: {old_value} -> {entry['value']}"
        )
    return logs


def write_soul(soul: Dict[str, Any]) -> None:
    """Write the soul data back to SOUL_FILE."""
    with open(SOUL_FILE, "w", encoding="utf-8") as f:
        json.dump(soul, f, indent=2, sort_keys=True)
        f.write("\n")


def log_deltas(deltas: List[str]) -> None:
    """Append the provided deltas to TRACE_FILE."""
    if not deltas:
        return
    with open(TRACE_FILE, "a", encoding="utf-8") as f:
        for line in deltas:
            f.write(line + "\n")


def main() -> None:
    entropy = load_entropy()
    soul = load_soul()
    deltas = mutate_entries(soul, entropy)
    write_soul(soul)
    log_deltas(deltas)


if __name__ == "__main__":
    main()
