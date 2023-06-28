import json
import random
import time

from confluent_kafka import Producer

from config import TOPIC, PRODUCER_CONFIG, PRODUCER_LOG, SLEEP_PERIOD, MAIL_TO


def kafka_producer(producer_config, topic, producer_log_file):
    p = Producer(producer_config)

    for order in generate_order(producer_log_file):
        p.produce(topic, value=json.dumps(order))
        p.flush()


def generate_order(producer_log_file):
    order_id = 1
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]

    # This is customer email, read from config as mock
    emails = [MAIL_TO]

    start_time = time.time()
    while True:
        order = {
            "order_id": order_id,
            "product": random.choice(products),
            "email": random.choice(emails),
            "timestamp": time.time()
        }
        with open(producer_log_file, 'a') as f:
            json.dump(order, f)
        yield order
        order_id += 1
        time.sleep(SLEEP_PERIOD)
        if time.time() - start_time > 60*1:
            break


if __name__ == '__main__':
    kafka_producer(PRODUCER_CONFIG, TOPIC, PRODUCER_LOG)
