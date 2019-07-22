# -*- coding: utf-8 -*-

import re
import os
import sys
import json
import time
import traceback
import configparser
from scrapy_frame.log import scrapy_log
import scrapy_frame.news
import scrapy_frame.kafka


class YuyanjiaScrapyPipeline(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read((os.getcwd()+'/config.ini'), encoding='utf-8')

    def process_item(self, item,name):
        item['_news_title'] = item['_news_title'].replace(' ','').replace('\r','').replace('\n','').replace('\t','')
        #日志实例化
        log = scrapy_log(item['_name'])
        try:
            #news对象实例化
            news = scrapy_frame.news.News()
            news._news_title            = item['_news_title']
            news._pub_time              = item['_pub_time']
            news._create_time           = item['_create_time']
            news._src_pub_time          = item['_src_pub_time']
            news._news_source           = item['_news_source']
            news._site_name             = item['_site_name']
            news._list_images           = item['_list_images']
            news._content               = self.rehandle(item['_from_source'],item['_content'],item['_name'],item['_type'])
            #news._content               = self.handle_content_news(item['_content'],item['_name'])
            news._tags                  = str(item['_tags'])
            news._id                    = item['_id']
            news._up_count              = item['_up_count']
            news._down_count            = item['_down_count']
            news._comment_count         = item['_comment_count']
            news._is_hot                = item['_is_hot']
            news._org_url               = str(item['_org_url'])
            news._cagetory              = item['_cagetory']
            news._sub_cagetory          = item['_sub_cagetory']
            news._type                  = item['_type']
            news._is_pass_directly      = item['_is_pass_directly']
            news._is_high_video         = item['_is_high_video']
            news._location              = item['_location']
            news._attention             = item['_attention']
            news._channel               = item['_channel']
            news._author                = item['_author']
            news._image_size_type       = item['_image_size_type']
            news._duration              = item['_duration']
            news._is_advertisement      = item['_is_advertisement']
            news._from_source           = item['_from_source']
            news._topic                 = item['_topic']
            news._image_type            = item['_image_type']
            news._num_src_list_images   = item['_num_src_list_images']
            news._is_used_src_resource  = item['_is_used_src_resource']
            news._redirect_type         = item['_redirect_type']
            news._is_auto_publish       = item['_is_auto_publish']
            news._has_attachment        = item['_has_attachment']    
            news._third_id              = item['_third_id']
            news._audio_url             = item['_audio_url']
            news._categories            = item['_categories']
            news._from_sources          = item['_from_sources']
            news._comment_list          = item['_comment_list']
            if news._content != '[]' and news._content !=  '':
                js = news.toJson()
                #print(js)
                ka = scrapy_frame.kafka.kafka_process()
                ka.sendto_kafka(self._type(news._type),js)
                time.sleep(0.2)
                log.log_info(js)

        except Exception:
            traceback.print_exc()
            log.log_error(traceback.format_exc(),item['_org_url'],str(item['_is_used_src_resource']),str(item['_is_pass_directly']),str(item['_third_id']))

    def _type(self,_type):
        if str(_type) == '1':
            return 'qiyu_news'
        elif str(_type) == '3':
            return 'qiyu_video'
        elif str(_type) == '5':
            return 'qiyu_audio'

    def rehandle(self,from_source,content,section,_type):
        if str(from_source) == 'shanxun' or str(from_source) == 'leting':
            return content
        else:
            return self.handle_content(content,section,_type)


    def handle_content(self,content,section,_type):
        p = ['\n','\t','\r']
        for i in p:
            content = content.replace(i,'')
        audio_sign = ['.mp3','.m4a']
        video_sign = ['.mp4','.m3u8','/video/']
        flag  = 0
        cont  = ''
        tmp   = ''
        voice = ''
        text = ''
        video  = ''
        video_str = []
        voice_str = []
        su_str     = ['<b>','</b>','<p>','</p>','<br>','</br>']
        all_str     = re.findall('<.+?>',content)
        img_str    = re.findall('<img.+?>',content)
        table_str  = re.findall('<table.+?</table>',content)
        for i in video_sign:
            video_str  += re.findall(('<.+'+i+'.*?>'),content)
        for i in audio_sign:
            voice_str  += re.findall(('<.+'+i+'.*?>'),content)
        save_str    = su_str + img_str + table_str + video_str + voice_str
        for a in all_str:
            if a not in save_str:
                content = content.replace(a,'')
        if str(_type) == '1':
            cont = self.handle_content_news(content,section)
            return cont
        else:
            if '<' not in content:
                for i in video_sign:
                    if i in content:
                        video += "{\"type\":\"video\",\"data\":\"" + content +"\"},"
                for i in audio_sign:
                    if i in content:
                        voice += "{\"type\":\"audio\",\"data\":\"" + content +"\"},"
            else:
                for i in range(len(content)):
                
            
                    if content[i] == '<':
                        flag = 1
                        
                    if content[i] == '>':
                        flag = 2
                    if flag == 0:
                        tmp += content[i]
                    if flag == 1:
                        if tmp != '':
                            tmp = tmp.replace('"','\\"')
                            print('=====================================')
                            print(text)
                            text += "{\"type\":\"text\",\"data\":\"" + tmp +"\"},"
                        tmp = ''
                        tmp += content[i]
                        flag = 0
                        
                    if flag == 2:
                        tmp += tmp+'>'
                        for i in video_sign:
                            if i in tmp:
                                data = re.search('src="(.+?)"',tmp).group(1)
                                video += "{\"type\":\"video\",\"data\":\"" + data +"\"},"
                            
                        for i in audio_sign:
                            if i in tmp:
                                data = re.search('src="(.+?)"',tmp).group(1)
                                voice += "{\"type\":\"audio\",\"data\":\"" + data +"\"},"
                        flag = 0
                        tmp  = ''   
        cont = video + voice + text
        video = ''
        vioce = ''
        text  = ''
        cont = '['+ cont[:len(cont)-1]+ ']'
        #print(cont)
        return cont 
                    
                
        


    def handle_content_news(self,content,section):
        flag = 0
        strtmp = ''
        strclass = ''
        strcont = ''
        width = '0'
        height = '0'
        tablestr = ''
        for item in content:
            tablestr += item
            if '<table' in tablestr:
                tablestr = ''
                flag = 2
            if 'table>' in tablestr:
                tablestr = "<table " +str(tablestr).replace('"','\'')
                i = re.findall(r'<.*?>',tablestr)
                
                for bc in i:
                    if not 'table' in bc and not 'tr' in bc and not 'td' in bc and not 'caption' in bc:
                        tablestr = str(tablestr).replace(bc,'')
                    if 'colspan' in bc:
                        h = re.search('colspan=.(\d+).*',bc).group(1)
                        z = re.search('<\w+',bc).group(0)
                        zoo = z + ' colspan=\'' + h + '\'>' 
                        tablestr = str(tablestr).replace(bc,zoo)
                       
                       

                    if 'rowspan' in bc:
                        h = re.search('rowspan=.(\d+).*',bc).group(1)
                        z = re.search('<\w+',bc).group(0)
                        zoo = z + ' rowspan=\'' + h + '\'>'
                        tablestr = str(tablestr).replace(bc,zoo)

                        
                sty = re.findall('<\w+(\s+.*?)>',tablestr)
                for i in sty:
                    
                    if not 'colspan' in i and not 'rowspan' in i:
                        
                        tablestr = str(tablestr).replace(i,'')
                strcont += "{\"type\":\"table\",\"data\":\"" + tablestr +"\"},"
                
                tablestr = ''
                flag = 0
            if item == "<" and flag != 2:
                flag = 1
                if strtmp.lstrip() != "":
                    strtmp = strtmp.replace('"','\\"')
                    strcont += "{\"type\":\"text\",\"data\":\"" + strtmp + "\"},"
                strtmp = ""
            if item == ">" and flag != 2:
                flag = 0
                if strclass.lstrip() != "":
                    
                        
                    if 'img' in strclass and 'src' in strclass:
                        src_index = strclass.index('src') + 5
                        src = ""
                        while strclass[src_index] != '\"':
                            src += strclass[src_index]
                            src_index += 1
                        he = (re.findall('height=\"(\d+)\"',strclass))
                        wi = (re.findall('width=\"(\d+)\"',strclass))
                        if not he == []:
                            height  = he[0]
                        if not wi == []:
                            width   = wi[0]
                        if 'http' in strclass:
                            strcont += "{\"type\":\"img\",\"data\":\"" + src + "\",\"width\":\"" + width + "\",\"height\":\"" + height + "\"},"
                        else:
                            strcont += "{\"type\":\"img\",\"data\":\"" + self.config.get(section,'src_str')  + src + "\",\"width\":\"" + width + "\",\"height\":\"" + height + "\"},"
                width = '0'
                height = '0'
                strclass = ""
            if item != "<" and flag == 1:
                strclass += item
            if item != ">" and flag == 0:
                strtmp   += item
        strcont = "[" + strcont[:len(strcont) - 1] + "]"
        return strcont


