# _*_ coding: utf-8 _*_
import json
import re
import urllib

import requests
from bs4 import BeautifulSoup

from CrawlerUtils.Utils import Tools
from SpiderModel.SpiderBase import SpiderBase


class SinaNewsSpider(SpiderBase):

    def __init__(self, newsUrl):
        super(SinaNewsSpider ,self).__init__(newsUrl)
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

    def getNewsUrlList(self):
        param = {"col": 90, "num": 5, "page": 1}
        paramStr = urllib.parse.urlencode(param)
        new_url = self.newsUrl + "?" + paramStr
        return new_url

    def getNewsList(self):
        interface_data = self.getUrlResponse(self.getNewsUrlList())
        # format_data = interface_data[15:len(interface_data)-1]
        print(interface_data)
        # jsonData = json.loads(format_data, encoding='utf-8')
        # print(jsonData)

#测试
if __name__ == "__main__":
    # http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=90&num=100&page=1
    newsUrl = 'http://interface.sina.cn/wap_api/layout_col.d.json?showcid=56261&col=56261&level=1,2&show_num=30&page=1&act=more&jsoncallback=callbackFunction&_=1492738020527&callback=jsonp1'
    # newsUrl = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php'
    spider = SinaNewsSpider(newsUrl)
    spider.getNewsList()