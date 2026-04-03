class DecisionSafety:

    def validate_action(self, action: str, obd_data: dict):
        speed = obd_data.get("speed", 0)

        # ห้าม force stop ถ้าความเร็วสูงเกิน
        if action == "FORCE_STOP" and speed > 40:
            return {
                "allowed": False,
                "reason": "HIGH_SPEED_BLOCK"
            }

        # reduce speed ใช้ได้เสมอ
        if action == "REDUCE_SPEED":
            return {
                "allowed": True
            }

        return {
            "allowed": True
        }
