from dependency_injector.wiring import inject, Provide
from fastapi import Depends
import logging

from server.src.containers import SwarmContainer
from server.src.services import SwarmService

logger = logging.getLogger(__name__)


@inject
def get_swarm_service(
    swarm_instance: SwarmService = Depends(
        Provide[SwarmContainer.swarm_instance]
    ),
) -> SwarmService:
    return SwarmService(swarm_instance)
