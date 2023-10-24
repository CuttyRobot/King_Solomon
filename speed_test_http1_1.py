import time
import requests
import json

address = "http://localhost:13412/message"
b = time.time()


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
    response = requests.post(address, data=json.dumps(data), headers=headers)
    # print(f'{i}-message was sended')
print(f'Total time: {time.time() - b}')