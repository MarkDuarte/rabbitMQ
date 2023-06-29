import pika
from callback import my_callback

class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__virtual_host = "new_virtual_host"
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_paraments = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            virtual_host=self.__virtual_host,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_paraments).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel
    
    def start(self):
        print('listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()

rabbitmq = RabbitmqConsumer(my_callback)
rabbitmq.start()