# Auto Evolution System
# AI adjusts strategy based on feedback

from core.multi_project_intelligence import get_best_global
from core.resource_feedback import get_score


def evolve_strategy(domain):
    best = get_best_global(domain, "models")

    if not best:
        print("[EVOLVE] No model found")
        return None

    name, info = best

    score = get_score(name)

    if score < 0:
        print(f"[EVOLVE] Model {name} is weak → searching alternative...")
        return None

    print(f"[EVOLVE] Using model {name} (score={score})")

    return name
