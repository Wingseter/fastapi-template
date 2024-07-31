from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example" : {
                "email": "email@gmail.com",
                "username": "strong",
                "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        scheme_extra = {
            "example": {
                "email": "email@gmail.com",
                "password": "strong",
                "events" : [],
            }
        }

