from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
from sqlalchemy import String


class BlacklistedToken(Base):
    __tablename__ = "blacklisted_tokens"

    token: Mapped[str] = mapped_column(String, primary_key=True)