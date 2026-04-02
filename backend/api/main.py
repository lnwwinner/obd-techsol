from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OBD TechSol API Running"}

@app.post("/data")
def receive_data(data: dict):
    print("Incoming data:", data)
    return {"status": "ok"}
