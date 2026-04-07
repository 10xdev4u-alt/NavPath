import asyncio
import websockets

async def handler(websocket):
    await websocket.send("Connected to NavPath")
