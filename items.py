# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JinmenItem(Item):
    title = Field()
    content = Field()
    image_urls = Field()
    url = Field()
    images = Field()
    source = Field()
    author = Field()
    logo = Field()