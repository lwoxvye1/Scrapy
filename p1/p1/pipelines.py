# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class P1Pipeline(object):
    #  这里定义__init__和close_spider方法，它不会来一个item就执行一边，只有最初第一个item来的时候
    #  才执行__init__，最后结束的时候才执行close

    # 需启用settings里的ITEM_PIPELINES=...
    def __init__(self):
        self.f = open(r"D:\学习\python\Scrapy\p1\p1\test_pipeline.json", "wb")

    def process_item(self, item, spider):
        context = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(context.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()
