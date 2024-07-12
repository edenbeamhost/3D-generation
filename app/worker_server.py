from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

import logging

@app.get("/start/")
async def start():
    logging.info("Order started")
    return {"message": "Order started"}

@app.post("/finish/")
async def finish():
    logging.info("Order finished")
    return {"message": "Order finished"}
