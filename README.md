## Kafka Orders

Setup Steps:
1. Clone this repo, and change directory to project root.
2. Create .env file:
```
KAFKA_TOPIC=orders
DLQ_TOPIC="failed_email_orders"

TMP_DIR=/app/data
SLEEP_PERIOD=5
OFFSET_RESET=earliest

EMAIL_CONSUMER_GROUP=email_consumer_group
PROCESSING_CONSUMER_GROUP=processing_consumer_group


MAIL_FROM=<your_mail_id>
MAIL_PASSWORD=<your_mail_password>
MAIL_TO=<mail_id_to_send_mail>
```
3. Run: `docker-compose up --build`
