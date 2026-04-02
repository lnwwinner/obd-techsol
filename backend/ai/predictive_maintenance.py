class PredictiveMaintenance:

    def analyze(self, vehicle_state: dict):
        """
        vehicle_state example:
        {
            "engine_temp": 95,
            "rpm": 3000,
            "error_code": "P0123",
            "usage_hours": 1200
        }
        """

        risks = []

        if vehicle_state.get("engine_temp", 0) > 100:
            risks.append("ENGINE_OVERHEAT_RISK")

        if vehicle_state.get("rpm", 0) > 4000:
            risks.append("HIGH_RPM_STRESS")

        if vehicle_state.get("error_code"):
            risks.append(f"ERROR_CODE_{vehicle_state['error_code']}")

        if vehicle_state.get("usage_hours", 0) > 1000:
            risks.append("MAINTENANCE_DUE")

        return {
            "vehicle_id": vehicle_state.get("vehicle_id"),
            "risks": risks,
            "level": "HIGH" if len(risks) >= 2 else "NORMAL"
        }
