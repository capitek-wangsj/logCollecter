# coding=utf-8
import json
import time

import pika


class Consumer(object):
    metric = "log.data"

    def __init__(self, mqClient, dbClient):
        self.mqClient = mqClient
        self.dbClient = dbClient

    def start(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(callback,
                              queue='hello',
                              no_ack=False)


def callback(self, ch, method, properties, body):
    print 'receive msg: %s' % body

    data = dict(
        sysdate='',
        acct_status_type='',
        called_station_id='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
        # sysdate='',
    )


    self.dbClient.send(self.metric, json.dumps(data), **data)
