# -*- coding:utf-8 -*-

import redis

from Config.InitConfig import InitConfig


class RedisBase(object):

    # def __init__(self):
    #     self.conf = InitConfig("ServerConfig.ini")
    #     self.use_redis = redis.StrictRedis(
    #         host=self.conf.getValue("Redis", "host"),
    #         port=self.conf.getValue("Redis", "port"),
    #         db=self.conf.getValue("Redis", "db"),
    #         password=self.conf.getValue("Redis", "password")
    #     )

    def __init__(self, host, port, db, password):
        self.use_redis = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password
        )

if __name__ == '__main__':
    redis = RedisBase().use_redis

    print(redis.ping())
    print(redis.info())
    # for i in range(20):
    #     redis.rpush("url" , i)
    #
    # urlk = redis.blpop("url")[1]
    # print(urlk)
    # print(dict(urlk).get("url"))
    #
    # for i in range(20):
    #     print(redis.blpop("url"))







