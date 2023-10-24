import time
import threading
import requests
import json
import os
import psutil
import multiprocessing

address = "http://192.168.31.102:13412/message"
b = time.time()
session = requests.session()
pool = []


def spammer():
    for i in range(0, 2000):
        a = time.time()
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
        # print(f'{i}-message was sended')
    print(f'Total time: {time.time() - b}')


if __name__ == "__main__":
    for i in range(8, 9):
        # Getting PID of a current process
        pid = os.getpid()

        # Creating a psutil object for process
        p = psutil.Process(pid)

        # Setting process affinity to targeted logic core
        p.cpu_affinity([i])
        process = multiprocessing.Process(target=spammer())
        process.start()
        pool.append(process)

    for elements in pool:
        elements.join()