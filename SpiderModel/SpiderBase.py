import queue
import re
import threading
import urllib

import requests
from snownlp import SnowNLP
from Config.RedisConf import RedisBase

class SpiderBase(object):
    def __init__(self):
        pass

    def __init__(self, seedUrl):
        self.seedUrl = seedUrl
        self.spiderClawNode = None
        self.redis_conn = self.redis_connector()

    @staticmethod
    def redis_connector():
        my_redis = RedisBase("192.168.19.155", 6379, 0, 62035529)
        return my_redis.use_redis

    def removeTag(self , soup, tagNameList):
        for tagName in tagNameList:
            [tag.extract() for tag in soup.find_all(tagName)]
        soup.prettify()
        return soup

    def getPureText(self, punctuationText):
        punctuation = u"""[\s+\.\!\/_,$%^*(+\"\']+|[A-Za-z0-9+——！“”''""‘’，。()？、~@#￥%……&*（）:：《》(图)]+"""
        pureText = re.sub(punctuation,"", punctuationText)
        return pureText

    def getNewsKeyWords(self, text):
        snow = SnowNLP(text)
        keyWords = snow.keywords(20)
        return " ".join(keyWords)

    def getUrlResponse(self , url):
        self.url = url
        use_session = requests.session()
        use_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
            # 'Host': 'news.163.com'
        }
        res_conn = use_session.get(self.url, headers=use_headers, timeout=None)
        if res_conn.status_code == 200:
            return res_conn.text
        else:
            return None

    # Abstract method to get new content.
    def getNewContent(self , html_cont):
        pass

    def getNewsList(self ):
        pass




