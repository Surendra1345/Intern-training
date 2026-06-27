from fastapi import FastAPI,WebSocket,WebSocketDisconnect
import asyncio

app=FastAPI()

clients=[]

@app.websocket('/ws')
async def chatbox(websocket:WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            message=await websocket.receive_text()
            for client in clients:
                await client.send_text(message)
    except WebSocketDisconnect:
        clients.remove(websocket)

