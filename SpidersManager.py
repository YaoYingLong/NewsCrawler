# _*_ coding: UTF-8 _*_
import queue as Queue

from SpiderModel.NetEaseNewsSpider import SpiderMain
from Config.InitConfig import InitConfig


class SpidersManager(object):

    def __init__(self, confPath):
        self.serverConnectConfig = self.GetServerConnectConfig(confPath)
        self.spiderList = []

    def GetServerConnectConfig(self,configPath):
        conf = InitConfig(configPath)
        serverConnectConfig = conf.getAllNodeItems("ServerSocket")
        serverConnectConfig["port"] = int(serverConnectConfig.get("port"))
        return serverConnectConfig

    def CreatSpiders(self, spiderType, seedUrl):
        spider = spiderType(seedUrl)
        self.spiderList.append(spider)

    def SpidersConnectServer(self):
        print("SpidersConnectServer Start" , len(self.spiderList))
        # map(lambda spider : hasattr(spider,"ConnectServer") and spider.ConnectServer(**self.serverConnectConfig),self.spiderList)
        # for spider in self.spiderList:
        #     if hasattr(spider,"ConnectServer"):
        #         spider.ConnectServer()
        #     else :
        #         print("No have attr ConnectServer")
        # print("SpidersConnectServer end")

    def StartSpiderList(self):
        print("StartSpiderList Start")
        # map(lambda spider : hasattr(spider,"StartMonitor") and spider.StartMonitor(),self.spiderList)
        for spider in self.spiderList:
            if hasattr(spider,"StartMonitor"):
                spider.StartMonitor()
            else :
                print("No have attr StartMonitor")
        print("StartSpiderList end")

    def StartMonitor(self):
        # self.SpidersConnectServer()
        self.StartSpiderList()

    def StopSpiderList(self):
        map(lambda spider : hasattr(spider,"StopMonirot") and spider.StopMonirot(),self.spiderList)

def StartMonitorSpiderManager():
    spiderManager = SpidersManager("ServerConfig.ini")
    # spiderManager.CreatSpiders(LocalHtmlTestSpider,(r"http://192.168.1.217:8080/MonitorSystem/reportlistAction"))
    # 推荐
    spiderManager.CreatSpiders(SpiderMain, "http://3g.163.com/touch/article/list/BA8J7DG9wangning/")

    spiderManager.CreatSpiders(SpiderMain, "http://3g.163.com/touch/article/list/BBM54PGAwangning/")

    # spiderManager.CreatSpiders(SpiderMain, "http://3g.163.com/touch/article/list/BA10TA81wangning/")

    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8E6OEOwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8EE5GMwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8F6ICNwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI67OGGwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI6I0O5wangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8D4A3Rwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI6RHDKwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI6JOD9wangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8FF5PRwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BDC4QSV3wangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BA8DOPCSwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI6P3NDwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BAI6MTODwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BEO4GINLwangning/"))
    # spiderManager.CreatSpiders(SpiderMain, (r"http://3g.163.com/touch/article/list/BEO4PONRwangning/"))
    spiderManager.StartMonitor()

if  __name__ == '__main__':
    StartMonitorSpiderManager()
