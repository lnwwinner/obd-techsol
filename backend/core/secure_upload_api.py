from flask import Flask, request, jsonify
import hashlib
import base64

app = Flask(__name__)

SECRET = "server-secret-key"

# Mock storage
STORAGE = {}

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.json

    image_base64 = data.get("image")
    vehicle = data.get("vehicle")
    driver = data.get("driver")

    if not image_base64 or not vehicle:
        return jsonify({"error": "invalid data"}), 400

    # decode image
    image_bytes = base64.b64decode(image_base64)

    # generate hash (anti-tamper)
    image_hash = hashlib.sha256(image_bytes).hexdigest()

    # store
    key = f"{vehicle}_{driver}_{image_hash}"
    STORAGE[key] = {
        "vehicle": vehicle,
        "driver": driver,
        "hash": image_hash,
        "size": len(image_bytes)
    }

    return jsonify({
        "status": "ok",
        "hash": image_hash
    })

@app.route('/api/verify/<hash>', methods=['GET'])
def verify(hash):
    for k, v in STORAGE.items():
        if v["hash"] == hash:
            return jsonify({"valid": True, "data": v})

    return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(port=8000)
