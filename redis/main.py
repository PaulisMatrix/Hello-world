import json
from redis_client import RedisClient
from operations import Operations
import pytz
from datetime import datetime


class RedisTesting(Operations):
    def __init__(self, redis_client: RedisClient):
        super().__init__()
        self.redis_client = redis_client
        self.hash_name = "testing"

    def set(self, mapping, *args, **kwargs):
        print("**Storing the key value pairs in redis**")
        print(self.redis_client.hset(name=self.hash_name, value=mapping))

    def get(self, key, *args, **kwargs):
        print("**Getting the data stored at key**")
        data = self.redis_client.hget(name=self.hash_name, key=key)
        if not data:
            print(f"{self.hash_name} HAS EXPIRED!!!!")
        else:
            print("**YOUR DATA**: ", json.loads(data))

    def expire_at(self, when, *args, **kwargs):
        print("**Expiring the key**", resp)
        resp = self.redis_client.expireat(name=self.hash_name, when=when, nx_=True)

    def hdel(self, keys, *args, **kwargs):
        print(f"Deleting keys:{keys} mapped at hash value:{self.hash_name}")
        self.redis_client.hdel(name=self.hash_name, keys=keys)


if __name__ == "__main__":

    test = RedisTesting(redis_client=RedisClient())
    value = [
        {"ATM_NAME": "name1", "ATM_LOCATION": "loc2"},
        {"ATM_NAME": "name2", "ATM_LOCATION": "loc2"},
        {"ATM_NAME": None, "ATM_LOCATION": "loc3"},
    ]
    key = "atm_response"
    test.set({key: json.dumps(value)})
    test.get(key=key)

    # expire the key
    tzinfo = pytz.timezone("Asia/Calcutta")
    expire_at = datetime(2022, 11, 2, 15, 25, tzinfo=tzinfo)
    test.expire_at(when=expire_at)

    # check if expired or not
    test.get(key=key)

    keys = []
    keys.append(key)
    test.hdel(keys=keys)
