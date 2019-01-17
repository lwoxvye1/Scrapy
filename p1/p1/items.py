# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class P1Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()

    title = scrapy.Field()

    info = scrapy.Field()


# 有些时候，我们需要根据需求对已有的自定义数据类(Item子类)进行拓展。如,test项目中又添加了一个
# 新spider负责爬取国外书籍，此类书籍的信息比以前多了一个译者字段，此时我们可以继承P1Item定义新类
"""
class P2Item(P1Item):
    translator = scrapy.Field()
"""