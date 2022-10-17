from pydantic import BaseModel, Field, EmailStr
from typing import Union


class UserId(BaseModel):
    id: int


class User(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    bio: str = Field(default=None)
    password: str = Field(default=None)


class UserLogin(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)


class UserUpdate(BaseModel):
    id: int
    username: Union[str, None] = None
    email: Union[EmailStr, None] = None
    bio: Union[str, None] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    bio: str

    class Config:
        orm_mode = True


class UserLoginResponse(UserResponse):
    access_token: str

    def __init__(self):
        super().__init__()


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str
