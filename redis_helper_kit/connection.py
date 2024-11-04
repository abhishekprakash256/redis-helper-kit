"""
The redis helper function to add the connection and methods to add the data 
"""

#imports 
import redis


def create_redis_client(host_name):
    """
    The function to create the redis client 
    """

    try:
        # Try connecting to MongoDB using the current host
        client = redis.Redis(host_name, port=6379, db=0, decode_responses=True)  # 2-second timeout
        client.ping()  # This forces a connection attempt.
        print(f"Redis client created successfully using host: {host_name}")
        return client
    
    except Exception as e:
        print(f"Failed to connect to Redis using host {host_name}: {e}")
    
    # If neither host works, raise an exception or return None
    print("Failed to create Redis client with all host options.")
    
    return None


redis_client = create_redis_client()



