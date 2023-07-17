from fastapi import APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.user import ShowUser
from db.session import get_db
from db.repository.users import retreive_user

router=APIRouter()

@router.get("/get/{user_id}",response_model=ShowUser)
def Show_user_by_user_id(user_id:int,db:Session = Depends(get_db)):
    user = retreive_user(user_id=user_id, db=db)
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with User_ID = {user_id} does not exist")
    return user