# coding=utf-8
import requests

payload = {
    "metric": "metric.log",
    "timestamp": '1489544891',
    "value": '20',
    "tags": {
        "host": "web01",
        "dc": "lga"
    }
}

payload1 = {
    "metric": "metric.log",
    "timestamp": '1489544892',
    "value": '30',
    "tags": {
        "host": "web01",
        "dc": "lga"
    }
}

payload2 = {
    "metric": "metric.log",
    "timestamp": '1489544893',
    "value": '50',
    "tags": {
        "host": "web01",
        "dc": "lga"
    }
}

payload3 = {
    "metric": "metric.log",
    "timestamp": '1489544894',
    "value": '100',
    "tags": {
        "host": "web01",
        "dc": "lga"
    }
}

ls = [payload, payload1, payload2, payload3]


def send_json(json):
    r = requests.post("http://localhost:4242/api/put?details", json=json)
    return r.text


def get_data_by_get(query):
    r = requests.get("http://localhost:4242/api/query?" + query)
    if r.status_code < 300 and r.json():
        return r.json()[0].get('dps')
    return []


def get_data_by_post(dict_query):
    r = requests.get("http://localhost:4242/api/query", json=dict_query)
    if r.status_code < 300 and r.json():
        return r.json()[0].get('dps')
    return []


def main():
    # 写入
    # print send_json(ls)

    # 通过 get 方法读取
    print get_data_by_get('start=2018/01/27 00:00:00&end=&m=sum:metric.log.input{user_name=zhaolk}')

    # # 通过 post 方法读取
    # cond_dic_receive = {
    #     "start": '1490586530',
    #     # "end": '',
    #     "queries": [
    #         {
    #             "aggregator": "sum",
    #             "metric": "metric.log.input",
    #             "tags": {}
    #         },
    #     ]
    # }
    # return get_data_by_post(cond_dic_receive)


if __name__ == "__main__":
    main()
