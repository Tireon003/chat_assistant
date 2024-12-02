from pydantic import BaseModel, Field


class ClientRequest(BaseModel):
    message: str = Field(min_length=6)
