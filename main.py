from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.post("/hack")
async def hack(target: str):
    print(target)
    return {"message": f"Received: {target}"}