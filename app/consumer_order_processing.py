import json
import time

from confluent_kafka import Consumer

from config import TOPIC, PROCESSING_CONSUMER_CONFIG, PROCESSING_CONSUMER_LOG, SLEEP_PERIOD

topic = 'orders'


def process_order(order):
    print(f"Processing order: {order}", flush=True)


def kafka_consumer_processing():
    c = Consumer(PROCESSING_CONSUMER_CONFIG)
    c.subscribe([TOPIC])

    while True:
        messages = c.consume(num_messages=1, timeout=1.0)
        for message in messages:
            if message is None:
                continue
            if message.error():
                print(f"Consumer error: {message.error()}", flush=True)
                continue

            order = message.value().decode('utf-8')
            order = json.loads(order)

            process_order(order)
            with open(PROCESSING_CONSUMER_LOG, 'a') as f:
                json.dump(order, f)
            time.sleep(SLEEP_PERIOD)


if __name__ == '__main__':
    kafka_consumer_processing()
