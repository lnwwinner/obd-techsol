import requests
import time
import random

SERVER_URL = "http://localhost:8000/data"

while True:
    data = {
        "vehicle_id": "TRUCK001",
        "lat": 13.7563 + random.uniform(-0.01, 0.01),
        "lon": 100.5018 + random.uniform(-0.01, 0.01),
        "speed": random.randint(0, 100),
        "fuel": random.uniform(10, 80)
    }

    try:
        res = requests.post(SERVER_URL, json=data)
        print("Sent:", data, "Status:", res.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)
