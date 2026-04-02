class EmergencyHandler:

    def __init__(self, timeline, notifier):
        self.timeline = timeline
        self.notifier = notifier

    def handle_unknown_driver(self, vehicle_id):
        event = {
            "event": "UNKNOWN_DRIVER",
            "severity": "CRITICAL",
            "message": "Vehicle in motion without identified driver"
        }

        # log to timeline
        self.timeline.log_event(
            vehicle_id=vehicle_id,
            driver_id="UNKNOWN",
            event_type="EMERGENCY_UNKNOWN_DRIVER",
            metadata=event
        )

        # notify system (dashboard / supervisor)
        self.notifier.send_alert(vehicle_id, event)

        return event

    def handle_no_sync(self, vehicle_id):
        event = {
            "event": "NO_DRIVER_SYNC",
            "severity": "WARNING",
            "message": "No driver sync detected"
        }

        self.timeline.log_event(
            vehicle_id=vehicle_id,
            driver_id="UNKNOWN",
            event_type="WARNING_NO_SYNC",
            metadata=event
        )

        self.notifier.send_alert(vehicle_id, event)

        return event
