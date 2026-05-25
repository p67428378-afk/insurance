
from fastapi import APIRouter
from server.app.api.v1.endpoints import premium

api_router = APIRouter()
api_router.include_router(premium.router, prefix="/premiums", tags=["premiums"])
