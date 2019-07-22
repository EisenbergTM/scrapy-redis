import re
import os
import time
import json
import requests
import configparser
from urllib.parse import unquote
from scrapy_frame.redis_push import redis_push
from scrapy_frame.spiders.start_parse.xinle import xinle
from scrapy_frame.spiders.start_parse.yuyan import yuyan
from scrapy_frame.spiders.start_parse.dongjiu import dongjiu
from scrapy_frame.spiders.start_parse.guangle import guangle
from scrapy_frame.spiders.start_parse.meizhuang import meizhuang
from scrapy_frame.spiders.start_parse.leting import leting
from scrapy_frame.spiders.start_parse.aidi import aidi


class model(object):
    def __init__(self,response):
        self.xinle        = xinle()
        self.yuyan        = yuyan()
        self.dongjiu      = dongjiu()
        self.guangle      = guangle()
        self.meizhuang    = meizhuang()
        self.leting       = leting()
        self.aidi         = aidi()
        self.response = response
        self.url      = response.url
        
        self.config   = configparser.ConfigParser()
        self.config.read((os.getcwd()+'/config.ini'), encoding='utf-8')

    def select(self):
        urllist_dynamic         = ['http://www.yidianzixun.com/channel/m141747','https://xueqiu.com/']
        urllist_meizhuang       = ['weibo.com','https://www.zhihu.com/api/v4/columns/sanshokaken/articles?include=data%5B*%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following']
        urllist_xinle           = ['http://sy.yzz.cn','www.huoxing24.com','http://www.shouyou.com/','https://new.qq.com/ch/ent/','http://ent.163.com/special/000380VU/newsdata_index.js','http://www.9game.cn/news/13_1/','https://www.119you.com/news/']
        urllist_yuyan           = ['https://feng.ifeng.com/index/recommendNews.json','http://www.1905.com/list-p-catid-220.html?page=1','https://36kr.com/','http://caozhi.news.163.com/','http://www.geekpark.net/column/85','http://feed.mix.sina.com.cn/api/roll/get?pageid=402&lid=2559&num=20&versionNumber=1.2.8&page=1','mp.sohu.com/apiV2/profile/newsListAjax?','http://www.geekpark.net/column/177','https://www.cbnweek.com/topics/36','https://www.cbnweek.com/topics/14','https://www.cbnweek.com/topics/28','https://www.cbnweek.com/topics/34','http://www.ellemen.com/heat&hit/','http://www.ellemen.com/culture/','http://www.ifengweekly.com/list.php?lmid=4','http://www.ifengweekly.com/list.php?lmid=40','http://www.ftchinese.com/channel/world.html','http://www.ftchinese.com/channel/lifestyle.html','http://news.ifeng.com','https://www.guokr.com/scientific/channel/viewpoint/','https://www.guokr.com/scientific/channel/frontier/','https://www.guokr.com/scientific/channel/hot/','https://www.guokr.com/scientific/channel/lifestyle/','https://www.guokr.com/scientific/channel/fact/','http://games.qq.com/cyfw/sy/index.htm','https://wallstreetcn.com/news/global?from=navbar','https://www.huxiu.com','https://www.huxiu.com/channel/4.html','https://www.huxiu.com/channel/22.html','https://www.jiemian.com/lists/132.html','https://www.jiemian.com/lists/3.html','https://www.jiemian.com/lists/79.html','https://www.jiemian.com/lists/31.html','https://www.jiemian.com/','https://www.jiemian.com/lists/53.html','http://www.jiemian.com/lists/50.html','http://www.geekpark.net/column/91','http://sports.sina.com.cn/zl/','https://www.cbnweek.com/topics/31','http://www.ikanchai.com/','http://songshuhui.net/','https://www.thepaper.cn/channel_25953','https://www.thepaper.cn/list_25842','http://money.163.com','https://www.cbnweek.com/topics/18','http://news.mtime.com/','http://www.esquire.com.cn/c/talk/','http://www.esquire.com.cn/c/culture/','http://data.163.com/special/datablog/','http://ent.sina.com.cn/zl/','https://api.yii.dgtle.com/v2/news?token=&perpage=24&typeid=0','http://yule.sohu.com/movie.shtml','http://it.sohu.com/','http://cul.sohu.com/','http://www.tmtpost.com/','http://sports.qq.com/l/cba/CBAleg/CBAteams/CBAother/list2017062620355.htm','http://dajia.qq.com/','https://pacaio.match.qq.com/irs/rcd?cid=52&token=8f6b50e1667f130c10f981309e1d8200&ext=102,111,113&page=0&expIds=&','https://pacaio.match.qq.com/irs/rcd?cid=52&token=8f6b50e1667f130c10f981309e1d8200&ext=101&page=0&expIds=&','https://new.qq.com/ch/tech/','https://pacaio.match.qq.com/irs/rcd?cid=52&token=8f6b50e1667f130c10f981309e1d8200&ext=106,118,108&page=0','http://games.qq.com/tvgame/','http://sports.qq.com/l/csocce/list20160112153548.htm','http://www.vogue.com.cn/invogue/vogue-style/','http://www.vogue.com.cn/invogue/dress-q/','http://www.bundpic.com/postpage?n=12&p=1&c=life','http://www.bundpic.com/postpage?n=12&p=1&c=style','http://www.bundpic.com/postpage?n=12&p=1&c=culture','http://play.163.com/','http://ent.163.com/','http://temp.163.com/special/00804KVA','https://temp.163.com/special/00804KVA','http://renjian.163.com/','http://art.163.com/special/00999815/art_redian_api.js','http://tech.163.com/','https://www.feng.com/view/','https://tech.feng.com/','https://news.feng.com/','http://finance.sina.com.cn/zl/','https://www.cbnweek.com/topics/10','http://youxiputao.com','http://www.youxituoluo.com/news','http://www.iceo.com.cn/','http://www.jwview.com/','http://www.qdaily.com/','news.qq.com','http://daily.zhihu.com/','https://pit.ifeng.com','https://www.toutiao.com/api/pc/feed/?']
        urllist_dongjiu         = ['https://v.douyu.com/directory/catelist/49','https://v.douyu.com/directory/catelist/104','https://v.douyu.com/directory/catelist/134','https://v.douyu.com/directory/catelist/138','https://v.douyu.com/directory/catelist/5']
        urllist_guangle         = ['https://www.zcool.com.cn/discover/0!0!0!0!0!!!!-1!0!1']
        urllist_leting          = ['https://app.leting.io/auth?uid']
        urllist_aidi            = ['http://news.xiancity.cn/index.shtml','http://www.xasqw.com/web/items.aspx?id01=320','http://news.xiancn.com/node_10490.htm','http://www.xashangwang.com/html/swtt/']
        
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
        for i in urllist_xinle:
            if i in self.url:
                return self.xinle.extract(self.response)
        for i in urllist_yuyan:
            if i in self.url:
                return self.yuyan.extract(self.response)
        for i in urllist_dongjiu:
             if i in self.url:
                return self.dongjiu.extract(self.response)


        for i in urllist_dynamic:
            urllist = []
            tm = []
            if i == self.url:
                content = self.dynamic(self.url)[0]
                site    = self.dynamic(self.url)[1]
                if 'www.yidianzixun.com' in i:
                    tm = re.findall('href="(/article.+?)"',content)
                elif 'xueqiu.com' in i:
                    tm = re.findall('href="(/\d+/\d+?)"',content)
              
                 
                for i in tm:
                    urllist.append(str(site)+i) 
                print(urllist)
                return urllist,0
                
                

    def dynamic(self,url):
        site = ''
        lis = ['http://www.yidianzixun.com','https://xueqiu.com']
        for i in lis:
            if i in url:
                site = i
        post_url = 'http://114.215.18.7:29889/probe_address'
        mes_url  = str(site)+'|'+str(url)
        body = '{\
            "news_type":"1",\
            "url":"'+mes_url+'"\
        }'
        html = requests.post(url=post_url,data=body)
        time.sleep(5)
        js = json.loads(html.content)
        print(js)
        html = requests.get(js['query_url'])
        time.sleep(5)
        js = json.loads(html.content)
        hl = unquote(js['response'])
        return hl,site


      
	    
            

 
