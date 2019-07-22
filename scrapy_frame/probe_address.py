
# -*- coding:utf-8 -*-
#!/usr/local/bin/python

import os
import sys
import time
import json
import random
import requests
import datetime
import traceback

class ProbeAdress():
    def __init__(self):
        #self.probe_url = 'http://114.215.29.53:29889/probe_address'
        self.probe_url = 'http://114.215.18.7:29889/probe_address'

    def query_play_address(self, news_type, url):
        json_str = '{\"news_type\":\"' + str(news_type) + '\",\"url\":\"' + url + '\"}'
        play_url = ''
        try:
            rsp = json.loads(requests.post(self.probe_url, json_str).content)
            query_url = rsp['query_url']

            print('==========================: ' + str(rsp))
            if str(query_url) != 'None':
                play_url = self.query_state(query_url)

        except Exception:
            traceback.print_exc()
        return play_url

    def query_state(self, url):
        try:
            for i in range(0, 60):
                rsp = json.loads(requests.get(url).content)
                print('==========================: ' + str(rsp))
                if str(rsp['errmsg']) == 'waiting':
                    time.sleep(1)
                    continue
                elif str(rsp['errmsg']) == 'ok':
                    return str(rsp['response'])
                else:
                    return ''
        except Exception:
            traceback.print_exc()
            return ''

                
            

