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


class guangle(value):
    def __init__(self):
        
        super(guangle,self).__init__()

    def extract(self,response):
        if 'https://www.zcool.com.cn' in response.url:
            return self.parse_guangle(response)

    def parse_guangle(self,response):
        cont = ''
        title    = response.xpath('//div[@class="details-contitle-box"]/h2/text()').extract()[0]
        cont     = response.xpath('//div[@class="work-center-con"]').extract()[0].replace('\n','').replace('\t','').replace('\r','').replace(' ','')
        tag      = response.xpath('//span[@class="head-index"]/span/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        author   = response.xpath('//a[@class="title-content"]/text()').extract()[0].replace('\n','').replace('\t','').replace('\r','').replace(' ','')
        self._name                 = 'zhanku'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '站酷'
        self._site_name            = '站库'
        self._content              = cont
        self._author               = author
        self._channel              = '图片'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '0'
        self._from_source          = 'guangle'
        self._from_sources         = '["qiyu","guangle"]'
        vlist = self.value_to_list()
        if 'http://video.zcool.cn' not in str(self._content):
            return vlist,0,response.url



