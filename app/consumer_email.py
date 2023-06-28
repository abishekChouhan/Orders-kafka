import json
import time

from confluent_kafka import Consumer, Producer

from config import TOPIC, EMAIL_CONSUMER_CONFIG, EMAIL_CONSUMER_LOG, SLEEP_PERIOD, KAFKA_SERVER, DLQ_TOPIC
from send_email import EmailException, send_email

DLQ_PRODUCER = Producer({'bootstrap.servers': KAFKA_SERVER})


def extract_email(order):
    return order.get('email')


def kafka_consumer_email():
    c = Consumer(EMAIL_CONSUMER_CONFIG)
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
            email_to = extract_email(order)
            with open(EMAIL_CONSUMER_LOG, 'a') as f:
                json.dump(order, f)

            try:
                subject = 'Order Confirmation'
                body = 'Your order has been placed successfully.'
                send_email(email_to, subject, body)
            except EmailException as e:
                print(f"Error in processing order: {order}, error: {e}", flush=True)

                # Send fail even to dead letter queue
                failure_event = {"type": "email failure", "details": order}
                DLQ_PRODUCER.produce(DLQ_TOPIC, value=json.dumps(failure_event))
            else:
                print(f"Email sent to : {email_to}, subject: {subject}, order_id: {order.get('order_id')}", flush=True)



if __name__ == '__main__':
    kafka_consumer_email()
