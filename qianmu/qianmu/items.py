# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
def convert_int(s):
    if isinstance(s,int):
        return s
    if not s:
        return 0
    return int(s.strip().replace(',',''))


class UniversityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field(serializer=int)
    country = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    undergraduate_num = scrapy.Field()
    postgraduate_num = scrapy.Field()
    website = scrapy.Field()

if __name__=="__main__":
    u = UniversityItem(name='哈佛大学')
    u['country'] = '美国'
    u['state']='纽约'
    print(u['name'])
    print(u['state'])
    #打印实例化后的字段
    print(u.keys())  # dict_keys(['name', 'country', 'state'])
    # 打印出所有定义过的字段
    print(u.fields.keys())
    # 打印出所有的fields及其所有的序列化函数
    print(u.fields)
    # 判断某个item对象是否包含指定字段
    print('name' in u.fields)
    # 判断某个字段是否设置了值
    print('name' in u)
    print('undergraduate_num' in u )

    u2 = UniversityItem(u)
    print(u2)
    u2['undergraduate_num']=242
    print(u2)
    print(u)
    # 将item对象转换为字典对象
    u_dict = dict(u)
    print(type(u_dict))
    # 从一个字典对象中创建item对象
    u3 = UniversityItem(u_dict)
    print(u3)

    # 如果设置一个未定义的字段则会抛出异常
    u4 = UniversityItem({'unknow':123})




