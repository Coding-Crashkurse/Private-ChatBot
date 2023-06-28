from pydantic import BaseModel
from typing import Optional
from enum import Enum


class UserLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    expert = "expert"


class UserBase(BaseModel):
    email: str
    username: str
    age: Optional[int] = None
    level: UserLevel = UserLevel.beginner


class UserIn(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
