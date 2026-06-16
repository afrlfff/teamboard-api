from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=1)
    completed: bool = False