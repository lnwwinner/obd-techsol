def check_alerts(data: dict):
    alerts = []

    # Speed alert
    if data.get("speed", 0) > 120:
        alerts.append("Over Speed")

    # Fuel anomaly (simple rule)
    if data.get("fuel", 100) < 5:
        alerts.append("Low Fuel")

    # Missing GPS
    if data.get("lat") is None or data.get("lon") is None:
        alerts.append("GPS Missing")

    return alerts
