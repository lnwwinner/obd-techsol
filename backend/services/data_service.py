from sqlalchemy.orm import Session
from backend.models.data_model import VehicleData

def save_vehicle_data(db: Session, data: dict):
    record = VehicleData(
        vehicle_id=data.get("vehicle_id"),
        lat=data.get("lat"),
        lon=data.get("lon"),
        speed=data.get("speed"),
        fuel=data.get("fuel")
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
