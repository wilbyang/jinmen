import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JinmenPipeline(object):
    def __init__(self):
        self.fs = open('result', 'a')
        pass
    def process_item(self, item, spider):
        self.fs.write(item['title'])
        return item