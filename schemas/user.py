from pydantic import BaseModel
from models.index import Role


class User(BaseModel):
    username: str
    email: str
    password: str
    role: Role
