class DriverScoring:

    def __init__(self):
        self.scores = {}

    def update_score(self, driver_id, event_type):
        if driver_id not in self.scores:
            self.scores[driver_id] = 100

        if event_type == "HARSH_BRAKE":
            self.scores[driver_id] -= 10
        elif event_type == "AGGRESSIVE_ACCEL":
            self.scores[driver_id] -= 8
        elif event_type == "OVERSPEED":
            self.scores[driver_id] -= 15

        return self.scores[driver_id]

    def get_score(self, driver_id):
        return self.scores.get(driver_id, 100)
