# -*- coding: utf-8 -*-
import os
import datetime

# Scrapy settings for scrapy_frame project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_frame'

SPIDER_MODULES = ['scrapy_frame.spiders']
NEWSPIDER_MODULE = 'scrapy_frame.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COMMANDS_MODULE = 'scrapy_frame.commands'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
FEED_EXPORT_ENCODING = 'utf-8'
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_frame.middlewares.ScrapyFrameSpiderMiddleware': 543,
#}
nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
if not (os.path.exists('./scrapy_frame/spiders/log')):
    os.mkdir('./scrapy_frame/spiders/log')
if not (os.path.exists('./scrapy_frame/spiders/log/'+str(nowdate)+'scrapy_log.txt')):
    file = open('./scrapy_frame/spiders/log/'+str(nowdate)+'scrapy_log.txt','w')


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_frame.middlewares.ScrapyFrameDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_frame.middlewares.ScrapyFrameDownloaderMiddleware': 543
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
    #'scrapy_frame.middlewares.MyproxiesSpiderMiddleware':125     
}
RETRY_ENABLED = True
RETRY_HTTP_CODES = ['403','505']
RETRY_TIMES = 1
DOWNLOAD_TIMEOUT = 60

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_frame.pipelines.YuyanjiaScrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 调度器中请求存放在redis中的key
SCHEDULER_QUEUE_KEY = '%(spider)s:requests'     
# 使用scrapy-redis里的去重组件，不使用scrapy默认的去重方式
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里的调度器组件，不使用默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停，redis请求记录不丢失
#SCHEDULER_PERSIST = True
# 默认的scrapy-redis请求队列形式（按优先级）
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式，请求先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈形式，请求先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
#REDIS_HOST = "10.30.180.221"
REDIS_HOST = "118.190.243.148"     
REDIS_PORT = 16379
#REDIS_PASS = 'xdrt@^oasdfasf=<'
REDIS_PARAMS={'password':'xdrt@^oasdfasf=<'}

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
