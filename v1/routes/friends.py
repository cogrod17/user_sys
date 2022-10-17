from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import or_
from core.models.database import Session, get_db
from core.schemas.friends import FriendRequestResponse, FriendsListItem, NewFriendRequest, RequestListItem,  RespondReq, RespondReturn
from core.models.friends import Friends, status_keys
from core.schemas.jwt import DecodedToken
from dependencies.authenticate import authenticate, parse_token
from datetime import datetime


router = APIRouter()


def is_sender(data: NewFriendRequest, token: DecodedToken = Depends(parse_token)) -> None:
    if data.sender_id != token['userId']:
        raise HTTPException(
            status_code=400, detail='You cannot perform this operation')


@router.put('/send_request', dependencies=[Depends(authenticate), Depends(is_sender)], response_model=FriendRequestResponse)
def send_friend_req(data: NewFriendRequest,  db: Session = Depends(get_db)) -> Friends:
    if data.sender_id == data.recipient_id:
        raise HTTPException(
            status_code=400, detail='You cannot send a request to yourself')

    exists = db.query(Friends).filter(
        Friends.sender_id == data.sender_id, Friends.recipient_id == data.recipient_id).first()

    if exists:
        raise HTTPException(
            status_code=400, detail="You have already sent a friend request to this user")

    new_req = Friends(message=data.message,
                      sender_id=data.sender_id, recipient_id=data.recipient_id,
                      )

    db.add(new_req)
    db.commit()
    db.refresh(new_req)

    return new_req


@router.put('/respond/{request_id}', dependencies=[Depends(authenticate)], response_model=RespondReturn, status_code=200)
def respond(data: RespondReq, request_id: int, token: DecodedToken = Depends(parse_token), db: Session = Depends(get_db)):
    req = db.query(Friends).filter(Friends.id == request_id,
                                   Friends.recipient_id == token['userId'], Friends.status == status_keys['pending']).first()

    if not req:
        raise HTTPException(status_code=404, detail='Request not found')

    if data.accept is True:
        req.status = 2
        req.accepted_at = datetime.now()

        db.commit()
        db.refresh(req)
        return {"accept": True, 'message': 'Request accepted'}
    else:
        db.delete(req)
        db.commit()
        return {'accept': False, 'message': 'Request declined'}


@router.get('/{user_id}', dependencies=[Depends(authenticate)], response_model=List[FriendsListItem])
def get_friends(user_id: int,  db: Session = Depends(get_db)) -> List[FriendsListItem]:
    friends = db.query(Friends).filter(or_(Friends.recipient_id ==
                                           user_id, Friends.sender_id == user_id), Friends.status == status_keys['accepted']).all()

    for relation in friends:
        if relation.sender_id == user_id:
            relation.friend = relation.recipient
        if relation.recipient_id == user_id:
            relation.friend = relation.sender

    return friends


@router.get('/requests/{user_id}', dependencies=[Depends(authenticate)], response_model=List[RequestListItem])
def get_requests(user_id: int, db: Session = Depends(get_db)) -> List[RequestListItem]:
    return db.query(Friends).filter(Friends.recipient_id ==
                                    user_id, Friends.status == status_keys['pending']).all()


@router.delete('/delete/{request_id}', dependencies=[Depends(authenticate)])
def delete_friend(request_id: int, token: DecodedToken = Depends(parse_token), db: Session = Depends(get_db)):
    relation = db.query(Friends).filter(Friends.id == request_id, or_(
        Friends.sender_id == token['userId'], Friends.recipient_id == token['userId'])).first()

    if not relation:
        raise HTTPException(status_code=404, detail='Could not find friend')

    db.delete(relation)
    db.commit()

    return {'success': True, 'message': 'You have removed this friend'}
