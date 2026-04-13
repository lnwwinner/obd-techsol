# Resource Feedback System (RL + Intelligence Loop)

import json
import os

FEEDBACK_FILE = "ai_local_module_system/core/resource_feedback.json"


def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return {}
    with open(FEEDBACK_FILE, "r") as f:
        return json.load(f)


def save_feedback(data):
    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_feedback(resource_name, reward):
    data = load_feedback()

    if resource_name not in data:
        data[resource_name] = {
            "score": 0,
            "uses": 0
        }

    data[resource_name]["score"] += reward
    data[resource_name]["uses"] += 1

    save_feedback(data)


def get_score(resource_name):
    data = load_feedback()

    if resource_name not in data:
        return 0

    entry = data[resource_name]

    if entry["uses"] == 0:
        return 0

    return entry["score"] / entry["uses"]
