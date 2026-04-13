# Training Data Collector
# Collects market data for AI training only (no trading)

import time
import json
import os

class DataCollector:
    def __init__(self, save_path="ai_storage/data"):
        self.save_path = save_path
        os.makedirs(save_path, exist_ok=True)

    def save(self, data, name="market"):
        filename = f"{self.save_path}/{name}_{int(time.time())}.json"
        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"[DATA] Saved: {filename}")


# Example usage
if __name__ == "__main__":
    dc = DataCollector()
    dc.save({"price": 100})
