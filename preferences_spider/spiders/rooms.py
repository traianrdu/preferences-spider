import scrapy


class RoomsSpider(scrapy.Spider):
    name = 'rooms'
    allowed_domains = ['www.booking.com']
    start_urls = ['https://www.booking.com/']

    def parse(self, response):
        pass
