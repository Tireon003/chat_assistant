from server.src.services import SwarmService


# @inject
def get_swarm_service() -> SwarmService:
    return SwarmService()
