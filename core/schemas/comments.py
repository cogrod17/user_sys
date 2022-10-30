from pydantic import BaseModel
from datetime import datetime
from core.schemas.posts import BasePost
from core.schemas.users import UserResponse


class BaseComment(BaseModel):
    id: int
    created_at: datetime
    text: str
    user_id: int
    post_id: int

    user: UserResponse
    post: BasePost

    class Config:
        orm_mode = True


class CreateComment(BaseModel):
    text: str
    post_id: int
    user_id: int


class CommentListItem(BaseModel):
    id: int
    created_at: datetime
    text: str
    user: UserResponse

    class Config:
        orm_mode = True


class CommentUpdate(BaseModel):
    text: str

    class Config:
        orm_mode = True
