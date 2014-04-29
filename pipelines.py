import sys
import MySQLdb
import hashlib
import re
from scrapy.exceptions import DropItem
from scrapy.http import Request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JinmenPipeline(object):


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    def __init__(self, settings):

        DBUSER = settings.get('DBUSER')
        DBPWD = settings.get('DBPWD')
        DBHOST = settings.get('DBHOST')
        DB = settings.get('DB')
        #self.conn = MySQLdb.connect(user='comein', passwd='ckleague168', db='comein', host='10.161.141.62', charset="utf8", use_unicode=True)
        #self.conn = MySQLdb.connect(user='root', passwd='yangbo', db='jinmen', host='192.168.1.154', charset="utf8", use_unicode=True)
        self.conn = MySQLdb.connect(user=DBUSER, passwd=DBPWD, db=DB, host=DBHOST, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        pass
    def process_item(self, item, spider):
        regex = re.compile(r'class=".*"|id=".*"|style=".*"', re.IGNORECASE)
        try:
            title = item['title'].encode("UTF-8")
            content =  re.sub(regex, '', item['content']).encode("UTF-8")
            url = item['url']
            author = item['author'].encode("UTF-8")
            source = item['source'].encode("UTF-8")
            logo = item['logo'].encode("UTF-8")
            self.cursor.execute("""insert into ts_column_tip(title, content, website, author, source, logo) values(%s, %s, %s, %s, %s, %s)""", (title, content, url, author, source, logo))
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item