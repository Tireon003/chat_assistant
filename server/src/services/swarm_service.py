from swarm import Swarm, Agent
from openai import OpenAI
import logging
from dependency_injector.wiring import inject, Provide

from server.config import settings
from server.src.schemas import ClientRequest, AssistantResponse
from server.src.prompts import (
    AGENT_FITNESS_COACH_PROMPT,
    AGENT_TRIAGE_PROMPT,
    AGENT_CAR_MECHANIC_PROMPT,
)


logger = logging.getLogger(__name__)

agent_triage = Agent(
    model=settings.OPENAI_MODEL_NAME,
    name="Агент Сортировщик",
    instructions=AGENT_TRIAGE_PROMPT,
)

agent_car_mechanic = Agent(
    model=settings.OPENAI_MODEL_NAME,
    name="Агент Автомеханик",
    instructions=AGENT_CAR_MECHANIC_PROMPT,
)

agent_fitness_coach = Agent(
    model=settings.OPENAI_MODEL_NAME,
    name="Агент Фитнес Тренер",
    instructions=AGENT_FITNESS_COACH_PROMPT,
)


def transfer_to_agent_triage(*args, **kwargs) -> Agent:
    """Функция передает управление агенту Сортировщик"""
    return agent_triage


def transfer_to_agent_mechanic(*args, **kwargs) -> Agent:
    """Функция передает вопрос агенту Механик."""
    return agent_car_mechanic


def transfer_to_agent_fitness_coach(*args, **kwargs) -> Agent:
    """Функция передает вопрос агенту Фитнес тренер."""
    return agent_fitness_coach


agent_car_mechanic.functions.extend(
    [
        transfer_to_agent_fitness_coach,
        transfer_to_agent_triage,
    ]
)

agent_fitness_coach.functions.extend(
    [
        transfer_to_agent_mechanic,
        transfer_to_agent_triage,
    ]
)

agent_triage.functions.extend(
    [
        transfer_to_agent_mechanic,
        transfer_to_agent_fitness_coach,
    ]
)


class SwarmService:
    """Сервис для взаиммодействия с сетью агентов"""

    # @inject
    def __init__(
        self,
        # client: Swarm,
    ) -> None:
        self._client = Swarm(  # fixme do inject instead of hardcode
            OpenAI(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL,
            )
        )
        # self._client = client
        self.agent = agent_triage  # fixme do inject instead of hardcode

    def request(self, request: ClientRequest) -> AssistantResponse:
        logger.info(
            "Received request. Message: %s",
            request.message[:40] + "...",
        )
        try:
            response = self._client.run(
                messages=[
                    dict(
                        role="user",
                        content=request.message,
                    )
                ],
                agent=self.agent,
                debug=True,
            )
            return AssistantResponse(message=response.messages[-1]["content"])
        except Exception as e:
            logger.error(
                "Error during request response generation: %s",
                f"{e}",
            )
            return AssistantResponse(
                message="Запрос не обработан в связи с проблемами на сервере!"
            )
