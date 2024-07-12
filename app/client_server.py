from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import threading
import requests
import time
import random
import logging

app = FastAPI()

@app.post("/order/")
async def order():
    try:
        threading.Thread(target=process_order, args=()).start()
    except Exception as e:
        logging.error(f"Error starting order processing: {e}")
        raise HTTPException(status_code=500, detail="Failed to process order")
    return {"message": "Order received"}

def process_order():
    try:
        # Send start request to worker server
        response = requests.get("http://localhost:8001/start/")
        if response.status_code == 200:
            # Simulate the order processing time
            logging.info("Order processing started")
            time.sleep(random.randint(30, 60))

            # Send finish request to worker server
            requests.post("http://localhost:8001/finish/")
            logging.info("Order processing completed")
        else:
            logging.error(f"Failed to start order: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Error processing order: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during order processing: {e}")
