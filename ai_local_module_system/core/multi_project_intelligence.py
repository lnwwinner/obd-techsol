# Multi Project Intelligence
from core.resource_feedback import get_score
from core.resource_intelligence import load_index

def get_best_global(domain, category):
    idx = load_index()
    best = None
    best_score = -1
    for name, info in idx.items():
        if info.get('domain') == domain and info.get('category') == category:
            score = get_score(name)
            if score > best_score:
                best_score = score
                best = (name, info)
    return best
