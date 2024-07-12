# The Caffeinated Odyssey

This project implements a whimsical yet robust HTTP server for a caffeinated haven using FastAPI. The server supports three essential routes: one for clients to order their americano, and two for baristas to start and finish the coffee preparation.

## Project Structure

## Routes

- `/order/` (POST): Clients place their americano orders.
- `/start/` (GET): Baristas start preparing the oldest order.
- `/finish/` (POST): Baristas mark an order as ready.

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
docker build -t caff .

### Run the Docker container:
docker run -p 8000:8000 -p 8001:8001 --network=host caff


The nginx.conf file provides a simple solution to protect against DDoS attacks. To use this configuration:

## Running Nginx separately
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
- The `nginx.conf` file provides basic DDoS protection.
- The `Dockerfile` allows for easy containerization of the application.
- The `README.md` provides clear instructions for setup and running the application.



