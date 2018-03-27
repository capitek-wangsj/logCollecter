# coding=utf-8
import pika
import time

MQ_HOST = 'localhost'
MQ_EXCHANGE = 'log_exchange'
MQ_QUEUE = 'hello'


def consumer():
    # credentials = pika.PlainCredentials('admin', '123456')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(
    #     '192.168.56.19', 5672, '/', credentials))

    connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=MQ_QUEUE)  # 把消费者和生产者通过 queue 绑定起来，生产者的queue的也是hello
    channel.basic_consume(callback, queue=MQ_QUEUE, no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()  # 创建死循环，监听消息队列


def callback(self, ch, method, properties, body):
    print 'retrieve msg from mq: %s' % body


def main():
    consumer()

if __name__ == '__main__':
    main()
