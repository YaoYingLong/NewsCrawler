import queue
import re
import threading
import urllib

import requests
from snownlp import SnowNLP

from Config.InitConfig import InitConfig
from Config.RedisConf import RedisBase

class SpiderBase(object):

    def __init__(self, newsUrl):
        self.newsUrl = newsUrl
        self.redis_conn = self.redis_connector()

    @staticmethod
    def redis_connector():
        initConf = InitConfig("ServerConfig.ini")
        redisConnectConfig = initConf.getAllNodeItems("Redis");
        my_redis = RedisBase(**redisConnectConfig)
        return my_redis.use_redis

    def removeTag(self , soup, tagNameList):
        for tagName in tagNameList:
            [tag.extract() for tag in soup.find_all(tagName)]
        soup.prettify()
        return soup

    def getPureText(self, punctuationText):
        punctuation = u"""[\s+\.\!\/_,$%^*(+\"\']+|[A-Za-z0-9+?????''""????()??~@#?%??&*??:???(?)]+|[+——！，。？、：~@#￥%……&*（）《》]+"""
        pureText = re.sub(punctuation,"", punctuationText)
        return pureText

    def getNewsKeyWords(self, text):
        snow = SnowNLP(text)
        keyWords = snow.keywords(20)
        return " ".join(keyWords)

    def getUrlResponse(self, newsUrl):
        use_session = requests.session()
        use_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Charset': 'utf-8',
            'Cache-Control': 'no-cache',
            'Content-Type': "text/html; charset:UTF-8",
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        }
        req = use_session.get(newsUrl, headers=use_headers, timeout=None)
        if (req.encoding == 'ISO-8859-1'):
            req.encoding = 'gbk'

        if req.status_code == 200:
            return req.text
        else:
            return None

    # Abstract method to get new content.
    def getNewContent(self , html_cont):
        pass

    def getNewsList(self):
        pass

    def StartMonitor(self):
        self.getNewsList();

    def StopMonirot(self):
        self.timerEventer.stop()




