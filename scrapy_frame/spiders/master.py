# -*- coding: utf-8 -*-

import re
import os
import sys
import time
import json
import scrapy
import random
import datetime
import requests
import traceback
import configparser
sys.path.append('../../../scrapy_frame')
from scrapy_frame.items import ScrapyItem
from scrapy_redis.spiders import RedisSpider
from scrapy_frame.log import scrapy_log
from scrapy_frame.redis_push import redis_push
from scrapy_frame.start_extract import model

# 创建一个爬虫类
class Master(RedisSpider):
    def __init__(self,*kargs,**kwargs):
        super(Master, self).__init__(*kargs,*kwargs)
        self.log         = scrapy_log(self.name)
        self.rds         = redis_push()


    # 爬虫名
    name = 'master'
    # 允许爬虫作用的范围
    allowd_domains = [] 
    # 爬虫其实的url
    redis_key = 'scrapy_start_urls'    
 
    def parse(self,response):
        print('=======================')
        if not response.status == 200:
            self.log.log_warning(response.status,response.url)
        else:
            try:
                u = model(response)  
                url   = u.select()[0]
                code  = u.select()[1]
                if code == 0:
                    if type(url) == list:
                        print('==============================================================================================================')
                        for i in url:
                            self.rds.push('scrapy_detail_urls',i)
                #东九
                elif code == 2:
                    duration_list = u.select()[2]
                    for i in range(len(url)):
                        self.rds.push('scrapy_detail_urls',url[i])
                        self.rds.set_key(url[i],duration_list[i])
                        self.rds.r.expire(url[i],600)
              

            except Exception:
                traceback.print_exc()
                log.log_error(traceback.format_exc(),url,'','','')




