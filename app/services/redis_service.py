import redis

# Create a Redis client
redis_client = redis.Redis(host="0.0.0.0", port=6379, db=0)
