# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup

from SpiderModel.SpiderBase import SpiderBase


class SpiderMain(SpiderBase):
    def __init__(self, newsUrl):
        super(SpiderMain ,self).__init__(newsUrl)
        self.newsUrl = newsUrl;



    #获取新闻具体内容的函数
    def getNewsDetail(self):
        result = {}
        res = self.getUrlResponse(self.newsUrl)
        soup = BeautifulSoup(res.text,'html.parser')
        result['title'] = soup.select('#artibodyTitle')[0].text
        result['newsSource'] = source = soup.select('#navtimeSource span a')[0].text
        timesource = soup.select('#navtimeSource')[0].contents[0].strip()
        # result['newsTime'] = datetzime.strptime(timesource,'%Y年%m月%d日%H:%M')
        result['article'] = '\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
        result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
        # result['commentsCount'] = getCommentsCount(newsUrl)
        return result

#测试
if __name__ == "__main__":
    # http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=90&num=100&page=1
    newsUrl = 'http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml'
    spider = SpiderMain(newsUrl);
    result = spider.getNewsDetail()
    print(result)