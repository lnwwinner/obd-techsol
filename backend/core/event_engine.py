class EventEngine:

    def __init__(self):
        self.events = []

    def publish(self, event_type: str, vehicle_id: str, data: dict):
        event = {
            "type": event_type,
            "vehicle_id": vehicle_id,
            "data": data
        }

        self.events.append(event)
        print("EVENT:", event)

    def get_all(self):
        return self.events
