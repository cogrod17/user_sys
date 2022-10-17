from fastapi import Depends
from core.models.database import Base, Session
from sqlalchemy import ForeignKey, String, Column, Integer, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    bio = Column(Text, nullable=True)
    password = Column(String, nullable=False)

    friend_requests = relationship(
        'Friends', cascade='all, delete',  primaryjoin="and_(or_(Friends.sender_id == User.id, Friends.recipient_id == User.id),  Friends.status == '1')", lazy='dynamic')
    friends = relationship('Friends', cascade='all, delete',
                           primaryjoin="and_(or_(Friends.sender_id == User.id, Friends.recipient_id == User.id),  Friends.status == '2')", lazy='dynamic')

    posts = relationship('Post', cascade='all, delete',
                         primaryjoin='Post.user_id == User.id')

    @classmethod
    def get_user(self, id: int, db: Session):
        return db.query(self).with_entities(User.id, User.username, User.email, User.bio).filter(self.id == id).first()

    def get_bio(self) -> str:
        return f'{self.bio}'

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"
