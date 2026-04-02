from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.models.user_model import User

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    user = User(username=data['username'], password=data['password'], role=data.get('role','user'))
    db.add(user)
    db.commit()
    return {"status":"registered"}

@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username==data['username'], User.password==data['password']).first()

    if not user:
        return {"status":"fail"}

    return {
        "status":"success",
        "role": user.role,
        "username": user.username
    }
