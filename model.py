from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: str
    item: str

class TodoItem(BaseModel):
    item: str
    
    class Config:
        schema_extra = {
            "example": {
                "item": "Example Schema"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example" : {
                "todos" : [
                    {
                        "item" : "Example schema 1"
                    },
                    {
                        "item" : "Example schema 2"
                    }
                ]
            }
        }