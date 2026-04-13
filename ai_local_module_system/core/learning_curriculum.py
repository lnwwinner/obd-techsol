# Learning Curriculum System
# Step-by-step progression with evaluation gates

import json
import os

CURRICULUM_FILE = "ai_local_module_system/core/learning_progress.json"

DEFAULT = {
    "stage": 1,
    "metrics": {
        "winrate": 0.0,
        "avg_reward": 0.0,
        "episodes": 0
    }
}

# Passing criteria per stage
CRITERIA = {
    1: {"episodes": 50},
    2: {"winrate": 0.55, "episodes": 100},
    3: {"winrate": 0.60, "avg_reward": 0.1, "episodes": 200},
    4: {"winrate": 0.62, "avg_reward": 0.15, "episodes": 300},
}

STAGE_DESC = {
    1: "Data Collection",
    2: "Feature Engineering",
    3: "Model Training",
    4: "Evaluation",
    5: "Autonomous Learning"
}

class Curriculum:
    def __init__(self):
        self.data = self._load()

    def _load(self):
        if not os.path.exists(CURRICULUM_FILE):
            self._save(DEFAULT)
            return DEFAULT.copy()
        with open(CURRICULUM_FILE, 'r') as f:
            return json.load(f)

    def _save(self, data):
        os.makedirs(os.path.dirname(CURRICULUM_FILE), exist_ok=True)
        with open(CURRICULUM_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    def get_stage(self):
        return self.data.get('stage', 1)

    def get_desc(self):
        return STAGE_DESC.get(self.get_stage(), 'Unknown')

    def update_metrics(self, winrate=None, avg_reward=None, episodes_inc=1):
        m = self.data['metrics']
        if winrate is not None:
            m['winrate'] = winrate
        if avg_reward is not None:
            m['avg_reward'] = avg_reward
        m['episodes'] = m.get('episodes', 0) + episodes_inc
        self._save(self.data)

    def _passed(self, stage):
        crit = CRITERIA.get(stage, {})
        m = self.data['metrics']
        for k, v in crit.items():
            if m.get(k, 0) < v:
                return False
        return True

    def try_advance(self):
        s = self.get_stage()
        if self._passed(s):
            self.data['stage'] = s + 1
            # reset metrics for next stage but keep episodes as history if needed
            self.data['metrics'] = {"winrate": 0.0, "avg_reward": 0.0, "episodes": 0}
            self._save(self.data)
            print(f"[CURRICULUM] Advanced to stage {s+1}: {STAGE_DESC.get(s+1)}")
            return True
        else:
            print(f"[CURRICULUM] Stage {s} not passed yet")
            return False

# Example hook
if __name__ == '__main__':
    c = Curriculum()
    print(c.get_stage(), c.get_desc())
    c.update_metrics(winrate=0.56, avg_reward=0.12, episodes_inc=10)
    c.try_advance()
