# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import re
import sys
import json
import time
import random
import scrapy
from scrapy import signals
from scrapy_frame.redis_push import redis_push

class ScrapyFrameSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyFrameDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #header = '{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36","Content-Type":"pplication/x-www-form-urlencoded","Cookie":"UBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5F-zMQkXjLcWigTIELCP--; SINAGLOBAL=2894048341379.66.1527646318554; SUB=_2AkMs-sZtf8NxqwJRmP4QzWjra4t-ywHEieKapje2JRMxHRl-yj83qkMYtRB6B3rogqcMnNHGiyvtLq_d9cBl7YieLqg3; YF-Page-G0=5c7144e56a57a456abed1d1511ad79e8; _s_tentry=-; Apache=2427440948739.0703.1538116802783; ULV=1538116802821:14:3:1:2427440948739.0703.1538116802783:1537623583081; YF-V5-G0=9717632f62066ddd544bf04f733ad50a; UOR=finance.ifeng.com,widget.weibo.com,www.megoal.org"}'
        #cookie = {'UBP':'0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5F-zMQkXjLcWigTIELCP--','SINAGLOBAL':'2894048341379.66.1527646318554', 'SUB':'_2AkMs-sZtf8NxqwJRmP4QzWjra4t-ywHEieKapje2JRMxHRl-yj83qkMYtRB6B3rogqcMnNHGiyvtLq_d9cBl7YieLqg3', 'YF-Page-G0':'5c7144e56a57a456abed1d1511ad79e8', '_s_tentry':'-', 'Apache':'2427440948739.0703.1538116802783', 'ULV':'1538116802821:14:3:1:2427440948739.0703.1538116802783:1537623583081', 'YF-V5-G0':'9717632f62066ddd544bf04f733ad50a', 'UOR':'finance.ifeng.com,widget.weibo.com,www.megoal.org'}
        #request.headers = header
        #request.cookies = cookie
        #print(request.method)
        #print(request.headers)
        '''
        count = 0
        for count,l in enumerate(open('/home/mitian/mitian_scrapy-redis/scrapy_frame/scrapy_frame/proxies.txt','r')):
            count += 1
        line = random.randint(0,count-1)
        f = open('/home/mitian/mitian_scrapy-redis/scrapy_frame/scrapy_frame/proxies.txt','r').readlines()[line]
        ip = re.sub('\n','',f)
        print("this is ip:"+ip)
        request.meta["proxy"]=ip
        '''
        if 'https://app.leting.io/c/sync_data?' in request.url:
            rds        = redis_push()
            token      = rds.query('leting_headers')
            headers    = '{"uid":"12345","token":"'+ token +'"}'
            print(headers)
            #request.headers = eval(headers)
            request.headers['uid'] = 12345
            request.headers['token'] = token
            #request.method = 'post'
            #return request

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        print(response.status)
        print(response.url)
        #if response.status != 200:
            #request.meta["proxy"]='https://124.200.104.234:47076'
        #    ip = self.get_proxy_ip()
        #    request.meta["proxy"]= ip
        #    return request
        if 'https://www.toutiao.com/api/pc/feed/?' in response.url and response.body.decode('utf-8') == '{"message": "error", "data": [], "has_more": false}':
            request.headers = {'authority': 'www.toutiao.com',
               'method': 'GET',
               'path': '/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1358B1D31C6653&cp=5BD1B676D5A33E1&_signature=dMRbyhAQLxje6xtKM62xTXTEW9',
               'scheme': 'https',
               'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9',
               'content-type': 'application/x-www-form-urlencoded',
               'cookie': 'tt_webid=6587558487722100228; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1651cbd28afa29-0046714cb652ab-5e442e19-100200-1651cbd28b0821; tt_webid=6587558487722100228; csrftoken=b4db1ea21f618562b3646f6b104fd176; uuid="w:b29cd9d32f104edd9d3f428b877cbe7b"; _ga=GA1.2.1746268479.1539164736; _gid=GA1.2.1194639724.1540439783; __tasessionId=c3783oads1540445595536; CNZZDATA1259612802=615777214-1533781554-https%253A%252F%252Fwww.baidu.com%252F%7C1540447945',
               'referer': 'https://www.toutiao.com/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
               'x-requested-with': 'XMLHttpRequest'}
            time.sleep(2)
            return request

        if 'https://app.leting.io/c/sync_data?' in response.url:
            js = json.loads(response.body)
            if js['code'] == 401 or js['code'] == '401':
                rds        = redis_push()
                token      = rds.query('leting_headers')
                headers    = '{"uid":"12345","token":"'+ token +'"}'
                print(headers)
                request.headers = eval(headers)
                #return request

        return response

    def get_proxy_ip(self):
        count = 0
        for count,l in enumerate(open('/home/mitian/mitian_scrapy-redis/scrapy_frame/scrapy_frame/proxies.txt','r')):
            count += 1
        line = random.randint(0,count-1)
        f = open('/home/mitian/mitian_scrapy-redis/scrapy_frame/scrapy_frame/proxies.txt','r').readlines()[line]
        ip = re.sub('\n','',f)
        print("this time's ip:"+ip)
        return ip


    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
