# -*- coding: utf-8 -*-

# Scrapy settings for Wenkuxiazai project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Wenkuxiazai'

SPIDER_MODULES = ['Wenkuxiazai.spiders']
NEWSPIDER_MODULE = 'Wenkuxiazai.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Wenkuxiazai (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# #为同一网站的请求设置请求延迟
# DOWNLOAD_DELAY = 3
# DOWNLOAD_TIMEOUT = 60 #请求超时的时间
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

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
#    'Wenkuxiazai.middlewares.WenkuxiazaiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Wenkuxiazai.middlewares.WenkuxiazaiDownloaderMiddleware': 543,
    'Wenkuxiazai.middlewares.ProxyMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Wenkuxiazai.pipelines.WenkuxiazaiPipeline': 300,
    'Wenkuxiazai.pipelines.MongoPipeline':400,
    # 'scrapy_redis.pipelines.RedisPipeline': 300#添加pipeline# 如果添加这行配置，每次爬取的数据也都会入到redis数据库中，所以一般这里不做这个配置
}

MONGO_URI = "192.168.8.211"#在全局配置mongodb连接需要的地址和数据库名称
MONGO_DB = "Runoob"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

from .get_dtip import get_ip
# PROXIES =
# PROXIES = [get_ip(0),get_ip(1),get_ip(2),get_ip(3),get_ip(4),get_ip(5),get_ip(6),get_ip(7),get_ip(8),get_ip(9)]
# print(PROXIES)

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"#替换scrapy调度器
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"#添加去重的class
# REDIS_URL = 'redis://127.0.0.1:6379'
# SCHEDULER = True#调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
# SCHEDULER_FLUSH_ON_START=False #设置重启爬虫时是否清空爬取队列,这样每次重启爬虫都会清空指纹和请求队列,一般设置为False
