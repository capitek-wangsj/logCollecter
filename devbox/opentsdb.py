# coding=utf-8
import requests

payload = {
    "metric": "metric.log",
    "timestamp": '1489544891',
    "value": '29',
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
    "value": '29',
    "tags": {
        "host": "web01",
        "dc": "lga"
    }
}

payload3 = {
    "metric": "metric.log",
    "timestamp": '1489544894',
    "value": '30',
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
    print r.json()
    if r and r.json():
        return r.json()[0].get('dps')
    return []

def main():
    # 写入
    # print send_json(ls)

    # 读取
    print get_data_by_get('start=1489544891&m=sum:metric.log')


if __name__ == "__main__":
    main()