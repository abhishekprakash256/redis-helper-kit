# Design Document for `redis_helper_kit`

## Project Overview

The `redis_helper_kit` is a Python package developed to simplify CRUD operations in Redis databases. The package aims to streamline working with Redis data structures such as sets and hashes, allowing easy storage, retrieval, and management of data. It’s particularly helpful for applications that require quick caching or need to manage data in a distributed key-value store.

## Objectives

- **Simplify Redis Interactions**: Provide easy-to-use CRUD methods for Redis sets and hashes.
- **Increase Portability**: Create a flexible helper class that allows easy setup and teardown of Redis connections and data.
- **Ensure Reliability**: Include comprehensive error handling to ensure stability.
- **Promote Code Reusability**: Facilitate usage of Redis across different components in multi-container applications.
- **Testability**: Ensure that the package can be easily tested with mock Redis clients.

## System Architecture

The architecture is modular and consists of a main helper class (`Helper_fun`) which interacts with Redis through the Redis client. It’s designed to be flexible and portable, supporting integration in various environments, such as local testing, production containers, or multi-container Docker setups.

### Component Overview

1. **Connection Layer**: Manages Redis connections by initializing a Redis client and setting a host.
2. **Helper Class**: Provides CRUD functions for interacting with Redis sets and hashes.
3. **Testing Suite**: Contains unit tests using `pytest` and `mongomock` for verifying CRUD operations.

## Functional Requirements

1. **CRUD Operations on Redis Sets**:
   - Add, retrieve, delete, and pop elements.
   - Check if elements exist within a set.
   
2. **CRUD Operations on Redis Hashes**:
   - Add, retrieve, delete, and update key-value pairs.
   - Store complex data structures in JSON format.

3. **Connection Management**:
   - Allow connections to a Redis instance specified by the hostname.
   - Provide error handling if a connection fails.

4. **Data Cleanup**:
   - Remove databases or collections when required.

## Non-functional Requirements

1. **Portability**: The package should work across different Redis setups (local, Docker).
2. **Reliability**: Implement retry mechanisms to handle intermittent connectivity issues.
3. **Usability**: The interface should be simple to use, with clear method names and parameter requirements.
4. **Testability**: Enable testing with mock Redis instances.

## Design

### Class Diagram

#### Helper_fun

```plaintext
+---------------------------+
|       Helper_fun          |
+---------------------------+
| - hash_name: str          |
| - set_name: str           |
| - redis_client: Redis     |
+---------------------------+
| + __init__()              |
| + add_value_to_set()      |
| + add_value_to_hash()     |
| + delete_db()             |
| + pop_set_val()           |
| + get_hash_value()        |
| + check_hash_exist()      |
| + get_all_set_val()       |
| + get_all_hash_val()      |
| + store_hash_val()        |
| + store_list_hash_val()   |
| + get_users_value_from_hash() |
| + delete_hash_val()       |
+---------------------------+
```

### Component Descriptions

#### 1. Connection Component (`connection.py`)

Responsible for creating and managing Redis connections. A single function, `create_redis_client`, is defined to return a Redis client instance connected to the specified host.

- **Function**: `create_redis_client(host_name: str) -> Redis`
  - **Description**: Establishes a connection to a Redis server on the provided host.
  - **Returns**: Redis client object.

#### 2. Helper Class (`Helper_fun` in `redis_helper.py`)

The main class that provides an abstraction layer over Redis operations. It requires:
- **Constructor**: `Helper_fun(hash_name: str, set_name: str, host_name: str)`
  - Initializes with a hash name, set name, and Redis client.

#### CRUD Methods for Sets and Hashes

1. **add_value_to_set(value)**: Adds an element to a Redis set.
2. **add_value_to_hash(key, value)**: Adds a key-value pair to a Redis hash.
3. **delete_db(db_name)**: Deletes a Redis database or data structure if it exists.
4. **pop_set_val()**: Removes and returns a random element from the Redis set.
5. **get_hash_value(hash_val)**: Retrieves a specific value from the Redis hash by key.
6. **check_hash_exist(hash_val)**: Checks if a key exists within the hash.
7. **get_all_set_val()**: Retrieves all elements in a Redis set.
8. **get_all_hash_val()**: Retrieves all key-value pairs in a Redis hash.
9. **store_hash_val(hash_map)**: Stores a dictionary of values in Redis as a hash.
10. **store_list_hash_val(key, value)**: Stores a JSON list in Redis as a hash value.
11. **get_users_value_from_hash(key)**: Retrieves a JSON list stored in a Redis hash.
12. **delete_hash_val(key)**: Deletes a specific key from the Redis hash.

## Error Handling

- Redis operations may raise exceptions if the Redis server is unavailable. Each function should include try-except blocks to catch and log errors without terminating the program.
- `ConnectionError`: Raised when Redis cannot establish a connection. The `create_redis_client` method can attempt reconnections or provide a clear error message to guide debugging.

## Dependencies

### Python Packages

- `redis`: To connect and interact with Redis.
- `json`: For serializing complex data structures.
- `pytest`: For unit testing.
- `mongomock`: For testing Redis CRUD functions with mock objects.
  
### External Dependencies

- **Redis Server**: Redis must be running on the specified hostname for the package to function. This can be either a local Redis server or one hosted in Docker.

## Testing Strategy

1. **Unit Tests**:
   - Test each CRUD operation independently.
   - Use fixtures to initialize Redis client and helper classes with mock data.
   
2. **Integration Tests**:
   - Test interactions between methods, such as adding and then retrieving/deleting values.

3. **Mocking Redis with `mongomock`**:
   - Use `mongomock` for simulating Redis CRUD operations in memory, ensuring tests do not rely on an active Redis server.

### Sample Test Cases

1. **Test Set Operations**:
   - `test_add_value_to_set`: Verifies that values are correctly added.
   - `test_pop_set_val`: Verifies that elements are popped correctly.

2. **Test Hash Operations**:
   - `test_add_value_to_hash`: Checks that a key-value pair is stored in the hash.
   - `test_get_hash_value`: Confirms correct retrieval of stored values.
   
3. **Test Error Handling**:
   - Simulate connectivity issues to ensure proper exception handling.

### Sample Code for Testing

```python
@pytest.fixture
def redis_helper():
    return Helper_fun(hash_name="test_hash", set_name="test_set", host_name="localhost")

def test_add_value_to_set(redis_helper):
    redis_helper.add_value_to_set("test_value")
    assert redis_helper.check_set_exist("test_value") is True

def test_get_hash_value(redis_helper):
    redis_helper.add_value_to_hash("test_key", "test_value")
    assert redis_helper.get_hash_value("test_key") == "test_value"
```

## Future Enhancements

1. **Support for Other Data Structures**: Extend support to Redis lists, sorted sets, and streams.
2. **Redis Cluster Support**: Add connection pooling and support for Redis cluster setups.
3. **Enhanced Error Logging**: Use a logging library for better tracking of connection and CRUD operation issues.
4. **Retry Logic**: Implement retry logic for operations, especially for network-related errors.
5. **Custom Serialization**: Provide support for custom serializers to handle non-JSON serializable objects.

## Conclusion

This design document provides a detailed overview of the `redis_helper_kit` package, covering its objectives, system architecture, class design, and testing strategy. By following this design, the package will be reliable, testable, and ready for integration into larger applications that use Redis for data caching and storage.