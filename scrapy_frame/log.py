# -*- coding:utf-8 -*-


import os
import sys
import time
import json
import datetime
import logging
import socket
sys.path.append('../scrapy_frame')


class scrapy_log():

    def __init__(self,section):
       if not(os.path.exists('./scrapy_frame/log')):
            os.mkdir('./scrapy_frame/log')
       #if not(os.path.exists('./scrapy_frame/log/news')):
       #     os.mkdir('./scrapy_frame/log/news')
       ct = time.time()
       hm = (ct - int(ct)) * 1000
       self.nowtime = str("%s.%03d" %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),hm)).replace('.',',')
       nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
       self.section = section
       info = 'info'
       warning = 'warning'
       error = 'error'
       formatter = logging.Formatter('%(message)s')
       self.logger_info = logging.getLogger(info)
       self.logger_info.setLevel(level = logging.INFO)
       self.handler_info = logging.FileHandler("./scrapy_frame/log/"+str(nowdate)+"log_info.txt")
       self.handler_info.setLevel(logging.INFO)
       self.handler_info.setFormatter(formatter)


       self.logger_warning = logging.getLogger(warning)
       self.logger_warning.setLevel(level = logging.WARNING)
       self.handler_warning = logging.FileHandler("./scrapy_frame/log/"+str(nowdate)+"log_warning.txt")
       self.handler_warning.setLevel(logging.WARNING)
       self.handler_warning.setFormatter(formatter)


       self.logger_error= logging.getLogger(error)
       self.logger_error.setLevel(level = logging.ERROR)
       self.handler_error = logging.FileHandler("./scrapy_frame/log/"+str(nowdate)+"log_error.txt")
       self.handler_error.setLevel(logging.ERROR)
       self.handler_error.setFormatter(formatter)



    def get_host_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:

           s.connect(('8.8.8.8', 80))
           ip = s.getsockname()[0]
        finally:
           s.close()

        return ip

    def log_info(self,jss):
        self.logger_info.addHandler(self.handler_info)
        js = json.loads(jss)
        info_str = '{\
      "ip":"'+self.get_host_ip()+'",\
      "module":"crawl",\
      "date":"'+self.nowtime+'",\
      "from_sources":'+str(js['from_sources']).replace('\'','"')+',\
      "log_type":"INFO",\
      "web":"'+js['site_name']+'-'+js['channel']+'",\
      "news_type":"news",\
      "org_url":"'+js['org_url']+'",\
      "nid":"'+str(js['id'])+'",\
      "is_used_src_resource":"'+str(js['is_used_src_resource'])+'",\
      "is_pass_directly":"'+str(js['is_pass_directly'])+'",\
      "third_id":"'+str(js['third_id'])+'",\
      "status":"TRUE"\
}'
        js = json.loads(info_str)
        self.logger_info.info('============================================================\n'+str(info_str).replace(' ',''))
        self.logger_info.removeHandler(self.handler_info)
        self.handler_info.close()

    def log_warning(self,messages,url,is_use,is_pass,third_id):
        self.logger_warning.addHandler(self.handler_warning)
        warning_str = '{\
      "ip":"'+self.get_host_ip()+'",\
      "module":"crawl",\
      "date":"'+self.nowtime+'",\
      "log_type":"WARNING",\
      "web":"'+self.section+'",\
      "news_type":"news",\
      "org_url":"'+url+'",\
      "is_used_src_resource":"'+str(is_use)+'",\
      "is_pass_directly":"'+str(is_pass)+'",\
      "third_id":"'+str(third_id)+'",\
      "file":"'+os.path.basename(sys.argv[0]).split(".")[0]+'",\
      "warning":"'+str(messages)+'"\
}'
        js = json.loads(warning_str)
        self.logger_warning.warning('============================================================\n'+warning_str.replace(' ',''))
        self.logger_warning.removeHandler(self.handler_warning)
        self.handler_warning.close()

    def log_error(self,messages,url,is_use,is_pass,third_id):
        self.logger_error.addHandler(self.handler_error)
        error_str = '{\
      "ip":"'+self.get_host_ip()+'",\
      "module":"crawl",\
      "date":"'+self.nowtime+'",\
      "log_type":"ERROR",\
      "web":"'+self.section+'",\
      "news_type":"news",\
      "org_url":"'+url+'",\
      "is_used_src_resource":"'+str(is_use)+'",\
      "is_pass_directly":"'+str(is_pass)+'",\
      "third_id":"'+str(third_id)+'",\
      "file":"'+os.path.basename(sys.argv[0]).split(".")[0]+'",\
      "error":"'+messages+'"\
}'
        js = json.loads(error_str)
        self.logger_error.error('============================================================\n'+error_str.replace(' ',''))
        self.logger_error.removeHandler(self.handler_error)
        self.handler_error.close()
