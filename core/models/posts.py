from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, sql
from core.models.database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=sql.func.now())
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)

    user = relationship('User', foreign_keys=[user_id])
