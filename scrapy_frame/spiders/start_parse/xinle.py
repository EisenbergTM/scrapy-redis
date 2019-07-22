# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')


class xinle():
    def __init__(self):
        
        super(xinle,self).__init__()

    def extract(self,response):
        print(response.url)
        if 'http://sy.yzz.cn' in response.url:
            return self.parse_yzz(response)
        if 'www.huoxing24.com' in response.url:
            return self.parse_huoxingcaijing(response)
        if 'http://www.shouyou.com/' in response.url:
            return self.parse_shouyouwang(response)
        if 'https://new.qq.com/ch/ent/' in response.url:
            return self.parse_tengxunyule(response)
        if 'http://ent.163.com/' in response.url:
            return self.parse_wangyiyule(response)      
        if 'https://www.119you.com/news/' in response.url:
            return self.parse_119shouyou(response)
        if 'http://www.9game.cn/news/13_1/' in response.url:
            return self.parse_jiuyou(response)

    def parse_jiuyou(self,response):
        urllist = []
        li = response.xpath('//div[@class="title"]/h2/a/@href').extract()
        for i in li:
            urllist.append('http://www.9game.cn'+i)
        print(urllist)
        return urllist,0


    def parse_119shouyou(self,response):
        urllist = []
        li = response.xpath('//a[@class="u-title"]/@href').extract()
        for i in li:
            urllist.append('https://www.119you.com'+i)
        return urllist,0

    def parse_wangyiyule(self,response):
        urllist = []
        js = json.loads(response.body[14:-1].decode('utf-8','ignore'))
        for a in js:
            if 'http://ent.163.com/1' in a['docurl']:
                urllist.append(a['docurl'])
        print(urllist)
        return urllist,0

    def parse_tengxunyule(self,response):
        urllist = re.findall('"url":"(.+?)"',response.text)
        print(urllist)
        return urllist,0

    def parse_shouyouwang(self,response):   
        urllist = response.xpath('//span[@class="tit"]/a/@href').extract()
        return urllist,0
    
    def parse_yzz(self,response):
        urllist = response.xpath('//ul[@class="item-pt-list"]/li/div[2]/a/@href').extract()
        return urllist,0
 
    def parse_huoxingcaijing(self,response):
        urllist = response.xpath('//div[@class="index-news-list"]/a/@href').extract()
        return urllist,0


