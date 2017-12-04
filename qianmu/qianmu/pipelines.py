# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import redis
import pymysql,pymysql.cursors
import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class CheckPipeline(object):
    def process_item(self, item, spider):
        # 检查本科生人数和研究生人数，二者至少有一个有值
        if item['undergraduate_num'] or item['postgraduate_num']:
            return item
        # 否则将该item丢弃
        raise DropItem('Missing undergraduate_num and postgradudate_num in %s' % item['name'])


# class RedisPipeline(object):
#
#     def __init__(self):
#         self.r = redis.Redis()
#
#     def process_item(self, item, spider):
#         self.r.sadd(spider.name, item['name'])
#         logger.info('redis: add %s to list %s' % (item['name'], spider.name))
#         return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='rock1204',
            db='qianmu',
            charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % key for key in cols]
        # sql = "INSERT INTO `universities` (" + ','.join(cols) + ")" \
        #                                                         "VALUES  (" + ','.join(['%s'] * 8) + ")"


        sql="INSERT INTO `universities`("+','.join(cols)+")VALUES("+','.join(["%s"]*8)+")"
        logger.info(sql)
        self.cur.execute(sql, values)
        self.conn.commit()
        logger.info(self.cur._last_executed)
        logger.info('mysql: add %s to universities' % item['name'])
        return item

    def close_spider(self, spider):
        """当spider被关闭时，这个方法被调用"""
        self.cur.close()
        self.conn.close()