from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.routers import register_routers

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title='Fast Api project',
        lifespan=lifespan
    )
    register_routers(app)
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f'Application startup!')
    yield
    logger.info(f'Application shutdown!')