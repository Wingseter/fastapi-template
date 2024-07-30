from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model = List[Event])
async def retrive_all_evnets() -> List[Event]:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/new")
async def create_event(body:Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) ->dict:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
