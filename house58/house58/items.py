# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# def convert_int(s,int):
#     if isinstance(s,int):
#         return s
#     if not s:
#         return 0
#     return int(s.strip().replace(',',''))



class House58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rent = scrapy.Field(serializer=int)
    payment = scrapy.Field()
    lease = scrapy.Field()
    htype = scrapy.Field()
    orientation =scrapy.Field()
    apartment = scrapy.Field()
    area = scrapy.Field()
    Detaile_address = scrapy.Field()

