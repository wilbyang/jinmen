from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.settings import Settings
from jinmen.items import JinmenItem
from scrapy.utils.project import get_project_settings
from itertools import *


class ConfigurableSpider(CrawlSpider):
	name = 'configurable'
	def __init__(self, *a, **kw):
		settings = get_project_settings()
		CURRENTSET = settings.get('CURRENTSET')
		self.allowed_domains = settings.getlist(CURRENTSET + 'ALLOWED_DOMAINS')
		self.start_urls = settings.getlist(CURRENTSET + 'START_URLS')
		self.rules = (
			Rule(SgmlLinkExtractor(allow=(settings.get(CURRENTSET + 'LIST_REGEX')), restrict_xpaths=(settings.get(CURRENTSET+'LIST_RESTRICT_XPATHS')))),
			Rule(SgmlLinkExtractor(allow=(settings.get(CURRENTSET + 'ITEM_REGEX')), restrict_xpaths=(settings.get(CURRENTSET+'ITEM_RESTRICT_XPATHS'))), callback='parse_item'),
		)
		super(ConfigurableSpider, self).__init__(*a, **kw)


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