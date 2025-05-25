"""
Test the redis crud operations using redis flush 
"""
import pytest
import json
from redis_helper_kit import Helper_fun
from redis import Redis
import fakeredis


@pytest.fixture
def redis_client():
    # Create a FakeRedis client
    return fakeredis.FakeRedis()

# Fixture for Helper_fun with setup
@pytest.fixture
def redis_helper(redis_client):
    # Flush the Redis database before each test
    redis_client.flushdb()
    # Create instance of Helper_fun with FakeRedis client instead of a real Redis connection
    return Helper_fun(default_hash_name = "test_hash", default_set_name = "test_set", host_name="localhost", redis_client=redis_client)


def test_add_value_to_set(redis_helper):
    redis_helper.add_value_to_set("test_value")
    assert redis_helper.redis_client.sismember("test_set", "test_value"), "Value not added to set."

def test_pop_set_val(redis_helper):
    redis_helper.add_value_to_set("test_value")
    popped_value = redis_helper.pop_set_val()
    assert popped_value == "test_value", "Popped value does not match expected value."
    assert not redis_helper.redis_client.sismember("test_set", "test_value"), "Value still exists in set after pop."


def test_delete_db(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    redis_helper.delete_db("test_hash")
    assert not redis_helper.redis_client.exists("test_hash"), "Hash not deleted."


def test_get_hash_value(redis_helper):   
    redis_helper.add_value_to_hash("test_key", "test_value")

    assert redis_helper.get_hash_value("test_key") == "test_value", "Incorrect value retrieved from hash."  #the output comces decoded

def test_check_hash_exist(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    assert redis_helper.check_hash_exist("test_key"), "Hash key does not exist when it should."

def test_get_all_set_val(redis_helper):
    # Add values to the Redis set
    redis_helper.add_value_to_set("value1")
    redis_helper.add_value_to_set("value2")

    # Collect all values yielded by the method
    results = list(redis_helper.get_all_set_val())

    # Convert bytes to strings if needed (depending on Redis config)
    decoded_results = [val.decode() if isinstance(val, bytes) else val for val in results]

    # Check that the values are in the set
    assert "value1" in decoded_results
    assert "value2" in decoded_results


def test_get_all_hash_val(redis_helper):
    redis_helper.add_value_to_hash("key1", "value1")
    redis_helper.add_value_to_hash("key2", "value2")

    output = list(redis_helper.get_all_hash_val())

    assert "key1: value1" in output
    assert "key2: value2" in output


def test_delete_hash_val(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    result = redis_helper.delete_hash_val("test_key")
    assert result == True
    assert not redis_helper.redis_client.hexists("test_hash", "test_key"), "Hash key still exists after deletion."
