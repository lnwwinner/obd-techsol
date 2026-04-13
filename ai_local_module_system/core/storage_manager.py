# Central Storage System (Data / Models / Modules / Experience)

import os
import json
import time

BASE_PATH = os.path.expanduser("~/ai_storage")

class StorageManager:
    def __init__(self):
        self.paths = {
            "data": os.path.join(BASE_PATH, "data"),
            "models": os.path.join(BASE_PATH, "models"),
            "modules": os.path.join(BASE_PATH, "modules"),
            "experience": os.path.join(BASE_PATH, "experience")
        }

        for p in self.paths.values():
            os.makedirs(p, exist_ok=True)

    def save_data(self, data, tag="market"):
        path = f"{self.paths['data']}/{tag}_{int(time.time())}.json"
        with open(path, "w") as f:
            json.dump(data, f)
        return path

    def save_experience(self, exp):
        path = f"{self.paths['experience']}/exp_{int(time.time())}.json"
        with open(path, "w") as f:
            json.dump(exp, f)
        return path

    def save_model(self, name, model_data):
        path = f"{self.paths['models']}/{name}_{int(time.time())}.pkl"
        with open(path, "w") as f:
            f.write(str(model_data))
        return path

    def list_all(self):
        return self.paths
