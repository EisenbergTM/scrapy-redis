# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import html
import redis
import random
import datetime
sys.path.append('../../scrapy_frame')
from scrapy_frame.value import value
from scrapy_frame.redis_push import redis_push
from scrapy_frame.grab_comments import comment

class yuyan(value):
    def __init__(self):
        
        super(yuyan,self).__init__()
        self.rds        = redis_push()
        self.comment    = comment()

    def extract(self,response):
        if 'http://wemedia.ifeng.com/' in response.url:
            return self.parse_dafenghao(response)
        if 'http://www.yidianzixun.com' in response.url:
            return self.parse_meirirenwu(response)
        if 'https://xueqiu.com' in response.url:
            return self.parse_xueqiu(response)
        if 'http://www.1905.com' in response.url:
            return self.parse_1905wang(response)
        if 'https://36kr.com/' in response.url:
            return self.parse_36kr(response)
        if 'http://caozhi.news.163.com' in response.url:
            return self.parse_caozhi(response)
        if 'http://www.geekpark.net/news' in response.url:
            return self.parse_chanpinguancha(response)
        if 'http://tech.sina.com.cn/csj' in response.url:
            return self.parse_chuangshiji(response)
        if 'www.sohu.com/a' in response.url:
            return self.parse_sohutoutiaohao(response)
        if 'https://www.cbnweek.com/articles' in response.url:
            return self.parse_diyicaijing(response)
        if 'http://www.ellemen.com' in response.url:
            return self.parse_ellemen(response)
        if 'http://www.ifengweekly.com/detil.php' in response.url:
            return self.parse_denghuangzhoukan(response)
        if 'http://www.ftchinese.com' in response.url:
            return self.parse_FT(response)
        if 'http://news.ifeng.com/a' in response.url:
            return self.parse_fenghuang(response)
        if 'https://www.guokr.com/article' in response.url:
            return self.parse_guoke(response)   
        if 'new.qq.com/' in response.url and 'omn' not in response.url and 'cmsn' not in response.url:
            return self.parse_tengxunomn(response)
        if 'https://wallstreetcn.com' in response.url:
            return self.parse_huaerjiejianwen(response)
        if 'https://www.huxiu.com' in response.url:
            return self.parse_huxiu(response)
        if 'https://www.jiemian.com' in response.url:
            return self.parse_jiemian(response)
        if 'http://sports.sina.com.cn/zl' in response.url:
            return self.parse_jingjichang(response)
        if 'ikanchai.com' in response.url:
            return self.parse_kanchaiwang(response)
        if 'http://songshuhui.net' in response.url:
            return self.parse_kexuesongshuhui(response)
        if 'https://www.thepaper.cn' in response.url:
            return self.parse_pengpai(response)
        if 'http://money.163.com' in response.url:
            return self.parse_qingnianyanlun(response)
        if 'http://news.mtime.com' in response.url:
            return self.parse_shiguangxinwen(response)
        if 'http://www.esquire.com.cn' in response.url:
            return self.parse_shishangxiansheng(response)
        if 'http://data.163.com/' in response.url:
            return self.parse_shudu(response)
        if 'http://ent.sina.com.cn' in response.url:
            return self.parse_shuizhuyu(response)
        if 'http://news.dgtle.com' in response.url:
            return self.parse_shuziweiba(response)
        if 'http://www.tmtpost.com/' in response.url:
            return self.parse_taimeiti(response)
        if 'http://sports.qq.com/a' in response.url:
            return self.parse_tengxuntiyu(response) 
        if 'http://dajia.qq.com' in response.url:
            return self.parse_tengxundajia(response)
        if 'new.qq.com/omn' in response.url or 'new.qq.com/cmsn' in response.url:
            return self.parse_tengxunnomal(response)
        if 'http://www.vogue.com.cn' in response.url:
            return self.parse_vogue(response)
        if 'https://mp.weixin.qq.com' in response.url:
            return self.parse_waitan(response)
        if 'http://play.163.com' in response.url:
            return self.parse_wangyiaiwan(response)
        if 'http://ent.163.com' in response.url:
            return self.parse_wangyidianshi(response)
        if 'https://news.163.com' in response.url:
            return self.parse_wangyiguojixinwen(response)
        if 'http://tech.163.com' in response.url:
            return self.parse_wangyitech(response)
        if 'http://renjian.163.com' in response.url:
            return self.parse_wangyirenjian(response)
        if 'http://art.163.com' in response.url:
            return self.parse_wangyiyishu(response)
        if 'https://www.feng.com/view/Views' in response.url:
            return self.parse_weifengguandian(response)
        if 'https://tech.feng.com' in response.url:
            return self.parse_weifengkeji(response)
        if 'https://www.feng.com/iPhone' in response.url:
            return self.parse_weifengxinwen(response)
        if 'http://finance.sina.com.cn/zl' in response.url:
            return self.parse_xinlangyijianlingxiu(response)
        if 'http://youxiputao.com' in response.url:
            return self.parse_youxiputao(response)
        if 'http://www.youxituoluo.com' in response.url:
            return self.parse_youxituoluo(response)
        if 'http://www.iceo.com.cn' in response.url:
            return self.parse_zhongguoqiyejia(response)
        if 'http://www.jwview.com/jingwei' in response.url:
            return self.parse_zhongxinjingwei(response)
        if 'http://www.qdaily.com' in response.url:
            return self.parse_haoqixinribao(response)
        if 'http://view.news.qq.com' in response.url:
            return self.parse_tengxunjinrihuati(response)
        if 'zhihu.com/story' in response.url:
            return self.parse_zhihuribao(response)
        if 'https://pit.ifeng.com' in response.url:
            return self.parse_fenghuangzhiku(response)
        if 'https://www.toutiao.com/a' in response.url:
            return self.parse_jinritoutiao(response)

    def handle(self,content):
        cont_str = ['&lt;','&gt;','&quot;','&#x3D;']
        content = content.replace(cont_str[0],'<')
        content = content.replace(cont_str[1],'>')
        content = content.replace(cont_str[2],'"')
        content = content.replace(cont_str[3],'=')

        return content


    def parse_jinritoutiao(self,response):
        soup    = response.body.decode('utf-8')
        title   = re.search('title:(.+)\',',str(soup)).group(1)
        title   = self.handle(html.unescape(title[2:]))
        content = re.search('content:(.+)\',',str(soup),re.M).group(1)
        cont    = self.handle(html.unescape(content[2:]))
        pubtime = re.search('time:.+?\'(.+?)\'',soup).group(1)[:-1]
        pubtime = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M:%S"))*1000)


        self._name                 = 'jinritoutiao'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '今日头条推荐'
        self._site_name            = '今日头条推荐'
        self._content              = cont
        self._pubtime              = pubtime
        self._channel              = '头条'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        self._comment_list         = self.comment.get_comments(self._org_url,'20','今日头条')
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_fenghuangzhiku(self,response):
        title   = response.xpath('//h1[@id="artical_topic"]/text()').extract()[0]
        content = response.xpath('//div[@id="main_content"]').extract()[0]
        cont = content.replace('（注：本文所有观点仅代表作者本人，均不代表凤凰网国际智库立场）','')
        pubtime = response.xpath('//p[@class="p_time"]/span[1]/text()').extract()[0].replace('年','-').replace('月','-').replace('日','')
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M:%S"))*1000)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'fenghuangzhiku'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._pubtime              = pubtime
        self._channel              = '国际'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url
    


    def parse_zhihuribao(self,response):
        cont = ''
        title   = response.xpath('//h1[@class="headline-title"]/text()').extract()[0]
        img     = response.xpath('//div[@class="img-wrap"]/img/@src').extract()[0]
        content = response.xpath('//div[@class="content"]/*').extract()
        for i in range(len(content)-1):
            cont += content[i]
        cont = img + cont
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'zhihuribao'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '日报'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_tengxunjinrihuati(self,response):
        if 'original' in str(str(response.url)[8:]):
            title   = response.xpath('//h2[@class="title"]/text()').extract()[0]
            cont    = response.xpath('//div[@class="article"]').extract()[0]
            author  = response.xpath('//div[@class="intro_text"]/h3/text()').extract()[0]
            pubtime = response.xpath('//div[@class="timer"]/strong/text()').extract()[0]
            pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d"))*1000)
        else:
            title   = response.xpath('//div[@class="hd"]/h1/text()').extract()[0]
            cont    = response.xpath('//div[@id="Cnt-Main-Article-QQ"]').extract()[0]
            author  = response.xpath('//span[@class="color-a-3"]/text()').extract()[0] 
            pubtime = response.xpath('//span[@class="article-time"]/text()').extract()[0] 
            pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M"))*1000)         
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'tengxunjinrihuati'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '话题'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_haoqixinribao(self,response):
        cont = ''
        title   = response.xpath('//h2[@class="title"]/text()').extract()[0]
        content = response.xpath('//div[@class="detail"]/*').extract()
        for i in content:
            if '</style>' not in i:
                cont += i
        author  = response.xpath('//span[@class="name"]/text()').extract()[0]
        tag     = response.xpath('//ul[@class="tags items clearfix"]/li/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'haoqixinribao'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '好奇心日报'
        self._site_name            = '好奇心日报'
        self._content              = cont
        self._channel              = '热点'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_zhongxinjingwei(self,response):
        cont = ''
        title    = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="content_zw bgwhite"]/p | //div[@class="content_zw bgwhite"]/div').extract()
        for i in content:
            if '</p>' in i or '<img' in i:
                cont += i
        cont = cont.replace('关注中新经纬微信公众号(微信搜索“中新经纬”或“jwview”)，看更多精彩财经资讯。','').replace('细>>>','').replace('中新经纬版权所有，未经书面授权，任何单位及个人不得转载、摘编以其它方式使用。','')
        self._name                 = 'zhongxinjingwei'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '中新经纬'
        self._site_name            = '中新经纬'
        self._content              = cont
        self._channel              = '财经'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_zhongguoqiyejia(self,response):
        title    = response.xpath('//h1[@class="titleh1 clearfix"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="article_body article-content"]').extract()[0]
        if response.xpath('//div[@class="info"]/span/i/text()').extract() != []:
            author   = response.xpath('//div[@class="info"]/span/i/text()').extract()[0]
        else:
            author = ''
        self._name                 = 'zhongguoqiyejia'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '中国企业家'
        self._site_name            = '中国企业家'
        self._content              = cont
        self._channel              = '财经'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_youxituoluo(self,response):
        cont     = ''
        title    = response.xpath('//div[@class="newshead"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="info_p"]/p | //div[@class="info_p"]/div').extract()
        for i in content:
            if 'class="focus"' not in i:
                cont += i
        cont = cont.replace('关注微信公众号：游戏陀螺（shouyoushouce）,定时推送，游戏行业干货分享、爆料揭秘、互动精彩多。','')
        tag      = response.xpath('//a[@rel="tag"]/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'youxituoluo'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '游戏陀螺资讯'
        self._site_name            = '游戏陀螺资讯'
        self._content              = cont
        self._channel              = '游戏'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_youxiputao(self,response):
        print(str(response.url)[8:])
        title    = response.xpath('//div[@class="title-box"]/h2/text()').extract()[0]
        cont     = response.xpath('//div[@class="cover"]').extract()[0]
        cont     += response.xpath('//div[@class="info"]').extract()[0]
        tag     = response.xpath('//div[@class="pull-left"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'youxiputao'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '游戏'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_xinlangyijianlingxiu(self,response):
        title    = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        cont     = response.xpath('//div[@id="artibody"]').extract()[0]
        pubtime  = str(response.xpath('//span[@id="pub_date"]/text()').extract()[0]).replace('年','-').replace('月','-').replace('日','')
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M"))*1000)
        author   = response.xpath('//span[@class="art_author"]/text()').extract()[0]
        for i in author.split(':'):
            author = i
        tag  = response.xpath('//div[@class="art_keywords"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'xinlangyijianlingxiu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '新浪意见领袖'
        self._site_name            = '新浪意见领袖'
        self._content              = cont
        self._channel              = '财经'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_weifengxinwen(self,response):
        title    = response.xpath('//div[@class="detail_title"]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="detail_content"]').extract()[0]
        self._name                 = 'weifengxinwen'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '威锋新闻'
        self._site_name            = '威锋新闻'
        self._content              = cont
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_weifengkeji(self,response):
        title    = response.xpath('//a[@class="h2"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="detail_content"]').extract()[0]
        author   = response.xpath('//div[@class="meta clear"]/a/text()').extract()[0]
        tag      = response.xpath('//div[@class="meta clear"]/span/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'weifengkeji'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '威锋科技'
        self._site_name            = '威锋科技'
        self._content              = cont
        self._channel              = '科技'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url



    def parse_weifengguandian(self,response):
        title    = response.xpath('//div[@class="view_title"]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="text"]').extract()[0]
        pubtime  = response.xpath('//p[@class="article_time"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="user_des"]/p/em/a/text()').extract()[0]
        self._name                 = 'weifengguandian'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '威锋观点'
        self._site_name            = '威锋观点'
        self._content              = cont
        self._channel              = '科技'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

        

    def parse_wangyiyishu(self,response):
        cont = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@class="post_text"]/p').extract()
        for p in content:
            cont += p
        pubtime  = self.get_time(response.xpath('//div[@class="post_time_source"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="ep-source cDGray"]/span[2]/text()').extract()[0]
        for a in author.split('：'):
            author = a
        self._name                 = 'wangyiyishu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '网易艺术'
        self._site_name            = '网易艺术'
        self._content              = cont
        self._channel              = '娱乐'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url 
   

    def parse_wangyirenjian(self,response):
        cont = ''
        title    = response.xpath('//div[@class="bannertext"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@class="endText"]/p | //div[@class="endText"]/img').extract()
        for p in content:
            if 'class="end"' not in p:
                cont += p
        pubtime  = self.get_time(response.xpath('//div[@class="pub_time"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M:%S"))*1000)
        self._name                 = 'wangyirenjian'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '网易人间'
        self._site_name            = '网易人间'
        self._content              = cont
        self._channel              = '生活'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url        


    def parse_wangyitech(self,response):
        cont = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@class="post_text"]/p').extract()
        for p in content:
            if 'otitle' not in p:
                cont += p
        pubtime  = self.get_time(response.xpath('//div[@class="post_time_source"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="ep-source cDGray"]/span[2]/text()').extract()[0]
        for a in author.split('：'):
            author = a
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'wangyikeji'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_wangyiguojixinwen(self,response):
        cont = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@class="post_text"]/p').extract()
        for p in content:
            if 'otitle' not in p:
                cont += p
        pubtime  = self.get_time(response.xpath('//div[@class="post_time_source"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="ep-source cDGray"]/span[2]/text()').extract()[0]
        for a in author.split('：'):
            author = a
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'wangyiguojixinwen'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._channel              = '国际'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_wangyidianshi(self,response):
        cont      = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@id="endText"]/p').extract()
        for p in content:
            if '<style>' not in p:
                cont += p
        pubtime  = self.get_time(response.xpath('//div[@class="post_time_source"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="ep-source cDGray"]/span[2]/text()').extract()[0]
        for a in author.split('：'):
            author = a
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'wangyidianshi'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_wangyiaiwan(self,response):
        cont = ''
        title    = response.xpath('//h1[@class="article-h1"]/text()').extract()[0]
        content     = response.xpath('//div[@id="endText"]/p').extract()
        for p in content:
            if '<style>' not in p:
                cont += p
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'wangyiaiwan'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '游戏'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url
        


    def parse_waitan(self,response):
        title    = response.xpath('//h2[@id="activity-name"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="rich_media_content "]').extract()[0]
        cont = cont.replace('"外滩TheBund（the-bund）"','')
        author   =  response.xpath('//div[@class="reward-author"]/text()').extract()[0]
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'waitan'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._channel              = site[2:]
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

 
    def parse_vogue(self,response):
        cont = ''
        title    = response.xpath('//h1[@class="artitle"]/text()').extract()[0]
        content  = response.xpath('//div[@class="artile-bodycont"]/p').extract()
        for a in content:
            cont += a 
        author   = response.xpath('//div[@class="art-author clearfix"]/span[1]/text()').extract()[0]
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'vogue'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._channel              = '时尚'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url
        

 
    def parse_tengxunnomal(self,response):
        print(str(response.url)[8:])
        cont = ''
        title    = response.xpath('//div[@class="LEFT"]/h1/text()').extract()[0]
        content     = response.xpath('//div[@class="content-article"]/p').extract()
        for p in content:
            cont += p
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'tengxunnormal'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '资讯'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_tengxundajia(self,response):
        title    = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@id="articleContent"]').extract()[0]
        pubtime  = response.xpath('//span[@class="publishtime"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d"))*1000)
        self._name                 = 'tengxundajia'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '腾讯大家'
        self._site_name            = '腾讯大家'
        self._content              = cont
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


 
    def parse_tengxuntiyu(self,response):
        cont = ''
        title    = response.xpath('//div[@class="hd"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="Cnt-Main-Article-QQ"]/p').extract()
        for i in content:
            if '</script>' not in i:
                cont += i
        pubtime  = str(response.xpath('//span[@class="a_time"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M"))*1000)
        author   = response.xpath('//div[@class="qq_editor"]/text()').extract()[0]
        for i in author.split('：'):
            author = i
        tag      = response.xpath('//div[@id="videokg"]/span/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'tengxuntiyu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '体育'
        self._tags                 = str(tags).replace('\'','"')
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_taimeiti(self,response):
        title    = response.xpath('//div[@class="post-container c-page"]/article/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="inner"]').extract()[0]
        pubtime  = response.xpath('//span[@class="time "]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M"))*1000)
        tag      = response.xpath('//span[@class="tag "]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        author   = response.xpath('//div[@class="post-info"]/a/@title').extract()[0]
        self._name                 = 'taimeiti'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '钛媒体'
        self._site_name            = '钛媒体'
        self._content              = cont
        self._channel              = '科技'
        self._tags                 = str(tags).replace('\'','"')
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url



    def parse_shuziweiba(self,response):
        title    = response.xpath('//div[@class="v-banner-info"]/h3/text()').extract()[0]
        cont     = response.xpath('//div[@class="forum-viewthread-article-box"]').extract()[0]
        div      = response.xpath('//div[@class="tip tip_4 aimg_tip"]').extract()
        for i in div:
            cont = cont.replace(i,'') 
        self._name                 = 'shuziweiba'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '数字尾巴'
        self._site_name            = '数字尾巴'
        self._content              = cont
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

  
    def parse_shuizhuyu(self,response):
        title    = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        cont     = response.xpath('//div[@id="artibody"]').extract()[0]
        pubtime  = str(response.xpath('//span[@id="pub_date"]/text()').extract()[0]).replace('年','-').replace('月','-').replace('日','')
        pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M"))*1000)
        author   = response.xpath('//span[@class="author"]/a[1]/text()').extract()[0]
        tag     = response.xpath('//p[@class="art_keywords"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'shuizhuyu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '水煮娱'
        self._site_name            = '水煮娱'
        self._content              = cont
        self._channel              = '娱乐'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_shudu(self,response):
        cont = ''
        
        title    = response.xpath('//div[@class="left"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@id="endText"]/p').extract()
        for i in content:
            if '<style>'not in i:
                cont += i
        pt       = response.xpath('//p[@id="ptime"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M:%S"))*1000)
        self._name                 = 'shudu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '数读'
        self._site_name            = '数读'
        self._content              = cont
        self._channel              = '国内'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_shishangxiansheng(self,response):
        title    = response.xpath('//div[@class="post-title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="show-content"]').extract()[0]
        pt       = response.xpath('//div[@class="translate-middle-y"]/span[1]/small/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M"))*1000)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'shishangxiansheng'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '时尚'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_shiguangxinwen(self,response):
        title    = response.xpath('//div[@class="newsheadtit"]/h2/text()').extract()[0]
        cont     = response.xpath('//div[@id="newsContent"]').extract()[0]
        cont = cont.replace('</a>','').replace('</b>','')
        tag      = response.xpath('//div[@class="newskeyword clearfix lh18"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'shiguangxinwen'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '时光新闻'
        self._site_name            = '时光新闻'
        self._content              = cont
        self._channel              = '娱乐'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


 
    def parse_qingnianyanlun(self,response):
        cont = ''
        title    = response.xpath('//div[@class="post_content_main"]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="post_text"]/p').extract()
        cont = cont.replace('点击进入网易研究局>>','').replace('【精彩推荐】','').replace('移驾微信公号 看这里看不到的内容','').replace('网易研究局（微信公号：wyyjj163） 出品','').replace('网易研究局是网易新闻打造的财经专业智库，整合网易财经原创多媒体矩阵，依托于上百位国内外顶尖经济学家的智慧成果，针对经济学热点话题，进行理性、客观的分析解读，打造有态度的前沿财经智库。','')
        pt  = self.get_time(response.xpath('//div[@class="post_time_source"]/text()').extract()[0])
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//div[@class="ep-source cDGray"]/span[2]/text()').extract()[0]
        for a in author.split('：'):
            author = a
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'wangyiyanjiuju'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '财经'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def get_time(self,st):
        date = re.search(r'(\d+).+(\d+:\d+:\d+)',st).group(0)
        date = date.replace(' ','').replace('\n','')
        return date

    def parse_pengpai(self,response):
        title    = response.xpath('//h1[@class="news_title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="news_txt"]').extract()[0]
        pt       = response.xpath('//div[@class="news_about"]/p[2]/text()').extract()[0].replace(' ','').replace('\n','').replace('\t','')
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d%H:%M"))*1000)
        author   = response.xpath('//div[@class="news_about"]/p[1]/text()').extract()[0]
        tags     = []
        tag      = response.xpath('//div[@class="news_keyword"]/text()').extract()[0].replace('关键词 >> ','')
        for a in tag.split(','):
            
            tags.append(a)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'pengpai'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '生活'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        self._comment_list         = self.comment.get_comments(self._org_url,'20','澎湃')
        vlist = self.value_to_list()
        return vlist,0,response.url



    def parse_kexuesongshuhui(self,response):
        cont = ''
        title    = response.xpath('//span[@class="contenttitle"]/a/text()').extract()[0]
        content  = response.xpath('//div[@class="entry"]/p | //div[@class="wp-caption aligncenter"]').extract()
        for a in content:
            cont += a
        author  = response.xpath('//div[@class="metax_single"]/a/text()').extract()[0]
        tag     = response.xpath('//div[@class="metax_single"]/em/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = 'kexuesongshuhui'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '科学松鼠会'
        self._site_name            = '科学松鼠会'
        self._content              = cont
        self._channel              = '科学'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_kanchaiwang(self,response):
        cont = ''
        title    = response.xpath('//h1[@class="show_title"]/text()').extract()[0]
        content     = response.xpath('//div[@class="show_content"]/p').extract()
        for p in content:
            cont += p
        year     = response.xpath('//div[@class="show_time_y"]/b/text()').extract()[0]
        month    = response.xpath('//div[@class="show_time_m"]/text()').extract()[0]
        sec      = response.xpath('//div[@class="show_time_i"]/text()').extract()[0]
        pt       = year+'/'+month+' '+sec
        pubtime  = int(time.mktime(time.strptime(pt,"%Y/%m/%d %H:%M"))*1000)
        tags     = response.xpath('//a[@class="key"]/text()').extract()[0]
        self._name                 = 'kanchaiwang'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '砍柴网'
        self._site_name            = '砍柴网'
        self._content              = cont
        self._channel              = '科技'
        self._tags                 = '["'+str(tags)+'"]'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_jingjichang(self,response):
        title    = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        cont     = response.xpath('//div[@id="artibody"]').extract()[0]
        pt       = str(response.xpath('//span[@id="pub_date"]/text()').extract()[0]).replace('年','-').replace('月','-').replace('日','')
        author   = response.xpath('//div[@class="b_txt"]/h3/text()').extract()[0]
        for i in author.split('：'):
            author = i
        tag     = response.xpath('//p[@class="art_keywords"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d%H:%M"))*1000)
        self._name                 = 'jingjichang'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '竞技场'
        self._site_name            = '竞技场'
        self._content              = cont
        self._channel              = '体育'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_jiemian(self,response):
        cont = ''
        title    = response.xpath('//div[@class="article-header"]/h1/text()').extract()[0]
        img      = response.xpath('//div[@class="article-img"]').extract()[0]
        content  = response.xpath('//div[@class="article-content"]/*').extract()
        for i in range(len(content)-4):
            cont += content[i]
        cont = img + cont
        cont = cont.replace('欢迎你来微博找我们，请点这里。','').replace('也可以关注我们的微信公众号“界面文化”【ID:BooksAndFun】','').replace('……………………………………','')
        #author   = response.xpath('//span[@class="author"]/a/text()').extract()[0]
        author   = ''
        tag  = response.xpath('//div[@class="main-mate"]/a/text() | //div[@class="main-mate"]/spana/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'jiemian'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '娱乐'
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        self._comment_list         = self.comment.get_comments(self._org_url,'20','界面')
        vlist = self.value_to_list()
        return vlist,0,response.url
    
    def parse_huxiu(self,response):
        cont = ''
        title    = response.xpath('//div[@class="article-wrap"]/h1/text()').extract()[0]
        title = title.replace('\n','').replace('\r','').replace('\r','')
        img = response.xpath('//div[@class="article-img-box"]').extract()[0]
        content     = response.xpath('//div[@class="article-content-wrap"]/p | //div[@class="article-content-wrap"]/article').extract()
        for p in content:
            cont += p
        cont = img + cont
        cont = cont.replace('data-src','src')
        pt      = response.xpath('//span[@class="article-time pull-left"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M"))*1000)
        tags     = response.xpath('//ul[@class="transition"]/a/li/text()').extract()
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'huxiu'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '生活'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_huaerjiejianwen(self,response):
        title    = response.xpath('//div[@class="article__heading__title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="node-article-content"]').extract()[0]
        cont = str(cont).replace('</a>','').replace('*本文来自华尔街见闻（微信ID：wallstreetcn），编辑陶旖洁。更多精彩资讯请登陆','').replace('，或下载华尔街见闻APP。线索和反馈请发邮箱 ','').replace('am@wallstreetcn.com >    。* ','').replace('欢迎订阅见闻主编精选，每天10篇文章，让你读懂金融市场。','').replace('点击这里或扫描下图二维码订阅>>','')
        author   = response.xpath('//div[@class="from"]/span/text()').extract()[0].replace(' ','').replace('\n','')
        self._name                 = 'huaerjiejianwen'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '华尔街见闻'
        self._site_name            = '华尔街见闻'
        self._content              = cont
        self._channel              = '财经'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_tengxunomn(self,response):
        cont = ''
        title    = response.xpath('//div[@class="LEFT"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="content-article"]/p').extract()
        for p in content:
            cont += p
        tags     = []
        tag_cont = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
        for i in tag_cont.split(','):
            tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'tengxun'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '科技'
        self._tags                 = str(tags).replace('\'','"')
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_guoke(self,response):
        cont = ''
        title    = response.xpath('//h1[@id="articleTitle"]/text()').extract()[0]
        content     = response.xpath('//div[@class="document"]/div').extract()
        for a in content:
            cont += a
        comt_num = len(response.xpath('//ul[@class="cmts-list cmts-all cmts-hide"]/li'))
        tag      = response.xpath('//a[@class="label label-common"]/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'guoke'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '科学'
        self._comment_count        = comt_num
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url     


    def parse_fenghuang(self,response):
        cont = ''
        if response.xpath('//div[@class="yc_tit"]/h1/text()').extract() != []:
            title    = response.xpath('//div[@class="yc_tit"]/h1/text()').extract()[0]
            content   = response.xpath('//div[@id="yc_con_txt"]/p').extract()
            for i in content:
                cont += i
            author   = response.xpath('//div[@class="yc_tit"]/p/span[2]/text()').extract()[0]
            self._author               = author
            self._pub_time             = self.creat_time()
            self._src_pub_time         = self.creat_time()
        else:
            title    = response.xpath('//h1[@id="artical_topic"]/text()').extract()[0]
            cont     = response.xpath('//div[@id="main_content"]').extract()[0]
            pubtime  = response.xpath('//span[@itemprop="datePublished"]/text()').extract()[0].replace('年','-').replace('月','-').replace('日','')
            pubtime  = int(time.mktime(time.strptime(pubtime,"%Y-%m-%d %H:%M:%S"))*1000)
            self._pub_time             = pubtime
            self._src_pub_time         = pubtime
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'fenghuang'
        self._news_title           = title
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '历史'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_FT(self,response):
        title    = response.xpath('//h1[@class="story-headline"]/text()').extract()[0]
        cont     = response.xpath('//div[@class=" story-image image"]').extract()[0]
        content  = response.xpath('//div[@id="story-body-container"]/p').extract()
        for a in content:
            cont += a
        author   = response.xpath('//span[@class="story-author"]/a/text()').extract()[0]
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'FTzhongwenwang'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '生活'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_denghuangzhoukan(self,response):
        title    = response.xpath('//h1[@class="title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="jfont"]').extract()[0]
        tag      = response.xpath('//span[@class="keyword"]/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'fenghuangzhoukan'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._tags                 = str(tags).replace('\'','"')
        self._content              = cont
        self._channel              = '财经'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_ellemen(self,response):
        title    = response.xpath('//div[@class="title-txt"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="page-content"]').extract()[0]        
        pt       = response.xpath('//b[@class="data"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d"))*1000)
        tag      = response.xpath('//div[@class="bread-tag"]/b/text()').extract()
        del tag[0]
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])
        self._name                 = 'ellemen'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._tags                 = str(tags).replace('\'','"')
        self._content              = cont
        self._channel              = '时尚'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_diyicaijing(self,response):
        title    = response.xpath('//div[@class="article-full-content "]/h1/text()').extract()[0]
        cont     = response.xpath('//div[@class="article-content"]').extract()[0]
        author   = response.xpath('//div[@class="article-author-name text-center"]/text()').extract()[0]
        site     = self.rds.query(str(response.url)[8:])       
        self._name                 = 'diyicaijing'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._channel              = '财经'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_sohutoutiaohao(self,response):
        cont = ''
        content_str = ['返回搜狐，查看更多','责任编辑：']
        title    = response.xpath('//div[@class="text-title"]/h1/text()').extract()[0]
        content  = response.xpath('//article[@class="article"]/p | //article[@class="article"]/h1 | //article[@class="article"]/ul').extract()
        for i in content:
            if 'original-title' not in i:
                cont += i
        for a in content_str:
            cont = cont.replace(a,'')
        tag      = response.xpath('//span[@class="tag"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        pt       = response.xpath('//span[@class="time"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M"))*1000)
        site     = self.rds.query(str(response.url)[8:]) 
        self._name                 = 'sohutoutiaohao'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        self._comment_list         = self.comment.get_comments(self._org_url,'20','搜狐')
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_chuangshiji(self,response):
        content_str = ['欢迎关注“创事记”的微信订阅号：sinachuangshiji','（声明：本文仅代表作者观点，不代表新浪网立场。）','src="//n.sinaimg.cn/tech/transform/20171107/rTya-fynmzun0700720.jpg']
        title    = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        cont     = response.xpath('//div[@id="artibody"]').extract()[0]
        for a in content_str:
            cont = cont.replace(a,'')
        pt       = response.xpath('//span[@id="pub_date"]/text()').extract()[0].replace(' ','').replace('\n','')
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d%H:%M:%S"))*1000)
        author   = response.xpath('//span[@class="author"]/a/text()').extract()[0]
        tags     = response.xpath('//p[@class="art_keywords"]/a/text()').extract()[0]

        self._name                 = 'chuangshiji'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '创事记'
        self._site_name            = '创事记'
        self._content              = cont
        self._author               = author
        self._tags                 = '["'+tags+'"]'
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_chanpinguancha(self,response):
        title    = response.xpath('//h1[@class="topic-title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="topic-cover"]').extract()[0]
        cont     += response.xpath('//div[@class="article-content"]').extract()[0]
        pt       = response.xpath('//span[@class="release-date"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y/%m/%d"))*1000)
        author   = response.xpath('//div[@class="user-info"]/a/span/text()').extract()[0]
        tag      = response.xpath('//a[@class="article-tag"]/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        site     = self.rds.query(str(response.url)[8:])        
        self._name                 = 'jikegongyuan'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = site
        self._site_name            = site
        self._content              = cont
        self._author               = author
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url


    def parse_caozhi(self,response):
        cont = ''
        title    = response.xpath('//div[@class="brief"]/h1/text()').extract()[0]
        content  = response.xpath('//div[@class="endText"]/p').extract()
        for i in content:
            if '<style>'not in i and '<font color="#974806"' not in i:
                cont += i
        cont = cont.replace('想要在第一时间收到槽值文章的推送，欢迎关注我们的公众号，搜索“槽值”或者“caozhi163”就可以啦。','').replace('微博@槽值，有态度的情感吐槽，等你来撩。>    槽值已入驻简书专栏，下载简书app阅读更多。','')
        pt   = response.xpath('//div[@class="pub_time"]/text()').extract()[0]
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M:%S"))*1000)

        self._name                 = 'caozhi'
        self._news_title           = title
        self._pub_time             = pubtime 
        self._src_pub_time         = pubtime
        self._news_source          = '槽值'
        self._site_name            = '槽值'
        self._content              = cont
        self._channel              = '国内'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()
        return vlist,0,response.url

    def parse_36kr(self,response):
        js = json.loads(response.text)
        title    = js['data']['title']
        cont     = js['data']['content']
        cont     = cont.replace('36氪经授权转载。','')
        pt       = js['data']['published_at']
        pubtime  = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M:%S"))*1000)
        tag      = js['data']['extraction_tags'].encode('utf-8').decode('unicode_escape')
        tags     = re.findall('"(.+?)"',tag)
         
        self._name                 = '36kr'
        self._news_title           = title
        self._pub_time             = pubtime 
        self._src_pub_time         = pubtime
        self._news_source          = '36kr'
        self._site_name            = '36kr'
        self._content              = cont
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '科技'
        self._id                   = self.set_id()
        self._org_url              = 'http://36kr.com/p/'+str(js['data']['id'])+'.html'
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()

        return vlist,0,response.url


    def parse_1905wang(self,response):
        cont = ''   
        title    = response.xpath('//h1[@class="title"]/text()').extract()[0]
        content  = response.xpath('//div[@class="pic-content"]/p | //div[@class="pic-content"]/table').extract()
        for p in content:
            cont += p
        author   = ''
        for a in author.split('：'):
            author = a
        tag      = response.xpath('//div[@class="fl rel-label"]/a/text()').extract()
        tags = []
        for i in tag:
            i = i.replace('\n','').replace('\r','').replace('\t','')
            if i != '':
               tags.append(i)
        self._name                 = '1905wang'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '1905网'
        self._site_name            = '1905网'
        self._content              = cont
        self._tags                 = str(tags).replace('\'','"')
        self._channel              = '娱乐'
        self._author               = author
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._is_hot               = '1'
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()

        return vlist,0,response.url


    def parse_dafenghao(self,response):
        cont = ''
        title   = response.xpath('//div[@class="yc_tit"]/h1/text()').extract()[0]
        content = response.xpath('//div[@class="yc_con_txt"]/p').extract()
        for i in content:
            if '原标题:' not in i and 'style="color:' not in i:
                cont += i
        pt      = response.xpath('//p[@class="clearfix"]/a/span/text()').extract()[0]
        print(pt)
        pubtime = int(time.mktime(time.strptime(pt,"%Y-%m-%d %H:%M:%S"))*1000)
        author  = response.xpath('//p[@class="clearfix"]/a[2]/text()').extract()[0]
 
        self._name                 = 'dafenghao'
        self._news_title           = title
        self._pub_time             = pubtime
        self._src_pub_time         = pubtime
        self._news_source          = '大风号'
        self._site_name            = '大风号'
        self._content              = cont
        self._channel              = '生活'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()

        return vlist,0,response.url
 
    def parse_meirirenwu(self,response):
        
        title     = response.xpath('//div[@class="left-wrapper"]/h2/text()').extract()[0]
        cont      = response.xpath('//div[@class="imedia-article"]').extract()[0]
        
         
        cont = cont.replace('文章为面孔原创，尊重原创，侵权必究。','').replace('想看更多，请移步面孔（ID：miankongportrait）','').replace('本文为一点号作者原创，未经授权不得转载','')

        self._name                 = 'meirirenwu'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._news_source          = '每日人物'
        self._site_name            = '每日人物'
        self._content              = cont
        self._channel              = '娱乐'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()

        return vlist,0,response.url

    def parse_xueqiu(self,response):
        content = ''
        title    = response.xpath('//h1[@class="article__bd__title"]/text()').extract()[0]
        cont     = response.xpath('//div[@class="article__bd__detail"]/p').extract()
        for i in cont:
            content += i
        author   =  response.xpath('//div[@class="article__bd__from"]/a/text()').extract()[0]

        self._name                 = 'xueqiu'
        self._news_title           = title
        self._pub_time             = self.creat_time()
        self._src_pub_time         = self.creat_time()
        self._author               = author
        self._news_source          = '雪球网'
        self._site_name            = '雪球网'
        self._content              = content
        self._channel              = '财经'
        self._id                   = self.set_id()
        self._org_url              = response.url
        self._from_source          = 'qiyu'
        self._from_sources         = '["qiyu"]'
        vlist = self.value_to_list()

        return vlist,0,response.url


