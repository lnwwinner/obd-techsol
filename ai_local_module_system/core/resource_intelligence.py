# Resource Intelligence System
# AI selects best resource based on metadata + simple scoring (extendable to RL)

import json
import os

INDEX_FILE = "ai_local_module_system/core/resource_index.json"


def load_index():
    if not os.path.exists(INDEX_FILE):
        return {}
    with open(INDEX_FILE, "r") as f:
        return json.load(f)


def save_index(data):
    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)
    with open(INDEX_FILE, "w") as f:
        json.dump(data, f, indent=4)


def register_resource(name, domain, category, path, metadata=None):
    idx = load_index()
    idx[name] = {
        "domain": domain,
        "category": category,
        "path": path,
        "metadata": metadata or {}
    }
    save_index(idx)


def score_resource(meta, context):
    score = 0
    # simple heuristics (extendable)
    if not meta:
        return score

    if "winrate" in meta and context.get("min_winrate"):
        if meta["winrate"] >= context["min_winrate"]:
            score += 5

    if "market" in meta and context.get("market"):
        if meta["market"] == context["market"]:
            score += 3

    if "latency" in meta and context.get("max_latency"):
        if meta["latency"] <= context["max_latency"]:
            score += 2

    return score


def select_best(domain, category, context=None):
    idx = load_index()
    context = context or {}

    candidates = [
        (name, info) for name, info in idx.items()
        if info.get("domain") == domain and info.get("category") == category
    ]

    if not candidates:
        return None

    best = None
    best_score = -1

    for name, info in candidates:
        s = score_resource(info.get("metadata", {}), context)
        if s > best_score:
            best_score = s
            best = (name, info)

    return best
