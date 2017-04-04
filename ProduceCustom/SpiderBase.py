import queue

from ServerClientSocket.ProcessingQueueNode import ProcessingQueueNode

urlQueue = queue.Queue()
newsQueue = queue.Queue()

class SpiderBaseTest(object):

    def __init__(self):
        self.spiderClawNode = None

    def ConnectServer(self, serveraddress="localhost", port=80, key=None):
        print("kkkkkkkkk")
        # if(self.spiderClawNode == None):
        spiderClawNode = ProcessingQueueNode()
        spiderClawNode.StartConnect(serveraddress, port, key)
        self.spiderClawNode = spiderClawNode
        print("kkkkkkkkk")