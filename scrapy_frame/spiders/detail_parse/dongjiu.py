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
from scrapy_frame.probe_address import ProbeAdress
from scrapy_frame.query_realtime import Query_realtime

class dongjiu(value):
    def __init__(self):
        
        super(dongjiu,self).__init__()
        #self.rds      = redis.Redis(host='10.30.180.221',port=16379,password='xdrt@^oasdfasf=<',db=0)
        self.rds      = redis.Redis(host='118.190.243.148',port=16379,password='xdrt@^oasdfasf=<',db=0)

    def extract(self,response):
        print(response.url)
        if 'https://v.douyu.com/show/' in response.url:
            return self.parse_douyu(response)
    
    def parse_douyu(self,response):
        duration = self.rds.get(response.url).decode('utf-8')
        title    = response.xpath('//div[@class="video-title"]/h1/text()').extract()[0]
        pubtime  = response.xpath('//span[@class="video-publish-date"]/text()').extract()[0]
        tag     = response.xpath('//a[@class="video-cate"]/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        if re.search('\d+-\d+-\d+',pubtime) == None:
           pubtime = round(time.time()*1000)
        else:
           pubtime  = re.search('\d+-\d+-\d+',pubtime).group()
           pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d"))*1000)
        duration = str(duration).split(':')
        duration = int(duration[0])*60+int(duration[1])
        query = Query_realtime('dongjiu')
        js = query.query_message()
        probe = ProbeAdress()
        play_url = probe.query_play_address(3,response.url)
        print(play_url)

        self._name                 = 'douyu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '斗鱼视频'
        self._site_name            = '斗鱼视频'
        self._content              = play_url
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '游戏'
        self._cagetory             = '游戏'
        self._type                 = '3'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._duration             = str(self.default_zero(str(duration)))
        self._from_source          = 'dongjiu'
        self._from_sources         = '["qiyu","dongjiu"]'
        vlist = self.value_to_list()
        if int(js['current_grab_video']) < int(js['grab_videos_day']) and int(self._duration) <= int(js['max_video_duration']):
            return vlist,0,response.url
        else:
            return [],0,[]

    def default_zero(self,data):
        if data == '' or data == None:
            return '0'
        else:
            return data
