from datetime import datetime
from typing import Union
from pydantic import BaseModel
from core.schemas.users import UserResponse


class BaseFriend(BaseModel):
    id: int
    sent_at: datetime
    message: str
    status: int
    sender_id: int
    accepted_at: Union[datetime, None]
    recipient_id: int

    class Config:
        orm_mode = True


class NewFriendRequest(BaseModel):
    message: str = None
    sender_id: int
    recipient_id: int


class FriendRequestResponse(BaseModel):
    message: str = None
    sender_id: int
    recipient_id: int
    sent_at: datetime
    sender: UserResponse
    recipient: UserResponse

    class Config:
        orm_mode = True


class RespondReq(BaseModel):
    accept: bool


class RespondReturn(RespondReq):
    message: str


class FriendsListItem(BaseFriend):
    friend: UserResponse


class RequestListItem(BaseFriend):
    sender: UserResponse


class DeleteRes(BaseModel):
    success: bool
    message: str
