# Created automatically by Cursor AI (2024-08-26)
import asyncio
import json
from typing import Dict, Set, Any
from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect

class WebSocketManager:
    """Manages WebSocket connections for real-time updates"""
    
    def __init__(self):
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        self.connection_data: Dict[WebSocket, Dict[str, Any]] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        """Connect a new WebSocket client"""
        await websocket.accept()
        
        if client_id not in self.active_connections:
            self.active_connections[client_id] = set()
        
        self.active_connections[client_id].add(websocket)
        self.connection_data[websocket] = {
            "client_id": client_id,
            "connected_at": datetime.now().isoformat()
        }
        
        print(f"Client {client_id} connected. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        """Disconnect a WebSocket client"""
        client_id = self.connection_data.get(websocket, {}).get("client_id")
        
        if client_id and client_id in self.active_connections:
            self.active_connections[client_id].discard(websocket)
            
            if not self.active_connections[client_id]:
                del self.active_connections[client_id]
        
        if websocket in self.connection_data:
            del self.connection_data[websocket]
        
        print(f"Client {client_id} disconnected. Total connections: {len(self.active_connections)}")
    
    async def send_personal_message(self, message: Dict[str, Any], websocket: WebSocket):
        """Send a message to a specific WebSocket client"""
        try:
            await websocket.send_text(json.dumps(message))
        except Exception as e:
            print(f"Error sending message to client: {e}")
            self.disconnect(websocket)
    
    async def broadcast_to_client(self, client_id: str, message: Dict[str, Any]):
        """Broadcast a message to all connections of a specific client"""
        if client_id in self.active_connections:
            disconnected = set()
            
            for websocket in self.active_connections[client_id]:
                try:
                    await websocket.send_text(json.dumps(message))
                except Exception as e:
                    print(f"Error broadcasting to client {client_id}: {e}")
                    disconnected.add(websocket)
            
            # Clean up disconnected websockets
            for websocket in disconnected:
                self.disconnect(websocket)
    
    async def broadcast_export_progress(self, lesson_id: str, progress_data: Dict[str, Any]):
        """Broadcast export progress updates"""
        message = {
            "type": "export_progress",
            "lesson_id": lesson_id,
            "data": progress_data,
            "timestamp": datetime.now().isoformat()
        }
        
        # Broadcast to all clients (in a real app, you'd filter by lesson_id)
        for client_id in list(self.active_connections.keys()):
            await self.broadcast_to_client(client_id, message)
    
    async def broadcast_export_complete(self, lesson_id: str, export_data: Dict[str, Any]):
        """Broadcast export completion"""
        message = {
            "type": "export_complete",
            "lesson_id": lesson_id,
            "data": export_data,
            "timestamp": datetime.now().isoformat()
        }
        
        for client_id in list(self.active_connections.keys()):
            await self.broadcast_to_client(client_id, message)

# Global WebSocket manager instance
websocket_manager = WebSocketManager()

async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """WebSocket endpoint for handling connections"""
    await websocket_manager.connect(websocket, client_id)
    
    try:
        while True:
            # Keep connection alive and handle incoming messages
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Handle different message types
            if message.get("type") == "ping":
                await websocket_manager.send_personal_message({
                    "type": "pong",
                    "timestamp": datetime.now().isoformat()
                }, websocket)
            
            elif message.get("type") == "subscribe_export":
                lesson_id = message.get("lesson_id")
                if lesson_id:
                    # Subscribe to export updates for this lesson
                    websocket_manager.connection_data[websocket]["subscribed_lessons"] = \
                        websocket_manager.connection_data[websocket].get("subscribed_lessons", set())
                    websocket_manager.connection_data[websocket]["subscribed_lessons"].add(lesson_id)
                    
                    await websocket_manager.send_personal_message({
                        "type": "subscribed",
                        "lesson_id": lesson_id,
                        "timestamp": datetime.now().isoformat()
                    }, websocket)
    
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
    except Exception as e:
        print(f"WebSocket error: {e}")
        websocket_manager.disconnect(websocket)
