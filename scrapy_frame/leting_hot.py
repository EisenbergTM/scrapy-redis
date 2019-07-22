import os
import time
import requests
import redis
import traceback
from redis_push import redis_push
from find_id import BloomFilter
import random
import json

class sync_leting():
    def __init__(self):

        self.redis_url   = '118.190.243.148|16379|xdrt@^oasdfasf=<|7'
        self.bf          = BloomFilter('shanxun', self.redis_url, [5, 7, 13, 17, 23])
        self.reds        = redis_push()

    def query_redis(self,url):
        if self.bf.isContains(str(url)):
            print('exist')
            return 'exist'
        else:
            print('ok')
            print('-------------------------------------------------------------------------------')
            self.bf.insert(str(url))
            return 'ok'



    def leting_hot(self):

        try:
            print('last_hot_id:',self.reds.query('last_hot_id'))
            query_url = 'http://10.66.181.119:9200/nm_*/_search'
            query_headers = {'Content-Type':'application/json;charset=UTF-8'}
            hot_ids = []
            last_hot_id = self.reds.query('last_hot_id')
            token = self.reds.query('leting_headers')
            leting_url = 'https://app.leting.io/c/get_hot_tags?log_id=1234'
            leting_headers = {"uid":"12345","token":str(token)}
            html = requests.get(leting_url,headers=leting_headers)
            print(html.json())
            for i in html.json()['data']['data']:
                print(i,type(i))
                a = i['sync_id']
                if self.query_redis('leting_hot'+str(i['sync_id'])) == 'ok':
                    query_str = '{"query":{"bool":{"must":[{"term":{"third_id":"'+str(a)+'"}}]}}}'
                    html = requests.get(query_url,data=query_str.encode('utf-8'),headers=query_headers)
                    for i in html.json()['hits']['hits']:
                        hot_ids.append(i['_id'])
                    self.reds.set_key('last_hot_id',str(a))
            req_str = ''
            a = str(time.localtime(time.time()).tm_year)+str(time.localtime(time.time()).tm_mon)
            now_month = 'nm_' + a[2:]
            if hot_ids != []:
                for i in hot_ids:
                    req_str += '{ "update" : {"_id" : "'+str(i)+'", "_type" : "news","_index":"'+str(now_month)+'"} }\n { "doc" : {"is_hot" : 1},"detect_noop":false }\n'
                print(req_str)
                url = 'http://10.66.181.119:9200/_bulk'
                html = requests.post(url,data=req_str.encode('utf-8'),headers=query_headers)
                print(html.json())
        except BaseException:
            print('error')
            traceback.print_exc()

    def leting_sync(self):
        try:
           pub_time = self.reds.query('leting')
           if pub_time == None:
               p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','r')
               a = p.read()
               error = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt_error.txt','a')
               error.write(_id+'\n')
               error.close()
               self.reds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')
           else:
               self.reds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')
               p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','w')
               p.write(pub_time+':leting_pubtime')
               p.close()
               p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/Log_lt.txt','a')
               p.write(pub_time+':leting_pubtime'+'\n')
               p.close()
        except BaseException:
            print('error')
            traceback.print_exc()


if __name__=='__main__':
    a = sync_leting()
    while True:
        time.sleep(1)
        p = time.localtime(time.time()).tm_sec
        if p%10 == 0:
           #print(p,p/10)
           a.leting_hot()
           a.leting_sync() 
    #a.leting_sync() 

