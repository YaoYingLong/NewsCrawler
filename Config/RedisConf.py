# -*- coding:utf-8 -*-

import redis


class RedisBase(object):
    def __init__(self, host, port, db, password):
        self.use_redis = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password
        )

if __name__ == '__main__':
    redis = RedisBase("192.168.19.155", 6379, 0, 62035529).use_redis

    print(redis.ping())
    print(redis.info())
    # for i in range(20):
    #     redis.rpush("url" , i)

    # urlk = redis.blpop("url")[1]
    # print(urlk)
    # print(dict(urlk).get("url"))

    # for i in range(20):
    #     print(redis.blpop("url"))







