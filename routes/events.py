from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from models.events import Event, EventUpdate

from database.connection import Database
from beanie import PydanticObjectId

from auth.authenticate import authenticate

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model = List[Event])
async def retrive_all_evnets(session = Depends(get_session)) -> List[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event

@event_router.post("/new")
async def create_event(new_event: Event, 
                       user: str = Depends(authenticate)) -> dict:
    await event_database.save(body)
    
    return {
        "message": "Event created successfully"
    }

@event_router.delete("{id}")
async def delete_event(id: PydanticObjectId) ->dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message" : "Event deleted successfully"
    }

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message" : "Event deleted successfully"
    }

@event_router.put("/{id}", response_model = Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user : str = Depends(authenticate)) ->dict:
    updated_event = await event_database.update(id, body)

    if not update_event:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event
