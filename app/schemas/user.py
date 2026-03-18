from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime




class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    user_role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S") if v else None
        }
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str = "bearer"
