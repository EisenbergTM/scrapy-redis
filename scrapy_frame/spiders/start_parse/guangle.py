# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')


class guangle():
    def __init__(self):
        
        super(guangle,self).__init__()

    def extract(self,response):
        if 'https://www.zcool.com.cn/discover/0!0!0!0!0!!!!-1!0!1' in response.url:
            return self.parse_zhanku(response)

    def parse_zhanku(self,response):
        urllist = response.xpath('//div[@class="card-img"]/a/@href').extract()
        print(urllist)
        return urllist,0



