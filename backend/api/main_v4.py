from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal, engine, Base
from backend.services.data_service import save_vehicle_data
from backend.services.alert_service import check_alerts
from backend.services.driver_score import calculate_score

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "OBD TechSol API Running (AI + Score Enabled)"}

@app.post("/data")
def receive_data(data: dict, db: Session = Depends(get_db)):
    save_vehicle_data(db, data)

    alerts = check_alerts(data)
    score = calculate_score(data)

    if alerts:
        print("🚨 ALERT:", alerts)

    print("🧠 SCORE:", score)

    return {
        "status": "saved",
        "alerts": alerts,
        "score": score
    }
