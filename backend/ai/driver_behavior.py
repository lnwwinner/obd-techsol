import math

class DriverBehaviorAnalyzer:

    def __init__(self):
        self.prev_speed = None
        self.prev_time = None

    def analyze(self, speed, timestamp, engine_on=True, moving=True):
        result = {
            "aggressive_acceleration": False,
            "harsh_braking": False,
            "idling": False,
            "score": 100
        }

        if self.prev_speed is not None and self.prev_time is not None:
            dt = timestamp - self.prev_time
            dv = speed - self.prev_speed

            if dt > 0:
                accel = dv / dt

                # aggressive acceleration
                if accel > 3:  # m/s^2
                    result["aggressive_acceleration"] = True
                    result["score"] -= 10

                # harsh braking
                if accel < -4:
                    result["harsh_braking"] = True
                    result["score"] -= 15

        # idling detection
        if engine_on and not moving:
            result["idling"] = True
            result["score"] -= 5

        self.prev_speed = speed
        self.prev_time = timestamp

        return result
