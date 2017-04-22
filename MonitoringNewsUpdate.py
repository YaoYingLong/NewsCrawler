# -*- coding: utf-8 -*-
import json

from Config.InitConfig import InitConfig
from Config.MongoDBConf import MyMongoDB
from Config.RedisConf import RedisBase

if  __name__ == '__main__':

    initConf = InitConfig("ServerConfig.ini")
    dataBaseConnectConfig = initConf.getAllNodeItems("DataBase");
    dataBaseConnectConfig["port"] = int(dataBaseConnectConfig.get("port"))
    redisConnectConfig = initConf.getAllNodeItems("Redis");

    mongo = MyMongoDB(**dataBaseConnectConfig)
    redis_conn = RedisBase(**redisConnectConfig).use_redis

    while True:
        try:
            newsDict = eval((redis_conn.blpop("NewsDict")[1]).decode())
            mongo.db_conn["NewsDetails"].insert_one(newsDict)
            print("output newsInfo:" + str(newsDict))
        except Exception as e:
            print("Have a exception:", e)
