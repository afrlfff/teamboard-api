from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=1)
    completed: bool = False

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        title = value.strip()

        if not title:
            raise ValueError("Task title must not be empty")

        return title