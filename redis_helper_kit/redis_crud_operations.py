"""
The file for making the redis crud operations
"""
import json
from .connection import create_redis_client



class Helper_fun():

    def __init__(self, hash_name, set_name, host_name, redis_client=None):
        self.hash_name = hash_name
        self.set_name = set_name
        # If no redis_client is provided, create one using the host_name
        if redis_client:
            self.redis_client = redis_client
        else:
            self.redis_client = create_redis_client(host_name)

    def add_value_to_set(self,value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = self.redis_client.sadd(self.set_name, value)

        if res: 
            print("Data added in set succesfully")
        
        else:
            print("Failed to add data in set")
    
    
    def add_value_to_hash(self, key , value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = self.redis_client.hset(self.hash_name, key, value)

        #testting the code
        #print(type(key))
        #print(type(value))

        #print(res)

        if res: 
            print("Data added in hash succesfully")
        
        else:
            print("Failed to add data in hash")

    
    def delete_db(self,db_name):
        """
        The function to delete the hash if exists 
        and then delete the hash
        """
        # check the hash exists 
        if self.redis_client.exists(db_name):
            
            #delete the hash or set 
            self.redis_client.delete(db_name)
            print("The db has been deleted succesfully")
        
        else:

            print("The db doesn't exists")

    
    def pop_set_val(self):
        """
        The funcion to pop a value from the set 
        """

        res = self.redis_client.spop(self.set_name)

        if res:
            return res
        
        else:
            return None
    
    def get_hash_value(self,hash_val):
        """
        The function to get the hash value 
        """
        res = self.redis_client.hget(self.hash_name, hash_val)
        if res:
            return res
        else:
            return "Value not found"

    def check_hash_exist(self,hash_val):
        """
        The function to check the hash value exist in the set and in the redis hash
        """

        hash_check = self.redis_client.hexists(self.hash_name, hash_val)
        
        if hash_check:
            return True 
        
        else:
            return False
    
    def get_all_set_val(self):
        """
        The function to get all the hash value 
        """

        set_members = self.redis_client.smembers(self.set_name)
        
        print("Values in Redis set :")
        
        for member in set_members:
            print(member)
            

    def get_all_hash_val(self):
        """
        The function to get all the set value 
        """

        hash_fields = self.redis_client.hgetall(self.hash_name)
        print("\nFields and values in Redis hash ")
        for field, value in hash_fields.items():
            print(f"{field}: {value}")


    def store_hash_val(self,hash_map):
        """
        The function to store all values in hash map
        """

        hash_fields = self.redis_client.hgetall(self.hash_name)
        print("Fields and values in Redis hash ")
        for field, value in hash_fields.items():
            hash_map[field] = value



    #------added the values to the redis hash --------------
     
    #the method to store the hash value in the list foramt

    def store_list_hash_val(self,key,value):
        """
        The function to store the key and value (list) in hash set
        """

        uers_json = json.dumps(value)
        self.redis_client.hset(self.hash_name,key,uers_json)   



    #the method to show the values from the chat hash 
    def get_users_value_from_hash(self,key):

        # Retrieve and deserialize the list from JSON string
        retrieved_data_str = self.redis_client.hget(self.hash_name, key)

        if retrieved_data_str:
            # Deserialize the JSON string to a Python list
            retrieved_data_list = json.loads(retrieved_data_str)
            return retrieved_data_list
        
        return "None"




    def delete_hash_val(self,key):
        """
        The method to delete the hash value from the redis hash
        """

        res = self.redis_client.hdel(self.hash_name,key)

        if res:
            return "deleted succesfully"
        else:
            return "data not found"