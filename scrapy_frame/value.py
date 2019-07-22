# -*- coding: utf-8 -*-

import re
import os
import sys
import time
import random
import datetime
import json


class value(object):
    def __init__(self):
        self._name                  = ''
        self._news_title            = ''
        self._pub_time              = '0'
        self._create_time           = self.creat_time()
        self._src_pub_time          = '0'
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
        self._type                  = '1'
        self._is_pass_directly      = '0'
        self._is_high_video         = '0'
        self._location              = '{}' #{"province":"shandong","city":"qingdao","district":"laoshan"}
        self._attention             = '{}' #json array
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
        self._redirect_type         = '0'
        self._is_auto_publish       = '0'
        self._has_attachment        = '0'
        self._third_id              = ''
        self._audio_url             = ''
        self._categories            = []
        self._from_sources          = []
        self._comment_list          = []

    def set_id(self):
        t = time.time()
        now_time = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        number = random.randint(0, 999999)
        rand_number = str(number).zfill(6)
        _id = str(now_time) + rand_number
        
        return _id
        
    def creat_time(self):           
        t = time.time()             
        now_timestamp = int(round(t * 1000))
        return now_timestamp        
        
    def value_to_list(self):        
        value_list = [self._name,self._news_title,self._pub_time,self._create_time,self._src_pub_time,self._news_source,self._site_name,self._list_images,self._content,self._tags,self._id,self._up_count,self._down_count,self._comment_count,self._is_hot,self._org_url,self._cagetory,self._sub_cagetory,self._type,self._is_pass_directly,self._is_high_video,self._location,self._attention,self._channel,self._author,self._image_size_type,self._duration,self._is_advertisement,self._from_source,self._topic,self._image_type,self._num_src_list_images,self._is_used_src_resource,self._redirect_type,self._is_auto_publish,self._has_attachment,self._third_id,self._audio_url,self._categories,self._from_sources,self._comment_list]
        return value_list     
