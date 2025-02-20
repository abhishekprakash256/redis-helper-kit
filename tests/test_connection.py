"""
Test the Redis connection (mocked)
"""

import pytest
import redis_helper_kit
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_redis_client():  
    # Create a mock Redis client
    mock_client = MagicMock()
    mock_client.ping.return_value = True  # Simulate a successful ping response
    yield mock_client

@patch("redis_helper_kit.create_redis_client")  # Mock the function
def test_redis_connection(mock_create_client, mock_redis_client):
    # Mock the return value of create_redis_client to use mock_redis_client
    mock_create_client.return_value = mock_redis_client

    # Get the mocked client
    client = redis_helper_kit.create_redis_client("localhost")

    # Test if Redis client can connect and respond to ping
    assert client.ping() is True, "Redis client ping failed"
    print("Mocked Redis connection successful")
