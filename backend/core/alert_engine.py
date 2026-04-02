class AlertEngine:

    def __init__(self, timeline, notifier):
        self.timeline = timeline
        self.notifier = notifier

    def check_engine_light(self, vehicle_id, obd_data):
        # obd_data example: {"engine_light": True, "code": "P0123"}
        if obd_data.get("engine_light"):
            event = {
                "event": "ENGINE_ALERT",
                "code": obd_data.get("code"),
                "severity": "CRITICAL"
            }

            self.timeline.log_event(
                vehicle_id=vehicle_id,
                driver_id="UNKNOWN",
                event_type="ENGINE_ALERT",
                metadata=event
            )

            self.notifier.send_alert(vehicle_id, event)

            return event

        return None
