from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from apps.users.schemas import UserCreate, UserResponse
from apps.users.services import create_user, get_user_by_email
from core.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)