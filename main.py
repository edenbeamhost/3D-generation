# main.py
import uvicorn
from multiprocessing import Process

def start_client_server():
    uvicorn.run("app.client_server:app", host="0.0.0.0", port=8000, reload=True)

def start_worker_server():
    uvicorn.run("app.worker_server:app", host="0.0.0.0", port=8001, reload=True)

if __name__ == "__main__":
    client_server_process = Process(target=start_client_server)
    worker_server_process = Process(target=start_worker_server)
    
    client_server_process.start()
    worker_server_process.start()
    
    client_server_process.join()
    worker_server_process.join()