from datetime import datetime, timedelta

class DriverPresenceGuard:

    def __init__(self):
        self.last_seen = {}
        self.timeout_seconds = 15  # ถ้าไม่ sync เกินนี้ถือว่าไม่รู้ว่าใครขับ

    def update(self, vehicle_id, driver_id):
        key = vehicle_id
        self.last_seen[key] = {
            "driver_id": driver_id,
            "timestamp": datetime.utcnow()
        }

    def check(self, vehicle_id):
        data = self.last_seen.get(vehicle_id)

        if not data:
            return {
                "status": "UNKNOWN_DRIVER",
                "alert": True
            }

        now = datetime.utcnow()
        if now - data["timestamp"] > timedelta(seconds=self.timeout_seconds):
            return {
                "status": "NO_ACTIVE_DRIVER",
                "alert": True
            }

        return {
            "status": "OK",
            "driver_id": data["driver_id"],
            "alert": False
        }
