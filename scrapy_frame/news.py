# -*- coding:utf-8 -*-

import time
import random
import datetime
import json

class News():
    def __init__(self):
        self._news_title            = ''
        self._pub_time              = '0'
        self._create_time           = '0'
        self._src_pub_time          ='0'
        self._news_source           = ''
        self._site_name             = ''
        self._list_images           = []
        self._content               = [] 
        self._tags                  = []
        self._id                    = ''
        self._up_count              = '0'
        self._down_count            = '0'
        self._comment_count         = '0'
        self._is_hot                = '0'
        self._org_url               = ''
        self._cagetory              = ''
        self._sub_cagetory          = ''
        self._type                   = '1'
        self._is_pass_directly      = '0'
        self._is_high_video         = '0'
        self._location              = '' #{"province":"shandong","city":"qingdao","district":"laoshan"}
        self._attention             = '' #json array
        self._channel               = ''
        self._author                = ''
        self._image_size_type       = '0' #0 normal; 1 big
        self._duration              = '0'
        self._is_advertisement      = '0' #0 not; 1 yes
        self._from_source           = ''
        self._topic                 = ''
        self._image_type            = ''
        self._num_src_list_images   = '0'
        self._is_used_src_resource  = '0'
        self._redirect_type         = '0' #0 only to ours; 1 only to others; 2 all, (to ours must set _from_source = '', to others must set _from_source)
        self._is_auto_publish       = '0'
        self._has_attachment        = '0'
        self._num_content_images    = '0'
        self._third_id              = ''
        self._audio_url             = ''
        self._categories            = []
        self._from_sources          = []
        self._comment_list          = []



    #获取Id，格式为年月日时分秒+六位随机数
    def set_id(self):
        t = time.time()
        now_time = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        number = random.randint(0, 999999)
        rand_number = str(number).zfill(6)
        self._id = str(now_time) + rand_number

    #获取当前时间的毫秒级时间戳
    def generate_create_time(self):
        t = time.time()
        now_timestamp = int(round(t * 1000))
        return now_timestamp
    def replace_info(self,info, src, des):
        return info.replace(src, des)

    def toJson(self):
        title = self.replace_info(self._news_title, '"','\\\"')
        json_str = '{' \
                   + '\"id\":\"' + self._id + '\"'  \
                   + ',\"news_title\":\"' + title + '\"'    \
                   + ',\"content\":' + self._content \
                   + ',\"pub_time\":' + str(self._pub_time) \
                   + ',\"create_time\":' + str(self._create_time) \
                   + ',\"src_pub_time\":' + str(self._src_pub_time) \
                   + ',\"news_source\":\"' + str(self._news_source) + '\"' \
                   + ',\"site_name\":\"' + str(self._site_name) + '\"' \
                   + ',\"list_images\":' + str(self._list_images)  \
                   + ',\"tags\":' + str(self._tags)  \
                   + ',\"up_count\":' + str(self._up_count)  \
                   + ',\"down_count\":' + str(self._down_count)  \
                   + ',\"comment_count\":' + str(self._comment_count)  \
                   + ',\"is_hot\":' + str(self._is_hot)  \
                   + ',\"is_high_video\":' + str(self._is_high_video)  \
                   + ',\"cagetory\":\"' + str(self._cagetory) + '\"'  \
                   + ',\"sub_cagetory\":\"' + str(self._sub_cagetory) + '\"'  \
                   + ',\"attention\":' + str(self._attention)  \
                   + ',\"location\":' + str(self._location)  \
                   + ',\"type\":' + str(self._type)  \
                   + ',\"duration\":' + str(self._duration)  \
                   + ',\"author\":\"' + str(self._author)  + '\"' \
                   + ',\"channel\":\"' + str(self._channel)  + '\"' \
                   + ',\"org_url\":\"' + str(self._org_url)  + '\"' \
                   + ',\"is_pass_directly\":' + str(self._is_pass_directly)  \
                   + ',\"image_size_type\":' + str(self._image_size_type)  \
                   + ',\"is_advertisement\":' + str(self._is_advertisement)  \
                   + ',\"from_source\":\"' + str(self._from_source)  + '\"'  \
                   + ',\"topic\":\"' + str(self._topic)  + '\"'  \
                   + ',\"image_type\":\"' + str(self._image_type)  + '\"'  \
                   + ',\"num_src_list_images\":' + str(self._num_src_list_images)  \
                   + ',\"is_used_src_resource\":' + str(self._is_used_src_resource)  \
                   + ',\"redirect_type\":' + str(self._redirect_type)  \
                   + ',\"is_auto_publish\":' + str(self._is_auto_publish)  \
                   + ',\"has_attachment\":' + str(self._has_attachment)  \
                   + ',\"third_id\":\"' + str(self._third_id) +'\"' \
                   + ',\"audio_url\":\"' + str(self._audio_url) +'\"' \
                   + ',\"categories\":' + str(self._categories)  \
                   + ',\"from_sources\":' + str(self._from_sources)  \
                   + ',\"comment_list\":' + str(self._comment_list)  \
                   + '}'

        return json_str

    def getContentText(self):
        jstr = json.loads(self._content)
        txt = ''
        for i in jstr:
            if 'type' in i and 'text' == str(i['type']):
                if 'data' in i and str(i['data']) != '':
                    txt += str(i['data'])
        return txt


def create_news_from_json(json_str):
    jstr = json.loads(json_str)
    news = None
    if jstr is not None:
        news = News()
        if 'id' in jstr:
            news._id = str(jstr['id'])
        if 'news_title' in jstr:
            news._news_title = str(jstr['news_title'])
        if 'pub_time' in jstr:
            news._pub_time = str(jstr['pub_time'])
        if 'create_time' in jstr:
            news._create_time = str(jstr['create_time'])
        if 'src_pub_time' in jstr:
            news._src_pub_time = str(jstr['src_pub_time'])
        if 'news_source' in jstr:
            news._news_source = str(jstr['news_source'])
        if 'site_name' in jstr:
            news._site_name = str(jstr['site_name'])
        if 'list_images' in jstr:
            news._list_images = json.dumps(jstr['list_images'])
        if 'content' in jstr:
            news._content = json.dumps(jstr['content'])
        if 'tags' in jstr:
            news._tags = json.dumps(jstr['tags'])
        if 'up_count' in jstr:
            news._up_count = str(jstr['up_count'])
        if 'down_count' in jstr:
            news._down_count = str(jstr['down_count'])
        if 'comment_count' in jstr:
            news._comment_count = str(jstr['comment_count'])
        if 'is_hot' in jstr:
            news._is_hot = str(jstr['is_hot'])
        if 'org_url' in jstr:
            news._org_url = str(jstr['org_url'])
        if 'cagetory' in jstr:
            news._cagetory = str(jstr['cagetory'])
        if 'sub_cagetory' in jstr:
            news._sub_cagetory = str(jstr['sub_cagetory'])
        if 'type' in jstr:
            news._type = str(jstr['type'])
        if 'is_pass_directly' in jstr:
            news._is_pass_directly = str(jstr['is_pass_directly'])
        if 'is_high_video' in jstr:
            news._is_high_video = str(jstr['is_high_video'])
        if 'location' in jstr:
            news._location = json.dumps(jstr['location'])
        if 'attention' in jstr:
            news._attention = json.dumps(jstr['attention'])
        if 'channel' in jstr:
            news._channel = str(jstr['channel'])
        if 'author' in jstr:
            news._author = str(jstr['author'])
        if 'image_size_type' in jstr:
            news._image_size_type = str(jstr['image_size_type'])
        if 'duration' in jstr:
            news._duration = str(jstr['duration'])
        if 'is_advertisement' in jstr:
            news._is_advertisement = str(jstr['is_advertisement'])
        if 'from_source' in jstr:
            news._from_source = str(jstr['from_source'])
        if 'topic' in jstr:
            news._topic = str(jstr['topic'])
        if 'image_type' in jstr:
            news._image_type = str(jstr['image_type'])
        if 'num_src_list_images' in jstr:
            news._num_src_list_images = str(jstr['num_src_list_images'])
        if 'is_used_src_resource' in jstr:
            news._is_used_src_resource = str(jstr['is_used_src_resource'])
        if 'redirect_type' in jstr:
            news._redirect_type = str(jstr['redirect_type'])
        if 'is_auto_publish' in jstr:
            news._is_auto_publish = str(jstr['is_auto_publish'])
        if 'has_attachment' in jstr:
            news._has_attachment = str(jstr['has_attachment'])
        if 'third_id' in jstr:
            news._third_id = str(jstr['third_id'])
        if 'audio_url' in jstr:
            news._audio_url = str(jstr['audio_url'])
        if 'categories' in jstr:
            news._categories = json.dumps(jstr['categories'])
        if 'from_sources' in jstr:
            news._from_sources = json.dumps(jstr['from_sources'])
        if 'comment_list' in jstr:
            news._comment_list = json.dumps(jstr['comment_list'])

    return news

if __name__ == "__main__":        
    news = News()
    news._id = '20180625001933632248'
    news._news_title = 'hello world'
    news._pub_time = '1529857173026'
    news._create_time = '1529857173026'
    news._src_pub_time = '1529857173026'
    news._news_source = 'qq'
    news._site_name = 'qq'
    news._list_images = '[\"http://oozojm6hp.bkt.clouddn.com/FveVp6DFeDwRWPtdDGkiOCIvW6-K?imageView2/1/w/400/h/200/interlace/1/q/200/format/jpg\"]'
    news._content = '[{\"type\":\"text\",\"data\":\"aaaaaa\"}]'
    news._tags = '[\"video\", \"high\"]'
    news._up_count = '19'
    news._down_count = '10'
    news._comment_count = '11'
    news._is_hot = '1'
    news._org_url = 'http://op1ozwnbj.bkt.clouddn.com/260e034c6ae35b00db330268df18ec521529858191053.mp4'
    news._cagetory = 'tiyun'
    news._sub_cagetory = 'tiyun2'
    news._type = '3'
    news._is_pass_directly = '0'
    news._is_high_video = '1'
    news._location = '{\"province\":\"shandong\",\"city\":\"qingdao\",\"district\":\"laoshan\"}'
    news._attention = '[{\"child\":5.345544338226318},{\"small\":4.153561115264893},{\"work\":2.986873865127563}]'
    news._channel = 'child'
    news._author = 'xiaowang'
    news._image_size_type = '1'
    news._duration = '30'
    news._topic = 'aa'
    news._image_type = 'gif'
    news._num_src_list_images = '7'
    news._is_used_src_resource = '1'
    news._redirect_type = '2'
    news._is_auto_publish = '1'
    news._has_attachment = '1'
    news._third_id = '132142342'
    news._audio_url = 'www.baidu.com/1.mp3'
    news._categories= '[\"car\"]'
    news._from_sources = '[\"qiyu\"]'
    news._comment_list = ['***']
    print('src news: ' + news.toJson())

    print('content: ' + news.getContentText())

    news2 = create_news_from_json(news.toJson())
    print('news2 : ' + news2.toJson())
#news3 = create_news_from_json(news2.toJson())
#    print('news3 : ' + news3.toJson())
