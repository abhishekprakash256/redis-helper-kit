from redis_helper_kit.redis_crud_operations import Helper_fun
from redis_helper_kit.connection import create_redis_client

# Initialize Redis client
host_name = "localhost"  # Update to the appropriate host if necessary
redis_client = create_redis_client(host_name)

# Initialize the Helper_fun class with a hash name and set name
hash_name = "my_hash"
set_name = "my_set"
helper = Helper_fun(hash_name=hash_name, set_name=set_name, host_name=host_name)

# Basic usage examples
def basic_usage():
    print("=== Basic Usage of redis_helper_kit ===\n")

    # Example 1: Add values to a set
    print("Adding values to set...")
    helper.add_value_to_set("value1")
    helper.add_value_to_set("value2")
    print("Current values in set:", helper.get_all_set_val())

    # Example 2: Pop a value from the set
    print("\nPopping a value from set...")
    popped_value = helper.pop_set_val()
    print("Popped value:", popped_value)
    print("Remaining values in set:", helper.get_all_set_val())

    # Example 3: Add key-value pairs to a hash
    print("\nAdding key-value pairs to hash...")
    helper.add_value_to_hash("key1", "value1")
    helper.add_value_to_hash("key2", "value2")
    print("All key-value pairs in hash:", helper.get_all_hash_val())

    # Example 4: Retrieve a specific value from hash by key
    print("\nRetrieving value from hash by key...")
    value = helper.get_hash_value("key1")
    print("Retrieved value for 'key1':", value)

    # Example 5: Update value in hash
    print("\nUpdating value in hash...")
    helper.store_hash_val({"key1": "updated_value1"})
    updated_value = helper.get_hash_value("key1")
    print("Updated value for 'key1':", updated_value)

    # Example 6: Delete key from hash
    print("\nDeleting key from hash...")
    helper.delete_hash_val("key2")
    print("All key-value pairs in hash after deletion:", helper.get_all_hash_val())

    # Example 7: Check if a key exists in hash
    print("\nChecking if 'key1' exists in hash...")
    exists = helper.check_hash_exist("key1")
    print(f"Does 'key1' exist? {'Yes' if exists else 'No'}")

    # Clean up: Delete the hash and set from Redis
    print("\nCleaning up the Redis database...")
    helper.delete_db(hash_name)
    helper.delete_db(set_name)
    print("Cleanup complete.")

if __name__ == "__main__":
    basic_usage()
