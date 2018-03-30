# coding=utf-8
import argparse
import json
import random

import os
import time

import pika
import potsdb
import requests

import settings
from utils.util_logs import read_log_file, read_log_dir

parser = argparse.ArgumentParser(description='provide a role name')
parser.add_argument('--role', type=str, default=None)
args = parser.parse_args()

PUBLISHER = 'publisher'
CONSUMER = 'consumer'
ROLES = (PUBLISHER, CONSUMER)


class Worker:
    def __init__(self, role):
        self.role = role
        if self.role not in ROLES:
            raise Exception("Invalid role: %s" % self.role)

        self.db_client = self.get_db_client()
        self.connection, self.channel = self.get_mq_channel()

    def start(self):
        print "The {} is running...".format(args.role)
        if self.role == PUBLISHER:
            self.publisher()
        elif self.role == CONSUMER:
            self.consumer()
        else:
            return

    def get_db_client(self):
        return potsdb.Client(host=settings.OPENTSDB_HOST, port=settings.OPENTSDB_PORT,
                             qsize=1000, host_tag=True,
                             mps=100, check_host=True)

    def get_mq_channel(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.MQ_HOST))  # 创建一个连接
        channel = connection.channel()  # 创建通道
        channel.queue_declare(queue=settings.MQ_QUEUE, durable=True)  # 声明 queue
        return connection, channel

    def publisher(self):
        connection, channel = self.get_mq_channel()
        try:
            while 1:
                latest_log_name = self.get_latest_log_name()
                log_filenames = read_log_dir(settings.LOG_PATH, latest_log_name)
                channel.basic_publish(exchange=settings.MQ_EXCHANGE,
                                      routing_key=settings.MQ_ROUTING_KEY,
                                      body=json.dumps(log_filenames))
                time.sleep(settings.SLEEP_TIME)

        except Exception as ex:
            print ex.message
        finally:
            connection.close()

    def consumer(self):
        connection, channel = self.get_mq_channel()
        try:
            channel.basic_consume(self.callback, queue=settings.MQ_QUEUE, no_ack=True)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()  # 创建死循环，监听消息队列
        except Exception as ex:
            print ex.message
        finally:
            connection.close()

    def get_latest_log_name(self):
        # todo get the latest_log_name from one place
        with open(os.path.join("log_name")) as o:
            name = o.readline()
            return name

    def save_latest_log_name(self, latest_log_name):
        # todo save the latest_log_name in one place
        with open(os.path.join("log_name")) as o:
            o.write(latest_log_name)

    def send_json(self, json):
        r = requests.post("http://localhost:4242/api/put?details", json=json)
        return r.text

    # 回调函数中收到通知后，做相关操作： 解析body，保存存档点，循环读取日志内容，把日志内容写入数据库
    def callback(self, ch, method, properties, body):
        print 'ch: %s; method: %s; properties: %s; body: %s;' % (ch, method, properties, body)

        try:
            log_names = json.loads(body)
            if log_names:
                latest_log_name = log_names[0]
                self.save_latest_log_name(latest_log_name)
                for i, log_name in enumerate(log_names):
                    print '%d: Reading the file: %s' % (i, log_name)
                    logs = read_log_file(os.path.join(settings.LOG_PATH, log_name))
                    if logs:
                        # data = []
                        for j, log in enumerate(logs):
                            if isinstance(log, dict):
                                print '--- %d.%d: Reading the line' % (i, j)
                                d = dict(
                                    metric=settings.OPENTSDB_METRIC,
                                    timestamp=log.get('event_timestamp'),
                                    value=random.randint(0, 10000000),  # todo set what?
                                    tags=log,
                                )
                                response = self.send_json(d)
                                print 'Insert data to db. Response: %s' % response

                                # self.db_client.log('metric.log', 100, timestamp=log.get('event_timestamp'), **log)

                        # if data:
                        #     response = self.send_json(data)
                        #     print 'Insert %d data to db. Response: %s' % (len(data), response)

        except Exception as ex:
            print ex.message
            print "!!! the format of the body is invalid: %s" % body
        finally:
            pass


def main():
    worker = Worker(args.role)
    worker.start()


if __name__ == "__main__":
    main()
