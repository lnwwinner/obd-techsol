class ReplayEngine:

    def __init__(self, timeline_engine):
        self.timeline = timeline_engine

    def build_replay(self, vehicle_id):
        events = self.timeline.get_timeline(vehicle_id)

        replay = []

        for e in events:
            replay.append({
                "time": e["timestamp"],
                "action": e["event_type"],
                "driver": e["driver_id"]
            })

        return replay
