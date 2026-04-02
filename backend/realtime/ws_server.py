from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict

app = FastAPI()

# เก็บ connection ตาม vehicle_id
connections: Dict[str, WebSocket] = {}

@app.websocket("/ws/{vehicle_id}")
async def websocket_endpoint(websocket: WebSocket, vehicle_id: str):
    await websocket.accept()
    connections[vehicle_id] = websocket

    try:
        while True:
            data = await websocket.receive_json()

            # รับ heartbeat / status จาก mobile
            print(f"[{vehicle_id}] DATA:", data)

            # ส่ง command กลับ (mock)
            await websocket.send_json({
                "command": "SYNC_OK",
                "vehicle_id": vehicle_id
            })

    except WebSocketDisconnect:
        connections.pop(vehicle_id, None)
        print(f"{vehicle_id} disconnected")

# ฟังก์ชัน push command จาก server
async def push_command(vehicle_id: str, command: dict):
    ws = connections.get(vehicle_id)
    if ws:
        await ws.send_json(command)
