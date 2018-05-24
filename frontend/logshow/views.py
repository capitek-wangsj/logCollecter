# -*- coding:UTF-8 -*-
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render_to_response

from utils.opentsdb import get_data_by_get

OPENTSDB_METRIC_INPUT = 'metric.log.input'
OPENTSDB_METRIC_OUTPUT = 'metric.log.output'


def logshow(request):
    return render_to_response('line-marker.html')


def get_log_info(request):
    username = request.GET.get('username')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    query = "start=%s&end=%s&m=sum:metric.log.input" % (start_time, end_time)
    if username:
        query = "%s{user_name=%s}" % (query, username)
    data = get_data_by_get(query)
    if data:
        list_data = sorted(data.items(), cmp=lambda x, y: cmp(x[0], y[0]))  # 按照 key 正序排列
        byte_df = pd.DataFrame(list_data, columns=['date', 'byte'])  # 将 data 数据转换为 DataFrame操作
        # 原始列表: [1, 3, 3, 8, 15]
        # 增长率: [3, 3, 8, 15] - [1, 3, 3, 8] = [2, 0, 5, 7]
        byte_rise_df = pd.DataFrame(
            np.array(byte_df.byte[1:]) - np.array(byte_df.byte[:-1]),
            columns=['byte_rise_up']
        )
        byte_rise_df['byte'] = byte_df.byte[1:]
        byte_rise_df['date'] = byte_df.date[1:]  # 添加日期列
        # print byte_rise_df['date'].values
        # print byte_rise_df['byte_rise_up'].values

        return JsonResponse({'code': 0, 'message': byte_rise_df.to_dict()})
    return JsonResponse({'code': 1, 'message': 'Get emtpy'})
