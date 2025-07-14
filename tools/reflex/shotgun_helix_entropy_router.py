# ~/EchoLivingSystem/tools/reflex/shotgun_helix_entropy_router.py

import hashlib, json, random, requests
from datetime import datetime

BLOCK_HEADER = "04000000b6ff0b1b1680a2862a30ca44d346d9e829ab5f49ffff001d1dac2b7c"
TARGET_PREFIX = "00000"
SKIP_ZONES = set(range(0, 40)) | set(range(100, 180))
NODE_ID = "gyoa-node-α"

glyphs = []
for nonce in range(10000):
    full = bytes.fromhex(BLOCK_HEADER)[:-4] + nonce.to_bytes(4, 'little')
    hash1 = hashlib.sha256(full).digest()
    hash2 = hashlib.sha256(hash1).hexdigest()
    zone = int(hash2[:4], 16) // 256
    if zone in SKIP_ZONES: continue
    if hash2.startswith(TARGET_PREFIX):
        glyphs.append({
            "id": f"glyph_{nonce}",
            "zone": zone,
            "hash": hash2,
            "entropy": random.uniform(0.1, 0.7),
            "node": NODE_ID,
            "timestamp": datetime.now().isoformat()
        })

# Send found glyphs to pool
for g in glyphs:
    try:
        res = requests.post("http://localhost:7070", json=g)
        print(f"🚀 Sent {g['id']} → pool :: {res.text.strip()}")
    except:
        print("❌ Failed to connect to pool node.")
