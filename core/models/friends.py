from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey, sql
from core.models.database import Base
from sqlalchemy.orm import relationship

# delete if request is declined
'''
status: 
1 = pending
2 = accepted

'''

status_keys = {'pending': 1, 'accepted': 2}


class Friends(Base):
    __tablename__ = 'Friends'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, default=None)
    sent_at = Column(DateTime(timezone=True), server_default=sql.func.now())

    accepted_at = Column(DateTime(timezone=True),
                         nullable=True, default=None)
    status = Column(Integer, default=1)

    sender_id = Column(Integer, ForeignKey(
        'Users.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey(
        'Users.id'), nullable=False)

    sender = relationship('User', foreign_keys=[
                          sender_id])
    recipient = relationship("User", foreign_keys=[
                             recipient_id])

    def __repr__(self) -> str:
        return f'<Friend request_id={self.id} >'
