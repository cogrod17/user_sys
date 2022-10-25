from email.policy import HTTP
from typing import Literal
from fastapi import APIRouter, Body, Depends, HTTPException, Query
from sqlalchemy import asc, desc, sql
from core.models.database import get_db
from dependencies.authenticate import authenticate, get_user_id
from sqlalchemy.orm import Session
from core.models.posts import Post
from core.models.users import User
from core.schemas.posts import CreatePost, DeleteRes, EditPost, PostReturn
from fastapi_pagination import paginate, Page

router = APIRouter()


@router.post('/create', dependencies=[Depends(authenticate)], response_model=PostReturn)
def create_post(data: CreatePost, user_id: int = Depends(get_user_id),  db: Session = Depends(get_db)) -> PostReturn:
    new_post = Post(text=data.text, user_id=user_id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get('', dependencies=[Depends(authenticate)], response_model=Page[PostReturn])
def get_posts(
        order_by: Literal['text', 'created_at', 'username',
                          'user_email'] = Query(default='created_at'),
        order: Literal['asc', 'desc'] = Query(default='desc'),
        search_string: str = Query(default=''),
        db: Session = Depends(get_db)) -> Page[PostReturn]:

    try:
        order_fn = asc if order == 'asc' else desc
        keys = {
            'created_at': Post.created_at,
            'text': Post.text,
            'username': User.username,
            'user_email': User.email
        }

        term = '%' + search_string + "%"
        filter_by = User.username.like(term) | Post.text.like(
            term) | User.email.like(term)

        return paginate(db.query(Post).join(User).filter(
            filter_by).order_by(order_fn(keys[order_by])).all())
    except:
        HTTPException(status_code=500, detail='Something went wrong')


@router.put('/edit/{post_id}', dependencies=[Depends(authenticate)], response_model=PostReturn)
def edit_post(post_id: int, data: EditPost = Body(), user_id: int = Depends(get_user_id), db: Session = Depends(get_db)):
    post = Post.get_post_by_id(id=post_id, db=db)

    if post.user_id != user_id:
        raise HTTPException(status_code=401, detail='Unauthorized')

    try:
        setattr(post, 'text', data.text)
        db.commit()
        db.refresh(post)
        return post
    except:
        return HTTPException(status_code=500)


@router.delete('/delete/{post_id}', dependencies=[Depends(authenticate)], response_model=DeleteRes)
def delete_post(post_id: int, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post.user_id != user_id:
        raise HTTPException(status_code=401, detail='Unauthorized')

    try:
        db.delete(post)
        db.commit()
        return {'message': 'success'}
    except:
        raise HTTPException(status_code=500)
