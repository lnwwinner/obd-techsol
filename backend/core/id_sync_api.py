from flask import Flask, request, jsonify

app = Flask(__name__)

# mock state store
DEVICE_STATE = {}

@app.route('/api/sync', methods=['POST'])
def sync():
    data = request.json

    driver_id = data.get("driver_id")
    vehicle_id = data.get("vehicle_id")
    status = data.get("status")

    if not driver_id or not vehicle_id:
        return jsonify({"error": "missing id"}), 400

    key = f"{vehicle_id}_{driver_id}"

    # update state
    DEVICE_STATE[key] = {
        "vehicle_id": vehicle_id,
        "driver_id": driver_id,
        "status": status
    }

    # mock response (server decision)
    response = {
        "vehicle_id": vehicle_id,
        "driver_id": driver_id,
        "command": "CONTINUE",
        "message": "SYNC OK"
    }

    return jsonify(response)

@app.route('/api/status/<vehicle_id>/<driver_id>', methods=['GET'])
def get_status(vehicle_id, driver_id):
    key = f"{vehicle_id}_{driver_id}"
    return jsonify(DEVICE_STATE.get(key, {}))

if __name__ == '__main__':
    app.run(port=8002)
