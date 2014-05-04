from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.settings import Settings
from jinmen.items import JinmenItem
from scrapy.utils.project import get_project_settings
from itertools import *
class JinmenSpider2(CrawlSpider):

	name = 'jinmen.com'
	allowed_domains = ['www.36kr.com']
	start_urls = ['http://www.36kr.com']
	rules = (
		# Rule(SgmlLinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
		Rule(SgmlLinkExtractor(allow=('p/\d+\.html', )), callback='parse_item'),
	)	
	def parse_item(self, response):
		sel = Selector(response)
		item = JinmenItem()
		#item['id'] = sel.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
		item['title'] = sel.xpath('//title/text()').extract()[0]
		item['content'] = sel.xpath("//section[@class='article']").extract()[0]
		url = sel.xpath("//div[@class='single-post-header__headline']/img/@src").extract()[0]
		item['url'] = response.url
		item['image_urls'] = [url]
		return item
class JinmenSpider(CrawlSpider):

	name = 'cyzone.cn'
	settings = get_project_settings()
	CURRENTSET = settings.get('CURRENTSET')
	#allowed_domains = ['www.cyzone.cn']
	allowed_domains = settings.getlist(CURRENTSET + 'ALLOWED_DOMAINS')
	start_urls = settings.getlist(CURRENTSET + 'START_URLS')

	rules = (
		Rule(SgmlLinkExtractor(allow=(settings.get(CURRENTSET + 'LIST_REGEX')), restrict_xpaths=(settings.get(CURRENTSET+'LIST_RESTRICT_XPATHS')))),
		Rule(SgmlLinkExtractor(allow=(settings.get(CURRENTSET + 'ITEM_REGEX')), restrict_xpaths=(settings.get(CURRENTSET+'ITEM_RESTRICT_XPATHS'))), callback='parse_item'),
	)
	def parse_item(self, response):
		ruleset = self.settings.get('CURRENTSET')
		#settings = get_project_settings()
		sel = Selector(response)
		item = JinmenItem()
		#item['id'] = sel.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
		# item['title'] = sel.xpath("//h1[@class='Article_h3']/text()").extract()[0]
		item['title'] = sel.xpath(self.settings.get(ruleset+'TITLE_XPATH')).extract()[0].strip()
		item['content'] = sel.xpath(self.settings.get(ruleset+'CONTENT_XPATH')).extract()[0]
		item['url'] = response.url
		author = sel.xpath(self.settings.get(ruleset + 'AUTHOR_XPATH')).extract()
		if author:
			item['author'] = author[0]
		else:
			item['author'] = ''
		#item['author'] = sel.xpath(u"//div[@class='copyform']/span[contains(., '\u4f5c\u8005\uff1a')]/span/text()").extract()[0]
		source = sel.xpath(self.settings.get(ruleset + 'SOURCE_XPATH')).extract()
		if source:
			item['source'] = source[0]
		else:
			item['source'] = ''
		url = sel.xpath(self.settings.get(ruleset + 'IMAGES_XPATH')).extract()
		item['image_urls'] = []
		item['logo'] = ''
		if url:
			item['image_urls'] = url
			item['logo'] = url[0]
		return item
class DirectSohuSpider(CrawlSpider):
	name = 'sohuschool'
	allowed_domains = ['bschool.sohu.com']
	start_urls = []
	for i in xrange(1, 36):
		start_urls.append("http://bschool.sohu.com/xyfx/index_%d.shtml" % i)
	start_urls.append("http://bschool.sohu.com/xyfx/index.shtml")

	rules = (
		Rule(SgmlLinkExtractor(allow=('\d{8}/n\d+.shtml'), restrict_xpaths=('')), callback='parse_item'),
	)
	def parse_item(self, response):
		sel = Selector(response)
		item = JinmenItem()
		item['title'] = sel.xpath("//h1[@itemprop='headline']/text()").extract()[0].strip()
		item['content'] = sel.xpath("//div[@itemprop='articleBody']").extract()[0]
		item['url'] = response.url
		item['author'] = sel.xpath("//div[@class='news-info']//span[@class='source']/text()").extract()[0].strip()
		item['source'] = sel.xpath("//span[@id='media_span']/span[@itemprop='name']/text()").extract()[0].strip()
class DirectTheCaptialSpider(CrawlSpider):
	name = 'cap'
	allowed_domains = ['www.thecapital.com.cn']
	start_urls = []
	for i in xrange(1,74):
		start_urls.append("http://www.thecapital.com.cn/column.jsp?id=1368166768729&current=%d" % i)
	for i in xrange(1,8):
		start_urls.append("http://www.thecapital.com.cn/column.jsp?id=1368166861670&current=%d" % i)
	for i in xrange(1,42):
		start_urls.append("http://www.thecapital.com.cn/column.jsp?id=1368166870389&current=%d" % i)
	for i in xrange(1,30):
		start_urls.append("http://www.thecapital.com.cn/column.jsp?id=1368166878155&current=%d" % i)
	rules = (
		Rule(SgmlLinkExtractor(allow=('col/\d+/\d{4}/\d{2}/\d{2}/\d+.html'), restrict_xpaths=("//div[@class='wzlb']")), callback='parse_item'),
	)
	def parse_item(self, response):
		sel = Selector(response)
		item = JinmenItem()
		item['title'] = sel.xpath("//input[@name='ArticleTitle']/@value").extract()[0].strip()
		item['content'] = sel.xpath("//div[@class='wznr']//div[p]").extract()[0]
		item['url'] = response.url
		author = sel.xpath("//div[@class='news-info']//span[@class='source']/text()").extract()
		if author :
			item['author'] = author[0].strip()
		else:
			item['author'] = ''

		source = sel.xpath("//span[@id='media_span']/span[@itemprop='name']/text()").extract()
		if source:
			item['source'] = source[0]
		else:
			item['source'] = ''
		item['logo'] = ''
		item['image_urls'] = []
		return item