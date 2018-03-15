import argparse

import settings
from utils.mq_client import MQClient
from utils.opentsdb_client import OpentsdbClient
from publisher import Publisher
from consumer import Consumer

parser = argparse.ArgumentParser(description='provide a role name')
parser.add_argument('--role', type=str, default=None)
args = parser.parse_args()

PUBLISHER = 'publisher'
CONSUMER = 'consumer'
ROLES = (PUBLISHER, CONSUMER)


def main():
    if not args.role or args.role not in ROLES:
        print "please provide a role name: {}".format(ROLES)
        return

    print "The {} is running...".format(args.role)

    mqClient = MQClient(settings.MQ_ADDRESS, settings.MQ_USER, settings.MQ_PASSWORD, settings.MQ_EXCHANGE,
                        settings.MQ_QUEUE)
    dbClient = OpentsdbClient("", "", "")

    if args.role == PUBLISHER:
        pub = Publisher(mqClient, settings.LOG_PATH, settings.SLEEP_TIME)
        pub.start()
    elif args.role == CONSUMER:
        con = Consumer(mqClient, dbClient)
        con.start()
    else:
        return


if __name__ == "__main__":
    main()
