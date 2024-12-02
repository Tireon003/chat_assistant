from dependency_injector import containers, providers
from openai import OpenAI
from swarm import Swarm

from server.config import settings
from server.src.services import SwarmService


class SwarmContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["server.src.routers.messages_router"]
    )
    config = providers.Configuration()

    openai_instance = providers.Singleton(
        OpenAI,
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL,
    )

    swarm_instance = providers.Factory(Swarm, client=openai_instance.provider)

    service = providers.Factory(SwarmService, client=swarm_instance)
