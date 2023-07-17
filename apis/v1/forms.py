from typing import List
from typing import Optional

from fastapi import Request

class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.fullname: Optional[str] = None
        self.phone: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        self.picture: Optional[bytearray] = None
 
    async def load_data(self):
        form = await self.request.form()
        self.fullname = form.get("fullname")
        self.phone = form.get("phone")
        self.email = form.get("email")
        self.password = form.get("password")
        self.picture = form.get("picture")

    async def is_valid(self):
        if not self.fullname or not len(self.fullname) > 2:
            self.errors.append("Full Name should be > 2 chars")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email is not in the correct format")
        if not self.phone or not (self.phone.isdigit()) :
            self.errors.append("Phone number is not in the correct format")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.errors:
            return True
        return False