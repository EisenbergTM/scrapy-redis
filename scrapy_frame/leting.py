# -*- coding:utf-8 -*-

import os
import time
import redis
from redis_push import redis_push






if __name__=='__main__':
    rds = redis_push()
    pub_time = rds.query('leting')
    if pub_time == None:
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','r')
        a = p.read()
        error = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt_error.txt','a')
        error.write(_id+'\n')
        error.close()
        #rds.push('scrapy_start_urls','https://app.leting.io/auth?uid=12345&appid=8f5a691127c89465e44e3b195e588f05&app_secret=7c39c2f62a33ab61437fcd6e9e5c8be3&log_id=1234')
        rds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')
       
    else:
        rds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')
        #rds.push('scrapy_start_urls','https://app.leting.io/auth?uid=12345&appid=8f5a691127c89465e44e3b195e588f05&app_secret=7c39c2f62a33ab61437fcd6e9e5c8be3&log_id=1234')
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','w')
        p.write(pub_time+':leting_pubtime')
        p.close()
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/Log_lt.txt','a')
        p.write(pub_time+':leting_pubtime'+'\n')
        p.close()
    time.sleep(30)
    pub_time = rds.query('leting')
    if pub_time == None:
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','r')
        a = p.read()
        error = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt_error.txt','a')
        error.write(_id+'\n')
        error.close()
        #rds.push('scrapy_start_urls','https://app.leting.io/auth?uid=12345&appid=8f5a691127c89465e44e3b195e588f05&app_secret=7c39c2f62a33ab61437fcd6e9e5c8be3&log_id=1234')
        rds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')

    else:
        rds.push('scrapy_detail_urls','https://app.leting.io/c/sync_data?pub_time='+ str(pub_time)  +'&log_id=1234')
        #rds.push('scrapy_start_urls','https://app.leting.io/auth?uid=12345&appid=8f5a691127c89465e44e3b195e588f05&app_secret=7c39c2f62a33ab61437fcd6e9e5c8be3&log_id=1234')
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/lt.txt','w')
        p.write(pub_time+':leting_pubtime')
        p.close()
        p = open('/home/mitian/scrapy-redis/scrapy_frame/scrapy_frame/spiders/Log_lt.txt','a')
        p.write(pub_time+':leting_pubtime'+'\n')
        p.close()
















