from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import init_db

# importing routers for different API endpoints
from app.apis.system import router as system_router
from app.apis.events import router as events_router

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code can be added here (e.g., database connections, cache initialization)
    logger.info("Starting up the Event Analytics Platform API...")
    logger.info("Initializing database connection...")
    await init_db()
    logger.info("Database initialized successfully.")
    yield
    # Shutdown code can be added here (e.g., closing database connections, cleaning up resources)
    logger.info("Shutting down the Event Analytics Platform API...")


# Create FastAPI app with lifespan for startup and shutdown events
app = FastAPI(title="Event Analytics Platform API", version="1.0.0",
               lifespan=lifespan,
               debug=settings.DEBUG)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],  # Allow all origins (for development, restrict in production)
                   allow_methods=["*"],  # Allow all HTTP methods
                   allow_headers=["*"])  # Allow all headers

# Include the system router for health checks and API info
logger.info("Registering system API routes...")
app.include_router(system_router)
app.include_router(events_router)
logger.info("System API routes registered successfully.")


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the Event Analytics Platform API server on http://localhost:8000")
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info")