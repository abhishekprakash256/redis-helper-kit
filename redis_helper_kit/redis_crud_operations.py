"""
The file for making the redis crud operations
"""
import json
from .connection import create_redis_client



class Helper_fun:

    def __init__(self, default_hash_name=None, default_set_name=None, host_name=None, redis_client=None):
        self.default_hash_name = default_hash_name
        self.default_set_name = default_set_name
        if redis_client:
            self.redis_client = redis_client
        else:
            self.redis_client = create_redis_client(host_name)

    # ----------------- SET METHODS -----------------

    def add_value_to_set(self, value, set_name=None):
        """
        The function to add the value to the set
        """
        set_name = set_name or self.default_set_name
        res = self.redis_client.sadd(set_name, value)
        return bool(res)

    def pop_set_val(self, set_name=None):
        """
        The function to pop the value from the set
        """
        set_name = set_name or self.default_set_name
        res = self.redis_client.spop(set_name)
        if res:
            return res.decode() if isinstance(res, bytes) else res
        return None

    def get_all_set_val(self, set_name=None):
        """
        The function to get all the values from the set
        """
        set_name = set_name or self.default_set_name
        set_members = self.redis_client.smembers(set_name)
        for member in set_members:
            yield member.decode() if isinstance(member, bytes) else member

    def check_set_exist(self, value, set_name=None):
        """
        The function to check if the value exists in the set
        """
        set_name = set_name or self.default_set_name
        set_check = self.redis_client.sismember(set_name, value)
        return bool(set_check)

    def get_set_len(self, set_name=None):
        """
        The function to get the length of the set
        """
        set_name = set_name or self.default_set_name
        
        set_len = self.redis_client.scard(set_name)
        return set_len
    
    def delete_set_val(self, value, set_name=None):
        """
        The function to delete the value from the set
        """
        set_name = set_name or self.default_set_name

        res = self.redis_client.srem(set_name, value)
        return bool(res)


        # ----------------- HASH METHODS -----------------

    def add_value_to_hash(self, key, value, hash_name=None):
        """
        The function to add the value to the hash
        """
        hash_name = hash_name or self.default_hash_name
        res = self.redis_client.hset(hash_name, key, value)
        return bool(res)

    def get_hash_value(self, key, hash_name=None):
        """
        The function to get the value from the hash
        """
        hash_name = hash_name or self.default_hash_name
        res = self.redis_client.hget(hash_name, key)
        if res:
            return res.decode() if isinstance(res, bytes) else res
        return None

    def check_hash_exist(self, key, hash_name=None):
        """
        The function to check if the hash value exists
        """
        hash_name = hash_name or self.default_hash_name
        hash_check = self.redis_client.hexists(hash_name, key)
        return bool(hash_check)

    def get_all_hash_val(self, hash_name=None):
        """
        The function to get all the values from the hash
        """
        hash_name = hash_name or self.default_hash_name
        hash_fields = self.redis_client.hgetall(hash_name)
        for key, value in hash_fields.items():
            field_str = key.decode() if isinstance(key, bytes) else key
            value_str = value.decode() if isinstance(value, bytes) else value
            yield f"{field_str}: {value_str}"

    def delete_hash_val(self, key, hash_name=None):
        """
        The function to delete the hash value
        """
        hash_name = hash_name or self.default_hash_name
        res = self.redis_client.hdel(hash_name, key)
        return bool(res)


    # ----------------- DATABASE METHODS -----------------

    def delete_db(self, db_name):
        """
        The function to delete the database
        """
        if self.redis_client.exists(db_name):
            self.redis_client.delete(db_name)
            return True
        return False




    """"
    def store_hash_val(self,hash_map):
 
        hash_fields = self.redis_client.hgetall(self.hash_name)
        print("Fields and values in Redis hash ")
        for field, value in hash_fields.items():
            hash_map[field] = value

    """


