# The Caffeinated Odyssey

This project implements a whimsical yet robust HTTP server for a caffeinated haven using FastAPI. The server supports three essential routes: one for clients to order their americano, and two for baristas to start and finish the coffee preparation.

## Project Structure

## Routes

- `/client/order/` (POST): Clients place their americano orders.
- `/worker/start/` (GET): Baristas start preparing the oldest order.
- `/worker/finish/` (POST): Baristas mark an order as ready.

## Setup and Running

### Prerequisites

- Docker
- Docker Compose (optional)

### Running Locally

### Install dependencies:
pip install -r requirements.txt

### Run the FastAPI server:
uvicorn app.main:app --host 0.0.0.0 --port 8000


## Running with Docker

### Build the Docker image:
docker build -t caffeinated_odyssey .

### Run the Docker container:
docker run -p 8000:8000 caffeinated_odyssey



## DDoS Protection
The nginx.conf file provides a simple solution to protect against DDoS attacks. To use this configuration:

###  1. Install Nginx:
sudo apt update
sudo apt install nginx

### 2.Copy the nginx.conf file to the Nginx configuration directory:
sudo cp ddos_protection/nginx.conf /etc/nginx/sites-available/default

### 3.Restart Nginx:
sudo systemctl restart nginx



## Notes
Ensure that the FastAPI server is running before making requests to the endpoints.
Modify the nginx.conf file as needed to fit your specific requirements.
Happy brewing! ☕️

### Summary
- The project is structured to separate concerns and keep the code organized.
- The `client.py` handles client orders, while the `worker.py` handles barista actions.
- The `nginx.conf` file provides basic DDoS protection.
- The `Dockerfile` allows for easy containerization of the application.
- The `README.md` provides clear instructions for setup and running the application.



# Run the client server
uvicorn app.main:client_app --host 0.0.0.0 --port 8000

# Run the worker server
uvicorn app.main:worker_app --host 0.0.0.0 --port 8001



