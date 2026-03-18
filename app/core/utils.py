from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from .db import get_db
from app.models.token import BlacklistedToken

security = HTTPBearer()


def get_current_user(token=Depends(security), db: Session = Depends(get_db)):
    token_str = token.credentials

    blacklisted = db.query(BlacklistedToken).filter_by(token=token_str).first()
    if blacklisted:
        raise HTTPException(401, "Token is blacklisted")

    payload = decode_token(token_str)
    return payload["sub"]