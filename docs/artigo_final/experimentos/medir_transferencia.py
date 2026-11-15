"""Deterministic packing sizes only; not a production performance benchmark."""
import base64
import json
import zlib
import numpy as np


def measure():
    random = np.random.default_rng(42)
    arrays = {
        "constante": np.full((128, 128), 0.5, dtype="<f4"),
        "gradiente": np.tile(np.linspace(-0.2, 0.8, 128, dtype="<f4"), (128, 1)),
        "aleatoria": random.uniform(-1, 1, (128, 128)).astype("<f4"),
    }
    results = {}
    for name, array in arrays.items():
        raw = array.tobytes()
        compressed = zlib.compress(raw)
        results[name] = {
            "natureza": "matriz controlada, não dados agrícolas",
            "cells": array.size, "raw_bytes": len(raw),
            "zlib_bytes": len(compressed),
            "base64_bytes": len(base64.b64encode(compressed)),
            "compressed_to_raw": len(compressed) / len(raw),
        }
    return results


if __name__ == "__main__":
    print(json.dumps(measure(), ensure_ascii=False, indent=2))
