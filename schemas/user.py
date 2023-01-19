from pydantic import BaseModel, EmailStr
from typing import Optional
from models.index import Role



class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    password: str
    role: Optional[Role] = None