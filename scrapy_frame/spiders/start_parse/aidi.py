# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')


class aidi():
    def __init__(self):
        
        super(aidi,self).__init__()

    def extract(self,response):
        if 'http://news.xiancity.cn/index.shtml' in response.url:
            return self.parse_xianwangxinwen(response)
        if 'http://www.xasqw.com/web/items.aspx?' in response.url:
            return self.parse_xianjiaodianxinwen(response)
        if 'http://news.xiancn.com/node_10490.htm' in response.url:
            return self.parse_xianxinwenwang(response)
        if 'http://www.xashangwang.com/html/swtt/' in response.url:
            return self.parse_xianshangwangtoutiao(response)
       

    def parse_xianwangxinwen(self,response):
        urllist = response.xpath('//div[@class="xw_dep4"]/span/a/@href').extract()
        print(urllist)
        return urllist,0

    def parse_xianjiaodianxinwen(self,response):
        urllist = []
        li = response.xpath('//div[@class="m1n0"]/a/@href').extract()
        for i in li:
            urllist.append('http://www.xasqw.com'+i)
        print(urllist)
        return urllist,0

    def parse_xianxinwenwang(self,response):
        urllist = []
        li = response.xpath('//div[@class="headline"]/a/@href | //div[@class="artlist"]/a/@href').extract()
        for i in li:
            urllist.append('http://news.xiancn.com/'+i)
        print(urllist)
        return urllist,0

    def parse_xianshangwangtoutiao(self,response):
        urllist = response.xpath('//div[@class="list_show"]/h2/a/@href').extract()
        print(urllist)
        return urllist,0













