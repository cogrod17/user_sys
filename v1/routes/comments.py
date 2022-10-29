from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy import asc
from sqlalchemy.orm import Session
from core.models.database import get_db
from core.schemas.comments import CommentListItem, CreateComment, BaseComment
from core.models.comments import Comment
from dependencies.authenticate import authenticate


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


@router.get('/{post_id}', response_model=Page[CommentListItem])
def get_comments(post_id: int, db: Session = Depends(get_db)) -> List[CommentListItem]:
    return paginate(db.query(Comment).filter(Comment.post_id ==
                                             post_id).order_by(asc(Comment.created_at)).all())
