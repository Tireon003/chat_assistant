from dependency_injector.wiring import inject, Provide

from server.src.containers import SwarmContainer
from server.src.services import SwarmService


# @inject
def get_swarm_service(
    # client: Swarm = Provide[SwarmContainer.swarm_instance],
) -> SwarmService:
    # return SwarmService(client=client)
    return SwarmService()


# @inject
# def get_swarm_service():
#     ...
#     # return SwarmService(client=client)
