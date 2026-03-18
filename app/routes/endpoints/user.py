from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.db import get_db
from app.services.user import UserService
from app.schemas.user import UserCreate, UserLogin, UserUpdate, UserResponse
from app.core.utils import get_current_user


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.register_user(db, user)


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    return UserService.login(db, data.email, data.password)


@router.post("/logout")
def logout(token=Depends(get_current_user), db: Session = Depends(get_db)):
    return UserService.logout(db, token)


@router.get("", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return UserService.update_user(db, user_id, data.model_dump(exclude_unset=True))


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db, user_id)