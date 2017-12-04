from scrapy.exceptions import NotConfigured
import random

class RandonProxyMiddleware(object):
    def __init__(self,setting):
        self.proxies =setting.getlist('PROXIES')

    def random_proxy(self):

        return random.choice(self.proxies)

    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        if not crawler.settings.getlist('PROXIES'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self,request,spider):
        if 'proxy' not in request.meta:
            request.meta['proxy']=self.random_proxy()

