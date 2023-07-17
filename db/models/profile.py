from sqlalchemy import Column, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

from db.base_class import Base


class Profile(Base):
    id = Column(Integer, primary_key=True)
    profile_id =  Column(Integer,ForeignKey("user.user_id"))
    picture = Column(LargeBinary, nullable=True)
    user_profile = relationship("User",back_populates="profile")