def calculate_score(data: dict):
    score = 100
    issues = []

    speed = data.get("speed", 0)
    fuel = data.get("fuel", 100)

    if speed > 100:
        score -= 10
        issues.append("High Speed")

    if 80 < speed <= 100:
        score -= 5
        issues.append("Aggressive Driving")

    if fuel < 10:
        score -= 5
        issues.append("Low Fuel Risk")

    return {
        "score": max(score, 0),
        "issues": issues
    }
