import hashlib
import time

class IdentityGuard:

    def __init__(self):
        # driver_id -> device_id
        self.bindings = {}
        # token -> session
        self.sessions = {}

    def register_device(self, driver_id, device_id):
        # bind driver to a single device
        self.bindings[driver_id] = device_id
        return True

    def validate_device(self, driver_id, device_id):
        bound = self.bindings.get(driver_id)
        return bound == device_id

    def create_session(self, driver_id, device_id):
        if not self.validate_device(driver_id, device_id):
            return None

        raw = f"{driver_id}:{device_id}:{time.time()}"
        token = hashlib.sha256(raw.encode()).hexdigest()

        self.sessions[token] = {
            "driver_id": driver_id,
            "device_id": device_id,
            "created": time.time()
        }

        return token

    def validate_token(self, token, driver_id, device_id):
        session = self.sessions.get(token)

        if not session:
            return False

        if session["driver_id"] != driver_id:
            return False

        if session["device_id"] != device_id:
            return False

        return True

    def revoke(self, driver_id):
        # remove all sessions of this driver
        self.sessions = {
            k: v for k, v in self.sessions.items()
            if v["driver_id"] != driver_id
        }
