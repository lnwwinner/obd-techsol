from enum import Enum

class VehicleState(Enum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    WARNING = "WARNING"
    RISK = "RISK"
    CRITICAL = "CRITICAL"
    EMERGENCY = "EMERGENCY"


class StateMachine:

    def __init__(self):
        self.current_state = VehicleState.IDLE

    def update(self, obd_data: dict, validation_result: dict):
        speed = obd_data.get("speed", 0)

        if not validation_result.get("valid", True):
            self.current_state = VehicleState.WARNING
            return self.current_state

        if speed == 0:
            self.current_state = VehicleState.IDLE

        elif speed > 0:
            self.current_state = VehicleState.RUNNING

        if obd_data.get("engine_error"):
            self.current_state = VehicleState.CRITICAL

        return self.current_state
