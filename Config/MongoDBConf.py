# -*- coding:utf-8 -*-
import logging
import time
import pymongo
from pymongo.errors import DuplicateKeyError

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MyMongoDB(object):
    def __init__(self, host, port, user, password, db):
        self.db_conn = None
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db
        self._mongo_login()

    def _mongo_login(self):
        client = pymongo.MongoClient(self._host, self._port)
        self.db_conn = client[self._db]
        self.db_conn.authenticate(self._user, self._password)


if __name__ == '__main__':
    mongo = MyMongoDB("localhost", 27017, "wncg", "123456", "news_data")
    try:
        res = {};
        res["_id"] = "http://3g.163.com/news/17/0219/10/CDKOF1UB0001875N_0.html"
        res["title"] = "台游览车事故致33死11伤 2名官员口头请辞负责"
        res["context"] = "台当局“观光局长”周永晖(右)及“公路总局长”陈彦伯(左)请辞。（图片来源：台湾《联合报》）查看大图中国台湾网2月19讯据台湾《中时电子报》报道，台湾蝶恋花武陵赏樱团在五号高速路翻覆，造成33人罹难、11伤，成为近30年来最严重的公路事故。台当局“观光局长”周永晖及“公路总局长”陈彦伯自我处分辞去“局长”职位。13日晚间，蝶恋花游览车在台湾5号高速路翻覆造成33死11伤，车龄过旧、司机超时工作等问题一一浮现。但事件没有随着各处“部长”与蝶恋花创办人周比苍等人出面发言而平缓，反而因为台当局“交通部长”贺陈旦、“劳动部长”林美珠、“公路总局”不当发言惹议，遭各界痛批冷血。外界也质疑为什么没有官员为此事件负责、下台。国民党文传会副主委李明贤认为，2000年“八掌溪”4条人命意外，让台当局“行政院副院长”游锡堃下台扛责；2007年台铁重大车祸，台铁局长陈峰男请辞，如今台湾高速路接连发生重大车祸，有学者痛批这是耻辱，贺陈旦还能安然坐大位上？今日有台媒报道，周永晖及陈彦伯自我请分，辞去“局长”职位。台当局“交通部政务次长”王国材证实，前几天周、陈两人向贺陈旦口头请辞，尚未有书面辞呈，台当局“交通部”内部则还在讨论是否准辞。"
        res["ptime"]="2017-02-19 10:44:12"
        mongo.db_conn["NewsDetails"].insert_one(res)
    except DuplicateKeyError:
        pass
    except Exception as e:
        logging.error(e)
