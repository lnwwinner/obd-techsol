class ValidationEngine:

    def validate(self, mobile_data: dict, obd_data: dict):
        result = {
            "valid": True,
            "issues": []
        }

        # ตรวจความเร็ว
        if "speed" in mobile_data and "speed" in obd_data:
            if abs(mobile_data["speed"] - obd_data["speed"]) > 10:
                result["valid"] = False
                result["issues"].append("SPEED_MISMATCH")

        # ตรวจสถานะเครื่องยนต์
        if mobile_data.get("engine") != obd_data.get("engine"):
            result["valid"] = False
            result["issues"].append("ENGINE_STATE_MISMATCH")

        return result
