from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends

from server.src.containers import SwarmContainer
from server.src.depends import get_swarm_service
from server.src.schemas import AssistantResponse, ClientRequest
from server.src.services import SwarmService

router = APIRouter(
    tags=["Messages Router"],
    prefix="/api/v1/messages",
)


@router.post(
    path="/",
    response_model=AssistantResponse,
    status_code=200,
    description="Send a message to the assistant and returns response from LLM",
)
# @inject
async def send_message_to_assistant(
    request: Annotated[ClientRequest, Body()],
    service: Annotated[SwarmService, Depends(get_swarm_service)],
    # service: Annotated[SwarmService, Depends(Provide[SwarmContainer.service])],
) -> AssistantResponse:
    response = service.request(request)
    return response
