from sqlalchemy import String, Boolean, DateTime, text
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.core.db import Base


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    dob: Mapped[datetime] = mapped_column(DateTime)
    nationality: Mapped[str] = mapped_column(String(255))

    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("false")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
