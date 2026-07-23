"""FastAPI application entry point"""

import logging
from datetime import datetime

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.database import init_db
from app.schemas import HealthResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="Instagram Growth AI",
    description="AI-powered system to grow your Instagram account",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize application on startup"""
    logger.info("Starting Instagram Growth AI application...")
    try:
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")


@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on shutdown"""
    logger.info("Shutting down Instagram Growth AI application...")


@app.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check() -> HealthResponse:
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        database="connected",
        redis="connected",
        timestamp=datetime.utcnow(),
    )


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Instagram Growth AI API",
        "version": "0.1.0",
        "docs": "/docs",
    }


# API Router imports (to be implemented)
# from app.api import accounts, analytics, targeting, content, auth
# app.include_router(accounts.router, prefix="/api/accounts", tags=["Accounts"])
# app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
# app.include_router(targeting.router, prefix="/api/targeting", tags=["Targeting"])
# app.include_router(content.router, prefix="/api/content", tags=["Content"])
# app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )
