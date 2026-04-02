from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.core.database import Base

class VehicleData(Base):
    __tablename__ = "vehicle_data"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    speed = Column(Float)
    fuel = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
