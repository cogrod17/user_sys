from datetime import datetime
from typing import Literal
from pydantic import BaseModel
from core.schemas.users import UserResponse


class BasePost(BaseModel):
    id: int
    created_at: datetime = None
    text: str
    user_id: int

    class Config:
        orm_mode = True


class CreatePost(BaseModel):
    text: str


class PostReturn(BasePost):
    user: UserResponse
