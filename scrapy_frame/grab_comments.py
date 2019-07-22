# -*- coding: utf-8 -*-

import re
import os
import sys
import time
import random
import requests
import datetime
import json
from lxml import etree

class comment(object):
    def __init__(self):

        self._type        = 1
        self._comment     = ''
        self._up_count    = '0'
        self._reply_count = '0'
        self._post_time   = '0'
        self._location    = '{}'#{"province":"","city":"","district":""}
        self._user_name   = ''
        self._user_id     = '0'
        self._to_user_id  = '0'
        self._portrait    = ''

    def set_id(self):
        t = time.time()
        now_time = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        number = random.randint(0, 999999)
        rand_number = str(number).zfill(6)
        _id = str(now_time) + rand_number    
        
        return _id

    def comment_json(self):
        comment = '{"type":'+ str(self._type) +',"comment":"' + str(self._comment) + '","up_count":' + str(self._up_count) + ',"reply_count":' + str(self._reply_count)  + ',"post_time":' + str(self._post_time) + ',"comment_id":"' + self.set_id() + '","location":'+ str(self._location) +',"user":{"user_name":"' + str(self._user_name) + '","user_id":"' + str(self._user_id) + '","to_user_id":"' + str(self._to_user_id) + '","portrait":"' + str(self._portrait) + '"}},'
        return comment



    def get_comments(self,url,num,web_name):
        detail_id = ''
        if web_name == '今日头条':
            detail_id = re.search('\d+',url).group(0)
            return self.parse_jinritoutiao(detail_id,num)
        if web_name == '界面':
          
            detail_id = re.search('/(\d+?).html',url).group(1)
            return self.parse_jiemian(detail_id,num)
        if web_name == '搜狐':
            detail_id = re.search('\d+',url).group(0)
            return self.parse_sohu(detail_id,num)
        if web_name == '澎湃':
            detail_id = re.search('\d+',url).group(0)
            return self.parse_pengpai(detail_id,num)


    def parse_jinritoutiao(self,detail_id,num):
        jinritoutiao_headers = {'authority': 'www.toutiao.com',
                                'method': 'GET',
                                'path': '/api/comment/list/?group_id=6616123174557843971&item_id=6616123174557843971&count=50',
                                'scheme': 'https',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'zh-CN,zh;q=0.9',
                                'cache-control': 'max-age=0',
                                'cookie': 'tt_webid=6587558487722100228; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1651cbd28afa29-0046714cb652ab-5e442e19-100200-1651cbd28b0821; tt_webid=6587558487722100228; csrftoken=b4db1ea21f618562b3646f6b104fd176; uuid="w:b29cd9d32f104edd9d3f428b877cbe7b"; _ga=GA1.2.1746268479.1539164736; CNZZDATA1259612802=615777214-1533781554-https%253A%252F%252Fwww.baidu.com%252F%7C1540528945',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        url = 'https://www.toutiao.com/api/comment/list/?group_id=' + str(detail_id) +'&item_id=' + str(detail_id)  + '&count=' + str(num)
        js = json.loads(requests.get(url,headers = jinritoutiao_headers).content)
        comments = ''
        if 'comments' in str(js):
            for i in js['data']['comments']:
                self._comment     = str(i['text']).replace('\\','\\\\').replace('"','\\"').replace('\n','').replace('\r','')
                self._up_count    = str(i['digg_count'])
                self._reply_count = str(i['reply_count'])
                self._post_time   = str(int(i['create_time'])*1000)
                self._user_name   = str(i['user']['name'])
                self._user_id     = str(i['user']['user_id'])
                self._to_user_id  = str(detail_id)
                self._portrait    = str(i['user']['avatar_url'])

                comment = self.comment_json()
                comments += comment
            comments = '[' + comments[:-1] + ']'
        if comments == '':
            return '[]'
        else:
            return comments

    def jiemian_date(self,da_time):
        if '/' not in str(da_time):
            today    = datetime.date.today() + datetime.timedelta(days = 0)
            yestoday = datetime.date.today() + datetime.timedelta(days = -1)
            qiantian = datetime.date.today() + datetime.timedelta(days = -2)
            a = da_time.replace('今天',str(today)).replace('昨天',str(yestoday)).replace('前天',str(qiantian)).replace(' ','')
            tim = int(time.mktime(time.strptime(a,"%Y-%m-%d%H:%M"))*1000)
            return tim
        else:
            date = da_time.replace('/','-')
            a = str(time.localtime(time.time()).tm_year)+'-'+date
            tim = int(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M"))*1000)
            return tim


    def parse_jiemian(self,detail_id,num):
        url = 'https://a.jiemian.com/index.php?m=comment&a=getlistCommentP&aid=' + detail_id + '&comment_type=1&per_page=' + num
        js = json.loads(requests.get(url).content[12:-2])
        a =  etree.HTML(js['rs'])
        comments = ''
        up_count    = a.xpath('//span[@class="like"]/em/text()')
        reply_count = a.xpath('//span[@class="comment"]/em/text()')
        portrait    = a.xpath('///div[@class="jm-avatar"]/a/img/@src')
        pubtime     = a.xpath('//span[@class="date"]/text()')
        author      = a.xpath('//a[@class="author-name"]/text()')
        comment_id  = a.xpath('//dd[@class="comment-post"]/@id')
        commet      = a.xpath('//div[@class="comment-main"]/p/text()')
        for i in range(len(up_count)):
            self._comment     = commet[i].replace('\\','\\\\').replace('"','\\"').replace('\n','').replace('\r','')
            self._up_count    = up_count[i].replace('(','').replace(')','') 
            self._reply_count = reply_count[i].replace('(','').replace(')','')
            self._post_time   = self.jiemian_date(pubtime[i])
            self._user_name   = author[i]
            self._portrait    = portrait[i]
            comment = self.comment_json()
            comments += comment
        comments = '[' + comments[:-1] + ']'
        if comments == '':
            return '[]'
        else:
            print(comments)
            return comments

    def pengpai_id(self,url_list):
        user_id    = []
        comment_id = []
        for i in url_list:
            user_id.append(re.search('userId=(.+?)&',i).group(1))
            comment_id.append(re.search('commentId=(.+?)&',i).group(1))
        return user_id,comment_id

    def pengpai_date(self,date_sign):
        str_time = []
        for i in date_sign:
            if '天前' in str(i):
                day = re.search('\d+',str(date_sign)).group(1)
                print(day)
                str_time.append(int(time.mktime(time.strptime(str(datetime.date.today()-datetime.timedelta(days=int(day))), '%Y-%m-%d')))*1000) 
            else:
                str_time.append(int(time.mktime(time.strptime(str(datetime.date.today()), '%Y-%m-%d')))*1000)
        return str_time
        


    def parse_pengpai(self,detail_id,num):
        url = 'https://www.thepaper.cn/newDetail_commt.jsp?contid=' + detail_id
        html = requests.get(url).content
        a =  etree.HTML(html,parser=etree.HTMLParser(encoding='utf-8'))
        comments = ''
        up_count    = a.xpath('//div[@class="ansright_time"]/a[1]/text()')
        portrait    = a.xpath('///div[@class="ansleft_hdimg"]/a/img/@src')
        pubtime     = self.pengpai_date(a.xpath('//div[@class="aqwright"]/h3/a/text()'))
        author      = a.xpath('//div[@class="aqwright"]/h3/a/text()')
        comment_id  = self.pengpai_id(a.xpath('//div[@class="aqwright"]/h3/a/@href'))[1]
        user_id     = self.pengpai_id(a.xpath('//div[@class="aqwright"]/h3/a/@href'))[0]
        commet      = a.xpath('//div[@class="ansright_cont"]/a/text()')
        for i in range(len(up_count)):
            self._comment     = str(commet[i]).replace('\n','').replace('\t','').replace(' ','')
            self._up_count    = up_count[i]
            self._post_time   = pubtime[i]
            self._user_name   = str(author[i]).replace('\n','').replace('\t','').replace(' ','')
            self._portrait    = 'https:'+portrait[i]
            comment = self.comment_json()
            comments += comment
        comments = '[' + comments[:-1] + ']'
        if comments == '':
            return '[]'
        else:
            return comments

    def sohu_location(self,location):
        print(location) 
        a = ''
        if location == '':
            return '{}'
        if '省' not in str(location) and '市' not in str(location) and '区' not in str(location):
            return '{"province":"'+str(location)+'","city":"","district":""}'

        loc_list = ['省','市','区']
        
        for i in loc_list:
            
            if i in str(location):
                province = location.split(i)[0]+i
                city     = location.split(i)[1]
                a = '{"province":"'+str(province)+'","city":"'+str(city)+'","district":""}'
        
                return a

    def parse_sohu(self,detail_id,num):
        comments = ''
        url = 'http://apiv2.sohu.com/api/topic/load?page_size=50&source_id=mp_'+str(detail_id)
        html = requests.get(url).content
        js = json.loads(html)
        if js['jsonObject']['comments'] != []:
            for i in js['jsonObject']['comments']:
                self._comment     = str(i['content']).replace('\\','\\\\').replace('"','\\"').replace('\n','').replace('\r','')
                self._up_count    = str(i['support_count'])
                self._reply_count = str(i['reply_count'])
                self._post_time   = str(i['create_time'])
                self._user_name   = str(i['passport']['nickname'])
                self._user_id     = str(i['passport']['user_id'])
                self._location    = self.sohu_location(i['ip_location'])
                self._to_user_id  = str(detail_id)
                self._portrait    = str(i['passport']['img_url'])

                comment = self.comment_json()
                comments += comment
            comments = '[' + comments[:-1] + ']'
        if comments == '':
            return '[]'
        else:
            return comments
 


if __name__=='__main__':
    a = comment()
    #a.get_comments('https://www.toutiao.com/a6618649596069413390/','50','今日头条')
    a.get_comments('https://www.jiemian.com/article/2585014.html','50','界面')
    #a.get_comments('https://www.thepaper.cn/newsDetail_forward_2585461','50','澎湃')
    #a.get_comments('2585461','50','澎湃')
    #a.get_comments('272430442','50','搜狐')









