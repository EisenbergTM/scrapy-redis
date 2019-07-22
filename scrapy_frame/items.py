# -*- coding: utf-8 -*-

import scrapy
#from Scrapy.singleton import MyCommKafkaProducer

class ScrapyItem(scrapy.Item):
    # define the fields for your item here like:

    #爬虫名字
    _name                  = scrapy.Field()
    #标题
    _news_title            = scrapy.Field()
    #发布时间
    _pub_time              = scrapy.Field()
    #创建时间
    _create_time           = scrapy.Field()
    #图片发布时间 
    _src_pub_time          = scrapy.Field()
    #资讯来源
    _news_source           = scrapy.Field()
    #网站名称
    _site_name             = scrapy.Field()
    #图片列表
    _list_images           = scrapy.Field()
    #内容
    _content               = scrapy.Field()
    #标签
    _tags                  = scrapy.Field()
    #id
    _id                    = scrapy.Field()
    #点赞数
    _up_count              = scrapy.Field()
    #踩数
    _down_count            = scrapy.Field()
    #评论数
    _comment_count         = scrapy.Field()
    #是否热点
    _is_hot                = scrapy.Field()
    #源url
    _org_url               = scrapy.Field()
    #一级分类
    _cagetory              = scrapy.Field()
    #二级分类
    _sub_cagetory          = scrapy.Field()
    #资讯类型
    _type                  = scrapy.Field()
    #是否直接通过
    _is_pass_directly      = scrapy.Field()
    #是否高质量视频
    _is_high_video         = scrapy.Field()
    #区域
    _location              = scrapy.Field()
    #注意
    _attention             = scrapy.Field()
    #频道
    _channel               = scrapy.Field()
    #作者
    _author                = scrapy.Field()
    #图片大小类型
    _image_size_type       = scrapy.Field()
    #时长
    _duration              = scrapy.Field()
    #是否广告
    _is_advertisement      = scrapy.Field()
    #来源位置
    _from_source           = scrapy.Field()
    #话题
    _topic                 = scrapy.Field()
    #图片类型
    _image_type            = scrapy.Field()
    #封面图数量 
    _num_src_list_images   = scrapy.Field()
    #是否走7n
    _is_used_src_resource  = scrapy.Field()
    #。。。
    _redirect_type         = scrapy.Field()
    _is_auto_publish       = scrapy.Field()
    _has_attachment        = scrapy.Field()
    _third_id              = scrapy.Field()
    _audio_url             = scrapy.Field()
    _categories            = scrapy.Field()
    _from_sources          = scrapy.Field()
    _comment_list          = scrapy.Field()

