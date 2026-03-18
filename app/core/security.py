from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import get_settings
import bcrypt, hashlib


settings = get_settings()


def hash_password(password: str) -> str:
    password_bytes = hashlib.sha256(password.encode("utf-8")).digest()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode()


def verify_password(password: str, hashed: str) -> bool:
    password_bytes = hashlib.sha256(password.encode("utf-8")).digest()
    return bcrypt.checkpw(password_bytes, hashed.encode())


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])