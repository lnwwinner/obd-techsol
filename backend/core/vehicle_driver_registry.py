class VehicleDriverRegistry:

    def __init__(self):
        # vehicle_id -> list of driver records
        self.registry = {}

    def register_vehicle(self, vehicle_id):
        if vehicle_id not in self.registry:
            self.registry[vehicle_id] = []

    def assign_driver(self, vehicle_id, driver_id, timestamp):
        self.register_vehicle(vehicle_id)

        # set all to inactive
        for d in self.registry[vehicle_id]:
            d["status"] = "inactive"

        # add new active driver record
        record = {
            "driver_id": driver_id,
            "status": "active",
            "last_active": timestamp
        }

        self.registry[vehicle_id].append(record)
        return record

    def switch_driver(self, vehicle_id, driver_id, timestamp):
        self.register_vehicle(vehicle_id)

        found = False

        for d in self.registry[vehicle_id]:
            if d["driver_id"] == driver_id:
                d["status"] = "active"
                d["last_active"] = timestamp
                found = True
            else:
                d["status"] = "inactive"

        if not found:
            return self.assign_driver(vehicle_id, driver_id, timestamp)

        return True

    def get_active_driver(self, vehicle_id):
        for d in self.registry.get(vehicle_id, []):
            if d["status"] == "active":
                return d
        return None

    def get_history(self, vehicle_id):
        return self.registry.get(vehicle_id, [])
