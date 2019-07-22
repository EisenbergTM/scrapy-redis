# -*- coding:utf-8 -*-

import os
import time
import redis




class redis_push():
    def __init__(self):
        # 将start_url 存储到redis中的redis_key中，让爬虫去爬取
        self.redis_Host = "118.190.243.148"
 
        # 创建redis数据库连接
        self.pool = redis.ConnectionPool(host='118.190.243.148',port='16379',password='xdrt@^oasdfasf=<')
        #self.pool = redis.ConnectionPool(host='10.30.180.221',port='16379',password='xdrt@^oasdfasf=<')
        self.r = redis.Redis(connection_pool=self.pool)
        #flushdbRes = self.r.flushdb()

    def push(self,redis_key,url):
        # 先将redis中的requests全部清空
        #flushdbRes = self.r.flushdb()
        #print(f"flushdbRes = {flushdbRes}")
        self.r.lpush(redis_key, url)
    
    def query(self,key):
        a = self.r.get(key)
        if a != None:
            print(self.r.get(key).decode('utf-8'))
            return a.decode('utf-8')
        else:
            return None


    def set_key(self,key_name,value):
        self.r.set(key_name,value)

    def set_key_addtime(self,key_name,value,time):
        self.r.set(key_name,value.encode('utf-8'),time)



def shanxun():
    print('pushing-shanxun')
    _id = rds.query('shanxun')
    if _id == None:
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/sx.txt','r')
        a = p.read()
        error = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/sx_error.txt','a')
        error.write(_id+'\n')
        error.close()
        _id = a.split(':')[0]
        rds.push('scrapy_detail_urls','http://www.yzpai.cn/news/out/article?lastid='+_id+'&count=50&time=1532597459&sign=4A8E5794C130D752673FF768381E59F3')
    else:
        print(_id)
        rds.push('scrapy_detail_urls','http://www.yzpai.cn/news/out/article?lastid='+_id+'&count=50&time=1532597459&sign=4A8E5794C130D752673FF768381E59F3')
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/sx.txt','w')
        p.write(_id+':shanxun_id;')
        p.close()
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/Log_sx.txt','a')
        p.write(_id+':shanxun_id;')
        p.close()
    time.sleep(1800)


if __name__=='__main__':
    rds = redis_push()
    while True:
        shanxun()
    time.sleep(2)
    os._exit(0)
    
   
