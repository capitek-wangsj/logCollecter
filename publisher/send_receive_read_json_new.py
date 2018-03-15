#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json

import pika
from readfileConfigs import json_list


class RabbitMQPy(object):
    def __init__(self):
        self.msg_list = None
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='first_list111', exchange_type='fanout')
        self.rbt_connection()

    def rbt_connection(self):
        try:
            self.channel.queue_declare(queue='compute_queue1', durable=True)
        except:
            self.channel = self.connection.channel()
            self.channel.queue_delete(queue='compute_queue1')
            self.channel.queue_declare(queue='compute_queue1', durable=True)

    # 传入队列数据
    def publish(self, msg_list):
        msg = json.dumps(msg_list)
        # 将计算结构发送回控制中心
        self.channel.basic_publish(exchange='',
                                   routing_key='compute_queue1',
                                   body=msg,
                                   properties=pika.BasicProperties(delivery_mode=2, )  # properties 实现消息的持久化
                                   )

        # self.connection.close()

    def callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 消息不丢失的关键代码, 对应的是no_ack=False
        self.msg_list = body
        print u'callback数据是{0} 类型是{1}'.format(self.msg_list, type(self.msg_list))
        f = file('/home/share/demo-rabbit2/text.txt', 'w')
        f.write(self.msg_list)
        f.close()

    # 获取队列数据
    def consume(self):
        # 如果有多个消费者，不想跳着取数据，就按顺序取数据
        # 即只有工作者完成任务之后，才会再次接收到任务
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.callback,
                                   queue='news_list111',
                                   no_ack=False
                                   )

        # self.channel.start_consuming()


# 获取数据
def get_fence_nodes():
    rbt_obj = RabbitMQPy()
    rbt_obj.consume()
    # fence_codes = rbt_obj.consume()
    # print u'获取数据的方法值{0}'.format(fence_codes)
    # if not fence_codes:
    #     fence_codes = []
    #     return  fence_codes
    # else:
    #     rbt_obj.publish(fence_codes)
    #     return fence_codes


# 传入数据
def put_fence_nodes(fence_nodes):
    rbt_obj = RabbitMQPy()
    if fence_nodes:
        rbt_obj.publish(fence_nodes)


put_msg = json_list()
put_fence_nodes(put_msg)
get_fence_nodes()
