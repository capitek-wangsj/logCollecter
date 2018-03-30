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


def main():
    print send_json(ls)


if __name__ == "__main__":
    main()