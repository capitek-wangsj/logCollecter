# coding=utf-8
import logging
import time


class Publisher(object):
    def __init__(self, mqClient, logPath, sleep_time):
        self.mqClient = mqClient
        self.logPath = logPath
        self.sleep_time = sleep_time

    def start(self):
        # 隔10分钟读取一次
        timer = 0
        while 1:
            timer += 1
            print "read the {} times...".format(timer)
            # 读取 logPath 中的文件列表，最好是增量读取
            # 把读取到的文件列表写入到mq中
            time.sleep(self.sleep_time)
        pass
