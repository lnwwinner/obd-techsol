class DigitalTwin:

    def __init__(self):
        # vehicle_id -> state
        self.state = {}

    def update(self, vehicle_id, data: dict):
        if vehicle_id not in self.state:
            self.state[vehicle_id] = {}

        self.state[vehicle_id].update(data)
        return self.state[vehicle_id]

    def get(self, vehicle_id):
        return self.state.get(vehicle_id, {})

    def snapshot(self, vehicle_id):
        return {
            "vehicle_id": vehicle_id,
            "state": self.get(vehicle_id)
        }
