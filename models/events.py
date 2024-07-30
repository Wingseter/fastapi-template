from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        scheme_extra = {
            "title": "FastAPI Book Launch",
            "image": "https://linktomyimage.com/image.png",
            "description": "Wesill be discussing the contents of the FastAPI",
            "tags":["python", "fastapi", "book"],
            "location": "Gooogle Meet"
        }