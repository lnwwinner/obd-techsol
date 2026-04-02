import hashlib

class DeviceFingerprint:

    def generate(self, device_info: dict):
        """
        device_info example:
        {
            "imei": "123",
            "model": "Samsung",
            "os": "Android 14",
            "brand": "Samsung"
        }
        """
        raw = f"{device_info.get('imei')}|{device_info.get('model')}|{device_info.get('os')}|{device_info.get('brand')}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def verify(self, stored_fingerprint, device_info: dict):
        return stored_fingerprint == self.generate(device_info)
