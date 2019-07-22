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
from scrapy_frame.detail_extratct import model_detail

#code注释:0-nomal,1-shanxun-api,


# 创建一个爬虫类
class Slave1(RedisSpider):
    def __init__(self,*kargs,**kwargs):
        super(Slave1, self).__init__(*kargs,*kwargs)
        self.log         = scrapy_log(self.name)
        self.push        = redis_push()

    # 爬虫名
    name = 'slave1'
    # 允许爬虫作用的范围
    allowd_domains = [] 
    # 爬虫其实的url
    redis_key = 'scrapy_detail_urls'    
 
    def parse(self,response):
        print('=======================')
        if not response.status == 200:
            self.log.log_warning(response.status,response.url)
        else:
            try:
                item = ScrapyItem()
                url = ''
                u = model_detail(response)
              
                data  = u.select()
                item_value_list = data[0]
                code = data[1]
                print(code)
                if code == 0:
                    item = self.cal(item_value_list)
                    if item['_content'] != [] and item['_news_title'] != '':
                        yield item
                elif code == 1:
                    cycle = data[3]
                    for i in item_value_list:
                        item = self.cal(i)
                        if item['_content'] != [] and item['_news_title'] != '':
                            yield item
                    url = data[2] 
                    if cycle == 0:
                        self.push.push('scrapy_detail_urls',url)
                 

    
            except Exception:
                traceback.print_exc()
                self.log.log_error(traceback.format_exc(),response.url,'','','')

    def cal(self,item_value_list):
        item = ScrapyItem()
        item['_name']                   = item_value_list[0]
        item['_news_title']             = item_value_list[1]
        item['_pub_time']               = item_value_list[2]
        item['_create_time']            = item_value_list[3]
        item['_src_pub_time']           = item_value_list[4]
        item['_news_source']            = item_value_list[5]
        item['_site_name']              = item_value_list[6]
        item['_list_images']            = item_value_list[7]
        item['_content']                = item_value_list[8]
        item['_tags']                   = item_value_list[9]
        item['_id']                     = item_value_list[10]
        item['_up_count']               = item_value_list[11]
        item['_down_count']             = item_value_list[12]
        item['_comment_count']          = item_value_list[13]
        item['_is_hot']                 = item_value_list[14]
        item['_org_url']                = item_value_list[15]
        item['_cagetory']               = item_value_list[16]
        item['_sub_cagetory']           = item_value_list[17]
        item['_type']                   = item_value_list[18]
        item['_is_pass_directly']       = item_value_list[19]
        item['_is_high_video']          = item_value_list[20]
        item['_location']               = item_value_list[21]
        item['_attention']              = item_value_list[22]
        item['_channel']                = item_value_list[23]
        item['_author']                 = item_value_list[24]
        item['_image_size_type']        = item_value_list[25]
        item['_duration']               = item_value_list[26]
        item['_is_advertisement']       = item_value_list[27]
        item['_from_source']            = item_value_list[28]
        item['_topic']                  = item_value_list[29]
        item['_image_type']             = item_value_list[30]
        item['_num_src_list_images']    = item_value_list[31]
        item['_is_used_src_resource']   = item_value_list[32]
        item['_redirect_type']          = item_value_list[33]
        item['_is_auto_publish']        = item_value_list[34]
        item['_has_attachment']         = item_value_list[35]
        item['_third_id']               = item_value_list[36]
        item['_audio_url']              = item_value_list[37]
        item['_categories']             = item_value_list[38]
        item['_from_sources']           = item_value_list[39]
        item['_comment_list']           = item_value_list[40]
        return item
