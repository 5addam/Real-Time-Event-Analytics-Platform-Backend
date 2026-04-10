from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    event_type: str = Field(..., description="Type of the event (e.g., click, view, purchase)")
    timestamp: datetime = Field(..., description="Timestamp of when the event occurred")
    user_id: str = Field(description="ID of the user associated with the event")
    properties: Optional[dict] = Field(default_factory=dict, description="Additional properties of the event")
