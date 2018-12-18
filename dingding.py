import datetime
import json
import requests

def send_dingding_msg(content,robot_id="da78abf94f8041db2cbebb2f8545965bfe3776a41a5852317db7cf79427338c3"):
    try:
        msg = {
            "msgtype":"text",
            "text":{
                "content":content + '\n' + datetime.datetime.now().strftime("%m-%d %H:%M:%S")
            }
        }

        Headers = {"Content-Type":"application/json ;charset=utf-8"}
        url = 'https://oapi.dingtalk.com/robot/send?access_token='+robot_id
        body = json.dumps(msg)
        requests.post(url,data=body,headers=Headers)
    except Exception as err:
        print('发送失败')

if __name__ == '__main__':
    content = 'Hello world!'
    send_dingding_msg(content)