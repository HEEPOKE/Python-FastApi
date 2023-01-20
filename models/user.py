from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from config.db import Base
import enum


class Role(str, enum.Enum):
    admin = "admin"
    user = "user"


class users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), index=True)
    password = Column(String(255), index=True)
    role = Column(Enum(Role), default=Role.user, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
