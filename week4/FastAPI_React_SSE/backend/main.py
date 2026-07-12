from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from datetime import datetime
import asyncio

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def clock_stream():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        yield f"data:{current_time}\n\n"
        await asyncio.sleep(1)

@app.get("/clock")
async def clock():
    return StreamingResponse(
        clock_stream(),
        media_type="text/event-stream"
    )