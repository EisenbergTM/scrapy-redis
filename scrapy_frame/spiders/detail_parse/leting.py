# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import requests
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.value import value
from scrapy_frame.find_id import BloomFilter
from scrapy_frame.redis_push import redis_push

class leting(value):
    def __init__(self):
        
        super(leting,self).__init__()
        self.reds = redis_push()
        self.rds = redis.Redis(host='118.190.243.148',port=16379,password='xdrt@^oasdfasf=<',db=0)
        self.redis_url   = '118.190.243.148|16379|xdrt@^oasdfasf=<|7'
        self.bf          = BloomFilter('shanxun', self.redis_url, [5, 7, 13, 17, 23])

    def extract(self,response):
        if 'https://app.leting.io/c/sync_data?' in response.url:
            print('its  ok')
            return self.parse_leting(response)

    def parse_leting(self,response):
        data_list = []
        vlist = []
              

        js = json.loads(response.body)
        
        if js['code'] == 401 or js['code'] == '401':
            print(js)
            print('leting reauthenticate !')
            self.reds.push('scrapy_start_urls','https://app.leting.io/auth?uid=12345&appid=8f5a691127c89465e44e3b195e588f05&app_secret=7c39c2f62a33ab61437fcd6e9e5c8be3&log_id=1234')
            return [],1,'',1
        else:
            for i in js['data']['data']:
                #print(i)
                pub_time = i['pub_time']
                #print(self.query_redis('leting'+str(i['sync_id']))+'==============================================')
                if self.query_redis('leting'+str(i['sync_id'])) == 'ok':

                    print(i)
                    print('-------------------------id_filter ok')
                    tags     = []
                    for p in i['tags'].split(','):
                        tags.append(p)
    
                    self._name                 = 'leting'
                    self._news_title           = i['news_title']
                    self._pub_time             = int(i['pub_time'])*1000
                    self._src_pub_time         = int(i['pub_time'])*1000
                    self._news_source          = i['news_source']
                    self._site_name            = i['news_source']
                    self._list_images          = '["'+ i['list_images'] + '"]'
                    self._content              = '[{"type":"nlp","data":"'+ str(i['news_content']) +'"}]'
                    self._channel              = i['catalog_name']
                    self._tags                 = str(tags).replace('\'','"')
                    self._id                   = self.set_id()
                    self._type                 = 5
                    self._is_hot               = i['isHot']
                    self._duration             = i['duration']
                    self._from_source          = 'leting'
                    self._third_id             = i['sync_id']
                    self._is_used_src_resource = '1'
                    self._is_pass_directly     = '1'
                    self._from_sources         = '["leting"]'
                    vlist = self.value_to_list()
                    pub_time = i['pub_time']
                    self.reds.set_key('leting',str(pub_time))
                    #url = 'https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234'
                    data_list.append(vlist)
                else:
                    print('leting repead sync_id!!!',pub_time)
                    self.reds.set_key('leting',str(pub_time))
                url = 'https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234'    
            #time.sleep(10) 
            return data_list,1,url,1
    
    def query_redis(self,url):
        if self.bf.isContains(str(url)):
            print('exist')
            return 'exist'
        else:
            print('ok')
            print('-------------------------------------------------------------------------------')
            self.bf.insert(str(url))
            return 'ok'

    def get_hot(self):
        query_url = 'http://10.66.181.119:9200/nm_*/_search'
        query_headers = {'Content-Type':'application/json;charset=UTF-8'}
        hot_ids = []
        last_hot_id = self.reds.query('last_hot_id')
        token = self.reds.query('leting_headers')
        leting_url = 'https://app.leting.io/c/get_hot_tags?log_id=1234'
        leting_headers = {"uid":"12345","token":str(token)}
        html = requests.get(leting_url,headers=leting_headers)
        for i in html.json()['data']['data']:
            a = i['sync_id']
            if self.query_redis('leting_hot'+str(i['sync_id'])) == 'ok':
                query_str = '{"query":{"bool":{"must":[{"term":{"third_id":"'+str(a)+'"}}]}}}'
                html = requests.get(query_url,data=query_str.encode('utf-8'),headers=query_headers)
                for i in html.json()['hits']['hits']:
                    hot_ids.append(i['_id'])
                self.reds.set_key('last_hot_id',str(a))
        req_str = ''
        a = a = str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_mon)
        now_month = 'nm_' + a[2:]
        if hot_ids != []:
            for i in hot_ids:
                req_str += '{ "update" : {"_id" : "'+str(i)+'", "_type" : "news","_index":"'+str(now_month)+'"} }\n { "doc" : {"is_hot" : 1},"detect_noop":false }\n'
            url = 'http://10.66.181.119:9200/_bulk'
            html = requests.post(url,data=req_str.encode('utf-8'),headers=query_headers)
            return html.json()
        return ''





