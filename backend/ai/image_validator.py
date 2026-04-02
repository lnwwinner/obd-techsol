class ImageValidator:

    def validate(self, metadata):
        issues = []

        if not metadata.get("vehicle"):
            issues.append("Missing vehicle ID")

        if not metadata.get("driver"):
            issues.append("Missing driver ID")

        if metadata.get("blur_score", 0) > 0.7:
            issues.append("Image too blurry")

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }
