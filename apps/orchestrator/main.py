from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import uuid

from app.core.config import settings
from app.api.v1.api import api_router
from app.services.websocket_service import websocket_endpoint


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting AI Teacher's Lounge Orchestrator...")
    yield
    # Shutdown
    print("Shutting down AI Teacher's Lounge Orchestrator...")


app = FastAPI(
    title="AI Teacher's Lounge Orchestrator",
    description="CrewAI multi-agent lesson design orchestration",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "AI Teacher's Lounge Orchestrator is running!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.websocket("/ws/{client_id}")
async def websocket_route(websocket: WebSocket, client_id: str):
    """WebSocket endpoint for real-time updates"""
    await websocket_endpoint(websocket, client_id)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
