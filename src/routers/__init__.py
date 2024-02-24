from fastapi import APIRouter, FastAPI

from src.routers.auth import router as auth_router


def register_routers(app: FastAPI) -> None:
    router = APIRouter(prefix='/api/v1')
    router.include_router(auth_router)
    app.include_router(router)