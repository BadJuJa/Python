from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BestArtsSpider(CrawlSpider):
    name = 'best_arts'
    allowed_domains = ['joyreactor.cc']
    start_urls = ['https://joyreactor.cc/tag/art/best']

    rules = (
        Rule(LinkExtractor(allow='tag/art/best')),
        Rule(LinkExtractor(allow=''))
    )

    def get_last_page(self, response):
        return int(response.css("div.pagination_expanded span.current::text").get())

    def parse(self, response):
        last_page = self.get_last_page(response)
        for page in range(1, last_page):
            yield scrapy.Request(f'{self.start_urls[0]}/{page}', callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        item = {'page': 1}
        yield item
