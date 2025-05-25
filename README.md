# Redis Helper Kit

`redis_helper_kit` is a Python package that provides a convenient helper class for performing CRUD (Create, Read, Update, Delete) operations with Redis. It simplifies interactions with Redis by offering straightforward methods to manage Redis hashes, sets, and other data structures.

## Features

- Connect to a Redis instance with customizable settings.
- Perform CRUD operations on Redis sets and hashes.
- Store and retrieve JSON data in Redis hashes.
- Delete and manage Redis databases and data structures with ease.

## Installation

To install `redis_helper_kit`, clone this repository and then run:

```
git clone git@github.com:abhishekprakash256/redis-helper-kit.git
cd redis-helper-kit
pip install -r requirements.txt

#installing through pip as a package , standard appraoch , after github auth done
pip install git+https://github.com/abhishekprakash256/redis-helper-kit.git  
```

## Usage


### Running Redis 

The redis can be run either bare metal or using a docker container, preferred docker container approach 

```bash
docker pull redis

docker run -d --name redis --network my_network -p 6379:6379 redis:latest

```

### Running the usage file

After running the docker container or bare metal redis from root dir just above examples

```bash
python3 -m examples.basic_usage

```

### 1. Initial Setup

To use the helper functions, first import and initialize the `Helper_fun` class:

```python
from redis_helper_kit import Helper_fun

# Initialize Helper_fun with hash name, set name, and Redis host
redis_helper = Helper_fun(hash_name="my_hash", set_name="my_set", host_name="localhost")
```

### 2. Example CRUD Operations

#### Add a Value to a Redis Set

# Add a value to the default set
redis_helper.add_value_to_set("example_value")

# OR to a custom set
redis_helper.add_value_to_set("another_value", set_name="custom_set")

# Add a key-value pair to the default hash
redis_helper.add_value_to_hash("key1", "value1")

# OR to a custom hash
redis_helper.add_value_to_hash("key2", "value2", hash_name="custom_hash")


# Get value for a key in the default hash
value = redis_helper.get_hash_value("key1")
print(value)  # Output: value1


# Check if value exists in set
exists = redis_helper.check_set_exist("example_value")

# Check if key exists in hash
exists = redis_helper.check_hash_exist("key1")


# Iterate through all values in the default set
for item in redis_helper.get_all_set_val():
    print(item)

# OR use a specific set name
for item in redis_helper.get_all_set_val(set_name="custom_set"):
    print(item)


# Iterate through all key-value pairs in the default hash
for entry in redis_helper.get_all_hash_val():
    print(entry)

# OR for a specific hash name
for entry in redis_helper.get_all_hash_val(hash_name="custom_hash"):
    print(entry)


# Pop and return a random value from the set
popped_value = redis_helper.pop_set_val()
print(popped_value)


#### Delete a Database

```python
# Delete a database or data structure by name
redis_helper.delete_db("my_hash")
```

#### Retrieve All Values from a Redis Set

```python
# Get all values from the set
redis_helper.get_all_set_val()
```

#### Store and Retrieve JSON Data



## Configuration

The `Helper_fun` class allows you to specify custom names for your Redis hash and set, as well as the hostname for your Redis instance. By default, it connects to `localhost`, but you can pass any hostname where your Redis server is running.

## Running Tests

To test the package, ensure you have a running Redis instance (or use a mock client if needed), then run:

```bash
pytest tests/
```

This will execute all test cases in the `tests` directory to verify the CRUD operations work as expected.

## Note

- use host as "localhost" when using not as under the docker container
- use host as "redis' when using as under the docker container 

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, please reach out at [abhishekprakash47@gmail.com].





### Explanation of the Sections

1. **Features**: Lists the main functions of the package.
2. **Installation**: Instructions for installing the package locally or via PyPI.
3. **Usage**: Code snippets show how to use each CRUD method.
4. **Configuration**: Provides details on how to customize the connection settings.
5. **Running Tests**: Outlines how to run tests to ensure everything works.
6. **Contributing**: Invites others to contribute to the package.
7. **License**: Describes the license (MIT here, but adjust as needed).