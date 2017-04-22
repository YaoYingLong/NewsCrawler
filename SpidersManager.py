# _*_ coding: UTF-8 _*_

from SpiderModel.NetEaseNewsSpider import NetEaseNewsSpider

class SpidersManager(object):

    def __init__(self):
        self.spiderList = []

    def CreatSpiders(self, spiderType, seedUrl):
        spider = spiderType(seedUrl)
        self.spiderList.append(spider)

    def StartSpiderList(self):
        for spider in self.spiderList:
            spider.StartMonitor()

    def StartMonitor(self):
        self.StartSpiderList()

def StartMonitorSpiderManager():
    spiderManager = SpidersManager()
    spiderManager.CreatSpiders(NetEaseNewsSpider, "http://3g.163.com/touch/article/list/BD29LPUBwangning/")
    spiderManager.StartMonitor()

if  __name__ == '__main__':
    StartMonitorSpiderManager()
