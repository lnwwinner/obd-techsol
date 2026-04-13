# Evolution Stage System
# Gradual self-development instead of full system activation

import json
import os

STAGE_FILE = "ai_local_module_system/core/evolution_stage.json"

DEFAULT_STAGE = {
    "stage": 1
}


class EvolutionStage:
    def __init__(self):
        self.stage_data = self.load_stage()

    def load_stage(self):
        if not os.path.exists(STAGE_FILE):
            self.save_stage(DEFAULT_STAGE)
            return DEFAULT_STAGE

        with open(STAGE_FILE, "r") as f:
            return json.load(f)

    def save_stage(self, data):
        os.makedirs(os.path.dirname(STAGE_FILE), exist_ok=True)
        with open(STAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def get_stage(self):
        return self.stage_data.get("stage", 1)

    def next_stage(self):
        self.stage_data["stage"] += 1
        self.save_stage(self.stage_data)
        print(f"[EVOLUTION] Upgraded to stage {self.stage_data['stage']}")


# Stage meaning (you can expand later)
STAGE_MAP = {
    1: "Data Collection Only",
    2: "Feature Engineering",
    3: "Model Training",
    4: "Evaluation",
    5: "Autonomous Learning"
}
