#!/usr/bin/env python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
              'PUT URL RABBITMQ HERE'))
channel = connection.channel()
channel.queue_declare(queue='gans')
def callback(ch, method, properties, body):
   print " [x] Received %r" % (body,)
channel.basic_consume(callback,
                     queue='gans',
                     no_ack=True)
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
