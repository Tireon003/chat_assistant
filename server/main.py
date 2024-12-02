from fastapi import FastAPI
import logging

from server.config import settings
from server.src.containers import SwarmContainer
from server.src.routers import messages_router


logging.basicConfig(level=settings.LOG_LEVEL)

# swarm_container = SwarmContainer()
# swarm_container.wire(packages=[__name__])

app = FastAPI(
    title="Basic AI Assistant Network API",
    version="1.0.0",
    redoc_url=None,
)

# app.container = swarm_container

app.include_router(messages_router)
