from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.routers import register_routers

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title='Fast Api project',
        lifespan=lifespan
    )

    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://0.0.0.0:3000",
        "http://172.17.0.2:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/static", StaticFiles(directory="static"), name="static")
    register_routers(app)
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Application startup!')
    yield
    logger.info('Application shutdown!')