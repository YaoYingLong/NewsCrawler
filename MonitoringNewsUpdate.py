# -*- coding: utf-8 -*-
import json

from Config.MongoDBConf import MyMongoDB
from Config.RedisConf import RedisBase

if  __name__ == '__main__':
    mongo = MyMongoDB("localhost", 27017, "wncg", "123456", "news_data")
    redis_conn = RedisBase("192.168.19.155", 6379, 0, 62035529).use_redis
    while True:
        newsDict = (redis_conn.blpop("newsDict")[1]).decode()
        print("output newsInfo:" + newsDict)
