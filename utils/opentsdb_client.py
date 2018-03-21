import potsdb


class OpentsdbClient(object):
    def __init__(self, address, user, password):
        self.address = address
        self.user = user
        self.password = password
        metrics = potsdb.Client('hostname.local', port=4242, qsize=1000, host_tag=True, mps=100, check_host=True)

    def read(self):

        pass

    def write(self):
        pass


