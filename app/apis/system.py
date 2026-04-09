import logging
from fastapi import APIRouter

# System API router for health checks and system info
logger = logging.getLogger(__name__)

#create a router for system-related endpoints
router = APIRouter(tags=["System"],
                   responses={404: {"description": "Not found"},
                              500: {"description": "Internal server error"},
                              200: {"description": "Successful response"}})



@router.get("/health", 
           summary="Health Check", 
           description="Check the health status of the API")

async def health_check():
    """
    Health check endpoint to verify that the API is running.
    Returns a simple JSON response indicating the status of the API.
    """
    logger.info("Health check endpoint called")
    return {"status": "healthy",
            "version": "1.0.0",
            "service": "Event Analytics Platform API"}

@router.get("/",
            summary="API Info",
            description="Get basic information about the API",
            response_description="Basic information about the API")

async def root():
    """
    Root endpoint to provide basic information about the API.
    Returns a welcome message and some details about the API.
    """
    logger.info("Root endpoint called")
    return {"message": "Welcome to the Event Analytics Platform API!",
            "version": "1.0.0",
            "service": "Event Analytics Platform API",
            "description": "This API provides endpoints for event analytics and data processing.",
            "documentation": "/docs"
            }