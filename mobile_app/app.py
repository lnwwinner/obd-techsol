import requests
import time
import random

SERVER_URL = "http://localhost:8000/data"
VEHICLE_ID = "TRUCK001"


def get_gps():
    # จำลอง GPS (ของจริงจะใช้ mobile GPS)
    lat = 13.75 + random.uniform(-0.01, 0.01)
    lon = 100.50 + random.uniform(-0.01, 0.01)
    return lat, lon


def send_data():
    while True:
        lat, lon = get_gps()

        payload = {
            "vehicle_id": VEHICLE_ID,
            "lat": lat,
            "lon": lon,
            "speed": random.randint(40, 100),
            "fuel": random.randint(10, 50)
        }

        try:
            res = requests.post(SERVER_URL, json=payload)
            print("Sent:", payload, "Response:", res.json())
        except Exception as e:
            print("Error:", e)

        time.sleep(3)


if __name__ == "__main__":
    send_data()
