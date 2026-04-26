from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService
from app.db.session import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService(db).signup(user)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService(db).login(user)