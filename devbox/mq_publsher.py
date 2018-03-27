# coding=utf-8
import pika
import time

MQ_HOST = 'localhost'
MQ_EXCHANGE = 'log_exchange'
MQ_QUEUE = 'hello'

def publisher():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_HOST))  # 创建一个连接
    channel = connection.channel()  # 创建通道
    channel.queue_declare(queue=MQ_QUEUE)  # 声明 queue

    for i in range(0, 100):
        channel.basic_publish(exchange=MQ_EXCHANGE,
                              routing_key='balance',
                              body='Hello World!')
        time.sleep(5)
    connection.close()


def main():
    publisher()


if __name__ == '__main__':
    main()
