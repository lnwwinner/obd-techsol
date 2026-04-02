from datetime import datetime

class TimelineEngine:

    def __init__(self):
        # vehicle_id -> list of events
        self.timeline = {}

    def log_event(self, vehicle_id, driver_id, event_type, metadata=None):
        if vehicle_id not in self.timeline:
            self.timeline[vehicle_id] = []

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "driver_id": driver_id,
            "event_type": event_type,
            "metadata": metadata or {}
        }

        self.timeline[vehicle_id].append(event)
        return event

    def get_timeline(self, vehicle_id):
        return self.timeline.get(vehicle_id, [])

    def get_driver_timeline(self, vehicle_id, driver_id):
        return [
            e for e in self.timeline.get(vehicle_id, [])
            if e["driver_id"] == driver_id
        ]

    def get_recent_events(self, vehicle_id, limit=10):
        return self.timeline.get(vehicle_id, [])[-limit:]

    def summarize(self, vehicle_id):
        summary = {}

        for e in self.timeline.get(vehicle_id, []):
            etype = e["event_type"]
            summary[etype] = summary.get(etype, 0) + 1

        return summary
