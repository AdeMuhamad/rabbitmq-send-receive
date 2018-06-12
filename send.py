#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='PUT URL RABBITMQ HERE'))
channel = connection.channel()

channel.queue_declare(queue='gans')

channel.basic_publish(exchange='',
                      routing_key='gans',
                      body='Hello Gans!')
print " [x] Sent 'Hello Gans!'"
connection.close()
