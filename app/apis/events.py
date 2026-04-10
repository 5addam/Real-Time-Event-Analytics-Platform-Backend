from fastapi import APIRouter, Depends, HTTPException
from app.schemas.events import EventBase
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event_record import EventRecord as Event
from typing import Annotated
import uuid

# Create a router for event-related endpoints
router = APIRouter(prefix="/events", tags=["Events"],
                   responses={404: {"description": "Not found"},
                              500: {"description": "Internal server error"}})

@router.post("/", summary="Create Event", description="Create a new event with the provided data")
async def ingest_event(db: Annotated[AsyncSession, Depends(get_db)],event: EventBase):
    """
    Ingest a new event into the system.
    This endpoint accepts an event payload and processes it accordingly.
    """
    try:
        event_data = event.model_dump()
        event_data['event_uuid'] = str(uuid.uuid4())  # Generate a unique UUID for the event
        db_event = Event(**event_data)
        db.add(db_event)
        await db.commit()
        await db.refresh(db_event)  # Refresh the instance to get the generated ID and other default values
        print(f'event_data: {db_event}')


        return {"message": "Event ingested successfully", "event_id": db_event.event_uuid}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))