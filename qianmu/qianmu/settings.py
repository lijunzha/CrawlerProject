# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'

# Obey robots.txt rules
# 是否遵循robots.txt的规则
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求的数量
CONCURRENT_REQUESTS = 1
# 使用代理
HTTPPROXY_ENABLED = True
PROXIES = ['http://pc1120:pc1120@123.249.34.10:888', 'http://pc1120:pc1120@1.82.230.113:888']
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 请求延迟的时间(秒)，如果为0，则没有延迟
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否使用cookie，如果没有必要，最好把它关闭
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 是否启用telnet控制台，默认启用
TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# scrapy下载网页时使用的请求头信息
DEFAULT_REQUEST_HEADERS = {
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://www.baidu.com/link?url=lR44Mdx-lq-L1W4-LRe-PaM1Rmge-AImqd7QU-zfnZNhHkcP2Oiadj_5KuV3XwGUooEo4DSIHpJ9WYkBJjKYLbhdASlWHvkvD5y9Rb28Z8FUgoM9gIVebmz0norpY4BG&wd=&eqid=9bd3efd800012079000000025a1f9ec0",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'qianmu.middlewares.useragent.RandomUserAgentMiddleware': 500,
    'qianmu.middlewares.proxy.RandomProxyMiddleware': 749,

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#     'scrapy.extensions.corestats.CoreStats':500,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'qianmu.pipelines.CheckPipeline': 300,
    # 'qianmu.pipelines.RedisPipeline': 301,
    'qianmu.pipelines.MysqlPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
