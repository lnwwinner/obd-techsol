class AutoDecisionEngine:

    def decide(self, vehicle_state: dict, risks: dict):
        actions = []

        # ถ้ามีความเสี่ยงสูง
        if risks.get("level") == "HIGH":
            actions.append("REDUCE_SPEED")
            actions.append("NOTIFY_SUPERVISOR")

        # ถ้ามี error code
        if vehicle_state.get("error_code"):
            actions.append("CHECK_ENGINE_IMMEDIATELY")

        # ถ้าอุณหภูมิสูงมาก
        if vehicle_state.get("engine_temp", 0) > 110:
            actions.append("FORCE_STOP")

        return {
            "vehicle_id": vehicle_state.get("vehicle_id"),
            "actions": actions
        }
