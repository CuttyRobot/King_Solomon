import datetime
import json

import requests

# MorgenWald
if __name__ == "__main__":
    # alpha = requests.post('http://test2.western-gate.online/hello/world')
    # print(alpha.text)
    tabl_1 = {
        "message_id": 1,
        "date-time": str(datetime.datetime.now())
    }
    lost = requests.post('http://127.0.0.1:13412/message',
                         data=b'{"update_id":424869654,\n"message":{"message_id":10,"from":{"id":1897466312,"is_bot":false,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","language_code":"en"},"chat":{"id":1897466312,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","type":"private"},"date":1695919025,"text":"Hello, i\'m mister Misix"}}')
    print(lost.text)

    damned = requests.post('http://127.0.0.1:13412/message',
                           data=b'{"update_id":424869656,\n"message":{"message_id":16,"from":{"id":1897466312,"is_bot":false,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","language_code":"en"},"chat":{"id":1897466312,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","type":"private"},"date":1696175876,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}')
    print(damned.text)

    bared = requests.post('http://127.0.0.1:13412/message',
                          data=b'{"update_id":424869658,\n"message":{"message_id":22,"from":{"id":1897466312,"is_bot":false,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","language_code":"en"},"chat":{"id":1897466312,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","type":"private"},"date":1696176396,"video":{"duration":237,"width":1280,"height":720,"file_name":"_Ado_\\u65b0\\u6642\\u4ee3_\\u30a6\\u30bf_from_ONE_PIECE_FILM_RED_1FliVTcX8bQ_136.mp4","mime_type":"video/mp4","thumbnail":{"file_id":"AAMCAgADGQEAAxZlGZkMcYwowOTimrQ6lP3opHskBgACLTcAAoXCyEgKQrCl3weISQEAB20AAzAE","file_unique_id":"AQADLTcAAoXCyEhy","file_size":1266,"width":320,"height":180},"thumb":{"file_id":"AAMCAgADGQEAAxZlGZkMcYwowOTimrQ6lP3opHskBgACLTcAAoXCyEgKQrCl3weISQEAB20AAzAE","file_unique_id":"AQADLTcAAoXCyEhy","file_size":1266,"width":320,"height":180},"file_id":"BAACAgIAAxkBAAMWZRmZDHGMKMDk4pq0OpT96KR7JAYAAi03AAKFwshICkKwpd8HiEkwBA","file_unique_id":"AgADLTcAAoXCyEg","file_size":16158751}}}')
    print(bared.text)

    abridged = requests.post('http://127.0.0.1:13412/message',
                          data=b'{"update_id":424869661,\n"callback_query":{"id":"8149555758461737508","from":{"id":1897466312,"is_bot":false,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","language_code":"en"},"message":{"message_id":24,"from":{"id":6496231521,"is_bot":true,"first_name":"Cyber Doctor","username":"CyberDoctorBot"},"chat":{"id":1897466312,"first_name":"Aleksandr","last_name":"Anurov","username":"aleksandr_anurov","type":"private"},"date":1696176628,"text":"Welcome to HealthC bot. Choose system language:","reply_markup":{"inline_keyboard":[[{"text":"Fuck You!","callback_data":"1"},{"text":"No, Fuck You","callback_data":"2"}]]}},"chat_instance":"5027246075018156001","data":"2"}}')
    print(abridged.text)
