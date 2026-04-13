# Training Mode (NO REAL TRADING)

from core.ai_boot import AIBoot
from core.training_data_collector import DataCollector
import random

collector = DataCollector()


def training_execution(model):
    # simulate market data
    data = {
        "price": random.uniform(1.0, 2.0),
        "volume": random.randint(100, 1000)
    }

    collector.save(data)

    # simulate reward (for training only)
    reward = random.choice([-1, 1])

    return {"reward": reward}


boot = AIBoot(
    domain="trading",
    execution_func=training_execution,
    interval=5
)

boot.start()

import time
while True:
    time.sleep(1)
