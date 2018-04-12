#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic.base import View
import time
from django.core import serializers
# from forms import InputForm
from django.views.decorators.csrf import csrf_exempt
import requests
import json


def deal_times(*num_time):
    all_time = []
    new_all_time = []
    for ins in num_time:
        all_time.append(ins)

    for time_list in all_time:
        receive_time = time_list.split('T')
        start_year_mon_day = receive_time[0]
        start_hour_min_sec = receive_time[1]
        start_new_time = '%s %s' % (start_year_mon_day, start_hour_min_sec)
        new_all_time.append(start_new_time)

    return new_all_time

def deal_time(start_time, end_time):
    sta_time = start_time.split('T')
    start_year_mon_day = sta_time[0]
    start_hour_min_sec = sta_time[1]
    start_new_time = '%s %s' % (start_year_mon_day, start_hour_min_sec)

    en_time = end_time.split('T')
    end_year_mon_day = en_time[0]
    end_hour_min_sec = en_time[1]
    end_new_time = '%s %s' % (end_year_mon_day, end_hour_min_sec)

    return start_new_time, end_new_time

@csrf_exempt
def index(request):
    global new_start_time, new_end_time, result, query
    if request.method == 'POST':
        reqs = json.loads(request.body)
        username = reqs['username']
        start_time = reqs['start']
        end_time = reqs['end']

        if start_time and end_time=='':
            result = deal_times(start_time)
        else:
            result = deal_times(start_time, end_time)

        for get_time in range(len(result)):
            if len(result) == 1:
                time_Array_start = time.strptime(result[0], "%Y-%m-%d %H:%M:%S")
                timestamps_start = int(time.mktime(time_Array_start))
                query = 'start={0}&m=sum:sys.batch.test6'.format(timestamps_start)
            else:
                time_Array_start = time.strptime(result[0], "%Y-%m-%d %H:%M:%S")
                timestamps_start = int(time.mktime(time_Array_start))
                time_Array_end = time.strptime(result[1], "%Y-%m-%d %H:%M:%S")
                timestamps_end = int(time.mktime(time_Array_end))
                query = 'start={0}&end={1}&m=sum:sys.batch.test6'.format(timestamps_start, timestamps_end)
        r = requests.get("http://127.0.0.1:4242/api/query?" + query)
        if r.status_code == 200:
            print u'数据读取成功'
            if len(r.json()) > 0:
                dps = r.json()[0]['dps']
                # srvs_json = serializers.serialize("json", dps)
                print '数据是{0}'.format(dps)
                # return HttpResponse(dps)
        else:
            print u'数据读取失败'

        if not username:
            error_msg = u'请输入用户名'
            return render(request, 'index.html', {'errors': error_msg})
        else:
             return render(request, 'index.html', {'success': u'成功'})
    else:
        print u'跑出来了'
        inputform = InputForm()
        return render(request, 'index.html', {'inputform': inputform})