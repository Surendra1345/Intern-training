from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import StreamingResponse
import asyncio

app=FastAPI()

async def clock_stream():
    while True:
        time=datetime.now().strftime("%H:%M:%S")
        yield f"data:{time}\n\n"
        await asyncio.sleep(1)
    
@app.get('/clock')
async def  clock():
    return StreamingResponse(
    clock_stream(),
    media_type="text/event-stream"
    )