# -*- coding: utf-8 -*-
import scrapy
from qianmu.items import UniversityItem
def filter(html):

    return html.replace('\t','').replace('\r\n','')


class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['140.143.192.76']

    start_urls = ['http://140.143.192.76:8002/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D']
    def __init__(self,max_num=0):
        super(UniversitySpider, self).__init__()
        self.logger.info('max crawl pages set is %s' % max_num)
        self.max_num =int(max_num)

    def parse(self, response):

        links = response.xpath('//*[@id="content"]/table//tr/td[2]/a/@href').extract()
        for i,link in enumerate(links):
            if self.max_num and self.max_num <= i:
                break
            if not link.startswith('http://'):
                link = 'http://140.143.192.76:8002/%s'% link
            request = scrapy.Request(link,callback =self.parse_university)
            request.meta['rank'] = i +1
            yield request
    def parse_university(self,response):
        response = response.replace(body =filter(response.text))
        self.logger.info(response.url)
        wiki = response.xpath('//div[@id="wikiContent"]')[0]
        item = UniversityItem(rank =response.meta['rank'],
            name =response.xpath('//div[@id="wikiContent"]/h1/text()').extract_first())
        keys = wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[1]/p/text()').extract()
        cols = wiki.xpath('./div[@class="infobox"]/table/tbody/tr/td[2]')
        values = [','.join(col.xpath('.//text()').extract()) for col in cols]
        data = dict((zip(keys, values)))
        item['country'] = data.get('国家','')
        item['state'] =data.get('州省','')
        item['city'] = data.get('城市','')
        item['undergraduate_num'] = data.get('本科生人数','')
        item['postgraduate_num'] = data.get('研究生人数','')
        item['website'] = data.get('网址','')
        yield item
        self.logger.info('item %s scraped' % item['name'])
        info ={item['name']:item}
        print(info)


