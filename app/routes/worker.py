from fastapi import APIRouter, HTTPException
from typing import List
import random
import time
from app.services.redis_service import redis_client
import asyncio

router = APIRouter()

@router.get("/start/")
async def start_order():
    # Get the oldest order from Redis
    status = redis_client.get("status")
    if status == b"pending":
        redis_client.set("status", "in_progress")
        brew_time = random.randint(30, 60)
        await asyncio.sleep(brew_time)
        redis_client.set("status", "ready")
        return {"message": "Order started", "order_id": 1}
    elif status == b"in_progress":
        raise HTTPException(status_code=409, detail="Order already in progress")
    elif status == b"ready":
        raise HTTPException(status_code=409, detail="Order already ready")
    else:
        return {"message": "No orders in queue"}

@router.post("/finish/")
async def finish_order(order_id: int):
    # Mark the order as ready in redis_client
    status = redis_client.get("status")
    if status == b"in_progress":
        redis_client.set("status", "ready")
        return {"message": "Order finished", "order_id": order_id}
    elif status == b"ready":
        raise HTTPException(status_code=409, detail="Order already ready")
    else:
        raise HTTPException(status_code=404, detail="Order not found")
