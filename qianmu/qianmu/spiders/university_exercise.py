# -*- coding: utf-8 -*-
import scrapy

def filter(html):
    return html.replace('\t','').replace('\r\n','')

class UniversityExerciseSpider(scrapy.Spider):
    name = 'university_exercise'
    allowed_domains = ['140.143.192.76']
    start_urls = ['http://140.143.192.76:8002/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D']
    def __init__(self,max_num = 0):
        super(UniversityExerciseSpider, self).__init__()
        # 设置日志干什么？？？
        self.logger.info('max crawl pages set is %s'%max_num)
        self.max_num = int(max_num)
    def parse(self, response):

        links = response.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href').extract()
        print(links)
        for i,link in enumerate(links):
            ### ？？？？self.max_num
            # if self.max_num and self.max_num <= i:
            if  self.max_num <= i:
                break
            ### http://140.143.192.76:8002/苏黎世联邦理工学院  404
            if not link.startswith('http://'):
                link = 'http://140.143.192.76:8002/%s' % link
            request =scrapy.Request(link,callback=self.parse_university)
            ###???? rank
            request.meta['rank'] = i+1

            yield request

    def parse_university(self,response):
        response = response.replace(body=filter(response.text))
        # self.logger.info(response.url)
        wiki =response.xpath('//*[@id="wikiContent"]')[0]
        keys =wiki.xpath('//*[@id="wikiContent"]/div[1]/table/tbody/tr/td[1]/p/text()').extract()
        cols = wiki.xpath('//*[@id="wikiContent"]/div[1]/table/tbody/tr/td[2]/p')
        values =[','.join(col.xpath('.//text()').extract()) for col in cols]
        item =dict(rank = response.meta['rank'],
                   title =response.xpath('//*[@id="wikiContent"]/h1/text()').extract_first()
                   )
        item.update(zip(keys,values))

        yield item

        self.logger.info('item %s scraped' % item['title'])

        info={item['title']:item}
        print(info)
        
        
        






