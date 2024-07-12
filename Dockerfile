FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Nginx configuration file
COPY ddos_protection/nginx.conf /etc/nginx/conf.d/default.conf

COPY . .

EXPOSE 8000
EXPOSE 8001
EXPOSE 80

CMD ["bash", "-c", "nginx -g 'daemon off;' & uvicorn app.client_server:app --host 0.0.0.0 --port 8000 & uvicorn app.worker_server:app --host 0.0.0.0 --port 8001 ; wait -n"]
