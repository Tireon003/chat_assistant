from pydantic import BaseModel


class AssistantResponse(BaseModel):
    message: str
