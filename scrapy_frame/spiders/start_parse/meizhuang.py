# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')


class meizhuang():
    def __init__(self):
        
        super(meizhuang,self).__init__()

    def extract(self,response):
        if 'http://k.sina.com.cn/mediaDocList.d.html' in response.url:
            return self.parse_yulekandian(response)

    def parse_yulekandian(self,response):
        urllist = response.xpath('//a[@class="link-212121"]/@href').extract()
        return urllist,0


