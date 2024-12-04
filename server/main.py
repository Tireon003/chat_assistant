from fastapi import FastAPI
import logging

from server.config import settings
from server.src.containers import SwarmContainer
from server.src.routers import messages_router

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def init_app() -> FastAPI:
    logger.info("Initializing app")

    swarm_container = SwarmContainer()

    new_app = FastAPI(
        title="Basic AI Assistant Network API",
        version="1.0.0",
        redoc_url=None,
    )

    new_app.container = swarm_container

    new_app.include_router(messages_router)

    return new_app


app = init_app()
