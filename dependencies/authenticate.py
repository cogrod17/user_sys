from fastapi import Depends, Header,  Body, HTTPException
from core.schemas.jwt import DecodedToken
from core.schemas.users import UserId
from services.jwt import decode, is_self, verify_token
from typing import Union


def get_token(Authorization: str = Header()) -> Union[str, None]:
    try:
        token = Authorization.split(' ')[1]
        yield token
    finally:
        pass


def parse_token(token: str = Depends(get_token)) -> Union[DecodedToken, None]:
    try:
        x = decode(token)
        yield x
    finally:
        pass


def authenticate(token: str = Depends(get_token)) -> None:
    if not token:
        raise HTTPException(status_code=401, detail='Unauthorized')
    if not verify_token(token):
        raise HTTPException(status_code=401, detail='Your session has expired')


def check_is_self(token: str = Depends(get_token), data: UserId = Body()) -> None:
    if not token:
        raise HTTPException(status_code=401, detail='Unauthorized')
    if not data.id:
        raise HTTPException(status=400, detail='Please provide a user id')
    if not is_self(token=token, id=data.id):
        raise HTTPException(
            status_code=400, detail='You cannot perform this operation')


def get_user_id(token: str = Depends(get_token)) -> Union[int, None]:
    try:
        x = decode(token)
        yield x['userId']
    finally:
        pass
