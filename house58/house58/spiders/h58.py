# -*- coding: utf-8 -*-
import scrapy

from house58.items import House58Item
def filter(html):
    # return html
    return html.replace('\t', '').replace('\r\n', '').replace('&nbsp;&nbsp;','')
    # return html.replace('\r\n','').replace('&nbsp;&nbsp;','')



class H58Spider(scrapy.Spider):
    name = 'h58'
    allowed_domains = ['bj.58.com']
    start_urls = ['http://bj.58.com/chuzu/']
    def __init__(self,max_num = 0):
        super(H58Spider, self).__init__()
        self.logger.info('max crawl pages set is %s % max_num')
        self.max_num = int(max_num)

    def parse(self, response):
        links = response.xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a/@href').extract()
        # self.logger.info(links)
        # print(links)
        for i,link in enumerate(links):
            if self.max_num and self.max_num <= i:
                break
            # print('链接是--------------：',link)
            request = scrapy.Request(link,callback = self.parse_house)
            # print('1232221222222222222222222222222222')
            yield request

    def parse_house(self,response):
        # print('555555555555555555555')
        response = response.replace(body = filter(response.text))
        self.logger.info(response.url)
        keys = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li/span[1]/text()').extract()
        # print('名称有------------：',keys)
        cols = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li/span[2]')

        values = [','.join(col.xpath('.//text()').extract())for col in cols]
        # print(('相应的值有-----------：', values))
        data = dict((zip(keys,values)))
        # print(data)
        item = House58Item(title = response.xpath('/html/body/div[4]/div[1]/h1/text()').extract_first(),
                           rent = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/span[1]/b/text()').extract_first(),
                           payment = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/span[2]/text()').extract_first())
        item['lease'] = data.get('租赁方式：','').strip()
        item['htype'] = data.get('房屋类型：', '').strip()
        item['orientation'] = data.get('朝向楼层：','').strip()
        item['apartment'] = data.get('所在小区：', '').strip()
        item['area'] = data.get('所属区域：', '').strip()
        item['Detaile_address'] = data.get('详细地址：', '').strip()
        yield item
        # self.logger.info('')
        # info ={item['title']:item}
        # print(item)
