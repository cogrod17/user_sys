from ctypes import Union
from datetime import datetime
from typing import List
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


class CommentOnPost(BaseModel):
    # id: int
    created_at: datetime
    text: str
    user: UserResponse

    class Config:
        orm_mode = True


class PostReturn(BasePost):
    user: UserResponse


class PostReturnWithComments(PostReturn):
    comments: List[CommentOnPost]


class DeleteRes(BaseModel):
    message: str


class EditPost(BaseModel):
    text: str
