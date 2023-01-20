from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from models.index import Role


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[Role] = Field(None)


class ResponseUser(BaseUser):
    id: int
    username: str
    email: EmailStr
    role: str


class RequestUser(BaseUser):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = Field(None)

    class RequestUser:
        orm_mode = True
