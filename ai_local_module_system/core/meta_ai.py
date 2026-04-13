# Meta AI System
# AI creates and selects new models automatically

from core.multi_project_intelligence import get_best_global
from core.resource_manager import ResourceManager

rm = ResourceManager()


def generate_new_model(domain):
    # Placeholder for training logic
    model_name = f"auto_model_{domain}"
    print(f"[META AI] Generated new model: {model_name}")
    return model_name


def meta_decision(domain):
    best = get_best_global(domain, "models")

    if not best:
        return generate_new_model(domain)

    name, _ = best

    print(f"[META AI] Using existing best model: {name}")

    return name
