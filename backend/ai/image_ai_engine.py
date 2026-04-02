import random

class ImageAIEngine:

    def analyze(self, metadata):
        # mock AI analysis (replace with real model later)
        results = {}

        # ตรวจว่ามีรถหรือไม่
        results["vehicle_detected"] = True if metadata.get("vehicle") else False

        # ตรวจความเสียหาย (mock)
        results["damage_detected"] = random.choice([True, False])

        # ตรวจภาพปลอม (mock fraud detection)
        results["fraud_risk"] = random.choice(["LOW", "MEDIUM", "HIGH"])

        # ตรวจคุณภาพภาพ
        blur_score = metadata.get("blur_score", 0)
        results["quality"] = "BAD" if blur_score > 0.7 else "GOOD"

        return results
