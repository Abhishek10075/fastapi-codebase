import time
import asyncio
from fastapi import FastAPI
app=    FastAPI()
@app.get("/")
async def home():
    await asyncio.sleep(5)
    return{
        'message': 'Async Programming is successful'
    }