from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.models.data_model import VehicleData

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vehicle/{vehicle_id}/latest")
def get_latest(vehicle_id: str, db: Session = Depends(get_db)):
    data = db.query(VehicleData).filter(VehicleData.vehicle_id == vehicle_id).order_by(VehicleData.timestamp.desc()).first()

    if not data:
        return {}

    return {
        "vehicle_id": data.vehicle_id,
        "lat": data.lat,
        "lon": data.lon,
        "speed": data.speed,
        "fuel": data.fuel,
        "timestamp": str(data.timestamp)
    }
