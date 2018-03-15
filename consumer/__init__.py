# coding=utf-8
import time


class Consumer(object):
    def __init__(self, mqClient, dbClient):
        self.mqClient = mqClient
        self.dbClient = dbClient

    def start(self):
        # 订阅 mq 的通知
        # 收到通知后，把通知写到 opentadb
        while 1:
            print "I am waiting for the message from mq..."
            time.sleep(2)
