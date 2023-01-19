from pydantic import BaseModel
from typing import Optional
from models.index import Role



class User(BaseModel):
    # id: Optional[int] = None
    username: str
    email: str
    password: str
    role: Optional[Role] = None