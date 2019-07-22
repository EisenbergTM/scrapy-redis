#-*- coding:UTF-8 -*-

import json
import requests
import traceback
from threading import Thread

class kafka_process():

    def __init__(self):
        self.url      = 'http://118.190.243.148:23489/kafka_proxy'


    def sendto_kafka(self, topic, json_str):
        try:
            user_agent ='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
            headers = {'User-Agent':user_agent}
            #body = "{\"topic\":\"" + str(topic) + "\",\"data\":[" + str(json_str) + "]}"
            body = "{\"topic\":\""+topic+"\",\"data\":[" + str(json_str) + "]}"
            print('===============sending...')
            NETWORK_STATUS = True
            REQUEST_TIMEOUT = False
            try:
                #html = requests.post(self.url, body.encode('utf-8'), timeout=0.1)
                html = requests.post(self.url, body.encode('utf-8'), timeout=0.1,headers={'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'})
            except requests.exceptions.ConnectTimeout:#连接超时
                NETWORK_STATUS = False
            except requests.exceptions.Timeout:#请求超时
                REQUEST_TIMEOUT = True
            print("network_status", NETWORK_STATUS)
            print("request_timeout", REQUEST_TIMEOUT)
            print(html.content)
            return body
        except BaseException:
            traceback.print_exc()
