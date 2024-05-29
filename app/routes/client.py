from fastapi import APIRouter, HTTPException
import asyncio
import os
from app.services.redis_service import redis_client

router = APIRouter()
order_counter = 0

# Load timeout from environment file
TIMEOUT = int(os.getenv("ORDER_TIMEOUT", 120))

@router.post("/order/")
async def place_order():
    global order_counter
    order_counter += 1
    redis_client.set("status", "pending")
    print(f"Order status: {redis_client.get('status')}")

    start_time = asyncio.get_event_loop().time()
    while redis_client.get("status") != b"ready":
        if asyncio.get_event_loop().time() - start_time > TIMEOUT:
            redis_client.set("status", "failed")
            raise HTTPException(status_code=408, detail="Order timed out")
        await asyncio.sleep(1)

    if redis_client.get("status") == b"ready":
        return {"message": "Your americano is ready!", "order_id": order_counter}
    else:
        raise HTTPException(status_code=500, detail="Order failed")
