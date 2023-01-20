from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from models.index import Role
from datetime import datetime


class BaseUser(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr
    password: str
    role: Optional[Role] = Field(None)
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ResponseUser(BaseUser):
    status: str
    date: List[BaseUser]


class RequestUser(BaseUser):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = Field(None)

