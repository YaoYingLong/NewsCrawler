# _*_ coding: UTF-8 _*_

from ProduceCustom.SpiderBase import SpiderBaseTest
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

    def CreatSpiders(self, spider):
        self.spiderList.append(spider)

    def SpidersConnectServer(self):
        print("SpidersConnectServer Start" , len(self.spiderList))
        map(lambda spider : hasattr(spider,"ConnectServer") and spider.ConnectServer(**self.serverConnectConfig),self.spiderList)
        for spider in self.spiderList:
            if hasattr(spider, "ConnectServer"):
                spider.ConnectServer(self.serverConnectConfig)
            else :
                print("No have attr ConnectServer")
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
        self.SpidersConnectServer()
        # self.StartSpiderList()

    def StopSpiderList(self):
        map(lambda spider : hasattr(spider,"StopMonirot") and spider.StopMonirot(),self.spiderList)

def StartMonitorSpiderManager():
    spiderManager = SpidersManager("ServerConfig.ini")
    spiderManager.CreatSpiders(SpiderBaseTest)
    spiderManager.CreatSpiders(SpiderBaseTest)

    spiderManager.StartMonitor()

if  __name__ == '__main__':
    StartMonitorSpiderManager()
