# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymysql
import pymysql.cursors
import logging
logger =logging.getLogger(__name__)
logger.setLevel('DEBUG')
class CheckPipeline(object):
    def process_item(self,item,spider):
        if item['rent'] and item['payment']:
            return item
        raise DropItem('Miss rent or payment in %s' % item['title'])



class House58Pipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipleline(object):
    def __init__(self):
        self.conn = None
        self.cur = None
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = 'rock1204',
            db = 'house58',
            charset ='utf8'
        )
        self.cur = self.conn.cursor()
    def process_item(self,item,spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % key for key in cols]
        sql = "INSERT INTO `h58` ("+','.join(cols)+") VALUES ("+','.join(["%s"]*9)+")"
        # sql = "INSERT INTO `universities`(" + ','.join(cols) + ")VALUES(" + ','.join(["%s"] * 8) + ")"
        logger.info(sql)
        self.cur.execute(sql,values)
        self.conn.commit()
        logger.info(self.cur._last_executed)
        logger.info('mysql:add %s to h58' % item['title'])
        return item
