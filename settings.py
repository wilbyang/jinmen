# Scrapy settings for jinmen project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jinmen.com'

SPIDER_MODULES = ['jinmen.spiders']
NEWSPIDER_MODULE = 'jinmen.spiders'
ITEM_PIPELINES = {#'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
'jinmen.imagespiple.ImagesPipeline':1,
'jinmen.pipelines.JinmenPipeline':2
}
IMAGES_STORE = 'images'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jinmen (+http://www.yourdomain.com)'
IMAGES_THUMBS = {
    'big': (270, 270),
}



### crawling control  ###  cyzone.cn ###
CYZONE_ALLOWED_DOMAINS = ['www.cyzone.cn']
CYZONE_START_URLS = ['http://www.cyzone.cn/category/18/', 'http://www.cyzone.cn/category/19/', 'http://www.cyzone.cn/category/20/', 'http://www.cyzone.cn/category/22/', 'http://www.cyzone.cn/category/709/']
CYZONE_TITLE_XPATH = "//h1[@class='Article_h3']/text()"
CYZONE_CONTENT_XPATH = "//div[@id='text']"
CYZONE_AUTHOR_XPATH = u"//div[@class='copyform']/span[contains(., '\u4f5c\u8005\uff1a')]/span/text()"
CYZONE_SOURCE_XPATH = u"//div[@class='copyform']/span[contains(., '\u6765\u6e90\uff1a')]/span/text()"
CYZONE_IMAGES_XPATH = "//div[@id='text']//img/@src"
CYZONE_LIST_REGEX = 'category/\d+/index_\d+\.html'
CYZONE_ITEM_REGEX = 'a/\d+/\d+\.html'
CYZONE_LIST_RESTRICT_XPATHS = "//div[@class='left']"
CYZONE_ITEM_RESTRICT_XPATHS = "//div[@class='left']"

LIEYUN_ALLOWED_DOMAINS = ['www.lieyunwang.com']
LIEYUN_START_URLS = ['http://www.lieyunwang.com/archives/category/internet']
LIEYUN_TITLE_XPATH = "//div[@class='hd']/h2/text()"
LIEYUN_CONTENT_XPATH = "//div[@class='post_thumbnail']/following-sibling::div[position()=1]"
LIEYUN_AUTHOR_XPATH = "//div[@class='hd']//span[@class='author vcard']/a/text()"
LIEYUN_SOURCE_XPATH = ""
LIEYUN_IMAGES_XPATH = "//div[@class='post_thumbnail']/img/@src"
LIEYUN_LIST_REGEX = 'archives/category/internet/page/\d+'
LIEYUN_ITEM_REGEX = 'archives/\d+'
LIEYUN_LIST_RESTRICT_XPATHS = "//div[@id='pagenavi']"
LIEYUN_ITEM_RESTRICT_XPATHS = "//div[@class='listzone']"



IRESEARCH_ALLOWED_DOMAINS = ['column.iresearch.cn']
IRESEARCH_START_URLS = ['http://column.iresearch.cn/expert_app/']
IRESEARCH_TITLE_XPATH = "//h1[@class='content_title']/text()"
IRESEARCH_CONTENT_XPATH = "//div[@class='content_Article']"
IRESEARCH_AUTHOR_XPATH = "//div[@class='hd']//span[@class='author vcard']/a/text()"
IRESEARCH_SOURCE_XPATH = "//XXHH"
IRESEARCH_IMAGES_XPATH = "//XXHH"
IRESEARCH_LIST_REGEX = 'expert_app_\d+'
IRESEARCH_ITEM_REGEX = 'u/.+/\d+\.shtml'
IRESEARCH_LIST_RESTRICT_XPATHS = "//ul[@class='page']"
IRESEARCH_ITEM_RESTRICT_XPATHS = "//ul[@class='ul_ellipsis_2 column_list font_Large']"

CURRENTSET = 'IRESEARCH_'







SOUHUBSSCHOOL_ALLOWED_DOMAINS = ['bschool.sohu.com']
SOUHUBSSCHOOL_START_URLS = ['http://bschool.sohu.com/xyfx/index.shtml']
SOUHUBSSCHOOL_TITLE_XPATH = "//h1[@itemprop='headline']/text()"
SOUHUBSSCHOOL_CONTENT_XPATH = "//div[@itemprop='articleBody']"
SOUHUBSSCHOOL_AUTHOR_XPATH = "//div[@class='hd']//span[@class='author vcard']/a/text()"
SOUHUBSSCHOOL_SOURCE_XPATH = "//span[@id='media_span']/span"
SOUHUBSSCHOOL_IMAGES_XPATH = "//XXHH"
SOUHUBSSCHOOL_LIST_REGEX = 'expert_app_\d+'
SOUHUBSSCHOOL_ITEM_REGEX = 'u/.+/\d+\.shtml'
SOUHUBSSCHOOL_LIST_RESTRICT_XPATHS = "//ul[@class='page']"
SOUHUBSSCHOOL_ITEM_RESTRICT_XPATHS = "//ul[@class='ul_ellipsis_2 column_list font_Large']"



ONLINEEDU_ALLOWED_DOMAINS = ['www.online-edu.org/']
ONLINEEDU_START_URLS = ['http://www.online-edu.org/html/category/news/view','http://www.online-edu.org/html/category/news/overseanews','http://www.online-edu.org/html/category/news/chinanews','http://www.online-edu.org/html/category/articals/column-article','http://www.online-edu.org/html/category/articals/overseas-articals']


ONLINEEDU_TITLE_XPATH = "//h2"
ONLINEEDU_CONTENT_XPATH = "//div[@itemprop='articleBody']"
ONLINEEDU_AUTHOR_XPATH = "//div[@class='hd']//span[@class='author vcard']/a/text()"
ONLINEEDU_SOURCE_XPATH = "//span[@id='media_span']/span"
ONLINEEDU_IMAGES_XPATH = "//XXHH"
ONLINEEDU_LIST_REGEX = 'expert_app_\d+'
ONLINEEDU_ITEM_REGEX = 'html/[2]/\d+\.html'
ONLINEEDU_LIST_RESTRICT_XPATHS = "//div[@class='pagination']"
ONLINEEDU_ITEM_RESTRICT_XPATHS = "//ul[@id='post_container']"



#### db related ###
DBUSER ='root'
DBPWD ='yangbo'
DB ='jinmen'
DBHOST ='192.168.1.154'
