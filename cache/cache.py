import redis
import requests as r
import mysql.connector
from mysql.connector import pooling

class ConnectionManager:
    def __init__(self):
        self.redis_cache = None
        self.mysql_pool = None
        self._initialize_connections()
    
    def _initialize_connections(self):
        # Redis Connection
        try:
            self.redis_cache = redis.Redis(
                host='localhost', 
                port=6379, 
                db=0, 
                decode_responses=True,
                socket_connect_timeout=5,
                socket_keepalive=True
            )
            self.redis_cache.ping()
            print("Redis Connection Successful")
        except Exception as e:
            print(f"Redis Connection Failed: {e}")
        
        # MySQL Connection
        try:
            self.mysql_pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                host="localhost",
                user="root",
                password="",
                database="your_database_name"
            )
            print("MySQL Pool Created Successfully")
        except Exception as e:
            print(f"MySQL Pool Creation Failed: {e}")
        
        # Debian Connection
        try:
            response = r.get("http://localhost:5000", timeout=5)
            self.debian_service_available = response.status_code == 200
            print(f"Debian service ping successful: {response.status_code}")
        except Exception as e:
            print(f"Debian service connection failed: {e}")
            self.debian_service_available = False
    
    def get_mysql_connection(self):
        if not self.mysql_pool:
            raise Exception("MySQL pool not available")
        return self.mysql_pool.get_connection()
    

conn_manager = ConnectionManager()

# Get user ID
def get_user_id(email):
    if not conn_manager.redis_cache or not conn_manager.mysql_pool:
        raise Exception("Required connections not available")
    
    cache_key = f"user_id:{email}"
    user_id = conn_manager.redis_cache.get(cache_key)
    
    if user_id:
        print(f"User ID {user_id} found in cache")
        return user_id
    
    connection = conn_manager.get_mysql_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        
        if result:
            user_id = str(result[0])
            conn_manager.redis_cache.setex(cache_key, 3600, user_id)
            print(f"User ID {user_id} found in database and cached")
            return user_id
        else:
            raise Exception("User not found")
    finally:
        cursor.close()
        connection.close()

# Caching
class Cache:
    def __init__(self):
        self.redis_cache = conn_manager.redis_cache
    
    def cache(self, key, value, ttl=86400):
        if not self.redis_cache:
            print("Redis connection not available")
            return None
        
        cached_value = self.redis_cache.get(key)
        if cached_value is None:
            self.redis_cache.setex(key, ttl, value)
            print("Caching!")
            return None
        else:
            print("Cached!")
            return cached_value


'''
Here is the caching format:
-----------------------------

cache(key, value/data)

What the cache can be used for:
-------------------------
- Web page loading
- Retrive frequent data from database (mysql)
- Keep hold of AI reponses like human memory
'''