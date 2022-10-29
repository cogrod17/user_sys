from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, sql
from core.models.database import Base
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=sql.func.now())
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Posts.id'), nullable=False)

    user = relationship('User', foreign_keys=[user_id])
    post = relationship('Post', foreign_keys=[post_id])
