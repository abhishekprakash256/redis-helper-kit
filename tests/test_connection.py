"""
test the redis connection 
"""


import pytest
import redis_helper_kit 
import redis


@pytest.fixture
def redis_client():
    # Connect to the Redis server
    client = redis_helper_kit.create_redis_client("localhost")
    yield client
    client.close()

def test_redis_connection(redis_client):
    # Test if Redis client can connect and respond to ping
    try:
        response = redis_client.ping()
        assert response is True, "Redis client ping failed"
        print("Redis connection successful")
    except redis.exceptions.ConnectionError:
        pytest.fail("Redis client could not connect to the server")
