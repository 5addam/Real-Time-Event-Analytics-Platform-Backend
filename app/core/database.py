from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text
from typing import AsyncGenerator
from app.core.config import settings


engine = create_async_engine(str(settings.DATABASE_URL), echo=settings.DEBUG)


class Base(DeclarativeBase):
    """Base class for all database models."""
    pass

AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False)

async def init_db() -> None:
    """Initialize the database connection."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Provide a database session for dependency injection."""
    async with AsyncSessionLocal() as session:
        yield session




