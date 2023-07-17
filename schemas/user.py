from pydantic import BaseModel,EmailStr, Field

class UserCreate(BaseModel):
    fullname : str = Field('name', min_length=2)
    phone : str= Field (123456, min_length=6)
    email : EmailStr
    password : str = Field('pass', min_length=4)

class ProfileCreate(BaseModel):
    picture: bytes

class ShowUser(BaseModel):
    user_id: int
    fullname : str
    email : EmailStr
    phone: str
    password : str

    class Config(): 
        orm_mode = True