import os

import potsdb

HOST = os.environ.get('OTSDB_TEST_HOST', '127.0.0.1')
PORT = int(os.environ.get('OTSDB_TEST_PORT', '42424'))


def _get_client(**kwargs):
    my_kwargs = {"port": PORT, "check_host": False, "test_mode": True}
    my_kwargs.update(kwargs)
    return potsdb.Client(HOST, **my_kwargs)


def main():
    t = _get_client(host_tag=None)
    body = {'id': "1", "name": "wangsj", "event_timestamp": "1234567890"}
    output = t.log('log.metric', 100, timestamp=body.get('event_timestamp'), **body)
    print output


if __name__ == '__main__':
    main()
