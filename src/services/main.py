from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.routers import register_routers

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title='Fast Api project',
        lifespan=lifespan
    )
 
    origins = [
        "http://localhost:8080",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    register_routers(app)
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Application startup!')
    yield
    logger.info('Application shutdown!')