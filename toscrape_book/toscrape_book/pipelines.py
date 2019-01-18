# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ToscrapeBookPipeline(object):
    def __init__(self):
        self.f = open(r"D:\学习\python\Scrapy\toscrape_book\toscrape_book\json.json", "wb")

    def process_item(self, item, spider):
        context = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(context.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()
