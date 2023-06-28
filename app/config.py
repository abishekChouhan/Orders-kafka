import os

TOPIC = os.environ["KAFKA_TOPIC"]
DLQ_TOPIC = os.environ.get("DLQ_TOPIC")

SLEEP_PERIOD = float(os.environ["SLEEP_PERIOD"])
TMP_DIR = os.environ["TMP_DIR"]
KAFKA_SERVER = os.environ["KAFKA_BOOTSTRAP_SERVERS"]
OFFSET_RESET = os.environ["OFFSET_RESET"]
EMAIL_CONSUMER_GROUP = os.environ.get("EMAIL_CONSUMER_GROUP")
PROCESSING_CONSUMER_GROUP = os.environ.get("PROCESSING_CONSUMER_GROUP")

MAIL_FROM = os.environ.get("MAIL_FROM")
MAIL_TO = os.environ.get("MAIL_TO")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


PRODUCER_CONFIG = {
    'bootstrap.servers': KAFKA_SERVER,
    'client.id': 'kafka_producer'
}
PRODUCER_LOG = f'{TMP_DIR}/order.log'


EMAIL_CONSUMER_CONFIG = {
    'bootstrap.servers': KAFKA_SERVER,
    'group.id': EMAIL_CONSUMER_GROUP,
    'auto.offset.reset': OFFSET_RESET
}
EMAIL_CONSUMER_LOG = f'{TMP_DIR}/email.log'


PROCESSING_CONSUMER_CONFIG = {
    'bootstrap.servers': KAFKA_SERVER,
    'group.id': PROCESSING_CONSUMER_GROUP,
    'auto.offset.reset': OFFSET_RESET
}
PROCESSING_CONSUMER_LOG = f'{TMP_DIR}/processing.log'
