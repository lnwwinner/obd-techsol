# Learning Diagnostics System
# Analyze why AI fails and adapt learning strategy

import json
import os

DIAG_FILE = "ai_local_module_system/core/learning_diagnostics.json"

class LearningDiagnostics:
    def __init__(self):
        self.data = self._load()

    def _load(self):
        if not os.path.exists(DIAG_FILE):
            return {"history": []}
        with open(DIAG_FILE, "r") as f:
            return json.load(f)

    def _save(self):
        os.makedirs(os.path.dirname(DIAG_FILE), exist_ok=True)
        with open(DIAG_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def log_failure(self, stage, metrics):
        entry = {
            "stage": stage,
            "metrics": metrics
        }
        self.data["history"].append(entry)
        self._save()

    def analyze(self):
        issues = {
            "low_winrate": 0,
            "low_reward": 0,
            "insufficient_data": 0
        }

        for h in self.data["history"]:
            m = h["metrics"]

            if m.get("winrate", 0) < 0.5:
                issues["low_winrate"] += 1

            if m.get("avg_reward", 0) < 0:
                issues["low_reward"] += 1

            if m.get("episodes", 0) < 50:
                issues["insufficient_data"] += 1

        return issues

    def suggest_fix(self):
        issues = self.analyze()

        suggestions = []

        if issues["low_winrate"] > 5:
            suggestions.append("Improve strategy or features")

        if issues["low_reward"] > 5:
            suggestions.append("Adjust reward function")

        if issues["insufficient_data"] > 5:
            suggestions.append("Collect more data")

        return suggestions

# Example
if __name__ == "__main__":
    diag = LearningDiagnostics()
    diag.log_failure(2, {"winrate": 0.4, "avg_reward": -0.2, "episodes": 20})
    print(diag.suggest_fix())
