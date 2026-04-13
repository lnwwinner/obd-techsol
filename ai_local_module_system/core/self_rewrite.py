# Self-Rewrite System
# AI can improve its own logic dynamically

import json
import os

RULES_FILE = "ai_local_module_system/core/self_rules.json"


def load_rules():
    if not os.path.exists(RULES_FILE):
        return {}
    with open(RULES_FILE, "r") as f:
        return json.load(f)


def save_rules(rules):
    os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=4)


def update_rule(module, key, value):
    rules = load_rules()

    if module not in rules:
        rules[module] = {}

    rules[module][key] = value

    save_rules(rules)

    print(f"[SELF-REWRITE] Updated {module}.{key} = {value}")


def get_rule(module, key, default=None):
    rules = load_rules()
    return rules.get(module, {}).get(key, default)
