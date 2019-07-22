# -*- coding: utf-8 -*-


import re
import sys
import time
import json
import redis
import random
import datetime
from scrapy_frame.redis_push import redis_push
sys.path.append('../../scrapy_frame')


class yuyan():
    def __init__(self):
        
        super(yuyan,self).__init__()
        self.rds        = redis_push()

    def extract(self,response):
        if 'https://feng.ifeng.com/index/recommendNews.json' in response.url:
            return self.parse_dafenghao(response)
        if 'http://www.yidianzixun.com/home/q' in response.url:
            return self.parse_meirirenwu(response)
        if 'http://www.1905.com/list-p-catid-220.html?page=1' in response.url:
            return self.parse_1905wang(response)
        if 'https://36kr.com/' in response.url:
            return self.parse_36kr(response)
        if 'http://caozhi.news.163.com/' in response.url:
            return self.parse_caozhi(response)
        if 'http://www.geekpark.net/column/' in response.url:
            return self.parse_chanpinguancha(response)
        if 'http://feed.mix.sina.com.cn/api/roll/get?pageid=402&lid=2559&num=20&versionNumber=1.2.8&page=1' in response.url:
            return self.parse_chuangshiji(response)
        if '://mp.sohu.com/apiV2/profile/newsListAjax?' in response.url:
            return self.parse_sohuapi(response)
        if 'https://www.cbnweek.com/topics' in response.url:
            return self.parse_diyicaijing(response)
        if 'http://www.ellemen.com' in response.url:
            return self.parse_ellemen(response)
        if 'http://www.ifengweekly.com/list.php' in response.url:
            return self.parse_fenghuangzhoukan(response)
        if 'http://www.ftchinese.com' in response.url:
            return self.parse_FT(response)
        if 'http://news.ifeng.com/listpage' in response.url and '4765' not in response.url and '4764' not in response.url and '4763' not in response.url and '4762' not in response.url:
            return self.parse_fenghuanglishi(response)
        if 'https://www.guokr.com/scientific/channel' in response.url:
            return self.parse_guoke(response)
        if 'http://games.qq.com' in response.url:
            return self.parse_tengxunyouxi(response)
        if 'https://wallstreetcn.com/' in response.url:
            return self.parse_huaerjiejianwen(response)
        if 'https://www.huxiu.com' in response.url and 'channel' not in response.url:
            return self.parse_huxiu(response)
        if 'https://www.huxiu.com/channel/' in response.url:
            return self.parse_huxiuchannel(response)
        if 'https://www.jiemian.com' in response.url:
            return self.parse_jiemian(response)
        if 'http://sports.sina.com.cn/zl/' in response.url:
            return self.parse_jingjichang(response)
        if 'http://www.ikanchai.com/'in response.url:
            return self.parse_kanchaiwang(response)
        if 'http://songshuhui.net' in response.url:
            return self.parse_kexuesongshuhui(response)
        if 'https://www.thepaper.cn' in  response.url:
            return self.parse_pengpai(response)
        if 'http://money.163.com/special/qingnianyanlun' in  response.url:
            return self.parse_qingnianyanlun(response)
        if 'http://news.mtime.com/' in  response.url:
            return self.parse_shiguangxinwen(response)
        if 'http://news.ifeng.com/listpage/4765' in  response.url or 'http://news.ifeng.com/listpage/4764' in response.url or 'http://news.ifeng.com/listpage/4763' in response.url or 'http://news.ifeng.com/listpage/4762' in response.url:
            return self.parse_shijieshi(response)
        if 'http://www.esquire.com.cn/' in  response.url:
            return self.parse_shishangxiansheng(response)
        if 'http://data.163.com/special/datablog/' in  response.url:
            return self.parse_shudu(response)
        if 'http://ent.sina.com.cn/zl/' in  response.url:
            return self.parse_shuizhuyu(response)
        if 'https://api.yii.dgtle.com/' in  response.url:
            return self.parse_shuziweiba(response)
        if 'http://yule.sohu.com' in response.url:
            return self.parse_sohudianying(response)
        if 'http://it.sohu.com' in response.url:
            return self.parse_sohukeji(response)
        if 'http://cul.sohu.com/' in response.url:
            return self.parse_sohuwenhua(response)
        if 'http://www.tmtpost.com/' in response.url:
            return self.parse_taimeiti(response)
        if 'http://sports.qq.com/l/cba/CBAleg' in response.url:
            return self.parse_tengxunCBA(response)
        if 'http://dajia.qq.com/' in response.url:
            return self.parse_tengxundajia(response)
        if 'https://pacaio.match.qq.com' in response.url:
            return self.parse_tengxunnormal(response)
        if 'https://new.qq.com/ch/tech' in response.url:
            return self.parse_tengxunkeji(response)
        if 'http://games.qq.com/tvgame/' in response.url:
            return self.parse_tengxunzhujiyouxi(response)
        if 'http://sports.qq.com/l/csocce' in response.url:
            return self.parse_tengxunzhongguozuqiu(response)
        if 'http://www.vogue.com.cn' in response.url:
            return self.parse_vogue(response)
        if 'http://www.bundpic.com' in response.url:
            return self.parse_waitan(response)
        if 'http://play.163.com/' in response.url and 'newtougaolist' not in response.url:
            return self.parse_wangyiaiwanredian(response)
        if 'http://play.163.com/special/newtougaolist/' in response.url:
            return self.parse_wangyiaiwanzhuanti(response)
        if 'http://money.163.com/special/002557S5/' in response.url:
            return self.parse_wangyicaijing(response)
        if 'http://ent.163.com/special/000381P3' in response.url:
            return self.parse_wangyidinashi(response)
        if 'http://ent.163.com/special/000381Q1' in response.url:
            return self.parse_wangyidinying(response)
        if 'http://temp.163.com/special/00804KVA' in response.url:
            return self.parse_wangyiguojixinwen(response)
        if 'http://tech.163.com/special/00097UHL/tech' in response.url:
            return self.parse_wangyijinriredian(response)
        if 'http://tech.163.com/special/blockchain' in response.url:
            return self.parse_wangyiqukuailian(response)
        if 'http://renjian.163.com/' in response.url:
            return self.parse_wangyirenjian(response)
        if 'http://tech.163.com/telecom' in response.url:
            return self.parse_wangyitongxin(response)
        if 'http://art.163.com/special/00999815/art_redian' in response.url:
            return self.parse_wangyiyishu(response)
        if 'http://tech.163.com/special/00097UHL/smart' in response.url:
            return self.parse_wangyizhineng(response)
        if 'http://ent.163.com/special/00032VQS/zongyi' in response.url:
            return self.parse_wangyizongyi(response)
        if 'http://tech.163.com/' == response.url:
            return self.parse_wangyizuixinkuaixun(response)
        if 'https://www.feng.com/view/' in response.url:
            return self.parse_weifengguandian(response)
        if 'https://tech.feng.com/' in response.url:
            return self.parse_weifengkeji(response)
        if 'https://news.feng.com' in response.url:
            return self.parse_weifengxinwen(response)
        if 'http://finance.sina.com.cn/zl/' in response.url:
            return self.parse_xinlangyijianlingxiu(response)
        if 'http://youxiputao.com/article/index/id/' in response.url:
            return self.parse_youxiputaoshendu(response)
        if 'http://www.youxituoluo.com/news' in response.url:
            return self.parse_youxituoluo(response)
        if 'http://money.163.com/special/zhikuzhuanlan2017/' in response.url:
            return self.parse_zhikuzhuanlan(response)
        if 'http://www.iceo.com.cn/' in response.url:
            return self.parse_zhonguoqiyejia(response)
        if 'http://www.jwview.com/' in response.url:
            return self.parse_zhongxinjingwei(response)
        if 'http://www.qdaily.com/' in response.url:
            return self.parse_haoqixinribao(response)
        if 'http://news.qq.com/' in response.url:
            return self.parse_tengxunxinwenzhongxin(response)
        if 'http://view.news.qq.com/' in response.url:
            return self.parse_tengxunjinrihuati(response)
        if 'http://daily.zhihu.com/' in response.url:
            return self.parse_zhihuribao(response)
        if 'https://pit.ifeng.com' in response.url:
            return self.parse_fenghuangzhiku(response)
        if 'https://www.toutiao.com/api/pc/feed/?' in response.url:
            return self.parse_jinritoutiaotuijian(response)
        if 'temp.163.com/special/00804KVA/cm_dujia.js' in response.url:
            return self.parse_wangyidujia(response)

    def parse_wangyidujia(self,response):
        urllist = []
        #print((response.body[14:-1]).decode('uf-8').encode('uf-8'))
        a = response.body[14:-1].decode('utf-8','ignore').replace('\n','').replace('\t','').replace(' ','')
        js = json.loads(a)
        for i in js:
            urllist.append(i['docurl'])
        print(urllist)
        
     
        return urllist,0

    def parse_jinritoutiaotuijian(self,response):
        urllist = []
        js = json.loads(response.body)
        for i in js['data']:
            urllist.append('https://www.toutiao.com/a'+i['group_id']+'/')
        if 'news_hot' in str(response.url):
            for i in urllist:
                self.rds.set_key_addtime(i[8:],'今日头条热点',480)
        else:
            for i in urllist:
                self.rds.set_key_addtime(i[8:],'今日头条推荐',480)
        return urllist,0

    def parse_fenghuangzhiku(self,response):
        urllist = []
        li = response.xpath('//div[@class="bt"]/h1/a/@href').extract()
        for i in li:
            urllist.append(i.replace('http','https'))
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'凤凰智库',480)
        return urllist,0

    def parse_zhihuribao(self,response):
        urllist = []
        li = response.xpath('//a[@class="link-button"]/@href').extract()
        for i in li:
            urllist.append('http://daily.zhihu.com'+i)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'知乎日报',480)
        return urllist,0


    def parse_tengxunjinrihuati(self,response):
        urllist = response.xpath('//div[@class="contopic"]/ul/li/a/@href').extract()
        li = response.xpath('//div[@class="ship"]/ul/li/a/@href').extract()
        for i in li:
            urllist.append('http://view.news.qq.com'+i)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯今日话题',480)
        return urllist,0

    def parse_tengxunxinwenzhongxin(self,response):
        urllist = []
        li = response.xpath('//div[@class="item major"]/div/div/a/@href').extract()
        for i in li:
            if '.html' in i:
                urllist.append(i.replace('http','https'))
                self.rds.set_key_addtime(i.replace('http','https'),'腾讯今日话题',480)
        return urllist,0

    def parse_haoqixinribao(self,response):
        urllist = []
        li = response.xpath('//a[@class="com-grid-article"]/@href | //a[@class="com-grid-key-article"]/@href').extract()
        #li = response.xpath('//a[@class="com-grid-article]/@href').extract()
        for i in li:
            urllist.append('http://www.qdaily.com/'+i)
        return urllist,0

    def parse_zhongxinjingwei(self,response):
        urllist = []
        li  = response.xpath('//div[@class="pic"]/a/@href').extract()
        for i in li:
            if 'www.' not in i:
                urllist.append('http://www.jwview.com'+i)
        return urllist,0

    def parse_zhonguoqiyejia(self,response):
        urllist = response.xpath('//div[@class="list_box3 clearfix"]/dl/dd/h3/a/@href').extract()
        return urllist,0

    def parse_zhikuzhuanlan(self,response):
        urllist = response.xpath('//ul[@class="active"]/li/div/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'智库专栏',480)
        return urllist,0

    def parse_youxituoluo(self,response):
        urllist = []
        li = response.xpath('//div[@class="nimg"]/a/@href').extract()
        for i in li:
            urllist.append('http://www.youxituoluo.com'+i)
        return urllist,0

    def parse_youxiputaoshendu(self,response):
        urllist = []
        li = response.xpath('//div[@class="news-info-box"]/a/@href').extract()
        for i in li:
            urllist.append('http://youxiputao.com'+i)
            if '14' in response.url:
                print(i)
                self.rds.set_key_addtime('http://youxiputao.com'+i[8:],'游戏葡萄资讯',480)
            if '18' in response.url:
                self.rds.set_key_addtime('http://youxiputao.com'+i[8:],'游戏葡萄专栏',480)
            if '13' in response.url:
                self.rds.set_key_addtime('http://youxiputao.com'+i[8:],'游戏葡萄深度',480)
        return urllist,0

    def parse_xinlangyijianlingxiu(self,response):
        urllist = response.xpath('//div[@class = "pic"]/a/@href').extract()
        return urllist,0

    def parse_weifengxinwen(self,response):
        urllist = response.xpath('//div[@class="newsOne_img"]/a/@href').extract() 
        return urllist,0

    def parse_weifengkeji(self,response):
        urllist = response.xpath('//div[@class="tech_news"]/ul/li/a/@href').extract()
        return urllist,0

    def parse_weifengguandian(self,response):
        urllist = response.xpath('//a[@class = "show_img"]/@href').extract()
        return urllist,0

    def parse_wangyizuixinkuaixun(self,response):
        urllist = response.xpath('//li[@class="list_item"]/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易最新快讯','600')
        return urllist,0

    def parse_wangyizongyi(self,response):    
        urllist = response.xpath('//a[@class="newsList-img"]/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易综艺','600')
        return urllist,0

    def parse_wangyizhineng(self,response):
        urllist = []
        for a in str(response.body).split(':'):
            if '//tech.163.com/1' in a:
                urllist.append('http:'+a[:47])
                self.rds.set_key_addtime('http:'+a[:47],'网易智能','600')
        return urllist,0

    def parse_wangyiyishu(self,response): 
        urllist = []
        for a in str(response.text).split(':'):
            if 'commenturl' in a:
                for i in a.split('"'):
                    if 'art.163.com' in i:
                        urllist.append('http:'+i)
        return urllist,0

    def parse_wangyitongxin(self,response):
        urllist = response.xpath('//h3[@class="bigsize "]/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易通信','600')
        return urllist,0   
 
    def parse_wangyirenjian(self,response):
        urllist = []
        li = response.xpath('//li/a/@href').extract()
        for i in range(len(li)):
            if 'renjian.163.com' in li[i] and 'special' not in li[i]:
                urllist.append(li[i])
        return urllist,0   
 
    def parse_wangyiqukuailian(self,response):
        urllist = response.xpath('//h3[@class="bigsize "]/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易区块链','600')
        return urllist,0

    def parse_wangyijinriredian(self,response):
        urllist = []
        for a in str(response.body).split(','):
            if 'docurl' in a:
                urllist.append(a[28:-1])
                self.rds.set_key_addtime(a[28:-1],'网易今日热点','600')
        return urllist,0

    def parse_wangyiguojixinwen(self,response):
        urllist = []
        for a in str(response.body).split(','):
            if 'docurl' in a:
                urllist.append(a[20:-1])
        if 'guonei' in response.url:
            for i in urllist:
                self.rds.set_key_addtime(i[8:],'网易国内新闻','600')
        else:
            for i in urllist:
                self.rds.set_key_addtime(i[8:],'网易国际新闻','600')
        return urllist,0

    def parse_wangyidinying(self,response):
        urllist = []
        for i in str(response.body).split(':'):
            if 'commenturl' in i:
                urllist.append('http:'+i[:-24])
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易电影','600')
        return urllist,0

    def parse_wangyidinashi(self,response):
        urllist = []
        for i in str(response.body).split(':'):
            if 'commenturl' in i:
                urllist.append('http:'+i[:-24])
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易电视','600')
        return urllist,0

    def parse_wangyicaijing(self,response):
        urllist = []
        for a in str(response.text).split(','):
            if 'docurl' in a:
                urllist.append(a[19:-1])
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易财经','600')
        return urllist,0


    def parse_wangyiaiwanzhuanti(self,response):
        urllist = response.xpath('//li[@class="m-list-item"]/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易爱玩专题','600')
        return urllist,0

    def parse_wangyiaiwanredian(self,response):
        urllist = response.xpath('//div[@class="jingxuan-item m-cover"]/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'网易爱玩热点资讯','600')
        return urllist,0

    def parse_waitan(self,response):
        urllist = []
        js = json.loads(response.body)
        for a in js:
            urllist.append(a['链接'])
        for i in urllist:
            if 'life' in response.url:
                self.rds.set_key_addtime(i[8:],'外滩生活','600')
            if 'style' in response.url:
                self.rds.set_key_addtime(i[8:],'外滩时尚','600')
            if 'culture' in response.url:
                self.rds.set_key_addtime(i[8:],'外滩文化','600')
        return urllist,0

    def parse_vogue(self,response):
        urllist = []
        li = response.xpath('//div[@class="ThList-contimgbox"]/a/@href').extract()
        for i in li:
            urllist.append('http:'+i)
        for i in urllist:
            if 'style' in response.url:
                self.rds.set_key_addtime(i[8:],'vogue风格展示','600')
            else:
                self.rds.set_key_addtime(i[8:],'vogue衣Q进阶','600')
        return urllist,0

    def parse_tengxunzhongguozuqiu(self,response):
        urllist = []
        li = response.xpath('//div[@id="articleLiInHidden"]').extract()[0]
        for a in li.split(','):
            if 'url' in a and 'img' not in a:
                urllist.append(a[5:-1])
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯中国足球','600')
        return urllist,0

    def parse_tengxunzhujiyouxi(self,response):
        urllist = []
        li    =  response.xpath('//div[@class="newsapp newslist"]/a/@href').extract()
        for i in li:
            s1 = re.search(r'\d+',i)
            s2 = re.search(r'(\d+\w+)',i)
            urllist.append('http://new.qq.com/omn/'+s1.group()+'/'+s2.group()[:-2]+'.html')
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯游戏主机','600')
        return urllist,0

    def parse_tengxunkeji(self,response):
        urllist =  response.xpath('//div[@class="detail"]/h3/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯科技','600')
        return urllist,0

    def parse_tengxunnormal(self,response):
        urllist = []
        js = json.loads(response.body)
        for i in js['data']:
            urllist.append(i['vurl'])
        for i in urllist:
            if 'star' in response.url:
                self.rds.set_key_addtime(i[8:],'腾讯星闻','600')
            if 'tv' in response.url:
                self.rds.set_key_addtime(i[8:],'腾讯电视','600')
            if 'movie' in response.url:
                self.rds.set_key_addtime(i[8:],'腾讯电影','600')
        return urllist,0

    def parse_tengxundajia(self,response):
        urllist =  response.xpath('//li[@class="items"]/div/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯大家','600')
        return urllist,0

    def parse_tengxunCBA(self,response):
        urllist = []
        li = response.xpath('//div[@id="articleLiInHidden"]').extract()[0]
        for a in li.split(','):
            if 'url' in a and 'img' not in a:
                urllist.append(a[5:-1])
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯CBA','600')
        return urllist,0

    def parse_taimeiti(self,response):
        urllist = []
        li = response.xpath('//li[@class="post_part clear"]/a/@href').extract()
        for i in li:
            urllist.append('http://www.tmtpost.com'+i)
        return urllist,0
   
    def parse_sohuwenhua(self,response):
        urllist = []
        li = response.xpath('//a/@href').extract()
        for a in li:
            if '/a/' in a and '#' not in a:
                urllist.append('http:'+a)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'搜狐文化','600')
        return urllist,0

    def parse_sohukeji(self,response):
        urllist = []
        li = response.xpath('//div[@data-role="news-item"]/h4/a/@href').extract()
        for i in li:
            urllist.append('http:'+i)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'搜狐科技','600')
        return urllist,0

    def parse_sohudianying(self,response):
        urllist = response.xpath('//a[@test="a"]/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'搜狐电影','600')
        return urllist,0

    def parse_shuziweiba(self,response):
        urllist = []
        for a in str(response.body).split('>'):
            if '/tid' in a:
                urllist.append('http://news.dgtle.com/thread-'+a[:-5]+'-1-1.html')
        del urllist[0]
        return urllist,0

    def parse_shuizhuyu(self,response):
        urllist = response.xpath('//div[@class = "pic"]/a/@href').extract()
        return urllist,0

    def parse_shudu(self,response):
        urllist = []
        li = ''
        ls = response.xpath('//script[@type="text/javascript"]').extract()
        for i in ls:
            li += i   
        for a in li.split(':'):
            if 'data.163.com' in a:
                urllist.append('http:'+a[:-18])
        return urllist,0

    def parse_shishangxiansheng(self,response):
        urllist = response.xpath('//div[@class="infinite-container channel-infinite-container row"]/a/@href').extract()
        for i in urllist:
            if 'talk' in response.url:
                self.rds.set_key_addtime(i[8:],'时尚先生谈资','600')        
            else:
                self.rds.set_key_addtime(i[8:],'时尚先生文化','600')
        return urllist,0

    def parse_shijieshi(self,response):
        urllist = response.xpath('//div[@class="box_pic"]/a/@href').extract() 
        for i in urllist:
            if '4765' in response.url:
                self.rds.set_key_addtime(i[8:],'世界史','600')
            if '4764' in response.url:
                self.rds.set_key_addtime(i[8:],'中国古代史','600')
            if '4763' in response.url:
                self.rds.set_key_addtime(i[8:],'中国近代史','600')
            if '4762' in response.url:
                self.rds.set_key_addtime(i[8:],'中国现代史','600')
        return urllist,0

    def parse_shiguangxinwen(self,response):
        urllist = response.xpath('//div[@class="news-cont"]/a/@href').extract()
        return urllist,0

    def parse_qingnianyanlun(self,response):
        print(response.url)
        urllist = response.xpath('//ul[@class="active"]/li/div/a/@href').extract()
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'青年言论','600')
        return urllist,0

    def parse_pengpai(self,response):
        urllist = []
        li = response.xpath('//div[@class="news_tu"]/a/@href').extract()
        for i in li:
            urllist.append('https://www.thepaper.cn/'+i)
        for i in urllist:
            if '25953' in response.url:
                self.rds.set_key_addtime(i[8:],'澎湃生活','600')
            if '25842' in response.url:
                self.rds.set_key_addtime(i[8:],'澎湃私家地理','600')
        return urllist,0

    def parse_kexuesongshuhui(self,response):
        urllist = response.xpath('//p[@class="pic117"]/a/@href').extract()
        return urllist,0

    def parse_kanchaiwang(self,response):
        urllist = response.xpath('//div[@class="p"]/a/@href').extract()
        return urllist,0

    def parse_jingjichang(self,response):
        urllist = response.xpath('//div[@class = "pic"]/a/@href').extract()
        return urllist,0 

    def parse_jiemian(self,response):
        urllist = response.xpath('//div[@class="news-img"]/a/@href').extract()
        for i in urllist:
            if '79' in response.url:
                self.rds.set_key_addtime(i[8:],'界面文化','600')
            if '132' in response.url:
                self.rds.set_key_addtime(i[8:],'界面思想','600')
            if '31' in response.url:
                self.rds.set_key_addtime(i[8:],'界面消费','600')
            if '50' in response.url:
                self.rds.set_key_addtime(i[8:],'界面职场','600')
            if '/3.' in response.url:
                self.rds.set_key_addtime(i[8:],'界面歪楼','600')
            if '53' in response.url:
                self.rds.set_key_addtime(i[8:],'界面正午','600')
        return urllist,0

    def parse_huxiuchannel(self,response):
        urllist = []
        li = response.xpath('//div[@class="mod-thumb pull-left "]/a/@href').extract()
        for i in li:
            urllist.append('https://www.huxiu.com'+i)
        for i in urllist:
            if '22' not in response.url:
                self.rds.set_key_addtime(i[8:],'虎嗅生活腔调','600')
            else:
                self.rds.set_key_addtime(i[8:],'虎嗅娱乐淘金','600')
        return urllist,0

    def parse_huxiu(self,response):
        urllist = []
        li = response.xpath('//div[@class="mob-ctt index-article-list-yh"]/h2/a/@href').extract()
        for i in li:
            urllist.append('https://www.huxiu.com'+i)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'虎嗅','600')
        return urllist,0

    def parse_huaerjiejianwen(self,response):
        urllist = []
        li     = response.xpath('//div[@class="item-bottom"]/a[1]/@href').extract()
        for i in li:
            if 'premium' not in i:
                if 'https' in i:
                    urllist.append(i)
                else:
                    urllist.append('https://wallstreetcn.com'+i)
        return urllist,0

    def parse_tengxunyouxi(self,response):
        urllist = []
        li    =  response.xpath('//div[@class="newsapp newslist"]/a/@href').extract()
        for i in li:
            s1 = re.search(r'\d+',i)
            s2 = re.search(r'(\d+\w+)',i)
            urllist.append('http://new.qq.com/omn/'+s1.group()+'/'+s2.group()[:-2]+'.html')
        print(urllist)
        for i in urllist:
            self.rds.set_key_addtime(i[8:],'腾讯行业新闻','600')
        return urllist,0 

    def parse_guoke(self,response):
        urllist = response.xpath('//a[@data-gaevent="scientific_image:v1.1.1.1:scientific"]/@href').extract()
        for i in urllist:
            if 'hot' in response.url:
                self.rds.set_key_addtime(i[8:],'果壳热点','600')
            if 'fact' in response.url:
                self.rds.set_key_addtime(i[8:],'果壳谣言粉碎机','600')
            if 'frontier' in response.url:
                self.rds.set_key_addtime(i[8:],'果壳前沿','600')
            if 'viewpoint' in response.url:
                self.rds.set_key_addtime(i[8:],'果壳观点','600')
            if 'lifestyle' in response.url:
                self.rds.set_key_addtime(i[8:],'果壳生活方式','600')
        return urllist,0

    def parse_fenghuanglishi(self,response):
        urllist = response.xpath('//div[@class="con_lis"]/a/@href').extract()
        for i in urllist:
            if '41708' in response.url:
                self.rds.set_key_addtime(i[8:],'观世变','600')
            if '70296' in response.url:
                self.rds.set_key_addtime(i[8:],'蓝台说史','600')
        return urllist,0

    def parse_FT(self,response):
        urllist = []
        list_i = response.xpath('//a[@class="image"]/@href').extract()
        for i in list_i:
            if 'archive' not in i and '1800' in i:
                urllist.append('http://www.ftchinese.com/'+i.replace('#adchannelID=1800','?adchannelID=&full=y'))
            if 'archive' not in i and '1200' in i:
                urllist.append('http://www.ftchinese.com/'+i.replace('#adchannelID=1200','?adchannelID=&full=y'))
        for i in urllist:
            if 'lifestyle' in response.url:
                self.rds.set_key_addtime(i[8:],'FT生活时尚','600')
            if 'world' in response.url:
                self.rds.set_key_addtime(i[8:],'FT国际新闻','600')
        return urllist,0

    def parse_fenghuangzhoukan(self,response):
        urllist = []
        li = response.xpath('//div[@class="column"]/a/@href').extract()
        for i in li:
            urllist.append('http://www.ifengweekly.com/'+i)
        for i in urllist:
            if '=40' in response.url:
                self.rds.set_key_addtime(i[8:],'凤凰社会热点','600')
            if '=4' in response.url and '=40' not in response.url:
                self.rds.set_key_addtime(i[8:],'凤凰对话财经','600')
        return urllist,0

    def parse_ellemen(self,response):
        urllist = response.xpath('//a[@class="cover"]/@href').extract()
        for i in urllist:
            if 'culture' in response.url:
                self.rds.set_key_addtime(i[8:],'ellemen文化','600')
            if 'heat&' in response.url:
                self.rds.set_key_addtime(i[8:],'ellenmen世界','600')
        return urllist,0

    def parse_diyicaijing(self,response):
        urllist = []
        li = response.xpath('//a[@class="article-item-head"]/@href').extract()
        for i in li: 
            urllist.append('https://www.cbnweek.com'+i)
        for i in urllist:
            if '28' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经新鲜事','600')
            if '36' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经时尚时刻','600')
            if '34' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经读新数','600')
            if '18' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经商业家','600')
            if '10' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经新一线','600')
            if '31' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经金字招牌','600')
            if '14' in response.url:
                self.rds.set_key_addtime(i[8:],'第一财经新闻','600')
        return urllist,0

    def parse_sohuapi(self,response):
        urllist = []
        for a in str(response.text).split(','):
            if '//www.sohu.com/a' in a: 
                i = re.search('(\d+_\d+)',a).group()
                urllist.append('https://www.sohu.com/a/'+i)
        for i in urllist:
            if 'bGFubGFuZGUyMkBzb2h1LmNvbQ' in response.url:
                self.rds.set_key_addtime(i[8:],'三条','600')
            if 'NzJCMERBNUNDN0NEODJBOTkwMTZFMkM2NkU3REM3QjBAcXEuc29odS5jb20' in response.url:
                self.rds.set_key_addtime(i[8:],'数字之道','600')
            if 'ZmVpbHUyMTAxMjdAc29odS1pbmMuY29t' in response.url:
                self.rds.set_key_addtime(i[8:],'知世','600')
            if 'c29odW1wdW90b2lnQHNvaHUuY29t' in response.url:
                self.rds.set_key_addtime(i[8:],'有意思报告','600')
            if 'OTk5ODc4NDQ3MjUxODE2NDQ4QHNvaHUuY29t' in response.url:
                self.rds.set_key_addtime(i[8:],'大唐云文化','600')
            if 'ODM0RTFCREY0RTQ3RkRGMkY1NDlBMDJEQjlCRkMxMEFAcXEuc29odS5jb20' in response.url:
                self.rds.set_key_addtime(i[8:],'字媒体','600')
            if 'RUNENjAzMzY1RDZBRUQ0RTlGOEE3MEEwODA3OTMxMUFAcXEuc29odS5jb20' in response.url:
                self.rds.set_key_addtime(i[8:],'水木然','600')
            if 'c29odXptdHo1eXk3cEBzb2h1LmNvbQ' in response.url:
                self.rds.set_key_addtime(i[8:],'神吐槽','600')
        return urllist,0

    def parse_chuangshiji(self,response):
        urllist = []
        js = json.loads(response.text)
        for a in js['result']['data'] :
            urllist.append(a['url'])
        return urllist,0

    def parse_chanpinguancha(self,response):
        urllist = []
        li = response.xpath('//div[@class="article-info"]/a[2]/@href').extract()
        for i in li:
            urllist.append('http://www.geekpark.net'+i)
        for i in urllist:
            if '177' in response.url:
                self.rds.set_key_addtime(i[8:],'顶楼topview','600')
            if '85' in response.url:
                self.rds.set_key_addtime(i[8:],'产品观察','600')
            if '91' in response.url:
                self.rds.set_key_addtime(i[8:],'极客指南','600')
        return urllist,0

    def parse_caozhi(self,response):
        urllist = response.xpath('//a[@target= "_blank"]/@href').extract()
        return urllist,0

    def parse_dafenghao(self,response):
        urllist = []
        js = json.loads(response.text)
        for i in js:
            urllist.append(i['url'])
        return urllist,0
     
    def parse_1905wang(self,response):
        urllist = response.xpath('//ul[@class="pic-event-over"]/li/a/@href').extract()
        return urllist,0

    def parse_36kr(self,response):
        urllist = []
        print('=====================================')
        for a in str(response.text).split(':'):
            if '","summary"' in a and len(a) > 15 and len(a) < 20:
                urllist.append('http://36kr.com/api/post/'+a[1:-11]+'/next?_=1533025906826')
        return urllist,0

