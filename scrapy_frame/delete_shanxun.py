# -*- coding: utf-8 -*-

import re
import os
import sys
import time
import json
import hmac
import hashlib
import datetime
import requests
import traceback
import configparser

    
u = 'http://www.yzpai.cn/news/out/articleDel?lasttime=0&count=50&time=1532945802&sign=2ABFFE8423792E213AE1AB9C16AC1864'

def delete_one():
    pass
def exec_main():
    config = configparser.ConfigParser()
    config.read('/home/docker/script/mitian/shanxun/shanxun.ini')
    i = 0
    try:
        while i < 2000000:
            num = config.get('shanxun','lasttime')
            list_id = get_id(num)[0]
            last_time = get_id(num)[1]
            url = get_id(num)[2]      
        
            #print(list_id)
            #print(last_time)
            #print(url)
            delete_id(list_id) 
            i += 1
            config.set('shanxun','lasttime',last_time)
            config.write(open("/home/docker/script/mitian/shanxun/shanxun.ini", "w"))
            time.sleep(1)
    except BaseException:
        traceback.print_exc() 
        
        log(url+'--ERROR--'+traceback.format_exc())

def get_id(num):
    id_list = []
    url = 'http://www.yzpai.cn/news/out/articleDel?lasttime='+str(num)+'&count=50&time=1532945802&sign=2ABFFE8423792E213AE1AB9C16AC1864'
    html = requests.get(url)
    js = json.loads(html.content)
    if js['data'] != []:
        for a in js['data']:
            lasttime = str(a['lasttime'])
            id_list.append(a['id'])
    else:
        os._exit(0)
    return id_list,lasttime,url



def delete_id(id_list):
    
    url  = 'http://114.215.18.7:8010/HttpService2/remove_news'
    key  = 'g@4834readfasdyu'
    info = '010000001000020180522161452789383shanxun'+str(get_timestamp())
    #signature = base64.b64encode(hmac.new(key.encode('utf-8'),info.encode('utf-8'), digestmod=hashlib.sha256).digest())

    sign =hmac.new(key.encode('utf-8'),info.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    #sign=hex(hmac_hash256(key, info))
    #print(sign)
    num = 0
    for i in range(5):
        array = id_list[num:num+10]
        num += 10
        
        body = '{"qiyu_id":"010000001000020180522161452789383","app_id":"shanxun","ids":'+str(array)+',"timestamp":'+str(get_timestamp())+',"sign":"'+sign+'"}'
        print(body)
        html = requests.post(url=url,data=body)
        print(html.content)

def log(data):
    log = open('/home/docker/script/mitian/shanxun/shanxun_log.txt','a')
    log.write(str(data)+'-delete-'+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'\n')
    log.close     


def config():
    config = configparser.ConfigParser()
    config.read('/home/docker/script/mitian/shanxun/shanxun.ini')
    num = config.get('shanxun','last_id')
    print(num)
    config.set('shanxun','last_id','23')
    num = config.get('shanxun','last_id')
    print(num)
    config.write(open("shanxun.ini", "w"))


def get_timestamp():
    now = time.time()
    stamp = int(round(now))
    print(stamp)
    return stamp


if __name__ == '__main__':
    exec_main()
    #delete_id(['33678'])
    #get_id(0)
    os._exit(0)
