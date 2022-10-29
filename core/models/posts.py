from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, sql
from core.models.database import Base, Session
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=sql.func.now())
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)

    user = relationship('User', foreign_keys=[user_id])
    comments = relationship('Comment', cascade='all, delete',
                            primaryjoin='Comment.post_id == Post.id')

    @classmethod
    def get_post_by_id(self, id: int, db: Session):
        return db.query(self).filter(self.id == id).first()
