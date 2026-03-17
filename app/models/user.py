from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    phone: Mapped[str] = mapped_column(String(20), nullable=True)

    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    user_role: Mapped[str] = mapped_column(
        String(50), nullable=False, server_default="user"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    sessions = relationship("UserSession", back_populates="user")


class UserSession(Base):
    __tablename__ = "user_sessions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True
    )

    token: Mapped[str] = mapped_column(String(512), unique=True, index=True)

    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )

    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    user = relationship("User", back_populates="sessions")