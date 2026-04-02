from datetime import datetime, timedelta

class DriverPresenceIntegration:

    def __init__(self, event_engine, timeout_seconds=15):
        self.event_engine = event_engine
        self.last_seen = {}  # vehicle_id -> {driver_id, ts}
        self.timeout = timedelta(seconds=timeout_seconds)

    def update_from_mobile(self, vehicle_id: str, driver_id: str):
        self.last_seen[vehicle_id] = {
            "driver_id": driver_id,
            "ts": datetime.utcnow()
        }

    def check_with_obd(self, vehicle_id: str, obd_data: dict):
        moving = obd_data.get("speed", 0) > 0
        data = self.last_seen.get(vehicle_id)

        if moving:
            if not data:
                self.event_engine.publish(
                    "EMERGENCY_UNKNOWN_DRIVER",
                    vehicle_id,
                    {"reason": "NO_DRIVER_BINDING"}
                )
                return False

            if datetime.utcnow() - data["ts"] > self.timeout:
                self.event_engine.publish(
                    "WARNING_NO_SYNC",
                    vehicle_id,
                    {"reason": "HEARTBEAT_TIMEOUT"}
                )
                return False

        return True
