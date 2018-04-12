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

    query = 'start={}&end={}&m=sum:{}'.format(start_time, end_time, OPENTSDB_METRIC_INPUT)
    input_data = get_data_by_get(query)

    query = 'start={}&end={}&m=sum:{}'.format(start_time, end_time, OPENTSDB_METRIC_OUTPUT)
    out_data = get_data_by_get(query)

    # log_info = {"times": ['10:00', '11:11', '12:11', '222']}
    return JsonResponse(input_data)


def get_data_by_get(query):
    r = requests.get("http://localhost:4242/api/query?" + query)
    if len(r.json()) > 0:
        dps = r.json()[0]['dps']
        return dps
    else:
        return None
