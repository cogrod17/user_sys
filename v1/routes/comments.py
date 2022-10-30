from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy import asc
from sqlalchemy.orm import Session
from core.models.database import get_db
from core.schemas.comments import CommentListItem, CommentUpdate, CreateComment, BaseComment
from core.models.comments import Comment
from core.schemas.posts import DeleteRes
from dependencies.authenticate import authenticate, get_user_id


router = APIRouter()


@router.post('/create/', dependencies=[Depends(authenticate)], response_model=BaseComment)
def post_comment(data: CreateComment, db: Session = Depends(get_db)) -> BaseComment:

    try:
        new_comment = Comment(
            text=data.text, user_id=data.user_id, post_id=data.post_id)

        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)

        return new_comment
    except:
        raise HTTPException(status_code=500, detail='There was an error')


@router.get('/{post_id}', dependencies=[Depends(authenticate)], response_model=Page[CommentListItem])
def get_comments(post_id: int, db: Session = Depends(get_db)) -> List[CommentListItem]:
    return paginate(db.query(Comment).filter(Comment.post_id ==
                                             post_id).order_by(asc(Comment.created_at)).all())


@router.delete('/{comment_id}', dependencies=[Depends(authenticate)], response_model=DeleteRes)
def delete_comment(comment_id: int, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)) -> DeleteRes:
    comment = db.query(Comment).get(comment_id)

    if not comment:
        raise HTTPException(status_code=404)

    if comment.user_id != user_id:
        raise HTTPException(
            status_code=401, detail='You cannot perform this action')

    try:
        db.delete(comment)
        db.commit()
        return {'message': 'success'}
    except:
        raise HTTPException(status_code=500)


@router.put('/update/{comment_id}', dependencies=[Depends(authenticate)], response_model=BaseComment)
def update_comment(comment_id: int, body: CommentUpdate = Body(),  db: Session = Depends(get_db)) -> BaseComment:
    comment = db.query(Comment).get(comment_id)

    if not comment:
        raise HTTPException(status_code=404, detail='comment not found')

    try:
        setattr(comment, 'text', body.text)
        db.commit()
        db.refresh(comment)

        return comment
    except:
        raise HTTPException(status_code=500)
