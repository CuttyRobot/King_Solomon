import time
import fastapi
from fastapi import FastAPI
from telebot import async_telebot
import telebot
from telebot import types
import uvicorn
import aiohttp
import requests
import json
import httpx
import logging
import aio_pika
import asyncio
import os
import psutil
import hypercorn
from hypercorn.config import Config


app = FastAPI()

# docker run -it -d --name rabbit-production -p 194.85.203.38:5672:5672 -p 194.85.203.38:15672:15672 rabbitmq:3-management

project_url = "t.me/CyberDoctorBot"
personal_url = "test2.western-gate.online/message"
token = "6496231521:AAEoxoPKL2PctD2NEfF2GDtBoKubQWvFKcE"
url = f'https://api.telegram.org/bot{token}/setWebhook'
bot = async_telebot.AsyncTeleBot(token)


# Applying connection
# Initialize RabbitMQ connection and channel
rabbitMQ_connection = None
rabbitMQ_channel = None
queue_Images = "Images"
queue_Callbacks = "Callbacks"
queue_Messages = "Messages"

# Initialize three RabbitMQ queues
queue_names = [f"{queue_Messages}", f"{queue_Images}", f"{queue_Callbacks}"]
rabbitMQ_queues = {}
counter = 0
global_timer = 0


# Set up RabbitMQ during application startup
async def setup_rabbitmq():
    global rabbitMQ_connection, rabbitMQ_channel, rabbitMQ_queues

    if rabbitMQ_connection is None:
        rabbitMQ_connection = await aio_pika.connect_robust(
            "amqp://guest:guest@194.85.203.38:5672/"
        )

    rabbitMQ_channel = await rabbitMQ_connection.channel()

    # Create three queues
    for queue_name in queue_names:
        queue = await rabbitMQ_channel.declare_queue(queue_name, durable=False)
        rabbitMQ_queues[queue_name] = queue


# Event on startup of the application
@app.on_event("startup")
async def on_startup():
    # Create the aio-pika connection, channel, and queues when the FastAPI app starts
    await setup_rabbitmq()


# Event on terminating of the application
@app.on_event("shutdown")
async def on_shutdown():
    if rabbitMQ_connection:
        await rabbitMQ_connection.close()


# Telegram bot
@app.post("/message")
async def rocker(request: fastapi.Request):
    a = time.time()
    alpha = await request.body()

    # Decode string to byte format
    input_string_decoded = alpha.decode('utf-8')

    # Loading decoded string to json format
    json_data = json.loads(input_string_decoded)
    message = json_data

    # Message-first level keys
    first_level_keys = message.keys()

    # print('Message unpacking, before message processing:' + str(time.time() - a))

    if "message" in first_level_keys:
        # line -> Chat_ID
        line = int(message["message"]['chat']["id"])

        # Message second level keys
        second_level_keys = message["message"].keys()

        if "photo" in second_level_keys:
            # Message with image file
            print('Type: message with photo')

            # Publishing in RabbitMQ
            message_body = alpha
            message_head = line
            await rabbitMQ_channel.default_exchange.publish(
                aio_pika.Message(body=message_body,
                                 delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                routing_key=queue_Images
            )
            return

        elif "entities" in second_level_keys:
            # Text message (can include command)
            print('Type: command message')

            # Publishing in RabbitMQ
            message_body = alpha
            message_head = line
            await rabbitMQ_channel.default_exchange.publish(
                aio_pika.Message(body=message_body,
                                 delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                routing_key=queue_Messages
            )
            return

        else:
            # print('Before sending message:' + str(time.time() - a))
            # print('Type: common message')
            # await bot.send_message(line, str(message['message']['text']))
            # print(line)
            # print('After sending message:' + str(time.time() - a))

            # Publishing in RabbitMQ
            a = time.time()
            message_body = alpha
            await rabbitMQ_channel.default_exchange.publish(
                aio_pika.Message(body=message_body,
                                 delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                routing_key=queue_Messages
            )
            # print(time.time() - a)
            # print('After sending message and sending to query:' + str(time.time() - a))
            return

    elif "callback_query" in first_level_keys:
        print('Type: callback')
        print('Callback data:', message['callback_query']['data'])
        line = int(message['callback_query']["message"]['chat']["id"])

        # Publishing in RabbitMQ
        message_body = alpha
        await rabbitMQ_channel.default_exchange.publish(
            aio_pika.Message(body=message_body,
                                delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                                routing_key=queue_Callbacks
        )


@app.get("/check/{name}")
async def say_hello(name: str):
    return {"message": f"Checking system, {name}"}


@app.get("/uvertur/{balboa}")
async def uvertur(balboa: str):
    return {"message": f"Checking system, {balboa}"}


def set_webhook():
    url_webhook = f'https://api.telegram.org/bot{token}/setWebhook'
    webhook_url = 'https://test2.western-gate.online/message'
    response = requests.post(url_webhook, json={'url': webhook_url})
    print(response.text)


if __name__ == "__main__":
    set_webhook()

    # Get the number of CPU cores
    num_cores = psutil.cpu_count(logical=False)  # Physical CPU cores
    num_logical_cores = psutil.cpu_count(logical=True)  # Logical (including hyperthreaded) CPU cores

    print(f"Number of physical CPU cores: {num_cores}")
    print(f"Number of logical CPU cores: {num_logical_cores}")

    # Get information about the frequency of each core

    # cpu_frequency = psutil.cpu_freq()
    # print(f'Frequency of the CPU cores: {cpu_frequency}')

    # Getting PID of a current process
    pid = os.getpid()

    # Creating a psutil object for process
    p = psutil.Process(pid)

    # Setting process affinity to targeted logic core
    # p.cpu_affinity([0])

    # uvicorn.run(app, host='192.168.31.102', port=13412)
    uvicorn.run(app, host='194.85.203.38', port=13412)
