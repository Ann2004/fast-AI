import asyncio
from itertools import count

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_data():
    return "<h1>Hello World!</h1>"


@app.get("/info")
async def get_info():
    return {"company_name": "Horns and Hooves", "company_address": "Pushkin street, 12"}


@app.get("/counter")
async def number_stream():
    async def generate_numbers():
        counter = count(start=0, step=1)
        while True:
            yield str(next(counter))
            await asyncio.sleep(0.5)

    return StreamingResponse(generate_numbers(), media_type="text/html")
