class MQClient(object):

    def __init__(self, address, user, password, exchange, queue):
        self.address = address
        self.user = user
        self.password = password
        self.exchange = exchange
        self.queue = queue

    def connect(self):
        pass

    def get_message(self):
        pass

    def send_message(self):
        pass

