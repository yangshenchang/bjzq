# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class BjzqSpiderPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.bjzq.news.insert_one(item)
        return item

    def spider_close(self,spider):
        self.client.close()
