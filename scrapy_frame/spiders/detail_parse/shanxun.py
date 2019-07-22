# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.find_id import BloomFilter
from scrapy_frame.value import value


class shanxun(value):
    def __init__(self):
        
        super(shanxun,self).__init__()
        #self.rds = redis.Redis(host='10.30.180.221',port=16379,password='xdrt@^oasdfasf=<',db=0)
        self.rds = redis.Redis(host='118.190.243.148',port=16379,password='xdrt@^oasdfasf=<',db=0)
        #self.redis_url   = '10.30.180.221|16379|xdrt@^oasdfasf=<|7'
        self.redis_url   = '118.190.243.148|16379|xdrt@^oasdfasf=<|7'
        self.bf          = BloomFilter('shanxun', self.redis_url, [5, 7, 13, 17, 23])

    def extract(self,response):
        last_id = str(response.url).replace('http://www.yzpai.cn/news/out/article?lastid=','').replace('&count=50&time=1532597459&sign=4A8E5794C130D752673FF768381E59F3','')
        data_list = []
        value_list = []
        title = ''
        num = ''
        self.js = json.loads(response.text)
        if self.js['data'] != [] and last_id != '' and int(last_id) > 0:
            for a in self.js['data']:
                
                num = str(a['id'])
                if a['title'] == '':
                    title = a['description'].replace('\n','')
                else:
                    title = a['title']
                if a['description'] == '':
                    content = self.get_content_shanxun(title,a['pic_urls'])[0]
                else:
                    content = self.get_content_shanxun(a['description'],a['pic_urls'])[0]
                if self.query_redis(a['rec_url']) == 'ok': 
                    self._name                 = 'shanxun'
                    self._news_title           = title
                    self._pub_time             = str(a['posttime']*1000)
                    self._src_pub_time         = str(a['posttime']*1000)
                    self._news_source          = a['source_site']
                    self._site_name            = a['source_site']
                    self._content              = content
                    self._id                   = str(a['id'])
                    self._org_url              = a['rec_url']
                    self._cagetory             = self.get_cagetory_from_num(a['topic_category_id'])
                    self._type                 = self.tp(a['type'])
                    self._is_pass_directly     = '1'
                    self._channel              = a['topic_name']
                    self._from_source          = 'shanxun'
                    self._from_sources         = '["shanxun"]'
                    self._topic                = a['topic_name']
                    self._image_type           = self.get_content_shanxun(a['description'],a['pic_urls'])[2]
                    self._num_src_list_images  = self.get_content_shanxun(a['description'],a['pic_urls'])[1]
                    self._is_used_src_resource = '1'
                    value_list = self.value_to_list()
                    data_list.append(value_list)
            self.rds.set('shanxun',num)
            url = 'http://www.yzpai.cn/news/out/article?lastid='+num+'&count=50&time=1532597459&sign=4A8E5794C130D752673FF768381E59F3'
            return data_list,1,url,0
        else:
            return value_list,1,response.url,1


 
    def tp(self,i):
        if i < 3:
            return 1
        elif i == 3:
            return 3

    def get_cagetory_from_num(self,num):
        cagetory = ""
        if num == 0:
            cagetory = "推荐"
        elif num == 1:
            cagetory = "动漫"
        elif num == 2:
            cagetory = "体育"
        elif num == 3:
            cagetory = "游戏"
        elif num == 4:
            cagetory = "财经"
        elif num == 5:
            cagetory = "科技"
        elif num == 6:
            cagetory = "趣味"
        elif num == 7:
            cagetory = "文化"
        elif num == 8:
            cagetory = "音乐"
        elif num == 9:
            cagetory = "生活"
        elif num == 10:
            cagetory = "资讯"
        elif num == 11:
            cagetory = "娱乐"
        elif num == 12:
            cagetory = "搞笑"
        elif num == 13:
            cagetory = "时尚"
        elif num == 14:
            cagetory = "视频"
        elif num == 15:
            cagetory = "留学"
        elif num == 16:
            cagetory = "读书"
        elif num == 17:
            cagetory = "书讯"
        elif num == 30:
            cagetory = "健康美容"
        elif num == 31:
            cagetory = "教育"
        else:
            cagetory = "资讯"
   
          
        return cagetory

    def default_zero(self,data):
        if data == '' or data == None:
            return '0'
        else:
            return data


    def get_content_shanxun(self,text,images):
        image_num   = 0
        image_type  = ''
        list_image  = []
        list_width  = []
        list_height = []
        text = text.replace(' ','').replace('\n','').replace('\t','').replace('\r','')
        data = "{\"type\":\"text\",\"data\":\"" + text + "\"},"
        if images != '':
            j = json.loads(str(images))

            for n in j:
                list_image.append(n['big'])
                list_width.append(n['width'])
                list_height.append(n['height'])
            image_num = len(list_image)
            if image_num<3 and image_num>0:
               data += "{\"type\":\"img\",\"data\":\"" + str(list_image[0]) +"\",\"width\":\"" + str(list_width[0]) + "\",\"height\":\"" + str(list_height[0]) + "\"},"
            if image_num > 3:
                i = 0
                while i < 3:
                    data += "{\"type\":\"img\",\"data\":\"" + str(list_image[i]) +"\",\"width\":\"" + str(list_width[i]) + "\",\"height\":\"" + str(list_height[i]) + "\"},"
                    i += 1
        data =  "[" + data[:len(data) - 1] + "]"
        if '.gif' in data or '.GIF' in data:
            if '.jpg' not in data and '.png' not in data and '.JPG' not in data and '.PNG' not in data:
                image_type = 'gif'
            if '.jpg' in data or '.png' in data and '.JPG' in data or '.PNG' in data:
                image_type = 'gif_jpg'
        else:
            image_type = 'jpg'
        if image_num == 0:
            image_type = ''
        #print(data)           
        return data,image_num,image_type

    def query_redis(self,url):
        if self.bf.isContains(str(url)):
            print('exist')
            return 'exist'
        else:
            print('ok')
            print('-------------------------------------------------------------------------------')
            self.bf.insert(str(url))
            return 'ok'     


