from typing import Dict, Literal
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import asc, desc
from core.schemas.jwt import DecodedToken
from core.schemas.users import User as CreateUser, UserChangePassword, UserLogin, UserLoginResponse, UserResponse, UserUpdate
from core.models.users import User
from sqlalchemy.orm import Session
from core.models.database import get_db
import bcrypt
from services.jwt import signJWT
from dependencies.authenticate import authenticate, check_is_self, parse_token
from fastapi_pagination import paginate, Page

router = APIRouter()


@router.post('/create', response_model=UserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = User(username=user.username, email=user.email,
                    password=hashed_password, bio=user.bio)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/login', response_model=UserLoginResponse)
def login(data: UserLogin, db: Session = Depends(get_db)) -> UserLoginResponse:
    user = db.query(User).filter(User.email == data.email).first()

    if user is None:
        return HTTPException(status_code=404, detail='user not found')

    correctPassword = bcrypt.checkpw(data.password.encode(
        'utf-8'), user.password.encode('utf-8'))

    if not correctPassword:
        raise HTTPException(
            status_code=404, detail='incorrect email or password')

    user.access_token = signJWT(userId=user.id)

    return user


@router.patch('/update', dependencies=[Depends(check_is_self), Depends(authenticate)], response_model=UserResponse)
def update_user(data: UserUpdate, db: Session = Depends(get_db)) -> UserResponse:
    user = User.get_user(id=data.id, db=db)

    if not user:
        raise HTTPException(status_code=404, detail='user not found')

    update = data.dict(exclude={'id'}, exclude_unset=True)
    for key, value in update.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete('/delete/{user_id}', dependencies=[Depends(authenticate)], response_model=Dict[str, bool])
def delete_user(user_id: int, decoded_token: DecodedToken = Depends(parse_token), db: Session = Depends(get_db)) -> dict[str, bool]:
    if not user_id == decoded_token['userId']:
        raise HTTPException(
            status_code=401, details='you cannot delete this user')

    user = User.get_user(id=user_id, db=db)

    if not user:
        raise HTTPException(status_code=404, detail='user not found')

    db.delete(user)
    db.commit()

    return {'Success': True}


@router.put('/reset_password/{user_id}', dependencies=[Depends(authenticate)], response_model=UserResponse)
def change_password(data: UserChangePassword, user_id: int, decoded_token: DecodedToken = Depends(parse_token), db: Session = Depends(get_db)):
    user = User.get_user(id=user_id, db=db)

    if not user_id == decoded_token['userId']:
        raise HTTPException(
            status_code=401, detail='You cannot perfrom this operation')
    if not user:
        raise HTTPException(status_code=404, detail='user not found')

    correct_password = bcrypt.checkpw(data.old_password.encode(
        'utf-8'), user.password.encode('utf-8'))

    if not correct_password:
        raise HTTPException(
            status_code=401, detail='Incorrect password provided')

    hashed_password = bcrypt.hashpw(
        data.new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    setattr(user, 'password', hashed_password)

    db.commit()
    db.refresh(user)
    return user


@router.get('/all', dependencies=[Depends(authenticate)], response_model=Page[UserResponse])
def get_all_users(
        order_by: Literal['username', 'bio',
                          'email'] = Query(default='username'),
        search_string: str = Query(default=''),
        order: Literal['asc', 'desc'] = Query(default='asc'),
        db: Session = Depends(get_db)) -> Page[UserResponse]:

    term = f'%{search_string}%'
    order_fn = asc if order == 'asc' else desc
    keys = {
        "username": User.username,
        "email": User.email,
        "bio": User.bio
    }
    filter_by = User.username.like(
        term) | User.email.like(term) | User.bio.like(term)

    return paginate(db.query(User).filter(filter_by).order_by(order_fn(keys[order_by])).all())
