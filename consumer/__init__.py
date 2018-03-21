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



#
# ﻿               <parameter name="field" value="event_timestamp:sysdate"/>
# <parameter name="field" value="acct_status_type:0"/>
# <parameter name="field" value="called_station_id:0"/>
# <parameter name="field" value="calling_station_id:0"/>
# <parameter name="field" value="multi:cisco_avpair:ssid"/>
# <parameter name="field" value="multi:cisco_avpair:nas_location"/>
# <parameter name="field" value="multi:cisco_avpair:vlan_id"/>
# <parameter name="field" value="multi:cisco_avpair:auth_algo_type"/>
# <parameter name="field" value="multi:cisco_avpair:connect_progress"/>
# <parameter name="field" value="acct_authentic:0"/>
# <parameter name="field" value="acct_session_time:0"/>
# <parameter name="field" value="user_name:"/>
# <parameter name="field" value="acct_session_id:0"/>
# <parameter name="field" value="acct_output_octets:0"/>
# <parameter name="field" value="acct_input_octets:0"/>
# <parameter name="field" value="acct_output_packets:0"/>
# <parameter name="field" value="acct_input_packets:0"/>
# <parameter name="field" value="acct_terminate_cause:0"/>
# <parameter name="field" value="multi:request:cisco_avpair:disc_cause_ext"/>
# <parameter name="field" value="nas_port_type:0"/>
# <parameter name="field" value="cisco_nas_port:0"/>
# <parameter name="field" value="nas_port:0"/>
# <parameter name="field" value="nas_ip_address:0"/>
# <parameter name="field" value="service_type:0"/>
# <parameter name="field" value="acct_delay_time:0"/>
# <parameter name="field" value="proxy_type:0"/>
# <parameter name="field" value="3gpp2_correlation_id:0"/>
# <parameter name="field" value="acct_unique_session_id:0"/>


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
