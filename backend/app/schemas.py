from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class Users(BaseModel):
    users: list[User]
    total: int


class Token(BaseModel):
    access_token: str
    token_type: str