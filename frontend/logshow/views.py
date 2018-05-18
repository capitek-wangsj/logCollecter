# -*- coding:UTF-8 -*-
from copy import deepcopy
from datetime import time
import pandas as pd
import numpy as np
import matplotlib



import requests
from django.http import JsonResponse
from django.shortcuts import render_to_response

OPENTSDB_METRIC_INPUT = 'metric.log.input'
OPENTSDB_METRIC_OUTPUT = 'metric.log.output'


def logshow(request):
    return render_to_response('line-marker.html')


def get_log_info(request):
    username = request.GET.get('username')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    print locals()
    # query = 'start={}&end={}&m=sum:{}'.format(start_time, end_time, OPENTSDB_METRIC_INPUT)
    # input_data = get_data_by_get(query)
    #
    # query = 'start={}&end={}&m=sum:{}'.format(start_time, end_time, OPENTSDB_METRIC_OUTPUT)
    # out_data = get_data_by_get(query)

    query = {
        "start": timestamps_start,
        "end": timestamps_end,
        "queries": [
            {
                "aggregator": "sum",
                "metric": "sys.batch.receive",
                "tags": {"username": username}
            },
        ]
    }


    input_data = {"times": ['10:00', '11:11', '12:11', '222']}
    return JsonResponse(input_data)


def get_data_by_get(query):
    # r = requests.get("http://localhost:4242/api/query?" + json=query)
    r = requests.get("http://localhost:4242/api/query?" + query)
    if len(r.json()) > 0:
        dps = r.json()[0]['dps']
        # dps_sort=sorted(dps.items(),key=lambda k: k[0], reverse=False)   # 将字典按时间戳升序排列
        list_data = sorted(dps.items(), cmp=lambda x, y: cmp(x[0], y[0]))  # 按照 key 正序排列
        byte_df = pd.DataFrame(list_data, columns=['date', 'byte'])  # 将 data 数据转换为 DataFrame操作

        # 原始列表: [1, 3, 3, 8, 15]
        # 增长率: [3, 3, 8, 15] - [1, 3, 3, 8] = [2, 0, 5, 7]
        byte_rise_df = pd.DataFrame(
            np.array(byte_df.byte[1:]) - np.array(byte_df.byte[:-1]),
            columns=['byte_rise_up']
        )
        byte_rise_df['date'] = byte_df.date[1:]  # 添加日期列

        # print byte_rise_df
        print byte_rise_df['date']                   #横坐标时间
        print byte_rise_df['byte_rise_up']           #纵坐标增长率
        return JsonResponse(byte_rise_df)

