from db.repository.users import create_new_user
from db.repository.profile import create_profile
from db.session import get_db
from fastapi import APIRouter, Depends, Request, responses, status

from fastapi.templating import Jinja2Templates
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from apis.v1.forms import UserCreateForm
from schemas.user import ProfileCreate


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})


@router.post("/register/")
async def register(request: Request, db: Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            fullname=form.fullname, email=form.email, phone=form.phone,  password=form.password
        )
        profile = ProfileCreate(
            picture=form.picture
        )
        try:
            user = create_new_user(user=user, db=db)
            key = user.user_id
            profile = create_profile(profile=profile, db=db, key = key)
            return responses.RedirectResponse(
                "/", status_code=status.HTTP_302_FOUND
            ) 
        except IntegrityError:
            return {"msg":"Duplicate phone or email"}
    return templates.TemplateResponse("users/register.html", form.__dict__)