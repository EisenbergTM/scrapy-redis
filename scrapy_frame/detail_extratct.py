# -*- coding: utf-8 -*-

import sys
sys.path.append('../../scrapy_frame')
from scrapy_frame.spiders.detail_parse.xinle import xinle
from scrapy_frame.spiders.detail_parse.shanxun import shanxun
from scrapy_frame.spiders.detail_parse.yuyan import yuyan
from scrapy_frame.spiders.detail_parse.dongjiu import dongjiu
from scrapy_frame.spiders.detail_parse.guangle import guangle
from scrapy_frame.spiders.detail_parse.meizhuang import meizhuang
from scrapy_frame.spiders.detail_parse.leting import leting
from scrapy_frame.spiders.detail_parse.aidi import aidi


class model_detail(object):
    def __init__(self,response):
        self.xinle        = xinle()
        self.shanxun      = shanxun()
        self.yuyan        = yuyan()
        self.dongjiu      = dongjiu()
        self.guangle      = guangle()
        self.meizhuang    = meizhuang()
        self.leting       = leting()
        self.aidi         = aidi()
        self.response = response
        self.url      = response.url
        #self.rds      = redis.Redis(host='10.30.180.221',port=16379,password='xdrt@^oasdfasf=<',db=0)

    def select(self):
        urllist_shanxun    = ['http://www.yzpai.cn/news/out/article?lastid=']
        urllist_meizhuang  = ['https://weibo.com/ttarticle/p/show','https://zhuanlan.zhihu.com/p']
        urllist_xinle      = ['http://sy.yzz.cn/news','www.huoxing24.com/newsdetail/','http://news.17173.com','https://new.qq.com','http://ent.163.com/1','http://www.9game.cn','https://www.119you.com']
        urllist_dongjiu    = ['https://v.douyu.com']
        urllist_yuyan      = ['http://wemedia.ifeng.com','http://www.yidianzixun.com','https://xueqiu.com/','http://www.1905.com/','https://36kr.com','http://caozhi.news.163.com/','http://www.geekpark.net/','http://tech.sina.com.cn/csj/','www.sohu.com/a/','https://www.cbnweek.com/articles','http://www.ellemen.com','http://www.ifengweekly.com','http://www.ftchinese.com','http://news.ifeng.com/a','https://www.guokr.com/article','https://wallstreetcn.com','https://www.huxiu.com','https://www.jiemian.com','http://sports.sina.com.cn/zl','http://news.ikanchai.com','http://songshuhui.net','https://www.thepaper.cn','http://money.163.com','http://news.mtime.com','http://www.esquire.com.cn','http://data.163.com','http://ent.sina.com.cn','http://news.dgtle.com','http://www.tmtpost.com','http://sports.qq.com','http://dajia.qq.com','http://www.vogue.com.cn','https://mp.weixin.qq.com','http://play.163.com','http://ent.163.com','https://news.163.com','http://tech.163.com','http://renjian.163.com','http://art.163.com','https://www.feng.com/','https://tech.feng.com','http://finance.sina.com.cn','http://youxiputao.com','http://www.youxituoluo.com','http://www.iceo.com.cn','http://www.jwview.com','http://www.qdaily.com','http://view.news.qq.com','zhihu.com/story','https://pit.ifeng.com','https://www.toutiao.com/a']
        urllist_guangle     = ['https://www.zcool.com.cn']
        urllist_leting      = ['https://app.leting.io/c/sync_data?']
        urllist_aidi        = ['http://news.xiancity.cn','http://www.xasqw.com','http://news.xiancn.com','http://www.xashangwang.com']         



        for i in urllist_aidi:
            if i in self.url:
                return self.aidi.extract(self.response)
        for i in urllist_leting:
            if i in self.url:
                return self.leting.extract(self.response) 
        for i in urllist_meizhuang:
            if i in self.url:
                return self.meizhuang.extract(self.response)
        for i in urllist_guangle:
            if i in self.url:
                return self.guangle.extract(self.response)
        for i in urllist_yuyan:
            if i in self.url and i != 'http://ent.163.com':
                return self.yuyan.extract(self.response)
        for i in urllist_xinle:
            if i in self.url:
                return self.xinle.extract(self.response)
        for i in urllist_shanxun:
            if i in self.url:
                return self.shanxun.extract(self.response)
        for i in urllist_dongjiu:
            if i in self.url:
                return self.dongjiu.extract(self.response)
 
 
