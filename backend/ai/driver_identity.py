class DriverIdentityManager:

    def __init__(self):
        self.active_sessions = {}

    def login(self, username, device_id, vehicle_id):
        session = {
            "username": username,
            "device_id": device_id,
            "vehicle_id": vehicle_id,
            "status": "active"
        }

        self.active_sessions[vehicle_id] = session
        return session

    def get_driver(self, vehicle_id):
        return self.active_sessions.get(vehicle_id, None)

    def logout(self, vehicle_id):
        if vehicle_id in self.active_sessions:
            self.active_sessions[vehicle_id]["status"] = "inactive"
            return True
        return False
