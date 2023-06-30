import pika

connection_paramenters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="new_virtual_host",
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest",
    )
)

channel = pika.BlockingConnection(connection_paramenters).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="EstouMandandoAlgumaCoisa",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)