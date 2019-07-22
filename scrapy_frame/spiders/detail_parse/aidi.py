# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import requests
import random
import datetime
sys.path.append('../../scrapy_frame')
from bs4 import BeautifulSoup
from scrapy_frame.value import value


class aidi(value):
    def __init__(self):
        
        super(aidi,self).__init__()

    def extract(self,response):
        if 'http://news.xiancity.cn' in response.url:
            return self.parse_xianwangxinwen(response)
        if 'http://www.xasqw.com' in response.url:#西安社区焦点
            return self.parse_xianshequjiaodian(response)
        if 'http://news.xiancn.com' in response.url:#西安新闻网
            return self.parse_xianxinwenwang(response)
        if 'http://www.xashangwang.com' in response.url:#西安网商头条
            return self.parse_xianwangshangtoutiao(response)


    def xianxinwenwang(self,response):
        cont = ''
        if 'news_more_page_div_id' in str(response.body):
            urllist = response.xpath('//div[@id="news_more_page_div_id"]/a/@href').extract()
            last_url = urllist[len(urllist)-1]
            print(last_url)
            num = re.search('_(\d+?)\.',last_url).group(1)
            print(int(num))
            for i in range(int(num)):
                url = ''
                if i < 10:
                    url = response.url[:-6] + '_0' + str(i+1) + '.shtml'
                else:
                    url = response.url[:-6] + '_' + str(i+1) + '.shtml'
                print(url)
                html = requests.get(url).content
                soup = BeautifulSoup(html,'html.parser')
                for i in soup.find_all('div',id="artical"):
                    for p in i.find_all('p',class_="f-name"):
                        i = str(i).replace(str(p),'')
                    cont += i
        else:
           cont = response.xpath('//div[@id="artical"]').extract()[0]
        return cont
     
    def parse_xianshequjiaodian(self,response):

        title    = response.xpath('//div[@class="m1t1"]/text()').extract()[0]
        cont     = response.xpath('//div[@id="m0b3"]').extract()[0]
        self._name                 = 'xianshequjiaodian'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '西安社区焦点'
        self._site_name            = '西安社区焦点'
        self._content              = cont
        self._channel              = '社区'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '0'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu","aidi"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_xianxinwenwang(self,response):

        title    = response.xpath('//div[@class="biaoti"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="content"]').extract()[0]
        pubtime  = response.xpath('//div[@class="mess"]/text()').extract()[0]
        a = re.search('(\d+-\d+-\d+\s\d+:\d+)',pubtime).group(1)
        pubtime  = int(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M"))*1000)
        self._name                 = 'xianxinwenwang'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '西安新闻网'
        self._site_name            = '西安新闻网'
        self._content              = cont
        self._channel              = '新闻'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '0'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu","aidi"]'
        vlist = self.value_to_list()
        return vlist,0,response.url
        
    def parse_xianwangshangtoutiao(self,response):

        title    = response.xpath('//div[@class="insideL"]/h2/text()').extract()[0]
        cont     = response.xpath('//div[@class="showcontent"]').extract()[0]
        author   = response.xpath('//div[@class="copyfrom"]/text()').extract()[0]
        for i in author.split('：'):
            author = i
        pubtime  = response.xpath('//div[@class="copyfrom"]/text()').extract()[0]
        a = re.search('(\d+-\d+-\d+\s\d+:\d+:\d+)',pubtime).group(1)
        pubtime  = int(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))*1000)
        self._name                 = 'xianwangshangtoutiao'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '西安网商头条'
        self._site_name            = '西安网商头条'
        self._content              = cont
        self._author               = author
        self._channel              = '网商'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '0'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu","aidi"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_xianwangxinwen(self,response):
       
        title    = response.xpath('//h2[@id="newstitle"]/text()').extract()[0]
        cont     = self.xianxinwenwang(response)
        author   = response.xpath('//p[@class="f-name"]/span/text()').extract()[0]
        a        = response.xpath('//div[@class="note"]/span[2]/span/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M"))*1000)
        self._name                 = 'xianwangxinwen'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '西安网新闻'
        self._site_name            = '西安网新闻'
        self._content              = cont
        self._author               = author
        self._channel              = '新闻'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '0'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu","aidi"]'
        vlist = self.value_to_list()
        return vlist,0,response.url



