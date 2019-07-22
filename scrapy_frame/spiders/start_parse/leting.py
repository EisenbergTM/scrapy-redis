# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.redis_push import redis_push



class leting():
    def __init__(self):
        
        super(leting,self).__init__()
        self.rds        = redis_push()

    def extract(self,response):
        if 'https://app.leting.io/auth?' in response.url:
            return self.parse_leting(response)

    def parse_leting(self,response):
        print(response.url)
        urllist = []
        token = ''
        js = json.loads(response.body)
        print(js)
        if js['data'] != []:
            token = js['data']['token']
        #headers = {"uid":"qiyu_123456","token":token}
        #_id = self.rds.query('leting')
        pubtime = self.rds.query('leting')
        self.rds.set_key('leting_headers',token)
        url = 'https://app.leting.io/c/sync_data?pub_time='+ str(pubtime)  +'&log_id=1234'
        urllist.append(url)
            
        return urllist,0



