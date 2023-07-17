from fastapi import APIRouter

from apis.v1 import route_user
from apis.v1 import route_data

api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_data.router,prefix="",tags=["users_data"])