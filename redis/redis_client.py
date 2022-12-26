from dotenv import load_dotenv
import os
import redis

load_dotenv()


class RedisClient(object):
    def __init__(self):
        self.host = os.getenv("REDIS_HOST")
        self.port = os.getenv("REDIS_PORT")
        self.db = os.getenv("REDIS_DB")
        self.password = os.getenv("REDIS_PASSWORD")

        # use connection pooling
        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,
            decode_responses=True,
        )
        # max_connections is max number of connections available in a pool.
        # socket_timeout is operation timeout like client connecting to the socket or reading/writing from a socket.
        self.connection = redis.StrictRedis(
            connection_pool=pool, max_connections=10, socket_timeout=100
        )
        # set idle connections timeout to 100secs
        # so if a connection is idle for more than 240secs, close it.
        self.connection.config_set(name="timeout", value=240)

    def __str__(self) -> str:
        print("Redis settings:\n")
        return f"Redis host:{self.host}\tRedis port:{self.port}\tRedis db:{self.db}\tRedis password:{self.password}\n"

    def get(self, name):
        return self.connection.get(name)

    def set(self, name, value, exp_time=None):
        self.connection.set(name, value, exp_time)

    def hset(self, name, value):
        self.connection.hset(name, mapping=value)

    def hgetall(self, name):
        return self.connection.hgetall(name)

    def hget(self, name, key):
        return self.connection.hget(name, key)

    def hmset(self, name, mapping):
        return self.connection.hmset(name, mapping)

    def exists(self, name):
        return self.connection.exists(name)

    def ttl(self, name):
        return self.connection.ttl(name)

    def expireat(
        self,
        name,
        when,
        nx_: bool = False,
        xx_: bool = False,
        gt_: bool = False,
        lt_: bool = False,
    ):
        return self.connection.expireat(name, when)
