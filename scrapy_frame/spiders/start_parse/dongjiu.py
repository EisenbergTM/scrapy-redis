# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.query_realtime import Query_realtime


class dongjiu():
    def __init__(self):
        
        super(dongjiu,self).__init__()

    def extract(self,response):
        if 'https://v.douyu.com/directory/catelist' in response.url:
            return self.parse_douyu(response)
    
    def parse_douyu(self,response):
        urllist      = []
        durationlist = []
        query = Query_realtime('dongjiu')
        js = query.query_message()
        if int(js['current_grab_video']) < int(js['grab_videos_day']) :
            urllist      = response.xpath('//div[@class="list clearfix"]/a/@href').extract()
            durationlist = response.xpath('//div[@class="list clearfix"]/a/span[1]/b/text()').extract()
            return urllist,2,durationlist
        else:
            return [],0
 



