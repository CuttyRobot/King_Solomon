import time
import threading
import requests
import json
import os
import psutil
import multiprocessing

address = "http://localhost:13412/message"
address = "http://127.0.0.1:8000/message"
b = time.time()
pool = []
count_1 = 2000
count_2 = 1

def spammer():
    session = requests.session()
    a = time.time()
    for i in range(0, count_1):
        data = {
            "update_id": 424869840,
            "message": {
                "message_id": 357,
                "from": {
                    "id": 1897466312,
                    "is_bot": False,
                    "first_name": "Aleksandr",
                    "last_name": "Anurov",
                    "username": "aleksandr_anurov",
                    "language_code": "ru"
                },
                "chat": {
                    "id": 1897466312,
                    "first_name": "Aleksandr",
                    "last_name": "Anurov",
                    "username": "aleksandr_anurov",
                    "type": "private"
                },
                "date": 1697401093,
                "text": str(i)
            }
        }

        headers = {'Content-Type': 'application/json'}
        # print(time.time() - a)
        response = session.post(address, data=json.dumps(data), headers=headers)
        # print(f'{i}-message was sent')
    print(f'Time of process: {time.time() - a}')


if __name__ == "__main__":
    f = time.time()

    for i in range(0, count_2):
        session = requests.sessions
        process = multiprocessing.Process(target=spammer)
        process.start()
        pool.append(process)


    for elements in pool:
        elements.join()

    g = time.time() - f
    print(f"Time: {g}")
    print(f'RPS: {count_1*count_2/g}')