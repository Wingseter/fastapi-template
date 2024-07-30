from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

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

