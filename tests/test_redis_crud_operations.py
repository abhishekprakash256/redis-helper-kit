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
    return Helper_fun(hash_name="test_hash", set_name="test_set", host_name="localhost", redis_client=redis_client)


def test_add_value_to_set(redis_helper):
    redis_helper.add_value_to_set("test_value")
    assert redis_helper.redis_client.sismember("test_set", "test_value"), "Value not added to set."


def test_delete_db(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    redis_helper.delete_db("test_hash")
    assert not redis_helper.redis_client.exists("test_hash"), "Hash not deleted."


def test_get_hash_value(redis_helper):   
    redis_helper.add_value_to_hash("test_key", "test_value")

    assert redis_helper.get_hash_value("test_key").decode('utf-8') == "test_value", "Incorrect value retrieved from hash."  #the output comces decoded

def test_check_hash_exist(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    assert redis_helper.check_hash_exist("test_key"), "Hash key does not exist when it should."

def test_get_all_set_val(redis_helper, capsys):
    redis_helper.add_value_to_set("value1")
    redis_helper.add_value_to_set("value2")
    redis_helper.get_all_set_val()
    captured = capsys.readouterr()
    assert "Values in Redis set :" in captured.out
    assert "value1" in captured.out
    assert "value2" in captured.out

def test_get_all_hash_val(redis_helper, capsys):   
    redis_helper.add_value_to_hash("key1", "value1")
    redis_helper.add_value_to_hash("key2", "value2")
    redis_helper.get_all_hash_val()
    captured = capsys.readouterr()

    # Decode the captured output to remove byte literals
    decoded_output = captured.out.replace("b'", "").replace("'", "")

    print("Captured output:", decoded_output)  

    assert "Fields and values in Redis hash" in decoded_output
    assert "key1: value1" in decoded_output  
    assert "key2: value2" in decoded_output  

def test_store_hash_val(redis_helper):
    hash_map = {}
    redis_helper.add_value_to_hash("key1", "value1") 
    redis_helper.store_hash_val(hash_map)  #the output comes coded
    assert hash_map[b"key1"] == b"value1", "Value not correctly stored in hash map."

def test_store_list_hash_val(redis_helper):
    test_list = ["user1", "user2"]
    redis_helper.store_list_hash_val("users", test_list)
    stored_value = json.loads(redis_helper.redis_client.hget("test_hash", "users"))
    assert stored_value == test_list, "List not correctly stored in hash."

def test_get_users_value_from_hash(redis_helper):
    test_list = ["user1", "user2"]
    redis_helper.store_list_hash_val("users", test_list)
    retrieved_list = redis_helper.get_users_value_from_hash("users")
    assert retrieved_list == test_list, "List not correctly retrieved from hash."

def test_delete_hash_val(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    result = redis_helper.delete_hash_val("test_key")
    assert result == "deleted succesfully", "Value not deleted from hash."
    assert not redis_helper.redis_client.hexists("test_hash", "test_key"), "Hash key still exists after deletion."
