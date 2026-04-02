from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.models.user_vehicle import UserVehicle

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/bind")
def bind_vehicle(data: dict, db: Session = Depends(get_db)):
    record = UserVehicle(username=data['username'], vehicle_id=data['vehicle_id'])
    db.add(record)
    db.commit()
    return {"status":"bound"}

@router.get("/my-vehicles/{username}")
def get_my_vehicles(username: str, db: Session = Depends(get_db)):
    records = db.query(UserVehicle).filter(UserVehicle.username == username).all()
    return [r.vehicle_id for r in records]
