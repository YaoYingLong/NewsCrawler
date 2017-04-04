# _*_ coding: UTF-8 _*_
import json
import re
import urllib

from bs4 import BeautifulSoup

from Config.MongoDBConf import MyMongoDB
from CrawlerUtils.Utils import Tools
from SpiderModel.SpiderBase import SpiderBase

mongo = MyMongoDB("localhost", 27017, "wncg", "123456", "news_data")

class SpiderMain(SpiderBase):
    def __init__(self, seedUrl):
        super(SpiderMain, self).__init__(seedUrl)
        self.tools = Tools()

    def getNewContent(self , html_cont):
        _soup = BeautifulSoup(html_cont , 'html.parser')
        try:
            html_content = self.removeTag(_soup, ['a' , 'img'])
            contents = html_content.find('div', class_='content').find_all('p')
            news_content = ''.join(map(lambda content : ''.join(content.get_text().split()) , contents))
        except Exception as e:
            print("Exception: 获取新闻正文出现异常")
            return None
        return news_content

    def getRightInterfaceUrl(self, url , pageNum , pageSize):
        str_uri = str(pageNum) + '-' + str(pageSize) + '.html'
        new_url = urllib.parse.urljoin(url , str_uri)
        return new_url

    def getNewsList(self):
        interface_url = self.getRightInterfaceUrl(self.seedUrl , 0 , 600)
        print(interface_url)
        interface_data = self.getUrlResponse(interface_url)
        for data in self.tools.json_format_data(interface_data , interface_url):
            if self.tools.isUrl(data['url']):
                news_page_url = self.tools.insert(data['url'] , '_0' ,len(data['url']) - 5)
                try:
                    news_page = self.getUrlResponse(news_page_url)
                    content = self.getNewContent(news_page)
                    if content is not None:
                        newsDict = dict();
                        newsDict["_id"] = news_page_url
                        newsDict["title"] = data['title']
                        newsDict["pure_title"] = self.getPureText(data['title'])
                        newsDict["key_words"] = self.getNewsKeyWords(content)
                        newsDict["contents"] = content
                        newsDict["ptime"]= data['ptime']
                        print("input newsDict", newsDict)
                        self.redis_conn.rpush("newsDict" , newsDict)
                except Exception as e:
                    print('Have a exception:', e)

    # def craw(self):
    #     i = 0
    #     while i < 100:
    #         interface_url = self.getRightInterfaceUrl(self.seedUrl , i , 600)
    #         i += 1
    #         print(interface_url)
    #         interface_data = self.getUrlResponse(interface_url)
    #         for data in self.tools.json_format_data(interface_data , interface_url):
    #             u_str = self.tools.insert(data['url'] , '_0' ,len(data['url']) - 5)
    #             try:
    #                 _html = self.getUrlResponse(u_str)
    #                 contents = self.getNewContent(_html)
    #                 if contents is not None:
    #                     res = {};
    #                     res["_id"] = u_str
    #                     res["title"] = data['title']
    #                     res["pure_title"] = self.getPureText(data['title'])
    #                     res["key_words"] = self.getNewsKeyWords(contents)
    #                     res["contents"] = contents
    #                     res["ptime"]= data['ptime']
    #                     self.log(res);
    #                     mongo.db_conn["NewsDetails"].insert_one(res)
    #             except Exception as e:
    #                 print('Have a exception:', e)
    #
    # def log(self, news):
    #     print("url:", news["_id"])
    #     print("title:", news["title"])
    #     print("pureTitle:", news["pure_title"])
    #     print("key_words:", news["key_words"])
    #     print("contents:", news["contents"])
    #     print("ptime:", news["ptime"])

    def StartMonitor(self):
        print("SpiderMain StartMonitor")
        SpiderBase.StartMonitor(self, self.seedUrl)

if __name__=="__main__":
    # http://3g.163.com/touch/article/list/BA8J7DG9wangning/0-1000.html
    original_url = 'http://3g.163.com/touch/article/list/BA8J7DG9wangning/'
    obj_spider = SpiderMain(original_url);
    obj_spider.getNewsList()
    # for i in range(20):
    #     print(i)

    # spiderTencentChengDuNews = SpiderMain("http://3g.163.com/touch/article/list/BA8J7DG9wangning/")
    # spiderTencentChengDuNews.ConnectServer('127.0.0.1', 5000, b'abc')
    # print(spiderTencentChengDuNews.GetNewsListAndPutToQueue())