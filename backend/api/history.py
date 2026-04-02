from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.models.data_model import VehicleData

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vehicle/{vehicle_id}/history")
def get_history(vehicle_id: str, db: Session = Depends(get_db)):
    data = db.query(VehicleData).filter(VehicleData.vehicle_id == vehicle_id).order_by(VehicleData.timestamp.desc()).limit(50).all()

    return [
        {
            "lat": d.lat,
            "lon": d.lon,
            "speed": d.speed,
            "fuel": d.fuel,
            "timestamp": str(d.timestamp)
        }
        for d in data
    ]
