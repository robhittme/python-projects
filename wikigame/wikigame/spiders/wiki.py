import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikiSpider(CrawlSpider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://wikipedia.org/"]

    rules = (
            Rule(LinkExtractor(allow="wiki"), callback='parse_item')
    )
    def parse_item(self, response):
        print(response)
        pass
