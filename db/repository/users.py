from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher

def create_new_user(user:UserCreate,db:Session):
    user = User(
        fullname = user.fullname,
        email = user.email,
        phone = user.phone,
        password=Hasher.get_password_hash(user.password)
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def retreive_user(user_id:int,db:Session):
    results = db.query(User).filter(User.user_id==user_id).first()
    return results