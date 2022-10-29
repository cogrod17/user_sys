from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.models.database import get_db
from core.schemas.comments import CreateComment, BaseComment
from core.models.comments import Comment


router = APIRouter()


@router.post('/create/', response_model=BaseComment)
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
