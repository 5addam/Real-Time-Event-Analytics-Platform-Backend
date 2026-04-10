from sqlalchemy import Integer, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
import uuid
from datetime import datetime

class EventRecord(Base):
    __tablename__ = "event_record"

    id: Mapped[str] = mapped_column(Integer, primary_key=True, index=True)
    event_uuid: Mapped[str] = mapped_column(String, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    event_type: Mapped[str] = mapped_column(String, nullable=False, index=True)
    timestamp: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    properties: Mapped[dict] = mapped_column(JSON, nullable=True)
    user_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now())

    def __repr__(self):
        return f"<EventRecord(id={self.id}, event_type={self.event_type}, timestamp={self.timestamp}, user_id={self.user_id})>"
    
