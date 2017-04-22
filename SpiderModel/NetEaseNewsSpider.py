# _*_ coding: UTF-8 _*_
import json
import re
import urllib

from bs4 import BeautifulSoup

from CrawlerUtils.Utils import Tools
from SpiderModel.SpiderBase import SpiderBase

class NetEaseNewsSpider(SpiderBase):
    def __init__(self, newsUrl):
        super(NetEaseNewsSpider, self).__init__(newsUrl)
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
        for pageNum in range(100):
            interface_url = self.getRightInterfaceUrl(self.newsUrl , pageNum , 600)
            print(interface_url)
            interface_data = self.getUrlResponse(interface_url)
            print(interface_data)
            for data in self.tools.json_format_data(interface_data , interface_url):
                if self.tools.isUrl(data['url']):
                    news_page_url = self.tools.insert(data['url'] , '_0' ,len(data['url']) - 5)
                    try:
                        news_page = self.getUrlResponse(news_page_url)
                        content = self.getNewContent(news_page)
                        if content is not None:
                            NewsDict = dict();
                            NewsDict["_id"] = news_page_url
                            NewsDict["newsTitle"] = data['title']
                            NewsDict["pureTitle"] = self.getPureText(data['title'])
                            NewsDict["keyWords"] = self.getNewsKeyWords(content)
                            NewsDict["content"] = content
                            NewsDict["ptime"] = data['ptime']
                            print("input newsDict", NewsDict)
                            self.redis_conn.rpush("NewsDict", NewsDict)
                    except Exception as e:
                        print('Have a exception:', e)

if __name__=="__main__":
    # http://3g.163.com/touch/article/list/BA8J7DG9wangning/0-1000.html
    url = 'http://3g.163.com/touch/article/list/BD29LPUBwangning/'
    netEaseNewsSpoder = NetEaseNewsSpider(url);
    netEaseNewsSpoder.getNewsList()