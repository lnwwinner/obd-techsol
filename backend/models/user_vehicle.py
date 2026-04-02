from sqlalchemy import Column, Integer, String
from backend.core.database import Base

class UserVehicle(Base):
    __tablename__ = "user_vehicle"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    vehicle_id = Column(String)
