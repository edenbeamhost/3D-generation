from fastapi import FastAPI
from app.routes import client, worker

client_app = FastAPI()
worker_app = FastAPI()

# redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Include routes
client_app.include_router(client.router, prefix="/client")
worker_app.include_router(worker.router, prefix="/worker")

# Run the servers
if __name__ == "__main__":
    print("hello")
    import uvicorn
    uvicorn.run(client_app, host="0.0.0.0", port=8000)
    uvicorn.run(worker_app, host="0.0.0.0", port=8001)
