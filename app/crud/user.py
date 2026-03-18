from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User


class UserDAO:

    @staticmethod
    def get_by_email(db: Session, email: str) -> User:
        stmt = select(User).where(User.email == email)
        result = db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User:
        return db.get(User, user_id)

    @staticmethod
    def get_all(db: Session) -> list[User]:
        stmt = select(User)
        result = db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    def create(db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(db: Session, db_user: User, update_data: dict) -> User:
        for key, value in update_data.items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete(db: Session, db_user: User):
        db.delete(db_user)
        db.commit()