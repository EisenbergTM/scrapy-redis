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


class xinle(value):
    def __init__(self):
        
        super(xinle,self).__init__()

    def extract(self,response):
        if 'http://sy.yzz.cn/news' in response.url:
            return self.parse_yzz(response)
        if 'www.huoxing24.com/newsdetail/' in response.url:
            return self.parse_huoxingcaijing(response)
        if 'http://news.17173.com' in response.url:
            return self.parse_shouyouwang(response)
        if 'https://new.qq.com' in response.url:
            return self.parse_tengxun(response)
        if 'http://ent.163.com/1' in response.url:
            return self.parse_wangyiyule(response)
        if 'http://www.9game.cn' in response.url:
            return self.parse_jiuyou(response)
        if 'https://www.119you.com' in response.url:
            return self.parse_119shouyou(response)
    
    def parse_jiuyou(self,response):
        cont = ''
        title    = response.xpath('//div[@class="page-header"]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="post-content"]').extract()[0]
        pubtime  = response.xpath('//p[@class="meta"]/span[3]/text()').extract()[0].replace('发表时间：','')
        pubtime = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M:%S"))*1000)
 
        self._name                 = 'jiuyou'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '九游手游'
        self._site_name            = '九游手游'
        self._content              = cont
        self._pubtime              = pubtime
        self._channel              = '手游'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_119shouyou(self,response):
        title    = response.xpath('//h3[@class="u-article-title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="m-article-detail-box"]').extract()[0]
        
        self._name                 = '119shouyou'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '119手游'
        self._site_name            = '119手游'
        self._content              = cont
        self._channel              = '手游'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_wangyiyule(self,response):
        cont = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="post_text"]/p').extract()
        for p in content:
            cont += p

        self._name                 = 'wangyiyule'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '网易娱乐'
        self._site_name            = '网易娱乐'
        self._content              = cont
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()
        return vlist,0,response.url



    def parse_tengxun(self,response):
        cont = ''
        title    = response.xpath('//div[@class="LEFT"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="content-article"]/p').extract()
        for p in content:
            cont += p
        tags     = []
        tag_cont = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
        for i in tag_cont.split(','):
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'tengxun'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '腾讯娱乐'
        self._site_name            = '腾讯娱乐'
        self._content              = cont
        self._channel              = '娱乐'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_shouyouwang(self,response):
        title   = response.xpath('//h1[@class="gb-final-tit-article"]/text()').extract()[0]
        cont    = response.xpath('//div[@id="mod_article"]').extract()[0]
        #cont = cont.replace('再逛逛>>','')
        pt      = response.xpath('//span[@class="gb-final-date"]/text()').extract()[0]
        pubtime = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M:%S"))*1000)
        self._name                 = 'shouyouwang'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '手游网'
        self._site_name            = '手游网'
        self._content              = cont
        self._channel              = '手游'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()

        return vlist,0,response.url
    
    def parse_yzz(self,response):
        title   = response.xpath('//h2[@class="tit"]/text()').extract()[0]
        cont    = response.xpath('//div[@class="content"]/table/tr/td').extract()[0]
        #pubtime = int(time.mktime(time.strptime(pt,"%Y-%m-%d"))*1000)
        pubtime = int(round(time.time())*1000)
        author  = response.xpath('//div[@class="editor"]/text()').extract()[0]
        for i in author.split('：'):
            author = i[:-1]
        self._name                 = 'yezizhu'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '叶子猪'
        self._site_name            = '叶子猪'
        self._content              = cont
        self._channel              = '手游'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle"]'
        vlist = self.value_to_list()

        return vlist,0,response.url
 

    def parse_huoxingcaijing(self,response):
        content = ''
        title     = response.xpath('//div[@class="text-header"]/h1/text()').extract()[0]
        cont      = response.xpath('//div[@class="detail-text-cont simditor-body"]/div/p | //div[@class="detail-text-cont simditor-body"]/div/blockquote').extract()
        for i in cont:
            content += i
        content = content.replace('<b>','').replace('</b>','').replace('文章声明：本文为火星财经专栏作者作品，不代表火星财经观点，','').replace('版权归作者所有，','').replace('如需转载，请提前联系作者','').replace('或注明出处。','')
        tag      = response.xpath('//div[@class="keyword"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'huoxingcaijing'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '火星财经'
        self._site_name            = '火星财经'
        self._content              = content
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '财经'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'xinle'
        self._from_sources         = '["qiyu","xinle","blocklover","mcjys"]'
        vlist = self.value_to_list()

        return vlist,0,response.url



