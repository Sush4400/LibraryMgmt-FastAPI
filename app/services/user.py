from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud.user import UserDAO
from app.models.user import User
from app.models.token import BlacklistedToken
from app.core.security import hash_password, verify_password, create_access_token


class UserService:

    @staticmethod
    def register_user(db: Session, user_data):
        existing = UserDAO.get_by_email(db, user_data.email)
        if existing:
            raise HTTPException(400, "Email already registered")

        new_user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            username=user_data.username,
            hashed_password=hash_password(user_data.password),
        )

        return UserDAO.create(db, new_user)

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserDAO.get_by_email(db, email)

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

        token = create_access_token({"sub": str(user.id)})

        return {"access_token": token, "token_type": "bearer"}

    @staticmethod
    def logout(db: Session, token: str):
        print("inside logout")
        print("token: ", token)
        db.add(BlacklistedToken(token=token))
        db.commit()
        return {"message": "Logged out successfully"}

    @staticmethod
    def get_users(db: Session):
        return UserDAO.get_all(db)

    @staticmethod
    def get_user(db: Session, user_id: int):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        return user

    @staticmethod
    def update_user(db: Session, user_id: int, data: dict):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")

        return UserDAO.update(db, user, data)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")

        UserDAO.delete(db, user)
        return {"message": "User deleted"}