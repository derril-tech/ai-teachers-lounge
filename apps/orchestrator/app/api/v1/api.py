from fastapi import APIRouter

from app.api.v1.endpoints import lessons, agents, health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
