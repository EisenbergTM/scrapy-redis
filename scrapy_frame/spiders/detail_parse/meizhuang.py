# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.value import value


class meizhuang(value):
    def __init__(self):
        
        super(meizhuang,self).__init__()

    def extract(self,response):
        if 'http://k.sina.com.cn' in response.url:
            return self.parse_xinlangkandian(response)
    
    def parse_xinlangkandian(self,response):
        cont = ''
        title   = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
        content = response.xpath('//div[@class="article"]/*').extract()
        for i in content:
            if 'article-notice' not in i:
                cont += i
        #pubtime = int(time.mktime(time.strptime(pt,"%Y-%m-%d"))*1000)
        pt      =  response.xpath('//span[@class="date"]/text()').extract()[0].replace('年','-').replace('月','-').replace('日','')
        pubtime = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M"))*1000)
        author  = response.xpath('//a[@class="source ent-source"]/text()').extract()[0]

        self._name                 = 'xinlangyulekandian'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '新浪娱乐看点'
        self._site_name            = '新浪娱乐看点'
        self._content              = cont
        self._author               = author
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'meizhuangdasai'
        vlist = self.value_to_list()

        return vlist,0,response.url
 


