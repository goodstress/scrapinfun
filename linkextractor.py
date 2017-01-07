from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LxmlLinkExtractor
from myproject.items import someItem

class someSpider(CrawlSpider):
  name = 'crawltest'
  allowed_domains = ['someurl.com']
  start_urls = ['http://www.someurl.com/']

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        item = someItem()
        item['url'] = link.url
